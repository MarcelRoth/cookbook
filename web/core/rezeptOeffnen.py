def load(name : str) :
    file = open(name + ".rzp", "rt")
    content = file.read()
    file.close()
    return content

if __name__ == "__main__":
    print(load("Pizza"))