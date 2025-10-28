# ColumnLength

Checks whether the length of each row in a column conforms to a given expression.

**Syntax**

```
ColumnLength `<COL_NAME>``<EXPRESSION>`
```

- **COL_NAME** – The name of the column that you want to evaluate the data quality rule against.

**Supported column types**: String

- **EXPRESSION** – An expression to run against the rule type response in order to produce a Boolean value. For more information, see [Expressions](dqdl.md#dqdl-syntax-rule-expressions "dqdl.md#dqdl-syntax-rule-expressions").
  **Example: Column row length**

The following example rule checks whether the value in each row in the column named
`Postal_Code` is 5 characters long.

```
ColumnLength "Postal_Code" = 5
ColumnLength "weightinkgs" = 2 where "weightinkgs > 10"
```

**Null behavior**

The `ColumnLength` rule treats `NULL`s as 0 length strings. For a `NULL` row:

```
ColumnLength "Postal_Code" > 4 # this will fail
```

```
ColumnLength "Postal_Code" < 6 # this will succeed
```

The following example compound rule provides a way to explicitly fail `NULL` values:

```
(ColumnLength "Postal_Code" > 4) AND (ColumnValues "Postal_Code" != NULL)
```
