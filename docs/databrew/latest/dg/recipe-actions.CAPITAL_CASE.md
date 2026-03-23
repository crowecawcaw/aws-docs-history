# CAPITAL_CASE

Changes each string in a column to capitalize each word. In _capital
case,_ the first letter of each word is capitalized and the rest of the
word is transformed to lowercase. An example is: The Quick Brown Fox Jumped Over The
Fence.

###### Parameters

- `sourceColumn` – The name of an existing column.

###### Example

```
{
    "RecipeAction": {
        "Operation": "CAPITAL_CASE",
        "Parameters": {
            "sourceColumn": "last_name"
        }
    }
}
```
