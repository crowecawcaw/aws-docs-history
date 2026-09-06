

# Working with Numerical Data
<a name="NumericalData"></a>

**Topics**
+ [Negative Numbers Offsets](NegativeNumbersOffsets.md)
+ [Zero Padding](ZeroPadding.md)
+ [Dates](Dates.md)

Amazon SimpleDB is a schema-less data store and everything is stored as a UTF-8 string value. This provides application designers with the flexibility of enforcing data restrictions at the application layer without the data store enforcing constraints.

All comparisons are performed lexicographically. As a result, we highly recommend that you use negative number offsets, zero padding, and store dates in an appropriate format.