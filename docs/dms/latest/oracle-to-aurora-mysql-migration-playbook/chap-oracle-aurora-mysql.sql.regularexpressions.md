

# Oracle and MySQL regular expressions
<a name="chap-oracle-aurora-mysql.sql.regularexpressions"></a>

 *Regular expressions* help you locate and manipulate specific patterns within text data. You can leverage regular expressions for tasks such as data cleansing, validation, or transformation. The following sections provide details on constructing and utilizing regular expressions in Oracle and MySQL with AWS DMS.


| Feature compatibility |  AWS SCT / AWS DMS automation level |  AWS SCT action code index | Key differences | 
| --- | --- | --- | --- | 
|  ![Three star feature compatibility](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-compatibility-3.png)  |  ![Three star automation level](http://docs.aws.amazon.com/dms/latest/oracle-to-aurora-mysql-migration-playbook/images/pb-automation-3.png)  | N/A | Syntax and option differences. | 

## Oracle usage
<a name="chap-oracle-aurora-mysql.sql.regularexpressions.oracle"></a>

A regular expression is a set of characters that define a search pattern. The most basic example is `*`, which matches any character. Most Relational Database Management Systems use the same characters for regular expressions, but some use characters differently and provide additional expressions.

Oracle SQL implementation is based on the following standards:
+ IEEE Portable Operating System Interface (POSIX) standard draft 1003.2/D11.2.
+ Unicode Regular Expression Guidelines of the Unicode Consortium.

Oracle SQL extends the standards as follows:
+ Provides matching capabilities for multilingual data.
+ Supports some commonly used PERL regular expression operators not included in the POSIX standard (for example, character class shortcuts and the non-greedy modifier `[?]`).

Summary of Oracle SQL pattern matching:
+  `REGEXP_LIKE` — Can be used in `WHERE` clauses to find rows matching a certain pattern.
+  `REGEXP_COUNT` — Returns the number of occurrences of a pattern in a given string.
+  `REGEXP_INSTR` — Returns the position of a pattern within a string.
+  `REGEXP_REPLACE` — Replaces a pattern within a string and returns the new string.
+  `REGEXP_SUBSTR` — Similar to `REGEXP_INSTR`, but returns the matching substring itself instead of its position.

Summary of Oracle SQL pattern matching options:
+  **i** — Case-insensitive matching.
+  **c** — Case-sensitive matching.
+  **n** — Allows the dot operator `.` to act like a newline character.
+  **m** — Allows the string to contain multiple lines.
+  **x** — Ignores white-space characters in the search pattern.

### Examples
<a name="chap-oracle-aurora-mysql.sql.regularexpressions.oracle.examples"></a>

Find employees with a first name of Steven or Stephen.

```
SELECT * FROM EMPLOYEES
WHERE REGEXP_LIKE((first_name, '^Ste(v|ph)en$')
```

Find employees with a first name that includes g but not G twice starting at character position 3.

```
SELECT * FROM EMPLOYEES where
REGEXP_COUNT('George Washington', 'g', 3, 'c') = 2;
```

Find employees with a valid email address.

```
SELECT * FROM EMPLOYEES where
REGEXP_INSTR(email, '\w+@\w+(\.\w+)+') >0;
```

Get the country with a space after each character for each employee.

```
SELECT REGEXP_REPLACE(country_name, '(.)', '\1 ') FROM EMPLOYEES;
```

For more information, see [Oracle Regular Expression Support](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Oracle-Regular-Expression-Support.html#GUID-969230D6-FC1A-4C75-BF2A-6B1BE909DED6) in the *Oracle documentation*.

## MySQL usage
<a name="chap-oracle-aurora-mysql.sql.regularexpressions.mysql"></a>

Like Oracle, Aurora MySQL Regular Expressions to make complex searches easier.

MySQL and Oracle use Henry Spencer’s implementation of regular expressions, which implements the POSIX 1003.2 standard. MySQL uses the extended version to support regular expression pattern matching operations in SQL statements.

**Note**  
 Amazon Relational Database Service (Amazon RDS) for MySQL version 8.0, support for Regular Expressions will be more like Oracle. For more information, see [Regular Expressions](https://dev.mysql.com/doc/refman/5.7/en/regexp.html#function_regexp-replace) in the *MySQL documentation*.

### Regular expression operators
<a name="chap-oracle-aurora-mysql.sql.regularexpressions.mysql.operators"></a>
+  `NOT REGEXP` or `NOT RLIKE` — Returns 1 if the string expr does not match the regular expression specified by the pattern pat. Otherwise, it returns 0. If either expr or pat is NULL, the return value is NULL.
+  `REGEXP` or `RLIKE`: Returns 1 if the string expr matches the regular expression specified by the pattern pat. Otherwise, it returns 0. If either expr or pat is NULL, the return value is NULL.

 `RLIKE` is a synonym for `REGEXP`. For compatibility with Oracle, this section refers only to `REGEXP`.

MySQL uses the C escape syntax in strings. You must double any `\` used in your `REGEXP` arguments.

### Examples
<a name="chap-oracle-aurora-mysql.sql.regularexpressions.mysql.examples"></a>

Find employees with a first name of Steven or Stephen.

```
SELECT * FROM EMPLOYEES WHERE first_name REGEXP ('^Ste(v|ph)en$');
```

Find employees with a valid email address.

```
SELECT * FROM EMPLOYEES where
email NOT REGEXP '^[A-Z0-9._%-]+@[A-Z0-9.-]+\\.[A-Z]{2,4}$';
```

## Summary
<a name="chap-oracle-aurora-mysql.sql.regularexpressions.summary"></a>


| Search or usage | Oracle | MySQL | 
| --- | --- | --- | 
| Find employees with the first name of Steven or Stephen |  <pre>SELECT * FROM EMPLOYEES<br />WHERE REGEXP_LIKE((first_name,<br />  '^Ste(v|ph)en$')</pre>  |  <pre>SELECT * FROM EMPLOYEES<br />WHERE first_name REGEXP ('^Ste(v|ph)en$');</pre>  | 
| Find employees with the first name that includes g but not G twice , starting at character position 3 |  <pre>SELECT * FROM EMPLOYEES<br />WHERE<br />REGEXP_COUNT('George Washington',<br />'g', 3, 'c') = 2;</pre>  |  <pre>select * FROM EMPS WHERE<br />LENGTH(SUBSTRING(FULL_NAME,3)) -<br />LENGTH(REPLACE<br />(SUBSTRING(FULL_NAME,3), 'g', '')) = 2;</pre>  | 
| Find employees with a valid email address |  <pre>SELECT * FROM EMPLOYEES<br />where<br />REGEXP_INSTR(email, '\w+@\w+ (\.\w+)+') >0;</pre>  |  <pre>SELECT * FROM EMPLOYEES where<br />email NOT REGEXP '^[A-Z0-9._%-]+@[A-Z0-9.-]+\\.[A-Z]{2,4}$';</pre>  | 
| Get each employee’s country with space after each character |  <pre>SELECT REGEXP_REPLACE<br />(country_name, '(.)', '\1 ')<br />FROM EMPLOYEES;</pre>  | Make sure that you use a user-defined function | 

For more information, see [Regular Expressions](https://dev.mysql.com/doc/refman/5.7/en/regexp.html) and [Pattern Matching](https://dev.mysql.com/doc/refman/5.7/en/pattern-matching.html) in the *MySQL documentation*.