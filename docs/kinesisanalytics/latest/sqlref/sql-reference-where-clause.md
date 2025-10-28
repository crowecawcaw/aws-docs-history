# WHERE clause

The WHERE clause extracts records that meet a specified condition. The condition can be a
numeric or string comparison, or use the BETWEEN, LIKE, OR IN operators: see [Streaming SQL Operators](sql-reference-streaming-operators.md "sql-reference-streaming-operators.md"). Conditions
can be combined using logical operators such as AND, OR, and NOT.

The WHERE clause is like the [HAVING clause](sql-reference-having-clause.md "sql-reference-having-clause.md") clause. It applies to groups, that is, results
from a WHERE clause are individual original rows, whereas results from a HAVING clause
represent groupings or aggregations of original rows.

WHERE and HAVING can both appear in a single SELECT statement. The WHERE selects from the
stream or table those individual rows that satisfy its condition (the WHERE-condition). The
GROUP BY criteria apply only to the rows selected by the WHERE condition. Such a grouping,
for example "GROUP BY CustomerID", can be further qualified by a HAVING-condition, which
then selects aggregations of rows satisfying its condition within the specified grouping.
For example, "GROUP BY ClientID HAVING SUM(ShipmentValue) > 3600" would select only those
clients whose various shipments that fit the WHERE criteria also had values that added up to
exceed 3600.

##

To see where this clause fits into the SELECT statement, see [SELECT statement](sql-reference-select.md "sql-reference-select.md").

The condition must be a Boolean predicate expression. The query returns only rows for
which the predicate evaluates to TRUE; if the condition evaluates to NULL, the row is not
emitted.

The condition in the WHERE clause cannot contain windowed aggregation expressions, because
if the where clause condition caused rows to be dropped, it would alter the contents of the
window.

WHERE is also discussed in the topics [JOIN clause](sql-reference-join-clause.md "sql-reference-join-clause.md") and [HAVING clause](sql-reference-having-clause.md "sql-reference-having-clause.md") in
this guide.
