# PartiQL arithmetic, comparison, and logical operators for DynamoDB

PartiQL in Amazon DynamoDB supports the following [SQL standard
operators](https://www.w3schools.com/sql/sql_operators.asp "https://www.w3schools.com/sql/sql_operators.asp").

###### Note

Any SQL operators that are not included in this list are not currently supported in
DynamoDB.

## Arithmetic operators

| Operator | Description |
| -------- | ----------- |
| `+`      | Add         |
| `-`      | Subtract    |

## Comparison operators

| Operator | Description              |
| -------- | ------------------------ |
| `=`      | Equal to                 |
| `<>`     | Not Equal to             |
| `!=`     | Not Equal to             |
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |

## Logical operators

| Operator  | Description                                                                                                                                                                                                                                                                                                                            |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AND`     | `TRUE` if all the conditions separated by `AND`<br>are `TRUE`                                                                                                                                                                                                                                                                          |
| `BETWEEN` | `TRUE` if the operand is within the range of comparisons.<br>This operator is inclusive of the lower and upper bound of the operands on which you apply it.                                                                                                                                                                            |
| `IN`      | `TRUE` if the operand is equal to one of a list of<br>expressions (at max 50 hash attribute values or at max 100 non-key<br>attribute values).<br>Results are returned in pages of up to 10 items. If the<br>`IN` list contains more values, you must use the<br>`NextToken` returned in the response to retrieve subsequent<br>pages. |
| `IS`      | `TRUE` if the operand is a given, PartiQL data type, including<br>`NULL` or `MISSING`                                                                                                                                                                                                                                                  |
| `NOT`     | Reverses the value of a given Boolean expression                                                                                                                                                                                                                                                                                       |
| `OR`      | `TRUE` if any of the conditions separated by<br>`OR` are `TRUE`                                                                                                                                                                                                                                                                        |

For more information about using logical operators, see [Making
comparisons](Expressions.md#Expressions.OperatorsAndFunctions.Comparators "Expressions.md#Expressions.OperatorsAndFunctions.Comparators") and [Logical
evaluations](Expressions.md#Expressions.OperatorsAndFunctions.LogicalEvaluations "Expressions.md#Expressions.OperatorsAndFunctions.LogicalEvaluations").
