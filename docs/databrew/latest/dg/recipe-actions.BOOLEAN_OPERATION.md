

# BOOLEAN\_OPERATION
<a name="recipe-actions.BOOLEAN_OPERATION"></a>

Create a new column, based on the result of logical condition IF. Return true value if the boolean expression is true, false value if the boolean expression is false, or return a custom value.

**Parameters**
+ `trueValueExpression` – Result when the condition is met.
+ `falseValueExpression` – Result when the condition is not met.
+ `valueExpression` – Boolean condition.
+ `withExpressions` – Configuration for aggregate results.
+ `targetColumn` – A name for the newly created column.

You can use constant values, column references, and aggregate results in trueValueExpression, falseValueExpression and valueExpression.

**Example: Constant values**  
Values that remain unchanged, like a number or a sentence.  
  

```
{
  "RecipeStep": {
    "Action": {
      "Operation": "BOOLEAN_OPERATION",
      "Parameters": {
        "trueValueExpression": "It is true.",
        "falseValueExpression": "It is false.",
        "valueExpression": "`column.1` < 2000",
        "targetColumn": "result.column"
      }
    }
  }
}
```

**Example: Column references**  
Values that are columns in the dataset.  
  

```
{
  "RecipeStep": {
    "Action": {
      "Operation": "BOOLEAN_OPERATION",
      "Parameters": {
        "trueValueExpression": "`column.2`",
        "falseValueExpression": "`column.3`",
        "valueExpression": "`column.1` < `column.4`",
        "targetColumn": "result.column"
      }
    }
  }
}
```

**Example: Aggregate results**  
Values that are calculated by aggregate functions. An aggregate function performs a calculation on a column, and returns a single value.  
  

```
{
  "RecipeStep": {
    "Action": {
      "Operation": "BOOLEAN_OPERATION",
      "Parameters": {
        "trueValueExpression": "`:mincolumn.2`",
        "falseValueExpression": "`:maxcolumn.3`",
        "valueExpression": "`column.1` < `:avgcolumn.4`",
        "withExpressions": "[{\"name\":\"mincolumn.2\",\"value\":\"min(`column.2`)\",\"type\":\"aggregate\"},{\"name\":\"maxcolumn.3\",\"value\":\"max(`column.3`)\",\"type\":\"aggregate\"},{\"name\":\"avgcolumn.4\",\"value\":\"avg(`column.4`)\",\"type\":\"aggregate\"}]",
        "targetColumn": "result.column"
      }
    }
  }
}
```
Users need to convert the JSON to a string by escaping.  
Note that the parameter names in trueValueExpression, falseValueExpression, and valueExpression must match the names in withExpressions. To use the aggregate results from some columns, you need to create parameters for them and provide the aggregate functions.

**Example:**  

```
{
  "RecipeStep": {
    "Action": {
      "Operation": "BOOLEAN_OPERATION",
      "Parameters": {
        "trueValueExpression": "It is true.",
        "falseValueExpression": "It is false.",
        "valueExpression": "`column.1` < 2000",
        "targetColumn": "result.column"
      }
    }
  }
}
```

**Example: and/or**  
You can use and and or to combine multiple conditions.  
  

```
{
  "RecipeStep": {
    "Action": {
      "Operation": "BOOLEAN_OPERATION",
      "Parameters": {
        "trueValueExpression": "It is true.",
        "falseValueExpression": "It is false.",
        "valueExpression": "`column.1` < 2000 and `column.2` >= `column.3",
        "targetColumn": "result.column"
      }
    }
  }
}
{
  "RecipeStep": {
    "Action": {
      "Operation": "BOOLEAN_OPERATION",
      "Parameters": {
        "trueValueExpression": "`column.4`",
        "falseValueExpression": "`column.5`",
        "valueExpression": "startsWith(`column1`, 'value1') or endsWith(`column2`, 'value2')",
        "targetColumn": "result.column"
      }
    }
  }
}
```

## Valid aggregate functions
<a name="valid-aggregate-functions"></a>

The table below shows all of the valid aggregate functions that can be used in a boolean operation.



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

- ** String/Numeric/Date/Timestamp **
  - **Condition:** Is exactly / **valueExpression:** `column` = 'value' / **Description:** Condition to test if the value in column is exactly value
  - **Condition:** Is not / **valueExpression:** `column` \!= 'value' / **Description:** Condition to test if the value in column is not value
  - **Condition:** Is missing / **valueExpression:** isMissing(`column`) / **Description:** Condition to test if the value in column is missing
  - **Condition:** Is not missing / **valueExpression:** \!isMissing(`column`) / **Description:** Condition to test if the value in column is not missing
  - **Condition:** Is valid / **valueExpression:** isValid(`column`, datatype) / **Description:** Condition to test if the value in column is valid (the value is of datatype or it can be converted to datatype)
  - **Condition:** Is not valid / **valueExpression:** \!isValid(`column`, datatype) / **Description:** Condition to test if the value in column is not valid (the value is of datatype or it can be converted to datatype)

- ** Nested **
  - **Condition:** Is missing / **valueExpression:** isMissing(`column`) / **Description:** Condition to test if the value in column is missing
  - **Condition:** Is not missing / **valueExpression:** \!isMissing(`column`) / **Description:** Condition to test if the value in column is not missing
  - **Condition:** Is valid / **valueExpression:** isValid(`column`, datatype) / **Description:** Condition to test if the value in column is valid (the value is of datatype or it can be converted to datatype)
  - **Condition:** Is not valid / **valueExpression:** \!isValid(`column`, datatype) / **Description:** Condition to test if the value in column is not valid(the value is of datatype or it can be converted to datatype)

