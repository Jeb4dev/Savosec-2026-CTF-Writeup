# Content Discovery 1

## Description

**Goal:** Find the flag file hidden somewhere on the web site.



url: https://ctf1.savosec.fi/discover1/



### What is content discovery?



Web servers often host files and directories that aren't linked from the main site — backups, staging copies, admin panels, forgotten `.git` folders, dev endpoints. Content discovery means systematically probing the server for these hidden paths.



Attackers do this with wordlists and tools like `gobuster`, `feroxbuster`, `ffuf`, or `dirb`. Defenders do it too, during internal audits, to catch what their devs left behind.



### Tools



- `curl` — your first friend

- `gobuster` — classic directory bruteforcer

- `ffuf` — faster, more flexible

- Even a browser — check `/robots.txt`, HTML comments, etc.


https://ctf1.savosec.fi/discover1/backup-notes/flag.txt

````bash
└─$ curl https://ctf1.savosec.fi/discover1/robots.txt                                     
User-agent: *
Disallow: staging-area/
Disallow: backup-notes/
````

````bash
└─$ curl https://ctf1.savosec.fi/discover1/backup-notes/
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
 <head>
  <title>Index of /backup-notes</title>
 </head>
 <body>
<h1>Index of /backup-notes</h1>
<ul><li><a href="/"> Parent Directory</a></li>
<li><a href="._flag.txt"> ._flag.txt</a></li>
<li><a href="flag.txt"> flag.txt</a></li>
</ul>
<address>Apache/2.4.67 (Unix) Server at ctf1.savosec.fi Port 80</address>
</body></html>
````

````bash
└─$ curl https://ctf1.savosec.fi/discover1/backup-notes/flag.txt
SavoSec{860de899-a845-49b2-936c-965f29b58fb5}
````

Flag: SavoSec{860de899-a845-49b2-936c-965f29b58fb5}
