#!/usr/local/bin/python3
"""Lesson 16 Obj 2 - final.py
   Read in text from a file given on the command line.  Count the frequency 
   of words of each length without punctuation and display results.
   USAGE:  ./final.py file.txt
"""

import sys
import collections
import string


def len_no_punctuation(w):
        """ This function taks a string (word) as a parameter and then
            counts up just the ascii.letters for each word.  It returns the 
            number of actual letters and an integer.
        """
        n = 0						# loop over the letters and count up just the ascii_letters
        for letter in w:
            if letter in string.ascii_letters:
                n += 1
        return n

if __name__ == "__main__":
     
        try:
            fn = sys.argv[1]
            f = open(fn,'r') 				# create file f the close it
        except IndexError:				# catch index problem with file
            print('A test file is required')
            sys.exit()
        except FileNotFoundError:			# catch file not found
            print('Cannot find that file')
            sys.exit()
        except Exception as msg:			# catch if something else when wrong
            print("Something unexpected occurred: {0}".format(msg))
            sys.exit()
        

        lst_of_words = list()				# declare an empty list
        lst_of_words = f.read().strip().split()		# read text into list as stripped of white space and split
        c = collections.Counter()			# form the dict c using .Counter()

        for word in lst_of_words:			# update dict c for each key
            c.update({len_no_punctuation(word):1})	# uses def to exclude punctuation in the letter count
        print("Length Count")
        for k, v in sorted(c.items()):			# print results of dict c
            if ( k == 0 ):				# ignore the '&' word result				
                continue
            print(k, v)
        
