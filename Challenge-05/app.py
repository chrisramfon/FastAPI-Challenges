
word = "hello"

word_as_array = list( word )

reversed_word = ""

for index in range( 0,  len( word_as_array ) * -1, -1 ): reversed_word = reversed_word + word[ index - 1 ]

print( reversed_word ) 

