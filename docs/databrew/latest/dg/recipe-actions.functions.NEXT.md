# NEXT

Returns a new column, where each value represents a value that is
_n_ rows later in the source column.

###### Parameters

- `sourceColumn` – The name of an existing column.
- `numRows` – A value that represents _n_
  rows earlier in the source column. For example, if `numRows` is 3,
  then `NEXT` uses the third-next `sourceColumn` value as
  the new `targetColumn` value.
- `targetColumn` – A name for the newly created column.

###### Example

```
{
    "Action": {
        "Operation": "NEXT",
        "Parameters": {
            "numRows": "1",
            "sourceColumn": "age",
            "targetColumn": "age_NEXT"
        }
    }
}
```
