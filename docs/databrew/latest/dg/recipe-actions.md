# ONE_HOT_ENCODING

Creates _n_ numerical columns, where _n_ is the
number of unique values in a selected categorical variable.

For example, consider a column named `shirt_size`. Shirts are available in
small, medium, large, or extra large. The column data might look like the
following.

```
shirt_size
-----------
L
XL
M
S
M
M
S
XL
M
L
XL
M
```

In this scenario, there are four distinct values for `shirt_size`.
Therefore, `ONE_HOT_ENCODING` generates four new columns. Each new column is
named `shirt_size_`x`, where
 `x``represents a distinct`shirt_size` value.

The results of `shirt_size` and the four generated columns look like
this.

```
shirt_size    shirt_size_S    shirt_size_M    shirt_size_L    shirt_size_XL
------------    ------------    ------------    ------------    -------------
L              0               0               1               0
XL             0               0               0               1
M              0               1               0               0
S              1               0               0               0
M              0               1               0               0
M              0               1               0               0
S              1               0               0               0
XL             0               0               0               1
M              0               1               0               0
L              0               0               1               0
XL             0               0               0               1
M              0               1               0               0

```

The column that you specify for `ONE_HOT_ENCODING` can have a maximum of
ten (10) distinct values.

###### Parameters

- `sourceColumn` – The name of an existing column. The column
  can have a maximum of 10 distinct values.

###### Example

```
{
    "RecipeAction": {
        "Operation": "ONE_HOT_ENCODING",
        "Parameters": {
            "sourceColumn": "shirt_size"
        }
    }
}
```
