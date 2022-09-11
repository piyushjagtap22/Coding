class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = Node(data)
        if self.head is None: 
            self.head = new_node
            return
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_node

    def remove(self,data):
        temp = self.head

#if data is at head
        if(temp.data == data):
            self.head = temp.next
            temp.next = None
            return

#if data is at any node
        while(temp):
            if(temp.data == data):
                break
            prev = temp         #store the current as prev before pointing the current to next
            temp = temp.next
                
        

        if(temp == None):
            return

        prev.next = temp.next
        temp = None


    def printList(self):
        printval = self.head
        while printval != None:
            print(printval.data)
            printval = printval.next


    def detect_loop(self):
        s = set()
        temp =  self.head
        while(temp):
            if temp in s:
                temp = None
                return True
            s.add(temp)
            temp = temp.next
        return False



if __name__ == "__main__":
    ll = LinkedList()
    ll.push(10)
    ll.push(20)
    ll.push(30)
    ll.push(40)
    ll.push(50)


    ll.head.next.next.next = ll.head.next

    print(ll.detect_loop())

    # ll.printList()

    # ll.remove(40)
    # ll.printList()


    
    