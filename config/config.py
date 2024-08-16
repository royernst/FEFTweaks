import os
import json

class Config:
    def __init__(self, config_path="config/settings.json"):
        self.config_path = config_path
        self.settings = self.load_settings()

    def load_settings(self):
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, 'r') as file:
                    settings = json.load(file)
                    # Expand the user path for the default_linux_path
                    settings["default_linux_path"] = os.path.expanduser(settings["default_linux_path"])
                    return settings
            else:
                return {
                    "directory": None,
                    "window_size": {
                        "width_percentage": 0.5,
                        "height_percentage": 0.6
                    },
                    "default_linux_path": os.path.expanduser(
                        "~/.local/share/citra-emu/sdmc/Nintendo 3DS/00000000000000000000000000000000/00000000000000000000000000000000/title/00040000/00179800/data/00000001"
                    )
                }
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading settings: {e}")
            return {
                "directory": None,
                "window_size": {
                    "width_percentage": 0.5,
                    "height_percentage": 0.6
                },
                "default_linux_path": os.path.expanduser(
                    "~/.local/share/citra-emu/sdmc/Nintendo 3DS/00000000000000000000000000000000/00000000000000000000000000000000/title/00040000/00179800/data/00000001"
                )
            }

    def save_settings(self):
        try:
            # Save the settings, but ensure paths are saved as user-relative (using ~)
            self.settings["default_linux_path"] = os.path.relpath(self.settings["default_linux_path"], os.path.expanduser("~"))
            with open(self.config_path, 'w') as file:
                json.dump(self.settings, file, indent=4)
        except IOError as e:
            print(f"Error saving settings: {e}")

    def get_directory(self):
        try:
            directory = self.settings.get("directory")
            if directory is None and os.name == 'posix':
                default_linux_path = self.settings["default_linux_path"]
                if os.path.exists(default_linux_path):
                    directory = default_linux_path
                    self.set_directory(directory)
            return directory
        except Exception as e:
            print(f"Error getting directory: {e}")
            return None

    def set_directory(self, directory):
        try:
            self.settings["directory"] = directory
            self.save_settings()
        except Exception as e:
            print(f"Error setting directory: {e}")

    def get_window_size(self):
        try:
            return self.settings.get("window_size", {"width_percentage": 0.5, "height_percentage": 0.6})
        except Exception as e:
            print(f"Error getting window size: {e}")
            return {"width_percentage": 0.5, "height_percentage": 0.6}

    def set_window_size(self, width_percentage, height_percentage):
        try:
            self.settings["window_size"] = {
                "width_percentage": width_percentage,
                "height_percentage": height_percentage
            }
            self.save_settings()
        except Exception as e:
            print(f"Error setting window size: {e}")
