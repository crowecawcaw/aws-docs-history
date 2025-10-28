# Use constants in formula expressions

In AWS IoT SiteWise, you can use constants in your expressions and formulas to represent fixed values or predefined parameters. Constants can be used in various contexts, such as data transformations, alarm conditions, or visualization calculations. By using constants, you can simplify your expressions and make them more readable and maintainable.

You can use the following common mathematical constants in your expressions. All
constants are case insensitive.

###### Note

If you define a variable with the same name as a constant, the variable overrides
the constant.

| Constant | Description                                                                                                                                                                                 |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `pi`     | The number pi (`π`): `3.141592653589793`                                                                                                                                                    |
| `e`      | The number e: `2.718281828459045`                                                                                                                                                           |
| `true`   | Equivalent to the number 1. In AWS IoT SiteWise, Booleans convert to their number equivalents.                                                                                              |
| `false`  | Equivalent to the number 0. In AWS IoT SiteWise, Booleans convert to their number equivalents.                                                                                              |
| `none`   | Equivalent to no value. You can use this constant to output nothing as the result of a [conditional expression](expression-conditional-functions.md "expression-conditional-functions.md"). |
