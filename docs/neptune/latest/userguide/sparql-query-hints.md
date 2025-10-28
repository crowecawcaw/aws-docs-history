# SPARQL query hints

You can use query hints to specify optimization and evaluation strategies for a particular
SPARQL query in Amazon Neptune.

Query hints are expressed using additional triple patterns that are embedded in the SPARQL
query with the following parts:

```
`scope` `hint` `value`
```

- *scope* – Determines the part of the
  query that the query hint applies to, such as a certain group in the query or the full
  query.
- *hint* – Identifies the type of the
  hint to apply.
- *value* – Determines the behavior of
  the system aspect under consideration.
  The query hints and scopes are exposed as predefined terms in the Amazon Neptune
  namespace `http://aws.amazon.com/neptune/vocab/v01/QueryHints#`. The examples in this
  section include the namespace as a `hint` prefix that is defined and
  included in the query:

```
PREFIX hint: <http://aws.amazon.com/neptune/vocab/v01/QueryHints#>
```

For example, the following shows how to include a `joinOrder` hint in a
`SELECT` query:

```
PREFIX hint: <http://aws.amazon.com/neptune/vocab/v01/QueryHints#>
SELECT `...` {
 hint:Query hint:joinOrder "Ordered" .
 `...`
}
```

The preceding query instructs the Neptune engine to evaluate joins in the query in the
_given_ order and disables any automatic reordering.

Consider the following when using query hints:

- You can combine different query hints in a single query. For example, you can use the
  `bottomUp` query hint to annotate a subquery for bottom-up evaluation and a
  `joinOrder` query hint to fix the join order inside the subquery.
- You can use the same query hint multiple times, in different non-overlapping
  scopes.
- Query hints are hints. Although the query engine generally aims to consider given query
  hints, it might also ignore them.
- Query hints are semantics preserving. Adding a query hint does not change the output of
  the query (except for the potential result order when no ordering guarantees are
  given—that is, when the result order is not explicitly enforced by using ORDER BY).
  The following sections provide more information about the available query hints and their
  usage in Neptune.

###### Topics

- [Scope of SPARQL query hints in Neptune](#sparql-query-hints-scope "#sparql-query-hints-scope")
- [The joinOrder SPARQL query hint](sparql-query-hints-joinOrder.md "sparql-query-hints-joinOrder.md")
- [The evaluationStrategy SPARQL query hint](sparql-query-hints-evaluationStrategy.md "sparql-query-hints-evaluationStrategy.md")
- [The queryTimeout SPARQL query hint](sparql-query-hints-queryTimeout.md "sparql-query-hints-queryTimeout.md")
- [The rangeSafe SPARQL query hint](sparql-query-hints-rangeSafe.md "sparql-query-hints-rangeSafe.md")
- [The queryId SPARQL Query Hint](sparql-query-hints-queryId.md "sparql-query-hints-queryId.md")
- [The useDFE SPARQL query hint](sparql-query-hints-useDFE.md "sparql-query-hints-useDFE.md")
- [SPARQL query hints used with DESCRIBE](sparql-query-hints-for-describe.md "sparql-query-hints-for-describe.md")

## Scope of SPARQL query hints in Neptune

The following table shows the available scopes, associated hints, and descriptions for
SPARQL query hints in Amazon Neptune. The `hint` prefix in these entries represents
the Neptune namespace for hints:

```
PREFIX hint: <http://aws.amazon.com/neptune/vocab/v01/QueryHints#>
```

| Scope           | Supported Hint                                                                                            | Description                                                                                                                                                         |
| --------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `hint:Query`    | [joinOrder](sparql-query-hints-joinOrder.md "sparql-query-hints-joinOrder.md")                            | The query hint applies to the whole query.                                                                                                                          |
| `hint:Query`    | [queryTimeout](sparql-query-hints-queryTimeout.md "sparql-query-hints-queryTimeout.md")                   | The time-out value applies to the entire query.                                                                                                                     |
| `hint:Query`    | [rangeSafe](sparql-query-hints-rangeSafe.md "sparql-query-hints-rangeSafe.md")                            | Type promotion is disabled for the entire query.                                                                                                                    |
| `hint:Query`    | [queryId](sparql-query-hints-queryId.md "sparql-query-hints-queryId.md")                                  | The query ID value applies to the entire query.                                                                                                                     |
| `hint:Query`    | [useDFE](sparql-query-hints-useDFE.md "sparql-query-hints-useDFE.md")                                     | Use of the DFE is enabled (or disabled) for the entire query.                                                                                                       |
| `hint:Group`    | [joinOrder](sparql-query-hints-joinOrder.md "sparql-query-hints-joinOrder.md")                            | The query hint applies to the top-level elements in the specified group, but not to nested elements (such as subqueries) or parent elements.                        |
| `hint:SubQuery` | [evaluationStrategy](sparql-query-hints-evaluationStrategy.md "sparql-query-hints-evaluationStrategy.md") | The hint is specified and applied to a nested SELECT subquery. The subquery is evaluated independently, without considering solutions computed before the subquery. |
