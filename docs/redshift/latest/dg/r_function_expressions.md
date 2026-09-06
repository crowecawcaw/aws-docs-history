

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Function expressions
<a name="r_function_expressions"></a>

## Syntax
<a name="r_function_expressions-syntax"></a>

Any built-in can be used as an expression. The syntax for a function call is the name of a function followed by its argument list in parentheses. 

```
function ( [expression [, expression...]] )
```

## Arguments
<a name="r_function_expressions-arguments"></a>

 *function*   
Any built-in function. For some example functions, see [SQL functions reference](c_SQL_functions.md).

 *expression*   
Any expression(s) matching the data type and parameter count expected by the function. 

## Examples
<a name="r_function_expressions-examples"></a>

```
abs (variable)
select avg (qtysold + 3) from sales;
select dateadd (day,30,caldate) as plus30days from date;
```