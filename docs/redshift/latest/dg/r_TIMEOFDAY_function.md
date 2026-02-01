Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# TIMEOFDAY function

TIMEOFDAY is a special alias used to return the weekday, date, and time as a string
value. It returns the time of day string for the current statement,
even when it is within a transaction block.

## Syntax

```
TIMEOFDAY()
```

## Return type

VARCHAR

## Examples

The following example returns the current date and time by using the TIMEOFDAY
function.

```
`select timeofday();`

`timeofday
------------
Thu Sep 19 22:53:50.333525 2013 UTC`
```
