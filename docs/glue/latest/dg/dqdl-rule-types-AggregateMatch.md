# AggregateMatch

Checks the ratio of two column aggregations against a given expression. This ruletype works on multiple datasets. The two column aggregations are evaluated and a ratio is produced by dividing the result of the first column aggregation with the result of the second column aggregation. The ratio is checked against the provided expression to produce a boolean response.

**Syntax**

**Column aggregation**

```
AggregateMatch `<AGG_OPERATION>` (`<OPTIONAL_REFERENCE_ALIAS>`.`<COL_NAME>`)
```

- **AGG_OPERATION** – The operation to use for the aggregation. Currently, `sum` and `avg` are supported.

**Supported column types**: Byte, Decimal, Double, Float, Integer, Long, Short

- **OPTIONAL_REFERENCE_ALIAS** – This parameter needs to be provided if the column is from a reference dataset and not the primary dataset. If you are using this rule in the AWS Glue Data Catalog, your reference alias must follow the format "<database_name>.<table_name>.<column_name>

**Supported column types**: Byte, Decimal, Double, Float, Integer, Long, Short

- **COL_NAME** – The name of the column to aggregate.

**Supported column types**: Byte, Decimal, Double, Float, Integer, Long, Short
**Example: Average**

```
"avg(rating)"
```

**Example: Sum**

```
"sum(amount)"
```

**Example: Average of column in reference dataset**

```
"avg(reference.rating)"
```

**Rule**

```
AggregateMatch `<AGG_EXP_1>` `<AGG_EXP_2>` `<EXPRESSION>`
```

- **AGG_EXP_1** – The first column aggregation.

Supported column types: Byte, Decimal, Double, Float, Integer, Long, Short

**Supported column types**: Byte, Decimal, Double, Float, Integer, Long, Short

- **AGG_EXP_2** – The second column aggregation.

Supported column types: Byte, Decimal, Double, Float, Integer, Long, Short

**Supported column types**: Byte, Decimal, Double, Float, Integer, Long, Short

- **EXPRESSION** – An expression to run against the rule type response in order to produce a Boolean value. For more information, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions "dqdl.md#dqdl-syntax-rule-expressions").
  **Example: Aggregate Match using sum**

The following example rule checks whether the sum of the values in the `amount` column is exactly equal to the sum of the values in the `total_amount` column.

```
AggregateMatch "sum(amount)" "sum(total_amount)" = 1.0
```

**Example: Aggregate Match using average**

The following example rule checks whether the average of the values in the `ratings` column is equal to at least 90% of the average of the values in the `ratings` column in the `reference` dataset. The reference dataset is provided as an additional data source in the ETL or Data Catalog experience.

In AWS Glue ETL, you can use:

```
AggregateMatch "avg(ratings)" "avg(reference.ratings)" >= 0.9
```

In the AWS Glue Data Catalog, you can use:

```
AggregateMatch "avg(ratings)" "avg(database_name.tablename.ratings)" >= 0.9
```

**Null behavior**

The `AggregateMatch` rule will ignore rows with NULL values in the calculation of the
aggregation methods (sum/mean). For example:

````
+---+-----------+
|id |units      | +---+-----------+
|100|0          |
|101|null       |
|102|20         |
|103|null       |
|104|40         | +---+-----------+ ``` The mean of column `units` will be (0 + 20 + 40) / 3 = 20. Rows 101 and 103 are not considered in this calculation.
````
