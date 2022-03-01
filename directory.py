from pathlib import Path

# absolute path
#c:\program files\microsoft
# relative path

path = Path("ecommerce1")
# print(path.mkdir())
#print(path.rmdir())
path = Path()
for file in path.glob("*.py"):
    print(file)