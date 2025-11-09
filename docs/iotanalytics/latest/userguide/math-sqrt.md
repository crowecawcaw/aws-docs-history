End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# sqrt(Decimal)

Returns the square root of a number. `Decimal` arguments are rounded to double
precision before function application.

Examples: `sqrt(9)` = 3.0

| Argument type | Result                                                                                                           |
| ------------- | ---------------------------------------------------------------------------------------------------------------- |
| `Int`         | The square root of the argument.                                                                                 |
| `Decimal`     | The square root of the argument.                                                                                 |
| `Boolean`     | `Undefined`.                                                                                                     |
| `String`      | The square root of the argument. If the string cannot be converted to a<br>`Decimal`, the result is `Undefined`. |
| `Array`       | `Undefined`.                                                                                                     |
| `Object`      | `Undefined`.                                                                                                     |
| `Null`        | `Undefined`.                                                                                                     |
| `Undefined`   | `Undefined`.                                                                                                     |
