

# REPLACE\_WITH\_RANDOM\_DATE\_BETWEEN
<a name="recipe-actions.REPLACE_WITH_RANDOM_DATE_BETWEEN"></a>

Replaces values with a random date.

**Parameters**
+ `startDate` – The start of the range of dates from which a random date will be taken.
+ `sourceColumns` – A list of existing column names.
+ `endDate` – The end of the range of dates from which a random date will be taken.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "REPLACE_WITH_RANDOM_DATE_BETWEEN",
        "Parameters": {
            "startDate": "2020-12-12 12:12:12",
            "sourceColumns": ["column1", "column2"],
            "endDate": "2021-12-12 12:12:12"
        }
    }
}
```