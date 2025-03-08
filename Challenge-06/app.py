def find_first_duplicate( data: list ):

    temp_list = []

    for element in data:

        if element in temp_list:
            return element
        
        temp_list.append( element )

    return -1



list1 = [1, 2, 3, 4, 5]

list2 = [1, 2, 3, 4, 2]

print( find_first_duplicate( list1 ) )

print( find_first_duplicate( list2 ) )