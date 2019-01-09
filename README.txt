USE

maketag.exe (tag file) (addtags file) (newtags file) (basetag) /i[tagindent] /p[precisesearch]

(required) /_[optional]

tag file is the base file
addtags file is the tags to add under the basetag in the tag file when its found
newtags file is the file that will be created
basetag is the tag to look for
tagindent is what indent to look for with the basetag, starts at 1  (default: 1)
precisesearch is whether to look for exactly the basetag (default: True)



to build executable from maketag.py run buildexe.bat

requires cx_freeze

ORIGINAL SPECIFICATIONS

Hi Tom
I want to be able to use a command like the following
maketag tags.csv addtags.csv newtags.csv "basetag"



where:
maketag = name of the program/utility
tags.csv = the filename of the incoming file to read (allow for at least 200 comma separated variables per line). The file may be thousands of lines long.
newtags.csv = the filename of a list of tags (one column wide only) to add newlines in the tags.csv file
newtags.csv = the filename of the output .csv file
"basetag" = the name of the tag (first column) in tags.csv that we want to replicate with the tag names replaced by all the tags in the addtags.csv file
if the program is run with no inputs or the wrong number of parameters print to screen help info which says how it should be used and what it will do.

EXAMPLE

inputs:

File = tags.csv
xtag,4,2,3,4,5,6,7,UN,A,5,4,3,2,1
ztag,7,2,8,4,5,6,7,UN,A,5,4,3,2,1 
atag,1,2,9,4,5,6,7,UN,A,5,4,3,2,1
mytag,6,2,3,4,5,6,7,UN,A,5,4,3,2,1
qtag,1,2,3,2,5,6,7,UN,A,5,4,3,2,1
wtag,1,2,4,9,5,6,7,UN,A,5,4,3,2,1
etag,8,2,3,4,5,6,7,UN,A,5,4,3,2,1
rtag,9,2,3,4,5,6,7,UN,A,5,4,3,2,1 

(in reality the values for each line will be different)


File = addtags.csv
newtag1
newtag2
newtag3
newtag4

"basetag" = "mytag"

output:

file = newtags.csv
xtag,4,2,3,4,5,6,7,UN,A,5,4,3,2,1
ztag,7,2,8,4,5,6,7,UN,A,5,4,3,2,1 
atag,1,2,9,4,5,6,7,UN,A,5,4,3,2,1
mytag,6,2,3,4,5,6,7,UN,A,5,4,3,2,1
newtag1,6,2,3,4,5,6,7,UN,A,5,4,3,2,1
newtag2,6,2,3,4,5,6,7,UN,A,5,4,3,2,1
newtag3,6,2,3,4,5,6,7,UN,A,5,4,3,2,1
newtag4,6,2,3,4,5,6,7,UN,A,5,4,3,2,1
qtag,1,2,3,2,5,6,7,UN,A,5,4,3,2,1
wtag,1,2,4,9,5,6,7,UN,A,5,4,3,2,1
etag,8,2,3,4,5,6,7,UN,A,5,4,3,2,1
rtag,9,2,3,4,5,6,7,UN,A,5,4,3,2,1

UPDATED SPECIFICATIONS

add a way to check any indent (still only chaging the first column in the duplicated rows)
add a loose search which just searches if the tag is in a row