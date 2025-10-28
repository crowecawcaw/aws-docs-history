# Mean

Checks whether the mean (average) of all the values in a column matches a given
expression.

**Syntax**

```
Mean `<COL_NAME>` `<EXPRESSION>`
```

- **COL_NAME** – The name of the column that you want to evaluate the data quality rule against.

**Supported column types**: Byte, Decimal, Double, Float, Integer, Long, Short

- **EXPRESSION** – An expression to run against the rule type response in order to produce a Boolean value. For more information, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions "dqdl.md#dqdl-syntax-rule-expressions").
  **Example: Average value**

The following example rule checks whether the average of all of the values in a column
exceeds a threshold.

```
Mean "Star_Rating" > 3
Mean "Salary" < 6200 where "Customer_ID < 10"
```

**Sample dynamic rules**

- `Mean "colA" > avg(last(10)) + std(last(2))`
- `Mean "colA" between min(last(5)) - 1 and max(last(5)) + 1`
  **Null behavior**

The `Mean` rule will ignore rows with `NULL` values in the calculation of the mean. For example:

````
+---+-----------+
|id |units      | +---+-----------+
|100|0          |
|101|null       |
|102|20         |
|103|null       |
|104|40         | +---+-----------+ ``` The mean of column `units` will be (0 + 20 + 40) / 3 = 20. Rows 101 and 103 are not considered in this calculation.
````
