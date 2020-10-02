#!/usr/bin/python3
# Author: Ravindra, Manu
# SOFTWARE IS UNLICENSED AND FREE FOR ALL
# THE ONUS OF RESULTING CONSEQUENCES OF USING THIS TOOL IS ON THE USER AND NOT THE AUTHOR IN ANY WAY POSSIBLE. PLEASE USE YOUR BEST JUDGEMENT.

import sys # Import the system module to get arguments from the command line window
import os  # Import the os module to do some file path work

# Let us make some useful variables for the program
noOfArguments=len(sys.argv)                    # No of arguments entered
optionlist=['-h', '-a', '-f=', '-t=', '-r=']   # List of allowed options

# Write down the help section. Allows us to get a feel of how the tool would look
helptext='''
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

'''

# Define a section to perform comand based on options parsed
def filerenamer(help='No',all='No', file='', replace='', replacewith=''):
    if (help=='Yes'):
        print('\nAn option entered was -h, help overrides all options. Here is the help text.')
        print(helptext)

    elif ((all=='Yes') and (file!='')):
        # Invalid option combination
        print('\nInvalid combination of options. -a and -f cannot be used together.\nUse filerenamer -h to check the help section.')

    elif ((all=='Yes') and (file=='') and ((replace=='') or (replacewith==''))):
        # Text options were blank
        print('\n-t and -r options cannot be blank. \nUse filerenamer -h to check the help section.')

    elif ((all=='Yes') and (file=='') and (replace!='') and (replacewith!='')):
        # Always display safety prompt
        answer = input('Your actions might change filenames permanently.\nPlease acknowledge the risk.\nEnter ''Y'' if you are sure(Y or N):')
        if (answer!='Y'):
            return

        try:
            # Authorization received. Rename all files.
            if ((len(os.listdir(os.getcwd())) == 0)):
                print('No files found in current directory.')
            else:
                for filename in os.listdir(os.getcwd()):
                    if replace in filename:
                        os.rename(filename, str(filename).replace(replace, replacewith))

        except Exception as e:
            print(e)

    elif ((all=='No') and (file=='')):
        # Incorrect inputs
        print('\nNo arguments specified for -a and -f. Use filerenamer -h to check the help section.')

    elif ((all=='No') and (file!='') and ((replace=='') or (replacewith==''))):
        # Text options were blank
        print('\n-f and/or -r options cannot be blank. \nUse filerenamer -h to check the help section.')

    elif ((all=='No') and (file!='') and (replace!='') and (replacewith!='')):
        # Always display safety prompt
        answer = input('Your actions change filenames permanently.\nPlease acknowledge the risk.\nEnter ''Y'' if you are sure(Y or N):')
        if (answer!='Y'):
            return

        try:
            # Authorization received. Rename specific file.
            if ((len(os.listdir(os.getcwd())) == 0)):
                print('No files found in current directory.')
            else:
                for filename in os.listdir(os.getcwd()):
                    if file==filename:
                        os.rename(file, str(file).replace(replace, replacewith))

        except Exception as e:
            print(e)

    else:
        print('Incorrect Processing. Error.')

    return

# Define a processing section to parse all the options available
def processoptions():
    # Process each input argument
    loopcount=0
    help='No'
    all='No'
    file=''
    replace=''
    replacewith=''
    goodtocall='Yes'

    for argument in sys.argv[1:]:
        if (str(argument)==optionlist[0]): # Check for help
            help='Yes'
        elif (str(argument)==optionlist[1]): # Check for all option
            all='Yes'
        elif ((len(str(argument))>=3) and (str(argument)[:3]==optionlist[2]) and all=='No'): # Check for file option
            file=str(argument)[3:]
        elif ((len(str(argument))>=3) and (str(argument)[:3]==optionlist[3])): # Check for text to substitute option
            replace=str(argument)[3:]
        elif ((len(str(argument))>=3) and (str(argument)[:3]==optionlist[4])): # Check for substitute text option
            replacewith=str(argument)[3:]
        else:
            print('\nOption '+ str(argument) +' is incorrect. Use filerenamer -h to check the help section.')
            goodtocall='No'

    if goodtocall=='Yes':
        filerenamer(help, all, file, replace, replacewith)
    return

# Define a main section so that the tool wont run if you import it
def main():
    # First check the number of options entered and then validity of each option
    if (noOfArguments == 1):
        print('\nNo arguments specified. Use filerenamer -h to check the help section.')
    elif (noOfArguments > 4):
        print('\nFilerenamer cannot accept more than 3 arguments. Use filerenamer -h to check the help section.')
    else:
        processoptions() # Process the options
    return

if __name__ == '__main__':
    main()
