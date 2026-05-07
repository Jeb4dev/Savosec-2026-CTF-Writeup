# Auth bypass 1

## Description

An authentication bypass is a severe security vulnerability that occurs when an attacker circumvents an application's authentication protocols to gain unauthorized access without providing valid credentials. 



Discover the flag by modifying cookie payload



### What you need



- A browser (DevTools → Application → Cookies), OR

- `curl` (`-b` to send cookies)



Site: https://ctf4.savosec.fi/bypass1/

Change plain text cookie payload from:

role: user -> role: admin

reload the page:

Flag: SavoSec{343eabc8-9297-45bd-8a0b-923c2f2d31af}



