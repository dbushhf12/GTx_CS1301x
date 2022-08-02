#bubble sort
def sort_with_bubbles(lst):
    #Set swap_occurred to True to guarantee the loop runs once
    swap_occurred = True
    
    #Run the loop as long as a swap occurred the previous time
    while swap_occurred:
        
        #Start off assuming a swap did not occur
        swap_occurred = False
        
        #For every item in the list except the last one...
        for i in range(len(lst) - 1):

            #If the item should swap with the next item...
            if lst[i] > lst[i + 1]:

                #Then, swap them! But these lines aren't
                #quite right: fix this code!
                temp = lst[i]
                lst[i] = lst[i + 1]             
                lst[i + 1] = temp

                #One more line is needed here; add it!
                swap_occurred = True
    return lst

#selection sort
def sort_with_select(a_list):
    
    #For each index in the list...
    for i in range(len(a_list)):
        
        #Assume first that current item is already correct...
        minIndex = i

        #For each index from i to the end...
        for j in range(i + 1, len(a_list)):
            
            #Complete the reasoning of this conditional to
            #complete the algorithm! Remember, the goal is
            #to find the lowest item in the list between
            #index i and the end of the list, and store its
            #index in the variable minIndex.
            #
            #Write your code here!
            if a_list[minIndex] > a_list[j]:
                minIndex = j
                

        #Save the current minimum value since we're about
        #to delete it
        minValue = a_list[minIndex]
        
        #Delete the minimum value from its current index
        del a_list[minIndex]
        
        #Insert the minimum value at its new index
        a_list.insert(i, minValue)
    
    #Return the resultant list
    return a_list

#insertion sort
def insertion(lst):
    for i in range(1, len(lst)):
        j=i
        minNum=lst[j]
        while j>0 and minNum < lst[j-1]:
            lst[j] = lst[j-1]
            j-=1
        lst[j] = minNum

    return lst
print(insertion([5, 1, 3, 2, 4]))   

#insertion sort
def ins_sort(k):
    for i in range(1,len(k)):    #since we want to swap an item with previous one, we start from 1
        j = i                    #create i's copy (or not)
        temp = k[j]              #temp will be used for comparison with previous items, and sent to the place it belongs
        while j > 0 and temp < k[j-1]: #j>0 bcoz no point going till k[0] since there is no seat available on its left, for temp
            k[j] = k[j-1] #Move the bigger item 1 step right to make room for temp
            j=j-1 #take k[j] all the way left to the place where it has a smaller/no value to its left.
        k[j] = temp
    return k


    

#merge sort
def mergesort(lst):
    
    #Then, what does it do? mergesort should recursively
    #run mergesort on the left and right sides of lst until
    #it's given a list only one item. So, if lst has only
    #one item, we should just return that one-item list.
    
    if len(lst) <= 1:
        return lst
    
    #Otherwise, we should call mergesort separately on the
    #left and right sides. Since each successive call to
    #mergesort sends half as many items, we're guaranteed
    #to eventually send it a list with only one item, at
    #which point we'll stop calling mergesort again.
    else:

        #Floor division on the length of the list will
        #find us the index of the middle value.
        midpoint = len(lst) // 2

        #lst[:midpoint] will get the left side of the
        #list based on list slicing syntax. So, we want
        #to sort the left side of the list alone and
        #assign the result to the new smaller list left.
        left = mergesort(lst[:midpoint])

        #And same for the right side.
        right = mergesort(lst[midpoint:])

        #So, left and right now hold sorted lists of
        #each half of the original list. They might
        #each have only one item, or they could each
        #have several items.

        #Now we want to compare the first items in each
        #list one-by-one, adding the smaller to our new
        #result list until one list is completely empty.

        newlist = []
        while len(left) and len(right) > 0:

            #If the first number in left is lower, add
            #it to the new list and remove it from left
            if left[0] < right[0]:
                newlist.append(left[0])
                del left[0]

            #Otherwise, add the first number from right
            #to the new list and remove it from right
            else:
                newlist.append(right[0])
                del right[0]

        #When the while loop above is done, it means
        #one of the two lists is empty. Because both
        #lists were sorted, we can now add the remainder
        #of each list to the new list. The empty list
        #will have no items to add, and the non-empty
        #list will add its items in order.

        newlist.extend(left)
        newlist.extend(right)

        #newlist is now the sorted version of lst! So,
        #we can return it. If this was a recursive call
        #to mergesort, then this sends a sorted half-
        #list up the ladder. If this was the original
        #call, then this is the final sorted list.

        return newlist
