
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Linked_List:
	def __init__(self):
		self.head = None
		self.tail = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
		temp = self.head
		while temp.next:
			temp = temp.next
		self.tail = temp

	def push_at_tail(self,data):
		node = Node(data)
		if self.tail == None:
			self.head = node
			self.tail = node
		else:
			self.tail.next = node
			self.tail = node


	def delete_Node(self, key):
		
		#if (self.head):
		#	if (self.head.data == key):
		#		self.head = self.head.next
		#		return
			
		#temp = self.head

		#while(temp):
		#	if temp.data == key:
		#		break
		#	prev = temp
		#	temp = temp.next

		#if(temp == None):
		#	return
		
		#prev.next = temp.next

		#temp = None
		temp = self.head
		prev = Node(None)
		while temp != None:
			if temp.data == key:
				prev.next = temp.next
			else:
				prev = temp
			temp = temp.next
		
	def print_List(self):
		temp = self.head
		while(temp):
			print (temp.data)
			temp = temp.next
	
	def Remove_Dups(self): # 2.1
		# Part 1 : Using buffer : 
		# Space : O(n) / Time : O(n)
		#li = []
		#temp = self.head
		#prev = Node(None)
		#while temp != None:
		#	if temp.data in li:
		#		prev.next = temp.next
		#	else:
		#		li.append(temp.data)
		#		prev = temp
		#	temp = temp.next



		# Part 2 : Without Using Buffer
		# Space : O(1) / Time : O(n^2)

		temp = self.head
		while temp:
	

			runner = temp
			while runner.next != None:
				
				if runner.next.data == temp.data:
					runner.next = runner.next.next
				else:
					runner = runner.next

			temp = temp.next

	def partition(self,x):
		temp = self.head
		head = temp
		tail = temp
		
		while temp:
			next = temp.next
			if temp.data < x:
				temp.next = head
				head = temp
			else:
				tail.next = temp
				tail = temp
			temp = next
		tail.next = None 
		self.head = head 

	def insert_at(self,index,data):
		node = Node(data)
		if index == 0:
			if self.head == None:
				self.head = node
				self.tail = node
			else:
				node.next = self.head
				self.head = node
		else:
			temp = self.head
			size = 0
			while temp:
				size += 1
				temp = temp.next
			if index > size:
				print("Index more than size")
			else:
				temp = self.head
				prev = None
				while index:
					index -= 1
					prev = temp
					temp = temp.next
				prev.next = node
				node.next = temp
					

def return_kth_to_last(head,k):
	if head == None:
		return 0

	index = return_kth_to_last(head.next,k) + 1

	if index == k:
		print(str(k) + " to the last node is " + str(head.data))
	return index

def printbackwards(head):
	if head == None:
		return 0
	
	printbackwards(head.next)
	print(head.data)

def sum_lists(head1,head2):

	temp1 = head1
	size1 = 0
	while temp1:
		size1 += 1
		temp1 = temp1.next

	temp2 = head2
	size2 = 0
	while temp2:
		size2 += 1
		temp2 = temp2.next

	total = 0
	temp1 = head1
	while temp1:
		total = total + temp1.data*pow(10,size1-1)
		size1 = size1 - 1
		temp1 = temp1.next

	temp2 = head2
	while temp2:
		total = total + temp2.data*pow(10,size2-1)
		size2 = size2 - 1
		temp2 = temp2.next
	
	temp1 = None
	
	sumList = Linked_List()

	while total:
		data = total % 10
		sumList.push(data)
		total = int(total/10)

	return sumList
	



	


















llist = Linked_List()
llist.push_at_tail(3)
llist.push_at_tail(5)
llist.push(1)
llist.push_at_tail(2)
llist.push_at_tail(4)
llist.push_at_tail(8)
llist.push(9)
llist.push_at_tail(7)





#print(return_kth_to_last(llist.head,2))

#print(printbackwards(llist.head))



#llist.delete_Node(3)

llist.insert_at(0,6)


#llist.print_list()
#print("**")

#llist.partition(5)

#llist.print_list()
print("**")


list1 = Linked_List()
list1.push_at_tail(6)
list1.push_at_tail(1)
list1.push_at_tail(7)
list1.print_List()

print("**")

list2 = Linked_List()
list2.push_at_tail(3)
list2.push_at_tail(2)
list2.push_at_tail(1)
list2.print_List()

sumlist = sum_lists(list1.head,list2.head)

print("**")
sumlist.print_List()





