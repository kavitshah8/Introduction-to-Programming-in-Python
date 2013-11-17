""" crypto.py
    Implements a simple substitution cypher
"""

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key =   "XPMGTDHLYONZBWEARKJUFSCIQV"

cipher = {'':'',}
def main():
  keepGoing = True
  while keepGoing:
    response = menu()
    if response == "1":
      plain = raw_input("text to be encoded: ")
      print encode(plain)
    elif response == "2":
      coded = raw_input("code to be decyphered: ")
      print decode(coded)
    elif response == "0":
      print "Thanks for doing secret spy stuff with me."
      keepGoing = False
    else:
      print "I don't know what you want to do..."

def menu():
    

def encode(plain):
    length = len(plain)
    plain = plain.upper()
    for c in plain:
                
    return encoded

def decode(coded):
    length = len(plain)
    plain = plain.upper()
    
    return decoded
