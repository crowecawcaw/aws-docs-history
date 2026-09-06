

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# TIMEOFDAY function
<a name="r_TIMEOFDAY_function"></a>

TIMEOFDAY is a special alias used to return the weekday, date, and time as a string value. It returns the time of day string for the current statement, even when it is within a transaction block. 

## Syntax
<a name="r_TIMEOFDAY_function-syntax"></a>

```
TIMEOFDAY()
```

## Return type
<a name="r_TIMEOFDAY_function-return-type"></a>

VARCHAR

## Examples
<a name="r_TIMEOFDAY_function-examples"></a>

The following example returns the current date and time by using the TIMEOFDAY function. 

```
select timeofday();

timeofday
------------
Thu Sep 19 22:53:50.333525 2013 UTC
```