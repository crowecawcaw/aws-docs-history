# openCypher query hints

###### Important

openCypher query hint is only available from engine release
[1.3.2.0](engine-releases-1.3.2.md "engine-releases-1.3.2.md") and later.

In Amazon Neptune, you can use the `USING` clause to specify query hints for openCypher queries. These hints
allow you to control optimization and evaluation strategies.

The syntax for query hints is:

```
USING {scope}:{hint} {value}
```

1. `{scope}` defines the scope in which the hint applies to: `Query` or `Clause`.

A scope value of `Query` means that the query hint applies to the whole query (query-level).

A scope value of `Clause` means that the query hint applies to the clause the hint precedes
(clause-level). 2. `{hint}` is the name of the query hint being applied. 3. `{value}` is the argument for the `{hint}`.

The values can be case-insensitive.

For example, to enable the query plan cache for a query:

```
Using QUERY:PLANCACHE "enabled"
MATCH (a:Person {firstName: "Erin", lastName: $lastName})
 RETURN a
```

###### Note

Currently, the **Query** scope query hints **PLANCACHE**,
**TIMEOUTMILLISECONDS**, and **assumeConsistentDataTypes**
are supported. Supported query hints are listed below.

###### Topics

- [openCypher query plan cache hint](opencypher-query-hints-qpc-hint.md "opencypher-query-hints-qpc-hint.md")
- [AssumeConsistentDataTypes hint](opencypher-query-hints-AssumeConsistentDataTypes.md "opencypher-query-hints-AssumeConsistentDataTypes.md")
- [openCypher query timeout hint](opencypher-query-hints-timeout-hint.md "opencypher-query-hints-timeout-hint.md")
