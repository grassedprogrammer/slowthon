import shelve
import platform
windows = False
OS = platform.system()

def do_nothing():
    return None
if OS == "Windows":
    windows = True
class database:
    def __init__(self, name):
        self.name = name
        with shelve.open(str(name)) as db:
            do_nothing()
    #methods
    class table:
        def __init__(self, name):
            self.name = name
if __name__ == "__main__":
    print(OS)
    if windows == True:
        print("windows")