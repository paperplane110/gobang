# gobang--五子棋
可以在终端上和朋友一起玩的五子棋！
A little Gobang game running in terminal where you can play it with your friend!
## How to play
Open your terminal and `cd` to a dir which you feel convenient
```bash
git clone https://github.com/paperplane110/gobang.git
python3 gobang.py
```
Start the game!
### gobang.py
All game play methods have been stored in this file. It tells the order of the players' action and when to quit the game. It is the main body of the game.
### chess_map.py
Defined the map of the gobang. Containing the method of how to print the map.
### chesses.py
Defined the chesses appearence, location and check who is the winner.
### comment.py
Some hints and greeting shown in prompt.
