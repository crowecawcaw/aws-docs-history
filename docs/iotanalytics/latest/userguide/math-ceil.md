End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# ceil(Decimal)

Rounds the given `Decimal` up to the nearest `Int`.

Examples:

`ceil(1.2)` = 2

`ceil(11.2)` = -1

| Argument type | Result                                                                                                                                                        |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Int`         | `Int`, the argument value.                                                                                                                                    |
| `Decimal`     | `Int`, the string is converted to `Decimal` and rounded up to the nearest `Int`. If the string cannot be converted to a `Decimal`, the result is `Undefined`. |
| Other Value   | `Undefined`.                                                                                                                                                  |
