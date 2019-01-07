USE
go to the directory with py file/executable
type in "py maketag.py/exe tags.csv addtags.csv newtags.csv mytag"
where tags.csv and addtags.csv will be the input files and newtags.csv will be the output files

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