import os

from layeredconfig import Defaults, Environment, INIFile, LayeredConfig

CONFIG_FILE_NAME = ".tlog"


def load_config():
    """
    Searches a standard set of locations for .uh_tools.ini, and parses the first
    match.
    """
    pwd = os.getcwd()
    home = os.path.expanduser("~")
    paths = [
        os.path.join(home, CONFIG_FILE_NAME),
        os.path.join(pwd, CONFIG_FILE_NAME),
    ]
    config_file = None
    for path in paths:
        if os.path.exists(path):
            config_file = path
            break
    return LayeredConfig(INIFile(config_file), Environment(prefix="TLOG_"))
