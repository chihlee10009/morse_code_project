import os
import time
import random

#DONE: be able to input msg on cmd line
#DONE: be able to input morse on cmd line and get msg
#DONE: have program randomly show me a letter with the code 
#        I have to input the letter and code back
#        if I get it incorrect the program says try again 
#        If i get it correct then system plays the correct morse code sound
#DONE: have program randomly print a letter where I have to respond with morse
#DONE: plays the morse
#TODO:
#DONE: have program randomly print a morse and i have to respond with a letter
#TODO: review method for playing sound after typing the letter and code correctly
#TODO: program keeps running after first correct input
#        ask user if he wants to quit program by typing quit
class Morse_code:   
#python Dictionary
#can only have 1 __init__ method per class

  def __init__(self):
    self.morse_code = {
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
      "z"	: "--..",
      ".-" : "a",
      "-..." : "b",
      "-.-." : "c",
      "-.." : "d",
      "." : "e",
      "..-." : "f",
      "--." : "g",
      "...." : "h",
      ".." : "i",
      ".---" : "j",
      "-.-" : "k",
      ".-.." : "l",
      "--" : "m",
      "-." : "n",
      "---" : "o",
      ".--." : "p",
      "--.-" : "q",
      ".-." : "r",
      "..." : "s",
      "-" : "t",
      "..-" : "u",
      "...-" : "v",
      ".--" : "w",
      "-..-" : "x",
      "-.--" : "y",
      "--.." : "z"
    }  
  
  def input_message(self):
    self.msg = input("input your message: ")
  

  def input_morse(self):
    self.morse = input("input your morse code: ")
  
  def morse_code_to_english(self):
    self.input_morse()
    msg = ""
    for letter in self.morse.split():
      #print("printig letter", letter)
      #input(">>")
      msg += self.morse_code[letter]
    print(msg)  

  def english_to_morse_code(self):
    self.input_message()
    enc_msg = ""

    for letter in self.msg:
      enc_msg += self.morse_code[letter] + " "

    print(self.msg, ":", enc_msg)
    self.morse_msg = enc_msg
    self.play_sound()

  def play_sound(self):
    for sound in self.morse_msg: 
      if sound == ".":
        os.system("powershell.exe [System.Console]::Beep()")
      elif sound == "-":
        os.system("powershell.exe [System.Console]::Beep(500, 800)")
      elif sound == " ":
        time.sleep(1)

  def get_random_letter_and_code(self):
    num = random.randint(0, 26)
    keys = self.morse_code.keys()
    keys = list(keys)
    
    self.letter = keys[num]
    self.code = self.morse_code[self.letter]

  def morse_code_learning(self):
    self.get_random_letter_and_code()
    
    print(self.letter, self.code)
    repeat_letter_code = input("input the letter and code\n")
    
    while repeat_letter_code != self.letter + " " + self.code:
      print("try again!")
      repeat_letter_code = input("input the letter and code\n")
    
    print("well done!")
    self.morse_msg = self.code
    self.play_sound()

  def random_letter(self):
    self.get_random_letter_and_code()
    print(self.letter)
    user_morse = input("insert morse code for this letter\n>>")
    
    while user_morse != self.code:
      print("Wrong! Try again!")
      user_morse = input("insert morse code for this letter\n>>")
    
    print("Great Job!")
    self.morse_msg = self.code
    self.play_sound()

    print("ready for another?")
    continue_game = input("y/n: ")
    if continue_game == "y":
      self.random_letter()

  def random_morse(self):
    self.get_random_letter_and_code()
    print(self.code)
    user_letter = input("insert letter for this morse code:\n>>")

    while user_letter != self.letter:
      print("Wrong! Try again!:")
      user_letter = input("insert letter for this morse code:\n>>")

    print("Great Job!")
    self.morse_msg = self.code
    self.play_sound()

    print("ready for another?")
    continue_game = input("y/n: ")
    if continue_game == "y":
      self.random_morse()


      

  



  
  

morse_obj = Morse_code()
#morse_obj.english_to_morse_code()
#morse_obj.morse_code_to_english()
morse_obj.morse_code_learning()
