class Solution:
    def groupAnagrams(self, strs) :
        count={}
        for word in strs:
            temp="".join(sorted(word))
            if temp in count:
                count[temp].append(word)
            else:
                count[temp]=[word]
        return list(count.values())