

# percentile
<a name="percentile-function"></a>

The `percentile` function calculates the percentile of the values in measure, grouped by the dimension that's in the field well. There are two varieties of percentile calculation available in Quick:
+ [percentileCont](https://docs.aws.amazon.com/quicksight/latest/user/percentileCont-function.html) uses linear interpolation to determine result.
+ [percentileDisc (percentile)](https://docs.aws.amazon.com/quicksight/latest/user/percentileDisc-function.html) uses actual values to determine result. 

The `percentile` function is an alias of `percentileDisc`.