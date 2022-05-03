''' Solución óptima de un usuario de leetcode

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
        numeral = ""
        for i in roman:
            numeral += (num // i) * roman[i]
            print(num//i)
            print(roman[i])
            num %= i
        return numeral
'''

class Solution:
    def intToRoman(self, num: int) -> str:
        dict = { 'I': 1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        solution = ''
        r = num // 1000
        for _ in range(r):
            solution += 'M'
        num -= r*1000

        r = num // 100
        if r<4:
            for _ in range(r):
                solution += 'C'
        if r == 4:
            solution += 'CD'
        if r == 5:
            solution += 'D'
        if r == 9:
            solution += 'CM'
        if 5 < r < 9:
            solution += 'D'
            for _ in range(r-5):
                solution += 'C'
        num -= r*100

        r = num // 10
        print(r)
        if r<4:
            for _ in range(r):
                solution += 'X'
        if r == 4:
            solution += 'XL'
        if r == 5:
            solution += 'L'
        if r == 9:
            solution += 'XC'
        if 5 < r < 9:
            solution += 'L'
            for _ in range(r-5):
                solution += 'X'
        num -= r*10

        r = num
        if r<4:
            for _ in range(r):
                solution += 'I'
        if r == 4:
            solution += 'IV'
        if r == 9:
            solution += 'IX'
        if r == 5:
            solution += 'V'
        if 5 < r < 9:
            solution += 'V'
            for _ in range(r-5):
                solution += 'I'
        return solution

print(Solution().intToRoman(58))
