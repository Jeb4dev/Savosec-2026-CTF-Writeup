from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import binascii

# 1. Setup the extracted parameters
key = b"super_secret_encryption_key_here"

iv = bytes(range(16))

ct_hex = "27758c250a1834f18bbe00db706f5849f85b010390c1729a1933855ca6c5230161f5b53f5cf2c7c69bf24b2f305664ac"

# 2. Convert hex ciphertext to raw bytes
ciphertext = binascii.unhexlify(ct_hex)

# 3. Decrypt
cipher = AES.new(key, AES.MODE_CBC, iv)
padded_plaintext = cipher.decrypt(ciphertext)

# 4. Remove the PKCS#7 padding (\x0e bytes) and decode to a string
flag = unpad(padded_plaintext, AES.block_size).decode('utf-8')

print("Decrypted text:", flag) # Decrypted text: SavoSec{Caesar_Did_Not_Protect_Me}
