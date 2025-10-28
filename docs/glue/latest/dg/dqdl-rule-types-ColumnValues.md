# ColumnValues

Runs an expression against the values in a column.

**Syntax**

```
ColumnValues `<COL_NAME>` `<EXPRESSION>`
```

- **COL_NAME** – The name of the column that you want to evaluate the data quality rule against.

**Supported column types**: Any column type

- **EXPRESSION** – An expression to run against the rule type response in order to produce a Boolean value. For more information, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions "dqdl.md#dqdl-syntax-rule-expressions").
  **Example: Allowed values**

The following example rule checks whether each value in the specified column is in a set
of allowed values (including null, empty, and strings with only whitespaces).

```
ColumnValues "Country" in [ "US", "CA", "UK", NULL, EMPTY, WHITESPACES_ONLY ]
ColumnValues "gender" in ["F", "M"] where "weightinkgs < 10"
```

**Example: Regular expression**

The following example rule checks the values in a column against a regular
expression.

```
`ColumnValues "First_Name" matches "[a-zA-Z]*"`
```

**Example: Date values**

The following example rule checks the values in a date column against a date
expression.

```
ColumnValues "Load_Date" > (now() - 3 days)
```

**Example: Numeric values**

The following example rule checks whether the column values match a certain numeric
constraint.

```
ColumnValues "Customer_ID" between 1 and 2000
```

**Null behavior**

For all `ColumnValues` rules (other than `!=` and `NOT IN`), `NULL`
rows will fail the rule. If the rule fails due to a null value, the failure reason will display the following:

```
Value: NULL does not meet the constraint requirement!
```

The following example compound rule provides a way to explicitly allow for `NULL` values:

```
(ColumnValues "Age" > 21) OR (ColumnValues "Age" = NULL)
```

Negated ColumnValues rules using the `!=` and `not in` syntax will pass for `NULL` rows.
For example:

```
ColumnValues "Age" != 21
```

```
ColumnValues "Age" not in [21, 22, 23]
```

The following examples provide a way to explicitly fail `NULL` values

```
(ColumnValues "Age" != 21) AND (ColumnValues "Age" != NULL)
```

```
ColumnValues "Age" not in [21, 22, 23, NULL]
```
