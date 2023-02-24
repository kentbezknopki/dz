class Solution:
    def tree(self, n, c="*"):
        if n != 0:
            for i in range(1, n+1):
                print("*"*i)
        else:
            print("срубили ёлочку")
a=Solution()
n=int(input())
a.tree(n,"*")