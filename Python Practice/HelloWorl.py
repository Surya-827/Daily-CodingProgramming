# """
# Project{
#     Package / Directory {
#         File {
#             Class{
#                 Methods / Functions{
#                         logics {
#                             Loops
#                         }
#                 }
#             }
#         }
#     }
# }
# """
#
# Charan -> ascii - > a - 97,b-98,....123,   A- 65,B-66.....92
#
# 1 - [ _ _ _ _ _ _ _ _ ] => [32 16 8 4 2 1] -
#
# 1 =  0001
# 2 =  0010
# 3 =  0011
# 4 =  0100
# 5 =  0101
# 25=  011001
#
# Truth table - 0,1
# AND   &&  and
# x y  out
# 1 1  1
# 0 0  0
# 1 0  0
# 0 1  0
#
# OR  || or
# x y  out -sum   carry
# 1 1  1
# 1 0  1
# 0 1  1
# 0 0  0
#
# Not !
# x  ~x
# 1  0
# 0  1
#
# XOR
# x y z
# 0 0 1
# 1 1 0
# 1 0 0
# 0 1 0
#
# BITWISE Operators
#
# & | ^ >> << >>> ~
#
#
# Types of meory - > volatile memory, stack memory , queue, heap memory
#
# C - 67 - 0b1000011   - 1000011

#BITWISE OPERATORS
#
# print(
#     "BITWISE-Operators"
# )
#
# print(
#     f"Bitwise Operator - AND -> {1&0}",
#     f"Bitwise Operator - OR -> {1|0}",
#     f"Bitwise Operator - NOT -> {1!=1}",
#     f"Bitwise Operator - ~ -> {~-27}"
# )

import pyautogui
import time

time.sleep(10)

while True:
    pyautogui.typewrite("Hello")
    pyautogui.press("enter")


