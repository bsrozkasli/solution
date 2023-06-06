def isanagram( word1:str  , word2 :str)->bool:
     word1=word1.split()
     word2=word2.split()
     if(len(word1)!=len(word2)):
         return False
     else:
         if(word1.sort()==word2.sort()):
             return True
         else:
             return False
print(isanagram("note","tone"))