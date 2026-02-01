Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# datestyle

## Values (default in

bold)

Format specification (**ISO**, Postgres, SQL, or
German), and year/month/day ordering (DMY, **MDY**,
YMD).

- ISO – uses the datestyle of YYYY-MM-DD HH:MM:SS.
- Postgres – uses the datestyle of MM-DD HH:MM:SS YYYY.
- SQL – uses the datestyle of MM-DD-YYYY HH:MM:SS.
- German – uses the datestyle of DD-MM-YYYY HH:MM:SS.

## Description

Sets the display format for date and time values and also the rules for interpreting
ambiguous date input values. The string contains two parameters that you can change
separately or together.

## Example

```
show datestyle;
DateStyle
-----------
ISO, MDY
(1 row)

set datestyle to 'SQL,DMY';

```
