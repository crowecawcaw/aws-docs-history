Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# GETDATE function

GETDATE returns the current date and time in the current session time zone (UTC by
default). It returns the start date or time of the current statement,
even when it is within a transaction block.

## Syntax

```
GETDATE()
```

The parentheses are required.

## Return type

TIMESTAMP

## Examples

The following example uses the GETDATE function to return the full timestamp for the
current date.

```
`select getdate();`

`timestamp
---------------------
2008-12-04 16:10:43`
```

The following example uses the GETDATE function inside the TRUNC function to return
the current date without the time.

```
`select trunc(getdate());`

`trunc
------------
2008-12-04`
```
