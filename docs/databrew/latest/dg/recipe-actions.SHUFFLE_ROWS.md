# SHUFFLE_ROWS

Shuffles values in a given column. The shuffling can occur with values grouped by a
secondary column.

###### Parameters

- `sourceColumns` – An array of existing columns.
- `groupByColumns` – An array of columns to group the source columns by while shuffling.

###### Example

```
{
   "sourceColumns": ["age"],
   "*groupByColumns*": ["country"]
}
```
