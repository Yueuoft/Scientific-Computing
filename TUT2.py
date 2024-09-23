#!/usr/bin/env python
# coding: utf-8

# In[1]:


Books = {}

def add_Book(BookID, title, author):
    if BookID in Books:
        print("exists")
    else:
        Books[BookID] = {"title": title, 'author': author}

#try call this
add_Book('123', 'Le petite prince', 'yue')
print(Books)
add_Book('123', 'leee', 'IEEE')
print(Books)


# In[2]:


def search_in_nested_dict(Books, item_to_find):
    for BookID, title in Books.items():
        if item_to_find in title:
            return f"'{item_to_find}' found under the bookID '{BookID}' with title: {title[item_to_find]}"
    return f"'{item_to_find}' not found in the library."

#try call this
# item_to_find = 'Le petite prince'
# result = search_in_nested_dict(Books, item_to_find)
# print(result)


# In[3]:


def search(BookID):
    if BookID in Books:
        print(Books[BookID])
    else:
        print('not found')
        
#call it


# In[4]:


def remove(BookID):
    if BookID in Books:
        del Books[BookID]
    else:
        print("not found")
        
# call it
remove(321)
print(Books)


# In[5]:


while True:
    print("Library Management System")
    print('1. Add Book')
    print('2. Remove Book')
    print('3. Search Book')
    print('4. Exit')
    choice = input('Enter your choice')
    if choice == '1':
        BookID = input ('Enter the BookID')
        title = input ('Enter the title')
        author = input ('Enter the author')
        add_Book(BookID, title, author)
        print(Books)
    elif choice == '2':
        BookID = input ('Enter the BookID')
        remove(BookID)
        print(Books)
    elif choice == '3':
        BookID = input ('Enter the BookID')
        search(BookID)
    else:
        break


# In[ ]:





# In[ ]:




