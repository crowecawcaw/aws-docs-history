# Numeric Types and Precision

For DECIMAL we support a maximum of 18 digits for precision and scale.

Precision specifies the maximum number of decimal digits that can be stored in the column,
both to the right and to the left of the decimal point. You can specify precisions ranging from
1 digit to 18 digits or use the default precision of 18 digits.

Scale specifies the maximum number of digits that can be stored to the right of the decimal
point. Scale must be less than or equal to the precision. You can specify a scale ranging from 0
digits to 18 digits, or use the default scale of 0 digits.

###### Rule for Divide

Let p1, s1 be the precision and scale of the first operand, such as DECIMAL (10,1).

Let p2, s2 be the precision and scale of the second operand, such as DECIMAL (10,3).

Let p, s be the precision and scale of the result.

Let d be the number of whole digits in the result. Then, the result type is a decimal
as shown following:

|                          |                                                           |
| ------------------------ | --------------------------------------------------------- |
| `d = p1<br>• s1 + s2`    | D = 10<br>• 1 + 3<br>Number of whole digits in result = 6 |
| s <= MAX (6, s1 + p2 +1) | S <= MAX (6, 1 + 10 + 1)<br>Scale of result = 14          |
| p = d + s                | Precision of result = 18                                  |

Precision and scale are capped at their maximum values (18, where scale cannot be larger
than precision).

Precedence is first giving at least the scale of the first argument (s >= s1) followed by
enough whole digits to represent the result without overflow

###### Rule for Multiply

Let p1, s1 be the precision and scale of the first operand DECIMAL (10,1).

Let p2, s2 be the precision and scale of the second operand DECIMAL (10,3).

Let p, s be the precision and scale of the result.

Then, the result type is a decimal as shown following:

|             |                                         |
| ----------- | --------------------------------------- |
| p = p1 + p2 | p = 10 + 10<br>Precision of result = 18 |
| s = s1 + s2 | s = 1 + 3<br>Scale of result = 4        |

###### Rule for Sum or Subtraction

Type-inference strategy whereby the result type of a call is the decimal sum of two exact
numeric operands where at least one of the operands is a decimal.

Let p1, s1 be the precision and scale of the first operand DECIMAL (10,1).

Let p2, s2 be the precision and scale of the second operand DECIMAL (10,3).

Let p, s be the precision and scale of the result, as shown following:

|                                         |                                                        |
| --------------------------------------- | ------------------------------------------------------ |
| s = max(s1, s2)                         | s = max (1,3)<br>Scale of result = 3                   |
| p = max(p1<br>• s1, p2<br>• s2) + s + 1 | p = max(10-1,10-3) + 3 + 1<br>Precision of result = 11 |

s and p are capped at their maximum values
