import sys

if len(sys.argv) == 5:
    tags = open(sys.argv[1], "r").read()
    addtags = open(sys.argv[2], "r").read()
    newtags = open(sys.argv[3], "w")
    basetag = sys.argv[4]
else:
    raise SyntaxError("Incorrect syntax, use \"maketag.exe tags.csv addtags.csv newtags.csv basetag.csv\"")

tags = open(sys.argv[1], "r").read()
addtags = open(sys.argv[2], "r").read()
newtags = open(sys.argv[3], "w")
basetag = sys.argv[4]

starttags = tags.split("\n")
endouttags = tags.split("\n")
startaddtags = addtags.split("\n")

for i in range(len(starttags)):
    starttags[i] = starttags[i].split(",")
    if starttags[i][0] == basetag:
        concatlist = starttags[i]
        del concatlist[0]
        for j in range(len(startaddtags)):
            startaddtags[j].split(",")
            endouttags.insert(i + j + 1, startaddtags[j] + "," + ",".join(concatlist))

newtags.write("\n".join(endouttags))

print(endouttags)

a = input("press enter to continue")
