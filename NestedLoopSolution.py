"""
Method to convert a nested for loop to single for loop using Python dictionary. Works for non-linear looping parameters.

Based on iterations of loop, the dictionary provides more iterators to use in the code. For example, when i = 1, the lookup_table returns a = 2 and b = 5.
"""
lookup_table = {
            -1: (0,-1),
            0: (1, -1),
            1: (2, 5),
            2: (2, 5),
            3: (6, 17),
            4: (8, -1),
            5: (9, -15),
            6: ('a', 'z'),
            7: (11, -1),
            # etc.
        }


for i in range(10):
  a,b = lookup_table[i]

  variable1 = a
  variable2 = b

  print(variable1 * variable2)


