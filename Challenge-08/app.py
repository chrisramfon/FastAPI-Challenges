def bubble_sorting( data: list ):

    did_sort = True
    list_len = len( data )

    while( did_sort ):

        did_sort = False

        for index in range( 0, list_len ):

            if index + 1 == list_len: continue

            element_a = data[ index ]
            element_b = data[ index + 1 ]

            if element_a > element_b:
                data[ index ] = element_b
                data[ index + 1 ] = element_a
                did_sort = True
    
    return data


def bubble_sorting_two( data ):

    array_len = len( data )

    for index1 in range( array_len ):

        for index2 in range( array_len - index1 - 1 ):

            if data[ index2 ] > data[ index2 + 1]:
                temp = data[ index2 ]
                data[ index2 ] = data[ index2 + 1 ]
                data[ index2 + 1 ] = temp

    return data


list1 = [ 1, 5, 9, 6 ]
list2 = [ 9, 8, 7, 1, 10 ]
list3 = [ 7, 8, 5, 9, 3, 2, 2, 1, 4, 6 ]
print( bubble_sorting_two( list1 ) )
print( bubble_sorting_two( list2 ) )
print( bubble_sorting_two( list3 ) )
