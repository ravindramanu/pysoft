------------
FILERENAMER:
------------
File renamer is a command line tool that facilitates bulk renaming of files.
This is chore to do at some workplaces and an automation tool for this specific
purpose would be handy. You might need to be admin or need sudo. This only works
in the current directory.

Usage:
------
filerenamer [-a] [-f=specificfile] [-t=texttosubstitute] [-r=substitutetext] [-h]

Options:
--------
[-a]                          : Rename all files
[-f=specificfile]             : Find a specific file to rename
[-t=texttosubstitute]         : This is the text that is to be replaced from the
                                name of selected file(s)
[-r=substitutetext]           : This is the text that will replace the text that
                                is to be substituted in the name of the
                                selected file(s)
[-h]                          : This help section

Example:
--------

filerenamer -a -t=cat -r=jaguar
filerenamer -f=filenamedcat.txt -t=cat -r=jaguar
filerenamer -h

To use, copy the filerenamer.py python script to where you need to use it and either call the script directly or chmod +x it to make it an executable.
