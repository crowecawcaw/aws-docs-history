# BOOLEAN\_OPERATION

Create a new column, based on the result of logical condition IF. Return
true value if the boolean expression is true, false value if the boolean
expression is false, or return a custom value.

###### Parameters

- `trueValueExpression` – Result when the condition is met.
- `falseValueExpression` – Result when the condition is not met.
- `valueExpression` – Boolean condition.
- `withExpressions` – Configuration for aggregate results.
- `targetColumn` – A name for the newly created column.
  You can use constant values, column references, and aggregate results in trueValueExpression,
  falseValueExpression and valueExpression.

###### Example: Constant values

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

###### Example: Column references

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

###### Example: Aggregate results

Values that are calculated by aggregate functions. An aggregate function
performs a calculation on a column, and returns a single value.

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

Note that the parameter names
in trueValueExpression, falseValueExpression, and valueExpression must match the
names in withExpressions. To use the aggregate results from some columns, you need to
create parameters for them and provide the aggregate functions.

###### Example:

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

###### Example: and/or

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

The table below shows all of the valid aggregate functions that can be used in a boolean operation.

| Column type             | Condition                         | valueExpression                                                                                                                                     | withExpressions                                                                                                   | Return value                                   |
| ----------------------- | --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| Numeric                 | Sum                               | `:sum.column.1`                                                                                                                                     | ``<br>[<br>{<br>"name": "sum.column.1",<br>"value": "sum(`column.1`)",<br>"type": "aggregate"<br>}<br>]<br>``     | Returns the sum of `column.1`                  |
| Mean                    | `:mean.column.1`                  | ``<br>[<br>{<br>"name": "mean.column.1",<br>"value": "avg(`column.1`)",<br>"type": "aggregate"<br>}<br>]<br>``                                      | Returns the mean of `column.1`                                                                                    |
| Mean absolute deviation | `:meanabsolutedeviation.column.1` | ``<br>[<br>{<br>"name": "meanabsolutedeviation.column.1",<br>"value": "mean_absolute_deviation(`column.1`)",<br>"type": "aggregate"<br>}<br>]<br>`` | Returns the mean absolute deviation of `column.1`                                                                 |
| Median                  | `:median.column.1`                | ``<br>[<br>{<br>"name": "median.column.1",<br>"value": "median(`column.1`)",<br>"type": "aggregate"<br>}<br>]<br>``                                 | Returns the median of `column.1`                                                                                  |
| Product                 | `:product.column.1`               | ``<br>[<br>{<br>"name": "product.column.1",<br>"value": "product(`column.1`)",<br>"type": "aggregate"<br>}<br>]<br>``                               | Returns the product of `column.1`                                                                                 |
| Standard deviation      | `:standarddeviation.column.1`     | ``<br>[<br>{<br>"name": "standarddeviation.column.1",<br>"value": "stddev(`column.1`)",<br>"type": "aggregate"<br>}<br>]<br>``                      | Returns the standard deviation of `column.1`                                                                      |
| Variance                | `:variance.column.1`              | ``<br>[<br>{<br>"name": "variance.column.1",<br>"value": "variance(`column.1`)",<br>"type": "aggregate"<br>}<br>]<br>``                             | Returns the variance of `column.1`                                                                                |
| Standard error of mean  | `:standarderrorofmean.column.1`   | ``<br>[<br>{<br>"name": "standarderrorofmean.column.1",<br>"value": "standard_error_of_mean(`column.1`)",<br>"type": "aggregate"<br>}<br>]<br>``    | Returns the standard error of mean of `column.1`                                                                  |
| Skewness                | `:skewness.column.1`              | ``<br>[<br>{<br>"name": "skewness.column.1",<br>"value": "skewness(`column.1`)",<br>"type": "aggregate"<br>}<br>]<br>``                             | Returns the skewness of `column.1`                                                                                |
| Kurtosis                | `:kurtosis.column.1`              | ``<br>[<br>{<br>"name": "kurtosis.column.1",<br>"value": "kurtosis(`column.1`)",<br>"type": "aggregate"<br>}<br>]<br>``                             | Returns the kurtosis of `column.1`                                                                                |
| Datetime/Numeric/Text   | Count                             | `:count.column.1`                                                                                                                                   | ``<br>[<br>{<br>"name": "count.column.1",<br>"value": "count(`column.1`)",<br>"type": "aggregate"<br>}<br>]<br>`` | Returns the total number of rows in `column.1` |
| Count distinct          | `:countdistinct.column.1`         | ``<br>[<br>{<br>"name": "count.column.1",<br>"value": "count(distinct `column.1`)",<br>"type": "aggregate"<br>}<br>]<br>``                          | Returns the total number of distinct rows in `column.1`                                                           |
| Min                     | `:min.column.1`                   | ``<br>[<br>{<br>"name": "min.column.1",<br>"value": "min(`column.1`)",<br>"type": "aggregate"<br>}<br>]<br>``                                       | Returns the minimum value of `column.1`                                                                           |
| Max                     | `:max.column.1`                   | ``<br>[<br>{<br>"name": "max.column.1",<br>"value": "max(`column.1`)",<br>"type": "aggregate"<br>}<br>]<br>``                                       | Returns the maximum value of `column.1`                                                                           |

