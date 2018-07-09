def load(name : str) :
    file = open(name + ".rzp", "rt")
    content = file.read()
    file.close()
    print(content)

if __name__ == "__main__":
    load("Pizza")