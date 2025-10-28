# ColumnNamesMatchPattern

Checks whether the names of all columns in the primary dataset match the given regular expression.

**Syntax**

```
ColumnNamesMatchPattern `<PATTERN>`
```

- **PATTERN** – The pattern you want to evaluate the data quality rule against.

**Supported column types**: Byte, Decimal, Double, Float, Integer, Long, Short
**Example: Column names match pattern**

The following example rule checks whether all columns start with the prefix "aws\_"

```
ColumnNamesMatchPattern "aws_.*"
ColumnNamesMatchPattern "aws_.*" where "weightinkgs > 10"

```
