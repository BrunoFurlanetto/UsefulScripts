import subprocess
import psycopg2
import os
from .logger import log_info, log_success


def db_exists(dbname, config):
    """Check if a PostgreSQL database already exists"""
    conn = psycopg2.connect(
        dbname="postgres",
        user=config["DB_USER"],
        password=config["DB_PASS"],
        host=config["DB_HOST"],
        port=config["DB_PORT"]
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM pg_database WHERE datname = %s;", (dbname,))
    exists = cur.fetchone() is not None
    cur.close()
    conn.close()
    return exists


def run_psql(cmd, config):
    """Run SQL command using psql"""
    subprocess.run(
        [
            "psql",
            "-U", config["DB_USER"],
            "-h", config["DB_HOST"],
            "-p", str(config["DB_PORT"]),
            "-c", cmd,
        ],
        check=True,
        env={**os.environ, "PGPASSWORD": config["DB_PASS"]}
    )


def create_db_from_main(branch_db, config):
    """Clone the main database into a new branch database"""
    main_db = f"{config['DB_PREFIX']}{config['MAIN_BRANCH']}"
    dump_file = f"/tmp/{main_db}.dump"

    log_info(f"📦 Creating database '{branch_db}' from '{main_db}'...")

    # Dump main DB
    subprocess.run(
        [
            "pg_dump",
            "-U", config["DB_USER"],
            "-h", config["DB_HOST"],
            "-p", str(config["DB_PORT"]),
            "-Fc",
            "-f", dump_file,
            main_db,
        ],
        check=True,
        env={**os.environ, "PGPASSWORD": config["DB_PASS"]}
    )

    # Create new DB
    run_psql(f'CREATE DATABASE "{branch_db}" OWNER "{config["DB_USER"]}";', config)

    # Restore dump into new DB
    subprocess.run(
        [
            "pg_restore",
            "-U", config["DB_USER"],
            "-h", config["DB_HOST"],
            "-p", str(config["DB_PORT"]),
            "-d", branch_db,
            dump_file,
        ],
        check=True,
        env={**os.environ, "PGPASSWORD": config["DB_PASS"]}
    )

    log_success(f"Database '{branch_db}' created and populated successfully!")
