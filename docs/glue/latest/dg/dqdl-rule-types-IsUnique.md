# IsUnique

Checks whether all of the values in a column are unique, and returns a Boolean
value.

**Syntax**

```
IsUnique `<COL_NAME>`
```

- **COL_NAME** – The name of the column that you want to evaluate the data quality rule against.

**Supported column types**: Any column type
**Examples**

The following example rule checks whether all of the values in a column named
`email` are unique.

```
IsUnique "email"
IsUnique "Customer_ID" where "Customer_ID < 10"]
```

The following example rule checks multiple columns.

```
IsUnique "vendorid" "tpep_pickup_datetime"
```
