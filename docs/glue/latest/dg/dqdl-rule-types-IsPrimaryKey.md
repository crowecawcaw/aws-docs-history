# IsPrimaryKey

Checks whether a column contains a primary key. A column contains a primary key if all
of the values in the column are unique and complete (non-null). You can also check for primary keys with multiple columns.

**Syntax**

```
IsPrimaryKey `<COL_NAME>`
```

- **COL_NAME** – The name of the column that you want to evaluate the data quality rule against.

**Supported column types**: Any column type
**Example: Primary key**

The following example rule checks whether the column named `Customer_ID`
contains a primary key.

```
IsPrimaryKey "Customer_ID"
IsPrimaryKey "Customer_ID" where "Customer_ID < 10"
```

**Example: Primary key with multiple columns. Any of the following examples are valid.**

```
IsPrimaryKey "colA" "colB"
IsPrimaryKey "colA" "colB" "colC"
IsPrimaryKey colA "colB" "colC"

```
