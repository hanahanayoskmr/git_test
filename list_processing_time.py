"""
内包表記の処理時間計測
処理のみだと内包表記のほうが速いが、printまで処理をいれるとfor文の方が速い
"""

from time import time # 時間計測用
NUM = 10000

start_at = time() # 計測開始
lst = []
for i in range(NUM):
    lst.append(i)
# print(lst)
print("処理時間 ", time() - start_at)

start_at2 = time() # 計測開始
lst = [i for i in range(NUM)]
# print(lst)
print("処理時間 ", time() - start_at2)
