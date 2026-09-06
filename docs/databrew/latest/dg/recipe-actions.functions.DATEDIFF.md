

# DATE\_DIFF
<a name="recipe-actions.functions.DATEDIFF"></a>

Creates a new column containing the difference between two dates.

**Parameters**
+ `sourceColumn1` – The name of an existing column.
+ `sourceColumn2` – The name of an existing column.
+ `value1` – A character string to evaluate.
+ `value2` – A character string to evaluate.
+ `units` – A unit of measure for describe the difference between the dates. Valid values are `MONTHS`, `YEARS`, `MILLISECONDS`, `QUARTERS`, `HOURS`, `MICROSECONDS`, `WEEKS`, `SECONDS`, `DAYS`, and `MINUTES`.
+ `targetColumn` – A name for the newly created column.

**Note**  
You can only specify one of the following combinations:  
Both of `sourceColumn1` and `sourceColumn2`.
One of `sourceColumn1` or `sourceColumn2` and one of `value1` or `value2`.
Both of `value1` and `value2`.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "DATE_DIFF",
        "Parameters": {
            "value1": "2020-01-01",
            "value2": "2020-10-06",
            "units": "DAYS",
            "targetColumn": "DATEDIFF Column 1"
        }
    }
}
```