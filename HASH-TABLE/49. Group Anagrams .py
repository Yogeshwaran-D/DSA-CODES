class Solution:
    def groupAnagrams(self, strs):
        new_dict={}
        for i in strs:
            key="".join(sorted(i))
            if new_dict.get(key):
                temp=new_dict.get(key)
                temp.append(i)
            else:
                temp=[i]
            new_dict[key]=temp
        return new_dict.values()
