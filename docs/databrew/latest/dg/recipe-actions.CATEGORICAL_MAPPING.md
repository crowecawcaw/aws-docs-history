

# CATEGORICAL\_MAPPING
<a name="recipe-actions.CATEGORICAL_MAPPING"></a>

Maps one or more categorical values to numeric or other values

**Parameters**
+ `sourceColumn` – The name of an existing column. 

  `categoryMap` – A JSON-encoded string representing a map of values to categories.

  `deleteOtherRows` – If `true`, all non-mapped rows will be removed from the dataset.

  `other` – When provided, all non-mapped values will be replaced by this value.

  `keepOthers` – If true, all non-mapped values will remain the same.

  `mapType` – The data type of the mapped column.

  `targetColumn` – The name of a column to contain the results.

**Example**  
  

```
{
    "Action": {
        "Operation": "CATEGORICAL_MAPPING",
        "Parameters": {
            "categoryMap": "{\"United States of America\":\"1\",\"Canada\":\"2\",\"Cuba\":\"3\",\"Haiti\":\"4\",\"Dominican Republic\":\"5\"}",
            "deleteOtherRows": "false",
            "keepOthers": "true",           
            "mapType": "NUMERIC",
            "sourceColumn": "state_name",
            "targetColumn": "state_name_mapped"
        }
    }
}
```