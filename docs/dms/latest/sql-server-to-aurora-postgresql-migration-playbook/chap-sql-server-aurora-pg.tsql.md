# String functions for T-SQL

Compare string function compatibility between Microsoft SQL Server 2019 and Amazon Aurora PostgreSQL. Gain insights into how various string functions in SQL Server map to their PostgreSQL equivalents, which is crucial for database migration projects. The information highlights supported functions, unsupported ones, and alternative approaches in PostgreSQL.

| Feature compatibility           | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                |
| ------------------------------- | ---------------------------------- | ------------------------- | ------------------------------ |
| Four star feature compatibility | Four star automation level         | N/A                       | Syntax and option differences. |

## SQL Server Usage

String functions are typically scalar functions that perform an operation on string input and return a string or a numeric value.

### Syntax and Examples

The following table includes the most commonly used string functions.

| Function                         | Purpose                                                                                                                     | Example                                                                                   | Result      | Comments                                   |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ----------- | ------------------------------------------ |
| `ASCII` and `UNICODE`            | Convert an ASCII or UNICODE character to its ASCII or UNICODE code.                                                         | `SELECT ASCII ('A')`                                                                      | 65          | Returns a numeric integer value.           |
| `CHAR` and `NCHAR`               | Convert between ASCII or UNICODE code to a string character.                                                                | `SELECT CHAR(65)`                                                                         | 'A'         | Numeric integer value as input.            |
| `CHARINDEX` and `PATINDEX`       | Find the starting position of one string expression or string pattern within another string expression.                     | `SELECT CHARINDEX('ab','xabcdy')`                                                         | 2           | Returns a numeric integer value.           |
| `CONCAT` and `CONCAT_WS`         | Combine multiple string input expressions into a single string with, or without, a separator character (WS).                | `SELECT CONCAT ('a','b'), CONCAT_WS(',','a','b')`                                         | 'ab', 'a,b' |                                            |
| `LEFT`, `RIGHT`, and `SUBSTRING` | Return a partial string from another string expression based on position and length.                                        | `SELECT LEFT ('abs',2),SUBSTRING ('abcd',2,2)`                                            | 'ab', 'bc'  |                                            |
| `LOWER` and `UPPER`              | Return a string with all characters in lower or upper case. Use for presentation or to handle case insensitive expressions. | `SELECT LOWER('ABcd')`                                                                    | 'abcd'      |                                            |
| `LTRIM`, `RTRIM`, and `TRIM`     | Remove leading and trailing spaces.                                                                                         | `SELECT LTRIM ('abc d ')`                                                                 | 'abc d '    |                                            |
| `STR`                            | Convert a numeric value to a string.                                                                                        | `SELECT STR(3.1415927,5,3)`                                                               | 3.142       | Numeric expressions as input.              |
| `REVERSE`                        | Return a string in reverse order.                                                                                           | `SELECT REVERSE('abcd')`                                                                  | 'dcba'      |                                            |
| `REPLICATE`                      | Return a string that consists of zero or more concatenated copies of another string expression.                             | `SELECT REPLICATE ('abc', 3)`                                                             | 'abcabcabc' |                                            |
| `REPLACE`                        | Replace all occurrences of a string expression with another.                                                                | `SELECT REPLACE('abcd', 'bc', 'xy')`                                                      | 'axyd'      |                                            |
| `STRING_SPLIT`                   | Parse a list of values with a separator and return a set of all individual elements.                                        | `SELECT<br>• FROM STRING_SPLIT('1,2',',') AS X©`                                          | 12          | `STRING_SPLIT` is a table-valued function. |
| `STRING_AGG`                     | Return a string that consists of concatenated string values in row groups.                                                  | `SELECT STRING_AGG(C, ',') FROM VALUES(1, 'a'), (1, 'b'), (2,'c') AS X (ID,C) GROUP BY I` | 1 'ab'      | 2 'c'                                      |

