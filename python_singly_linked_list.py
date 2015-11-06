#Singly Linked List Implementation

# I've gotten the code started for you, showing you what your node class should look like
class Node(object):
    def __init__(self, val):
        # have our node hold a value
        self.value = val
        # initially it will not keep track of a node that comes after
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        # initially set our head attribute to None
        self.head = None

    def traverse(self):
        # this method prints the values of of all the nodes in the list
        print "traversing..."
        if self.head != None:
            # we will initialize our current node as the head node
            current_node = self.head
            #print the value of the head node
            print current_node.value
            # this while loop moves us forward through the linked list
            while current_node.next != None:
                current_node = current_node.next
                print current_node.value
        # in the case that there are no nodes
        else:
            print "No nodes"
            return False

    # create a method to add a new node
    def add_node(self, val):
        # creating a new node
        new_node = Node(val)
        # if there are no nodes yet set the head attribute to our new node
        if self.head == None:
            self.head = new_node
        # else we will have to traverse to the last node in the chain and
        #add our new node to the end
        else:
            current_node = self.head
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = new_node

    # now implement the following functions
    # as you are going through/when you finish each method,
    # make comments so you are aware of what's going on in each method
    def print_as_list(self):
        # Initialize the new list
        newList = []
        # this method should print all the values of the nodes in a list
        if self.head != None:
            # Set the current node to the head
            current_node = self.head
            # Since head isn't null, append the value of the node to a new list
            newList.append(current_node.value)
            while current_node.next != None:
                # while loop used to check for any additional nodes after the head
                current_node = current_node.next
                # append to list if more nodes are found
                newList.append(current_node.value)
            print newList
        else:
            # print there are no nodes to append and return false
            print "No Nodes to Append"
            return False


    def remove_node(self):
        # this method should remove the last node in the linked list
        # start if statement to look for the node that has null and set that node to none
        if self.head != None:
            # set the current node to head
            current_node = self.head
            # create a temp_node to keep track of current node
            temp_node = current_node
            # check to see if list only has one node.  If it does, remove the node
            if current_node.next == None:
                self.head = None
            while current_node.next != None:
                # while loop used to get to the last node
                # temp_node retains the current node
                temp_node = current_node
                # statement moves current_node to next node
                current_node = current_node.next
                # #### THIS PORTION OF CODE REMOVES NODE WITH A GIVEN VALUE #####
                # if current_node.value == val:
                #     temp_node.next = current_node.next
            # changes the next node pointer to None
            temp_node.next = None

        else:
            # print there are no nodes to remove and return false
            print "No Nodes to Remove"
            return False


    def insert_node_after(self, val, newVal):
        # this method should insert the node after the node with the value we pass in
        if self.head != None:
            # set the current node to head
            current_node = self.head
            # create a temp_node to keep track of current node
            temp_node = current_node

            while current_node.next != None:
                # while loop used to iterate through nodes
                # continually store temp_node to retain current node
                temp_node = current_node
                # update current_node to the next node
                current_node = current_node.next

                # if value parameter is met, insert node after node with given parameter
                if current_node.value == val:
                    # create a new node
                    new_node = Node(newVal)
                    # set the pointer of this new node to be the original pointer
                    # of the node you add in front of
                    new_node.next = current_node.next
                    # change the current nodes next pointer to the new node
                    current_node.next = new_node

        else:
            # print there are no nodes to insert and return false
            print "No Nodes to Insert"
            return False

    def remove_node_after(self, val):
        # this method should remove the node after the node with the value we pass in
        if self.head != None:
            # set the current node to head
            current_node = self.head

            while current_node.value != val:
                # while loop used to iterate through nodes as long as parameter is not satisfied
                # update current_node to the next node
                current_node = current_node.next
            # change the pointer to the pointer of the next node
            # this effectively drops the next node inline since pointer skips it
            current_node.next = current_node.next.next

        else:
            # print there are no nodes to remove and return false
            print "No Nodes to Remove"
            return False

    def find_value(self, val):
        # return True if val exists in the linked list
        # return False if val does not exist in the linked list
        if self.head != None:
            # set the current node to head
            current_node = self.head


            while current_node.next != None:
                # while loop used to iterate through nodes as long as parameter is not satisfied
                # update current_node to the next node
                current_node = current_node.next
                if current_node.value == val:
                    print "The current value of the node is", current_node.value
                    return True

            print "This node value is not in the singly linked list."
            return False

        else:
            # print there are no nodes to remove and return false
            print "No Nodes to Remove"
            return False

# creating a new instance of the Singly Linked List
sll = SinglyLinkedList()
# show how the traverse function works
sll.traverse()
sll.print_as_list()
# add more nodes and use traverse to look at all the values
sll.add_node(10)
sll.traverse()
sll.print_as_list()
sll.add_node(2)
sll.add_node(4)
sll.add_node(30)
sll.add_node(120)
sll.add_node(11)
sll.add_node(302)
sll.add_node(20)
sll.add_node(9)
sll.add_node(8002)
sll.remove_node()
sll.insert_node_after(4, 54)
sll.remove_node_after(2)
sll.traverse()
sll.print_as_list()
sll.find_value(5)
