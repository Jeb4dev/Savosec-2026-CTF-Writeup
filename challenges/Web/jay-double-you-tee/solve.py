import hmac
import hashlib
import base64

# Your JWT
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiYWRtaW4iLCJyb2xlIjoiZ3Vlc3QiLCJpYXQiOjE3NzgwNjIzMzUsImV4cCI6MTc3ODA2NTkzNX0.t8bEbuIYF8bIf_VOzH40HUmPqAsNoTlXddGbqVVxxgM"

# Split into header+payload and signature
header_payload, signature = token.rsplit('.', 1)


# Fix Base64Url padding for decoding
def decode_b64url(s):
    s += '=' * (-len(s) % 4)
    return base64.urlsafe_b64decode(s)


target_sig = decode_b64url(signature)

# Small wordlist of likely CTF candidates
wordlist = [
    "secret", "password", "admin", "123456", "qwerty",
    "omni", "omnicorp", "vault", "sector7", "neurosync", "guest",
    "savosec", "jaydoubleyoutee"
]

print("Starting brute force...")
for word in wordlist:
    # Generate an HMAC SHA256 signature using the current word
    sig = hmac.new(word.encode(), header_payload.encode(), hashlib.sha256).digest()

    if sig == target_sig:
        print(f"\n[+] SUCCESS! The secret key is: {word}")
        exit()

print("\n[-] Secret not found in the provided wordlist.")