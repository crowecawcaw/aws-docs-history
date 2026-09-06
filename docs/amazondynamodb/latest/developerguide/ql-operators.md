

# PartiQL arithmetic, comparison, and logical operators for DynamoDB
<a name="ql-operators"></a>

PartiQL in Amazon DynamoDB supports the following [SQL standard operators](https://www.w3schools.com/sql/sql_operators.asp).

**Note**  
Any SQL operators that are not included in this list are not currently supported in DynamoDB.

## Arithmetic operators
<a name="ql-operators.arithmetic"></a>



| Operator | Description | 
| --- | --- | 
| \+ | Add | 
| - | Subtract | 

## Comparison operators
<a name="ql-operators.comparison"></a>



| Operator | Description | 
| --- | --- | 
| = | Equal to | 
| <> | Not Equal to | 
| \!= | Not Equal to | 
| > | Greater than | 
| < | Less than | 
| >= | Greater than or equal to | 
| <= | Less than or equal to | 

## Logical operators
<a name="ql-operators.logical"></a>



| Operator | Description | 
| --- | --- | 
| AND | TRUE if all the conditions separated by AND are TRUE | 
| BETWEEN | `TRUE` if the operand is within the range of comparisons.<br />This operator is inclusive of the lower and upper bound of the operands on which you apply it. | 
| IN | `TRUE` if the operand is equal to one of a list of expressions (at max 50 hash attribute values or at max 100 non-key attribute values).<br />Results are returned in pages of up to 10 items. If the `IN` list contains more values, you must use the `NextToken` returned in the response to retrieve subsequent pages. | 
| IS | TRUE if the operand is a given, PartiQL data type, including NULL or MISSING | 
| NOT | Reverses the value of a given Boolean expression | 
| OR | TRUE if any of the conditions separated by OR are TRUE | 

For more information about using logical operators, see [Making comparisons](Expressions.OperatorsAndFunctions.md#Expressions.OperatorsAndFunctions.Comparators) and [Logical evaluations](Expressions.OperatorsAndFunctions.md#Expressions.OperatorsAndFunctions.LogicalEvaluations).