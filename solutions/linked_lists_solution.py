# create the LinkedList class
class LinkedList:
    #create the Node class
    class Node:
        def __init__(self, value):
            # define the main value
            self.value = value
            # define the value of "next"
            self.next = None
            # define the value of "prev"
            self.prev = None
    
    # creating an empty linked list
    def __init__(self):
        self.head = None
        self.tail = None

    
    def insert_head(self, value):
        #step 1: Create a new node
        new_node = LinkedList.Node(value)
    
        # if there is no head (meaning the list is empty)
        if self.head is None:
            # set the head and tail equal to the new_node
            self.head = new_node
            self.tail = new_node
        # if there is a head (meaning there is at least one node in the list)
        else:
            # follow the rest of the steps to insert a node at the head
            #step 2: Set the "next" pointer of the new node equal to the current head.
            new_node.next = self.head
            #step 3: Set the "prev" pointer of the current head equal to the new node.
            self.head.prev = new_node
            #step 4: Set the head equal to the new node
            self.head = new_node 


    def insert_tail(self, value):
        #step 1: Create a new node
        new_node = LinkedList.Node(value)

        # if there is no tail (meaning the list is empty)
        if self.tail is None:
            # set the head and tail equal to the new_node
            self.head = new_node
            self.tail = new_node
        # if there is a tail (meaning there is at least one node in the list)
        else:
            # follow the rest of the steps to insert a node at the tail
            #step 2: Set the "prev" pointer of the new node equal to the tail
            new_node.prev = self.tail
            #step 3: Set the "next" pointer of the tail equal to the new node
            self.tail.next = new_node
            #step 4: Set the tail equal to the new node
            self.tail = new_node 


    def insert_middle(self, value, new_value):

        current_node = self.head
    
        while current_node is not None:
            if current_node.value == value: 
                if current_node == self.tail: #<<----------
                    self.insert_tail(new_value)
                else:
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = current_node
                    new_node.next = current_node.next
                    current_node.next.prev = new_node
                    current_node.next = new_node
                return # put return here so we can exit the function once we have inserted our new node
            else:
                current_node = current_node.next


    def remove_head(self):
        # this is the code that is run if there is only one node in the list
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # these are the steps we just went over
        else:
            #step 1: Set the "prev" of the second node to None
            self.head.next.prev = None
            #step 2: Set the head equal to the second node
            self.head = self.head.next  


    def remove_tail(self):
        # this is the code that is run if there is only one node in the list
        if self.tail == self.head:
            self.head = None
            self.tail = None
        # these are the steps we just went over
        else:
            #step 1: Set the "next" of the second to last node to None
            self.tail.prev.next = None
            #step 2: Set the tail equal to the second to last node
            self.tail = self.tail.prev

    
    def remove_middle(self, value):
        """
        Remove the first node that contains 'value'.
        """
        curr = self.head #start at the head
        while curr is not None: #while there is a value in the node
            if curr.value == value: #if the current node's data matches the value we're looking for
                #if the value is the tail, we can call the remove tail function to remove it
                if curr == self.tail:
                    self.remove_tail()
                elif curr == self.head: #if the value is the head, then we can call the remove head function to remove it
                    self.remove_head()
                else:
                    #set the next node's preveious link to the node before the current node
                    curr.next.prev = curr.prev
                    #set the node before the current node's 'next' link to the node after the current node
                    curr.prev.next = curr.next
                return #exit the function after you delete the matching node
            curr = curr.next #go to the next node's value if you the current node's value is not a match

    def __iter__(self):
        """
        Iterate foward through the Linked List
        """
        curr = self.head  # Start at the begining since this is a forward iteration.
        while curr is not None:
            yield curr.value  # Provide (yield) each item to the user
            curr = curr.next # Go forward in the linked list


# TEST CODE

# ll = LinkedList()
# ll.insert_head(100)
# ll.insert_head(50)
# ll.insert_head(25)

# for x in ll:
#     print(x) #25, 50, 100

# print("===============")
# ll.insert_middle(50, 75)

# for x in ll:
#     print(x) #25, 50, 75, 100

# print("===============")

# ll.remove_head()
# ll.remove_middle(75)

# for x in ll:
#     print(x) #50, 100

# print("===============")

# ll.remove_tail()
# ll.remove_tail()

# for x in ll: 
#     print(x) #list should be empty

# print("===============")   

# ll.insert_tail(1)
# ll.insert_tail(2)
# ll.insert_tail(3)
# ll.insert_tail(4)
# ll.insert_tail(5)

# for x in ll:
#     print(x) #1, 2, 3, 4, 5