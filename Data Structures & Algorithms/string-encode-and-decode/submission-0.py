class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded=[]

        for string in strs:
            encoded.append(str(len(string))+"#"+string)
        
        return "".join(encoded)



    def decode(self, s: str) -> List[str]:
        answer = []
        i = 0

        while i <len(s):
            j=i

            while s[j]!="#":
                j+=1

            length = int(s[i:j])

            string_start = j+1
            string_end=string_start+length

            answer.append(s[string_start:string_end])
            i = string_end

        return answer



       

        



