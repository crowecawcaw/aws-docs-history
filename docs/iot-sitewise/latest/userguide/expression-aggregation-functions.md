# Use aggregation functions in formula

expressions

In [metrics](metrics.md "metrics.md") only, you can use the following
functions that aggregate input values over each time interval and calculate a single
output value. Aggregation functions can aggregate data from associated assets.

Aggregation function arguments can be [variables](expression-variables.md "expression-variables.md"), [number literals](expression-literals.md#number-literal-definition "expression-literals.md#number-literal-definition"),
[temporal functions](expression-temporal-functions.md "expression-temporal-functions.md"), nested
expressions, or aggregation functions. The formula `max(latest(x), latest(y),
 latest(z))` uses an aggregation function as an argument and returns the
largest current value of the `x`, `y`, and `z`
properties.

You can use nested expressions in aggregation functions. When you use nested
expressions, the following rules apply:

- Each argument can have only one variable.

For example, `avg(x*(x-1))` and `sum(x/2 )/avg(y^2 )`
are supported.

For example, `min(x/y)` isn't supported.

- Each argument can have multilevel nested expressions.

For example, `sum(avg(x^2 )/2)` is supported.

- Different arguments can have different variables.

For example, `sum(x/2, y*2)` is supported.

###### Note

- If your expressions contain measurements, AWS IoT SiteWise uses the last values over
  the current time interval for the measurements to compute aggregates.
- If your expressions contain attributes, AWS IoT SiteWise uses the latest values for
  the attributes to compute aggregates.

| Function             | Description                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `avg(x0, ..., xn)`   | Returns the mean of the given variables' values over the current time<br>interval.<br>This function outputs a data point only if the given<br>variables have at least one data point over the current time interval.                                                                                                                                                                                         |
| `sum(x0, ..., xn)`   | Returns the sum of the given variables' values over the current time<br>interval.<br>This function outputs a data point only if the given<br>variables have at least one data point over the current time interval.                                                                                                                                                                                          |
| `min(x0, ..., xn)`   | Returns the minimum of the given variables' values over the current time<br>interval.<br>This function outputs a data point only if the given<br>variables have at least one data point over the current time interval.                                                                                                                                                                                      |
| `max(x0, ..., xn)`   | Returns the maximum of the given variables' values over the current time<br>interval.<br>This function outputs a data point only if the given<br>variables have at least one data point over the current time interval.                                                                                                                                                                                      |
| `count(x0, ..., xn)` | Returns the total number of data points for the given variables over the<br>current time interval. For more information about how to count the number of<br>data points that meet a condition, see [Count data points that match a condition](expression-tutorials.md#count-filtered-data "expression-tutorials.md#count-filtered-data").<br>This function computes a data point for every time<br>interval. |
| `stdev(x0, ..., xn)` | Returns the standard deviation of the given variables' values over the current time interval.<br>This function outputs a data point only if the given variables have at least one data point over the current time interval.                                                                                                                                                                                 |
