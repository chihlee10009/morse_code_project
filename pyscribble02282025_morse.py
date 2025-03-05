import os
import time

#python Dictionary
morse_code = {
"a" : ".-",
"b"	: "-...",
"c"	: "-.-.",
"d" : "-..",
"e"	: ".",
"f"	: "..-.",
"g"	: "--.",
"h"	: "....",
"i"	: "..",
"j"	: ".---",
"k"	: "-.-",
"l"	: ".-..",
"m"	: "--",
"n"	: "-.",
"o"	: "---",
"p"	: ".--.",
"q"	: "--.-",
"r"	: ".-.",
"s"	: "...",
"t"	: "-",
"u"	: "..-",
"v"	: "...-",
"w"	: ".--",
"x"	: "-..-",
"y"	: "-.--",
"z"	: "--.."
}  

msg = "helpme"
enc_msg = ""

for letter in msg:
    enc_msg += morse_code[letter] + " "

print(msg, ":", enc_msg)
for sound in enc_msg: 
    if sound == ".":
        os.system("say da")
    elif sound == "-":
        os.system("say dash")
    elif sound == " ":
        time.sleep(1)

