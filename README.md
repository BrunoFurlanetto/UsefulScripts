# Dev/Ops Utility Scripts

Reusable dev/ops scripts for database automation, Git productivity, data tasks, and project maintenance — plug-and-play, cross-platform, minimal dependencies.

This repository gathers **utility scripts** to speed up development and operations workflows. Each script lives in **its own folder** with a README and optional dependencies, making it easy to understand, version, and reuse.

---

## Repository Structure

```
.
├── README.md
├── scripts/
│   ├── <script-1>/
│   │   ├── README.md
│   │   ├── main.py
│   │   ├── requirements.txt      # optional, only if the script needs deps
│   │   ├── .env.example          # expected environment variables
│   │   ├── helpers/              # auxiliary modules (optional)
│   └── <script-2>/
│       ├── README.md
│       ├── main.cs
│       └── ...
```

**Conventions**

* One folder per script under `scripts/<script-name>`.
* Indicate in README.md or entrypoint script
* Local `README.md` explains purpose, flags, examples, and env vars.
* `.env.example` lists environment variables; do **not** commit real `.env`.
* Add file with required external dependencies.
* Prefer minimal dependencies whenever possible.

---

## Requirements

Each script folder must contain in the local `README.md` the requirements necessary for using the script in question.

---

## Environment

Copy `.env.example` to `.env` and adjust values.

| Var    | Default | Description                 |
| ------ | ------- | --------------------------- |
| EX_VAR | (empty) | What this variable controls |

## Notes

* requirements, performance, edge cases…

````

**`scripts/<new-script>/.env.example`**
```env
# environment variables expected by this script
EX_VAR=example
````

**`scripts/<new-script>/requirements.txt`** (optional)

```
# add libraries here if needed
# python-dotenv==1.*
```

---

## Best Practices

* **Friendly CLI**: always implement `--help` with `argparse` (or similar).
* **No secrets in code**: use env vars and `.env.example`.
* **Portability**: prefer Python/standard CLI; document OS-specific notes.
* **Idempotence**: scripts should be safe to run multiple times.
* **Clear logs**: print what the script is doing; use proper exit codes.

---

## Troubleshooting

* **Commands not found**: ensure `psql`, `pg_dump`, etc., are on PATH.
* **Postgres permissions/owner**: adjust `--owner` or create the role first (`createuser`).
* **Name conflicts**: use flags like `--prefix` or `--force` where applicable.
* **Windows environments**: run via PowerShell/WSL, or keep scripts pure Python.

---

## Contributing

PRs and issues are welcome! Please keep scripts:

* Small and focused
* Documented (README + `--help`)
* Without unnecessary dependencies

Suggested tooling:

* `black`/`ruff` for formatting/linting (optional, via `pyproject.toml`)
* `pytest` for quick tests under `scripts/<tool>/tests/` (optional)

---

## License

MIT (unless otherwise specified in the script header).
