balance = 0

def main():
    
    print("Initial Balance: ", balance)
    deposite(100)
    withdrow(50)
    print("After Balance: ", balance )

def deposite(n):
    global balance
    balance += n

def withdrow(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()