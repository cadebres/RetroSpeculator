from RSapp.gui.main_window import MainWindow
import yaml
from pathlib import Path

def run():
    config_data = startup()
    app = MainWindow(config_data)
    app.mainloop()

def startup():
    config_path = Path(__file__).parent / "../../settings.yaml"

    try:
        with config_path.open() as f:
            config_data = yaml.load(f, Loader=yaml.FullLoader)
            return config_data
    except FileNotFoundError:
        with open(config_path, "w") as file:
            text = """background_color: black
bar_color: gray8
text_color: gray40
folder_mode: false
folder: ""
# format as follows:
# files:
#   - name: "File1"
#     path: "C:\\Other\\file1.exe"
#   - name: "File2"
#     path: "C:\\Other\\file2.exe"
files:
  - name: ""
    path: """""
            file.write(text)
        with config_path.open() as f:
            config_data = yaml.load(f, Loader=yaml.FullLoader)
            return config_data