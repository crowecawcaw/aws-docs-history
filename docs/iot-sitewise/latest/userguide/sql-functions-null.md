# Null data functions

Null data functions handle or manipulate NULL values, which represent the absence
of a value. The functions allow you to replace NULLs with other values, check if a value
is NULL, or perform operations that handle NULLs in a specific way.

| **Function** | **Signature**                                         | **Description**                                                                                  |
| ------------ | ----------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `COALESCE`   | COALESCE (expression1, expression2, ..., expressionN) | If all expressions evaluate to null, COALESCE returns null. Expressions<br>must be of same type. |

###### Example of a COALESCE function

```
SELECT COALESCE (l.double_value, 100) AS non_double_value FROM latest_value_time_series AS l LIMIT 1
```
