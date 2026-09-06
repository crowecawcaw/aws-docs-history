

# JSON\_TO\_STRUCTS
<a name="recipe-actions.JSON_TO_STRUCTS"></a>

Converts a JSON string to statically typed structs. During conversion, it detects the schema of every JSON object and merges them in order to get the most generic schema to represent the entire JSON string. The “unnestLevel” parameter specifies how many levels of JSON objects to convert to structs.

**Parameters**
+ `sourceColumns` – A list of source columns.
+ `regexColumnSelector –` A regular expression to select the columns.
+ `removeSourceColumn` – A Boolean value. If `true` then remove the source column; otherwise, keep it.
+ `unnestLevel` – The number of levels to unnest.
+ `conditionExpressions` – Condition expressions.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "JSON_TO_STRUCTS",
        "Parameters": {
            "sourceColumns": "[\"address\"]",
            "removeSourceColumn": "true",
            "unnestLevel": "2"
       }
    }
}
```