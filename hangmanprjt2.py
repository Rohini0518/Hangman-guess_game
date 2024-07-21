import random
import hmascilkeys
from hngmanwords import word_list
# guess the word problem
words=["rohini", "program", "birthday"]
print(hmascilkeys.logo)
selected_word=random.choice(word_list)
print(selected_word)
display=[]
display2=[]   
count1=len(selected_word)
print(count1)
for gme in selected_word:
    display.append("_")
    display2.append(gme)
print(display)
lives=7 
# def guessing():
#     guessd_letter=input("guess a letter: ")
#     for rho in range(count1):
#         letter=selected_word[rho]
#         if letter==guessd_letter:
#             display[rho]=guessd_letter
#             print(display) 
#         elif letter!=guessd_letter: 
#             lives-=1
            
                
    # print(display) 
end_of_game=False
while not end_of_game:   
   guessd_letter=input("guess a letter: ")
   for rho in range(count1):
       letter=selected_word[rho]
       if letter==guessd_letter:
            display[rho]=guessd_letter
            print(display) 
   if guessd_letter in display:
       print(f"you already guessed {guessd_letter} ")         
   if not guessd_letter in selected_word: 
        lives-=1 
        print("you have ",lives,"chances")
        print(hmascilkeys.stages[lives])
        if lives==0:
            print("your lives are completed")
            end_of_game=True
   if not "_" in display:
        end_of_game=True
 


    
 