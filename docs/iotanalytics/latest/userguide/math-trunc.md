End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# trunc(Decimal, Integer)

Truncates the first argument to the number of `Decimal` places specified by the
second argument. If the second argument is less than zero, it will be set to zero. If the
second argument is greater than 34, it will be set to 34. Trailing zeros are stripped from the
result.

Examples:

`trunc(2.3, 0)` = 2

`trunc(2.3123, 2)` = 2.31

`trunc(2.888, 2)` = 2.88

`trunc(2.00, 5)` = 2

| Argument type 1              | Argument type 2   | Result                                                                                                                                                                                                                                                                          |
| ---------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Int`                        | `Int`             | The source value.                                                                                                                                                                                                                                                               |
| `Int` / `Decimal` / `String` | `Int` / `Decimal` | The first argument is truncated to the length described by the second argument. The<br>second argument, if not an `Int`, will be rounded down to the nearest<br>`Int`. Strings are converted to `Decimal` values. If the string<br>conversion fails, the result is `Undefined`. |
| Other Value                  |                   | Undefined.                                                                                                                                                                                                                                                                      |
