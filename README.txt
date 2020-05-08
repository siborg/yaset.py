This little script has been written to help with creating symlink/copy versions of VST dll files to be used with YaBridge (https://github.com/robbert-vdh/yabridge) VST pluggin wrapper for Linux.
The intended use is to be integrated into file managers so that individual plugin links or copies can be easily created. 
I personally use it with Midnight Commander but it should be possible to integrate with with other linux file managers (Dolphin, Krusader etc)

BEFORE FIRST USE: 


Please edit the script first and set the yabridge_path variable to a valid location for your YaBridge installation. 

e.g. yabridge_path = '/usr/lib/libyabridge.so'

I will add autodetection in the future but for now this should suffice for a quick fix. 

USAGE: 

The plugin takes a dll file name as an agrument and by default creates a symling to libyabridge

Optional second argument --copy will make a copy of libyabridge.so with a matching VST plugin name 

The syntax is

yaset.py <filename of the dll VST plugin> < --copy (optional) to create a copy of libyabridge.so matching windows VST plugin name >

Any questions, issues, please let me know

S. 