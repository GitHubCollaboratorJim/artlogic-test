def encode():
    fin  = open("testencode.txt", "r")
    fout = open("ConvertedData.txt", "w")

    for x in fin:
        n = int(x)
        if n > 8191 or n < -8192:
            print(str(n) + " must be between -8192 and 8191" + "\n")
        else:
            n += 8192
            if n == 0:
                bytestring = '0000000000000000'
            else:
                bytestring = dec2bin(n)
            decodestr = bin2dec(bytestring[0] + bytestring[2:9] + '0' + bytestring[9:])
            fout.write(decodestr + "\n")
    fin.close
    fout.close

def decode():
    fin  = open("testdecode.txt", "r")
    fout = open("ConvertedData.txt", "a")

    for x in fin:
        n = str(x[0:4])
        bytestring = hex2bin(n)
        encodestr = bin2dec('0' + bytestring[0:8] + bytestring[9:])
        nhex = int(encodestr, 16)
        nint = nhex - 8192
        fout.write(str(nint) + "\n")
    fin.close
    fout.close

def hex2bin(n):
    hexDict = {
        '0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101',
        '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'a':'1010', 'b':'1011',
        'c':'1100', 'd':'1101', 'e':'1110', 'f':'1111', 'A':'1010', 'B':'1011',
        'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111', }

    return ''.join([hexDict[hstr] for hstr in str(n)[0:]])

def dec2bin(n):
    hexDict = {
        '0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101',
        '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'a':'1010', 'b':'1011',
        'c':'1100', 'd':'1101', 'e':'1110', 'f':'1111', 'A':'1010', 'B':'1011',
        'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111', }

    return ''.join([hexDict[hstr] for hstr in hex(n)[2:]])

def bin2dec(h):
    decDict = {
        '0000':'0', '0001':'1', '0010':'2', '0011':'3', '0100':'4', '0101':'5',
        '0110':'6', '0111':'7', '1000':'8', '1001':'9', '1010':'A', '1011':'B',
        '1100':'C', '1101':'D', '1110':'E', '1111':'F'}

    ds = ''
    i = 0
    for hstr in str(h)[i:i+4]:
        ds = ds + decDict.get(str(h)[i:i+4])
        i += 4
    return ds

encode()
decode()
