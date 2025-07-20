# PyQt app template

[![Github Actions Workflow](https://github.com/DiogoCarapito/PyQt6_app_template/actions/workflows/main.yaml/badge.svg)](https://github.com/DiogoCarapito/PyQt6_app_template/actions/workflows/main.yaml)

PyQt6 simple application template.

Python version: 3.12

## cheat sheet

### venv

create venv

```bash
python3.12 -m venv .venv
```

activate venv

```bash
source .venv/bin/activate
```

### build

build the application

```bash
pyinstaller --name App --onefile --windowed --icon=assets/logo.ico app.py
```
