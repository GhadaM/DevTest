##  Task 1, Searching
#### Approach
Using the keyword **in** to check if the array contains the element or not.
#### Code
```
searching.py

def searching_element(array_elements, element):
    # test element existence in the array
    if element in array_elements:
        return True
    else:
        return False
```
#### Tests
The code written above checks if an element is in the array.
```
test_searching_element.py

class TestSearchingElement(TestCase):
    def test_searching_element(self):
        self.assertEqual(searching_element([7, 8, 9, 1, 4, 6], 3), False)
        self.assertEqual(searching_element([1, 2, 3, 4, 5, 6, 0], 5), True)
```
------
##  Task 2, Books
#### Approach
Starting with a shelf of **N** books numbered from 1 
to N and assuming we only have one copy of a book ,the approach is that the slot 0 in the array needs to contain the first book and so on 
so the sorting method loops the array and checks if 
the existing book correspondence to the slot number
or not , in the later case it will finds the index of  the needed value and swaps it with the current value
- for example:

`
in: 3 1 5 4 2
`

we see here that the first slot should contain book  nb 1 so the algorithm locates the position of boob nb 1 and swaps its content with the first slot and so the first iteration results 
 `
in: 1 3 5 4 2
`
#### Code 
```
books.py

    def sort_books(books_array):
    sorting_operations = 0
    length = len(books_array)
    # loop through the array starting position 0
    for i in range(length):
        if books_array[i] != i + 1:
            # locating the index of the needed book for the current slot
            pos = books_array.index(i + 1)
            # swapping the values between the two slots
            temp = books_array[pos]
            books_array[pos] = books_array[i]
            books_array[i] = temp
            # increasing sorting_operations when a swap is done
            sorting_operations += 1
    return sorting_operations
```
#### Tests
The code written above returns the minimal number of operations required to sort books.
```
test_sort_books.py

class TestSortBooks(TestCase):
    def test_sort_books(self):
        self.assertEqual(sort_books([3, 1, 5, 4, 2]), 3)
        self.assertEqual(sort_books([7, 6, 5, 4, 3, 2, 1]), 3)
```
Using the test cases mentioned in the task, it returns *3* for the second test-case. 

