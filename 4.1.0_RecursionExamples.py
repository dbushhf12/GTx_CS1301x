def Factorial(n):
        if n > 1:
            return n * Factorial(n-1)
        else:
            return 1

#print(Factorial(10))


def count_down(start):
    if start <= 0:
        print(start)
    else:
        print(start)
        count_down(start - 1)
count_down(5)

def count_down2(start):
    while start >= 0:
        print(start)
        start -= 1



#Let's implement the Fibonacci function we saw in the
#previous video in Python!
#
#Like our Factorial function, our Fibonacci function
#should take as input one parameter, n, an integer. It
#should calculate the nth Fibonacci number. For example,
#fib(7) should give 13 since the 7th number in
#Fibonacci's sequence is 13.

#So, our function definition will basically be the same:

def fib(n):
    #What do we want to do inside the function? Once again,
    #there are really only two cases: either we're looking
    #for the first two Fibonacci numbers, or we're not.
    #What happens if we're looking for the first two? Well,
    #we already know that the 1st and 2nd Fibonacci numbers
    #are both 1, so if n == 1 or n == 2, we can go ahead
    #and return 1.
    
    if n == 1 or n == 2:
        return 1
    
    #What if n doesn't equal 1? For any value for n greater
    #than 2, the result should be the sum of the previous
    #two numbers. The previous Fibonacci number could then
    #be calculated with the same kind of function call,
    #decrementing n by 1 or 2.
    
    else:
        return fib(n - 1) + fib(n - 2)
    
    #If n is greater than 2, then it returns the sum of the
    #previous two fibonacci numbers, as calculated by the
    #same function.

#Now let's test it out! Run this file to see the results.
print("fib(5) is", fib(5))
print("fib(10) is", fib(10))






#Write a function called linked_list_search. Your
#linked_list_search function should take two parameters:
#a single linked list node, and a search term. Your
#function should return True if the search term is the
#value of the linked list node or any node after it.
#It should return False if the value is not found in
#the linked list.

class LinkedListNode:
    def __init__(self, value, next_node = None):
        self.value = value
        self.next_node = next_node
        
#Write your function here!
def linked_list_search(node, term):
    while node.next_node:
        if node.value == term:
            return True
        else:
            return linked_list_search(node.next_node, term)
    return False


#Below are lines of code that create a linked list,
#and then search for two values in that linked list:
#one that is there, one that isn't. If your function
#works, it should print True then False.
node_7 = LinkedListNode(5)
node_6 = LinkedListNode(2, node_7)
node_5 = LinkedListNode(9, node_6)
node_4 = LinkedListNode(1, node_5)
node_3 = LinkedListNode(4, node_4)
node_2 = LinkedListNode(6, node_3)
root_node = LinkedListNode(7, node_2)

print(linked_list_search(root_node, 9))
print(linked_list_search(root_node, 3))



class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
