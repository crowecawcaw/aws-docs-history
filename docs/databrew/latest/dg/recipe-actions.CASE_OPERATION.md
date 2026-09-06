

# CASE\_OPERATION
<a name="recipe-actions.CASE_OPERATION"></a>

Create a new column, based on the result of logical condition CASE. The case operation goes through case conditions and returns a value when the first condition is met. Once a condition is true, the operation stops reading and returns the result. If no conditions are true, it returns the default value.

**Parameters**
+ `valueExpression` – Conditions.
+ `withExpressions` – Configuration for aggregate results.
+ `targetColumn` – Name for the newly created column.

**Example**  
  

```
{
  "RecipeStep": {
    "Action": {
      "Operation": "CASE_OPERATION",
      "Parameters": {
        "valueExpression": "case when `column11` < `column.2` then 'result1' when `column2` < 'value2' then 'result2' else 'high' end",
        "targetColumn": "result.column"
      }
    }
  }
}
```

## Valid aggregate functions
<a name="valid-aggregate-functions"></a>

The table below shows all of the valid aggregate functions that can be used in a case operation.



- ** Numeric **
  - **Condition:** Sum / **valueExpression:** `:sum.column.1` / **withExpressions:**  <pre>[<br />   {<br />      "name": "sum.column.1",<br />      "value": "sum(`column.1`)",<br />      "type": "aggregate"<br />   }<br />]</pre>  / **Return value:** Returns the sum of `column.1`
  - **Condition:** Mean / **valueExpression:** `:mean.column.1` / **withExpressions:**  <pre>[<br />   {    <br />      "name": "mean.column.1",    <br />      "value": "avg(`column.1`)",    <br />      "type": "aggregate"  <br />   }<br />]</pre>  / **Return value:** Returns the mean of `column.1`
  - **Condition:** Mean absolute deviation / **valueExpression:** `:meanabsolutedeviation.column.1` / **withExpressions:**  <pre>[<br />   {    <br />      "name": "meanabsolutedeviation.column.1",<br />      "value": "mean_absolute_deviation(`column.1`)",<br />      "type": "aggregate"<br />   }<br />]</pre>  / **Return value:** Returns the mean absolute deviation of `column.1`
  - **Condition:** Median / **valueExpression:** `:median.column.1` / **withExpressions:**  <pre>[<br />   {<br />      "name": "median.column.1",<br />      "value": "median(`column.1`)",<br />      "type": "aggregate"<br />   }<br />]</pre>  / **Return value:** Returns the median of `column.1`
  - **Condition:** Product / **valueExpression:** `:product.column.1` / **withExpressions:**  <pre>[<br />   {<br />      "name": "product.column.1",<br />      "value": "product(`column.1`)",<br />      "type": "aggregate"<br />   }<br />]</pre>  / **Return value:** Returns the product of `column.1`
  - **Condition:** Standard deviation / **valueExpression:** `:standarddeviation.column.1` / **withExpressions:**  <pre>[<br />   {<br />      "name": "standarddeviation.column.1",<br />      "value": "stddev(`column.1`)",<br />      "type": "aggregate"<br />   }<br />]</pre>  / **Return value:** Returns the standard deviation of `column.1`
  - **Condition:** Variance / **valueExpression:** `:variance.column.1` / **withExpressions:**  <pre>[<br />   {<br />      "name": "variance.column.1",<br />      "value": "variance(`column.1`)",<br />      "type": "aggregate"<br />   }<br />]</pre>  / **Return value:** Returns the variance of `column.1`
  - **Condition:** Standard error of mean / **valueExpression:** `:standarderrorofmean.column.1` / **withExpressions:**  <pre>[<br />   {<br />   "name": "standarderrorofmean.column.1",<br />   "value": "standard_error_of_mean(`column.1`)",<br />   "type": "aggregate"<br />   }<br />]</pre>  / **Return value:** Returns the standard error of mean of `column.1`
  - **Condition:** Skewness / **valueExpression:** `:skewness.column.1` / **withExpressions:**  <pre>[<br />   {<br />      "name": "skewness.column.1",<br />      "value": "skewness(`column.1`)",<br />      "type": "aggregate"<br />   }<br />]</pre>  / **Return value:** Returns the skewness of `column.1`
  - **Condition:** Kurtosis / **valueExpression:** `:kurtosis.column.1` / **withExpressions:**  <pre>[<br />   {<br />      "name": "kurtosis.column.1",<br />      "value": "kurtosis(`column.1`)",<br />      "type": "aggregate"<br />   }<br />]</pre>  / **Return value:** Returns the kurtosis of `column.1`

- ** Datetime/Numeric/Text **
  - **Condition:** Count / **valueExpression:** `:count.column.1` / **withExpressions:**  <pre>[<br />   {<br />      "name": "count.column.1",<br />      "value": "count(`column.1`)",<br />      "type": "aggregate"<br />   }<br />]</pre>  / **Return value:** Returns the total number of rows in `column.1`
  - **Condition:** Count distinct / **valueExpression:** `:countdistinct.column.1` / **withExpressions:**  <pre>[<br />   {<br />      "name": "count.column.1",<br />      "value": "count(distinct `column.1`)",<br />      "type": "aggregate"<br />   }<br />]</pre>  / **Return value:** Returns the total number of distinct rows in `column.1`
  - **Condition:** Min / **valueExpression:** `:min.column.1` / **withExpressions:**  <pre>[<br />   {<br />      "name": "min.column.1",<br />      "value": "min(`column.1`)",<br />      "type": "aggregate"<br />   }<br />]</pre>  / **Return value:** Returns the minimum value of `column.1`
  - **Condition:** Max / **valueExpression:** `:max.column.1` / **withExpressions:**  <pre>[<br />   {<br />      "name": "max.column.1",<br />      "value": "max(`column.1`)",<br />      "type": "aggregate"<br />   }<br />]</pre>  / **Return value:** Returns the maximum value of `column.1`



