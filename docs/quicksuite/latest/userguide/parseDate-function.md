# parseDate

`parseDate` parses a string to determine if it contains a date value,
and returns a standard date in the format `yyyy-MM-ddTkk:mm:ss.SSSZ`
(using the format pattern syntax specified in [Class DateTimeFormat](http://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html "http://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html") in the Joda project documentation), for example
2015-10-15T19:11:51.003Z. This function returns all rows that contain a date in a
valid format and skips any rows that don't, including rows that contain null
values.

Quick Suite supports dates in the range from Jan 1, 1900 00:00:00 UTC to Dec
31, 2037 23:59:59 UTC. For more information, see [Supported date formats](../../../quicksight/latest/user/supported-date-formats.md "../../../quicksight/latest/user/supported-date-formats.md").

## Syntax

```
parseDate(`expression`, [`'format'`])
```

## Arguments

_expression_

The expression must be a string. It can be the name of a field
that uses the string data type, a literal value like
`'1/1/2016'`, or a call to another function
that outputs a string.

_format_

(Optional) A string containing the format pattern that
_date_string_ must match. For example, if you
are using a field with data like `01/03/2016`,
you specify the format 'MM/dd/yyyy'. If you don't specify a
format, it defaults to `yyyy-MM-dd`. Rows whose data
doesn't conform to _format_ are skipped.

Different date formats are supported based on the type of dataset
used. Use the following table to see details of supported date
formats.

| Date source type                                                                                                                                          | Supported date formats                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| File, Amazon Athena, and Salesforce data<br>sets                                                                                                          | All date format patterns specified in [Supported date<br>formats](../../../quicksight/latest/user/supported-date-formats.md "../../../quicksight/latest/user/supported-date-formats.md").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Direct query of Amazon Aurora, MariaDB, and MySQL<br>databases                                                                                            | • MM/dd/yyyy<br>• dd/MM/yyyy<br>• yyyy/MM/dd<br>• MMM/dd/yyyy<br>• dd/MMM/yyyy<br>• yyyy/MMM/dd<br>• MM/dd/yyyy HH:mm:ss<br>• dd/MM/yyyy HH:mm:ss<br>• yyyy/MM/dd HH:mm:ss<br>• MMM/dd/yyyy HH:mm:ss<br>• dd/MMM/yyyy HH:mm:ss<br>• yyyy/MMM/dd HH:mm:ss<br>• MM-dd-yyyy<br>• dd-MM-yyyy<br>• yyyy-MM-dd<br>• MMM-dd-yyyy<br>• dd-MMM-yyyy<br>• yyyy-MMM-dd<br>• MM-dd-yyyy HH:mm:ss<br>• dd-MM-yyyy HH:mm:ss<br>• yyyy-MM-dd HH:mm:ss<br>• MMM-dd-yyyy HH:mm:ss<br>• dd-MMM-yyyy HH:mm:ss<br>• yyyy-MMM-dd HH:mm:ss<br>• MM/dd/yyyy HH:mm:ss.SSS<br>• dd/MM/yyyy HH:mm:ss.SSS<br>• yyyy/MM/dd HH:mm:ss.SSS<br>• MMM/dd/yyyy HH:mm:ss.SSS<br>• dd/MMM/yyyy HH:mm:ss.SSS<br>• yyyy/MMM/dd HH:mm:ss.SSS<br>• MM-dd-yyyy HH:mm:ss.SSS<br>• dd-MM-yyyy HH:mm:ss.SSS<br>• yyyy-MM-dd HH:mm:ss.SSS<br>• MMM-dd-yyyy HH:mm:ss.SSS<br>• dd-MMM-yyyy HH:mm:ss.SSS<br>• yyyy-MMM-dd HH:mm:ss.SSS                                                   |
| Direct query of Snowflake                                                                                                                                 | • dd/MM/yyyy<br>• dd/MM/yyyy HH:mm:ss<br>• dd-MM-yyyy<br>• dd-MM-yyyy HH:mm:ss<br>• MM/dd/yyyy<br>• MM/dd/yyyy HH:mm:ss<br>• MM-dd-yyyy<br>• MM-dd-yyyy HH:mm:ss<br>• yyyy/MM/dd<br>• yyyy/MM/dd HH:mm:ss<br>• yyyy-MM-dd<br>• yyyy-MM-dd HH:mm:ss<br>• MM/dd/yyyy HH:mm:ss.SSS<br>• dd/MM/yyyy HH:mm:ss.SSS<br>• yyyy/MM/dd HH:mm:ss.SSS<br>• MMM/dd/yyyy HH:mm:ss.SSS<br>• dd/MMM/yyyy HH:mm:ss.SSS<br>• yyyy/MMM/dd HH:mm:ss.SSS<br>• MM-dd-yyyy HH:mm:ss.SSS<br>• dd-MM-yyyy HH:mm:ss.SSS<br>• yyyy-MM-dd HH:mm:ss.SSS<br>• MMM-dd-yyyy HH:mm:ss.SSS<br>• dd-MMM-yyyy HH:mm:ss.SSS<br>• yyyy-MMM-dd HH:mm:ss.SSS                                                                                                                                                                                                                                                                                                                     |
| Direct query of Microsoft SQL Server<br>databases                                                                                                         | • dd-MM-yyyy<br>• MM/dd/yyyy<br>• dd/MM/yyyy<br>• yyyy/MM/dd<br>• MMM/dd/yyyy<br>• dd/MMM/yyyy<br>• yyyy/MMM/dd<br>• dd/MM/yyyy HH:mm:ss<br>• yyyy/MM/dd HH:mm:ss<br>• MMM/dd/yyyy HH:mm:ss<br>• dd/MMM/yyyy HH:mm:ss<br>• yyyy/MMM/dd HH:mm:ss<br>• MM-dd-yyyy<br>• yyyy-MM-dd<br>• MMM-dd-yyyy<br>• yyyy-MMM-dd<br>• MM-dd-yyyy HH:mm:ss<br>• dd-MM-yyyy HH:mm:ss<br>• yyyy-MM-dd HH:mm:ss<br>• MMM-dd-yyyy HH:mm:ss<br>• dd-MMM-yyyy HH:mm:ss<br>• yyyy-MMM-dd HH:mm:ss<br>• MM/dd/yyyy HH:mm:ss.SSS<br>• dd/MM/yyyy HH:mm:ss.SSS<br>• yyyy/MM/dd HH:mm:ss.SSS<br>• MMM/dd/yyyy HH:mm:ss.SSS<br>• dd/MMM/yyyy HH:mm:ss.SSS<br>• yyyy/MMM/dd HH:mm:ss.SSS<br>• MM-dd-yyyy HH:mm:ss.SSS<br>• dd-MM-yyyy HH:mm:ss.SSS<br>• yyyy-MM-dd HH:mm:ss.SSS<br>• MMM-dd-yyyy HH:mm:ss.SSS<br>• dd-MMM-yyyy HH:mm:ss.SSS<br>• yyyy-MMM-dd HH:mm:ss.SSS                                                                                             |
| Direct query of Amazon Redshift or PostgreSQL<br>databases<br>Also, datasets from any DBMS that are stored<br>in Quick Suite [SPICE](spice.md "spice.md") | • MM/dd/yyyy<br>• dd/MM/yyyy<br>• yyyy/MM/dd<br>• MMM/dd/yyyy<br>• dd/MMM/yyyy<br>• yyyy/MMM/dd<br>• MM/dd/yyyy HH:mm:ss<br>• dd/MM/yyyy HH:mm:ss<br>• yyyy/MM/dd HH:mm:ss<br>• MMM/dd/yyyy HH:mm:ss<br>• dd/MMM/yyyy HH:mm:ss<br>• yyyy/MMM/dd HH:mm:ss<br>• MM-dd-yyyy<br>• dd-MM-yyyy<br>• yyyy-MM-dd<br>• MMM-dd-yyyy<br>• dd-MMM-yyyy<br>• yyyy-MMM-dd<br>• MM-dd-yyyy HH:mm:ss<br>• dd-MM-yyyy HH:mm:ss<br>• yyyy-MM-dd HH:mm:ss<br>• MMM-dd-yyyy HH:mm:ss<br>• dd-MMM-yyyy HH:mm:ss<br>• yyyy-MMM-dd HH:mm:ss<br>• yyyyMMdd'T'HHmmss<br>• yyyy-MM-dd'T'HH:mm:ss<br>• MM/dd/yyyy HH:mm:ss.SSS<br>• dd/MM/yyyy HH:mm:ss.SSS<br>• yyyy/MM/dd HH:mm:ss.SSS<br>• MMM/dd/yyyy HH:mm:ss.SSS<br>• dd/MMM/yyyy HH:mm:ss.SSS<br>• yyyy/MMM/dd HH:mm:ss.SSS<br>• MM-dd-yyyy HH:mm:ss.SSS<br>• dd-MM-yyyy HH:mm:ss.SSS<br>• yyyy-MM-dd HH:mm:ss.SSS<br>• MMM-dd-yyyy HH:mm:ss.SSS<br>• dd-MMM-yyyy HH:mm:ss.SSS<br>• yyyy-MMM-dd HH:mm:ss.SSS |

## Return type

Date

## Example

The following example evaluates `prodDate` to determine if it
contains date values.

```
parseDate(prodDate, 'MM/dd/yyyy')
```

The following are the given field values.

```
prodDate
--------
01-01-1999
12/31/2006
1/18/1982
7/4/2010
```

For these field values, the following rows are returned.

```
12-31-2006T00:00:00.000Z
01-18-1982T00:00:00.000Z
07-04-2010T00:00:00.000Z
```
