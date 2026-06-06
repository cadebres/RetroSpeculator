# RetroSpeculator

RetroSpeculator is a lightweight fullscreen game launcher designed for retro gaming setups, Raspberry Pi projects, and emulator frontends.

The application provides a simple controller-friendly interface for launching games, emulators, or any executable directly from a configurable menu.

---

## Features

* Fullscreen launcher interface
* Keyboard navigation
* Game controller support via Pygame
* Configurable game and application list
* Automatic focus highlighting
* Retro-inspired UI
* Launch external executables from a menu
* Hide launcher while a game is running
* Return to launcher automatically when a game exits
* YAML-based configuration

---

## Requirements

* Python 3.10+
* Tkinter
* Pygame
* PyYAML

Install dependencies:

```bash
pip install pygame pyyaml
```

---

## Configuration

RetroSpeculator uses a `settings.yaml` file for customization.

Example:

```yaml
background_color: black
bar_color: yellow
text_color: black

files:
  - name: Super Mario Bros
    path: C:\Games\Mario\Mario.exe

  - name: Sonic the Hedgehog
    path: C:\Games\Sonic\Sonic.exe
```

### Configuration Options

| Setting          | Description                            |
| ---------------- | -------------------------------------- |
| background_color | Main background color                  |
| bar_color        | Top and bottom bar and button color    |
| text_color       | Text color throughout the UI           |
| files            | List of launchable applications        |

---

## Controls

### Keyboard

| Key         | Action               |
| ----------- | -------------------- |
| Up Arrow    | Move selection up    |
| Down Arrow  | Move selection down  |
| Enter/Space | Launch selected item |
| Escape      | Exit fullscreen      |

### Controller

| Input           | Action               |
| --------------- | -------------------- |
| D-Pad Up        | Move selection up    |
| D-Pad Down      | Move selection down  |
| Left Stick Up   | Move selection up    |
| Left Stick Down | Move selection down  |
| A Button        | Launch selected item |

---

## Project Structure

```text
RetroSpeculatorApp/
│
├── settings.yaml
│
├── src/
│   ├──main.py
│   └──RSapp/
│      ├── app.py
│      └── gui/
│          └── main_window.py
│
└── README.md
```

### Folder Descriptions

#### gui/

Contains all user interface code, including windows, menus, and controller navigation.

---

## Running

Start the launcher:

```bash
python main.py
```

---

## Building an Executable

Using PyInstaller:

```bash
pip install pyinstaller

pyinstaller --onefile --windowed main.py
```

The executable will be generated in:

```text
dist/
```

---

## Future Plans

* Scrolling capabilites
* Search functionality
* Multiple controller profiles
* Emulator-specific launch options
* Settings window

---

## Author

Created by Caitlyn Breslow.

RetroSpeculator was created as a personal project to provide a clean, customizable launcher for retro gaming systems and emulator setups.
