from collections import Counter

class Solution:
    def isAnagram(s: str, t: str) -> bool:
        sList, tList = [x for x in s], [x for x in t]
        sList.sort(), tList.sort()

        result = True
        
        for i in range(len(sList)):
            if(sList[i] != tList[i]):
                result = False
                
        return result
    
    def mappedAnagram(s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        
        countS, countT = {}, {}
        
        # for letter in range(len(s)):
        #     countS[s[letter]] = 1 + countS.get(s[letter], 0)
        #     countT[t[letter]] = 1 + countT.get(t[letter], 0)
            
        # for key in countS:
        #     if countS[key] != countT.get(key, 0):
        #         return False
            
        # return True
        
        # OR
        
        # counterS, counterT = Counter(s), Counter(t)
        
        # for key in counterS:
        #     if counterS[key] != counterT.get(key, 0):
        #         return False
            
        # return True
        
        # OR
        
        return Counter(s) == Counter(t)
            
        

if __name__ == "__main__":
    print(Solution.isAnagram('anagram', 'nagaram'))
    print(Solution.mappedAnagram('anagram', 'nagaram'))