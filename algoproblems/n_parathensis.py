# Generate Parentheses Problem
# The problem is: Given N pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# For example, given N = 3, a solution set is:

# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]
# The naive solution is to generate all combinations of N pairs of parentheses, then checking if each one is valid.


#solution
# reference : https://www.youtube.com/watch?v=s9fokUqJ76A&t=109s&ab_channel=NeetCode
# conditions
# 1. openN=closedN=N
# 2. open> close --> condition to add parathensis 
# 3. valid if openN == closedN

import snoop
import heartrate 
heartrate.trace(browser=True)

@snoop
def generate_N_parathensis(N):
    stack=[]
    result=[]
    def backtrack(openN, closedN):

        # condition to return nothing 
        if openN==closedN==N:
            result.append("".join(stack))
            return
        
        if openN < N:
            print(openN, closedN, N)
            stack.append("(")

            backtrack(openN+1,closedN)
            stack.pop()


        if closedN <openN:
            print(openN, closedN, N)

            stack.append(")")
            backtrack(openN,closedN+1)
            stack.pop()

    backtrack(0,0)
    return result


print(generate_N_parathensis(3))

        


