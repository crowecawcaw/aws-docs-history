Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Numeric format strings

Following, you can find a reference for numeric format strings.

The following format strings apply to functions such as TO_NUMBER and TO_CHAR.

- For examples of formatting strings as numbers, see [TO_NUMBER](r_TO_NUMBER.md "r_TO_NUMBER.md").
- For examples of formatting numbers as strings, see [TO_CHAR](r_TO_CHAR.md "r_TO_CHAR.md").

| Format        | Description                                                                                        |
| ------------- | -------------------------------------------------------------------------------------------------- |
| 9             | Numeric value with the specified number of digits.                                                 |
| 0             | Numeric value with leading zeros.                                                                  |
| . (period), D | Decimal point.                                                                                     |
| , (comma)     | Thousands separator.                                                                               |
| CC            | Century code. For example, the 21st century started on<br>2001-01-01 (supported for TO_CHAR only). |
| FM            | Fill mode. Suppress padding blanks and zeroes.                                                     |
| PR            | Negative value in angle brackets.                                                                  |
| S             | Sign anchored to a number.                                                                         |
| L             | Currency symbol in the specified position.                                                         |
| G             | Group separator.                                                                                   |
| MI            | Minus sign in the specified position for numbers that are<br>less than 0.                          |
| PL            | Plus sign in the specified position for numbers that are<br>greater than 0.                        |
| SG            | Plus or minus sign in the specified position.                                                      |
| RN            | Roman numeral between 1 and 3999 (supported for TO_CHAR<br>only).                                  |
| TH or th      | Ordinal number suffix. Does not convert fractional<br>numbers or values that are less than zero.   |