## Valid conditions in a valueExpression
<a name="valid-conditions-table"></a>

The table below shows supported conditions and the value expressions you can use.



- ** String **
  - **Condition:** Contains / **valueExpression:** contains(`column`, 'text') / **Description:** Condition to test if the value in column contains text
  - **Condition:** Does not contain / **valueExpression:** \!contains(`column`, 'text') / **Description:** Condition to test if the value in column is does not contain text
  - **Condition:** Matches / **valueExpression:** matches(`column`, 'pattern') / **Description:** Condition to test if the value in column matches pattern
  - **Condition:** Does not match / **valueExpression:** \!matches(`column`, 'pattern') / **Description:** Condition to test if the value in column does not match pattern
  - **Condition:** Starts with / **valueExpression:** startsWith(`column`, 'text') / **Description:** Condition to test if the value in column starts with text
  - **Condition:** Does not start with / **valueExpression:** \!startsWith(`column`, 'text') / **Description:** Condition to test if the value in column does not start with text
  - **Condition:** Ends with / **valueExpression:** endsWith(`column`, 'text') / **Description:** Condition to test if the value in column ends with text
  - **Condition:** Does not end with / **valueExpression:** \!endsWith(`column`, 'text') / **Description:** Condition to test if the value in column does not end with text

- ** Numeric **
  - **Condition:** Less than / **valueExpression:** `column` < number / **Description:** Condition to test if the value in column is less than number
  - **Condition:** Less than or equal to / **valueExpression:** `column` <= number / **Description:** Condition to test if the value in column is less than or equal to number
  - **Condition:** Greater than / **valueExpression:** `column` > number / **Description:** Condition to test if the value in column is greater than number
  - **Condition:** Greater than or equal to / **valueExpression:** `column` >= number / **Description:** Condition to test if the value in column is greater than or equal to number
  - **Condition:** Is between / **valueExpression:** isBetween(`column`, minNumber, maxNumber) / **Description:** Condition to test if the value in column is in between minNumber and maxNumber
  - **Condition:** Is not between / **valueExpression:** \!isBetween(`column`, minNumber, maxNumber) / **Description:** Condition to test if the value in column is not in between minNumber and maxNumber

- ** Boolean **
  - **Condition:** Is true / **valueExpression:** `column` = TRUE / **Description:** Condition to test if the value in column is boolean TRUE
  - **Condition:** Is false / **valueExpression:** `column` = FALSE / **Description:** Condition to test if the value in column is boolean FALSE

- ** Date/Timestamp **
  - **Condition:** Earlier than / **valueExpression:** `column` < 'date' / **Description:** Condition to test if the value in column is earlier than date
  - **Condition:** Earlier than or equal to / **valueExpression:** `column` <= 'date' / **Description:** Condition to test if the value in column is earlier than or equal to date
  - **Condition:** Later than / **valueExpression:** `column` > 'date' / **Description:** Condition to test if the value in column is later than date
  - **Condition:** Later than or equal to / **valueExpression:** `column` >= 'date' / **Description:** Condition to test if the value in column is later than or equal to date

- **  String/Numeric/Date/Timestamp **
  - **Condition:** Is exactly / **valueExpression:** `column` = 'value' / **Description:** Condition to test if the value in column is exactly value
  - **Condition:** Is not / **valueExpression:** `column` \!= 'value' / **Description:** Condition to test if the value in column is not value
  - **Condition:** Is missing / **valueExpression:** isMissing(`column`) / **Description:** Condition to test if the value in column is missing
  - **Condition:** Is not missing / **valueExpression:** \!isMissing(`column`) / **Description:** Condition to test if the value in column is not missing
  - **Condition:** Is valid / **valueExpression:** isValid(`column`, datatype) / **Description:** Condition to test if the value in column is valid (the value is of datatype or it can be converted to datatype)
  - **Condition:** Is not valid / **valueExpression:** \!isValid(`column`, datatype) / **Description:** Condition to test if the value in column is not valid (the value is of datatype or it can be converted to datatype)

- ** Nested **
  - **Condition:** Is missing / **valueExpression:** isMissing(`column`) / **Description:** Condition to test if the value in column is missing
  - **Condition:** Is not missing / **valueExpression:** \!isMissing(`column`) / **Description:** Condition to test if the value in column is not missing
  - **Condition:** Is valid / **valueExpression:** isValid(`column`, datatype) / **Description:** Condition to test if the value in column is valid(the value is of datatype or it can be converted to datatype)
  - **Condition:** Is not valid / **valueExpression:** \!isValid(`column`, datatype) / **Description:** Condition to test if the value in column is not valid(the value is of datatype or it can be converted to datatype)

