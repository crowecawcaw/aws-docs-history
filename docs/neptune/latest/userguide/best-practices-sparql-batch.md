# Choosing Between FILTER, FILTER...IN, and VALUES in Your Queries

There are three basic ways to inject values in SPARQL queries:   `FILTER`,
  `FILTER...IN`,   and   `VALUES`.

For example, suppose that you want to look up the friends of multiple people within a
single query. Using `FILTER`, you might structure your query as follows:

```
  PREFIX ex: <https://www.example.com/>
  PREFIX foaf : <http://xmlns.com/foaf/0.1/>

  SELECT ?s ?o
  WHERE {?s foaf:knows ?o. FILTER (?s = ex:person1 || ?s = ex:person2)}
```

This returns all the triples in the graph that have `?s` bound to
`ex:person1` or `ex:person2` and have an outgoing edge labeled
`foaf:knows`.

You can also create a query using `FILTER...IN` that returns
equivalent results:

```
  PREFIX ex: <https://www.example.com/>
  PREFIX foaf : <http://xmlns.com/foaf/0.1/>

  SELECT ?s ?o
  WHERE {?s foaf:knows ?o. FILTER (?s IN (ex:person1, ex:person2))}
```

You can also create a query using `VALUES` that in this case also returns
equivalent results:

```
  PREFIX ex: <https://www.example.com/>
  PREFIX foaf : <http://xmlns.com/foaf/0.1/>

  SELECT ?s ?o
  WHERE {?s foaf:knows ?o. VALUES ?s {ex:person1 ex:person2}}
```

Although in many cases these queries are semantically equivalent, there are some cases
where the two `FILTER` variants differ from the `VALUES` variant:

- The first case is when you inject duplicate values, such as injecting the same person
  twice. In that case, the `VALUES` query includes the duplicates in your result.
  You can explicitly eliminate such duplicates by adding a `DISTINCT` to the
  `SELECT` clause. But there might be situations where you actually want
  duplicates in the query results for redundant value injection.

However, the `FILTER` and `FILTER...IN` versions extract the
value only once when the same value appears multiple times.

- The second case is related to the fact that `VALUES` always performs an
  exact match, whereas `FILTER` might apply type promotion and do fuzzy matching
  in some cases.

For instance, when you include a literal such as `"2.0"^^xsd:float` in your
values clause, a `VALUES` query exactly matches this literal, including literal
value and data type.

By contrast, `FILTER` produces a fuzzy match for these numeric literals.
The matches could include literals with the same value but different numeric data types,
such as `xsd:double`.

###### Note

There is no difference between the `FILTER` and
`VALUES` behavior when enumerating string literals or URIs.
The differences between `FILTER` and `VALUES` can affect
optimization and the resulting query evaluation strategy. Unless your use case requires fuzzy
matching, we recommend using `VALUES` because it avoids looking at special cases
related to type casting. As a result, `VALUES` often produces a more efficient
query that runs faster and is less expensive.
