
def mergesort(array, byfunc=None):
    if byfunc == None: #default sorting by the elements themselves
        if len(array) > 1:
            mergesort_recursive(array, 0, len(array)-1) 

    else: #sorting with custom function 'byfunc'
        transformed_array = [] #empty list
        for item in array: #access the array
            transformed_value = byfunc(item) #apply byfunc function to each item
            transformed_array.append((transformed_value, item)) #append the transformed tuple eg (1, (1,2)), (3, (3,2)) if byfunc is return item[0]

        mergesort_recursive(transformed_array, 0, len(transformed_array)-1)

        for i in range(len(array)):
            array[i] = transformed_array[i][1] # 1 is used to access the second element of the tuple> (transformed_value, original_item)
                                                # and then the original_item is assigned to the original array




def merge(array: list, p: int, q: int, r: int) -> None:
    nleft = q-p+1
    nright = r-q
    left_array = array[p:q+1]
    right_array = array[q+1:r+1]
    left = 0
    right = 0
    dest = p
    while (left < nleft) and (right< nright):
        if left_array[left] <= right_array[right]:
            array[dest] = left_array[left]
            left += 1
        else:
            array[dest] = right_array[right]
            right +=1
        dest += 1
    while (left < nleft): #copy any elements left in left array into destination array
        array[dest] = left_array[left]
        left += 1
        dest += 1
    while (right < nright): #copy any elements left in right array into destination array
        array[dest] = right_array[right]
        right +=1      
        dest += 1
   

def mergesort_recursive(array: list, p: int, r: int) -> None:
    if r-p > 0:
        q = (p+r)//2
        mergesort_recursive(array, p, q)
        mergesort_recursive(array, q+1,r)
        merge(array,p,q,r)

 
  
  

class Stack:
  pass

class EvaluateExpression:
  pass


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





