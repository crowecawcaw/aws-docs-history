# RowCount

Checks the row count of a dataset against a given expression. In the expression, you can
specify the number of rows or a range of rows using operators like `>` and
`<`.

**Syntax**

```
RowCount `<EXPRESSION>`
```

- **EXPRESSION** – An expression to run against the rule type response in order to produce a Boolean value. For more information, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions "dqdl.md#dqdl-syntax-rule-expressions").
  **Example: Row count numeric check**

The following example rule checks whether the row count is within a given range.

```
RowCount between 10 and 100
RowCount between 1 and 50 where "Customer_ID < 10"
```

**Sample dynamic rules**

```
RowCount > avg(last(10)) *0.8
```
