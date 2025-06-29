# PyQt6_app_template

[![Github Actions Workflow](https://github.com/DiogoCarapito/PyQt6_app_template/actions/workflows/main.yaml/badge.svg)](https://github.com/DiogoCarapito/PyQt6_app_template/actions/workflows/main.yaml)

PyQt6 app template

Python version: 3.12

## cheat sheet

### setup

move all files and folders to the current project folder

```bash
mv python_project_template/{*,.*} . && rm -r python_project_template/
```

### venv

create venv

```bash
python3.12 -m venv .venv
```

activate venv

```bash
source .venv/bin/activate
```

### Docker

build docker image

```bash
docker build -t main:latest .
```

### Compile with pyinstaller

To compile the application into a standalone executable, run the following command

```bash
pyinstaller --onefile --windowed app.py
```
