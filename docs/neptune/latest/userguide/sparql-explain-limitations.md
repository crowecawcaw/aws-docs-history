# Limitations of SPARQL `explain` in Neptune

The release of the Neptune SPARQL `explain` feature has the
following limitations.

###### Neptune Currently Supports Explain Only in SPARQL SELECT Queries

For information about the evaluation process for other query forms, such as
`ASK`, `CONSTRUCT`, `DESCRIBE`, and `SPARQL
 UPDATE` queries, you can transform these queries into a SELECT query. Then use
`explain` to inspect the corresponding SELECT query instead.

For example, to obtain `explain` information about an
`ASK WHERE {...}` query, run the corresponding
`SELECT WHERE {...} LIMIT 1` query with `explain`.

Similarly, for a `CONSTRUCT {...} WHERE {...}` query, drop the
`CONSTRUCT {...}` part and run a `SELECT` query with
`explain` on the second `WHERE {...}` clause. Evaluating
the second `WHERE` clause generally reveals the main challenges of
processing the `CONSTRUCT` query, because solutions flowing out of
the second `WHERE` into the `CONSTRUCT` template generally
only require straightforward substitution.

###### Explain Operators May Change in Future Releases

The SPARQL `explain` operators and their parameters may change
in future releases.

###### Explain Output May Change in Future Releases

For example, column headers could change, and more columns might
be added to the tables.
