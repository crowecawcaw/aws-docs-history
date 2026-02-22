# Invalid data when using Athena

with Amazon Quick Sight

An invalid data error can occur when you use any operator or function in a
calculated field. To address this, verify that the data in the table is consistent
with the format that you supplied to the function.

For example, suppose that you are using the function `parseDate(expression,
 [‘format’], [‘time_zone’])` as `parseDate(date_column,
 ‘MM/dd/yyyy’)`. In this case, all values in `date_column`
must conform to `'MM/dd/yyyy'` format (`’05/12/2016’`). Any
value that isn't in this format (`‘2016/12/05’`) can cause an
error.
