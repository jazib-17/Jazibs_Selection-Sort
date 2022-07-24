'''
   Jazib's Implementation of the Selection Sort Algorithm

   Author: Jazib Ahmed
   Email: jazib7537@gmail.com

   All my algorithms are done by looking at diagrams, no code is looked up.
'''

# Unsorted list example
unsorted = [769, 873, 932, 422, 908, 296, 786, 431, 442, 336, 806, 205, 265, 202, 525, 302, 670, 177, 254, 760, 824, 930, 423, 254, 867, 565, 763, 415, 657, 869, 399, 752, 665, 648, 952, 887, 783, 421, 928, 685, 937, 835, 191, 138, 151, 819, 329, 501, 562, 264, 50, 311, 795, 964, 516, 770, 939, 26, 804, 349, 493, 460, 329, 168, 555, 50, 749, 107, 751, 604, 784, 312, 412, 558, 346, 441, 774, 887, 367, 798, 386, 64, 485, 494, 606, 524, 477, 133, 913, 793, 926, 23, 179, 172, 397, 800, 343, 34, 597, 862]


def selection_sort(list1):
    """
    This function takes a list and uses the selection sort algorithm to sort it.
    """

    # If statement to avoid errors with a list with 0 or 1 elements.
    if len(list1) < 2:
        return list1

    sorting = list1.copy()

    # For loop to go through each index of the list
    for i in range(0,len(sorting)):

        # Setting the current minimum to the current index
        currentmin = i

        # For loop that searches through the rest of the list to find a smaller
        # number than the current minimum and make it the minimum if so.
        for j in range(i,len(sorting)):
            if sorting[currentmin] > sorting[j]:
                currentmin = j

        # If statement that swaps the element at the current index of the list
        # with the minimum number (if there is one other than at current index)
        if currentmin != i:
            temp = sorting[i]
            sorting[i] = sorting[currentmin]
            sorting[currentmin] = temp

    return sorting


# Calling the selection_sort function to sort the unsorted list and print it
sorted = selection_sort(unsorted)
print(sorted)