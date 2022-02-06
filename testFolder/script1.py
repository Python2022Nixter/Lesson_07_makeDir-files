# path
import os

print(f"__file__: {__file__}") # os_path_module/script1.py
# my_path = __file__.split("/")
my_path = __file__.split(os.path.sep)
print(f"os.path.curdir =  {os.path.curdir}")
print(f"os.getcwd() =  {os.getcwd()}")
print(f"ord(os.linesep) =  {ord(os.linesep)}")
print(f"os.path.abspath =  {os.path.abspath}")
print(f"os.path.isfile() =  {os.path.isfile(os.path.abspath(__file__))}")
print(f"os.path.isdir() =  {os.path.isdir(os.path.abspath(__file__))}")
print(f"os.path.dirname(__file__) =  {os.path.dirname(__file__)}")

f1 = open(os.path.join(os.getcwd(), "text_file1.txt"), "w")
f1.close()
f2 = open(os.path.join(os.path.dirname(__file__), "text_file1_2.txt"), "w")
f2.close()
