End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# power(Decimal, Decimal)

Returns the first argument raised to the second argument. `Decimal` arguments
are rounded to double precision before function application.

Examples: `power(2, 5)` = 32.0

| Argument type 1              | Argument type 2              | Output                                                                                                                                                                                                                          |
| ---------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Int` / `Decimal`            | `Int` / `Decimal`            | A `Decimal` (with double precision), the first argument raised to the<br>second argument's power.                                                                                                                               |
| `Int` / `Decimal` / `String` | `Int` / `Decimal` / `String` | A `Decimal` (with double precision), the first argument raised to the<br>second argument's power. Any strings are converted to `Decimals`. If any<br>`String` fails to be converted to `Decimal`, the result is<br>`Undefined`. |
| Other Value                  | Other Value                  | `Undefined`.                                                                                                                                                                                                                    |
