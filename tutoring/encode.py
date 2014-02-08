alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key =   "XPMGTDHLYONZBWEARKJUFSCIQV"

mydict = {k:v for k, v in zip(alpha, key)}

def encode(plain):
    plain = plain.upper()
    return ''.join([mydict.get(i, i) for i in plain])
