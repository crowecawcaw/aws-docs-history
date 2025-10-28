# RowCountMatch

Checks the ratio of the row count of the primary dataset and the row count of a reference dataset against the given expression.

**Syntax**

```
RowCountMatch `<REFERENCE_DATASET_ALIAS>` `<EXPRESSION>`
```

- **REFERENCE_DATASET_ALIAS** – The alias of the reference dataset against which to compare row counts.

**Supported column types**: Byte, Decimal, Double, Float, Integer, Long, Short

- **EXPRESSION** – An expression to run against the rule type response in order to produce a Boolean value. For more information, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions "dqdl.md#dqdl-syntax-rule-expressions").
  **Example: Row count check against a reference dataset**

The following example rule checks whether the row count of the primary dataset is at least 90% of the row count of the reference dataset.

```
RowCountMatch "reference" >= 0.9
```
