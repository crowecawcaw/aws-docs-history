End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# mod(Decimal, Decimal)

Returns the remainder of the division of the first argument of the second argument. You
can also use `%` as an infix operator for the same modulo functionality.

Examples: `mod(8, 3)` = 2

| Left operand                 | Right operand                | Output                                                                                                                     |
| ---------------------------- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `Int`                        | `Int`                        | `Int`, the first argument modulo of the second argument.                                                                   |
| `Int` / `Decimal`            | `Int` / `Decimal`            | `Decimal`, the first argument modulo of the second argument.                                                               |
| `String` / `Int` / `Decimal` | `String` / `Int` / `Decimal` | If all strings convert to `Decimals`, the result if the first argument modulo the second argument. Otherwise, `Undefined`. |
| Other Value                  | Other Value                  | `Undefined`.                                                                                                               |
