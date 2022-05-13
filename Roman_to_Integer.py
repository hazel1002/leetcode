class Solution:
    def romanToInt(self, s: str) -> int:
        roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        z=0
        for i in range(0,len(s)-1):
            if roman[s[i]]<roman[s[i+1]]:
                z-=roman[s[i]]
            else:
                z+=roman[s[i]]
        z+= roman[s[-1]]
        return z