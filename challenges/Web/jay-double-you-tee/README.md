# Jay Double You Tee!!

## Description

The Omni-Corp Sector 7 Data Vault is protected by state-of-the-art NeuroSync token technology. However, reports indicate that it may be possible to bypass the standard authentication protocols. Can you find a way to access the admin panel?



---



host: https://ctf3.savosec.fi/vault/

https://www.jwt.io/

Another related to cookies, this time JSON Web tokens (JWT). Using algo=none doesnt work, we need valid secret key.

Wow, key was signed with secret revealed on another room (i-have-trypanophobia) and it works!

secret key = ``ghost_in_the_omni_shell_secure_v1``

![img.png](img.png)

SavoSec{JwTs_4r3_4w3s0m3_but_s3cur1ty_m4tt3rs} 
