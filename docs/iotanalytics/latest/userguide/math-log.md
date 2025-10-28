End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# log(Decimal)

Returns the base 10 logarithm of the argument. `Decimal` arguments are rounded
to double precision before function application.

Examples: `log(100)` = 2.0

| Argument type | Result                                                                                                                                             |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Int`         | `Decimal` (with double precision), the base 10 log of the argument.                                                                                |
| `Decimal`     | `Decimal` (with double precision), the base 10 log of the argument.                                                                                |
| `Boolean`     | `Undefined`.                                                                                                                                       |
| `String`      | `Decimal` (with double precision), the base 10 log of the argument. If the `String` cannot be converted to a `Decimal`, the result is `Undefined`. |
| Array         | `Undefined`.                                                                                                                                       |
| Object        | `Undefined`.                                                                                                                                       |
| Null          | `Undefined`.                                                                                                                                       |
| Undefined     | `Undefined`.                                                                                                                                       |
