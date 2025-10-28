# SPARQL standards compliance in Amazon Neptune

After listing applicable SPARQL standards, the following sections provide specific
details about how Neptune's SPARQL implementation extends or diverges from those
standards.

###### Topics

- [Applicable Standards for SPARQL](#feature-sparql-applicable-standards "#feature-sparql-applicable-standards")
- [Default Namespace Prefixes in Neptune SPARQL](#sparql-default-prefixes "#sparql-default-prefixes")
- [SPARQL Default Graph and Named Graphs](#sparql-default-graph "#sparql-default-graph")
- [SPARQL XPath Constructor Functions Supported by Neptune](#access-graph-sparql-xpath-constructors "#access-graph-sparql-xpath-constructors")
- [Default base IRI for queries and updates](#opencypher-compliance-default-iri "#opencypher-compliance-default-iri")
- [xsd:dateTime Values in Neptune](#access-graph-sparql-xsd-date-time "#access-graph-sparql-xsd-date-time")
- [Neptune Handling of Special Floating Point Values](#feature-overview-special-values-comparisons "#feature-overview-special-values-comparisons")
- [Neptune Limitation of Arbitrary-Length Values](#feature-overview-arbitrary-length-values "#feature-overview-arbitrary-length-values")
- [Neptune Extends Equals Comparison in SPARQL](#feature-overview-sparql-not-equal "#feature-overview-sparql-not-equal")
- [Handling of Out-of-Range Literals in Neptune SPARQL](#feature-overview-sparql-out-of-range "#feature-overview-sparql-out-of-range")
  Amazon Neptune complies with the following
  standards in implementing the SPARQL graph query language.

## Applicable Standards for SPARQL

- SPARQL is defined by the W3C [SPARQL 1.1
  Query Language](https://www.w3.org/TR/sparql11-query/ "https://www.w3.org/TR/sparql11-query/") recommendation of March 21, 2013.
- The SPARQL Update protocol and query language are defined by the W3C [SPARQL 1.1 Update](https://www.w3.org/TR/sparql11-update/ "https://www.w3.org/TR/sparql11-update/")
  specification.
- For numeric formats, SPARQL follows the [W3C
  XML Schema Definition Language (XSD) 1.1 Part 2: Datatypes](https://www.w3.org/TR/xmlschema11-2/ "https://www.w3.org/TR/xmlschema11-2/") specification, which
  is consistent with the IEEE 754 specification ([IEEE
  754-2019 - IEEE Standard for Floating-Point Arithmetic](https://standards.ieee.org/content/ieee-standards/en/standard/754-2019.html "https://standards.ieee.org/content/ieee-standards/en/standard/754-2019.html"). For more information,
  see also the [Wikipedia IEEE 754 page](https://en.wikipedia.org/wiki/IEEE_754 "https://en.wikipedia.org/wiki/IEEE_754")). However, features that were
  introduced after the `IEEE 754-1985` version are not included in the
  specification.

## Default Namespace Prefixes in Neptune SPARQL

Neptune defines the following prefixes by default for use in SPARQL queries. For more
information, see [Prefixed
Names](https://www.w3.org/TR/sparql11-query/#prefNames "https://www.w3.org/TR/sparql11-query/#prefNames") in the SPARQL specification.

- `rdf`  – `http://www.w3.org/1999/02/22-rdf-syntax-ns#`
- `rdfs` – `http://www.w3.org/2000/01/rdf-schema#`
- `owl`  – `http://www.w3.org/2002/07/owl#`
- `xsd`  – `http://www.w3.org/2001/XMLSchema#`

## SPARQL Default Graph and Named Graphs

Amazon Neptune associates every triple with a named graph. The default graph is defined
as the union of all named graphs.

###### Default Graph for Queries

If you submit a SPARQL query without explicitly specifying a graph via the
`GRAPH` keyword or constructs such as `FROM NAMED`, Neptune always
considers all triples in your DB instance. For example, the following query returns all
triples from a Neptune SPARQL endpoint:

`SELECT * WHERE { ?s ?p ?o }`

Triples that appear in more than one graph are returned only once.

For information about the default graph specification, see the [RDF Dataset](https://www.w3.org/TR/sparql11-query/#rdfDataset "https://www.w3.org/TR/sparql11-query/#rdfDataset") section of the
SPARQL 1.1 Query Language specification.

###### Specifying the Named Graph for Loading, Inserts, or Updates

If you don't specify a named graph when loading, inserting, or updating triples,
Neptune uses the fallback named graph defined by the URI
`http://aws.amazon.com/neptune/vocab/v01/DefaultNamedGraph`.

When you issue a Neptune `Load` request using a triple-based format, you
can specify the named graph to use for all triples by using the `parserConfiguration:
 namedGraphUri` parameter. For information about the `Load` command syntax,
see [Neptune Loader Command](load-api-reference-load.md "load-api-reference-load.md").

###### Important

If you don't use this parameter, and you don't specify a named graph,
the fallback URI is used:
`http://aws.amazon.com/neptune/vocab/v01/DefaultNamedGraph`.

This fallback named graph is also used if you load triples via `SPARQL
 UPDATE` without explicitly providing a named graph target.

You can use the quads-based format N-Quads to specify a named graph for each triple in
the database.

###### Note

Using N-Quads allows you to leave the named graph blank. In this case,
`http://aws.amazon.com/neptune/vocab/v01/DefaultNamedGraph` is used.

You can override the default named graph for N-Quads using the `namedGraphUri`
parser configuration option.

## SPARQL XPath Constructor Functions Supported by Neptune

The SPARQL standard allows SPARQL engines to support an extensible set of XPath
constructor functions. Neptune currently supports the following constructor functions,
where the `xsd` prefix is defined as `http://www.w3.org/2001/XMLSchema#`:

- `xsd:boolean`
- `xsd:integer`
- `xsd:double`
- `xsd:float`
- `xsd:decimal`
- `xsd:long`
- `xsd:unsignedLong`

## Default base IRI for queries and updates

Because a Neptune cluster has several different endpoints, using the request
URL of a query or update as the base IRI could lead to unexpected results when
resolving relative IRIs.

As of [engine release 1.2.1.0](engine-releases-1.2.1.md "engine-releases-1.2.1.md"),
Neptune uses `http://aws.amazon.com/neptune/default/` as the base
IRI if an explicit base IRI is not part of the request.

In the following request, the base IRI is part of the request:

```
BASE <http://example.org/default/>
INSERT DATA { <node1> <id> "n1" }

BASE <http://example.org/default/>
SELECT * { <node1> ?p ?o }
```

And the result would be:

```
?p                                                   ?o
http://example.org/default/id                        n1
```

In this request, however, no base IRI is included:

```
INSERT DATA { <node1> <id> "n1" }

SELECT * { <node1> ?p ?o }
```

In that case, the result would be:

```
?p                                                   ?o
http://aws.amazon.com/neptune/default/id             n1
```

## xsd:dateTime Values in Neptune

For performance reasons, Neptune always stores date/time values as
Coordinated Universal Time (UTC). This makes direct comparisons very efficient.

This also means that if you enter a `dateTime` value
that specifies a particular time zone, Neptune translates the value to UTC and
discards that time-zone information. Then, when you retrieve the `dateTime`
value later, it is expressed in UTC, not the time of the original time zone,
and you can no longer tell what that original time zone was.

## Neptune Handling of Special Floating Point Values

Neptune handles special floating-point values in SPARQL as follows.

### SPARQL NaN Handling in Neptune

In Neptune, SPARQL can accept a value of `NaN` in a query. No distinction
is made between signaling and quiet `NaN` values. Neptune treats all
`NaN` values as quiet.

Semantically, no comparison of a `NaN` is possible, because nothing is
greater than, less than, or equal to a `NaN`. This means that a value
of `NaN` on one side of a comparison in theory never matches _anything_
on the other side.

However, the [XSD
specification](https://www.w3.org/TR/xmlschema-2/#double "https://www.w3.org/TR/xmlschema-2/#double") does treat two `xsd:double` or
`xsd:float` `NaN` values as equal. Neptune follows this
for the `IN` filter, for the equal operator in filter expressions,
and for exact match semantics (having a `NaN` in the object
position of a triple pattern).

### SPARQL Infinite Value Handling in Neptune

In Neptune, SPARQL can accept a value of `INF` or `-INF`
in a query. `INF` compares as greater than any other numeric value, and
`-INF` compares as less than any other numeric value.

Two INF values with matching signs compare as equal to each other regardless of
their type (for example, a float `-INF` compares as equal to a double
`-INF`).

Of course, no comparison with a `NaN` is possible because nothing is greater
than, less than, or equal to a `NaN`.

### SPARQL Negative Zero Handling in Neptune

Neptune normalizes a negative zero value to an unsigned zero. You can use negative
zero values in a query, but they aren't recorded as such in the database, and they compare
as equal to unsigned zeros.

## Neptune Limitation of Arbitrary-Length Values

Neptune limits the storage size of XSD integer, floating point, and decimal values in
SPARQL to 64 bits. Using larger values results in an `InvalidNumericDataException`
error.

## Neptune Extends Equals Comparison in SPARQL

The SPARQL standard defines a ternary logic for value expressions, where a value
expression can either evaluate to `true`, `false`, or
`error`. The default semantics for term equality as defined in the [SPARQL 1.1
specification](https://www.w3.org/TR/sparql11-query/#func-RDFterm-equal "https://www.w3.org/TR/sparql11-query/#func-RDFterm-equal")), which applies to `=` and `!=` comparisons in
`FILTER` conditions, produces an `error` when comparing data types
that are not explicitly comparable in the [operators table](https://www.w3.org/TR/sparql11-query/#OperatorMapping "https://www.w3.org/TR/sparql11-query/#OperatorMapping") in the
specification.

This behavior can lead to unintuitive results, as in the following example.

Data:

```
<http://example.com/Server/1> <http://example.com/ip> "127.0.0.1"^^<http://example.com/datatype/IPAddress>
```

Query 1:

```
SELECT * WHERE {
    <http://example.com/Server/1> <http://example.com/ip> ?o .
    FILTER(?o = "127.0.0.2"^^<http://example.com/datatype/IPAddress>)
}
```

Query 2:

```
SELECT * WHERE {
    <http://example.com/Server/1> <http://example.com/ip> ?o .
    FILTER(?o != "127.0.0.2"^^<http://example.com/datatype/IPAddress>)
}
```

With the default SPARQL semantics that Neptune used before release 1.0.2.1, both queries
would return the empty result. The reason is that `?o =
 "127.0.0.2"^^<http://example.com/IPAddress>` when evaluated for `?o :=
 "127.0.0.1"^^<http://example.com/IPAddress>` produces an `error`
rather than `false` because there are no explicit comparison rules specified for
the custom data type `<http://example.com/IPAddress>`. As a result, the
negated version in the second query also produces an `error`. In both queries, the
`error` causes the candidate solution to be filtered out.

Starting with release 1.0.2.1, Neptune has extended the SPARQL inequality operator in
accord with the specification. See the [SPARQL 1.1 section on
operator extensibility](https://www.w3.org/TR/sparql11-query/#operatorExtensibility "https://www.w3.org/TR/sparql11-query/#operatorExtensibility"), which allows engines to define additional rules on how to
compare across user-defined and non-comparable built-in data types.

Using this option, Neptune now treats a comparison of any two data types that is not
explicitly defined in the operator-mapping table as evaluating to `true` if the
literal values and data types are syntactically equal, and false otherwise. An
`error` is not produced in any case.

Using these new semantics, the second query would return
`"127.0.0.1"^^<http://example.com/IPAddress>` instead of an empty
result.

## Handling of Out-of-Range Literals in Neptune SPARQL

XSD semantics define each numeric type with its value space, except for `integer`
and `decimal`. These definitions limit each type to a range of values.
For example, the range of an `xsd:byte` range is from -128 to +127, inclusive.
Any value outside of this range is considered invalid.

If you try to assign a literal value outside of the value space of a type (for example, if
you try to set an `xsd:byte` to a literal value of 999), Neptune accepts the
out-of-range value as-is, without rounding or truncating it. But it doesn't persist it as a
numeric value because the given type can't represent it.

That is, Neptune accepts `"999"^^xsd:byte` even though it is a value outside
of the defined `xsd:byte` value range. However, after the value is persisted in the
database, it can only be used in exact match semantics, in an object position of a triple
pattern. No range filter can be executed on it because out-of-range literals are not treated
as numeric values.

The SPARQL 1.1 specification defines [range operators](https://www.w3.org/TR/sparql11-query/#OperatorMapping "https://www.w3.org/TR/sparql11-query/#OperatorMapping") in the
form `numeric`_-operator-_`numeric`,
`string`_-operator-_`string`,
`literal`_-operator-_`literal`, and so forth.
Neptune can't execute a range comparison operator anything like
`invalid-literal`_-operator-_`numeric-value`.
