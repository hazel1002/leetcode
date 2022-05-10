class Solution:
    def isPalindrome(self, x: int) -> bool:
        list_x = [str(i) for i in str(x)]
        reverse_list_x = list_x[::-1]
        str_x = "".join(reverse_list_x)
        return str_x == str(x)

testx = Solution()
a = testx.isPalindrome(23)
print(a)
