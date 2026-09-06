

# Conversion functions
<a name="chap-oracle-aurora-mysql.sql.conversionfunctions"></a>

With AWS DMS, you can transform data types between different database platforms during the migration process using conversion functions. Conversion functions define the mapping between data types in the source and target databases, allowing you to handle incompatible data types seamlessly.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Four star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-4.png)  |  ![Four star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-4.png)  | N/A | MySQL doesn’t support all functions. These unsupported functions require manual creation. | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.sql.conversionfunctions.oracle"></a>

All databases have their own conversion methods for transforming data between types and performing data manipulation. This section addresses the conversion functions `TO_CHAR` and `TO_NUMBER`.

### TO\_CHAR
<a name="chap-oracle-aurora-mysql.sql.conversionfunctions.oracle.char"></a>

 `TO_CHAR` can convert many types of data (mostly number, date, and string) to string. There are many format combinations. Some examples include:


|  `TO_CHAR` calls with strings | Results | 
| --- | --- | 
|  `to_char('0972')`  | 0972 | 
|  `to_char('0972','9999')`  | 972 | 
|  `to_char('0972','$9999.99')`  | $972.00 | 
|  `to_char('0972','$0009999.99')`  | $972.00 | 
|  `to_char('0972.48','$9999.999')`  | $972.480 | 


|  `TO_CHAR` calls with numbers | Results | 
| --- | --- | 
|  `to_char(0972)`  | 972 | 
|  `to_char(0972,'9999')`  | 972 | 
|  `to_char(0972,'$9999.99')`  | $972.00 | 
|  `to_char(0972,'$0009999.99')`  | $0000972.00 | 
|  `to_char(0972.48,'$9999.999')`  | $972.480 | 


|  `TO_CHAR` calls with date | Results | Description | 
| --- | --- | --- | 
|  `to_char(sysdate,'YYYY')`  | 2013 | Year | 
|  `to_char(sysdate,'YY')`  | 13 | Last two digits of the year | 
|  `to_char(sysdate,'YEAR')`  | TWENTY THIRTEEN | Year in words | 
|  `to_char(sysdate,'SYYYY')`  | 2017 | S prefixed (-) sign for BC | 
|  `to_char(sysdate,'Y,YYY')`  | 2017 | Year with comma | 
|  `to_char(sysdate,'MONTH')`  | SEPTEMBER | Complete month | 
|  `to_char(sysdate,'MON')`  | SEP | Three-letter month format | 
|  `to_char(sysdate,'MM')`  | 9 | Month of the year | 
|  `to_char(sysdate,'W')`  | 4 | Week of the current month | 
|  `to_char(sysdate,'WW')`  | 36 | Week of the year (1 - 53) | 
|  `to_char(sysdate,'DAY')`  | SATURDAY | Name of the day | 
|  `to_char(sysdate,'DD')`  | 30 | Day in number format | 
|  `to_char(sysdate,'D')`  | 7 | Day of the week (1 - 7) | 
|  `to_char(sysdate,'DDD')`  | 273 | Day of the year (1 - 366) | 
|  `to_char(sysdate,'DY')`  | SAT | Short form of the day | 
|  `to_char(sysdate,'HH')`  | 9 | Hour (1 - 12) | 
|  `to_char(sysdate,'HH12')`  | 9 | Hour in 12 hours format | 
|  `to_char(sysdate,'HH24')`  | 21 | Hour in 24 hours format | 
|  `to_char(sysdate,'MI')`  | 15 | Minute (0 - 59) | 
|  `to_char(sysdate,'SS')`  | 24 | Second (0 - 59) | 
|  `to_char(sysdate,'SSSSS')`  | 79100 | Seconds after midnight (0 - 86399) | 
|  `to_char(sysdate,'PM')`  | PM | AM or PM | 
|  `to_char(sysdate,'AM')`  | PM | AM or PM | 
|  `to_char(sysdate,'DL')`  | Saturday, February 23, 2017 | Date in long format | 
|  `to_char(sysdate,'Q')`  | 3 | Quarter of the Year (1 - 4) | 

### TO\_NUMBER
<a name="chap-oracle-aurora-mysql.sql.conversionfunctions.oracle.number"></a>

 `TO_NUMBER` converts one of the following to number data types: `CHAR`, `VARCHAR2`, `NCHAR`, `NVARCHAR2`, `BINARY_FLOAT`, or `BINARY_DOUBLE`. When converting one of the first four types, you can use the format parameter for the returned number.

The format parameter specifies one of the following options:


| Example data to convert | Format parameter | Results | 
| --- | --- | --- | 
| -1234567890 | 9999999999S | '1234567890-' | 
| 0 | 99.99 | ' .00' | 
| 0.1 | 99.99 | ' .10' | 
| -0.2 | 99.99 | ' -.20' | 
| 0 | 9999 | ' 0' | 
| 1 | 9999 | ' 1' | 
| 0 | B9999 | ' ' | 
| 1 | B9999 | ' 1' | 
| 123.456 | 999.999 | ' 123.456' | 
| 123.456 | FM999.009 | '123.456' | 
| 123.456 | 9.9EEEE | ' 1.2E\+02' | 
| 1.00E\+123 | 9.9EEEE | ' 1.0E\+123' | 
| 123.456 | FM9.9EEEE | '1.2E\+02' | 
| 123.45 | FM999.009 | '123.45' | 
| 123 | FM999.009 | '123.00' | 
| 123.45 | L999.99 | ' $123.45' | 
| 123.45 | FML999.99 | '$123.45' | 
| 1234567890 | 9999999999S | '1234567890\+' | 

### Examples
<a name="chap-oracle-aurora-mysql.sql.conversionfunctions.oracle.examples"></a>

The following example converts a string to a number.

```
select to_number('99999') from dual;

TO_NUMBER('99999')
99999
```

For more information, see [Functions](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Functions.html#GUID-D079EFD3-C683-441F-977E-2C9503089982) in the *Oracle documentation*.

## MySQL usage
<a name="chap-oracle-aurora-mysql.sql.conversionfunctions.mysql"></a>

For more information, see [Single-Row and Aggregate Functions](chap-oracle-aurora-mysql.sql.aggregate.md).