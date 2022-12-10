import time
import euclid

## RSA public-key encryption
## Encryption key N is the product of primes p,q
## e and d chosen so that
### GCD( e, (p-1)(q-1)  ) = 1
##### Note that phi(N) = (p-1)(q-1), which is the count of numbers < N that are relatively prime with N
### e*d % phi(N) = 1
## Encrypt with C = P ** e % N
## Decrypt with C ** d % N
## Questions to ponder:
## Why is it useful for decryption to find d so that e*d % phi(N) = 1
## How do we find d, the multiplicative inverse of e, mod phi(N)
## Why can't we find d even if we know N and e?

p = 53
q = 71

N = p*q

phi_N = (p-1)*(q-1)

e = 17
(gcd, d, y) = euclid.xgcd(17,phi_N)
print(d)
## Confirm that e*d = 1 mod phi_N
## Note that it is easy to generate d if you know e and phi_N


print("\nThe public key is", "( N=", N, ", e=", e, ")")

print("IMPORTANT! Keep these private:," "(p=", p, ", q=", q, ", phi_N=", phi_N, ", d=", d, ")")


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

print("\nDecrypt the encrypted chunks to yield", decrypted)    
print("Expressed as plain text:", decryptedText)    
print('Execution time:', decrypt_elapsed_time, 'seconds')

