# Oracle and MySQL regular expressions

_Regular expressions_ help you locate and manipulate specific patterns within text data. You can leverage regular expressions for tasks such as data cleansing, validation, or transformation. The following sections provide details on constructing and utilizing regular expressions in Oracle and MySQL with AWS DMS.

| Feature compatibility            | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                |
| -------------------------------- | ---------------------------------- | ------------------------- | ------------------------------ |
| Three star feature compatibility | Three star automation level        | N/A                       | Syntax and option differences. |

## Oracle usage

A regular expression is a set of characters that define a search pattern. The most basic example is `*`, which matches any character. Most Relational Database Management Systems use the same characters for regular expressions, but some use characters differently and provide additional expressions.

Oracle SQL implementation is based on the following standards:

- IEEE Portable Operating System Interface (POSIX) standard draft 1003.2/D11.2.
- Unicode Regular Expression Guidelines of the Unicode Consortium.

Oracle SQL extends the standards as follows:

- Provides matching capabilities for multilingual data.
- Supports some commonly used PERL regular expression operators not included in the POSIX standard (for example, character class shortcuts and the non-greedy modifier `[?]`).

Summary of Oracle SQL pattern matching:

- `REGEXP_LIKE` — Can be used in `WHERE` clauses to find rows matching a certain pattern.
- `REGEXP_COUNT` — Returns the number of occurrences of a pattern in a given string.
- `REGEXP_INSTR` — Returns the position of a pattern within a string.
- `REGEXP_REPLACE` — Replaces a pattern within a string and returns the new string.
- `REGEXP_SUBSTR` — Similar to `REGEXP_INSTR`, but returns the matching substring itself instead of its position.

Summary of Oracle SQL pattern matching options:

- **i** — Case-insensitive matching.
- **c** — Case-sensitive matching.
- **n** — Allows the dot operator `.` to act like a newline character.
- **m** — Allows the string to contain multiple lines.
- **x** — Ignores white-space characters in the search pattern.

### Examples

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

For more information, see [Oracle Regular Expression Support](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Oracle-Regular-Expression-Support.html#GUID-969230D6-FC1A-4C75-BF2A-6B1BE909DED6 "https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/Oracle-Regular-Expression-Support.html#GUID-969230D6-FC1A-4C75-BF2A-6B1BE909DED6") in the _Oracle documentation_.

## MySQL usage

Like Oracle, Aurora MySQL Regular Expressions to make complex searches easier.

MySQL and Oracle use Henry Spencer’s implementation of regular expressions, which implements the POSIX 1003.2 standard. MySQL uses the extended version to support regular expression pattern matching operations in SQL statements.

###### Note

Amazon Relational Database Service (Amazon RDS) for MySQL version 8.0, support for Regular Expressions will be more like Oracle. For more information, see [Regular Expressions](https://dev.mysql.com/doc/refman/5.7/en/regexp.html#function_regexp-replace "https://dev.mysql.com/doc/refman/5.7/en/regexp.html#function_regexp-replace") in the _MySQL documentation_.

### Regular expression operators

- `NOT REGEXP` or `NOT RLIKE` — Returns 1 if the string expr does not match the regular expression specified by the pattern pat. Otherwise, it returns 0. If either expr or pat is NULL, the return value is NULL.
- `REGEXP` or `RLIKE`: Returns 1 if the string expr matches the regular expression specified by the pattern pat. Otherwise, it returns 0. If either expr or pat is NULL, the return value is NULL.

`RLIKE` is a synonym for `REGEXP`. For compatibility with Oracle, this section refers only to `REGEXP`.

MySQL uses the C escape syntax in strings. You must double any `\` used in your `REGEXP` arguments.

### Examples

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

| Search or usage                                                                                       | Oracle                                                                                                  | MySQL                                                                                                                                  |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Find employees with the first name of Steven or Stephen                                               | ```<br>SELECT<br>• FROM EMPLOYEES<br>WHERE REGEXP_LIKE((first_name,<br>'^Ste(v                          | ph)en$')<br>```                                                                                                                        | ```<br>SELECT<br>• FROM EMPLOYEES<br>WHERE first_name REGEXP ('^Ste(v | ph)en$');<br>``` |
| Find employees with the first name that includes g but not G twice , starting at character position 3 | `<br>SELECT<br>• FROM EMPLOYEES<br>WHERE<br>REGEXP_COUNT('George Washington',<br>'g', 3, 'c') = 2;<br>` | `<br>select<br>• FROM EMPS WHERE<br>LENGTH(SUBSTRING(FULL_NAME,3)) -<br>LENGTH(REPLACE<br>(SUBSTRING(FULL_NAME,3), 'g', '')) = 2;<br>` |
| Find employees with a valid email address                                                             | `<br>SELECT<br>• FROM EMPLOYEES<br>where<br>REGEXP_INSTR(email, '\w+@\w+ (\.\w+)+') >0;<br>`            | `<br>SELECT<br>• FROM EMPLOYEES where<br>email NOT REGEXP '^[A-Z0-9._%-]+@[A-Z0-9.-]+\\.[A-Z]{2,4}$';<br>`                             |
| Get each employee’s country with space after each character                                           | `<br>SELECT REGEXP_REPLACE<br>(country_name, '(.)', '\1 ')<br>FROM EMPLOYEES;<br>`                      | Make sure that you use a user-defined function                                                                                         |

For more information, see [Regular Expressions](https://dev.mysql.com/doc/refman/5.7/en/regexp.html "https://dev.mysql.com/doc/refman/5.7/en/regexp.html") and [Pattern Matching](https://dev.mysql.com/doc/refman/5.7/en/pattern-matching.html "https://dev.mysql.com/doc/refman/5.7/en/pattern-matching.html") in the _MySQL documentation_.
