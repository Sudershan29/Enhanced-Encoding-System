#!/usr/bin/env python
# coding: utf-8

# # Rudimentary stages 

# In[36]:


#Reading File which consists of Greek and English 

f = open("greekenglish.txt", "r")

f2=f.read()
print(f2)
print("\n size = ",end=' ')
print(len(f2))
f.close()


# In[37]:


#Exploring


# In[38]:


#Testing how to read character by character
f = open("greekenglish.txt", "r")
ctr=1
while ctr<10:
    char=f.read(1)
    if not char:  
        break         
    print(char) 
    ctr+=1
f.close()

# U+0370–U+03FF Greek   49 letters
#U+0041-U+007A English 52 (uppercase and lower)

#Website to spot Unicode => https://unicode-table.com/en/alphabets/english/
#Reference https://www.youtube.com/watch?v=ls-177DIGao
# In[39]:


# Working with bytes
b= b'aBc'
print(type(b))
print(b[1])

s='Ελλη'
s=bytes(s,encoding="utf-8")
print(s)
str(s,encoding='utf-8')

# Encoding in utf-8 and decoding back in latin-1    (LOL)
str(s,encoding='latin-1')


# # Getting Characters

# In[40]:


str(b,encoding='utf-8')


# In[41]:


#finding a method to extract alphabets

z = []   
z = [chr(x) for x in range(ord('a'), ord('z') + 1)]  
for x in range(ord('A'), ord('Z') + 1):
    z.append(chr(x))
print(str(z)) 
print("\n[",end='')
for x in z:
    print(hex(ord(x))+" ",end=',')
print("]")
#DOESNT WORK for non consequetive characters


# In[42]:


#Copying characters

y=['Α','α', 'Β', 'β', 'Γ', 'γ', 'Δ' ,'δ', 'Ε' ,'ε', 'Ζ', 'ζ', 'Η' ,'η', 'Θ' ,'θ', 'Ι', 'ι', 'Κ', 'κ', 'Λ' ,'λ', 'Μ' ,'μ', 'Ν', 'ν', 'Ξ', 'ξ', 'Ο', 'ο', 'Π' ,'π', 'Ρ', 'ρ', 'Σ' ,'σ','ς','Τ','τ','Υ' ,'υ', 'Φ', 'φ', 'Χ' ,'χ', 'Ψ', 'ψ','Ω','ω','ή','ί','έ','ά','ό','ΐ','ώ','ύ']
print(y)
print("\n[",end='')
for x in y:
    print(hex(ord(x))+" ",end=',')
print("]")


# In[43]:


# xD Greek A and English A look the same but have different codes
if('A'!='Α'):
    print('Not Equal')


# # Creating Dictionary 

# In[44]:


class my_dictionary(dict): 
  
    # __init__ function 
    def __init__(self): 
        self = dict() 
          
    # Function to add key:value 
    def add(self, key, value): 
        self[key] = value 
  
every = my_dictionary() 


# In[45]:


print("Greek ",end='')
print(len(y))
print("English ",end='') 
print(len(z))

#Combining all languages together

all=[z,y]
print(all)


# Declaring the Overlapping size

# In[132]:


overlap=12


# In[133]:


count=overlap+1
for l in all:
    count-=overlap
    for x in l:
        every.add(x,count)
        count+=1

extra=['1','2','3','4','5','6','7','8','9','0',' ',')',']','}']
#                       Trust me this isnt empty^

end=[',','(','[','{','.',',','-','\'','\"',':',';','\n','\t']

fin=extra+end

for x in fin:
    every.add(x,count)
    count+=1
print(every)


# Finding Unknowns

# In[134]:


f = open("greekenglish.txt", "r")
while 1:
    char=f.read(1)
    if not char:  
        break         
    if char not in every:
        print(ord(char))
f.close()


# # Encoding

# In[135]:


bin(256).replace("0b", "")


# In[136]:


f=open('pro_trail.txt','wb')
byte_arr = []
f2= open("greekenglish.txt", "r")
while 1:
    char=f2.read(1)
    if not char:  
        break         
    byte_arr.append(every[char])
f2.close()
binary_format= bytearray(byte_arr)
f.write(binary_format);
f.close()


# In[137]:


#not marking with language names, might be an addon later


# # Decoding

# In[138]:


#For now assuming, more than 2 languages dont overlap


# In[139]:


#Initials
limits=[42,53]   # 0-42 can only be ENG. 42-53 is ambigious.  53-91 has to be only GREEK 
lang=1 #it could be 0 or 1
lastindex=0


# In[140]:


f=open("pro_trail.txt","rb")
num=list(f.read())
print (num)
f.close()


# In[141]:


test=num
write=''
index=0
lastindex=0
for i in test:
    if(i<42 and lang==1):
        lang=0
        write=write[0:lastindex]
        for j in range(lastindex,index+1):
                listOfKeys = [key  for (key, value) in every.items() if value == test[j]]
                write=write+listOfKeys[0]
    elif(i>53 and lang==0 and i<99):
        lang=1
        write=write[0:lastindex]
        for j in range(lastindex,index+1):
                listOfKeys = [key  for (key, value) in every.items() if value == test[j]]
                if(len(listOfKeys)==1):
                    write=write+listOfKeys[0]                        
                else:
                    write=write+listOfKeys[1]
    else:
        listOfKeys = [key  for (key, value) in every.items() if value == i]
        if(len(listOfKeys)==1):
            write=write+listOfKeys[0]                        
        else:
            write=write+listOfKeys[lang]
        if(listOfKeys[0] in end):
            lastindex=index+1
    index=len(write)
print(write)


f=open("compare.txt",'w')
f.write(write)
f.close()

#Failed Attempt 

test=num[0:10]
write=''

for i in test:
    if(i<=limits[lang]):
        for j in range(1,lang+1):
            if(limits[j+1]>i and limits[j-1]<i):
                lang=j
        write=write[0:lastindex]
        for j in range(lastindex,i+1):
                listOfKeys = [key  for (key, value) in every.items() if value == j]
                print(listOfKeys)    
    elif(i>=limits[lang+1]):
        for j in range(lang+1,len(limits)-1):
            if(limits[j-1]<i and limits[j+1]>i):
                lang=j
        write=write[0:lastindex]
        for j in range(lastindex,i+1):
                listOfKeys = [key  for (key, value) in every.items() if value == j]
                write=write+listOfKeys[1]
    else:
        listOfKeys = [key  for (key, value) in every.items() if value == i]
        print(listOfKeys)
print(write)
# # Cosine similarity

# In[121]:


from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 

f = open("greekenglish.txt", "r")
X =f.read() 
Y = write
  
# tokenization 
X_list = word_tokenize(X)  
Y_list = word_tokenize(Y) 
  
# sw contains the list of stopwords 
sw = stopwords.words('english')  
l1 =[];l2 =[] 
  
# remove stop words from string 
X_set = {w for w in X_list if not w in sw}  
Y_set = {w for w in Y_list if not w in sw} 
  
# form a set containing keywords of both strings  
rvector = X_set.union(Y_set)  
for w in rvector: 
    if w in X_set: l1.append(1) # create a vector 
    else: l1.append(0) 
    if w in Y_set: l2.append(1) 
    else: l2.append(0) 
c = 0
  
# cosine formula  
for i in range(len(rvector)): 
        c+= l1[i]*l2[i] 
cosine = c / float((sum(l1)*sum(l2))**0.5) 
print("similarity: ", cosine) 

f.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




