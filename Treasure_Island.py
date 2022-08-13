print('''
     .... NO! ...                  ... MNO! ...
   ..... MNO!! ...................... MNNOO! ...
 ..... MMNO! ......................... MNNOO!! .
..... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .
 ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....
    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...
   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....
   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...
    ....... MMMMM..    OPPMMP    .,OMI! ....
     ...... MMMM::   o.,OPMP,.o   ::I!! ...
         .... NNM:::.,,OOPM!P,.::::!! ....
          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....
         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....
           .. MMMMMNNOOMMNNIIIPPPOO!! ......
          ...... MMMONNMMNNNIIIOO!..........
       ....... MN MOMMMNNNIIIIIO! OO ..........
    ......... MNO! IiiiiiiiiiiiI OOOO ...........
  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........
   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........
   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........
      ...... OO! ................. ON! .......
         ................................
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n').lower()
if choice1 == 'left':
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
  if choice2 == 'wait':
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n").lower()
    if choice3 == 'red':
      print('''

               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
 jgs^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^      
      ''')
      print("It's a room full of fire. Game Over.\n")
    elif choice3 == 'yellow':
      print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
      ''')
      print("\n\nYou found the treasure! You Win!\n")
    else:
      print('''

                                    ___---|
                                   /::::::|
                                  /:::::::|
                                 /`------'|__
                           ___..:::......::::---,
                           \::::::::::::::::::/'
                              \::--::--::-r'
                                |  X      |
                                | ___     /
                                 \     _-'
             ___booooo________ooo-/~~~~ _\00ooo_________ooooood___
            ////88888888888888888'_/_||_\888888888888888888888\\\\\
           /////8888888888888888888888888888888888888888888888\\\\\\
          //////8888"""888888""8888888888888888""888888""""888\\\\\\\
          ||||| 87              88888888888887              "8 ||||||
           |||  7               8888888888888                V  ||||
            V                  d8888888888888                    ||
                               88888888888888                    /
                               888888888888888
                              88888888888888888
                               `8888888888888'
                                 MMMMMMMMMMMm
                                MMMMMMMMMMMMMM
                                MMMMMMMMMMMMMM
                                MMMMMMMMMMMMMM
                                `MMMMMM|MMMMMM
                                 MMMMMM|MMMMM
                                 MMMMMM|MMMMM
                                 MMMMMM|MMMMM
                                 MMMMMM|MMMMM
                                 MMMMMM/MMMMM
                                 MMMMMM\MMMMM
                                MMMMMMMM|MMMM
                                MMMMMMMM|MMMMM
                                `MMMMM'MMMMMM'
                                /MMMMM`MMMM'
                                ///||\/MMMMM\
                               ///|||\\//||\\
                               ||||||||//||\\\
                               |||||||||||||||
                                |||||| ||||||
                                 ||||   ||||
                                        ||
      ''')
      print("You enter a room of toys. Game Over.\n")
  else:
    print('''

                                (()))
                               /|x x|
                              /\( - )
                      ___.-._/\/
                     /=`_'-'-'/  !!
                     |-{-_-_-}     !
                     (-{-_-_-}    !
                      \{_-_-_}   !
                       }-_-_-}
                       {-_|-_}
                       {-_|_-}
                       {_-|-_}
                       {_-|-_}  ZOT
                   ____%%@ @%%_______
  ''')
    print("You get eaten by a swamp monster. Game Over!!\n")
    
else:
  print('''
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;-' ___      '-;;;;;;;;;;;;;;;;
;;;;;;;;;;;;-'    `'-.`'-.      '-;;;;;;;;;;;;
;;;;;;;;;;'           )   `\       ';;;;;;;;;;
;;;;;;;;'            /      \   ^V^  ';;;;;;;;
;;;;;;;           __/________\__       ;;;;;;;
;;;;;;  ^V^      '--/}}}}}}"}}--'       ;;;;;;
;;;;;              {{{{{{  aa\__         ;;;;;
;;;;;              }}}}} ,___ __}        ;;;;;
;;;;;             {{{{{\  \_//           ;;;;;
;;;;;              }}}}//'--u            ;;;;;
;;;;;        _     .--'`U\               ;;;;;
;;;;;   ::::| \   (   _,\\\              ;;;;;
;;;;;;  ::::|  |===\  \\=\))=======D    ;;;;;;
;;;;;;; ::::|_/     `> \\              ;;;;;;;
;;;;;;;;.           /__//            .;;;;;;;;
;;;;;;;;;;.         Y\_\\_         .;;;;;;;;;;
;;;;;;;;;;;;-._                _.-;;;;;;;;;;;;
;;;;;;;jgs;;;;;;-.          .-;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

''')
  print("Right was wrong. Game Over!!\n")

