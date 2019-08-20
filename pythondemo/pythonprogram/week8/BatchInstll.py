# coding: utf-8

import os
libs = {"numpt", "matplotlib", "pillow", "sklearn", "requests", "jieba",
        "beautifulsoup4", "wheel", "networkx", "sympy", "pyinstaller",
        "django", "flask", "werobot", "myqt5",
        "pandas", "pyogengl", "pypdf2", "docopt", "pygame"}
try:
    for lib in libs:
        os.system("pip install " + lib)
    print("Successful")
except:
    print("Failed Somehow")
