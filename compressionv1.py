##########################################
#                                        #
#    Algrithm Name : Steal Algorithm     #
#    Script Name : compressorv1.py       #
#    Author : Ankit kumar                #
#                                        #
#           TIME : 10:00 AM              #
#           DATE : 02-Dec-2016           #
##########################################
import os
import shutil as sh
content = []
#FILE
def main():
    '''
     This function open file and
     read the content

    '''
    with open('fileA.txt') as file:
        lines = file.readlines()
        content.append(lines)
        file.close()
#File Content
def compress():
    '''This function is used to remove
       file after seperating file with content
    '''
    os.remove('fileA.txt')
    print('file compressed')


def decompress():
    decompressedFile = open('fileA.txt','w')
    #dataToWrite = ''.join(content).strip()
    for item in content:
        decompressedFile.write("%s\n" % ''.join(item).strip())
    print("file compressed done")
    
    


if __name__ == '__main__':
    main()



    
