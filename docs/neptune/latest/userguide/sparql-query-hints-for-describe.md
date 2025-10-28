# SPARQL query hints used with DESCRIBE

A SPARQL `DESCRIBE` query provides a flexible mechanism for requesting
resource descriptions. However, the SPARQL specifications do not define the precise
semantics of `DESCRIBE`.

Starting with [engine release 1.2.0.2](engine-releases-1.2.0.md "engine-releases-1.2.0.md"),
Neptune supports several different `DESCRIBE` modes and algorithms that
are suited to different situations.

This sample dataset can help illustrate the different modes:

```
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix : <https://example.com/> .

:JaneDoe :firstName "Jane" .
:JaneDoe :knows :JohnDoe .
:JohnDoe :firstName "John" .
:JaneDoe :knows _:b1 .
_:b1 :knows :RichardRoe .

:RichardRoe :knows :JaneDoe .
:RichardRoe :firstName "Richard" .

_:s1 rdf:type rdf:Statement .
_:s1 rdf:subject :JaneDoe .
_:s1 rdf:predicate :knows .
_:s1 rdf:object :JohnDoe .
_:s1 :knowsFrom "Berlin" .

:ref_s2 rdf:type rdf:Statement .
:ref_s2 rdf:subject :JaneDoe .
:ref_s2 rdf:predicate :knows .
:ref_s2 rdf:object :JohnDoe .
:ref_s2 :knowsSince 1988 .
```

The examples below assume that a description of the resource `:JaneDoe`
is being requested using a SPARQL query like this:

```
DESCRIBE <https://example.com/JaneDoe>
```

## The `describeMode` SPARQL query hint

The `hint:describeMode` SPARQL query hint is used to select one of the
following SPARQL `DESCRIBE` modes supported by Neptune:

### The `ForwardOneStep` DESCRIBE mode

You invoke the `ForwardOneStep` mode with the `describeMode`
query hint like this:

```
PREFIX hint: <http://aws.amazon.com/neptune/vocab/v01/QueryHints#>
DESCRIBE <https://example.com/JaneDoe>
{
  hint:Query hint:describeMode "ForwardOneStep"
}
```

The `ForwardOneStep` mode only returns the attributes and forward
links of the resource to be described. In the example case, this means it returns the
triples that have `:JaneDoe`, the resource to be described, as subject:

```
:JaneDoe :firstName "Jane" .
:JaneDoe :knows :JohnDoe .
:JaneDoe :knows _:b301990159 .
```

Note that the DESCRIBE query may return triples with blank nodes, such as
`_:b301990159`, which have different IDs each time, compared to the
input dataset.

### The `SymmetricOneStep` DESCRIBE mode

`SymmetricOneStep` is the default DESCRIBE mode if you don't provide a
query hint. You can also invoke it explicitly with the `describeMode` query
hint like this:

```
PREFIX hint: <http://aws.amazon.com/neptune/vocab/v01/QueryHints#>
DESCRIBE <https://example.com/JaneDoe>
{
  hint:Query hint:describeMode "SymmetricOneStep"
}
```

Under `SymmetricOneStep` semantics, `DESCRIBE` returns the
attributes, forward links, and reverse links of the resource to be described:

```
:JaneDoe :firstName "Jane" .
:JaneDoe :knows :JohnDoe .
:JaneDoe :knows _:b318767375 .

_:b318767631 rdf:subject :JaneDoe .

:RichardRoe :knows :JaneDoe .

:ref_s2 rdf:subject :JaneDoe .
```

### The Concise Bounded Description (`CBD`) DESCRIBE mode

The Concise Bounded Description (`CBD`) mode is invoked using the
`describeMode` query hint like this:

```
PREFIX hint: <http://aws.amazon.com/neptune/vocab/v01/QueryHints#>
DESCRIBE <https://example.com/JaneDoe>
{
  hint:Query hint:describeMode "CBD"
}
```

