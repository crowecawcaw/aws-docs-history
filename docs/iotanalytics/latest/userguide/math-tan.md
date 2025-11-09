End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# tan(Decimal)

Returns the tangent of a number in radians. `Decimal` values are rounded to
double precision before function application.

Examples: `tan(3)` = -0.1425465430742778

| Argument type | Result                                                                                                                                             |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Int`         | `Decimal` (with double precision), the tangent of the argument.                                                                                    |
| `Decimal`     | `Decimal` (with double precision), the tangent of the argument.                                                                                    |
| `Boolean`     | `Undefined`.                                                                                                                                       |
| `String`      | `Decimal` (with double precision), the tangent of the argument. If the<br>string cannot be converted to a `Decimal`, the result is<br>`Undefined`. |
| `Array`       | `Undefined`.                                                                                                                                       |
| `Object`      | `Undefined`.                                                                                                                                       |
| `Null`        | `Undefined`.                                                                                                                                       |
| `Undefined`   | `Undefined`.                                                                                                                                       |
