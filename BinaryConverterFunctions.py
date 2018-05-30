hex2bin = dict('{:x} {:04b}'.format(x,x).split() for x in range(16))
bin2hex = dict('{:b} {:x}'.format(x,x).split() for x in range(16))
 
def float_dec2bin(d):
    neg = False
    if d < 0:
        d = -d
        neg = True
    hx = float(d).hex()
    p = hx.index('p')
    bn = ''.join(hex2bin.get(char, char) for char in hx[2:p])
    return (('-' if neg else '') + bn.strip('0') + hx[p:p+2]
            + bin(int(hx[p+2:]))[2:])
 
def float_bin2dec(bn):
    #print(bn)
    neg = False
    if bn[0] == '-':
        bn = bn[1:]
        neg = True
    #print(bn[0])   
    if ('.' in bn):
        dp = bn.index('.')
    else:
    #print("bn = ", str(bn))
        return 0
    extra0 = '0' * ((4 - (dp % 4)) % 4)
    bn2 = extra0 + bn
        
    
    if ('.' in bn2 and 'p' in bn2):
        dp = bn2.index('.')
        p = bn2.index('p')
    else:
    #print("bn = ", str(bn))
        return 0
    
    

    hx = ''.join(bin2hex.get(bn2[i:min(i+4, p)].lstrip('0'), bn2[i])
for i in range(0, dp+1, 4))

    bn3 = bn2[dp+1:p]
    extra0 = '0' * (4 - (len(bn3) % 4))
    bn4 = bn3 + extra0
    #print(bn4)

    for i in range(0, len(bn4), 4):
        if (bn4[i:i+4])=='0000':
            hx += ''
        else:
            #print(bn4[i:i+4])
            try:
                hx += ''.join(bin2hex.get(bn4[i:i+4].lstrip('0')))
            except TypeError:
                #print("Type error")
                return 0
        if('+' in bn2[p+2:]):
        #print("bn = ", str(bn))
            return 0
        else:
            try:
                hx = (('-' if neg else '') + '0x' + hx + bn2[p:p+2]
                      + str(int('0b' + bn2[p+2:], 2)))
            except ValueError:
                print("Value error")
                return 0
        #print(hx)
        try:
            result = float.fromhex(hx)
        except ValueError:
            print("Value error")
            return 0    
        return float.fromhex(hx)
