Perfect 🔥 — here’s a complete **README.md** written in clear English and formatted for GitHub.
It explains the purpose of your project, folder structure, environment setup, and Git hook configuration step by step.

---


# 🧩 SyncBranchDB

**SyncBranchDB** is a lightweight automation tool designed to keep your development branches and databases isolated and in sync.  
Each Git branch automatically gets its own cloned database based on the main branch, allowing developers to work independently without affecting shared environments.

---

## 🚀 Key Features

- 🔀 Automatically clones the main database when switching branches  
- 🧱 Creates new databases dynamically (`<prefix>-<branch>`)  
- ⚙️ Configurable via `.env`  
- 🪝 Fully integrated with Git **post-checkout hooks**  
- 🧩 Works on Windows, macOS, and Linux (including WSL)  
- 🧠 Supports PostgreSQL out of the box  

---

## 🗂️ Project Structure

```text
SyncBranchDB/
├── .githooks/                # Git hooks directory (if using custom hooks)
│   └── post-checkout         # Hook that triggers after branch switch
│
├── branch_db_manager/        # Core logic for DB and environment management
│   ├── **init**.py
│   ├── db_manager.py         # Database cloning and management
│   ├── env_utils.py          # .env loading helpers
│   ├── git_utils.py          # Branch detection and git helpers
│   └── logger.py             # Logging with colored output
│
├── scripts/                  # Auxiliary scripts (optional)
│   └── sync_branch_db.py     # Entry script for manual database sync
│
├── .env                      # Environment configuration file
├── main.py                   # Main entry point (used by Git hook or manual run)
└── README.md                 # Project documentation
```

---

## ⚙️ Environment Configuration

Create a `.env` file in the root directory with your PostgreSQL credentials and project info:

```dotenv
DB_USER=dev
DB_PASS=dev123
DB_HOST=localhost
DB_PORT=5433
DB_PREFIX=teste
MAIN_BRANCH=main
````

### Optional values

```dotenv
DB_BASE=postgres   # (default) base database used for CREATE DATABASE commands
```

---

## 🧰 Setting Up the Virtual Environment

```bash
# 1. Create a virtual environment
python -m venv .venv

# 2. Activate it
# Windows
.\.venv\Scripts\activate
# Linux / macOS / WSL
source .venv/bin/activate

# 3. Install dependencies
pip install python-dotenv psycopg2
```

---

## 🪝 Git Hook Configuration

The **post-checkout** hook runs automatically every time you switch branches
and ensures that the corresponding branch database is created or updated.

### Option 1 — Use the default Git hooks folder

1. Copy your hook script to:

   ```
   .git/hooks/post-checkout
   ```
2. Make it executable:

   ```bash
   chmod +x .git/hooks/post-checkout
   ```

The hook will automatically trigger when running:

```bash
git checkout <branch>
```

### Option 2 — Use a versioned `.githooks` folder

If you prefer to version your hooks:

1. Move the hook into `.githooks/post-checkout`
2. Configure Git to use that folder:

   ```bash
   git config core.hooksPath .githooks
   ```
3. Make sure it’s executable:

   ```bash
   chmod +x .githooks/post-checkout
   ```

---

## 🧩 How It Works

1. When you checkout a new branch:

   ```bash
   git checkout feature/add-login
   ```
2. The `post-checkout` hook triggers:

   * Activates your Python virtualenv
   * Runs `main.py`
   * Detects the current branch
   * Clones the main DB (`teste-main`) into a new one (`teste-feature-add-login`)
3. The Django (or any app) `local_settings.py` picks the right DB based on branch name.

---

## 🧠 How Branch Databases Are Named

All databases follow the pattern:

```
<DB_PREFIX>-<branch_name>
```

Example:

| Branch               | Database                   |
| -------------------- | -------------------------- |
| `main`               | `teste-main`               |
| `feature/user-login` | `teste-feature-user-login` |
| `fix/typo`           | `teste-fix-typo`           |

---

## 🧱 Manual Execution

You can run the sync manually without changing branches:

```bash
python main.py
```

This will:

1. Detect your current branch
2. Clone the main database if necessary
3. Print progress logs

---

## 🧪 Troubleshooting

| Problem                            | Cause                      | Solution                                                    |
| ---------------------------------- | -------------------------- | ----------------------------------------------------------- |
| `pg_dump: command not found`       | PostgreSQL not in PATH     | Add `C:\Program Files\PostgreSQL\<version>\bin` to PATH     |
| `database "<user>" does not exist` | Default DB missing         | Set `DB_BASE=postgres` in `.env`                            |
| `UnicodeEncodeError` on Windows    | Console not UTF-8          | Add `sys.stdout.reconfigure(encoding='utf-8')` to `main.py` |
| `/tmp/*.dump` not found            | Using Unix path on Windows | Use `tempfile.gettempdir()` instead                         |

---

## 💡 Logging Output Example

```
🚀 Git post-checkout hook triggered — syncing branch database...
📦 Creating database 'teste-feature-login' from 'teste-main'...
🧭 Using pg_dump at: C:\Program Files\PostgreSQL\17\bin\pg_dump.exe
✅ Database 'teste-feature-login' created and populated successfully!
```

---

## 📜 License

This project is under the **MIT License**.
Feel free to use, modify, and integrate it into your own workflow.

---

## 🧑‍💻 Author

**Bruno Furlanetto**
Developer | Automation Enthusiast


---

Would you like me to adjust the README to include **colored output examples** (using ANSI codes for terminal logs) or keep it minimal like this version?
