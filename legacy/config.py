import os
import xml.etree.ElementTree as ET

class Config:
    _config_path = os.path.join(os.getcwd(), "Config.xml")

    @staticmethod
    def get_startup_path():
        root = Config._get_config_root()
        settings = root.find("misc")
        return settings.get("startupPath")

    @staticmethod
    def set_startup_path(value):
        root = Config._get_config_root()
        settings = root.find("misc")
        settings.set("startupPath", value)
        Config._set_config_root(root)

    @staticmethod
    def get_unit_path():
        root = Config._get_config_root()
        settings = root.find("misc")
        return settings.get("unitPath")

    @staticmethod
    def set_unit_path(value):
        root = Config._get_config_root()
        settings = root.find("misc")
        settings.set("unitPath", value)
        Config._set_config_root(root)

    @staticmethod
    def in_design_mode():
        # Python equivalent might check for certain environment variables
        # or simply return False as Python generally doesn't have a "design mode" concept.
        return False

    @staticmethod
    def _get_config_root():
        try:
            tree = ET.parse(Config._config_path)
            return tree.getroot()
        except FileNotFoundError:
            # Create a default XML structure if the config file doesn't exist
            root = ET.Element("root")
            misc = ET.SubElement(root, "misc", startupPath="", unitPath="")
            tree = ET.ElementTree(root)
            Config._set_config_root(root)
            return root

    @staticmethod
    def _set_config_root(root):
        tree = ET.ElementTree(root)
        tree.write(Config._config_path, encoding="utf-8", xml_declaration=True)
