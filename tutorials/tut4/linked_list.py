# tutorial 4
from typing import Any

class Node: # node object for linked list implementation
    def __init__(self, val: Any):
        if val is None:
            raise ValueError("Node 'val' cannot be None.")
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head # keeps track of head
        self.tail = self.head
        self.length = 0 # keeps track of length of linked list
        p = self.head
        while p:
            self.length += 1
            if not p.next:
                self.tail = p
            p = p.next


    def append(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            self.length += 1
            return
        self.tail.next = node # append to tail
        self.tail = node
        self.length += 1


    def remove(self, val):
        """
        Removes the first occurence of val
        """
        p = self.head
        while p.next:
            if p.next.val == val:
                p.next = p.next.next # link prev to next
                self.length -= 1
                return

                
    def display(self):
        p = self.head
        while p:
            print(p.val, end=" ")
            p = p.next
        print("")


    def move_even_items_to_back_ll(self):
        """
        Moves all even nodes to the back of LL
        """
        count = self.length
        while count > 0 and self.head.val % 2 == 0: # this block ensures head is not even
            curr = self.head # hold head temporarily in curr
            self.head = curr.next # update head
            curr.next = None # unlink curr
            self.tail.next = curr # move curr to back
            self.tail = curr # update tail
            count -= 1

        p = self.head
        while count > 1 and p and p.next: # count > 1 because head is already checked
            curr = p.next
            if curr and curr.val % 2 == 0: # if even
                p.next = p.next.next # detach curr
                curr.next = None # unlink curr
                self.tail.next = curr # move curr to back
                self.tail = curr # update tail
            else:
                p = p.next
            count -= 1


    def move_max_to_front(self):
        """
        Traverse down LL, finding max, and moving it to the front
        """
        if not self.head:
            return

        largest = self.head
        p = self.head
        prev = None # prevents crashes if head is already largest
        while p.next:
            if p.next.val > largest.val:
                prev = p # keep track of node before largest, so we can reconnect
                largest = p.next
            p = p.next

        if not prev: # exit early if head is largest
            return
        
        prev.next = prev.next.next # unlink largest from LL
        largest.next = self.head # move largest to front
        self.head = largest # update head


    def remove_duplicated_sorted_ll(self):
        """
        Removes duplicates from a sorted linked list
        """
        if not self.head:
            self.tail = None
            return
        
        p = self.head
        while p and p.next: # if p.next is None, then we are done checking
            if p.next.val == p.val: # if same, then skip
                p.next = p.next.next
                self.length -= 1
            else:
                p = p.next # traverse down LL
        self.tail = p

def test(nums):
    ll = LinkedList()
    for item in nums:
        ll.append(Node(item)) # add to LL

    # ll.display()
    # ll.move_even_items_to_back_ll()
    # ll.display()
    # ll.move_max_to_front()
    # ll.display()
    ll.remove_duplicated_sorted_ll()
    ll.display()


nums_1 = [2, 3, 4, 7, 15, 18] # initialise test list
test(nums_1)
nums_2 = [2, 4, 6, 8, 10] # initialise test list
test(nums_2)
nums_3 = [1, 2, 2, 4, 4, 5, 5]
test(nums_3)
nums_4 = [1, 4, 2]
test(nums_4)