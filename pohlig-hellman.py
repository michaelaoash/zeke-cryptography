import time


## Pohlig-Hellman exponentiation cypher
## (This is not RSA public key encryption.)
## Encryption key N is a prime
## e and d chosen so that
#### GCD(e,N-1) = 1 
#### e*d % N-1 = 1
## Encrypt with C = P ** e % N
## Decrypt with C ** d % N
## Questions to ponder:
## Why is it useful for decryption to find d so that e*d % N-1 = 1
## How do we find d, the multiplicative inverse of e, mod N-1


N = 2819
e = 769
d = 1693

## Provide plaintext in two-letter blocks with spaces
plaintext = 'po we rt ot he pe op le'
# plaintext = 'ab cd ef gh ij kl mn op'
# plaintext = 'aa bb cc dd ee ff gg hh ii jj'


## Encrypting using built-in exponents and DIY exponentiation

encrypted = [] 
plaintextNumeric = []
st = time.time()
for plaintextBlock in plaintext.split(' '):
    P = int(str(ord(plaintextBlock[0])-96) + str(ord(plaintextBlock[1])-96).zfill(2))
    plaintextNumeric.append(str(P).zfill(4))
    C = str( (P ** e) % N).zfill(4)
    encrypted.append(C)
et = time.time()
encrypt_elapsed_time = et - st
print("\nThe plaintext in two-character chunks is", plaintext)
print("The numeric version of the plaintext is", plaintextNumeric)
print("The encrypted version of each chunk is", encrypted)
print('Execution time:', encrypt_elapsed_time, 'seconds')


## Compute
encrypted = [] 
plaintextNumeric = []
st = time.time()
for plaintextBlock in plaintext.split(' '):
    P = int(str(ord(plaintextBlock[0])-96) + str(ord(plaintextBlock[1])-96).zfill(2))
    plaintextNumeric.append(str(P).zfill(4))
    C = 1
    for i in range(e):
        C = (C * P) % N
    C = str(C).zfill(4)
    encrypted.append(C)
et = time.time()
encrypt_elapsed_time = et - st
print("\nThe plaintext in two-character chunks is", plaintext)
print("The numeric version of the plaintext is", plaintextNumeric)
print("The encrypted version of each chunk is", encrypted)
print('Execution time:', encrypt_elapsed_time, 'seconds')


encrypted = [] 
plaintextNumeric = []
st = time.time()
for plaintextBlock in plaintext.split(' '):
    P = int(str(ord(plaintextBlock[0])-96) + str(ord(plaintextBlock[1])-96).zfill(2))
    plaintextNumeric.append(str(P).zfill(4))
    P10 = P**10
    P100 = P10**10
    C = str( (  (P100 ** 7) * (P10 ** 6) * P**9 ) % N).zfill(4)
    encrypted.append(C)
et = time.time()
encrypt_elapsed_time = et - st
print("\nThe plaintext in two-character chunks is", plaintext)
print("The numeric version of the plaintext is", plaintextNumeric)
print("The encrypted version of each chunk is", encrypted)
print('Execution time:', encrypt_elapsed_time, 'seconds')





print("\nDecrypting with and without key")


decrypted = []
decryptedText = ''
st = time.time()
for encryptedBlock in encrypted:
    P = str( (int(encryptedBlock) ** d) % N).zfill(4)
    decrypted.append(P)
    P = chr(int(P[0:2]) + 96) + chr(int(P[2:4]) + 96) + ' '
    decryptedText = decryptedText + P
et = time.time()
decrypt_elapsed_time = et - st

print("Decrypt the encrypted chunks to yield", decrypted)    
print("Expressed as plain text:", decryptedText)    
print('Execution time:', decrypt_elapsed_time, 'seconds')
print('\n')

st = time.time()
decryptedText = ''
d = 1
while decryptedText != plaintext + ' ':
    decrypted = []
    decryptedText = ''    
    for encryptedBlock in encrypted:
        P = str( (int(encryptedBlock) ** d) % N).zfill(4)
        decrypted.append(P)
        P = chr(int(P[0:2]) + 96) + chr(int(P[2:4]) + 96) + ' '
        decryptedText = decryptedText + P
    if d % 500 == 0:
        print(d, plaintext, decryptedText)
    d = d + 1
print(d, plaintext, decryptedText)    
et = time.time()
crack_elapsed_time = et - st


print("Guess the encrypted chunks to yield", decrypted)    
print("Expressed as plain text:", decryptedText)    
print('Execution time:', crack_elapsed_time, 'seconds', 'which is', crack_elapsed_time/decrypt_elapsed_time, 'times as long as decryption with key')






## Some modular notes with N=2819, e=769
(2819 - 1)*307  +  769*(-1125)
769*(-1125) % 2818
769*(2818-1125) % 2818
2818-1125
769*(1693) % 2818

(2819 - 1)*307  +  769*(-1125)
( (2819 - 1)*307  +  769*(1693) ) % 2818
