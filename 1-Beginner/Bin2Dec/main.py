from bin2dec import bin2dec

while True:
    try:
        a = int(input("Please inform binary to convert to decimal(input value lower than 0 to exit):"))
    except:
        print("It's allow only numbers")
        continue
    if(a>=0):
        try:
            print(bin2dec(a))
        except TypeError:
            print(("The value {0} is invalid").format(a))
        a=0
    else:
        print("Exiting....")
        break