For more information, see [String Functions (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/functions/string-functions-transact-sql?view=sql-server-ver15 "https://docs.microsoft.com/en-us/sql/t-sql/functions/string-functions-transact-sql?view=sql-server-ver15") in the _SQL Server documentation_.

## PostgreSQL Usage

Most of SQL Server string functions are supported in PostgreSQL, there are few which aren’t:

- `UNICODE` returns the integer value of the first character as defined by the Unicode standard. If you will use UTF8 input, ASCII can be used to get the same results.
- `PATINDEX` returns the starting position of the first occurrence of a pattern in a specified expression, or zeros if the pattern isn’t found, there is no equivalent function for that but you can create the same function with the same name so it will be fully compatible.

Some of the functions aren’t supported but they have an equivalent function in PostgreSQL that you can use to get the same functionality.

Some of the functions such as regular expressions don’t exist in SQL Server and may be useful for your application.

### Syntax and Examples

The following table includes the most commonly used string functions.

| PostgreSQL function             | Function definition                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- | ------------------------ | --- | --- | --- | ----------- |
| `CONCAT`                        | Concatenate the text representations of all the arguments: `concat('a', 1)` → a1. Also, can use the (                                                                                                                                                                                                                                                                                                     |     | ) operators: `select 'a' |     | ' ' |     | 'b'` → a b. |
| `LOWER` or `UPPER`              | Returns char, with all letters lowercase or uppercase: `lower ('MR. Smith')` → mr. smith.                                                                                                                                                                                                                                                                                                                 |
| `LPAD` or `RPAD`                | Returns `expr1`, left or right padded to length n characters with the sequence of characters in `expr2`: `LPAD('Log-1',10,'@')` → @@@@@Log-1.                                                                                                                                                                                                                                                             |
| `REGEXP_REPLACE`                | Replace substrings matching a POSIX regular expression: `regexp_replace('John', '[hn].', '1')` → Jo1.                                                                                                                                                                                                                                                                                                     |
| `REGEXP_MATCHES` or `SUBSTRING` | Return all captured substrings resulting from matching a POSIX regular expression against the string:<br>`<br>REGEXP_MATCHES ('http://www.aws.com/products', '(http://[[: alnum:]]+.*/)')<br>`<br>The result is `{http://www.aws.com/}`.<br>You can use the following example<br>`<br>SUBSTRING ('http://www.aws.com/products', '(http://[[: alnum:]]+.*/)')<br>`<br>The result is `http://www.aws.com/`. |
| `REPLACE`                       | Returns char with every occurrence of search string replaced with a replacement string: `replace ('abcdef', 'abc', '123')` → 123def.                                                                                                                                                                                                                                                                      |
| `LTRIM` or `RTRIM`              | Remove the longest string containing only characters from characters (a space by default) from the start of string: `ltrim('zzzyaws', 'xyz')` → aws.                                                                                                                                                                                                                                                      |
| `SUBSTRING`                     | Extract substring: `substring ( 'John Smith', 6 ,1)` → S.                                                                                                                                                                                                                                                                                                                                                 |
| `TRIM`                          | Remove the longest string containing only characters from characters (a space by default) from the start, end, or both ends: `trim (both from 'yxJohnxx', 'xyz')` → John.                                                                                                                                                                                                                                 |
| `ASCII`                         | Returns the decimal representation in the database character set of the first character of char: `ascii('a')` → 97.                                                                                                                                                                                                                                                                                       |
| `LENGTH`                        | Return the length of char: `length ('John S.')` → 7.                                                                                                                                                                                                                                                                                                                                                      |

To create the `PATINDEX` function, use the following code snippet. Note the 0 means that the expression doesn’t exist so the first position will be 1.

```
CREATE OR REPLACE FUNCTION "patindex"( "pattern" VARCHAR, "expression" VARCHAR )
RETURNS INT AS $BODY$
SELECT COALESCE(STRPOS($2,(
  SELECT(REGEXP_MATCHES($2,'(' ||
  REPLACE( REPLACE(TRIM( $1, '%' ), '%', '.*?' ), '_', '.' )
    || ')','i') )[ 1 ] LIMIT 1)),0);
$BODY$ LANGUAGE 'sql' IMMUTABLE;

SELECT patindex( 'Lo%', 'Long String' );

patindex
1

SELECT patindex( '%rin%', 'Long String' );
patindex
8

SELECT patindex( '%g_S%', 'Long String' );
patindex
4
```

## Summary

| SQL Server function              | Aurora PostgreSQL function                         |
| -------------------------------- | -------------------------------------------------- |
| `ASCII`                          | `ASCII`                                            |
| `UNICODE`                        | For UTF8 inputs, you can use only `ASCII`.         |
| `CHAR` and `NCHAR`               | `CHR`                                              |
| `CHARINDEX`                      | `POSITION`                                         |
| `PATINDEX`                       | See examples                                       |
| `CONCAT` and `CONCAT_WS`         | `CONCAT` and `CONCAT_WS`                           |
| `LEFT`, `RIGHT`, and `SUBSTRING` | `LEFT`, `RIGHT`, and `SUBSTRING`                   |
| `LOWER` and `UPPER`              | `LOWER` and `UPPER`                                |
| `LTRIM`, `RTRIM` and `TRIM`      | `LTRIM`, `RTRIM` and `TRIM`                        |
| `STR`                            | `TO_CHAR`                                          |
| `REVERSE`                        | `REVERSE`                                          |
| `REPLICATE`                      | `LPAD`                                             |
| `REPLACE`                        | `REPLACE`                                          |
| `STRING_SPLIT`                   | `regexp_split_to_array` or `regexp_split_to_table` |
| `STRING_AGG`                     | `STRING_AGG`                                       |

For more information, see [String Functions and Operators](https://www.postgresql.org/docs/13/functions-string.html "https://www.postgresql.org/docs/13/functions-string.html") in the _PostgreSQL documentation_.
