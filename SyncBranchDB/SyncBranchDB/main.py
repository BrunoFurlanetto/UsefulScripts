"""
main.py — Main CLI entry point for SyncBranchDB

Automatically manages PostgreSQL databases by Git branch.
When switching branches, it creates a new database (if missing) cloned from the main branch database.

Can be executed manually or automatically through a Git hook (post-checkout).
"""

import sys
from SyncBranchDB.SyncBranchDB.branch_db_manager.env_utils import load_env
from SyncBranchDB.SyncBranchDB.branch_db_manager.git_utils import get_current_branch
from SyncBranchDB.SyncBranchDB.branch_db_manager.db_manager import db_exists, create_db_from_main
from SyncBranchDB.SyncBranchDB.branch_db_manager.logger import log_info, log_warn, log_success, log_error


def main():
    try:
        # 1️⃣ Load environment variables
        config = load_env()

        # 2️⃣ Detect current Git branch
        branch = get_current_branch()
        log_info(f"Detected branch: {branch}")

        # 3️⃣ Skip if on main branch
        if branch == config["MAIN_BRANCH"]:
            log_info("Main branch detected — no database creation needed.")
            sys.exit(0)

        # 4️⃣ Build branch database name
        branch_db = f"{config['DB_PREFIX']}{branch}"
        log_info(f"Target database: {branch_db}")

        # 5️⃣ Check if database already exists
        if db_exists(branch_db, config):
            log_warn(f"Database '{branch_db}' already exists. Nothing to do.")
            sys.exit(0)

        # 6️⃣ Create new branch database from main
        create_db_from_main(branch_db, config)
        log_success(
            f"Database '{branch_db}' successfully created from '{config['DB_PREFIX']}{config['MAIN_BRANCH']}'."
        )

    except KeyboardInterrupt:
        log_warn("Execution cancelled by user.")
        sys.exit(1)
    except Exception as e:
        log_error(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
