'''
Description: Class Chesses
version: 
Author: TianyuYuan
Date: 2021-01-17 12:55:11
LastEditors: TianyuYuan
LastEditTime: 2021-01-17 18:31:03
'''
class Chesses():
    def __init__(self,length,p1="@",p2="&"):
        self.length = length
        self.matrix = []
        self.origin_matrix()
        # Graph setting the looking of chess_piece
        self.p1 = "\033[1;36m({})\033[0m".format(p1)
        self.p2 = "\033[1;31m({})\033[0m".format(p2)

    def origin_matrix(self) -> list:
        """
        初始化棋盘的矩阵，任何棋子的位置用它在矩阵中的检索号来表达。
        --棋盘上所有位置初始化的值为：0
        --白棋子的值为：1
        --黑棋子的值为：2
        --e.g. self.matrix[0][1] = 0 棋盘第一行第二列为空
        --e.g. self.matrix[1][2] = 1 棋盘第二行第三列为白棋
        """
        for i in range(self.length):
            self.matrix.append([])
            for j in range(self.length):
                self.matrix[i].append(0)

    def refresh_matrix(self,player:int,position:list):
        """
        更新棋盘矩阵
        --player: 玩家编号
        --position: 棋子坐标
        """
        assert isinstance(player,int), "Error: Wrong type of player in refresh_matrix method!"
        row = position[0]
        column = position[1]
        self.matrix[row][column] = player

    def check_same_position(self,position:list) -> bool:
        """
        检查该位置是否已经存在棋子
        --position:输入棋子位置
        --return:不存在棋子True，已经存在棋子False
        """ 
        row = position[0]
        column = position[1]   
        if self.matrix[row][column] == 0: # empty postion
            return True
        else:
            return False

    def check_out_of_map(self,position:list) -> bool:
        """
        检查棋子是否落在棋盘外
        --outside:True
        --inside:False
        """
        l = self.length-1
        row = position[0]
        column = position[1]
        #print(row,column)
        if (row>l) or (row<0) or (column>l) or (column<0):
            #print("T")
            return True
        else: 
            #print("F")
            return False

    def list_horizon(self,row:int,column:int) -> list:
        """返回以（row，column）开始，水平向右五个格子棋子的列表"""
        chess_list = []
        for i in range(5):
            chess_list.append(self.matrix[row][column+i])
        return chess_list
    
    def list_vertical(self,row:int,column:int) -> list:
        """返回以（row，column）开始，竖直向下五个格子棋子的列表"""
        chess_list = []
        for i in range(5):
            chess_list.append(self.matrix[row+i][column])
        return chess_list

    def list_southeast(self,row:int,column:int) -> list:
        """返回以（row，column）开始，右下朝向五个格子棋子的列表"""
        chess_list = []
        for i in range(5):
            chess_list.append(self.matrix[row+i][column+i])
        return chess_list

    def list_southwest(self,row:int,column:int) -> list:
        """返回以（row，column）开始，左下朝向五个格子棋子的列表"""
        chess_list = []
        for i in range(5):
            chess_list.append(self.matrix[row+i][column-i])
        return chess_list
    
    def scan_matrix(self) -> int:
        """扫描四遍，横、纵、右下、左下，返回赢家编号或者0"""
        def who_is_winner(chess_list) -> int:
            """return the num of winner 1,2 or 0"""
            if 0 in chess_list:
                return 0 
            elif sum(chess_list) == 5:
                return 1
            elif sum(chess_list) == 10:
                return 2
            else:
                return 0 
        # 横向扫描，划定范围
        for row in range(self.length):
            for column in range(self.length-4):
                chess_list = self.list_horizon(row,column)
                result = who_is_winner(chess_list)
                if result != 0:
                    return result
                else:
                    continue
        # 纵线扫描，划定范围
        for row in range(self.length-4):
            for column in range(self.length):
                chess_list = self.list_vertical(row,column)
                result = who_is_winner(chess_list)
                if result != 0:
                    return result
                else:
                    continue
        for row in range(self.length-4):
            for column in range(self.length-4):
                chess_list = self.list_southeast(row,column)
                result = who_is_winner(chess_list)
                if result != 0:
                    return result
                else:
                    continue
        for row in range(self.length-4):
            for column in range(4,self.length):
                chess_list = self.list_southwest(row,column)
                result = who_is_winner(chess_list)
                if result != 0:
                    return result
                else:
                    continue
        return 0

    def pick_chess(self,player:int) -> str:
        if player == 1:
            return self.p1
        else:
            return self.p2




##### Trash code #####
    # def check_win(self) -> int:
    #     """
    #     一个棋子要赢，从四个方向上去看，每个方向上棋子的顺位有五种；
    #     特殊情况：每个方向上可能遇到棋盘边界，可能遇到空位，可能遇到其他棋子
    #     --self: 检查棋盘上的每一个棋子
    #     --return: piece == winner
    #     """
    #     def check_out_of_map(position:list) -> bool:
    #         """outside:True; inside:False"""
    #         l = self.length-1
    #         row = position[0]
    #         column = position[1]
    #         if (row>l) or (row<0) or (column>l) or (column<0):
    #             return True
    #         else: 
    #             return False

    #     def check_diff_piece(position,piece):
    #         """diff from center:True; same as center: False"""
    #         row = position[0]
    #         column = position[1]
    #         tmp_piece = self.matrix[row][column]
    #         if tmp_piece != piece:
    #             return True
    #         else:
    #             return False

    #     def check_piece(i,j) -> bool:
    #         piece = self.matrix[i][j]
    #         sum_piece = {"horizon":[],"vertical":[],"northeast":[],"northwest":[]}
    #         octo_pos = {
    #             "pos_1":[i-dist,j-dist],
    #             "pos_2":[i-dist,j],
    #             "pos_3":[i-dist,j+dist],
    #             "pos_4":[i,j-dist],
    #             "pos_5":[i,j+dist],
    #             "pos_6":[i+dist,j-dist],
    #             "pos_7":[i+dist,j],
    #             "pos_8":[i+dist,j+dist]
    #             }
    #         for d in range(4):
    #             dist = d+1
    #             for pos in octo_pos:
    #                 """"""
    #                 # 先检查所有方向是否已经有五子
    #                 for direction in sum_piece:
    #                     if len(sum_piece[direction]) >= 5:
    #                         return True
    #                     else:
    #                         continue
    #                 if len(octo_pos) == 0:
    #                     # 所有方向没有五子，且所有方向没有相同棋子的可能了，跳出循环
    #                     break
    #                 if check_out_of_map(octo_pos[pos]):
    #                     del octo_pos[pos]
    #                 elif check_diff_piece(octo_pos[pos],piece):
    #                     del octo_pos[pos]
    #                 else:
    #                     """添加到sum_piece中"""

    #         return False
    #     # main        
    #     for i in range(self.length):
    #         for j in range(self.length):
    #             piece = self.matrix[i][j]
    #             if piece != 0:
    #                 if check_piece(i,j):
    #                     return piece
    #             else:
    #                 continue