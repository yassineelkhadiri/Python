np_height = [74 74 72  75 75 73]
np_baseball = [[ 74 180]
 [ 74 215]
 [ 72 210]

 [ 75 205]
 [ 75 190]
 [ 73 195]]
# Import numpy as np
import numpy as np 

# For loop over np_height
for x in np_height : 
    print(str(x)+" inches ")

# For loop over np_baseball
for y in np.nditer(np_baseball):
    print(y)