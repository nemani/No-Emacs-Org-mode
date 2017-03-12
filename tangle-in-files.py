import sys

f = open(sys.argv[1], 'r')
main = open("main.org", 'a') #replace main.org with name of output org-file
main.write("\n\n#+BEGIN_SRC " + sys.argv[2] + " :tangle " + sys.argv[1] + "\n" + f.read() + "\n\n#+END_SRC\n")



# usage 
# python3 tangle-in-files.py (file-to-tangle) (language-of-file)