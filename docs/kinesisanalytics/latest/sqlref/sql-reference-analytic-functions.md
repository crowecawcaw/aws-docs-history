# Analytic Functions

An analytic function is one that returns a result calculated from data in (or about) a
finite set of rows identified by a [SELECT clause](sql-reference-select-clause.md "sql-reference-select-clause.md") or in the [ORDER BY clause](sql-reference-order-by-clause.md "sql-reference-order-by-clause.md").

The SELECT topic
explains the order-by clause, showing the order-by chart, as well as the windowing clause (and
window-specification chart). To see where an order-by clause is used in Select statements, see
the Select chart in the SELECT topic of this guide.

1. Analytic functions must specify a window. Since there are a few restrictions on window
   specifications, and a few differences between specifying windows for windowed aggregation
   and windowed join, please see [Allowed and Disallowed Window Specifications](sql-reference-allowed-disallowed-window.md "sql-reference-allowed-disallowed-window.md") for explanations.
2. Analytic functions may only appear in the <selection list> portion of a SELECT
   clause or in the ORDER BY clause.
   Other differences are described in the table later in this topic.

Performing queries using analytic functions is commonly referred to as windowed aggregation
(discussed below), as distinct from [Aggregate Functions](sql-reference-aggregate-functions.md "sql-reference-aggregate-functions.md").

Because of the presence of the window specification, queries that use analytic functions
produce results in a different manner than do aggregate queries. For each row in the input set,
the window specification identifies a different set of rows on which the analytic function
operates. If the window specification also includes a PARTITION BY clause, then the only rows in
the window that will be considered in producing a result will be those that share the same
partition as the input row.

If an input row contains a null in a column used as an input to an analytic function, the
analytic function ignores the row, except for COUNT, which does count rows with null values. In
cases where the window (or in the case of a PARTITION BY, a partition within the window)
contains no rows, an analytic function will return null. The exception to this is COUNT, which
returns zero.

| Differences Between Aggregate and Analytic Functions                                               | Function Type                           | Outputs                                                                       | Rows or Windows Used                                                                                                                                                                                                                      | Notes                                                                                                                                                                                                                                                                                                                     |
| -------------------------------------------------------------------------------------------------- | --------------------------------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Aggregate Functions](sql-reference-aggregate-functions.md "sql-reference-aggregate-functions.md") | One output row per group of input rows. | All output columns are calculated over the same window or same group of rows. | COUNT DISTINCT is not allowed in [Aggregate Functions](sql-reference-aggregate-functions.md "sql-reference-aggregate-functions.md"). Statements of the following type are not allowed: SELECT COUNT(DISTINCT x) ... FROM ... GROUP BY ... |
| Analytic Functions                                                                                 | One output row for each input row.      | Each output column may be calculated using a different window or partition.   | COUNT DISTINCT can't be used as analytic functions or in windowed aggregation.                                                                                                                                                            | ## Related Topics <br>• [Windowed Aggregation on Streams](sql-reference-windowed-aggregation-stream.md "sql-reference-windowed-aggregation-stream.md") <br>• [SELECT statement](sql-reference-select.md "sql-reference-select.md") <br>• [SELECT clause](sql-reference-select-clause.md "sql-reference-select-clause.md") |
