I compare the effectiveness of **bubble sorting** and **merge sorting** methods, applying to a linked list.


## Initial requirements

In the input file `input.txt` there is a long non-negative integer written on each line
(the maximum length of the number is 100 characters).

1. Read the given numbers as a **singly linked list** data structure
2. Return the given numbers in non-decreasing order.

**Extra:**
1. Hide data members in Node. Return by methods or properties;
2. Implement the LinkedList class with the methods: append, find, remove, insert, swap;
3. Try to do it through **merge sort** and **bubble sort**. Measure the time of each method.

:no_entry_sign: You cannot use built-in python types: list, all

## Guide
In the input file `input.txt ` you may specify any array that meets the requirement of the task. 
To run the script you need to call:
```
def runtime_test(sort_method, elements)
```

specifying as parameters the desired sorting method and an array of numbers from `input.txt`.
It will return the average runtime result for 1 000 000 calls.
