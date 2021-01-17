'''
Description: 定义了一些展示提示语的方法
version: 
Author: TianyuYuan
Date: 2021-01-17 11:53:28
LastEditors: TianyuYuan
LastEditTime: 2021-01-17 18:34:10
'''
def intro():
    print("##############################")
    print("###---------五子棋---------###")
    print("##############################")
    print("\033[1;32m ---Programmed @ TianyuYuan--- \033[0m")
    print("\n")
    print("\033[1;32m->规则提示：\033[0m \
                \n--胜利条件：一方棋子连成五子即胜利 \
                \n--定义棋盘大小：棋盘边长应大于5且小于25 \
                \n--自定义棋子符号：一个字符的符号（也可使用默认棋子）\
                \n--如何下棋：输入行号列号，并用逗号隔开 \
                \n--退出游戏：输入‘q’即可退出游戏\n")

def game_start():
    print("##############################")
    print("###-------!游戏开始!-------###")
    print("##############################")
    print("\n")  

def congrats(winner:int,chess_piece:str):
    print("\n\033[32m \
        #############################\n \
        >>>>>>CONGRATULATIONS!!!<<<<<\n \
        #############################\033[0m\n")
    print("\033[32m \
        >>>>玩家「{}」赢得了比赛！<<<<\n \
        >>>>冠军的棋子：「{}」  <<<<\033[0m\n".format(winner,chess_piece))

def quit_game():
    print("-> 退出游戏")
    print("\033[32m\
-> 感谢您玩这款游戏！:)\n\
-> Hope you have a nice day!\n\
-> <五子棋 Terminal version> Programmed by Tianyu with love!\033[0m")
    exit()