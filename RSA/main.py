import math

def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n

p = 3
q = 7

n = p * q
print("n =", n)

phi = (p-1)*(q-1)
print("phi =", phi)

e = 2
while(e < phi):
    if (math.gcd(e, phi) == 1 and IsPrime(e)):
        break
    else:
        e += 1

print("e =", e)
# Пара {e,n} - открытый ключ

for i in range(phi): # от 0 до phi-1 (в range последнее число не входит)
    if(e*i % phi == 1):
        d = i
        break

# Пара {d,n} - закрытый ключ
# Открытый ключ отправляется всем, закрытый остается у нас

print("d =", d)
print(f'Открытый ключ: {e, n}')
print(f'Закрытый ключ: {d, n}')

# Входное сообщение (работает с числом <= n)
msg = 19
print(f'Входное сообщение:{msg}')

# Шифрование
C = pow(msg, e)
C = C % n
print(f'Зашифрованное сообщение: {C}')

# Расшифрование
M = pow(C, d)
M = M % n

print(f'Расшифрованное сообщение: {M}')