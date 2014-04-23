#-------------------------------------------------------------------------------
# Name:        vnt-step1.py
# Purpose:     Make VNT files readable in two steps. 
#              This is step 1. VNT files come from samsung galaxy phones' memo 
#              app. 
#              This program reads "all.txt", so I recommend that before
#              running it, open a terminal and type "cat *.vnt > all.txt"
#              which will copy the text from all your VNT files to 1 file.
#              Change line 28 according to whether you want to keep the date
#              After runnning this, use vnt-step2.py to remove some
#              characters and replace them with Swedish ones. 
# Author:      natwei
#
# Created:     15/10/2013
# Copyright:   (c) natwei 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def main():

    notecounter = 0
    file = "all.txt"
    fo= open ("cleaner.txt", 'w')

    f = open(file, 'r')
    lines = f.readlines()
    for l in lines:
        if "BEGIN:VNOTE" in l:
            notecounter += 1
        elif "VERSION:1.1" in l:
            pass
        elif "DCREATED" in l:
            fo.write (l)  #write pass here if you don't want the date 
        elif "LAST-MOD" in l:
            pass
        elif "END:VNOTE" in l:
            pass
        else:
            s = l.strip ("BODY;CHARSET=UTF-8;ENCODING=QUOTED-PRINTABLE")
            fo.write (s)

    fo.close()
    f.close()


if __name__ == '__main__':
    main()
