

# Math helpers in $util.math
<a name="math-helpers-in-util-math"></a>

**Note**  
We now primarily support the APPSYNC\_JS runtime and its documentation. Please consider using the APPSYNC\_JS runtime and its guides [here](https://docs.aws.amazon.com/appsync/latest/devguide/resolver-reference-js-version.html).

 `$util.math` contains methods to help with common Math operations. 

## $util.math utils list
<a name="math-helpers-in-util-math-list"></a>

** `$util.math.roundNum(Double) : Integer` **  
Takes a double and rounds it to the nearest integer. 

** `$util.math.minVal(Double, Double) : Double` **  
Takes two doubles and returns the minimum value between the two doubles.

** `$util.math.maxVal(Double, Double) : Double` **  
Takes two doubles and returns the maximum value between the two doubles.

** `$util.math.randomDouble() : Double` **  
Returns a random double between 0 and 1.  
This function shouldn't be used for anything that needs high entropy randomness (for example, cryptography).

** `$util.math.randomWithinRange(Integer, Integer) : Integer` **  
Returns a random integer value within the specified range, with the first argument specifying the lower value of the range and the second argument specifying the upper value of the range.   
This function shouldn't be used for anything that needs high entropy randomness (for example, cryptography).