

# SORT
<a name="recipe-actions.SORT"></a>

Sorts the data in one or more columns of a dataset in ascending, descending, or custom order.

**Parameters**
+ `expressions` – A string that contains one or more JSON-encoded strings representing sorting expressions.
  + `sourceColumn` – A string that contains the name of an existing column.
  + `ordering` – Ordering can be either ASCENDING or DESCENDING.
  + `nullsOrdering` – Nulls ordering can be either NULLS\_TOP or NULLS\_BOTTOM to place null or missing values at the beginning or at the bottom of the column. 
  + `customOrder` – A list of strings that defines a custom order for the string sorting. By default, strings are sorted alphabetically.
  + `isCustomOrderCaseSensitive` – Boolean. The default value is `false`.

**Example**  
  

```
{
    "RecipeAction": {
        "Operation": "SORT",
        "Parameters": {
            "expressions": "[{\"sourceColumn\": \"A\", \"ordering\": \"ASCENDING\", \"nullsOrdering\": \"NULLS_TOP\"}]",
       }
    } 
 }
```


**Example of custom sort order**  
In the following example, the customOrder expression string has the format of a list of objects. Each object describes a sorting expression for one column.  
  

```
[
  {
    "sourceColumn": "A",
    "ordering": "ASCENDING",
    "nullsOrdering": "NULLS_TOP",
  },
  {
    "sourceColumn": "B",
    "ordering": "DESCENDING",
    "nullsOrdering": "NULLS_BOTTOM",
    "customOrder": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "isCustomOrderCaseSensitive": false,
  }
]
```