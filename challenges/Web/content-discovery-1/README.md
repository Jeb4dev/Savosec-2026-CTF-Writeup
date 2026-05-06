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

