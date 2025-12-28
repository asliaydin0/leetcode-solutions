class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""  # En uzun palindromu tutacak değişken
        resLen = 0  # En uzun palindromun uzunluğu

        for i in range(len(s)):
            # 1. Durum: Tek sayı uzunluklu palindromlar (Odd length)
            # Merkez s[i] noktasıdır
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

            # 2. Durum: Çift sayı uzunluklu palindromlar (Even length)
            # Merkez s[i] ve s[i+1] arasındadır
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res