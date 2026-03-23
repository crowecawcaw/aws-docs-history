# CASE_OPERATION

Create a new column, based on the result of logical condition CASE. The case operation
goes through case conditions and returns a value when the first condition is
met. Once a condition is true, the operation stops reading and returns the result.
If no conditions are true, it returns the default value.

###### Parameters

- `valueExpression` – Conditions.
- `withExpressions` – Configuration for aggregate results.
- `targetColumn` – Name for the newly created column.

###### Example

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

The table below shows all of the valid aggregate functions that can be used in a case operation.

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
| Is valid                      | isValid(`column`, datatype)                | Condition to test if the value in column is valid(the value is of datatype or it can be converted to datatype)      |
| Is not valid                  | !isValid(`column`, datatype)               | Condition to test if the value in column is not valid(the value is of datatype or it can be converted to datatype)  |
