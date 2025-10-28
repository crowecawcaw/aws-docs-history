# Aggregate functions

Aggregate functions are database operations that perform calculations across multiple
rows of data to produce a single summarized result. These functions analyze data sets to
return computed values like sums, averages, counts, or other statistical measures.

| **Function**                | **Signature**                                                                                                                    | **Description**                                           |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | -------------------------- | ----------------------------------------------------- |
| `AVG`                       | AVG (expression)                                                                                                                 | Returns the average of a numerical expression.            |
| `COUNT`                     | COUNT (expression)                                                                                                               | Returns the number of rows that match the given criteria. |
| `MAX`                       | MAX (expression)                                                                                                                 | Returns the largest value of the selected expressions.    |
| `MIN`                       | MIN (expression)                                                                                                                 | Returns the smallest value of the selected expressions.   |
| `SUM`                       | SUM (expression)                                                                                                                 | Returns the sum of a numerical expression.                |
| `STDDEV`                    | STDDEV (expression)                                                                                                              | Returns the sample standard deviation.                    |
| `GROUP BY`                  | GROUP BY expression                                                                                                              | Returns a row created by the grouping columns.            |
| `HAVING`                    | HAVING boolean-expression                                                                                                        | Returns group rows filtered by `GROUP BY` clause.         | Examples of all functions: |
| **Function**                | **Example**                                                                                                                      |                                                           | ---                        | ---                                                   |
| AVG                         | `SELECT d.asset_id, d.property_id, AVG(d.int_value) FROM raw_time_series AS d`                                                   |                                                           | COUNT                      | `SELECT COUNT(d.int_value) FROM raw_time_series AS d` |
|                             | MAX                                                                                                                              | `SELECT MAX(d.int_value) FROM raw_time_series AS d`       |
| MIN                         | `SELECT MIN(d.int_value) FROM raw_time_series AS d`                                                                              |                                                           | SUM                        | `SELECT SUM(d.int_value) FROM raw_time_series AS d`   |
|                             | STDDEV                                                                                                                           | `SELECT STDDEV(d.int_value) FROM raw_time_series AS d`    |
| <br>• GROUP BY <br>• HAVING | `SELECT MAX(d.int_value) AS max_int_value, d.asset_id FROM raw_time_series AS d GROUP BY d.asset_id HAVING MAX(d.int_value) > 5` |
