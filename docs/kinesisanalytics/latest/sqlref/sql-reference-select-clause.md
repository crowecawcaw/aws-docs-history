# SELECT clause

The <select-clause> uses the following items after the
STREAM keyword:

```
  <select-list> :=
    <select-item> { , <select-item> }...
 <select-item> :=
    <select-expression> [ [ AS ] <simple-identifier> ]
 <simple-identifier> :=
    <identifier> | <quoted-identifier>
 <select-expression> :=
    <identifier> . *  | *  | <expression>
```

## Expressions

Each of these expressions may be:

- a scalar expression
- a call to an [Aggregate Functions](sql-reference-aggregate-functions.md "sql-reference-aggregate-functions.md"), if this is an
  aggregating query (see [GROUP BY clause](sql-reference-group-by-clause.md "sql-reference-group-by-clause.md"))
- a call to an [Analytic Functions](sql-reference-analytic-functions.md "sql-reference-analytic-functions.md"), if this is not an
  aggregating query
- the wildcard expression \* expands to all columns of all relations in the FROM
  clause
- the wildcard expression alias.\* expands to all columns of the relation named
  alias
- the [ROWTIME](sql-reference-rowtime.md "sql-reference-rowtime.md")
- a [CASE expression](#sql-reference-select-clause-caseexpr "#sql-reference-select-clause-caseexpr")

Each expression may be assigned an alias, using the AS column_name syntax. This is the
name of the column in the result set of this query. If this query is in the FROM clause of
an enclosing query, this will be the name that will be used to reference the column. The
number of columns specified in the AS clause of a stream reference must match the
number of columns defined in the original stream.

Amazon Kinesis Data Analytics has a few simple rules to derive the alias of an expression that does not have
an alias. The default alias of a column expression is the name of the column: for example,
EMPS.DEPTNO is aliased DEPTNO by default. Other expressions are given an alias like EXPR$0.
You should not assume that the system will generate the same alias each time.

In a streaming query, aliasing a column AS ROWTIME has a special meaning: For more information, see
[ROWTIME](sql-reference-rowtime.md "sql-reference-rowtime.md").

###### Note

All streams have an implicit column called ROWTIME.
This column may impact your use of the syntax 'AS t(c1, c2, ...)' that is now supported by
SQL:2008. Previously in a FROM clause you could only write

```
SELECT ... FROM r1 AS t1 JOIN r2 as t2

```

but t1 and t2 would have the same columns as r1 and t2. The AS syntax enables you to
rename r1's columns by writing the following:

```
SELECT ... FROM r1 AS t1(a, b, c)

```

(r1 must have precisely 3 columns for this syntax to work).

If r1 is a stream, then ROWTIME is implicitly included, but it doesn't count as a column.
As a result, if a stream has 3 columns without including ROWTIME, you cannot rename ROWTIME
by specifying 4 columns. For example, if the stream Bids has three columns, the following
code is invalid.

```
SELECT STREAM * FROM Bids (a, b, c, d)

```

It is also invalid to rename another column ROWTIME, as in the following example.

```
SELECT STREAM * FROM Bids (ROWTIME, a, b)

```

because that would imply renaming another column to ROWTIME. For more information about expressions
and literals, see [Expressions and Literals](sql-reference-expressions.md "sql-reference-expressions.md").

## CASE expression

The CASE expression enables you to specify a set of discrete test expressions and a
specific return-value (expression) for each such test. Each test expression is specified
in a WHEN clause; each return-value expression is specified in the corresponding THEN
clause. Multiple such WHEN-THEN pairs can be specified.

If you specify a comparison-test-expression before the first WHEN clause, then each
expression in a WHEN clause is compared to that comparison-test-expression. The first one to
match the comparison-test-expression causes the return-value from its corresponding THEN
clause to be returned. If no WHEN clause expression matches the comparison-test-expression,
the return-value is null unless an ELSE clause is specified, in which case the return-value
in that ELSE clause is returned.

If you do not specify a comparison-test-expression before the first WHEN clause, then each
expression in a WHEN clause is evaluated (left to right) and the first one to be true causes
the return-value from its corresponding THEN clause to be returned. If no WHEN clause
expression is true, the return-value is null unless an ELSE clause is specified, in which
case the return-value in that ELSE clause is returned.

## VALUES

VALUES uses expressions to calculate one or more row values, and is often used within a
larger command. When creating more than one row, the VALUES clause must specify the same
number of elements for every row. The resulting table-columns data-types are derived from
the explicit or inferred types of the expressions appearing in that column. VALUES is
allowed syntactically wherever SELECT is permitted. See also the discussion of VALUES as an
operator, in the topic Query in this guide.

SYNTAX

```
VALUES ( expression [, ...] ) [, ...]
    [ ORDER BY sort_expression [ ASC | DESC | USING operator ] [, ...] ]

```

VALUES is a SQL operator, on a par with SELECT and UNION, enabling the following types of
actions:

- You can write VALUES (1), (2) to return two rows each with a single anonymous
  column.
- You can write VALUES (1, 'a'), (2, 'b') to return two rows of two columns.
- You can name the columns using AS, as in the following example:

```
SELECT * FROM (VALUES (1, 'a'), (2, 'b')) AS t(x, y)

```

The most important use of VALUES is in an INSERT statement, to insert a single row:

```
  INSERT INTO emps (empno, name, deptno, gender)
    VALUES (107, 'Jane Costa', 22, 'F');

```

However, you can also insert multiple rows:

```
   INSERT INTO Trades (ticker, price, amount)
     VALUES ('MSFT', 30.5, 1000),
            ('ORCL', 20.25, 2000);

```

When you use VALUES in the FROM clause of a SELECT statement, the entire VALUES clause
must be enclosed in parentheses, consistent with the fact that it operates as a query, not a
table expression. For additional examples, see [FROM clause](sql-reference-from-clause.md "sql-reference-from-clause.md").

###### Note

Using INSERT with streams engages some additional
considerations as to rowtimes, pumps, and INSERT EXPEDITED. For more information, see [INSERT](sql-reference-insert.md "sql-reference-insert.md").
