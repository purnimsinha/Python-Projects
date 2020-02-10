import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("path")
parser.add_argument("FN")
args = parser.parse_args()

print("Path is "+args.path)
print("Folder Name is "+args.FN)



dirName = args.path+"\\"+args.FN
print(dirName)
try:
# Create target Directory
    os.mkdir(dirName)
    print("Directory " , dirName ,  " Created ") 
except FileExistsError:
    print("Directory " , dirName ,  " already exists")
