For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# String functions

###### Note

The input data type of these functions is assumed to be varchar unless otherwise
specified.

| Function                            | Output data type | Description                                                                                                                                                                                    |
| ----------------------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| chr(n)                              | varchar          | Returns the Unicode code point n as a varchar.                                                                                                                                                 |
| codepoint(x)                        | integer          | Returns the Unicode code point of the only character of str.                                                                                                                                   |
| concat(x1, ..., xN)                 | varchar          | Returns the concatenation of x1, x2, ..., xN.                                                                                                                                                  |
| hamming_distance(x1,x2)             | bigint           | Returns the Hamming distance of x1 and x2, i.e. the number of positions at<br>which the corresponding characters are different. Note that the two varchar<br>inputs must have the same length. |
| length(x)                           | bigint           | Returns the length of x in characters.                                                                                                                                                         |
| levenshtein_distance(x1, x2)        | bigint           | Returns the Levenshtein edit distance of x1 and x2, i.e. the minimum number<br>of single-character edits (insertions, deletions or substitutions) needed to<br>change x1 into x2.              |
| lower(x)                            | varchar          | Converts x to lowercase.                                                                                                                                                                       |
| lpad(x1, bigint size, x2)           | varchar          | Left pads x1 to size characters with x2. If size is less than the length of<br>x1, the result is truncated to size characters. size must not be negative and<br>x2 must be non-empty.          |
| ltrim(x)                            | varchar          | Removes leading whitespace from x.                                                                                                                                                             |
| replace(x1, x2)                     | varchar          | Removes all instances of x2 from x1.                                                                                                                                                           |
| replace(x1, x2, x3)                 | varchar          | Replaces all instances of x2 with x3 in x1.                                                                                                                                                    |
| Reverse(x)                          | varchar          | Returns x with the characters in reverse order.                                                                                                                                                |
| rpad(x1, bigint size, x2)           | varchar          | Right pads x1 to size characters with x2. If size is less than the length of<br>x1, the result is truncated to size characters. size must not be negative and<br>x2 must be non-empty.         |
| rtrim(x)                            | varchar          | Removes trailing whitespace from x.                                                                                                                                                            |
| split(x1, x2)                       | array(varchar)   | Splits x1 on delimiter x2 and returns an array.                                                                                                                                                |
| split(x1, x2, bigint limit)         | array(varchar)   | Splits x1 on delimiter x2 and returns an array. The last element in the<br>array always contain everything left in the x1. limit must be a positive<br>number.                                 |
| split_part(x1, x2, bigint pos)      | varchar          | Splits x1 on delimiter x2 and returns the varchar field at pos. Field<br>indexes start with 1. If pos is larger than the number of fields, then null is<br>returned.                           |
| strpos(x1, x2)                      | bigint           | Returns the starting position of the first instance of x2 in x1. Positions<br>start with 1. If not found, 0 is returned.                                                                       |
| strpos(x1, x2,bigint instance)      | bigint           | Returns the position of the Nth instance of x2 in x1. Instance must be a<br>positive number. Positions start with 1. If not found, 0 is returned.                                              |
| strrpos(x1, x2)                     | bigint           | Returns the starting position of the last instance of x2 in x1. Positions<br>start with 1. If not found, 0 is returned.                                                                        |
| strrpos(x1, x2, bigint instance)    | bigint           | Returns the position of the Nth instance of x2 in x1 starting from the end<br>of x1. instance must be a positive number. Positions start with 1. If not<br>found, 0 is returned.               |
| position(x2 IN x1)                  | bigint           | Returns the starting position of the first instance of x2 in x1. Positions<br>start with 1. If not found, 0 is returned.                                                                       |
| substr(x, bigint start)             | varchar          | Returns the rest of x from the starting position start. Positions start with<br>1. A negative starting position is interpreted as being relative to the end of<br>x.                           |
| substr(x, bigint start, bigint len) | varchar          | Returns a substring from x of length len from the starting position start.<br>Positions start with 1. A negative starting position is interpreted as being<br>relative to the end of x.        |
| trim(x)                             | varchar          | Removes leading and trailing whitespace from x.                                                                                                                                                |
| upper(x)                            | varchar          | Converts x to uppercase.                                                                                                                                                                       |
