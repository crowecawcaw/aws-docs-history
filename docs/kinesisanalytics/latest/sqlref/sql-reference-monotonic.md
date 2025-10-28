# Monotonic Function

```
MONOTONIC(<expression>)
```

Streaming GROUP BY requires that at least one of the grouped expressions be monotonic and
non-constant. The only column known in advance to be monotonic is ROWTIME. For more information, see [Monotonic Expressions and Operators](sql-reference-monotonic-expressions-operators.md "sql-reference-monotonic-expressions-operators.md").

The MONOTONIC function allows you to declare that a given expression is monotonic, enabling
a streaming GROUP BY to use that expression as a key.

The MONOTONIC function evaluates its argument and returns the result (as the same type as
its argument).

By enclosing an expression in MONOTONIC, you are asserting that values of that expression
are either non-increasing or non-decreasing and never change direction. For example, if you have
a stream LINEITEMS consisting of the line items of orders, and you wrote MONOTONIC(orderId), you
are asserting that line items are consecutive in the stream. It would be OK if there were line
items for order 1000, followed by line items for order 1001, followed by line items for order 1005. It would be illegal if there were then a line item for order 1001 (that is, the line item
sequence became 1000, 1001, 1005, 1001). Similarly, a line item sequence of 987, 974, 823 would
be legal, but the following line item sequences would be illegal:

- 987, 974, 823, 973
- 987, 974, 823, 1056
  An expression declared monotonic can decrease, or even have arbitrary order.

Note that the definition of MONOTONIC is precisely what is needed for GROUP BY to make
progress.

If an expression declared monotonic is not monotonic (that is, if the assertion is not valid
for the actual data) then Amazon Kinesis Data Analytics behavior is unspecified.

In other words, if you are certain that an expression is monotonic, you can use this
MONOTONIC function to enable Amazon Kinesis Data Analytics to treat the expression as monotonic.

However, if you are mistaken and the values resulting from evaluating the expression change
from ascending to descending or from descending to ascending, unexpected results may arise.
Amazon Kinesis Data Analytics streaming SQL will take you at your word and operate on your assurance that the
expression is monotonic. But if in fact it is not monotonic, the resulting Amazon Kinesis Data Analytics behavior
cannot be determined in advance, and so results may not be as expected or desired.
