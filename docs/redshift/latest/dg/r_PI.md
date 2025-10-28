Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# PI function

The PI function returns the value of pi to 14 decimal places.

## Syntax

```
PI()
```

## Return type

`DOUBLE PRECISION`

## Examples

To return the value of pi, use the following example.

````
`SELECT PI();`

`+-------------------+
| pi | +-------------------+
| 3.141592653589793 | +-------------------+` ```
````
