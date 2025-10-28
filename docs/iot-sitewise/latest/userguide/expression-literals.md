# Use literals in formula expressions

AWS IoT SiteWise supports the use of literals in expressions and formulas. Literals are fixed values that represent a specific data type. In AWS IoT SiteWise, you can define number and string literals in formula expressions. Literals can be used in various contexts, including data transformations, alarm conditions, and visualization calculations.

- Numbers

Use numbers and scientific notation to define integers and doubles. You can use
[E
notation](https://en.wikipedia.org/wiki/Scientific_notation#E_notation "https://en.wikipedia.org/wiki/Scientific_notation#E_notation") to express numbers with scientific notation.

Examples: `1`, `2.0`, `.9`, `-23.1`,
`7.89e3`, `3.4E-5`

- Strings

Use the `'` (quote) and `"` (double quote) characters to
define strings. The quote type for the start and end must match. To escape a quote
that matches the one that you use to declare a string, include that quote character
twice. This is the only escape character in AWS IoT SiteWise strings.

Examples: `'active'`, `"inactive"`, `'{"temp":
 52}'`, `"{""temp"": ""high""}"`
