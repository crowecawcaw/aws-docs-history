# ColumnCount

Checks the column count of the primary dataset against a given expression. In the expression, you can specify the number of columns or a range of columns using operators like `>` and `<`.

**Syntax**

```
ColumnCount `<EXPRESSION>`
```

- **EXPRESSION** – An expression to run against the rule type response in order to produce a Boolean value. For more information, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions "dqdl.md#dqdl-syntax-rule-expressions").
  **Example: Column count numeric check**

The following example rule checks whether the column count is within a given range.

```
ColumnCount between 10 and 20
```

**Sample dynamic rules**

- `ColumnCount >= avg(last(10))`
- `ColumnCount between min(last(10))-1 and max(last(10))+1`
