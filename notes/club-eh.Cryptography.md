---
id: 6fxn5vgrwgkzzq2ofgfqnsp
title: Cryptography
desc: ''
updated: 1668727047172
created: 1668727038638
---
Next Chapter: [[club-eh.Password_Cracking]]

- Pratice of concealing messages or information within other non-secret text or data
- Critical for secure comminication

###  Ciphers
~ *Taking plaintext messages and making them unrecognizable to anyone who does not have the key*
Cryptanalysis : Crypher identification 

[Common ciphers](https://www.dcode.fr/tools-list#cryptography)
- At a glance:
    - Caesar Cipher
    - Vigenere Cipher
    - ROT13
    - Base64
    - Rail Fence
    - Pigpen Cipher
    - Alberti Cipher
   

## Encoding 
~ *Taking plaintext and converting it to another format for the purpose of efficient data transmission across computers*
 
![](/assets/Encoding.png){width: 40%, float: right, margin: 10px 1px 10px}
- Common readable encodings: 
    - ASCII
    - UTF-8
    - UNICODE
    - ISO-8859

- Common non-readable encodings:
    - Binary
    - Hexadecimal
    - Base64
    - QR Code/ Barcodes
    - Decimal


- Constructed Languages / Scripts 
    - Sometimes people will encrypt their messages by creating artificial languages or charater scripts. There are catalogues of these online. Any alphabet or writing system is composed of "constructed scripts". [List](https://omniglot.com/conscripts/) 


- Hashing
    - One way function
    - Takes a string of any length and returns a fixed length string
    - Used for password storage
    - MD5, SHA1, SHA256, SHA512

## Steganography
~ *Hiding messages or files within other files or messages *

- There are many tools out there that can be used to hide data within other data adn the algorithm used is unique to that tool. Because of this, you need to know what tool was used to hide the data in order to the data back out. You may need to know a password in order to extract the data, even if you know the right tool.
- [TL:DR] Lots of different ways of hiding data... like a lot
 > - Hide messages in images
    - Hide images in images
    - hide text in images
    - hide zip files in images
  - Hiding messages in audio
    - You map
  - Hiding messages in software
    - This is explotation and enumeration, where we reverse engineer software

#### Common Tools
- Steghide
    - StegCracker can be used to BF stego made using steghide
- Digital Invisible Ink Toolkit
- Binwalk
    -Used to explore suspected stego files
- Sonic Visualiser
    - For exploring audio files


## Encryption
~ *Using algorithms to turn a message into a string of data that looks meaningless and scrambled noise.*

