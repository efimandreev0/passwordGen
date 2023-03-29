import random, string

def info():
    print("Usage: python toolName.py passwordCharactersCount")
    
def main():
    password = ('').join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k = sys.argv[0]))
    print ("Your password: " + password)
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        info()
    else:
        main()    