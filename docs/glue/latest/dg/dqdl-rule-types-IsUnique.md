

# IsUnique

Checks whether all of the values in a column are unique, and returns a Boolean value.

**Syntax**

```json
IsUnique {{<COL_NAME>}}
```
+ **COL\_NAME** – The name of the column that you want to evaluate the data quality rule against.

  **Supported column types**: Any column type

**Examples**

The following example rule checks whether all of the values in a column named `email` are unique.

```json
IsUnique "email"
IsUnique "Customer_ID" where "Customer_ID < 10"
```

The following example rule checks multiple columns. 

```json
IsUnique "vendorid" "tpep_pickup_datetime"
```