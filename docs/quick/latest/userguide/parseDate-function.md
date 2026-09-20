

# parseDate
<a name="parseDate-function"></a>

`parseDate` parses a string to determine if it contains a date value, and returns a standard date in the format `yyyy-MM-ddTkk:mm:ss.SSSZ` (using the format pattern syntax specified in [Class DateTimeFormat](http://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html) in the Joda project documentation), for example 2015-10-15T19:11:51.003Z. This function returns all rows that contain a date in a valid format and skips any rows that don't, including rows that contain null values.

Quick supports dates in the range from Jan 1, 1900 00:00:00 UTC to Dec 31, 2037 23:59:59 UTC. For more information, see [Supported date formats](https://docs.aws.amazon.com/quicksight/latest/user/supported-date-formats.html).

## Syntax
<a name="parseDate-function-syntax"></a>

```
parseDate({{expression}}, [{{'format'}}])
```

## Arguments
<a name="parseDate-function-arguments"></a>

 *expression*   
The expression must be a string. It can be the name of a field that uses the string data type, a literal value like **'1/1/2016'**, or a call to another function that outputs a string.

 *format*   
(Optional) A string containing the format pattern that *date\_string* must match. For example, if you are using a field with data like **01/03/2016**, you specify the format 'MM/dd/yyyy'. If you don't specify a format, it defaults to `yyyy-MM-dd`. Rows whose data doesn't conform to *format* are skipped.   
Different date formats are supported based on the type of dataset used. Use the following table to see details of supported date formats.  



<table>
<thead>
  <tr><th>Date source type</th><th>Supported date formats</th></tr>
</thead>
<tbody>
  <tr><td>File, Amazon Athena, and Salesforce data sets</td><td>All date format patterns specified in <a href="https://docs.aws.amazon.com/quicksight/latest/user/supported-date-formats.html">Supported date formats</a>.</td></tr>
  <tr><td>Direct query of Amazon Aurora, MariaDB, and MySQL databases</td><td> <ul><li> MM/dd/yyyy </li><li> dd/MM/yyyy </li><li> yyyy/MM/dd </li><li> MMM/dd/yyyy </li><li> dd/MMM/yyyy </li><li> yyyy/MMM/dd </li><li> MM/dd/yyyy HH:mm:ss </li><li> dd/MM/yyyy HH:mm:ss </li><li> yyyy/MM/dd HH:mm:ss </li><li> MMM/dd/yyyy HH:mm:ss </li><li> dd/MMM/yyyy HH:mm:ss </li><li> yyyy/MMM/dd HH:mm:ss </li><li> MM-dd-yyyy </li><li> dd-MM-yyyy </li><li> yyyy-MM-dd </li><li> MMM-dd-yyyy </li><li> dd-MMM-yyyy </li><li> yyyy-MMM-dd </li><li> MM-dd-yyyy HH:mm:ss </li><li> dd-MM-yyyy HH:mm:ss </li><li> yyyy-MM-dd HH:mm:ss </li><li> MMM-dd-yyyy HH:mm:ss </li><li> dd-MMM-yyyy HH:mm:ss </li><li> yyyy-MMM-dd HH:mm:ss </li><li> MM/dd/yyyy HH:mm:ss.SSS </li><li> dd/MM/yyyy HH:mm:ss.SSS </li><li> yyyy/MM/dd HH:mm:ss.SSS </li><li> MMM/dd/yyyy HH:mm:ss.SSS </li><li> dd/MMM/yyyy HH:mm:ss.SSS </li><li> yyyy/MMM/dd HH:mm:ss.SSS </li><li> MM-dd-yyyy HH:mm:ss.SSS </li><li> dd-MM-yyyy HH:mm:ss.SSS </li><li> yyyy-MM-dd HH:mm:ss.SSS </li><li> MMM-dd-yyyy HH:mm:ss.SSS </li><li> dd-MMM-yyyy HH:mm:ss.SSS </li><li> yyyy-MMM-dd HH:mm:ss.SSS </li></ul> </td></tr>
  <tr><td>Direct query of Snowflake</td><td> <ul><li> dd/MM/yyyy </li><li> dd/MM/yyyy HH:mm:ss </li><li> dd-MM-yyyy </li><li> dd-MM-yyyy HH:mm:ss </li><li> MM/dd/yyyy </li><li> MM/dd/yyyy HH:mm:ss </li><li> MM-dd-yyyy </li><li> MM-dd-yyyy HH:mm:ss </li><li> yyyy/MM/dd </li><li> yyyy/MM/dd HH:mm:ss </li><li> yyyy-MM-dd </li><li> yyyy-MM-dd HH:mm:ss </li><li> MM/dd/yyyy HH:mm:ss.SSS </li><li> dd/MM/yyyy HH:mm:ss.SSS </li><li> yyyy/MM/dd HH:mm:ss.SSS </li><li> MMM/dd/yyyy HH:mm:ss.SSS </li><li> dd/MMM/yyyy HH:mm:ss.SSS </li><li> yyyy/MMM/dd HH:mm:ss.SSS </li><li> MM-dd-yyyy HH:mm:ss.SSS </li><li> dd-MM-yyyy HH:mm:ss.SSS </li><li> yyyy-MM-dd HH:mm:ss.SSS </li><li> MMM-dd-yyyy HH:mm:ss.SSS </li><li> dd-MMM-yyyy HH:mm:ss.SSS </li><li> yyyy-MMM-dd HH:mm:ss.SSS </li></ul> </td></tr>
  <tr><td>Direct query of Microsoft SQL Server databases</td><td> <ul><li> dd-MM-yyyy </li><li> MM/dd/yyyy </li><li> dd/MM/yyyy </li><li> yyyy/MM/dd </li><li> MMM/dd/yyyy </li><li> dd/MMM/yyyy </li><li> yyyy/MMM/dd </li><li> dd/MM/yyyy HH:mm:ss </li><li> yyyy/MM/dd HH:mm:ss </li><li> MMM/dd/yyyy HH:mm:ss </li><li> dd/MMM/yyyy HH:mm:ss </li><li> yyyy/MMM/dd HH:mm:ss </li><li> MM-dd-yyyy </li><li> yyyy-MM-dd </li><li> MMM-dd-yyyy </li><li> yyyy-MMM-dd </li><li> MM-dd-yyyy HH:mm:ss </li><li> dd-MM-yyyy HH:mm:ss </li><li> yyyy-MM-dd HH:mm:ss </li><li> MMM-dd-yyyy HH:mm:ss </li><li> dd-MMM-yyyy HH:mm:ss </li><li> yyyy-MMM-dd HH:mm:ss </li><li> MM/dd/yyyy HH:mm:ss.SSS </li><li> dd/MM/yyyy HH:mm:ss.SSS </li><li> yyyy/MM/dd HH:mm:ss.SSS </li><li> MMM/dd/yyyy HH:mm:ss.SSS </li><li> dd/MMM/yyyy HH:mm:ss.SSS </li><li> yyyy/MMM/dd HH:mm:ss.SSS </li><li> MM-dd-yyyy HH:mm:ss.SSS </li><li> dd-MM-yyyy HH:mm:ss.SSS </li><li> yyyy-MM-dd HH:mm:ss.SSS </li><li> MMM-dd-yyyy HH:mm:ss.SSS </li><li> dd-MMM-yyyy HH:mm:ss.SSS </li><li> yyyy-MMM-dd HH:mm:ss.SSS </li></ul> </td></tr>
  <tr><td>Direct query of Amazon Redshift or PostgreSQL databases<br />Also, datasets from any DBMS that are stored in Quick <a href="spice.md">SPICE</a> </td><td> <ul><li> MM/dd/yyyy </li><li> dd/MM/yyyy </li><li> yyyy/MM/dd </li><li> MMM/dd/yyyy </li><li> dd/MMM/yyyy </li><li> yyyy/MMM/dd </li><li> MM/dd/yyyy HH:mm:ss </li><li> dd/MM/yyyy HH:mm:ss </li><li> yyyy/MM/dd HH:mm:ss </li><li> MMM/dd/yyyy HH:mm:ss </li><li> dd/MMM/yyyy HH:mm:ss </li><li> yyyy/MMM/dd HH:mm:ss </li><li> MM-dd-yyyy </li><li> dd-MM-yyyy </li><li> yyyy-MM-dd </li><li> MMM-dd-yyyy </li><li> dd-MMM-yyyy </li><li> yyyy-MMM-dd </li><li> MM-dd-yyyy HH:mm:ss </li><li> dd-MM-yyyy HH:mm:ss </li><li> yyyy-MM-dd HH:mm:ss </li><li> MMM-dd-yyyy HH:mm:ss </li><li> dd-MMM-yyyy HH:mm:ss </li><li> yyyy-MMM-dd HH:mm:ss </li><li> yyyyMMdd'T'HHmmss </li><li> yyyy-MM-dd'T'HH:mm:ss </li><li> MM/dd/yyyy HH:mm:ss.SSS </li><li> dd/MM/yyyy HH:mm:ss.SSS </li><li> yyyy/MM/dd HH:mm:ss.SSS </li><li> MMM/dd/yyyy HH:mm:ss.SSS </li><li> dd/MMM/yyyy HH:mm:ss.SSS </li><li> yyyy/MMM/dd HH:mm:ss.SSS </li><li> MM-dd-yyyy HH:mm:ss.SSS </li><li> dd-MM-yyyy HH:mm:ss.SSS </li><li> yyyy-MM-dd HH:mm:ss.SSS </li><li> MMM-dd-yyyy HH:mm:ss.SSS </li><li> dd-MMM-yyyy HH:mm:ss.SSS </li><li> yyyy-MMM-dd HH:mm:ss.SSS </li></ul> </td></tr>
</tbody>
</table>


## Return type
<a name="parseDate-function-return-type"></a>

Date

## Example
<a name="parseDate-function-example"></a>

The following example evaluates `prodDate` to determine if it contains date values.

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