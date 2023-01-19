# -*- coding: utf-8 -*-
'''In this script we are going to control our files are a fasta file
and checking the container of the file'''

import sys
# The sys module lets us access system-specific parameters and functions
import os.path
# The os.path module is used to verify the presence or not of the files


def fasta_control(fastafile):  # This function is used to check the file
    # regarding the extention of the file and the greater sign taking in argument the file name
    # Using the split function to check the extension of the file
    extension = fastafile.split(".")[-1]
    if extension in ["fasta", "faa", "fa", "fna"]: #if the extension match with any to those
        with open(fastafile, "r") as file:
            fasta_header = file.read(1)  # so we extract the first line or header
            if fasta_header.split()[0] == ">":  # to check if it start with the greater sign
                    return True  # So we can say it's a fasta file
            return False

ADN_LIST = ("A", "C", "G", "T") # Defining the list of nucelotides


def adn_read(fastafile):  #This function verifies if our file only contains nucleotides
    with open(fastafile, "r") as file:
        lines = file.readlines()
        #print(lines)
        counter = 0 #creating a counter for lines
        header = "" #creating a variable
        for line in lines: #Going line by line
            counter += 1 #So we count the lines
            if line[0] == ">": #If the line start with the greater sign
                header = line.strip()
                #So it's the header of the sequence,
                # and we return a copy of the string as a header
            else:
                line = line.strip() #It's the sequence and we return a copy of the string as line
                line = line.upper() #And we change all the characters in this line to upper alphabet
                column_counter = 0 #creating a counter for columns
                for char in line: #for every character in line
                    column_counter += 1 #So we count the numbers of the characters
                    if char not in ADN_LIST: #If the characters is not in the list
                        print("In the file" + fastafile + ":" + char +
                        " It's not a nucl in line " + str(counter) +
                        " and column " + str(column_counter) +
                        " for the sequence " + header[1:])

for arg in sys.argv[1:]: #For every file we put in our args except the script
    if os.path.isfile(arg): #If our file exists
        if os.path.splitext(arg)[1] == '.fasta' \
        or os.path.splitext(arg)[1] == '.faa' \
        or os.path.splitext(arg)[1] == '.fa' \
        or os.path.splitext(arg)[1] == '.fna': #If our file extention is a fasta file
        #And if the fasta control is True
            if fasta_control(arg) is True:
                # So we apply the adn_read function
                adn_read(arg)
            # The file doesn't contain a greater sign
            else:
                print("The following file : " + str(arg)
                + " may be not a fasta file, doesn't contain any headers. ")
        # The extension is not a fasta extension
        else:
            print("The following file : " + str(arg)
            + " is not a fasta file, check the extension. ")

    else: #The File doesn't exist
        print("The following file : " + str(arg) + " doesn't exist. ")
