# % = modulus ** exponent
name = "I don't what the hell that supposed to mean"
word = ""
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def coprime(a, b):
    return gcd(a, b) == 1


p = 79; #prime number 1
q = 89; #prime number 2
N = p*q
primen = (p-1)*(q-1)

def enc():
    for i in range(0, 2**20):
        if i > 1 and i < primen and coprime(i,N) and coprime(i,primen):
            return i




def dec():
    x = 1
    for i in range(0, 2**20):
        if i*enc()%primen == 1:
            return(i)


def encrypt(x):
    numa = ''
    for i in range(0,len(x)):
        num1 = ord(x[i])

        for z in range (0, len(str(num1))):
            numa += str(int(str(num1)[z])**enc()%N)
            if z < len(str(num1))-1:
                numa += ','
            else:
                numa += ';'

    return numa


def decrypt(x):
    prot = x
    cap = int(prot)**dec()%N
    return cap






job2 = encrypt(name).split(';')[:-1]

decmsg = ''

for i in job2:
    breakdown = i.split(',')
    for a in range(0,len(breakdown)):
        unpro = decrypt(int(breakdown[a]))
        decmsg += str(unpro)

        if a == len(breakdown)-1:
            decmsg += ';'

print(job2)
print(decmsg)

newlist = decmsg.split(';')[:-1]

clearmsg = ''
for i in newlist:
    clearmsg += chr(int(i))

print(clearmsg)

















