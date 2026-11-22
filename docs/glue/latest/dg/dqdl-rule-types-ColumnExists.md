

# ColumnExists

Checks whether a column exists.

**Syntax**

```json
ColumnExists {{<COL_NAME>}}
```
+ **COL\_NAME** – The name of the column that you want to evaluate the data quality rule against.

  **Supported column types**: Any column type

**Example: Column exists**

The following example rule checks whether the column named `Middle_Name` exists.

```json
ColumnExists "Middle_Name"
```