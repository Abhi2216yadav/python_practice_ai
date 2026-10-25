# import cowsay
import sys

# from saying import hello
from saying import goodbye

if len(sys.argv) == 2:
    # cowsay.cow("Hello, " + sys.argv[1]) # for cow
    # cowsay.trex("Hello, " + sys.argv[1]) #for dianasour
    # hello(sys.argv[1])
    goodbye(sys.argv[1])
