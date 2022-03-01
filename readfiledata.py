myfile = open("websiteData.txt", encoding="utf-8")
data = ""
lines = myfile.readlines()
for line in lines:
    data = data + line.strip();