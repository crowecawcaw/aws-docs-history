# Uniqueness

Checks the percentage of unique values in a column against a given expression. Unique
values occur exactly once.

**Syntax**

```
Uniqueness `<COL_NAME>` `<EXPRESSION>`
```

- **COL_NAME** – The name of the column that you want to evaluate the data quality rule against.

**Supported column types**: Any column type

- **EXPRESSION** – An expression to run against the rule type response in order to produce a Boolean value. For more information, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions "dqdl.md#dqdl-syntax-rule-expressions").
  **Example**

The following example rule checks whether the percentage of unique values in a column
matches certain numeric criteria.

```
Uniqueness "email" = 1.0
Uniqueness "Customer_ID" != 1.0 where "Customer_ID < 10"
```

The following example rule checks multiple columns.

```
Uniqueness "vendorid" "tpep_pickup_datetime" = 1
```

**Sample dynamic rules**

- `Uniqueness "colA" between min(last(10)) and max(last(10))`
- `Uniqueness "colA" >= avg(last(10))`
