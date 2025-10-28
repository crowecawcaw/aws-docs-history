# Concatenate strings and arrays

Concatenating strings and concatenating arrays use similar techniques.

## Concatenate strings

To concatenate two strings, you can use the double pipe `||` operator, as
in the following example.

```
SELECT 'This' || ' is' || ' a' || ' test.' AS Concatenated_String
```

This query returns:

| #   | Concatenated_String                       |
| --- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --- | ---------------------------------- | --- | --------------------------------------------------------------------- |
| `1` | `This is a test.`                         | You can use the `concat()` function to achieve the same result. `SELECT concat('This', ' is', ' a', ' test.') AS Concatenated_String` This query returns:                                                                                                                                                          |
| #   | Concatenated_String                       |
| --- | ---                                       |
| `1` | `This is a test.`                         | You can use the `concat_ws()` function to concatenate strings with the separator specified in the first argument. `SELECT concat_ws(' ', 'This', 'is', 'a', 'test.') as Concatenated_String` This query returns:                                                                                                   |
| #   | Concatenated_String                       |
| --- | ---                                       |
| `1` | `This is a test.`                         | To concatenate two columns of the string data type using a dot, reference the two columns using double quotes, and enclose the dot in single quotes as a hard-coded string. If a column is not of the string data type, you can use `CAST("`column_name`" as VARCHAR)` to cast the column first. ``` SELECT "col1" |     | '.'                                |     | "col2" as Concatenated_String FROM `my_table` ``` This query returns: |
| #   | Concatenated_String                       |
| --- | ---                                       |
| `1` | ``col1_string_value`.`col2_string_value`` | ## Concatenate arrays You can use the same techniques to concatenate arrays. To concatenate multiple arrays, use the double pipe `                                                                                                                                                                                 |     | ` operator. ``` SELECT ARRAY [4,5] |     | ARRAY[ ARRAY[1,2], ARRAY[3,4] ] AS items ``` This query returns:      |
| #   | items                                     |
| --- | ---                                       |
| `1` | `[[4, 5], [1, 2], [3, 4]]`                | To combine multiple arrays into a single array, use the double pipe operator or the `concat()` function. `WITH dataset AS ( SELECT ARRAY ['Hello', 'Amazon', 'Athena'] AS words, ARRAY ['Hi', 'Alexa'] AS alexa ) SELECT concat(words, alexa) AS welcome_msg FROM dataset` This query returns:                     |
| #   | welcome_msg                               |
| --- | ---                                       |
| `1` | `[Hello, Amazon, Athena, Hi, Alexa]`      | For more information about `concat()` other string functions, see [String functions and operators](https://trino.io/docs/current/functions/string.html "https://trino.io/docs/current/functions/string.html") in the Trino documentation.                                                                          |
