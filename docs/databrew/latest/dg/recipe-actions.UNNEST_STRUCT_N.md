

# UNNEST\_STRUCT\_N
<a name="recipe-actions.UNNEST_STRUCT_N"></a>

Creates a new column for each field of a selected column of type `struct`.

For example, given the following struct:

```
            user {
               name: “Ammy” 
               address: {
                  state: "CA",
                  zipcode: 12345
               }
            }
```

This function creates 3 columns:


| user.name | user.address.state | user.address.zipcode | 
| --- | --- | --- | 
| Ammy | CA | 12345 | 

**Parameters**
+ `sourceColumns` — List of the source columns.
+ `regexColumnSelector` — A regular expression to select the columns to unnest.
+ `removeSourceColumn` — A Boolean value. If true, then remove the source column; otherwise keep it.
+ `unnestLevel` — The number of levels to unnest.
+ `delimiter` — The delimiter is used in the newly created column name to separate the different levels of the struct. For example: if the delimiter is “/”, the column name will be in this form: “user/address/state”.
+ `conditionExpressions` — Condition expressions.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "UNNEST_STRUCT_N",
        "Parameters": {
            "sourceColumns": "[\"address\"]",
            "removeSourceColumn": "true",
            "unnestLevel": "2",
            "delimiter": "/"
        }
    }
}
```