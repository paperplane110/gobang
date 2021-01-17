'''
Description: 五子棋
version: 
Author: TianyuYuan
Date: 2021-01-17 00:16:16
LastEditors: TianyuYuan
LastEditTime: 2021-01-17 18:31:56
'''
from chess_map import Map
from chesses import Chesses
from comment import intro,game_start,congrats,quit_game

def another_player(player:int) -> int:
    """玩家交换"""
    if player == 1:
        return 2
    else:
        return 1

def format_position(input_str:str) -> list:
    """将输入的字符串坐标格式化，输出list形式的坐标"""
    position = input_str.strip().split(",")
    for i in range(len(position)):
        position[i] = int(position[i])-1
    return position

def game_play(chess_map:Map,chess:Chesses) -> int:
    """游戏过程
    --chess_map:<class Map>
    --chess:<class Chesses>
    --return:胜利玩家编号
    """
    # init
    game_start()
    chess_map.show_map(chess.matrix,chess.p1,chess.p2)
    player = 1

    while True:
        # Wait input
        while True:
            chess_piece = chess.pick_chess(player)
            print("请玩家{}「{}」输入棋子坐标，横纵坐标请用逗号隔开：".format(player,chess_piece))
            position = input()
            if position == "q":
                quit_game()
            if "," not in position:
                print("请用逗号隔开横纵坐标；")
                continue
            position = format_position(position)
            if chess.check_out_of_map(position):
                print("棋子位置超出棋盘范围，请重新落子；")
                continue
            if chess.check_same_position(position):
                break
            else:
                print("该位置已有棋子，请重新输入坐标；")
        chess.refresh_matrix(player,position)
        # show chess
        chess_map.show_map(chess.matrix,chess.p1,chess.p2)
        # check who win
        winner = chess.scan_matrix()
        if winner != 0:
            break
        # take turns
        player = another_player(player)
    return winner

def init_chess() -> (Map,Chesses):
    # 初始化棋盘
    intro()
    while True:
        print("请输入棋盘大小「默认边长15格」")
        length = input()
        if length == "q":
            quit_game()
        elif length == "":
            length = 15
            break
        elif int(length) <= 20:
            length = int(length)
            break
        else:
            print("棋盘有些太大了，只能生成边长小于20的棋盘哦～，请重新输入")
    while True:
        # default chess
        print("想使用默认棋子吗？(y/n)")
        chess_default = input()
        check = chess_default.lower()
        if (check == "y") or (check=="yes"):
            chess_map = Map(length)
            chess = Chesses(length)
            return chess_map,chess
        elif (check == "n") or (check=="no"):
            '''Diy chess'''
            # player1 init
            print("请玩家1输入一个字符作为自己的棋子，若输入'n'，则采用默认棋子")
            p1 = input()
            assert len(p1) == 1, "玩家一：棋子符号必须是一位哦～" 
            # player2 init
            print("请玩家2输入一个字符作为自己的棋子，若输入'n'，则采用默认棋子")
            p2 = input()
            assert len(p2) == 1, "玩家二：棋子符号必须是一位哦～"
            chess_map = Map(length)
            chess = Chesses(length,p1,p2)
            return chess_map,chess
        else:
            print("错误输入，请重新输入是否使用默认棋子(y/n)")

def run():
    while True:
        chess_map,chess = init_chess()
        winner = game_play(chess_map,chess)
        congrats(winner,chess.pick_chess(winner))
        # Another round
        print("希望再玩一局吗？(y/n)")
        another_round = input()
        another_round.lower()
        if (another_round=="no") or (another_round=="n"):
            break
        else:
            print("再来一把！")
    quit_game()

if __name__ == "__main__":
    run()