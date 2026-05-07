# Content Discovery 2

## Description

Find the flag.

url: https://ctf1.savosec.fi/discover2/

----
``https://ctf1.savosec.fi/discover2/robots.txt`` reveals ``private`` folder:

Looking for hidden files in private folder using ffuf:

````bash
└─$ ffuf -u https://ctf1.savosec.fi/discover2/private/FUZZ -w /usr/share/wordlists/dirb/common.txt -e .txt,.php,.html,.bak,.log,.json -fc 404        


        /'___\  /'___\           /'___\       
       /\ \__/ /\ \__/  __  __  /\ \__/       
       \ \ ,__\\ \ ,__\/\ \/\ \ \ \ ,__\      
        \ \ \_/ \ \ \_/\ \ \_\ \ \ \ \_/      
         \ \_\   \ \_\  \ \____/  \ \_\       
          \/_/    \/_/   \/___/    \/_/       

       v2.1.0-dev
________________________________________________

 :: Method           : GET
 :: URL              : https://ctf1.savosec.fi/discover2/private/FUZZ
 :: Wordlist         : FUZZ: /usr/share/wordlists/dirb/common.txt
 :: Extensions       : .txt .php .html .bak .log .json 
 :: Follow redirects : false
 :: Calibration      : false
 :: Timeout          : 10
 :: Threads          : 40
 :: Matcher          : Response status: 200-299,301,302,307,401,403,405,500
 :: Filter           : Response status: 404
________________________________________________

backup.txt              [Status: 200, Size: 46, Words: 1, Lines: 2, Duration: 56ms]
````

ctf1.savosec.fi/discover2/private/backup.txt

SavoSec{46e3c353-a41e-4535-999f-7a2dee77a2ea}
