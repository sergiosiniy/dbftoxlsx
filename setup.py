import sys, os
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"includes": ["chardet", "dbfread","xlsxwriter"],
                     "include_files":['tcl86t.dll','tcl86tg.dll','tk86t.dll',\
                                      'tk86tg.dll']}

os.environ['TCL_LIBRARY'] = "D:\\Python\\Lang\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "D:\\Python\\Lang\\tcl\\tk8.6"

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "autoupdater_farmaco",
    version = "0.1",
    description = "Farmaco Autoupdater",
    options = {"build_exe": build_exe_options},
    executables = [Executable("dbftoxls.py", base = base)])
