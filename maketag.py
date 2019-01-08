# command syntax:
# maketag.exe [tag file] [addtags file] [newtags file] [basetag] [tagindent]
# tag file is the base file
# addtags file is the tags to add under the basetag in the tag file when its found
# newtags file is the file that will be created
# basetag is the tag to look for
# tagindent is what indent to look for with the basetag (starts at 1)

import sys

if len(sys.argv) == 5:
    tags = open(sys.argv[1], "r").read()
    addtags = open(sys.argv[2], "r").read()
    newtags = open(sys.argv[3], "w")
    basetag = sys.argv[4]
    tagindent = 1
elif len(sys.argv) == 6:
    tags = open(sys.argv[1], "r").read()
    addtags = open(sys.argv[2], "r").read()
    newtags = open(sys.argv[3], "w")
    basetag = sys.argv[4]
    tagindent = int(sys.argv[5])
else:
    raise SyntaxError("Incorrect syntax, use \"maketag.exe tags.csv addtags.csv newtags.csv basetag [tagindent]\"")

tags = open(sys.argv[1], "r").read()
addtags = open(sys.argv[2], "r").read()
newtags = open(sys.argv[3], "w")
basetag = sys.argv[4]

starttags = tags.split("\n")
endouttags = tags.split("\n")
startaddtags = addtags.split("\n")

foundtag = False

for i in range(len(starttags)):
    starttags[i] = starttags[i].split(",")
    try:
        if starttags[i][tagindent - 1] == basetag:
            foundtag = True
            concatlist = starttags[i]
            del concatlist[0]
            for j in range(len(startaddtags)):
                startaddtags[j].split(",")
                endouttags.insert(i + j + 1, startaddtags[j] + "," + ",".join(concatlist))
    except IndexError:
        pass

if not foundtag:
    print("WARNING: no changes to output file, specified tag not found")
else:
    print("successfully added tags")

newtags.write("\n".join(endouttags))
