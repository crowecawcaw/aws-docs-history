

# Single-row and aggregate Oracle and MySQL functions
<a name="chap-oracle-aurora-mysql.sql.aggregate"></a>

Single-row and aggregate functions are essential SQL constructs that perform operations on individual rows or groups of rows, respectively. The following sections compare Oracle and MySQL single-row and aggregate functions.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Four star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-4.png)  |  ![Four star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-4.png)  | N/A | MySQL doesn’t support all functions. These unsupported functions require manual creation. | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.sql.aggregate.oracle"></a>

Oracle provides two main categories of built-in SQL functions based on the number of rows used as input and generated as output.
+  **Single-row** or scalar functions return a single result for each row of the queried table or view. You can use them with a `SELECT` statement in the `WHERE` clause, the `START WITH` clause, the `CONNECT BY` clause, and the `HAVING` clause. The single-row functions are divided into groups according to data types such as `NUMERIC` functions, `CHAR` functions, and `DATETIME` functions.
+  **Aggregative** or group functions are used to summarize a group of values into a single result. Examples include `AVG`, `MIN`, `MAX`, `SUM`, `COUNT`, `LISTAGG`, `FIRST`, and `LAST`.

See the following section for a comparison of Oracle and MySQL single-row functions.

Oracle 19 adds ability to eliminate duplicate items in `LISTAGG` function results with new `DISTINCT` keyword.

Oracle 19 introduces several new bitmap SQL aggregate functions such as `BITMAP_BUCKET_NUMBER`, `BITMAP_BIT_POSITION` and `BITMAP_CONSTRUCT_AGG`. These functions help speed up `COUNT DISTINCT` operations.

