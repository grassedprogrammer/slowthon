import Termine_tools
import platform
import sys
import math
import random
import time
import datetime

version = "indev: 0.1"
import Termine_tools
import terbaser
from terbaser import Terbaser
import platform
import sys
import math
import random
import time
import datetime

version = "indev: 0.1"
OS = platform.system()
windows = False
#checking if its the module is safe to import
if OS.lower() == "windows":
    windows = True
    import os

print(f"  ---termine {version}---")
print(f"  ---OS: {OS}---")
print(f"")

def clearscreen():
    for i in range(1, 1000):print("")

class bitmap:
    def __init__(self,matrixmap,dictionary):
        self.map = matrixmap
        self.dictionary = dictionary

if __name__ == "__main__":
    print(OS)
    test = mainscene()
    test2 = mainscene.scene()