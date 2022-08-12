class node:
  def __init__(self,data=None,next=None):
    self.data=data
    self.next=next

class linkedlist:
  def __init__(self):
    self.head=None
  def append(self,data):
    n=node(data)
    if self.head is None:
      self.head=n
    else:
      temp=self.head
      while temp:
        if temp.next is None:
          temp.next=n
          break
        temp=temp.next
        
  def insert(self,index,data):
    if index>=self.count():
      self.append(data)
    else:
      n=node(data)
      temp=self.head
      if index>0:
        
        for i in range(index):
          temp=temp.next
        n.next=temp
        
        temp=self.head
        for i in range(index-1):
          temp=temp.next
        temp.next=n
      elif index==0:       
        n.next=temp
        self.head=n
      
      
  def count(self):
    if self.head is None:
      return 0
    else:
      temp=self.head
      len=0
      while temp:
        temp=temp.next
        len=len+1
      return len   
     
  def index(self,data):
      temp=self.head
      for index in range(self.count()):
            if data == temp.data:
                value_in_list = True
                break
            temp=temp.next
            value_in_list = False
      if value_in_list:
          return index
      else:
          print("\nvalue is not in the list.")
  def display(self):
    if self.head is None:
      print("linked list is empty")
    else:
      temp=self.head
      while temp:
       print(temp.data,"-->",end="")
       temp=temp.next
      
l1=linkedlist()
for i in range(5,10):
  l1.append(i)
  
  
print(l1.count())
print(l1.index(44))
l1.display()
