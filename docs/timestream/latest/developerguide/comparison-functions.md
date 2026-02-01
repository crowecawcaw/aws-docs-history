For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# ALL(), ANY() and SOME()

The `ALL`, `ANY` and `SOME` quantifiers can be used
together with comparison operators in the following way.

| Expression    | Meaning                                                      |
| ------------- | ------------------------------------------------------------ |
| A = ALL(...)  | Evaluates to true when A is equal to all values.             |
| A <> ALL(...) | Evaluates to true when A does not match any value.           |
| A < ALL(...)  | Evaluates to true when A is smaller than the smallest value. |
| A = ANY(...)  | Evaluates to true when A is equal to any of the values.      |
| A <> ANY(...) | Evaluates to true when A does not match one or more values.  |
| A < ANY(...)  | Evaluates to true when A is smaller than the biggest value.  |

## Examples and usage

notes

###### Note

When using `ALL`, `ANY` or `SOME`, the keyword
`VALUES` should be used if the comparison values are a list of literals.

## Example: `ANY()`

An example of `ANY()` in a query statement as follows.

```
SELECT 11.7 = ANY (VALUES 12.0, 13.5, 11.7)
```

An alternative syntax for the same operation is as follows.

```
SELECT 11.7 = ANY (SELECT 12.0 UNION ALL SELECT 13.5 UNION ALL SELECT 11.7)
```

In this case, `ANY()` evaluates to `True`.

## Example: `ALL()`

An example of `ALL()` in a query statement as follows.

```
SELECT 17 < ALL (VALUES 19, 20, 15);
```

An alternative syntax for the same operation is as follows.

```
SELECT 17 < ALL (SELECT 19 UNION ALL SELECT 20 UNION ALL SELECT 15);
```

In this case, `ALL()` evaluates to `False`.

## Example: `SOME()`

An example of `SOME()` in a query statement as follows.

```
SELECT 50 >= SOME (VALUES 53, 77, 27);
```

An alternative syntax for the same operation is as follows.

```
SELECT 50 >= SOME (SELECT 53 UNION ALL SELECT 77 UNION ALL SELECT 27);
```

In this case, `SOME()` evaluates to `True`.