Under `CBD` semantics, `DESCRIBE` returns the
Concise Bounded Description (as [defined
by W3C](http://www.w3.org/Submission/CBD "http://www.w3.org/Submission/CBD")) of the resource to be described:

```
:JaneDoe :firstName "Jane" .
:JaneDoe :knows :JohnDoe .
:JaneDoe :knows _:b285212943 .
_:b285212943 :knows :RichardRoe .

_:b285213199 rdf:subject :JaneDoe .
_:b285213199 rdf:type rdf:Statement .
_:b285213199 rdf:predicate :knows .
_:b285213199 rdf:object :JohnDoe .
_:b285213199 :knowsFrom "Berlin" .

:ref_s2 rdf:subject :JaneDoe .
```

The Concise Bounded Description of an RDF resource (that is, a node in an
RDF graph) is the smallest subgraph centered around that node that can stand
alone. In practice this means that if you think of this graph as a tree,
with the designated node as the root, there are no blank nodes (bnodes)
as leaves of that tree. Since bnodes can't be addressed externally or
used in subsequent queries, it's not enough for browsing the graph
just to find the next single hop(s) from the current node. You also
have to go far enough to find something that can be used in subsequent
queries (that is, something other than a bnode).

#### Computing the CBD

Given a particular node (the starting node or root) in the source
RDF graph, the CBD of that node is computed as follows:

1. Include in the subgraph all statements in the source graph where the
   _subject_ of the statement is the starting node.
2. Recursively, for all statements in the subgraph thus far that
   have a blank node _object_, include in the subgraph all statements in the
   source graph where the _subject_ of the statement is that blank node, and
   which are not already included in the subgraph.
3. Recursively, for all statements included in the subgraph
   thus far, for all reifications of these statements in the source graph,
   include the CBD beginning from the `rdf:Statement` node of
   each reification.

This results in a subgraph where the _object_ nodes are either IRI
references or literals, or blank nodes not serving as the _subject_ of
any statement in the graph. Note that the CBD cannot be computed using
a single SPARQL SELECT or CONSTRUCT query.

### The Symmetric Concise Bounded Description (`SCBD`) DESCRIBE mode

The Symmetric Concise Bounded Description (`SCBD`) mode is invoked
using the `describeMode` query hint like this:

```
PREFIX hint: <http://aws.amazon.com/neptune/vocab/v01/QueryHints#>
DESCRIBE <https://example.com/JaneDoe>
{
  hint:Query hint:describeMode "SCBD"
}
```

Under `SCBD` semantics, `DESCRIBE` returns the
Symmetric Concise Bounded Description of the resource (as defined by W3C in [Describing Linked Datasets with the VoID
Vocabulary](http://www.w3.org/TR/void/ "http://www.w3.org/TR/void/"):

```
:JaneDoe :firstName "Jane" .
:JaneDoe :knows :JohnDoe .
:JaneDoe :knows _:b335544591 .
_:b335544591 :knows :RichardRoe .

:RichardRoe :knows :JaneDoe .

_:b335544847 rdf:subject :JaneDoe .
_:b335544847 rdf:type rdf:Statement .
_:b335544847 rdf:predicate :knows .
_:b335544847 rdf:object :JohnDoe .
_:b335544847 :knowsFrom "Berlin" .

:ref_s2 rdf:subject :JaneDoe .
```

The advantage of CBD and SCBD over the `ForwardOneStep` and `SymmetricOneStep`
modes is that blank nodes are always expanded to include their representation.
This may be an important advantage because you can't query a blank
node using SPARQL. In addition, CBD and SCBD modes also consider reifications.

Note that the `describeMode` query hint can also be part of a
`WHERE` clause:

```
PREFIX hint: <http://aws.amazon.com/neptune/vocab/v01/QueryHints#>
DESCRIBE ?s
WHERE {
  hint:Query hint:describeMode "CBD" .
  ?s rdf:type <https://example.com/Person>
}
```

## The `describeIterationLimit` SPARQL query hint

The `hint:describeIterationLimit` SPARQL query hint provides an
**optional** constraint on the maximum number of iterative
expansions to be performed for iterative DESCRIBE algorithms such as CBD and SCBD.

DESCRIBE limits are ANDed together. Therefore, if both the iteration limit and
the statements limit are specified, then both limits must be met before the DESCRIBE
query is cut off.

The default for this value is 5. You may set it to ZERO (0) to specify NO limit
on the number of iterative expansions.

## The `describeStatementLimit` SPARQL query hint

The `hint:describeStatementLimit` SPARQL query hint provides an
**optional** constraint on the maximum number of statements
that may be present in a DESCRIBE query response. It is only applied for iterative
DESCRIBE algorithms such as CBD and SCBD.

DESCRIBE limits are ANDed together. Therefore, if both the iteration limit and
the statements limit are specified, then both limits must be met before the DESCRIBE
query is cut off.

The default for this value is 5000. You may set it to ZERO (0) to
specify NO limit on the number of statements returned.
