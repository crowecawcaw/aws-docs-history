# String functions

String functions are built-in tools used to manipulate and process text data. They
enable tasks like concatenation, extraction, formatting, and searching within strings.
These functions are essential for cleaning, transforming, and analyzing text-based data
within a database.

| String functions | **Function**                                                                              | **Signature**                                                                                                                                                                                                                                                                                                | **Description** |
| ---------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| `LENGTH`         | LENGTH (string)                                                                           | Returns the length of the string.                                                                                                                                                                                                                                                                            |
| `CONCAT`         | CONCAT (string, string)                                                                   | Concatenates arguments in a string.                                                                                                                                                                                                                                                                          |
| `SUBSTR`         | • SUBSTR (string, start)<br>• SUBSTR (string, start, length)<br>• SUBSTR (string, regexp) | Returns one of the following:<br>• Returns the substring of the input string starting the specified<br>location and optionally having the specified length.<br>• Returns the first substring of the input string matching the specified<br>regular expression.<br>Uses 1-based indexing for start parameter. |
| `UPPER`          | UPPER (string)                                                                            | Converts the characters in the input string to uppercase.                                                                                                                                                                                                                                                    |
| `LOWER`          | LOWER (string)                                                                            | Converts the characters in the input string to lowercase.                                                                                                                                                                                                                                                    |
| `TRIM`           | TRIM (string)                                                                             | Removes any space characters from the beginning, end, or both sides of<br>string.                                                                                                                                                                                                                            |
| `LTRIM`          | LTRIM (string)                                                                            | Removes any space characters from the beginning of string.                                                                                                                                                                                                                                                   |
| `RTRIM`          | RTRIM (string)                                                                            | Removes any space characters from the end of string.                                                                                                                                                                                                                                                         |
| `STR_REPLACE`    | STR_REPLACE (string, from, to)                                                            | Replaces all occurrences of the specified substring with another specified<br>substring.                                                                                                                                                                                                                     |

Examples of all the functions:

| **Function** | **Example**                                                                                                                                                                                                                                  |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LENGTH       | `SELECT LENGTH(a.asset_id) AS asset_id_length FROM asset AS<br>a`                                                                                                                                                                            |
| CONCAT       | `SELECT CONCAT(p.property_id, p.property_name) FROM asset_property AS p`                                                                                                                                                                     |
| SUBSTR       | • `SELECT SUBSTR(a.asset_name, 1, 3) AS substr-val FROM asset AS a`<br>• `SELECT SUBSTR(p.property_name, 3) AS substr_val1 FROM asset_property AS p`<br>• `SELECT SUBSTR(p.property_name, '@[^.]*') AS substr_val2 FROM asset_property AS p` |
| UPPER        | `SELECT UPPER(d.string_value) AS up_string FROM raw_time_series AS<br>d`                                                                                                                                                                     |
| LOWER        | `SELECT LOWER(d.string_value) AS low_string FROM raw_time_series AS<br>d`                                                                                                                                                                    |
| TRIM         | `SELECT TRIM(d.string_value) AS tm_string FROM raw_time_series AS<br>d`                                                                                                                                                                      |
| LTRIM        | `SELECT LTRIM(d.string_value) AS ltrim_string FROM raw_time_series AS<br>d`                                                                                                                                                                  |
| RTRIM        | `SELECT RTRIM(d.string_value) AS rtrim_string FROM raw_time_series AS<br>d`                                                                                                                                                                  |
| STR_REPLACE  | `SELECT STR_REPLACE(d.string_value, 'abc', 'def') AS replaced_string FROM<br>raw_time_series AS d`                                                                                                                                           |

## Concatenation operator

The concatenation operator `||`, or pipe operator, joins two strings together. It
provides an alternative to the `CONCAT` function, and is more readable when combining
multiple strings.

###### Example of the concatenation operator

```
SELECT a.asset_name || ' - ' || p.property_name
  AS full_name
  FROM asset a, asset_property p
```
