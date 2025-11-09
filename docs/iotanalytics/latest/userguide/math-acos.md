End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# acos(Decimal)

Returns the inverse cosine of a number in radians. `Decimal` arguments are
rounded to double precision before function application.

Examples: `acos(0)` = 1.5707963267948966

| Argument type | Result                                                                                                                                                                                   |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Int`         | `Decimal` (with double precision), the inverse cosine of the argument.<br>Imaginary results are returned as `Undefined`.                                                                 |
| `Decimal`     | `Decimal` (with double precision), the inverse cosine of the argument.<br>Imaginary results are returned as `Undefined`.                                                                 |
| `Boolean`     | `Undefined`.                                                                                                                                                                             |
| `String`      | `Decimal` (with double precision) the inverse cosine of the argument. If<br>the string cannot be converted, the result is `Undefined`. Imaginary results<br>are returned as `Undefined`. |
| Array         | `Undefined`.                                                                                                                                                                             |
| Object        | `Undefined`.                                                                                                                                                                             |
| Null          | `Undefined`.                                                                                                                                                                             |
| Undefined     | `Undefined`.                                                                                                                                                                             |
