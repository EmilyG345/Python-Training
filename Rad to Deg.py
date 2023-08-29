def getrad1():
    while True:
        try:
            x = float(input("Please enter a number:").replace(',', '.').strip())
            deg = x * (180/math.pi)
            print(deg)
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
            
getrad1()
