# from collections import deque
#
#
# def min_jumps_to_escape(N, X, Y, A):
#     if X == Y:
#         return 0
#
#     queue = deque([(X, 0)])
#
#     visited = set()
#     visited.add(X)
#
#     while queue:
#         position, jumps = queue.popleft()
#
#         left_move = (position - A[position - 1]) % N
#         right_move = (position + A[position - 1]) % N
#
#         left_move = N if left_move == 0 else left_move
#         right_move = N if right_move == 0 else right_move
#
#
#         if left_move == Y or right_move == Y:
#             return jumps + 1
#
#         if left_move not in visited:
#             visited.add(left_move)
#             queue.append((left_move, jumps + 1))
#
#         if right_move not in visited:
#             visited.add(right_move)
#             queue.append((right_move, jumps + 1))
#
#     return -1
#
#
#
# N = 5
# X = 1
# Y = 3
# A = [2, 3, 1, 1, 2]
#
# result = min_jumps_to_escape(N, X, Y, A)
# print(result)