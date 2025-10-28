# ColumnDataType

Checks if the values in a given column can be cast in Apache Spark to the provided type. Accepts a `with threshold` expression to
check for a subset of the values in the column.

**Syntax**

```
ColumnDataType `<COL_NAME>` = `<EXPECTED_TYPE>`
```

- **COL_NAME** – The name of the column that you want to evaluate the data quality rule against.

Supported column types: String type

**Supported column types**: Byte, Decimal, Double, Float, Integer, Long, Short

- **EXPECTED_TYPE** – The expected type of the values in the column.

Supported values: Boolean, Date, Timestamp, Integer, Double, Float, Long

**Supported column types**: Byte, Decimal, Double, Float, Integer, Long, Short

- **EXPRESSION** – An optional expression to specify the percentage of values that should be of the expected type.

**Supported column types**: Byte, Decimal, Double, Float, Integer, Long, Short

**Example: Column data type integers as strings**

The following example rule checks whether the values in the given column, which is of type string, can be cast as integers.

```
ColumnDataType "colA" = "INTEGER"
```

**Example: Column data type integers as strings check for a subset of the values**

The following example rule checks whether more than 90% of the values in the given column, which is of type string, can be cast as integers.

```
ColumnDataType "colA" = "INTEGER" with threshold > 0.9
```
