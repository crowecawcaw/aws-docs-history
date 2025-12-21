# Set operators

The _set operators_ are used to compare and merge the results of two
separate query expressions.

AWS Clean Rooms Spark SQL supports the following set operators listed in the following table.

| Set operator  |
| ------------- |
| INTERSECT     |
| INTERSECT ALL |
| EXCEPT        |
| EXCEPT ALL    |
| UNION         |
| UNION ALL     |

For example, if you want to know which users of a website are both buyers and sellers but
their user names are stored in separate columns or tables, you can find the
_intersection_ of these two types of users. If you want to know which website
users are buyers but not sellers, you can use the EXCEPT operator to find the
_difference_ between the two lists of users. If you want to build a list of
all users, regardless of role, you can use the UNION operator.

###### Note

The ORDER BY, LIMIT, SELECT TOP, and OFFSET clauses can't be used in the query expressions
merged by the UNION, UNION ALL, INTERSECT, and EXCEPT set operators.

###### Topics

- [Syntax](#UNION-synopsis "#UNION-synopsis")
- [Parameters](#UNION-parameters "#UNION-parameters")
- [Order of evaluation for set
  operators](#UNION-order-of-evaluation-for-set-operators "#UNION-order-of-evaluation-for-set-operators")
- [Usage notes](#UNION-usage-notes "#UNION-usage-notes")
- [Example UNION queries](example_union_query.md "example_union_query.md")
- [Example UNION ALL query](example_unionall_query.md "example_unionall_query.md")
- [Example INTERSECT queries](example_intersect_query.md "example_intersect_query.md")
- [Example EXCEPT query](Example_EXCEPT_query.md "Example_EXCEPT_query.md")

## Syntax

```
*subquery1*
{ { UNION [ ALL | DISTINCT ] |
              INTERSECT [ ALL | DISTINCT ] |
              EXCEPT [ ALL | DISTINCT ] } subquery2 } [...] }
```

## Parameters

_subquery1, subquery2_

A query expression that corresponds, in the form of its select list, to a second query
expression that follows the UNION, UNION ALL, INTERSECT, INTERSECT ALL, EXCEPT, or EXCEPT ALL
operator. The two expressions must contain the same number of output columns with compatible
data types; otherwise, the two result sets can't be compared and merged. Set operations
don't allow implicit conversion between different categories of data types. For more
information, see [Type compatibility and conversion](s_Type_conversion.md "s_Type_conversion.md").

You can build queries that contain an unlimited number of query expressions and link
them with UNION, INTERSECT, and EXCEPT operators in any combination. For example, the
following query structure is valid, assuming that the tables T1, T2, and T3 contain
compatible sets of columns:

```
select * from t1
union
select * from t2
except
select * from t3
```

UNION [ALL | DISTINCT]

Set operation that returns rows from two query expressions, regardless of whether the
rows derive from one or both expressions.

INTERSECT [ALL | DISTINCT]

Set operation that returns rows that derive from two query expressions. Rows that
aren't returned by both expressions are discarded.

EXCEPT [ALL | DISTINCT]

Set operation that returns rows that derive from one of two query expressions. To
qualify for the result, rows must exist in the first result table but not the second.

EXCEPT ALL doesn't remove duplicates from the result rows.

MINUS and EXCEPT are exact synonyms.

## Order of evaluation for set

operators

The UNION and EXCEPT set operators are left-associative. If parentheses aren't
specified to influence the order of precedence, a combination of these set operators is
evaluated from left to right. For example, in the following query, the UNION of T1 and T2 is
evaluated first, then the EXCEPT operation is performed on the UNION result:

```
select * from t1
union
select * from t2
except
select * from t3
```

The INTERSECT operator takes precedence over the UNION and EXCEPT operators when a
combination of operators is used in the same query. For example, the following query evaluates
the intersection of T2 and T3, then union the result with T1:

```
select * from t1
union
select * from t2
intersect
select * from t3
```

By adding parentheses, you can enforce a different order of evaluation. In the following
case, the result of the union of T1 and T2 is intersected with T3, and the query is likely to
produce a different result.

```
(select * from t1
union
select * from t2)
intersect
(select * from t3)
```

## Usage notes

- The column names returned in the result of a set operation query are the column names (or
  aliases) from the tables in the first query expression. Because these column names are
  potentially misleading, in that the values in the column derive from tables on either side of
  the set operator, you might want to provide meaningful aliases for the result set.
- When set operator queries return decimal results, the corresponding result columns are
  promoted to return the same precision and scale. For example, in the following query, where
  T1.REVENUE is a DECIMAL(10,2) column and T2.REVENUE is a DECIMAL(8,4) column, the decimal
  result is promoted to DECIMAL(12,4):

```
select t1.revenue union select t2.revenue;
```

The scale is `4` because that is the maximum scale of the two columns. The
precision is `12` because T1.REVENUE requires 8 digits to the left of the decimal
point (12 - 4 = 8). This type promotion ensures that all values from both sides of the UNION
fit in the result. For 64-bit values, the maximum result precision is 19 and the maximum
result scale is 18. For 128-bit values, the maximum result precision is 38 and the maximum
result scale is 37.

If the resulting data type exceeds AWS Clean Rooms precision and scale limits, the query returns an
error.

- For set operations, two rows are treated as identical if, for each corresponding pair of
  columns, the two data values are either _equal_ or _both
  NULL_. For example, if tables T1 and T2 both contain one column and one row, and
  that row is NULL in both tables, an INTERSECT operation over those tables returns that
  row.
