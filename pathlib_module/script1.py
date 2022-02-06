
import pathlib
import os
import time

print(f"pathlib.Path(__file__) = {pathlib.Path(__file__)}")
print(f"pathlib.Path(__file__).parent = {pathlib.Path(__file__).parent}")
print(f"pathlib.Path(__file__).name = {pathlib.Path(__file__).name}")
pathlib_path = pathlib.Path(__file__)
print(f"pathlib.Patn(__file__).parts = {pathlib_path.parts}")
print(f"pathlib.Patn(__file__).suffics = {pathlib_path.suffix}") # on linux may be suffics suffics
print(f"pathlib.Patn(__file__).exists = {pathlib_path.exists()}")
print(f"pathlib.Patn(__file__).is_file = {pathlib_path.is_file()}")
print(f"pathlib.Patn(__file__).home = {pathlib_path.home()}")

# Directory list

for chld in pathlib_path.parent.iterdir(): # iterdir() - получить список дочерних элементов
    print(f"name: {chld.name}, size = {chld.stat().st_size} bytes")
    pass

# Create directory
# new_dir_path = pathlib_path.parent.joinpath("new_dir2").mkdir()
# new 1
# new_dir_path.mkdir(parents=True, exist_ok=True)
new_dir_path1 = pathlib_path.parent.joinpath("new_dir1")
if not new_dir_path1.exists():
    new_dir_path1.mkdir()
new_dir_path2 = pathlib_path.parent.joinpath("new_dir2")
if not new_dir_path2.exists():
    new_dir_path2.mkdir()


# create file 
f1_path = new_dir_path1.joinpath("new_file1.py")
with open(f1_path, "w") as f1:
    f1.write("print(" + "\"Hello, world!\"" + ")")
    print(f"f1_path = {f1_path}")




time.sleep(5)
os.system(f"python3 {f1_path}" )
f1_new_path = f1_path.parent.joinpath("new_file1.scv")
f1_path.rename(f1_new_path) # rename file

time.sleep(5)
for next_f1 in pathlib_path.parent.iterdir():
    print(f"stat = {next_f1.stat().st_size}")
    pass
print(pathlib_path.stat())

# os.system(f"python3 {f1_path}" )
time.sleep(15)
f1_new_path.unlink() # delete file

time.sleep(5)
new_dir_path1.rmdir()
new_dir_path2.rmdir()
