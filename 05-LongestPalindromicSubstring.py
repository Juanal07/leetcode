# not optimal but works
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]
        fakeLen = len(s) * 2 - 1
        # print("fakeLen", fakeLen)
        i = 0
        while i < fakeLen:
            # print("i:", i)
            auxResult = ""
            if i % 2 == 0:
                par = 1
            else:
                par = 0
            fakePosL = i - 1 - par
            fakePosR = i + 1 + par
            # print("posL fake:", fakePosL)
            # print("posR fake:", fakePosR)
            posL = fakePosL // 2
            posR = fakePosR // 2
            # print("posL real:", posL)
            # print("posR real:", posR)
            while posL >= 0 and posR < len(s) and s[posL] == s[posR]:
                # print("posL real while:", posL)
                # print("posR real while:", posR)
                if s[posL] == s[posR]:
                    if i % 2 == 0:
                        if len(auxResult) > 1:
                            auxResult = s[posL] + auxResult + s[posR]
                        else:
                            auxResult = s[posL] + s[i // 2] + s[posR]
                    else:
                        auxResult = s[posL] + auxResult + s[posR]
                # print(auxResult)

                # if i % 2 == 0:
                #     posL -= 2
                #     posR += 2
                # else:
                posL -= 1
                posR += 1

            # check if new auxResult is larger than result
            if len(auxResult) > len(result):
                result = auxResult
            # print("result: ", result)

            i += 1

        # result = auxResult
        # print("--------------result")
        return result


# print("Final result", Solution().longestPalindrome("zvavxjhijji"))
print("Final result", Solution().longestPalindrome("cccabb"))
