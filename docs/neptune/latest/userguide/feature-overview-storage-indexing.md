# How Statements Are Indexed in Neptune

When you query a graph of quads, for each quad position, you can either specify a value
constraint, or not. The query returns all the quads that match the value constraints that you
specified.

Neptune uses indexes to resolve graph queries patterns. These indexes are over the four primary components
of a graph edge: Subject (source vertex in LPG); Predicate (RDF), or Property or Edge Label (LPG); Object
(target vertex or property value in LPG); and Graph (RDF) or Edge Identifier (LPG). There are 16 (2^4) possible
access patterns for these four quad component positions. You can query all 16 patterns efficiently without having
to scan and filter by using six indexes. Each quad statement index uses a key that is composed of the four position
values concatenated in a different order. One possible combination of quad statment indexes that would cover all
16 access paths is:

```

       Access Pattern                                     Index key order
  ----------------------------------------------------    ---------------
   1.  ????  (No constraints; returns every quad)             SPOG
   2.  SPOG  (Every position is constrained)                  SPOG
   3.  SPO?  (S, P, and O are constrained; G is not)          SPOG
   4.  SP??  (S and P are constrained; O and G are not)       SPOG
   5.  S???  (S is constrained; P, O, and G are not)          SPOG
   6.  S??G  (S and G are constrained; P and O are not)       SPOG

   7.  ?POG  (P, O, and G are constrained; S is not)          POGS
   8.  ?PO?  (P and O are constrained; S and G are not)       POGS
   9.  ?P??  (P is constrained; S, O, and G are not)          POGS

  10.  ?P?G  (P and G are constrained; S and O are not)       GPSO
  11.  SP?G  (S, P, and G are constrained; O is not)          GPSO
  12.  ???G  (G is constrained; S, P, and O are not)          GPSO

  13.  S?OG  (S, O, and G are constrained; P is not)          OGSP
  14.  ??OG  (O and G are constrained; S and P are not)       OGSP
  15.  ??O?  (O is constrained; S, P, and G are not)          OGSP

  16.  S?O?  (S and O are constrained; P and G are not)       OSGP
```

Neptune creates and maintains only three out of those six indexes by default:

- `SPOG –` Uses a key composed of `Subject + Predicate + Object + Graph`.
- `POGS –` Uses a key composed of `Predicate + Object + Graph + Subject`.
- `GPSO –` Uses a key composed of `Graph + Predicate + Subject + Object`.
  These three indexes handle many of the most common access patterns. Maintaining only three
  full statement indexes instead of six greatly reduces the resources that you need to support
  rapid access without scanning and filtering. For example, the `SPOG` index allows
  efficient lookup whenever a prefix of the positions, such as the vertex or vertex and property
  identifier, is bound. The `POGS` index allows efficient access when only the edge
  or property label stored in `P` position is bound.

The low-level API for finding statements takes a statement pattern in which some
positions are known and the rest are left for discovery by index search. By composing
the known positions into a key prefix according to the index key order for one
of the statement indexes, Neptune performs a range scan to retrieve all the
statements matching the known positions.

However, one of the statement indexes that Neptune does _not_ create
by default is a reverse traversal `OSGP` index, which can gather predicates across
objects and subjects. Instead, Neptune by default tracks distinct predicates in a separate
index that it uses to do a union scan of `{all P x POGS}`. When you are working
with Gremlin, a predicate corresponds to a property or an edge label.

If the number of distinct predicates in a graph becomes large, the default Neptune access
strategy can become inefficient. In Gremlin, for example, an `in()` step where no edge
labels are given, or any step that uses `in()` internally such as `both()`
or `drop()`, may become quite inefficient.

## Enabling OSGP Index Creation Using Lab Mode

If your data model creates a large number of distinct predicates, you may experience
reduced performance and higher operational costs that can be dramatically improved by using
Lab Mode to enable the [OSGP index](features-lab-mode.md#features-lab-mode-features-osgp-index "features-lab-mode.md#features-lab-mode-features-osgp-index")
in addition to the three indexes that Neptune maintains by default.

###### Note

This feature is available starting in [Neptune engine release 1.0.2.1](engine-releases-1.0.1.0.200463.md "engine-releases-1.0.1.0.200463.md").

Enabling the OSGP index can have a few down-sides:

- The insert rate may slow by up to 23%.
- Storage increases by up to 20%.
- Read queries that touch all indexes equally (which is quite rare) may
  have increased latencies.

In general, however, it is worth enabling the OSGP index for DB Clusters with a
large number of distinct predicates. Object-based searches become highly efficient
(for example, finding all incoming edges to a vertex, or all subjects connected to
a given object), and as a result dropping vertices becomes much more efficient too.

###### Important

You can only enable the OSGP index in an empty DB cluster, before
you load any data into it.

 

## Gremlin statements in the Neptune data model

Gremlin property-graph data is expressed in the SPOG model using three classes
of statements, namely:

- [Vertex Label Statements](gremlin-explain-background-statements.md#gremlin-explain-background-vertex-labels "gremlin-explain-background-statements.md#gremlin-explain-background-vertex-labels")
- [Edge Statements](gremlin-explain-background-statements.md#gremlin-explain-background-edge-statements "gremlin-explain-background-statements.md#gremlin-explain-background-edge-statements")
- [Property Statements](gremlin-explain-background-statements.md#gremlin-explain-background-property-statements "gremlin-explain-background-statements.md#gremlin-explain-background-property-statements")

For an explanation of how these are used in Gremlin queries, see [Understanding how Gremlin queries work in
Neptune](gremlin-explain-background.md "gremlin-explain-background.md").
