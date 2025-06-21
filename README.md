# PolylineConverter
Takes an array of vectors and converts it to a string corresponding to the relative XYZ distance of specified locations using custom parameters

- First 3 parameters represent the maximum dimensions of the X, Y, and Z area
- Next 3 parameters represent a "threshold" for calculating the processed values
- the thresholds are simply checking if a vector's value is equal to or greater than a threshold value and if so, outputs one of the 3 correlated parameter names followed by a subtraction symbol (-) and the numeric    value that the vector exceeds the threshold value by.

  Example: (1,1,1),(1,5,1),(5,5,5)
    - Param1 = 10
    - Param2 = 10
    - Param3 = 10
    - Thresh1 = 5
    - Thresh2 = 5
    - Thresh3 = 2
 
    Result = (1,1,1),(1,Param2 - 5,1),(Param1 - 5,Param1 - 5,2)

 - The first set of vectors is unchanged because none of the values met or exceeded the relevent threshold values
 - The second set has the Y value converted to its corresponding parameter name and subtracts the corresponding threshold value from it as a formula
 - The third set has the same behavior seen in vector set #2 except it now applies to both the X and Y vectors  and you can see that although the Z vectors value changed, it did not meet or exceed its corresponding threshold, thus only shows its current numerical value and not as a function being applied to a parameter
  