For more information, see [Single-Row Functions](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Single-Row-Functions.html#GUID-B93F789D-B486-49FF-B0CD-0C6181C5D85C) and [Aggregate Functions](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Aggregate-Functions.html#GUID-62BE676BAF18-4E63-BD14-25206FEA0848) in *Oracle documentation*.

## MySQL usage
<a name="chap-oracle-aurora-mysql.sql.aggregate.mysql"></a>

MySQL provides an extensive list of single-row and aggregation functions. Some are similar to their Oracle counterparts by name and functionality, or under a different name but with similar functionality. Other functions can have identical names to their Oracle counterparts, but exhibit different functionality. In the following tables, the Equivalent column indicates functional equivalency.

### Numeric functions
<a name="chap-oracle-aurora-mysql.sql.aggregate.mysql.numeric"></a>


| Oracle function and definition | MySQL function and definition | Equivalent | 
| --- | --- | --- | 
|  `ABS` — Absolute value of n: `abs (-11.3) = 11.3`. |  `ABS` — Absolute value of n: `abs (-11.3) = 11.3`. | Yes | 
|  `CEIL` — Returns the smallest integer that is greater than or equal to n: `ceil (-24.9) = -24`. |  `CEIL` — Returns the smallest integer that is greater than or equal to n: `ceil (-24.9) = -24`. | Yes | 
|  `FLOOR` — Returns the largest integer equal to or less than n: `floor (-43.7) = -44`. |  `FLOOR` — Returns the largest integer equal to or less than n: `floor (-43.7) = -44`. | Yes | 
|  `MOD` — Remainder of n2 divided by n1: `mod(10,3) = 1`. |  `MOD` — Remainder of n2 divided by n1: `mod(10,3) = 1`. | Yes | 
|  `ROUND` — Returns n rounded to integer places to the right of the decimal point: `round (3.49, 1) = 3.5`. |  `ROUND` — Returns n rounded to integer places to the right of the decimal point: `round (3.49, 1) = 3.5`. | Yes | 
|  `TRUNC` — Returns n1 truncated to n2 decimal places: `trunc(13.5) = 13`. |  `TRUNCATE` — Returns n1 truncated to n2 decimal places: `trunc(13.5) = 13`. | Yes | 

### Character functions
<a name="chap-oracle-aurora-mysql.sql.aggregate.mysql.character"></a>


| Oracle function and definition | MySQL function and definition | Equivalent | 
| --- | --- | --- | 
|  `CONCAT` — Returns char1 concatenated with char2: `concat('a', 1) → a1`. |  `CONCAT` — Returns char1 concatenated with char2: `concat('a', 1) → a1`. | Yes | 
|  `LOWER` and `UPPER` — Returns char, with all letters lowercase or uppercase: `lower ('MR. Smith') → mr. smith`. |  `LOWER` and `UPPER` — Returns char, with all letters lowercase or uppercase: `lower ('MR. Smith') → mr. smith`. | Yes | 
|  `LPAD` and `RPAD` — Returns `expr1`, left or right padded to length n characters with the sequence of characters in `expr2`: `LPAD('Log-1',10,'-') → -----Log-1`. |  `LPAD` and `RPAD` — Returns `expr1`, left or right padded to length n characters with the sequence of characters in `expr2`: `LPAD('Log-1',10,'-') → -----Log-1`. | Yes | 
|  `REGEXP_REPLACE` — Search a string for a regular expression pattern: `regexp_replace('John', '[hn].', '1') → Jo1`. | You can simulate Oracle `REGEXP_REPLACE` function using MySQL built-in function. | No | 
|  `REGEXP_SUBSTR` — Extends the functionality of the `SUBSTR` function by searching a string for a regular expression pattern:<pre>REGEXP_SUBSTR('http://www.aws.-com/products',<br />'http://([[:alnum:]]+\.?){3,4}/?')</pre><br /> `→ http://www.aws.com/`. | You can simulate Oracle `REGEXP_SUBSTR` function using MySQL built-in function. | No | 
|  `REPLACE` — Returns char with every occurrence of search string replaced with a replacement string: `replace ('abcdef', 'abc', '123') → 123def`. |  `REPLACE` — Returns char with every occurrence of search string replaced with a replacement string: `replace ('abcdef', 'abc', '123') → 123def`. | Yes | 
|  `LTRIM` and `RTRIM` — Removes from the left or right end of char all of the characters that appear in set: `ltrim ('zzzyaws', 'xyz') → aws`. |  `LTRIM` and `RTRIM` — Removes spaces from the left or right end of char: `ltrim(' Amazon') → Amazon`. Combine with the `REPLACE` function to get the results similar to Oracle. | Partly | 
|  `SUBSTR` — Returns a portion of char, beginning at character position, substring length characters long: `substr('John Smith', 6 ,1) → S`. |  `SUBSTR` — Returns a portion of char, beginning at character position, substring length characters long: `substr('John Smith', 6 ,1) → S`. | Yes | 
|  `TRIM` — Trim leading or trailing characters or both from a character string: `trim (both 'x' FROM 'xJohnxx') → John`. |  `TRIM` — Trim leading or trailing characters or both from a character string: `trim (both 'x' FROM 'xJohnxx') → John`. | Yes | 
|  `ASCII` — Returns the decimal representation in the database character set of the first character of char: `ascii('a') → 97`. |  `ASCII` — Returns the decimal representation in the database character set of the first character of char: `ascii('a') → 97`. | Yes | 
|  `INSTR` — Search string for substring. |  `INSTR` — Search string for substring. | Yes | 
|  `LENGTH` — Returns the length of char: `length ('John S.') → 7`. |  `LENGTH` — Returns the length of char: `length ('John S.') → 7`. | Yes | 
|  `REGEXP_COUNT` — Returns the number of times, a pattern occurs in a source string. | You can simulate Oracle `REGEXP_COUNT` function using MySQL built-in function. | No | 
|  `REGEXP_INSTR` — Searches a string position for a regular expression pattern. | You can simulate Oracle `REGEXP_INSTR` function using MySQL built-in function. | No | 

### Date and time functions
<a name="chap-oracle-aurora-mysql.sql.aggregate.mysql.dt"></a>


| Oracle function and definition | MySQL function and definition | Equivalent | 
| --- | --- | --- | 
|  `ADD_MONTHS` — Returns the date plus integer months: `add_months( sysdate,1)`  |  `ADDDATE` — MySQL can implement the same functionality using the `ADDDATE` function. | No | 
|  `CURRENT_DATE` — Returns the current date in the session time zone: `select current_date from dual → 2017-01-01 13:01:01`. |  `CURRENT_DATE` — Returns date without time. Use the `now()` or the `current_timestamp` function to achieve the same results: `select now() → 2017-01-01 13:01:01`. | Partly | 
|  `CURRENT_TIMESTAMP` — Returns the current date and time in the session time zone: `select current timestamp from dual; → 2017-01-01 13:01:01`. |  `CURRENT_TIMESTAMP`— Returns the current date and time in the session time zone: `select current timestamp from dual; → 2017-01-01 13:01:01`. | Yes | 
|  `EXTRACT (date part)` — Returns the value of a specified date time field from a date time or interval expression: `EXTRACT (YEAR FROM DATE '2017-03-07') → 2017`. |  `EXTRACT (date part)` — Returns the value of a specified date time field from a date time or interval expression: `EXTRACT (YEAR FROM DATE '2017-03-07') → 2017`. | Yes | 
|  `LAST_DAY` — Returns the date of the last day of the month that contains date: `LAST_DAY('05-07-2018') → 05-31-2018`. |  `LAST_DAY` — Returns the date of the last day of the month that contains date: `LAST_DAY('05-07-2018') → 05-31-2018`. | Yes | 
|  `BETWEEN` — Returns the number of months between dates date1 and date2: `MONTHS_BETWEEN ( sysdate, sysdate-100) → 3.25`. |  `PERIOD_DIFF` — Returns the number of months between periods P1 and P2. P1 and P2 should be in the format `YYMM` or `YYYYMM`: `SELECT PERIOD_DIFF(201801,201703) → 10`  | Partly | 
|  `SYSDATE` — Returns the current date and time set for the operating system on which the database server resides: `select sysdate from dual → 2017-01-01 13:01:01`. |  `SYSDATE` — Returns the current date and time set for the operating system on which the database server resides: `select sysdate() → 2017-01-01 13:01:01`. | Yes | 
|  `SYSTIMESTAMP` — Returns the system date, including fractional seconds and time zone: `select systimestamp from dual → 2017-01-01 13:01:01.123456 PM+00:00`. |  `CURRENT_TIMESTAMP` — Returns the current date and time in the session time zone: `select current timestamp from dual; → 2017-01-0113:01:01.123456+00`. | Yes | 
|  `LOCALTIMESTAMP` — Returns the current date and time in the session time zone in a value of the `TIMESTAMP` data type: `select localtimestamp from dual → 01-JAN-17 10.01.10.123456 PM`. |  `LOCALTIMESTAMP` — Returns the current date and time in the session time zone in a value of the `TIMESTAMP` data type: `select localtimestamp from dual → 01-JAN-17 10.01.10.123456 PM`. | Yes | 
|  `TO_CHAR(datetime)` — Converts a date time or timestamp to data type to a value of `VARCHAR2` data type in the format specified by the date format: `to_char(sys-date, 'DD-MON-YYYY HH24:MI:SS') → 01-JAN-2017 01:01:01`. |  `DATE_FORMAT` — Changes the format of the date and time: `DATE_FORMAT (SYSDATE(), '%Y-%m-%d %H:%i:%s')`  | Yes | 
|  `TRUNC (date)` — Returns a date with the time portion of the day truncated to the unit specified by the format model: `trunc(systimestamp) → 2017-01-01 00:00:00`. | You can simulate Oracle `TRUNC` function using MySQL built-in function. | No | 

### Encoding and decoding functions
<a name="chap-oracle-aurora-mysql.sql.aggregate.mysql.encoding"></a>


| Oracle function and definition | MySQL function and definition | Equivalent | 
| --- | --- | --- | 
|  `DECODE` — Compares an expression to each search value one by one using the functionality of an `IF-THEN-ELSE` statement. |  `CASE` — Compares an expression to each search value one by one. | No | 
|  `DUMP` — Returns a `VARCHAR2` value containing the data type code, length in bytes, and internal representation of expression. | N/A | No | 
|  `ORA_HASH` — Computes a hash value for a given expression. |  `SHA` — Calculates an SHA-1 160-bit checksum for the string. | No | 

### Null functions
<a name="chap-oracle-aurora-mysql.sql.aggregate.mysql.null"></a>


| Oracle function and definition | MySQL function and definition | Equivalent | 
| --- | --- | --- | 
|  `CASE` — Chooses from a sequence of conditions and runs a corresponding statement: `CASE WHEN condition THEN result [WHEN …​] [ELSE result] END`. |  `CASE` — Chooses from a sequence of conditions and runs a corresponding statement: `CASE WHEN condition THEN result [WHEN …​] [ELSE result] END`. | Yes | 
|  `COALESCE` — Returns the first non-null expr in the expression list: `coalesce (null, 'a', 'b') → a`. |  `COALESCE` — Returns the first of its arguments that isn’t null: `coalesce (null, 'a', 'b') → a`. | Yes | 
|  `NULLIF` — Compares `expr1` and `expr2`. If they are equal, the function returns null. If they aren’t equal, the function returns `expr1`: `NULLIF('a', 'b') → a`. |  `NULLIF` — Compares `expr1` and `expr2`. If they are equal, the function returns null. If they aren’t equal, the function returns `expr1`: `NULLIF('a', 'b') → a`. | Yes | 
|  `NVL` — Replaces null (returned as a blank) with a string in the results of a query: `NVL (null, 'a') → a`. |  `IFNULL` — Replaces null (returned as a blank) with a string in the results of a query: `IFNULL (null, 'a') → a`. | No | 
|  `NVL2` — Determines the value returned by a query based on whether a specified expression is null or not null. |  `CASE` — Chooses from a sequence of conditions and runs a corresponding statement: `CASE WHEN condition THEN result [WHEN …​] [ELSE result] END`. | No | 

### Environment and identifier functions
<a name="chap-oracle-aurora-mysql.sql.aggregate.mysql.environment"></a>


| Oracle function and definition | MySQL function and definition | Equivalent | 
| --- | --- | --- | 
|  `SYS_GUID` — Generates and returns a globally unique identifier (RAW value) made up of 16 bytes: `select sys_guid() from dual → 5A280ABA8C76201EE0530-100007FF691`. |  `UUID` and `REPLACE` — `REPLACE(UUID(), '-', '')`. | No | 
|  `UID` — Returns an integer that uniquely identifies the session user (the user who logged on): `select uid from dual → 84`. | N/A | No | 
|  `USER` — Returns the name of the session user: `select user from dual`. |  `USER` — Returns the name of the session user and source machine: `select USER()`. | No | 
|  `USERENV` — Returns information about the current session using parameters: `SELECT USERENV ('LANGUAGE') "Language" FROM DUAL`. |  `SHOW SESSION VARIABLES` — Displays the system variable values that are in effect for the current connection: `myshow SESSION VARIABLES LIKE 'collation_connection';`. | No | 

### Oracle conversion functions
<a name="chap-oracle-aurora-mysql.sql.aggregate.mysql.conversion"></a>


| Oracle function and definition | MySQL function and definition | Equivalent | 
| --- | --- | --- | 
|  `CAST` — Converts one built-in data type or collection-typed value into another built-in data type or collection-typed value: `cast ('10' as int) + 1 → 11`. |  `CAST` — Converts one built-in data type or collection-typed value into another built-in data type or collection-typed value: `cast ('10' as UNSIGNED) + 1`. | Yes | 
|  `CONVERT` — Converts a character string from a one-character set to another: `select convert ('Ä Ê Í Õ Ø A B C D E ', 'US7ASCII', 'WE8ISO8859P1') from dual`. |  `CONVERT` — Converts a character string from a one-character set to another: `select convert ('Ä Ê Í Õ Ø A B C D E ' USING utf8)`. | Yes | 
|  `TO_CHAR (string / numeric)` — Converts `NCHAR`, `NVARCHAR2`, `CLOB`, or `NCLOB` data to the database character set: `select to_char ('01234') from dual → 01234`. |  `FORMAT` — Converts string data to the database character set: `FORMAT('01234', 0) -→ 01234`. | No | 
|  `TO_DATE` — Converts char of `CHAR`, `VARCHAR2`, `NCHAR`, or `NVARCHAR2` data type to a value of `DATE` data type: `to_date('01Jan2017','DDMonYYYY') → 01-JAN-17`. |  `STR_TO_DATE` — Convert string data type to a value of `DATE` data type: `SELECT STR_TO_DATE('01Jan2017','%d%M%Y')`. | No | 
|  `TO_NUMBER` — Converts an expression to a value of `NUMBER` data type: `to_number('01234') → 1234 or to_number('01234', '99999') → 1234`. | N/A | No | 

### Aggregate functions
<a name="chap-oracle-aurora-mysql.sql.aggregate.mysql.aggregate"></a>


| Oracle function and definition | MySQL function and definition | Equivalent | 
| --- | --- | --- | 
|  `AVG` — Returns an average value of an expression: `select avg(salary) from employees`. |  `AVG` — Returns an average value of an expression: `select avg(salary) from employees`. | Yes | 
|  `COUNT` — Returns the number of rows returned by the query: `select count(*) from employees`. |  `COUNT` — Returns the number of rows returned by the query: `select count(*) from employees`. | Yes | 
|  `LISTAGG` — Orders data within each group specified in the `ORDER BY` clause and then concatenates the values of the measure column: `select listagg(firstname,' ,') within group (order by customerid) from customer`. |  `GROUP_CONCAT` — Orders data within each group specified in the `ORDER BY` clause and then concatenates the values of the measure column: `select GROUP_CONCAT(firstname order by customerid) from customer`. | No | 
|  `MAX` — Returns the maximum value of an expression: `select max(salary) from employees`. |  `MAX` — Returns the maximum value of an expression: `select max(salary) from employees`. | Yes | 
|  `MIN` — Returns the minimum value of an expression: `select min(salary) from employees`. |  `MIN` — Returns the minimum value of an expression: `select min(salary) from employees`. | Yes | 
|  `SUM` — Returns the sum of values of an expression: `select sum(salary) from employees`. |  `SUM` — Returns the sum of values of an expression: `select sum(salary) from employees`. | Yes | 

### Top-N Query Oracle 12c
<a name="chap-oracle-aurora-mysql.sql.aggregate.mysql.topn"></a>


| Oracle function and definition | MySQL function and definition | Equivalent | 
| --- | --- | --- | 
|  `FETCH` — Retrieves rows of data from the result set of a multi-row query: `select * from customer fetch first 10 rows only`. |  `LIMIT` — Retrieves just a portion of the rows that are generated by the rest of the query: `select * from customer LIMIT 10`. | Yes | 

For more information, see [String Functions and Operators](https://dev.mysql.com/doc/refman/5.7/en/string-functions.html) and [Numeric Functions and Operators](https://dev.mysql.com/doc/refman/5.7/en/numeric-functions.html) in the *MySQL documentation*.