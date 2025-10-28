# Completeness

Checks the percentage of complete (non-null) values in a column against a given
expression.

**Syntax**

```
Completeness `<COL_NAME>` `<EXPRESSION>`
```

- **COL_NAME** – The name of the column that you want to evaluate the data quality rule against.

**Supported column types**: Any column type

- **EXPRESSION** – An expression to run against the rule type response in order to produce a Boolean value. For more information, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions "dqdl.md#dqdl-syntax-rule-expressions").
  **Example: Null value percentage**

The following example rules check if more than 95 percent of the values in a column are
complete.

```
Completeness "First_Name" > 0.95
Completeness "First_Name" > 0.95 where "weightinkgs > 10"
```

**Sample dynamic rules**

- `Completeness "colA" between min(last(5)) - 1 and max(last(5)) + 1`
- `Completeness "colA" <= avg(last(10))`
  **Null behavior**

Note on CSV Data Formats: Blank rows on CSV columns can display multiple behaviors.

- If a column is of `String` type, the blank row will be recognized as an empty string and will not fail the
  `Completeness` rule.
- If a column is of another data type like `Int`, the blank row will be recognized as `NULL` and
  will fail the `Completeness` rule.
