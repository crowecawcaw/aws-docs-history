

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# datestyle
<a name="r_datestyle"></a>

## Values (default in bold)
<a name="t_Modifying_the_default_settings-values"></a>

 Format specification (**ISO**, Postgres, SQL, or German), and year/month/day ordering (DMY, **MDY**, YMD).
+ ISO – uses the datestyle of YYYY-MM-DD HH:MM:SS.
+ Postgres – uses the datestyle of MM-DD HH:MM:SS YYYY.
+ SQL – uses the datestyle of MM-DD-YYYY HH:MM:SS.
+ German – uses the datestyle of DD-MM-YYYY HH:MM:SS.

## Description
<a name="description"></a>

Sets the display format for date and time values and also the rules for interpreting ambiguous date input values. The string contains two parameters that you can change separately or together.

## Example
<a name="example"></a>

```
show datestyle;
DateStyle
-----------
ISO, MDY
(1 row)

set datestyle to 'SQL,DMY';
```