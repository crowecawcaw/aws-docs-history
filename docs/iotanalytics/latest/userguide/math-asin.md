End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# asin(Decimal)

Returns the inverse sine of a number in radians. `Decimal` arguments are
rounded to double precision before function application.

Examples: `asin(0)` = 0.0

| Argument type | Result                                                                                                                                                                                  |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Int`         | `Decimal` (with double precision), the inverse sine of the argument.<br>Imaginary results are returned as `Undefined`.                                                                  |
| `Decimal`     | `Decimal` (with double precision), the inverse sine of the argument.<br>Imaginary results are returned as `Undefined`.                                                                  |
| `Boolean`     | `Undefined`.                                                                                                                                                                            |
| `String`      | `Decimal` (with double precision), the inverse sine of the argument. If<br>the string cannot be converted, the result is `Undefined`. Imaginary results<br>are returned as `Undefined`. |
| Array         | `Undefined`.                                                                                                                                                                            |
| Object        | `Undefined`.                                                                                                                                                                            |
| Null          | `Undefined`.                                                                                                                                                                            |
| Undefined     | `Undefined`.                                                                                                                                                                            |
