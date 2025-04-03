import os
import time
import random
import platform
#DONE: be able to input msg on cmd line
#DONE: be able to input morse on cmd line and get msg
#DONE: have program randomly show me a letter with the code 
#        I have to input the letter and code back
#        if I get it incorrect the program says try again 
#        If i get it correct then system plays the correct morse code sound
#DONE: have program randomly print a letter where I have to respond with morse
#        plays the morse
#DONE: have program randomly print a morse and i have to respond with a letter
#        plays the morse
#DONE: program keeps running after first correct input
#        ask user if he wants to quit program by typing quit
#DONE: Play game 1 {letter_and_morse}, game 2{morse_to_letter}, game 3{letter_to_morse}
#        new method to select bewteen games 1 through 3
#DONE: have program figure out whether it's running on a Windows or Mac?
#       if on windows system then use Windows sounds
#       if on mac system the use mac sounds
#TODO: after 3 attempts give letter and morse as answer
#       have user input morse
#       go back to selected game



class Morse_code:   
#python Dictionary
#can only have 1 __init__ method per class

  def __init__(self):
    self.operating_system_discovery = platform.system()
    self.failed_attempts = 0
    
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
        if self.operating_system_discovery.startswith("Win"):
          os.system("powershell.exe [System.Console]::Beep()")
        else:
          os.system("say da")

      elif sound == "-":
        if self.operating_system_discovery.startswith("Win"):
          os.system("powershell.exe [System.Console]::Beep(500, 800)")
      
        else:
          os.system("say daa")

      elif sound == " ":
        time.sleep(1)

  def get_random_letter_and_code(self):
    num = random.randint(0, 26)
    keys = self.morse_code.keys()
    keys = list(keys)
    
    self.letter = keys[num]
    self.code = self.morse_code[self.letter]

  def play_again(self):
    self.failed_attempts = 0
    print("ready for another?")
    self.continue_game = input("y/n: ")
      
  def user_input_loop(self):
    #count the number of failed attempts as a result of user incorrect imput

    self.failed_attempts += 1
    if self.failed_attempts >= 3:
      print(self.letter, self.code)

  def letter_and_morse(self):
    self.get_random_letter_and_code()
    
    print(self.letter, self.code)
    repeat_letter_code = input("input the letter and code\n")

    while repeat_letter_code != self.letter + " " + self.code:
      print("try again!")
      repeat_letter_code = input("input the letter and code\n")
      self.user_input_loop()
      
    print("well done!")
    self.morse_msg = self.code
    self.play_sound()

    self.play_again()
    if self.continue_game == "y":
      self.letter_and_morse()


  def random_letter_to_morse(self):
    self.get_random_letter_and_code()
    print(self.letter)
    user_morse = input("insert morse code for this letter\n>>")
  
    while user_morse != self.code:
      print("Wrong! Try again!")
      user_morse = input("insert morse code for this letter\n>>")
      self.user_input_loop()
      
    print("Great Job!")
    self.morse_msg = self.code
    self.play_sound()

    self.play_again()
    if self.continue_game == "y":
      self.random_letter_to_morse()

  def random_morse_to_letter(self):
    self.get_random_letter_and_code()
    print(self.code)
    user_letter = input("insert letter for this morse code:\n>>")

    while user_letter != self.letter:
      print("Wrong! Try again!:")
      user_letter = input("insert letter for this morse code:\n>>")
      self.user_input_loop()

    print("Great Job!")
    self.morse_msg = self.code
    self.play_sound()

    self.play_again()
    if self.continue_game == "y":
      self.random_morse_to_letter()

  def game_selection(self, game_number):
    if game_number == "1":
      self.letter_and_morse()

    elif game_number == "2":
      self.random_letter_to_morse()

    elif game_number == "3":
      self.random_morse_to_letter()

    elif game_number == "0":
      exit() 

    else:
      print("wrong selection! please input 0 to 3")

  def user_game_selection(self):
    while True:
      user_game_input = input("please input 0 to 3:\n>>")
      self.game_selection(user_game_input)

  
if __name__ == "__main__":
  morse_obj = Morse_code()
  morse_obj.user_game_selection()

  #morse_obj.english_to_morse_code()
  #morse_obj.morse_code_to_english()
  #morse_obj.morse_code_learning()
