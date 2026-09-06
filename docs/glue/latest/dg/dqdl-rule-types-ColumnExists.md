

# ColumnExists
<a name="dqdl-rule-types-ColumnExists"></a>

Checks whether a column exists.

**Syntax**

```
ColumnExists {{<COL_NAME>}}
```
+ **COL\_NAME** – The name of the column that you want to evaluate the data quality rule against.

  **Supported column types**: Any column type

**Example: Column exists**

The following example rule checks whether the column named `Middle_Name` exists.

```
ColumnExists "Middle_Name"
```