## Valid conditions in a valueExpression

The table below shows supported conditions and the value expressions you can use.

| Column type                   | Condition                                  | valueExpression                                                                                                     | Description                                                   |
| ----------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| String                        | Contains                                   | contains(`column`, 'text')                                                                                          | Condition to test if the value in column contains text        |
| Does not contain              | !contains(`column`, 'text')                | Condition to test if the value in column is does not contain text                                                   |
| Matches                       | matches(`column`, 'pattern')               | Condition to test if the value in column matches pattern                                                            |
| Does not match                | !matches(`column`, 'pattern')              | Condition to test if the value in column does not match pattern                                                     |
| Starts with                   | startsWith(`column`, 'text')               | Condition to test if the value in column starts with text                                                           |
| Does not start with           | !startsWith(`column`, 'text')              | Condition to test if the value in column does not start with text                                                   |
| Ends with                     | endsWith(`column`, 'text')                 | Condition to test if the value in column ends with text                                                             |
| Does not end with             | !endsWith(`column`, 'text')                | Condition to test if the value in column does not end with text                                                     |
| Numeric                       | Less than                                  | `column` < number                                                                                                   | Condition to test if the value in column is less than number  |
| Less than or equal to         | `column` <= number                         | Condition to test if the value in column is less than or equal to number                                            |
| Greater than                  | `column` > number                          | Condition to test if the value in column is greater than number                                                     |
| Greater than or equal to      | `column` >= number                         | Condition to test if the value in column is greater than or equal to number                                         |
| Is between                    | isBetween(`column`, minNumber, maxNumber)  | Condition to test if the value in column is in between minNumber and maxNumber                                      |
| Is not between                | !isBetween(`column`, minNumber, maxNumber) | Condition to test if the value in column is not in between minNumber and maxNumber                                  |
| Boolean                       | Is true                                    | `column` = TRUE                                                                                                     | Condition to test if the value in column is boolean TRUE      |
| Is false                      | `column` = FALSE                           | Condition to test if the value in column is boolean FALSE                                                           |
| Date/Timestamp                | Earlier than                               | `column` < 'date'                                                                                                   | Condition to test if the value in column is earlier than date |
| Earlier than or equal to      | `column` <= 'date'                         | Condition to test if the value in column is earlier than or equal to date                                           |
| Later than                    | `column` > 'date'                          | Condition to test if the value in column is later than date                                                         |
| Later than or equal to        | `column` >= 'date'                         | Condition to test if the value in column is later than or equal to date                                             |
| String/Numeric/Date/Timestamp | Is exactly                                 | `column` = 'value'                                                                                                  | Condition to test if the value in column is exactly value     |
| Is not                        | `column` != 'value'                        | Condition to test if the value in column is not value                                                               |
| Is missing                    | isMissing(`column`)                        | Condition to test if the value in column is missing                                                                 |
| Is not missing                | !isMissing(`column`)                       | Condition to test if the value in column is not missing                                                             |
| Is valid                      | isValid(`column`, datatype)                | Condition to test if the value in column is valid (the value is of datatype or it can be converted to datatype)     |
| Is not valid                  | !isValid(`column`, datatype)               | Condition to test if the value in column is not valid (the value is of datatype or it can be converted to datatype) |
| Nested                        | Is missing                                 | isMissing(`column`)                                                                                                 | Condition to test if the value in column is missing           |
| Is not missing                | !isMissing(`column`)                       | Condition to test if the value in column is not missing                                                             |
| Is valid                      | isValid(`column`, datatype)                | Condition to test if the value in column is valid (the value is of<br>datatype or it can be converted to datatype)  |
| Is not valid                  | !isValid(`column`, datatype)               | Condition to test if the value in column is not valid(the value is of datatype or it can be converted to datatype)  |
