# command syntax:
# maketag.exe [tag file] [addtags file] [newtags file] [basetag] /i[tagindent] /p[preciseSearch]
# tag file is the base file
# addtags file is the tags to add under the basetag in the tag file when its found
# newtags file is the file that will be created
# basetag is the tag to look for
# tagindent is what indent to look for with the basetag, starts at 1 (default: 1)
# precisesearch is whether to look for exactly the basetag (default: True)

import sys

true = ["True", "true"]
false = ["False", "false"]

tagindent = 1
preciseSearch = True
if len(sys.argv) == 5:
    tags = open(sys.argv[1], "r").read()
    addtags = open(sys.argv[2], "r").read()
    newtags = open(sys.argv[3], "w")
    basetag = sys.argv[4]
elif len(sys.argv) >= 6:
    tags = open(sys.argv[1], "r").read()
    addtags = open(sys.argv[2], "r").read()
    newtags = open(sys.argv[3], "w")
    basetag = sys.argv[4]
    for i in range (5, len(sys.argv)):
        command = sys.argv[i][:2]
        arg = sys.argv[i][2:]
        print(str(command))
        print(str(arg))
        if command == "/i":
            tagindent = int(arg)
        if command == "/p":
            if arg in true:
                preciseSearch = True
            elif arg in false:
                preciseSearch = False
            else:
                print("WARNING: neither true or false supplied for preciseSearch, defaulting to True")
else:
    raise SyntaxError("Incorrect syntax, use \"maketag.exe tags.csv addtags.csv newtags.csv basetag /i[tagindent] /p[preciseSearch]\"")
print(tagindent)
print(preciseSearch)

tags = open(sys.argv[1], "r").read()
addtags = open(sys.argv[2], "r").read()
newtags = open(sys.argv[3], "w")
basetag = sys.argv[4]

starttags = tags.split("\n")
endouttags = tags.split("\n")
startaddtags = addtags.split("\n")
startaddtags = list(filter(None, startaddtags))
print(startaddtags)

foundtag = False
indentoffset = 1

for i in range(len(starttags)):
    foundclonetag = False
    starttags[i] = starttags[i].split(",")
    try:
        if preciseSearch:
            if starttags[i][tagindent - 1] == basetag:
                foundclonetag = True
        else:
            if basetag in starttags[i][tagindent - 1]:
                foundclonetag = True
        if foundclonetag:
            print("Found a tag on row " + str(i + indentoffset))
            foundtag = True
            for j in range(len(startaddtags)):
                indentoffset += 1
                print("Added tag on row" + str(i + indentoffset))
                toreplace = starttags[i][tagindent - 1]
                replacewith = startaddtags[j]
                within = tags.split("\n")[i]
                replaced = within.replace(toreplace, replacewith)
                endouttags.insert(i + indentoffset - 1, replaced)
                
    except IndexError:
        pass

if not foundtag:
    print("WARNING: no changes to output file, specified tag not found")
else:
    print("successfully added tags")

newtags.write("\n".join(endouttags))
