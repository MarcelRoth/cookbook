import sys

def load(name : str) :
    file = open(name + ".rzp", "rt")
    content = file.read()
    file.close()
    print(content)

def create(name : str) :
    file = open(name  + ".rzp", "wt")
    file.write("Zutaten\n")
    file.close()

def add(name : str, toAdd : str) :
    file = open(name  + ".rzp", "at")
    file.write(toAdd)
    file.close();

def main(args):
    if(args[0] == "create") :
        create(args[1])
    elif (args[0] == "load") :
        load(args[1])
    elif (args[0] == "add") :
        add(args[1], args[2])

if __name__ == "__main__":
    # execute only if run as a script
    main(sys.argv[1:])

