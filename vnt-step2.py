#coding: utf-8 
#-------------------------------------------------------------------------------
# Name:        vnt-step2.py
# Purpose:     Make VNT files readable in two steps. 
#              This is step 2. VNT files come from samsung galaxy phones' memo 
#              app. Run this file after running vnt-step1.py
#              use vnt-step2.py to remove some
#              characters and replace them with Swedish ones. 
# Author:      natwei# Created:     15/10/2013
# Copyright:   (c) natwei 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def main():

    notecounter = 0

    fo= open ("cleaner3.txt", 'w')
    f = open("cleaner.txt", 'r')
    lines = f.readlines()
    for l in lines:
        l2 = l.replace ('=C3=B6', 'ö')
        l3 = l2.replace ('=C3=A4', 'ä')
        l4 = l3.replace ('=C3=A5', 'å')
        l5 = l4.replace ("=0A", '\n') 
        
        fo.write (l5)

    fo.close()
    f.close()


if __name__ == '__main__':
    main()
