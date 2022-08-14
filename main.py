class node:
  def __init__(self,data=None,next=None):
    self.data=data
    self.next=next

class linkedlist:
  def __init__(self):
    self.head=None
  def popend(self):
        if self.head is None:
                pass
        elif self.count()==1:
                self.head=None 
        else:
                temp=self.head
                i=0
                while i<self.count()-2:
                    i=i+1
                    temp=temp.next
                del temp.next
                temp.next=None 
  def popstart(self):
      if self.head is None:
          pass
      elif self.count()==1:
          self.head=None
      else:
          temp=self.head
          self.head=temp.next
          del temp
  def pop(self,index):
      if self.count()==0:
          pass
      elif index>=self.count():
          self.popend()
      elif index==0:
          self.popstart()
      else:
          temp=self.head
          for i in range(index+1):
              temp=temp.next
          node=temp

          temp=self.head
          for i in range(index-1):
              temp=temp.next
    
          del temp.next
          temp.next=node
  def copy(self):
      list=linkedlist()
      temp=self.head
      while temp:
          list.append(temp.data)
          temp=temp.next
      return list
  def clear(self):
      for i in range(self.count()):
        self.popend()
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
  def extend(self,list):
      list_duplicate=list.copy()
      temp=list_duplicate.head
      while temp:
          self.append(temp.data)
          temp=temp.next
  def combine(self,list):
      temp=self.head
      for i in range(self.count()-1):
        temp=temp.next
      temp.next=list.head
  def reverse(self):
      duplicate=self.copy()
      temp=duplicate.head
      self.clear()
      while temp:
          self.insert(0,temp.data)
          temp=temp.next
l1=linkedlist()
l2=linkedlist()
for i in range(5):
    l1.append(i)
for i in range(5,10):
    l2.append(i)

l2.display()
l2.reverse()
print('\n')
l2.display()
