import random # by importing the random library it allows me to create random orders and implement the random.coice function
dice1 = (1,2,3,4,5,6) #I have chosen to get random numbers from a list instead of using the random.int function 
dice2 = (1,2,3,4,5,6)
playagain = True #the playagain variable is used to loop the whole game when the playagain variable is set to true it allows the game to play. At the end of the game the user is given the option to play again or to quit is the user chooses to playagain the variable is left as true and starts the game again, if the user chooses to quit then the playagain variable is set to false and the loop is broken
while playagain == True:
  print("welcome to double hog the aim of the game is to get 100 points first ")
  menu_choice = input("""
would you like to
E: exit
P: play the game
R: see the rules """)
  print("")

  menu_choice = menu_choice.upper() # I used the .upper function so that if the user inputs a lower case letter while the code only accepts upper case letters it will change the letter from lower case to upper case and therefore the code will accept this input
  while 1 == 1: # to make an infinite loop I chose to make a loop where while 1 is equal to 1 so that until the user chooses to play or exit it will keep on looping 
      if menu_choice == "E":
        print("you have chosen to exit the program")
        exit()
      if menu_choice == "P":
        break
      if menu_choice == "R":
        print("""RULES 
  press r to roll and p to pass\nyour score is based on the numbers\n of the dice that you roll\nif you get a double your score will\n be both of the numbers added up and\n then multiplied by two \nyou can keep on going until\n you roll a one this will end your\n turn and the next person will be able\n to roll until they get a turn\nif you roll a one also the total of the\n two dice will be deducted for your score, \notherwise this is the sum of the two dice that \nyou rolled will be added to your score""")
        menu_choice = input("""
would you like to
E: exit
P: play the game
R: see the rules""")
        menu_choice = menu_choice.upper()
      else: # this else statement makes sure that the program does not crash when the user does not input E P or R 
        print("you did not enter a valid letter")
        menu_choice = input("""
would you like to
E: exit
P: play the game
R: see the rules """)
  menu_choice = menu_choice.upper()
  
  
  
  while 1 == 1 : # this creates an infinite loop
    
    players_amount = input("how many players are playing 2,3 or 4 ")# asks the user/s how many people are playing
  
  
    if players_amount == "2":
      print("")
      player1 = input("what is the name of player 1? ")
      while player1 == "":
        print("")
        player1 = input("what is the name of player 1? ")
      print("")  
      player2 = input("what is the name of player 2? ")
      while player2 == "":
        print("")
        player2 = input("what is the name of player 2? ")
        
      break
    if players_amount == "3":
      print("")
      player1 = input("what is the name of player 1? ")
      while player1 == "":
        print("")
        player1 = input("what is the name of player 1? ")
      print("")  
      player2 = input("what is the name of player 2? ")
      while player2 == "":
        print("")
        player2 = input("what is the name of player 2? ")
      print("")  
      player3 = input("what is the name of player 3? ")
      while player3 == "":
        print("")
        player3 = input("what is the name of player 3? ")
      break
    if players_amount == "4":
      player1 = input("what is the name of player 1? ")
      while player1 == "":
        player1 = input("what is the name of player 1? ")
      player2 = input("what is the name of player 2? ")
      while player2 == "":
        player2 = input("what is the name of player 2? ")
      player3 = input("what is the name of player 3? ")
      while player3 == "":
        player3 = input("what is the name of player 3? ")
      player4 = input("what is the name of player 4? ")
      while player4 == "":
        player4 = input("what is the name of player 4? ")
      break
    else: # if the user inputs anything other than 2,3 or 4  the program will ask the user to input a valid number until the user inputs a valid number
      print("please enter 2 3 or 4 ")
      players_amount = input("how many players are playing ")
  
  
  if players_amount == "2":# this if statement randomly shuffles the order of the players by using the .shuffle function
    order = [player1, player2]
    random.shuffle(order)
    player1 = order[0]
    player2 = order[1]
    print("")
    print ("the order is ",order[0],",",order[1])
  
  elif players_amount == "3":# this if statement randomly shuffles the order of the players by using the .shuffle function
    order = [player1, player2, player3]
    random.shuffle(order)
    print("")
    print ("the order is ",order[0],",",order[1],",",order[2]) 
  elif players_amount == "4":# this if statement randomly shuffles the order of the players by using the .shuffle function
    order = [player1, player2, player3, player4]
    random.shuffle(order)
    print("")
    print ("the order is ",order[0],",",order[1],",",order[2],",",order[3])
    #i did not need an else statement here because I already have a else statement which makes sure that the correct value is inputted
  p1score = 0 # these lines of code set all of the players scores to 0 so that if the game is started again no one gets an advantage by starting from a higher number
  p2score = 0
  p3score = 0
  p4score = 0
  
  
  
  
  turn = 1
  player_number = len(order)#this line checks to see how many people are playing by looking at the length of the list created when asking how many people are playing and sets the variable player number to what ever the amount of players there are
  if player_number == 2:
    while p1score < 100 and p2score < 100:
        if turn == 1:
          print("")
          print("it is " + order[0] +"'s turn")#this says who's turn it is
          print("score " , p1score) #this prints out the first players score
          print("")
          passorroll = str(input(order[0]+" would you like to pass:P or roll:R "))
          passorroll = passorroll.upper()
          
          if passorroll == "P" :
            print("")
            print(order[0],"has decided to pass")
            
            diceone= 0 # I set diceone and dicetwo to zero because once this line of code has been read the scoring procedure is still implemented, this means that it will check to see if the numbers are the same, two ones, a single one or different and will add the results onto the players score, so by setting dice one and dicetwo to zero the scores will not be affected in a positive or negative way
            dicetwo= 0 
            turn = 2
            
          elif passorroll == "R" :
            diceone=random.choice(dice1) # this refers back to the list that I made earlier with 1,2,3,4,5 and 6 it chooses a random number from this list 
            dicetwo=random.choice(dice2)
            print("")
            print(dicetwo,diceone)
            #scoring part
          else: # this checks makes sure that the user inputs the correct letter and if they don't it will ask the question again
            passorroll = str(input(order[0]+" would you like to pass:P or roll:R "))
            passorroll = passorroll.upper()
            continue # the continue function makes the loop start again from the top 
          if diceone == 1 and dicetwo == 1:
            dicescore = 25
            p1score = dicescore + p1score
            print(p1score)
          elif passorroll =="R" and diceone == 1 or dicetwo == 1 :
            dicescore = -1*(diceone + dicetwo) # by multiplying any number by -1 it will automatically turn that number into a negative 
            p1score = dicescore + p1score # this adds the negative number to the players score
            print("")
            print("score ",p1score)
            print("oh no, you got a 1 it is", player2, "'s turn")
            turn = 2 # by changing the turn variable to 2 it makes it the next players turn
            
          elif diceone == dicetwo :
            dicescore = 2*(diceone + dicetwo)# by putting the two variables dice one and dicetwo inside the brackets it allows the score to be multiplied by the sum of the two variables instead of having to multiply them individually 
            
            p1score= dicescore + p1score
          
          else: # this code only executes if none of the above conditions are met
            dicescore = diceone + dicetwo
            p1score = dicescore + p1score
        elif turn == 2:
            while p1score < 100 and p2score < 100:
              if turn == 2:
                print("it is " + order[1] +"'s turn")
                print("score " , p2score) 
                passorroll = str(input(order[1]+" would you like to pass:P or roll:R "))
                print("")
                passorroll = passorroll.upper()
                if passorroll == ("P") :
                  print(order[1],"has decided to pass")
                  
                  diceone= 0 
                  dicetwo= 0 # I set diceone and dicetwo to zero because once this line of code has been read the scoring procedure is still implemented, this means that it will check to see if the numbers are the same, two ones, a single one or different and will add the results onto the players score, so by setting dice one and dicetwo to zero the scores will not be affected in a positive or negative way
                  turn = 1
                  break
                elif passorroll == "R" :
                  diceone=random.choice(dice1)# this refers back to the list that i made earlier with 1,2,3,4,5 and 6 it chooses a random number from this list
                  dicetwo=random.choice(dice2)
                  print(diceone,dicetwo)
                  
                  
                  #scoring part
                else:
                  passorroll = str(input(order[1]+" would you like to pass:P or roll:R "))
                  print("")
                  passorroll = passorroll.upper()
                  continue
                if diceone == 1 and dicetwo == 1:
                  dicescore = 25
                  p2score = dicescore + p2score
                  print(p2score)
                elif diceone == 1 or dicetwo == 1 and passorroll =="R":
                  dicescore = -1*(diceone + dicetwo)
                  p2score = dicescore + p2score
                  print("")
                  print("score ",p2score)
                  print("oh no you got a 1 it is", player1, "'s turn")# by changing the turn variable to 2 it makes it the next players turn
                  turn = 1
                  break
                elif diceone == dicetwo:
                  dicescore = 2*(diceone + dicetwo)
                  
                  p2score= dicescore + p2score
                elif diceone == 1 and dicetwo == 1:
                  dicescore = 25
                  p2score = dicescore + p2score
                  print(p2score)
                else:
                  dicescore = diceone + dicetwo
                  p2score = dicescore + p2score
        continue

  

  turn = 1
  player_number = len(order)#this line checks to see how many people are playing by looking at the length of the list created when asking how many people are playing and sets the variable player number to what ever the amount of players there are
  if player_number == 3:
    while p1score < 100 and p2score < 100 and p3score <100: #this will automatically start the loop because i have already set p1 ,p2 and p3 scores to zero
        if turn == 1:
          
          print("it is " + order[0] +"'s turn")
          print("score " , p1score) 
          passorroll = str(input(order[0]+" would you like to pass:P or roll:R "))
          passorroll = passorroll.upper()
          if passorroll == ("P") :
            print("player1 has decided to pass")
            turn = 2
            diceone= 0
            dicetwo= 0 # I set diceone and dicetwo to zero because once this line of code has been read the scoring procedure is still implemented, this means that it will check to see if the numbers are the same, two ones, a single one or different and will add the results onto the players score, so by setting dice one and dicetwo to zero the scores will not be affected in a positive or negative way
          elif passorroll == "R" :
            diceone=random.choice(dice1)
            dicetwo=random.choice(dice2)# this refers back to the list that i made earlier with 1,2,3,4,5 and 6 it chooses a random number from this list
            print(diceone,dicetwo)
          else:
            passorroll = str(input(order[0]+" would you like to pass:P or roll:R "))
            passorroll = passorroll.upper()
            continue
          if diceone == 1 and dicetwo == 1:
            dicescore = 25
            p1score = dicescore + p1score
            print(p1score)
            #scoring part
          elif diceone == 1 or dicetwo == 1 and diceone != dicetwo:
            dicescore = -1*(diceone + dicetwo)# by multiplying any number by -1 it will automatically turn that number into a negative 
            p1score = dicescore + p1score
            print("oh no, you got a 1 it is", player2, "'s turn")
            turn = 2 # by changing the turn variable to 2 it makes it the next players turn
          elif diceone == dicetwo:
            dicescore = 2*(diceone + dicetwo)
            print("score")
            p1score= dicescore + p1score

          else:
            dicescore = diceone + dicetwo
            p1score = dicescore + p1score
        elif turn == 2:
            while p1score < 100 and p2score < 100 and p3score < 100:
              if turn == 2:
                print("it is " + order[1] +"'s turn")
                print("score " , p2score) 
                passorroll = str(input(order[1]+" would you like to pass:P or roll:R "))
                passorroll = passorroll.upper()
                if passorroll == ("P") :
                  print("player2 has decided to pass")
                  diceone= 0 
                  dicetwo= 0 
                  turn = 3 
                  break# I set diceone and dicetwo to zero because once this line of code has been read the scoring procedure is still implemented, this means that it will check to see if the numbers are the same, two ones, a single one or different and will add the results onto the players score, so by setting dice one and dicetwo to zero the scores will not be affected in a positive or negative way
                elif passorroll == "R" :
                  diceone=random.choice(dice1)
                  print(diceone)
                  dicetwo=random.choice(dice2)
                  print(dicetwo)
                else:
                  passorroll = str(input(order[1]+" would you like to pass:P or roll:R "))
                  passorroll = passorroll.upper()
                  continue
                  #scoring part
                if diceone == 1 and dicetwo == 1:
                  dicescore = 25
                  p2score = dicescore + p2score
                  print(p2score)
                elif diceone == 1 or dicetwo == 1 and diceone != dicetwo:
                  dicescore = -1*(diceone + dicetwo)
                  p2score = dicescore + p2score
                  print("oh no you got a 1 it is", player3, "'s turn")
                  turn = 3
                  break
                elif diceone == dicetwo:
                  dicescore = 2*(diceone + dicetwo)
                  print("score")
                  p2score= dicescore + p2score

                else:
                  dicescore = diceone + dicetwo
                  p2score = dicescore + p2score
        elif turn == 3:
            while p1score < 100 and p2score < 100 and p3score < 100:
              if turn == 3:
                print("it is " + order[2] +"'s turn")
              print("score " , p3score) 
              passorroll = str(input(order[2]+" would you like to pass:P or roll:R "))
              passorroll = passorroll.upper()
              if passorroll == ("P") :
                print("player3 has decided to pass")
                diceone= 0 
                dicetwo= 0
                turn = 1 
                break# I set diceone and dicetwo to zero because once this line of code has been read the scoring procedure is still implemented, this means that it will check to see if the numbers are the same, two ones, a single one or different and will add the results onto the players score, so by setting dice one and dicetwo to zero the scores will not be affected in a positive or negative way
              elif passorroll == "R" :
                diceone=random.choice(dice1)
                dicetwo=random.choice(dice2)
                print(diceone,dicetwo)# this refers back to the list that i made earlier with 1,2,3,4,5 and 6 it chooses a random number from this list
              else:
                passorroll = str(input(order[2]+" would you like to pass:P or roll:R "))
                passorroll = passorroll.upper()
                continue
                #scoring part
              if diceone == 1 and dicetwo == 1:
                dicescore = 25
                p3score = dicescore + p3score
                print(p3score)
              elif diceone == 1 or dicetwo == 1 and diceone != dicetwo:
                dicescore = -1*(diceone + dicetwo)
                p3score = dicescore + p3score
                print("oh no you got a 1 it is", player1, "'s turn")
                turn = 1
                break
              elif diceone == dicetwo:
                dicescore = 2*(diceone + dicetwo)
                print("score")
                p3score= dicescore + p3score
              elif diceone == 1 and dicetwo == 1:
                dicescore = 25
                p3score = dicescore + p3score
                print(p3score)
              else:
                dicescore = diceone + dicetwo
                p3score = dicescore + p3score
              continue

  
  turn = 1
  player_number = len(order)#this line checks to see how many people are playing by looking at the length of the list created when asking how many people are playing and sets the variable player number to whatever the amount of players there are
  if player_number == 4:
    while p1score < 100 and p2score < 100 and p3score < 100 and p4score < 100: #this will automatically start the loop because I have already set p1 ,p2 ,p3 and p4 scores to zero
        if turn == 1:
          
          print("it is " + order[0] +"'s turn")
          print("score " , p1score) 
          passorroll = str(input(order[0]+" would you like to pass:P or roll:R "))
          passorroll = passorroll.upper()
          if passorroll == ("P") :
            print("player1 has decided to pass")
            
            diceone= 0 
            dicetwo= 0
            turn = 2 
            # I set diceone and dicetwo to zero because once this line of code has been read the scoring procedure is still implemented, this means that it will check to see if the numbers are the same, two ones, a single one or different and will add the results onto the players score, so by setting dice one and dicetwo to zero the scores will not be affected in a positive or negative way
          elif passorroll == "R" :
            diceone=random.choice(dice1)
            print(diceone)
            dicetwo=random.choice(dice2)
            print(dicetwo)
          else:
            passorroll = str(input(order[0]+" would you like to pass:P or roll:R "))
            passorroll = passorroll.upper()
            continue
            #scoring part
          if diceone == 1 and dicetwo == 1:
            dicescore = 25
            p1score = dicescore + p1score
            print(p1score)
          elif diceone == 1 or dicetwo == 1 and diceone != dicetwo:
            dicescore = -1*(diceone + dicetwo)
            p1score = dicescore + p1score
            print("oh no, you got a 1 it is", order[1], "'s turn")
            turn = 2
          elif diceone == dicetwo:
            dicescore = 2*(diceone + dicetwo)
            print("score")
            p1score= dicescore + p1score
          
          else:
            dicescore = diceone + dicetwo
            p1score = dicescore + p1score
        elif turn == 2:
            while p1score < 100 and p2score < 100 and p3score < 100:
              if turn == 2:
                print("it is " + order[1] +"'s turn")
                print("score " , p2score) 
                passorroll = str(input(order[1]+" would you like to pass:P or roll:R "))
                passorroll = passorroll.upper()
                if passorroll == ("P") :
                  print("player2 has decided to pass")
                  diceone= 0 
                  dicetwo= 0
                  turn = 3 
                  break# I set diceone and dicetwo to zero because once this line of code has been read the scoring procedure is still implemented, this means that it will check to see if the numbers are the same, two ones, a single one or different and will add the results onto the players score, so by setting dice one and dicetwo to zero the scores will not be affected in a positive or negative way
                elif passorroll == "R" :
                  diceone=random.choice(dice1)
                  print(diceone)
                  dicetwo=random.choice(dice2)
                  print(dicetwo)
                else:
                  passorroll = str(input(order[1]+" would you like to pass:P or roll:R "))
                  passorroll = passorroll.upper()
                  continue
                  #scoring part
                if diceone == 1 and dicetwo == 1:
                  dicescore = 25
                  p2score = dicescore + p2score
                  print(p2score)
                elif diceone == 1 or dicetwo == 1 and diceone != dicetwo:
                  dicescore = -1*(diceone + dicetwo)
                  p2score = dicescore + p2score
                  print("oh no you got a 1 it is", order[2], "'s turn")
                  turn = 3
                  break
                elif diceone == dicetwo:
                  dicescore = 2*(diceone + dicetwo)
                  print("score")
                  p2score= dicescore + p2score
                
                else:
                  dicescore = diceone + dicetwo
                  p2score = dicescore + p2score
        elif turn == 3:
            while p1score < 100 and p2score < 100 and p3score < 100:
              if turn == 3:
                print("it is " + order[2] +"'s turn")
              print("score " , p3score) 
              passorroll = str(input(order[2]+" would you like to pass:P or roll:R "))
              passorroll = passorroll.upper()
              if passorroll == ("P") :
                print("player3 has decided to pass")
                diceone= 0 
                dicetwo= 0 
                turn = 4
                break
              elif passorroll == "R" :
                diceone=random.choice(dice1)
                print(diceone)
                dicetwo=random.choice(dice2)
                print(dicetwo)
              else:
                passorroll = str(input(order[2]+" would you like to pass:P or roll:R "))
                passorroll = passorroll.upper()
                continue
                #scoring part
              if diceone == 1 and dicetwo == 1:
                dicescore = 25
                p3score = dicescore + p3score
                print(p3score)
              elif diceone == 1 or dicetwo == 1 and diceone != dicetwo:
                dicescore = -1*(diceone + dicetwo)
                p3score = dicescore + p3score
                print("oh no you got a 1 it is", order[3], "'s turn")
                turn = 4
                break
              elif diceone == dicetwo:
                dicescore = 2*(diceone + dicetwo)
                print("score")
                p3score= dicescore + p3score
              elif diceone == 1 and dicetwo == 1:
                dicescore = 25
                p3score = dicescore + p3score
                print(p3score)
              else:
                dicescore = diceone + dicetwo
                p3score = dicescore + p3score
        elif turn == 4:
            while p1score < 100 and p2score < 100 and p3score < 100 and p4score < 100:
              if turn == 4:
                print("it is " + order[3] +"'s turn")
              print("score " , p4score) 
              passorroll = str(input(order[3]+" would you like to pass:P or roll:R "))
              passorroll = passorroll.upper()
              if passorroll == ("P") :
                print("player4 has decided to pass")
                diceone= 0 
                dicetwo= 0 
                turn = 1 
                break# I set diceone and dicetwo to zero because once this line of code has been read the scoring procedure is still implemented, this means that it will check to see if the numbers are the same, two ones, a single one or different and will add the results onto the players score, so by setting dice one and dicetwo to zero the scores will not be affected in a positive or negative way
              elif passorroll == "R" :
                diceone=random.choice(dice1)
                dicetwo=random.choice(dice2)
                print(diceone,dicetwo)
                
                
              else:
                passorroll = str(input(order[3]+" would you like to pass:P or roll:R "))
                passorroll = passorroll.upper()
                continue
                #scoring part
              if diceone == 1 and dicetwo == 1:
                dicescore = 25
                p4score = dicescore + p4score
                print(p4score)
              elif diceone == 1 or dicetwo == 1 and diceone != dicetwo:
                dicescore = -1*(diceone + dicetwo)
                p4score = dicescore + p4score 
                print("oh no you got a 1 it is", order[0], "'s turn")
                turn = 1
                break
              elif diceone == dicetwo:
                dicescore = 2*(diceone + dicetwo)
                print("score")
                p4score= dicescore + p4score
              
              else:
                dicescore = diceone + dicetwo
                p4score = dicescore + p4score
              continue
  if p1score > 100:
    print(order[0]," wins")
  elif p2score > 100:
    print(order[1]," wins")
  elif p3score > 100:
    print(order[2]," wins")
  elif p4score > 100:
    print(order[3]," wins")
    
  if p1score > 100 or p2score > 100 or p3score > 100 or p4score > 100:
    playagain=input("would you like to play again? yes or no ")
    if playagain == "yes":
      print("you have chosen to play again\n")  
      playagain = True
    
    else:
      print("you have chosen not to play again")
      playagain = False
