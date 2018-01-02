
class Node:
    def __init__(self):
        self.data = None
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

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

    def delete_from_front(self):
        if self.head == None:
            print("List is already empty")
        else:
            self.head = self.head.next
            print("Deleted from the beginning of the list")

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

    def insert_at_nth_position(self,data,n):
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

    def delete_from_nth_position(self,n):
        if self.head == None:
            print("list is already empty")
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

    def display(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp = temp.next

    def count(self):
        temp = self.head
        count = 1
        while temp.next != None:
            temp = temp.next
            count += 1
        return count

l = Linked_List()
l.insert_at_end(12)
l.insert_at_end(23)
l.insert_at_end(45)
l.insert_at_front(98)
l.display()
l.delete_from_end()
l.display()
l.delete_from_front()
l.display()
l.insert_at_nth_position(123,3)
l.display()
l.insert_at_end(234)
l.insert_at_end(342)
l.insert_at_nth_position(567,3)
l.display()
l.delete_from_nth_position(2)
l.display()
print(l.count())
