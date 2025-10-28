# The `queryTimeout` SPARQL query hint

The `queryTimeout` query hint specifies a timeout that is shorter than
the `neptune_query_timeout` value set in the DB parameters group.

If the query terminates as a result of this hint, a `TimeLimitExceededException`
is thrown, with an `Operation terminated (deadline exceeded)` message.

## `queryTimeout` SPARQL hint syntax

```
PREFIX hint: <http://aws.amazon.com/neptune/vocab/v01/QueryHints#>
SELECT ... WHERE {
    hint:Query hint:queryTimeout 10 .
    # OR
    hint:Query hint:queryTimeout "10" .
    # OR
    hint:Query hint:queryTimeout "10"^^xsd:integer .
 ...
}
```

The time-out value is expressed in milliseconds.

The time-out value must be smaller than the `neptune_query_timeout`
value set in the DB parameters group. Otherwise, a `MalformedQueryException`
exception is thrown with a `Malformed query: Query hint 'queryTimeout' must be less than
 neptune_query_timeout DB Parameter Group` message.

The `queryTimeout` query hint should be specified in the `WHERE`
clause of the main query, or in the `WHERE` clause of one of the subqueries
as shown in the example below.

It must be set only once across all the queries/subqueries and SPARQL Updates
sections (such as INSERT and DELETE). Otherwise, a `MalformedQueryException`
exception is thrown with a `Malformed query: Query hint 'queryTimeout' must be set
 only once` message.

###### Available Scopes

The `queryTimeout` hint can be applied both to SPARQL queries and updates.

- In a SPARQL query, it can appear in the WHERE clause of the main query or a
  subquery.
- In a SPARQL update, it can be set in the INSERT, DELETE, or WHERE clause.
  If there are multiple update clauses, it can only be set in one of them.

For more information about query hint scopes, see [Scope of SPARQL query hints in Neptune](sparql-query-hints.md#sparql-query-hints-scope "sparql-query-hints.md#sparql-query-hints-scope").

## `queryTimeout` SPARQL hint example

Here is an example of using `hint:queryTimeout` in the main `WHERE`
clause of an `UPDATE` query:

```

PREFIX hint: <http://aws.amazon.com/neptune/vocab/v01/QueryHints#>
INSERT {
    ?s ?p ?o
} WHERE {
    hint:Query hint:queryTimeout 100 .
    ?s ?p ?o .
}
```

Here, the `hint:queryTimeout` is in the `WHERE`
clause of a subquery:

```
PREFIX hint: <http://aws.amazon.com/neptune/vocab/v01/QueryHints#>
SELECT * {
   ?s ?p ?o .
   {
      SELECT ?s WHERE {
         hint:Query hint:queryTimeout 100 .
         ?s ?p1 ?o1 .
      }
   }
}
```
