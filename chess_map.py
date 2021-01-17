'''
Description: 类：五子棋的棋盘
*version: 
*Author: TianyuYuan
*Date: 2021-01-17 04:05:51
LastEditors: TianyuYuan
LastEditTime: 2021-01-17 13:20:34
'''
class Map():
    '''五子棋的棋盘'''

    def __init__(self,length=20):
        '''棋盘的边长'''
        self.length = length 

        # Graph setting
        self.space = "-+-"

    def print_row(self,chesses_matrix:list,p1:str,p2:str) -> str:
        """
        打印棋盘上会放置棋子的一行
        --map_row：这一行每个位置的值
        """
        row = str()
        for i in range(self.length):
            if chesses_matrix[i] == 0:
                pattern = self.space
            elif chesses_matrix[i] == 1:
                pattern = p1
            elif chesses_matrix[i] == 2:
                pattern = p2
            else:
                print("Warning: Wrong piece num in matrix!")
            if i < self.length-1:
                row = row + pattern + "--"
            else:
                row = row + pattern
        return row
            
    def print_interval_row(self) -> str:
        """打印行间空隙"""
        row = str()
        for i in range(self.length):
            if i == 0:
                row = row + " |    "
            elif i < self.length-1:
                row = row + "|    "
            else:
                row = row + "|"   # 行尾情况
        return row

    def print_title_row(self) -> str:
        """打印漂亮的棋盘的表头"""
        row = str()
        for i in range(self.length):
            row_key = "%.2d"%(i+1)
            if i == 0:
                row = row + "  " + row_key + "   "
            elif i < self.length-1:
                row = row + row_key + "   "
            else:
                row = row + row_key   # 行尾情况
        return row

    def show_map(self,chesses_matrix,p1,p2):
        # 打印表头行
        title_row = self.print_title_row()
        print(title_row)
        # 打印棋盘
        for r in range(self.length):
            row_key = "%.2d"%(r+1)
            null_key = "  "
            if r < self.length-1:
                # 不是最后一行，需要打印空隙行
                row = row_key + self.print_row(chesses_matrix[r],p1,p2)
                print(row)
                row = null_key + self.print_interval_row()
                print(row)
            else:
                # 最后一行，无需打印空隙行
                row = row_key + self.print_row(chesses_matrix[r],p1,p2)
                print(row)
