# Monotonic Expressions and Operators

Since Amazon Kinesis Data Analytics queries operate on infinite streams of rows, some operations are only possible if something is known about those streams.

For example, given a stream of orders, it makes sense to ask for a stream summarizing orders by day and product (because day is increasing) but not to ask for a stream summarizing orders by product and shipping state. We can never complete the summary of, say Widget X to Oregon, because we never see the 'last' order of a Widget to Oregon.

This property, of a stream being sorted by a particular column or expression, is called monotonicity.

Some time-related definitions:

- **Monotonic**. An expression is monotonic if it is ascending or descending. An equivalent phrasing is "non-decreasing or non-increasing."
- **Ascending**. An expression e is ascending within a stream if the value of e for a given row is always greater than or equal to the value in the previous row.
- **Descending**. An expression e is descending within a stream if the value of e for a given row is always less than or equal to the value in the previous row.
- **Strictly Ascending**. An expression e is strictly ascending within a stream if for the value of e for a given row is always greater than the value in the previous row.
- **Strictly Descending**. An expression e is strictly descending within a stream if the value of e for a given row is always less than the value in the previous row.
- **Constant**. An expression e is constant within a stream if the value of e for a given row is always equal to the value in the previous row.
  Note that by this definition, a constant expression is considered monotonic.

## Monotonic columns

The ROWTIME system column is ascending. The ROWTIME column is not strictly ascending: it is acceptable for consecutive rows to have the same timestamp.

Amazon Kinesis Data Analytics prevents a client from inserting a row into a stream whose timestamp is less than the previous row it wrote into the stream. Amazon Kinesis Data Analytics also ensures
that if multiple clients are inserting rows into the same stream, the rows are merged so that the ROWTIME column is ascending.

Clearly it would be useful to assert, for instance, that the orderId column is ascending; or that no orderId is ever more than 100 rows from sorted order.
However, declared sort keys are not supported in the current release.

## Monotonic expressions

Amazon Kinesis Data Analytics can deduce that an expression is monotonic if it knows that its arguments are monotonic. (See also the
[Monotonic Function](sql-reference-monotonic.md "sql-reference-monotonic.md").)

Another definition:

Functions or operators that are monotonic

A function or operator is monotonic if, when applied to a strictly increasing sequence of values, it yields a monotonic sequence of results.

For example, the FLOOR function, when applied to the ascending inputs {1.5, 3, 5, 5.8, 6.3}, yields {1, 3, 5, 5, 6}. Note that the input is strictly ascending,
but the output is merely ascending (includes duplicate values).

## Rules for deducing monotonicity

Amazon Kinesis Data Analytics requires that one or more grouping expressions are valid in order for a streaming GROUP BY statement to be valid. In other cases, Amazon Kinesis Data Analytics may
be able to operate more efficiently if it knows about monotonicity; for example it may be able to remove entries from a table of windowed aggregate totals if it
knows that a particular key will never be seen on the stream again.

In order to exploit monotonicity in this way, Amazon Kinesis Data Analytics uses a set of rules for deducing the monotonicity of an expression. Here are the rules for deducing monotonicity:

| Expression                                                                                                                                                                                                                                                                                                                                        | Monotonicity                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| c                                                                                                                                                                                                                                                                                                                                                 | Constant                                                                                                                                                                                            |
| [FLOOR](sql-reference-floor.md "sql-reference-floor.md")(m)                                                                                                                                                                                                                                                                                       | Same as m, but not strict                                                                                                                                                                           |
| [CEIL / CEILING](sql-reference-ceil.md "sql-reference-ceil.md")(m)                                                                                                                                                                                                                                                                                | Same as m, but not strict                                                                                                                                                                           |
| [CEIL / CEILING](sql-reference-ceil.md "sql-reference-ceil.md")(m TO timeUnit)                                                                                                                                                                                                                                                                    | Same as m, but not strict                                                                                                                                                                           |
| [FLOOR](sql-reference-floor.md "sql-reference-floor.md")(m TO timeUnit)                                                                                                                                                                                                                                                                           | Same as m, but not strict                                                                                                                                                                           |
| [SUBSTRING](sql-reference-substring.md "sql-reference-substring.md")(m FROM 0 FOR c)                                                                                                                                                                                                                                                              | Same as m, but not strict                                                                                                                                                                           |
| + m                                                                                                                                                                                                                                                                                                                                               | Same as m                                                                                                                                                                                           |
| - m                                                                                                                                                                                                                                                                                                                                               | Reverse of m                                                                                                                                                                                        |
| m + c c + m                                                                                                                                                                                                                                                                                                                                       | Same as m                                                                                                                                                                                           |
| m1 + m2                                                                                                                                                                                                                                                                                                                                           | Same as m1, if m1 and m2 have same direction; otherwise not monotonic                                                                                                                               |
| c - m                                                                                                                                                                                                                                                                                                                                             | Reverse of m                                                                                                                                                                                        |
| m \* c c \* m                                                                                                                                                                                                                                                                                                                                     | Same as m if c is positive; reverse of m is c is negative; constant (0) c is 0                                                                                                                      |
| c / m                                                                                                                                                                                                                                                                                                                                             | Same as m if m is always positive or always negative, and c and m have same sign; reverse of m if m is always positive or always negative, and c and m have different sign; otherwise not monotonic |
|                                                                                                                                                                                                                                                                                                                                                   | Constant                                                                                                                                                                                            |
| [LOCALTIME](sql-reference-localtime.md "sql-reference-localtime.md") [LOCALTIMESTAMP](sql-reference-local-timestamp.md "sql-reference-local-timestamp.md") [CURRENT_ROW_TIMESTAMP](sql-reference-current-row-timestamp.md "sql-reference-current-row-timestamp.md") [CURRENT_DATE](sql-reference-current-date.md "sql-reference-current-date.md") | Ascending                                                                                                                                                                                           | Throughout the table, c is a constant, and m (also m1 and m2) is a monotonic expression. |
