# Comparison operators

AWS IoT SiteWise supports the following comparison operators. All comparison operations are
available for built in data types and evaluate to a boolean.

| Logical operators | **Operator**             | **Description** |
| ----------------- | ------------------------ | --------------- |
| `<`               | Less than                |
| `>`               | Greater than             |
| `<=`              | Less than or equal to    |
| `>=`              | Greater than or equal to |
| `=`               | Equals                   |
| `!=`              | Not equal                |

| Comparison operation truth table for non numeric values | **Type** | **Type >= x** | **Type <= x** | **Type > x** | **Type < x** | **Type = x** | **Type != x** |
| ------------------------------------------------------- | -------- | ------------- | ------------- | ------------ | ------------ | ------------ | ------------- |
| `NULL`                                                  | `FALSE`  | `FALSE`       | `FALSE`       | `FALSE`      | `FALSE`      | `TRUE`       |

Some predicates behave like operators but have special syntax. See below:

| Comparision predicates | **Operator**                    | **Description** |
| ---------------------- | ------------------------------- | --------------- |
| `IS NULL`              | Tests if a value is `NULL`.     |
| `IS NOT NULL`          | Tests if a value is not `NULL`. |

## NaN operators

`NaN`, or 'Not a Number', is a special value in floating-point arithmetic. Here is a list of `NaN`
comparisions and how they work.

- `NaN` values must be enclosed within single quotes. For example, '`NaN`'.
- `NaN` values are considered equal to each other.
- `NaN` is greater than other numeric values.
- In aggregate functions like `AVG()`, `STDDEV()`, and `SUM()`,
  if any values are `NaN`, the result is `NaN`.
- In aggregate functions like `MAX()` and `MIN()`,
  `NaN` values are included in the calculations.

| NaN value comparisions | **Comparison**                        | **Result** |
| ---------------------- | ------------------------------------- | ---------- |
| `'NaN' ≥ x`            | True                                  |
| `'NaN' ≤ x`            | True if x equals NaN, False otherwise |
| `'NaN' > x`            | False if x equals NaN, True otherwise |
| `'NaN' < x`            | False                                 |
| `'NaN' = x`            | True if x equals NaN, False otherwise |
| `'NaN' != x`           | False if x equals NaN, True otherwise |
