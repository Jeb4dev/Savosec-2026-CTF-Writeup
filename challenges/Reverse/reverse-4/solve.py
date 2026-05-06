from Crypto.Cipher import AES
import binascii

# 1. Setup the extracted parameters
key = b"super_secret_encryption_key_here"
iv = b"\x00" * 16  # Assuming null IV
ct_hex = "27758c250a1834f18bbe00db706f5849f85b010390c1729a1933855ca6c5230161f5b53f5cf2c7c69bf24b2f305664ac"

# 2. Convert hex ciphertext to raw bytes
ciphertext = binascii.unhexlify(ct_hex)

# 3. Decrypt
cipher = AES.new(key, AES.MODE_CBC, iv)
plaintext = cipher.decrypt(ciphertext)

print("Decrypted text:", plaintext)