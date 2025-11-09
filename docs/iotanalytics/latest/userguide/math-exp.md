End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# exp(Decimal)

Returns
`e` raised to the decimal argument.
`Decimal` arguments are rounded to double precision before function
application.

Examples: `exp(1)` = 1

| Argument type | Result                                                                                                                              |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `Int`         | `Decimal` (with double precision), e^argument.                                                                                      |
| `Decimal`     | `Decimal` (with double precision), e^argument                                                                                       |
| `String`      | `Decimal` (with double precision), e^argument. If the `String`<br>cannot be converted to a `Decimal`, the result if<br>`Undefined`. |
| Other Value   | `Undefined`.                                                                                                                        |
