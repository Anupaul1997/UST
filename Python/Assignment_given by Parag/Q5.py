
"""
5. For the given string 

Python is a widely used general-purpose, high level programming language. It was created by Guido
 van Rossum in 1991 and further developed by the Python Software Foundation. It was designed with an 
 emphasis on code readability, and its syntax allows programmers to express their concepts in fewer lines of code


calculate the number of vowels individually i.e number of a, e, i , o and u , 
calculate total number of consonants without considering any punctuation character

"""

dict={'a':0,'e':0,'i':0,'o':0,'u':0,'consonents':0}

str1="""Python is a widely used general-purpose, high level programming language. It was created by Guido van Rossum in 1991 and further developed by the Python
Software Foundation. It was designed with an emphasis on code readability, and its syntax allows programmers to express their concepts in fewer lines of code"""
str=str1.lower()
for i in str:
    if(i.isalpha()==True):
        if i in dict.keys():
            dict[i]+=1
        else:
            dict['consonents']+=1
    
for j in dict:
     print(j,"=",dict[j])
        
