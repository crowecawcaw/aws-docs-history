Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Scalar Python UDF example

The following example creates a function that compares two numbers and returns the
larger value. Note that the indentation of the code between the double dollar signs
($$) is a Python requirement. For more information, see [CREATE FUNCTION](r_CREATE_FUNCTION.md "r_CREATE_FUNCTION.md").

```
create function f_py_greater (a float, b float)
  returns float
stable
as $$
  if a > b:
    return a
  return b
$$ language plpythonu;
```

The following query calls the new `f_greater` function to query the SALES
table and return either COMMISSION or 20 percent of PRICEPAID, whichever is
greater.

```
select f_py_greater (commission, pricepaid*0.20) from sales;
```
