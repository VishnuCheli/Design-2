#Time Complexity:: push(): O(1), pop():O(1) , top(): O(1), getMin(): O(1), Average: O(1)
#Space Complexity:: O(n) where n is the maximum number of elements
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No

class MinStack(object):

    def __init__(self):
        self.stack = [] #initialize the main stack as list
        self.minstack= [] #initialize a min stack to keep track of the current minimum value

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val) #any element being pushed goes into the stack
        if len(self.minstack)==0: #checking if minstack is empty
            self.minstack.append(val) #if empty setting the first pushed value as the minimum
        else: #every other time you push after first push
            if self.minstack[-1]>val: #check top of minstack>pushed value
                self.minstack.append(val) #then append new min to the top of the stack
            else: #otherwise new value is more than current minimum
                self.minstack.append(self.minstack[-1])#then duplicate the current minimum value present on top of minstack
        
    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop() #removing the top element 
        self.minstack.pop() #removing top element from minstack, to keep track of the current minimum value still present in the stack
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1] #return the top element of the stack 

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1] #return the current minimum value


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()