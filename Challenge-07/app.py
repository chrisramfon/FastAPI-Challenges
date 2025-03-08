def check_subset( data1: list, data2: list ):

    subset = []

    for index1 in range( len ( data1 ) ):

        if data1[ index1 ] == data2[ index1 ]: subset.append( data1[ index1 ] )

        if data1 == subset: return True

    return False
    

data1 = [1, 2]
data2 = [1, 2, 3, 4]

data3 = [1, 2, 3]
data4 = [4, 3, 2, 1]

print( check_subset( data1, data2 ) )
print( check_subset( data3, data4 ) )