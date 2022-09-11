"""
Chef has N numbers written on his board. He wants only one number to remain on the board
and so he devises a special tactic to do so.

He randomly picks up 2 numbers written on the board say A and B respectively.
He erases both of them from the board and writes a new number on the board which equals -
A−B if parity of A = parity of B
A+B if parity of A != parity of B

Here parity refers to remainder obtained when a number is divided by 2

Notice that the total numbers on the board reduced by 1 after 1 such operation.
After a finite number of operations there would only be 1 number remaining on the board.

Chef is interested in knowing how many different final numbers he could end up with.


Input Format
The first line contains a single integer N denoting the amount of numbers initially present on the board.
The second line consists of NN space-separated integers
A_1, A_2,..., A_N denoting the numbers written on the board initially.

Output Format
For each testcase, output a single integer denoting the number of possible final numbers on the board.
"""


def parity_result(x, y):
    return (x - y, y - x) if x % 2 == y % 2 else x + y


a = [2, 7, 6, 3]

for i in a:

