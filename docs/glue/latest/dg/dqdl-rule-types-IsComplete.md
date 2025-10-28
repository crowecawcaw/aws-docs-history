# IsComplete

Checks whether all of the values in a column are complete (non-null).

**Syntax**

```
IsComplete `<COL_NAME>`
```

- **COL_NAME** – The name of the column that you want to evaluate the data quality rule against.

**Supported column types**: Any column type
**Example: Null values**

The following example checks whether all of the values in a column named
`email` are non-null.

```
IsComplete "email"
IsComplete "Email" where "Customer_ID between 1 and 50"
IsComplete "Customer_ID"  where "Customer_ID < 16 and Customer_ID != 12"
IsComplete "passenger_count" where "payment_type<>0"

```

**Null behavior**

Note on CSV Data Formats: Blank rows on CSV columns can display multiple behaviors.

- If a column is of `String` type, the blank row will be recognized as an empty string and will
  not fail the `Completeness` rule.
- If a column is of another data type like `Int`, the blank row will be recognized as `NULL` and
  will fail the `Completeness` rule.
