# Walking my way downtown

## Description

![doggo.jpg](/files/7a0f72f12b2323fa3e1796e86ffa1a38/doggo.jpg)



---

I found the best doggo in this part of town. It was digging for some secrets...



┌──(kali㉿kali)-[~/Downloads]
└─$ exiftool doggo.jpg
ExifTool Version Number         : 13.50
File Name                       : doggo.jpg
Directory                       : .
File Size                       : 588 kB
File Modification Date/Time     : 2026:05:06 10:56:21-04:00
File Access Date/Time           : 2026:05:06 10:56:55-04:00
File Inode Change Date/Time     : 2026:05:06 10:56:21-04:00
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
Comment                         : YmVzdGRvZ2ludG93bg==
Image Width                     : 1530
Image Height                    : 1417
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 1530x1417
Megapixels                      : 2.2
                                                                                                                                                                               
┌──(kali㉿kali)-[~/Downloads]
└─$ echo "YmVzdGRvZ2ludG93bg==" | base64 -d                                                                                                                  
bestdogintown                                                                                                                                                                               
┌──(kali㉿kali)-[~/Downloads]
└─$ 7z x doggo.jpg                         

7-Zip 26.00 (x64) : Copyright (c) 1999-2026 Igor Pavlov : 2026-02-12
 64-bit locale=en_US.UTF-8 Threads:8 OPEN_MAX:1024, ASM

Scanning the drive for archives:
1 file, 587819 bytes (575 KiB)

Extracting archive: doggo.jpg
--
Path = doggo.jpg
Type = 7z
Offset = 587625
Physical Size = 194
Headers Size = 146
Method = LZMA2:12 7zAES
Solid = -
Blocks = 1

    
Enter password (will not be echoed):
    
Would you like to replace the existing file:
  Path:     ./secret.txt
  Size:     36 bytes (1 KiB)
  Modified: 2026-05-02 09:45:15
with the file from archive:
  Path:     secret.txt
  Size:     36 bytes (1 KiB)
  Modified: 2026-05-02 09:45:15
? (Y)es / (N)o / (A)lways / (S)kip all / A(u)to rename all / (Q)uit? y

Everything is Ok 

Size:       36
Compressed: 587819
                                                                                                                                                                               
┌──(kali㉿kali)-[~/Downloads]
└─$ cat secret.txt
SavoSec{The_D0gg0_dUg_w1th_B1nw4lk}

