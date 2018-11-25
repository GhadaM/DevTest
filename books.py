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
