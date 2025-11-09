End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# atan2(Decimal, Decimal)

Returns the angle, in radians, between the positive x-axis and the (x, y) point defined in
the two arguments. The angle is positive for counter-clockwise angles (upper half-plane, y >
0), and negative for clockwise angles
`Decimal` arguments are rounded to double precision before function
application.

Examples: `atan(1, 0)` = 1.5707963267948966

| Argument type                | Argument type                | Result                                                                                                                |
| ---------------------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `Int` / `Decimal`            | `Int` / `Decimal`            | `Decimal` (with double precision), the angle between the x-axis and the<br>specified (x,y) point                      |
| `Int` / `Decimal` / `String` | `Int` / `Decimal` / `String` | `Decimal`, the inverse tangent of the point described. If a string cannot<br>be converted, the result is `Undefined`. |
| Other Value                  | Other Value                  | `Undefined`.                                                                                                          |
