class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = {}
        for i, w in enumerate(strs) :
            counter = [0] * 26 #idx = pos in alphabet
            for char in w:
                counter[ord(char)-97] += 1

            new_key = tuple(counter)

            if new_key in counts.keys() :
                counts[new_key].append(i)
            else : 
                counts[new_key] = [i]
        
        result = []
        for anagram_indicies in counts.values() :
           result.append([strs[i] for i in anagram_indicies])
                
        return result
