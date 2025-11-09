# ColumnCorrelation

Checks the _correlation_ between two columns against a
given expression. AWS Glue Data Quality uses the Pearson correlation coefficient to measure the linear
correlation between two columns. The result is a number between -1 and 1 that measures the
strength and direction of the relationship.

**Syntax**

```
ColumnCorrelation `<COL_1_NAME>` `<COL_2_NAME>` `<EXPRESSION>`
```

- **COL_1_NAME** – The name of the first column that you want
  to evaluate the data quality rule against.

**Supported column types**: Byte, Decimal, Double, Float, Integer, Long, Short

- **COL_2_NAME** – The name of the second column that you
  want to evaluate the data quality rule against.

**Supported column types**: Byte, Decimal, Double, Float, Integer, Long, Short

- **EXPRESSION** – An expression to run against the rule type response in order to produce a Boolean value. For more information, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions "dqdl.md#dqdl-syntax-rule-expressions").
  **Example: Column correlation**

The following example rule checks whether the correlation coefficient between the
columns `height` and `weight` has a strong positive correlation (a
coefficient value greater than 0.8).

```
ColumnCorrelation "height" "weight" > 0.8
```

```
ColumnCorrelation "weightinkgs" "Salary" > 0.8 where "weightinkgs > 40"
```

**Sample dynamic rules**

- `ColumnCorrelation "colA" "colB" between min(last(10)) and max(last(10))`
- `ColumnCorrelation "colA" "colB" < avg(last(5)) + std(last(5))`
  **Null behavior**

The `ColumnCorrelation` rule will ignore rows with `NULL` values in the calculation of the
correlation. For example:

```
+---+-----------+
|id |units      |
+---+-----------+
|100|0          |
|101|null       |
|102|20         |
|103|null       |
|104|40         |
+---+-----------+
```

Rows 101 and 103 will be ignored, and the `ColumnCorrelation` will be 1.0.
