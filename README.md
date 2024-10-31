# MARIO AND LUIGI'S PIZZERIA DOCUMENTATION

## Activating the virtual environment

**Position yourself on mario_luigi path**

```zsh
source venv/bin/activate
```

```bash

```

## Deactivating the virtual environment

```zsh
deactivate
```

## Dependancies

- **Arduino**
  **_Download arduino cli or arduino ide_**

- **Python**

macOS

```zsh
brew install python
```

- **Pip**

macOS

```zsh
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
```

- **Flask**

macOS

```zsh
python3 -m pip install flask
```

- **pySerial**

macOS

```zsh
python3 -m pip install pyserial
```

## File Structure

MARIO_LUIGI
|---.venv
|---Arduino
|   |---oven
|   |   |---oven.ino
|---Python
|   |---data
|   |   |---accounts.json
|   |---services
|   |   |---json_ops.py
|   |---static
|   |   |---colors
|   |   |   |---colors.css
|   |   |---icons
|   |   |   |---temp.py
|   |   |---images
|   |   |   |---temp.py
|   |   |---styles
|   |   |   |---style.css
|   |---templates
|   |   |---login.html
|   |   |---register.html
|   |---__init__.py
|---.gitignore
|---README.md
|---requirements.txt