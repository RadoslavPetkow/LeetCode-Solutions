class Solution(object):
    def check(self,idx ,string_x,target):
        if idx == len(string_x):
            return target == 0

        for j in range(idx,len(string_x)):
            x = string_x[idx:j+1]
            y = int(x)
            if self.check(j + 1, string_x, target - y):
                return True
        return False

    def punishmentNumber(self, n):
        ans = 0
        for i in range(1,n+1):
            x =i*i
            string_x = str(x)
            if self.check(0,string_x,i):
                ans += x
        return ans
        
