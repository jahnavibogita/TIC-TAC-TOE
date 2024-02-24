import os
import sys
import time
board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player=1
Win=1
Draw=-1
Running=0
Stop=1
Game=Running
Mark='X'
#to draw the game board
def DrawBoard():
  print("%c | %c | %c "%(board[1],board[2],board[3]))
  print("___|___|___")
  print("%c | %c | %c "%(board[4],board[5],board[6]))
  print("___|___|___")
  print("%c | %c | %c "%(board[7],board[8],board[9]))
#to check the position if it is empty or not
def CheckPosition(x):
  if(board[x]==' '):
    return True
  else:
    return False
#to check if player won or not
def CheckWin():
  global Game
  #horizontal check
  if(board[1]==board[2] and board[2]==board[3] and board[1]!=' '):
    Game=Win
  elif(board[4]==board[5] and board[5]==board[6] and board[4]!=' '):
    Game=Win
  elif(board[7]==board[8] and board[8]==board[9] and board[7]!=' '):
    Game=Win
  #vertical check
  elif(board[1]==board[4] and board[4]==board[7] and board[1]!=' '):
    Game=Win
  elif(board[2]==board[5] and board[5]==board[8] and board[2]!=' '):
    Game=Win
  elif(board[3]==board[6] and board[6]==board[9] and board[3]!=' '):
    Game=Win
  #diagonal check
  elif(board[1]==board[5] and board[5]==board[9] and board[5]!=' '):
    Game=Win
  elif(board[3]==board[5] and board[5]==board[7] and board[5]!=' '):
    Game=Win
  #draw match check
  elif(board[1]!=' '  and  board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' '  and board[8]!=' ' and board[9]!=' '):
    Game=Draw
  else:
    Game=Running
print("Tic-Tac-Toe Game")
print("Player 1 [X] --- Player 2[0]\n")
print()
print()
print("Please wait...")
time.sleep(3)
while(Game==Running):
  os.system('cls')
  DrawBoard()
  if(player%2!=0):
    print("Player 1's chance")
    Mark='X'
  else:
    print("Player 2's chance")
    Mark='O'
  choice=int(input("enter the position between [1-9] where you wanna mark:"))
  if(CheckPosition(choice)):
    board[choice]=Mark
    player+=1
    CheckWin()
os.system('cls')
DrawBoard()
if(Game==Draw):
  print("Game is draw")
elif(Game==Win):
  player-=1
  if(player%2!=0):
    print("player 1 won")
  else:
    print("player 2 won")

try:
  DrawBoard()
except IndexError as e:
  # Print the error message
  print(f"Error: {e}")
    # Print the traceback
  print(sys.exc_info()[2])