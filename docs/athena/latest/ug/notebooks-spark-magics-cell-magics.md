# Use cell magics

Magics that are written on several lines are preceded by a double percent sign
(`%%`) and are called _cell magic functions_ or
_cell magics_.

## %%sql

This cell magic allows to run SQL statements directly without having to decorate
it with Spark SQL statement. The command also displays the output by implicitly
calling `.show()` on the returned dataframe.

![Using %%sql.](images/notebooks-spark-magics-1.png)

The `%%sql` command auto truncates column outputs to a width of 20
characters. Currently, this setting is not configurable. To work around this
limitation, use the following full syntax and modify the parameters of the
`show` method accordingly.

```
spark.sql("""`YOUR_SQL`""").show(n=`number`, truncate=`number`, vertical=`bool`)
```

- n
  `int`, optional. The number of rows to show.
- truncate – `bool` or
  `int`, optional – If `true`, truncates
  strings longer than 20 characters. When set to a number greater than 1,
  truncates long strings to the length specified and right aligns
  cells.
- vertical – `bool`,
  optional. If `true`, prints output rows vertically (one line per
  column value).
