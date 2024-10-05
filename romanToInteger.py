class Solution(object):
    def romanToint(self, s):
        #things to keep in mind:
        '''
        I           1
        V           5   *
        X           10
        L           50  *
        C           100
        D           500
        M           1000
        we always start from left and see that the numbers that are great are on the left
        example: 21 - XI, 37- XXXVII, 55 - LV and so on..
        but in case of digits like 4 and 9 or anyother digit close to the last 5 number we put: 4 - IV a smaller number before because we subtract that 1 from 5 = 4
        or IX 10 - 1 = 9 and so on till biggest numbers like XL = 40 or CD = 400 or CM = 900
        
        I can be placed before V (5) and X (10) to make 4 and 9. 
        X can be placed before L (50) and C (100) to make 40 and 90. 
        C can be placed before D (500) and M (1000) to make 400 and 900.

        and this spans till whatever number comes on your mind
        random number 795 - DCCXCV

        now when we take these numbers as input as string s, this function should be able to return a number
        '''
        s = s.upper()

        #first lets define these values upto 100 also lets put them in an array where we will be easy to access them as key value pairs.
        k = {'I' : 1,
             'V' : 5,
             'X' : 10,
             'L' : 50,
             'C' : 100,
             'D' : 500,
             'M' : 1000}
        #now we need to make a logic thaat takes the input s and traverses through out the input and gives each character a value
        #example XXV X - 10, X - 10, V - 5, X+X+V = 25
        #also the key insight is that if a smaller number comes before a bigger one we subtract it: IX, if a bigger number comes first and then a smaller number we add it: XI

        #to store the final value:
        ans = 0
        
        if not s:
            print("There is no input")
            return None
        
        #To traverse lets make a for loop
        for i in range(len(s)):
            #two if statements will do the job:
            if i < len(s) - 1 and k[s[i]] < k[s[i + 1]]: #if the first letter is smaller then the next one and we are also checking if this is the last letter
                ans -= k[s[i]]
            else:
                ans += k[s[i]]
        return ans
            
def main():
    sol = Solution()
    inp = input("enter the Roman Numeral: ")
    answer = sol.romanToint(inp)
    print("The converted roman numeral is : ", answer)

if __name__ == "__main__":
    main()