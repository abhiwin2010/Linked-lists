# Singly-linked list implementation in Python3
# author = Abhijeet Mohapatra

#this is the Node class which contains a data and a next attribute
class Node:
    def __init__(self):
        self.data = None
        self.next = None
#this is the linked list class which uses the Node class to create a linked list
class Linked_List:
    def __init__(self):
        self.head = None
#inserting an element at the beginning of the linked List
    def insert_at_front(self,data):
        if self.head == None:
            new = Node()
            new.data = data
            self.head = new
            print("Inserted at the beginning of the list")
        else:
            new = Node()
            new.data = data
            new.next = self.head
            self.head = new
            print("Inserted at the beginning of the list")
#inserting an element at the end of the linked List
    def insert_at_end(self,data):
        if self.head == None:
            new = Node()
            new.data = data
            self.head = new
            print("Inserted at the end of the list")
        else:
             temp = self.head
             while temp.next != None:
                 temp = temp.next
             new = Node()
             new.data = data
             temp.next = new
             print("Inserted at the end of the list")
#deleting an element from the beginning of the List
    def delete_from_front(self):
        if self.head == None:
            print("List is already empty")
        else:
            self.head = self.head.next
            print("Deleted from the beginning of the list")
#deleting an element from the end of the end of the list
    def delete_from_end(self):
        if self.head == None:
            print("List is already empty")
        elif self.head.next == None:
            self.head = None
            print("Deleted from the end of the list")
        else:
            temp = self.head
            while temp.next.next != None:
                temp = temp.next
            temp.next = None
            print("Deleted from the end of the list")
#inserting an element at a given position
    def insert_at_nth_position(self,data,n):
        if n == 1:
            self.insert_at_front(data)
        else:
            temp = self.head
            if int(n) <=self.count():
                count = 1
                while count < int(n-1):
                    if temp.next != None:
                        temp = temp.next
                        count += 1
                new = Node()
                new.data = data
                new.next = temp.next
                temp.next = new
                print("Inserted at postion",n)
            else:
                print("entered position exceeds list length")
#deleting an element from a given position of the list
    def delete_from_nth_position(self,n):
        if self.head == None:
            print("list is already empty")
        elif n == 1:
            self.delete_from_front()
        elif int(n) > self.count():
            print("entered position exceeds list length")
        else:
            temp = self.head
            count = 1
            while count < int(n-1):
                temp = temp.next
                count += 1
            temp.next = temp.next.next
            print("Deleted from position",n)
#displaying the elements of the list
    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next
#counting the number of nodes in the List
#the count starts from 1 not from 0
    def count(self):
        temp = self.head
        count = 1
        while temp.next != None:
            temp = temp.next
            count += 1
        return count
