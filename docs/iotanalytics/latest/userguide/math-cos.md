End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# cos(Decimal)

Returns the cosine of a number in radians. `Decimal` arguments are rounded to
double precision before function application.

Examples: `cos(0)` = 1

| Argument type | Result                                                                                                                                                                                     |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `Int`         | `Decimal` (with double precision), the cosine of the argument. Imaginary results are returned as `Undefined`.                                                                              |
| `Decimal`     | `Decimal` (with double precision), the cosine of the argument. Imaginary results are returned as `Undefined`.                                                                              |
| `Boolean`     | `Undefined`.                                                                                                                                                                               |
| `String`      | `Decimal` (with double precision), the cosine of the argument. If the string cannot be converted to a `Decimal`, the result is `Undefined`. Imaginary results are returned as `Undefined`. |
| Array         | `Undefined`.                                                                                                                                                                               |
| Object        | `Undefined`.                                                                                                                                                                               |
| Null          | `Undefined`.                                                                                                                                                                               |
| Undefined     | `Undefined`.                                                                                                                                                                               |
