End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# abs(Decimal)

Returns the absolute value of a number.

Examples: `abs(-5)` returns 5.

| Argument type | Result                                                                                                                        |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `Int`         | `Int`, the absolute value of the argument.                                                                                    |
| `Decimal`     | `Decimal`, the absolute value of the argument                                                                                 |
| `Boolean`     | `Undefined`.                                                                                                                  |
| `String`      | `Decimal`. The result is the absolute value of the argument. If the string<br>cannot be converted, the result is `Undefined`. |
| Array         | `Undefined`.                                                                                                                  |
| Object        | `Undefined`.                                                                                                                  |
| Null          | `Undefined`.                                                                                                                  |
| Undefined     | `Undefined`.                                                                                                                  |
