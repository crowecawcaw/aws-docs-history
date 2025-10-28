# UniqueValueRatio

Checks the _unique value ratio_ of a column against a
given expression. A unique value ratio is the fraction of unique values divided by the
number of all distinct values in a column. Unique values occur exactly one time, while
distinct values occur _at least_ once.

For example, the set `[a, a, b]` contains one unique value (`b`)
and two distinct values (`a` and `b`). So the unique value ratio of the
set is ½ = 0.5.

**Syntax**

```
UniqueValueRatio `<COL_NAME>` `<EXPRESSION>`

```

- **COL_NAME** – The name of the column that you want to evaluate the data quality rule against.

**Supported column types**: Any column type

- **EXPRESSION** – An expression to run against the rule type response in order to produce a Boolean value. For more information, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions "dqdl.md#dqdl-syntax-rule-expressions").
  **Example: Unique value ratio**

This example checks the unique value ratio of a column against a range of values.

```
UniqueValueRatio "test_score" between 0 and 0.5
UniqueValueRatio "Customer_ID" between 0 and 0.9 where "Customer_ID < 10"
```

**Sample dynamic rules**

- `UniqueValueRatio "colA" > avg(last(10))`
- `UniqueValueRatio "colA" <= index(last(10),2) + std(last(5))`
