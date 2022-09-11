"""
Total Prize Money:
In a coding contest, there are prizes for the top rankers. The prize scheme is as follows:
Top 10 participants receive rupees X each.
Participants with rank 11 to 100 (both inclusive) receive rupees Y each
Find the total prize money over all the contestants.

Input Format:
First line will contain T, number of test cases. Then the test cases follow
Each test case contains of a single line of input, two integers X and Y -
the prize for top 10 rankers and the prize for ranks 11 to 100 respectively
"""


for _ in range(int(input())):
    (x, y) = map(int, input().split(' '))
    print(x*10+y*90)

    
#[print((lambda x: x[0]*10+x[1]*90)(list(map(int, input().split(' '))))) for _ in range(int(input()))]
