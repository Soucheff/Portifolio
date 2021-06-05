def bin2dec(bin):
    dec = 0
    i = 0
    if type(bin) != int:
        raise TypeError("Not Numeric")
    while bin > 0:
        if(bin%10 > 1):
            raise TypeError("Invalid Number")
        dec += pow(2,i)*(bin%10)
        bin = bin//10
        i+=1
    return dec


def unit_test():
    assert bin2dec(0) == 0
    assert bin2dec(1) == 1
    assert bin2dec(10) == 2
    assert bin2dec(10101) == 21
    assert bin2dec(1010101010101010001010100101101000101011) == 732999342635
    try:
        assert bin2dec(1234)
        assert False
    except TypeError:
        assert True
    try:
        assert bin2dec('0')
        assert False
    except TypeError:
        assert True

if __name__ == "__main__":
    try:
        unit_test()
        print("Everything is fine...")
    except:
        print("Failed...")

