import sys
import rezeptOeffnen

def create(name : str) :
    file = open(name  + ".rzp", "wt")
    file.write("Zutaten\n")
    file.close()

def add(name, toAdd) : #["zeile1", "zeile2"]
    file = open(name  + ".rzp", "at")
    for line in toAdd:
        file.write("\n")
        file.write(line)
    file.close();

def main(args):
    if(args[0] == "create") :
        create(args[1])
    elif (args[0] == "load") :
        rezeptOeffnen.load(args[1])
    elif (args[0] == "add") :
        add(args[1], args[2:])

if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv[1:])
