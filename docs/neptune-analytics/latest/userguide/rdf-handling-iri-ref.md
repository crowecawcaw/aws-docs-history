# Referencing IRIs in queries

There are two ways to reference an IRI in an openCypher query:

- Wrap the full IRI inside `<` and `>` . Depending on where in the query this IRI
  is referenced, the IRI is then provided as a String, such as `"<http://example.com/Alice>"`
  (when the IRI is the value of property `~id`), or in backticks such as
  `<http://example.com/Alice>` (when the IRI is a label, or property key).

```
CREATE (:`<http://xmlns.com/foaf/0.1/Person>` {`~id`: "<http://example.com/Alice>"})
```

- Define a PREFIX at the start of the query, and inside the query reference an IRI using
  `prefix::suffix`. For example, after `PREFIX ex: <http://example.com/>`
  the reference `ex::Alice` also references the full IRI `<http://example.com/Alice>`.

```
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX ex: <http://example.com/>
CREATE (: foaf::Person {`~id`: ex::Alice})
```

Additional query examples below show the use of both full IRIs and the prefix syntax.
