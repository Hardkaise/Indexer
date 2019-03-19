This script is made to count the word occurrences in a movie script

You need to install python3.6 and matplotlib library:
https://www.python.org/downloads/
https://matplotlib.org/faq/installing_faq.html

To see how this script work, you can use "./indexer --help"

All the parameters are not mandatory except the filename
You must provide correct .txt file and not empty
You can change the number of words display by the graphics, the height and width of the window but you need to provide all the parameters in this case.

Ex: ./indexer filename.txt 50 6.4 4.8
It will count the occurrence of words in the file named filename.txt and will show the 50 words more used by decreasing in a window of 640x480 pixels

In the graphic window, you can zoom using magnifying glass by by drawing a rectangle on the curve.
You can click on the house to restore the original state
This script will also display the result with the total number of words at the end in the standard output, you can redirect in a file by doing this: ./indexer filename.txt > result.txt
