End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# sign(Decimal)

Returns the sign of the given number. When the sign of the argument is positive, 1 is
returned. When the sign of the argument is negative, -1 is returned. If the argument is 0, 0 is
returned.

Examples:

`sign(-7)` = -1

`sign(0)` = 0

`sign(13)` = 1

| Argument type | Result                                                                                                                                                                                                                |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Int`         | `Int`, the sign of the `Int` value.                                                                                                                                                                                   |
| `Decimal`     | `Int`, the sign of the `Decimal` value.                                                                                                                                                                               |
| `String`      | `Int`, the sign of the `Decimal` value. The string if converted to a `Decimal` value, and the sign of the `Decimal` value is returned. If the `String` cannot be converted to a `Decimal`, the result is `Undefined`. |
| Other Value   | `Undefined`.                                                                                                                                                                                                          |
