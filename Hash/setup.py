# -*- coding: utf8 -*-


import sys
from cx_Freeze import Executable, setup

base = None
if sys.platform == "win32":
    base = "Win32GUI"

options = {
    'build_exe': {
        'include_msvcr': True,
        "packages": ["sqlite3", "sys", "random", "time", "PyQt5"],
        "include_files": ["data", "icopath.txt"],

    }
}


setup(name="Hash",
      version="0.0.1",
      description="HASH!",
      options=options,
      executables=[Executable("main.py", targetName="Hash!.exe", icon="logo.ico", base=base)])
