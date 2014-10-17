#Directory Tree Copier
v1.1

##Description

Directory Tree Copier copies the entire directory structure and all files of the \<input_directory\> and creates the same structure in \<output_directory\> with blank files. Useful for cloning directory structures/files without taking up much room on the disk.

##Dependencies
Directory Tree Copier was designed for Linux.

* Bash
* Python 2.7+

##Install
* Clone git archive via the following command; 
  
  `git clone https://github.com/p014k/cpdirtree.git cpdirtree`
* Change directories via `cd cpdirtree`
* Run the following command to install;
  
  `sudo ./setup.sh install`

This will install Directory Tree Copier (`cpdirtree`) to /usr/local/bin.

##Usage
Run from the command line;

`cpdirtree [-h] <input_directory> <output_directory> [-b] BLACKLIST`

####Required parameters
`<input_directory>` and `<output_directory>` are required.

####Optional parameters
`-h` for help

`-b BLACKLIST`, `--blacklist BLACKLIST` specifies a list of files and/or directories (separated by a space) to omit from rescuing (case-sensitive). Wildcards are accepted.
###Example 
`user@computer:$ cpdirtree /media/Drive1/ /media/Drive2/Backup/ -b *.mp3 'Pictures Of Me'` (This will omit all mp3 files and a directory called Pictures Of Me). 

Note: Directories and files with characters that need escaping can be put in quotes. Files and directories are case-sensitive. Wildcards are accepted.

##Uninstall
* Run the following command to uninstall;
  
  `sudo ./setup.sh uninstall`

##Changelog
* v1.1

  Added `--version`

  Removed regex in favor of pythonic solution to hidden directories.

* v1.0 (09 October 2014)

  Initial Release

##Development Notes
Tested with the following program versions;

* Bash v4.3.11(1)-release (i686-pc-linux-gnu)
* Python 2.7.6

##Author
[Brian Mikolajczyk](https://github.com/p014k), brianm12@gmail.com

##Legal
Copyright (c) 2014, Brian Mikolajczyk, brianm12@gmail.com

###Licence
Please see file LICENCE.

###Copying
Please see file COPYING.
