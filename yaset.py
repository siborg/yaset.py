#!/usr/bin/env python3
#this little script takes as a argument a dll filename (with or without path) and either by default creates a symlink to libyabridge.so
#or if used with an optional --copy argument will make copy of libyabridge.so to match the plugin name. 
#please set your path to libyabridge in the yabridge_path variable


#set the path to libyabridge
yabridge_path = '/usr/lib/libyabridge.so'

#define a class for handling exceptions
class ExitExit(Exception): pass

#inport the required modules
import sys
import os
import shutil 

# print syntax function
def print_syntax():
    print('Syntax: yaset.py < file name with or without path, of the vst dll file (required) > < --copy - copies instead of symlinking (optional) >')
    exit

# function checks if file exists, and if so raises our ExitExit exception 
def check_path(path):
    if os.path.exists(path) == True:
        print('File ' + path + ' already exists, exiting')
        raise ExitExit
    else:
        return
# print operation error function    
def print_error(operation):
    print('Unable to carry out the ' + operation + ' operation, please check the the filenames/paths and try again')
    raise ExitExit

#check if file is an actual DLL file - this only checks extention, not whether a file is a vst plugin for real, raises custom exception if it is a dll extension
def dll_check(extension):
    if extension != '.dll':
        print('The file is not a dll file ,exiting')
        raise ExitExit
    else:
        return

# check for basic cmdline syntax errors 
if(  (len(sys.argv) <2 ) or ( len(sys.argv) == 1 ) or ( len(sys.argv) > 3) ):
    print_syntax()
else:
    try:
        # set the file name for the the target of link or file copy 
        filename = ((os.path.splitext(sys.argv[1]))[0] + '.so')
        
        #check if symlink/copied plugin path exists, and if yes, exit (function exception)
        check_path(filename)

        #check if file extention is a dll, and if so exit (function exception) 
        dll_check(os.path.splitext(sys.argv[1])[1])

        # if 2 arguments passes to the cmdline then check if the last one was --copy, if yes, try to carry out a copy operaton
        if len(sys.argv) == 3:

        #copy file instead of defaulting to symlinking
            
            if sys.argv[2] == '--copy':
                try:
                    shutil.copyfile(yabridge_path , filename)
                except ExitExit:
                    print_error('copy')                          
                #if arg #3 not == "--copy" then print syntax and exit       
            else:
                print_syntax()
        
        else:
        #create a symlink instead as the --copy was not specified on the cmd line
            try:
                os.symlink (yabridge_path, filename)
            except ExitExit:
                print_error('symlink')
    except ExitExit:
        exit