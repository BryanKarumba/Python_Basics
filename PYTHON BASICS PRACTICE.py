#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Creating  list
users=['kim','john','george','valor','peter']
users


# In[3]:


# Accessing the first element in the list
users[0]


# In[4]:


#Creating a duplicate
copy_users=users[:]
copy_users


# In[5]:


#Adding an element in a given index
users[0]='kimm'
users


# In[6]:


#Changing all elements to uppercase
uppercase_users=[users.upper() for users in users]
uppercase_users


# In[7]:


dimensions=(800,600)
print (dimensions)


# In[8]:


#finding the number of elements.
len(users)


# In[9]:


#Forming a simple message using the length above
print('We have' +  str(len(users))  + 'CAS in the county government')


# In[10]:


for user in users:
    print(user)



# In[14]:


for user in users:
    print('Welcome'+ '' + user + '! We are happy you signed up')



# #adding elements in a list
# users=[]
# users.append('mia')
# users.append('kia')
# users

# In[11]:


users.insert(0, 'joe')
users.insert(2, 'joel')
users


# In[30]:


#length of users and printing a line
len(users)
print("We have" + str(len(users)) + ' '+ "users.")


# In[13]:


copy_users=users[:]
copy_users.append('kino')
copy_users.insert(3, 'rio')
copy_users.remove('kino')
copy_users


# # Dictionaries
# #Dictionaries are a concept that allows you to store data(usually related) as a
# key-value pair.

# In[15]:


dict={'name':'John', 'age':'25'}
dict['name']


# In[21]:


#Adding new key value pairs
dict['city']= 'Nakuru'
dict['Points']=14,16,17,19,12
dict


# In[22]:


dict['Points']


# In[15]:


#creating a list in a key value
users1={'names':['john','james','kinuthia'], 'ages':[16,33,44], 
      'city':['K','N','L']
     }
users1

#users1['city']


# In[16]:


#Nesting dictionaries-creating couple of dictionaries in one definer
users2=[]
user2a={'name':'johne', 'year':'2002'}
user22a={'language':'kikuyu', 'town':'kiambu'}
user22a
users2.append(user2a)
users2.append(user22a)
users2


# In[17]:


squares=[x**2 for x in range(10)]
squares


# # Functions in python
# Functions are named block of codes designed to do a specific job.
# The code can be run whenever you need to  accomplish the same task.

# In[18]:


def add_numbers(a,b):
    """Adds numbers"""
    result=a+b
    return result
    


# In[19]:


#num_1=5
#num_2=6
#sum_of_numbers=add_numbers(num_1,num_2)
#sum_of_numbers
num=[2,3,4,2]
sumn=sum(num)
sumn


# In[20]:


def describe_pet(animal,name):
    print('I have a' + ' ' + animal + '.') 
    print('Its name is' + ' ' + name +'.')
    
describe_pet('cat','harry')    


# In[21]:


# Adding a space between two strings
string1 = "Hello"
string2 = "World"

result = string1 + ' ' + string2
print(result)


# In[31]:


#RETURN VALUES
#A function stops  when it reaches the return value. When a function returns a value , the  calling line must provide a variable in which to store the return value 
def get_full_name(first_name,second_name):
    full_name = first_name + " " + second_name
    return full_name.title()

user=get_full_name('John','Mawega')
user


# In[32]:


#here, we request input from the user
def invoice(username, amount, due_date):
    print(f'Hello {username}')
    print(f'Your bill of ${amount} is due: {due_date}')
    
invoice('John', 100, '1/2/2024')    
    


# In[40]:


def invoice(name, amount, due_date):
    print(f'Hello {name}')
    print(f'Your bill is ${amount}')
    print(f'Which is due on {due_date}')
          
invoice('Bryan', 100, '01-02-2004') 


# In[24]:


#using return function for the above code
def full_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    
    return first + " " + last
full_name("bryan","karumba")


# In[25]:


import pandas as pd
df=pd.read_csv('price_data.csv')
df.head()


# # If statements
# If statements allow you to execute a code if a given condition is met

# In[1]:


#Conditional statements
c=10
c==10


# In[3]:


age=21
age>21


# In[41]:


age1=21
age2=18

age1>=21 and age2>=10


# In[5]:


age1=21
age2=18

age1>=21 or age2>=21


# In[14]:


age=19

if age>=18:
    print("You are allowed to vote")


# In[42]:


age=19

if age>=18:
    print("You are allowed to vote")
else :
    print("You can't vote yet")


# In[46]:


#if-elif-else chain
age=35
if age<4:
  price=5
elif age <18:
        price=15
else:
        price=20
print("Your cost is Ksh" + ' '+ str(price)+ ".")
        


# In[ ]:


# conditional test in lists
#We can test whether a certain value is in a list
players = ['al','bea','john','toto']
y='al' in players
y


# In[31]:


'eric' in players


# In[52]:


#Testing if a value is not in a list
banned_users=['ann','chad','dee']
user='de'

if user is not banned_users:
    print("You can play!")
else:
    print("You are not allowed to play")


# # While statements
# While statements run as long as certain conditions are true.
# a "while" statement is a control flow structure that allows a block of code to 
# be executed repeatedly as long as a specified condition is true. 
# The basic idea is to create a loop where the code inside the loop will 
# continue to run until the specified condition becomes false.

# In[56]:


#a simple example.
current_number=2
while current_number<5:
    print(current_number)
    current_number +=1


# In[65]:


current_number=1
while current_number<5:
    print(current_number)
    if current_number == 4:
        break
    current_number +=1


# In[67]:


current_number=1
while current_number<5:
    current_number +1
    print(current_number)
    if current_number == 4:
        break
    current_number +=1
else:print('No longer less than 5')    


# In[ ]:




