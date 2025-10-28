# Numeric format strings

The following numeric format strings apply to functions such as TO_NUMBER and TO_CHAR.

- For examples of formatting strings as numbers, see [TO_NUMBER](TO_NUMBER.md "TO_NUMBER.md").
- For examples of formatting numbers as strings, see [TO_CHAR](TO_CHAR.md "TO_CHAR.md").

| Format        | Description                                                                                     |
| ------------- | ----------------------------------------------------------------------------------------------- |
| 9             | Numeric value with the specified number of digits.                                              |
| 0             | Numeric value with leading zeros.                                                               |
| . (period), D | Decimal point.                                                                                  |
| , (comma)     | Thousands separator.                                                                            |
| CC            | Century code. For example, the 21st century started on 2001-01-01 (supported for TO_CHAR only). |
| FM            | Fill mode. Suppress padding blanks and zeroes.                                                  |
| PR            | Negative value in angle brackets.                                                               |
| S             | Sign anchored to a number.                                                                      |
| L             | Currency symbol in the specified position.                                                      |
| G             | Group separator.                                                                                |
| MI            | Minus sign in the specified position for numbers that are less than 0.                          |
| PL            | Plus sign in the specified position for numbers that are greater than 0.                        |
| SG            | Plus or minus sign in the specified position.                                                   |
| RN            | Roman numeral between 1 and 3999 (supported for TO_CHAR only).                                  |
| TH or th      | Ordinal number suffix. Does not convert fractional numbers or values that are less than zero.   |
