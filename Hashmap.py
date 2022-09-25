#Time Complexity:: hashindex(): O(1), findNode():O(n) , put(): O(n), get(): O(n), remove: O(n) ,Average: O(n)
#Space Complexity:: O(n) where n is the maximum number of elements
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No

class MyHashMap(object):
    class ListNode:
        def __init__(self,key,value):#constructor to assign attributes
            self.key = key
            self.val = value
            self.next = None
            
    def __init__(self):
        self.hashmap=[None]*10000 #Using 10^4 as the primary array size sqrt(10^6)=10^3, make it 10^4 to compensate space for time
    
    def hashindex(self,key):
        return key%10000 #returning hashindex of the linkedlist head node
    
    def findNode(self,head,key):#to return previous node of the value being searched
        prev = head #starting of the linked list represented as head so it's passed into the function to search that linked list
        curr = prev.next #to check for end of linked list
        
        while curr!=None and curr.key != key: #checking for end of linked list and if the key is already present there
            prev = curr #reassigning the prev
            curr = curr.next #reassigning the current
        return prev #returning index of the previous node
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        hash_index = self.hashindex(key) #getting location of the linked list the key value should be stored in
        if self.hashmap[hash_index]==None: #checking if the secondary array has already been created at that index
            self.hashmap[hash_index] = self.ListNode(-1,-1) #creating the linked list dummy node as we can't create node with 0
        prev = self.findNode(self.hashmap[hash_index],key)
        
        if prev.next==None: #checks for tail
            prev.next = self.ListNode(key,value) #adding
        else:
            prev.next.val = value #updates the new value into the hashindex without changing key
            
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        hash_index = self.hashindex(key)
        if self.hashmap[hash_index]== None:
            return -1 #if no node at hashindex then return '-1'
        
        prev = self.findNode(self.hashmap[hash_index],key) #findNode using head of linked list at that index and using a key
        if prev.next == None:
            return -1
        else:
            return prev.next.val #return the value in the node if node exists

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        hash_index = self.hashindex(key)
        if self.hashmap[hash_index]== None:
            return None #returns nothing since rtype is none
        
        prev = self.findNode(self.hashmap[hash_index],key)  #finding the node
        if prev.next == None:
            return None 
        else:
            prev.next = prev.next.next #breaking of the node from the chain

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)