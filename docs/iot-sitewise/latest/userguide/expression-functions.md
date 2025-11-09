# Use functions in formula expressions

You can use the following functions to operate on data in your formula
expressions.

Transforms and metrics support different functions. The following table indicates
which types of functions are compatible with each type of formula property.

###### Note

You can include a maximum of 10 functions in a formula expression.

| Function type                                                                                                                          | Transforms | Metrics |
| -------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------- |
| [Use common functions in formula<br>expressions](expression-common-functions.md "expression-common-functions.md")                      | Yes        | Yes     |
| [Use comparison functions in formula<br>expressions](expression-comparison-functions.md "expression-comparison-functions.md")          | Yes        | Yes     |
| [Use conditional functions in formula<br>expressions](expression-conditional-functions.md "expression-conditional-functions.md")       | Yes        | Yes     |
| [Use string functions in formula<br>expressions](expression-string-functions.md "expression-string-functions.md")                      | Yes        | Yes     |
| [Use aggregation functions in formula<br>expressions](expression-aggregation-functions.md "expression-aggregation-functions.md")       | No         | Yes     |
| [Use temporal functions in formula<br>expressions](expression-temporal-functions.md "expression-temporal-functions.md")                | Yes        | Yes     |
| [Use date and time functions in<br>formula expressions](expression-date-and-time-functions.md "expression-date-and-time-functions.md") | Yes        | Yes     |

## Function syntax

You can use the following syntax to create functions:

Regular syntax

With the regular syntax, the function name is followed by parentheses with
zero or more arguments.

``function_name`(`argument1,
 argument2, argument3, ...`)`. For example, functions with
 the regular syntax might look like `log(x)`and`contains(s,
substring)`.

Uniform function call syntax (UFCS)

UFCS enables you to call functions using the syntax for method calls in
object-oriented programming. With UFCS, the first argument is followed by dot
(`.`), then the function name and the remaining arguments (if any)
inside parentheses.

``argument1`.`function_name`(`argument2`,
`argument3`, ...)`. For example, functions
 with UFCS might look like `x.log()`and
`s.contains(substring)`.

You can also use UFCS to chain subsequent functions. AWS IoT SiteWise uses the
evaluation result of the current function as the first argument for the next
function.

For example, you can use
`message.jp('$.status').lower().contains('fail')` instead of
`contains(lower(jp(message, '$.status')),'fail')`.

For more information, visit the [D
Programming Language](https://tour.dlang.org/tour/en/gems/uniform-function-call-syntax-ufcs "https://tour.dlang.org/tour/en/gems/uniform-function-call-syntax-ufcs") website.

###### Note

You can use UFCS for all AWS IoT SiteWise functions.

AWS IoT SiteWise functions are not case sensitive. For example, you can use
`lower(s)` and `Lower(s)` interchangeably.
