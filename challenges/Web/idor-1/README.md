# idor 1

Goal

Read the admin user's profile, which contains the flag.

url: https://ctf2.savosec.fi/03-idor1/
What is IDOR?

IDOR = Insecure Direct Object Reference. The app exposes an internal ID in the URL or request body and uses it to fetch data — without checking whether the requesting user is allowed to see that specific record.

Classic shape:

GET /users/42            ← "I want user 42's profile page"
GET /orders/18923        ← "I want order 18923"
GET /invoices/2024-0031

The server fetches the record but forgets to check "is the caller the owner of this record, or at least authorized to see it?" So any authenticated user can read any record by changing the ID.
Tools

    curl
    Your browser
    Burp Suite (intercept + modify) in real engagements

---

Change 

https://ctf2.savosec.fi/03-idor1/users/2

-> 

https://ctf2.savosec.fi/03-idor1/users/1

reveals the flag:

SavoSec{93bb0e2c-7943-45b3-aa16-c755110ef83a}
