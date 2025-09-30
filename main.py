# main.py
from mylib import myfunc

def ask(prompt, default=None):
   
    s = input(prompt).strip()
    return default if s == "" and default is not None else s

def main():
    
    char = ask("Enter a character (default = x): ", default="x")
    
    
    turns_raw = ask("How many turns you want to run [4]: ", default="4")

    try:
        turns = int(turns_raw)
    except ValueError:
        print("Invalid number. Using default = 4.")
        turns = 4

    if turns < 0:
        print("Turns must be non-negative. Using 0.")
        turns = 0

    
    for i in range(1, turns + 1):
        print(myfunc(char, i))

if __name__ == "__main__":
    main()
