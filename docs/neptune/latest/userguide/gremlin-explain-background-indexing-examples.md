# How Neptune processes Gremlin

queries using statement indexes

Statements are accessed in Amazon Neptune by way of three statement indexes, as detailed in
[How Statements Are Indexed in Neptune](feature-overview-storage-indexing.md "feature-overview-storage-indexing.md"). Neptune extracts a statement
_pattern_ from a Gremlin query in which some positions are known, and the
rest are left for discovery by index search.

Neptune assumes that the size of the property graph schema is not large. This means that
the number of distinct edge labels and property names is fairly low, resulting in a low total
number of distinct predicates. Neptune tracks distinct predicates in a separate index. It
uses this cache of predicates to do a union scan of `{ all P x POGS }` rather than
use an OSGP index. Avoiding the need for a reverse traversal OSGP index saves both storage
space and load throughput.

The Neptune Gremlin Explain/Profile API lets you obtain the predicate count in your
graph. You can then determine whether your application invalidates the Neptune assumption
that your property graph schema is small.

The following examples help illustrate how Neptune uses indexes to process Gremlin
queries.

**Question: What are the labels of vertex
`v1`?**

```
  Gremlin code:      g.V('v1').label()
  Pattern:           (<v1>, <~label>, ?, ?)
  Known positions:   SP
  Lookup positions:  OG
  Index:             SPOG
  Key range:         <v1>:<~label>:*
```

**Question: What are the 'knows' out-edges of vertex
`v1`?**

```
  Gremlin code:      g.V('v1').out('knows')
  Pattern:           (<v1>, <knows>, ?, ?)
  Known positions:   SP
  Lookup positions:  OG
  Index:             SPOG
  Key range:         <v1>:<knows>:*
```

**Question: Which vertices have a `Person` vertex
label?**

```
  Gremlin code:      g.V().hasLabel('Person')
  Pattern:           (?, <~label>, <Person>, <~>)
  Known positions:   POG
  Lookup positions:  S
  Index:             POGS
  Key range:         <~label>:<Person>:<~>:*
```

**Question: What are the from/to vertices of a given edge
`e1`?**

```
  Gremlin code:      g.E('e1').bothV()
  Pattern:           (?, ?, ?, <e1>)
  Known positions:   G
  Lookup positions:  SPO
  Index:             GPSO
  Key range:         <e1>:*
```

One statement index that Neptune does **not** have is a
reverse traversal OSGP index. This index could be used to gather all incoming edges across all
edge labels, as in the following example.

**Question: What are the incoming adjacent vertices
`v1`?**

```
  Gremlin code:      g.V('v1').in()
  Pattern:           (?, ?, <v1>, ?)
  Known positions:   O
  Lookup positions:  SPG
  Index:             OSGP  // <-- Index does not exist
```
