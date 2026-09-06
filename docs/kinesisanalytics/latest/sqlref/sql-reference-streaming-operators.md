

# Streaming SQL Operators
<a name="sql-reference-streaming-operators"></a>
<a name="TOC1"></a>
**Subquery Operators**  
Operators are used in queries and subqueries to combine or test data for various properties, attributes, or relationships.

The available operators are described in the topics that follow, grouped into the following categories:
+ [Scalar Operators](#scalaroprs)
  + [Operator Types](#OPRTYPES)
  + [Precedence](#PRECEDENCE)
+ [Arithmetic Operators](#ARITHMOPRS)
+ [String Operators](sql-reference-string-operators.md)
  +  (Concatenation)
  + LIKE patterns
  + SIMILAR TO patterns
+ [Date, Timestamp, and Interval Operators](sql-reference-date-timestamp-interval.md)
+ [Logical Operators](sql-reference-logical-operators.md)
  + 3-state boolean logic
  + Examples

## IN Operator
<a name="INOPERATOR"></a>

As an operator in a condition test, IN tests a scalar or row value for membership in a list of values, a relational expression, or a subquery.

```
Examples:
1. --- IF column IN ('A','B','C')
2. --- IF (col1, col2) IN (
    select a, b from my_table
    )
```

Returns TRUE if the value being tested is found in the list, in the result of evaluating the relational expression, or in the rows returned by the subquery; returns FALSE otherwise.

**Note**  
IN has a different meaning and use in [CREATE FUNCTION](sql-reference-create-function.md). 

## EXISTS Operator
<a name="EXISTSOPERATOR"></a>

Tests whether a relational expression returns any rows; returns TRUE if any row is returned, FALSE otherwise.

## Scalar Operators
<a name="scalaroprs"></a>
<a name="OPRTYPES"></a>
**Operator Types**  
The two general classes of scalar operators are:
+ unary: A unary operator operates on only one operand. A unary operator typically appears with its operand in this format:

  ```
  operator operand
  ```
+ binary: A binary operator operates on two operands. A binary operator appears with its operands in this format:

  ```
  operand1 operator operand2
  ```

A few operators that use a different format are noted specifically in the operand descriptions below.

If an operator is given a null operand, the result is almost always null (see the topic on logical operators for exceptions).
<a name="PRECEDENCE"></a>
**Precedence**  
Streaming SQL follows the usual precedence of operators:

1. Evaluate bracketed sub-expressions.

1. Evaluate unary operators (e.g., \+ or -, logical NOT).

1. Evaluate multiplication and divide (\* and /).

1. Evaluate addition and subtraction (\+ and -) and logical combination (AND and OR).

If one of the operands is NULL, the result is also NULL If the operands are of different but comparable types, the result will be of the type with the greatest precision. If the operands are of the same type, the result will be of the same type as the operands. For instance 5/2 = 2, not 2.5, as 5 and 2 are both integers. 

## Arithmetic Operators
<a name="ARITHMOPRS"></a>


| Operator | Unary/Binary | Description | 
| --- | --- | --- | 
| \+ | U | Identity | 
| - | U | Negation | 
| \+ | B | Addition | 
| - | B | Subtraction | 
| \* | B | Multiplication | 
| / | B | Division | 



Each of these operators works according to normal arithmetic behavior, with the following caveats:

1. If one of the operands is NULL, the result is also NULL

1. If the operands are of different but comparable types, the result will be of the type with the greatest precision.

1. If the operands are of the same type, the result will be of the same type as the operands. For instance 5/2 = 2, not 2.5, as 5 and 2 are both integers.

### Examples
<a name="operators_examples"></a>


| Operation | Result | 
| --- | --- | 
| 1 \+ 1 | 2 | 
| 2.0 \+ 2.0 | 4.0 | 
| 3.0 \+ 2 | 5.0 | 
| 5 / 2 | 2 | 
| 5.0 / 2 | 2.500000000000 | 
| 5\*2\+2 | 12 | 