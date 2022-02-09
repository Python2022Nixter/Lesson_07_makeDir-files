import pathlib
import random
from time import sleep
import os

# loop files in current directory
# remove temporary files


t = random.randrange(1, 5)
names = []
for i in range(t):
    names.append(f"file{i}.txt")
for i in range(t*5):
    names.append(f"file{i}.tmp")

# 1. create path to current parent pathlib_path.parent
pathlib_path = pathlib.Path(__file__)
for i in names:
    pathlib.Path.joinpath(pathlib_path.parent, i).touch()

# 2. pathlib_path.parent.iterdir()
sleep(5)
for chld in pathlib_path.parent.iterdir():
    if chld.name.endswith(".tmp"):
        chld.unlink()

        pass
    pass
print("all files .tmp deleted")
sleep(3)

t = 5
for i in range(t):
    os.system("clear")

    print(f"after {t} seconds all .txt files will be deleted \r", end="")

    if t == 1:
        for chld in pathlib_path.parent.iterdir():
            if chld.suffix == ".txt":
                chld.unlink()
                pass
            pass
        os.system("clear")
        print("all files .txt deleted\n")
        break

    t -= 1
    sleep(1)
    pass


# 3. loop ,

# 4. get file suffix == "tmp", -> unlink(), ~1
