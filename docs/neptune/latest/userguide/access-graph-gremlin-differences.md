# Gremlin standards compliance in Amazon Neptune

The following sections provide an overview of the Neptune implementation of Gremlin and
how it differs from the Apache TinkerPop implementation.

Neptune implements some Gremlin steps natively in its engine, and uses the Apache
TinkerPop Gremlin implementation to process others (see [Native Gremlin step support in Amazon Neptune](gremlin-step-support.md "gremlin-step-support.md")).

###### Note

For some concrete examples of these implementation differences shown in Gremlin Console
and Amazon Neptune, see the [Using Gremlin to access graph data in Amazon Neptune](get-started-graph-gremlin.md "get-started-graph-gremlin.md") section of the Quick
Start.

###### Topics

- [Applicable Standards for Gremlin](#feature-gremlin-applicable-standards "#feature-gremlin-applicable-standards")
- [Variables and parameters in scripts](#feature-gremlin-differences-variables "#feature-gremlin-differences-variables")
- [TinkerPop enumerations](#feature-gremlin-differences-tinkerpop "#feature-gremlin-differences-tinkerpop")
- [Java code](#feature-gremlin-differences-java "#feature-gremlin-differences-java")
- [Properties on elements](#feature-gremlin-differences-properties-on-elements "#feature-gremlin-differences-properties-on-elements")
- [Script execution](#feature-gremlin-differences-script "#feature-gremlin-differences-script")
- [Sessions](#feature-gremlin-differences-sessions "#feature-gremlin-differences-sessions")
- [Transactions](#feature-gremlin-differences-transactions "#feature-gremlin-differences-transactions")
- [Vertex and edge IDs](#feature-gremlin-differences-vertex-edge-ids "#feature-gremlin-differences-vertex-edge-ids")
- [User-supplied IDs](#feature-gremlin-differences-user-supplied-ids "#feature-gremlin-differences-user-supplied-ids")
- [Vertex property IDs](#feature-gremlin-differences-vertex-property-ids "#feature-gremlin-differences-vertex-property-ids")
- [Cardinality of vertex properties](#feature-gremlin-differences-vertex-property-cardinality "#feature-gremlin-differences-vertex-property-cardinality")
- [Updating a vertex property](#feature-gremlin-differences-vertex-property-update "#feature-gremlin-differences-vertex-property-update")
- [Labels](#feature-gremlin-differences-labels "#feature-gremlin-differences-labels")
- [Escape characters](#feature-gremlin-differences-escapes "#feature-gremlin-differences-escapes")
- [Groovy limitations](#feature-gremlin-differences-groovy "#feature-gremlin-differences-groovy")
- [Serialization](#feature-gremlin-differences-serialization "#feature-gremlin-differences-serialization")
- [Lambda steps](#feature-gremlin-differences-lambda "#feature-gremlin-differences-lambda")
- [Unsupported Gremlin methods](#feature-gremlin-differences-unsupported-methods "#feature-gremlin-differences-unsupported-methods")
- [Unsupported Gremlin steps](#feature-gremlin-differences-unsupported-steps "#feature-gremlin-differences-unsupported-steps")
- [Gremlin graph features in Neptune](#gremlin-api-reference-features "#gremlin-api-reference-features")

## Applicable Standards for Gremlin

- The Gremlin language is defined by [Apache TinkerPop Documentation](http://tinkerpop.apache.org/docs/current/reference/ "http://tinkerpop.apache.org/docs/current/reference/")
  and the Apache TinkerPop implementation of Gremlin rather than by a formal specification.
- For numeric formats, Gremlin follows the IEEE 754 standard ([IEEE
  754-2019 - IEEE Standard for Floating-Point Arithmetic](https://standards.ieee.org/content/ieee-standards/en/standard/754-2019.html "https://standards.ieee.org/content/ieee-standards/en/standard/754-2019.html"). For more information,
  also see the [Wikipedia IEEE 754
  page](https://en.wikipedia.org/wiki/IEEE_754 "https://en.wikipedia.org/wiki/IEEE_754")).

## Variables and parameters in scripts

Where pre-bound variables are concerned, the traversal object `g` is
Pre-bound in Neptune, and the `graph` object is not supported.

Although Neptune does not support Gremlin variables or parameterization in
scripts, you may often encounter sample scripts for Gremlin Server on the Internet
that contain variable declarations, such as:

```
String query = "x = 1; g.V(x)";
List<Result> results = client.submit(query).all().get();
```

There are also many examples that make use of [parameterization](https://tinkerpop.apache.org/docs/current/reference/#parameterized-scripts "https://tinkerpop.apache.org/docs/current/reference/#parameterized-scripts")
(or bindings) when submitting queries, such as:

```
Map<String,Object> params = new HashMap<>();
params.put("x",1);
String query = "g.V(x)";
List<Result> results = client.submit(query).all().get();
```

The parameter examples are usually associated with warnings about performance
penalties for not parameterizing when possible. There are a great many such examples
for TinkerPop that you may encounter, and they all sound quite convincing about the
need to parameterize.

Since Neptune uses the `gremlin-language` ANTLR grammar instead of
the `GremlinGroovyScriptEngine` which relies on the Groovy programming
language for query processing, it does not support variable declarations or
parameterization features that are typically found in TinkerPop's Gremlin Server.
This means you can submit queries directly without parameterization in Neptune
without any performance penalties, as demonstrated in this simplified example:

```
String query = "g.V(1)";
List<Result> results = client.submit(query).all().get();
```

This distinction may not be apparent in older online documentation that assumes
the use of `GremlinGroovyScriptEngine`.

## TinkerPop enumerations

Neptune does not support fully qualified class names for enumeration values. For
example, you must use `single` and not
`org.apache.tinkerpop.gremlin.structure.VertexProperty.Cardinality.single` in
your Groovy request.

The enumeration type is determined by parameter type.

The following table shows the allowed enumeration values and the related TinkerPop fully
qualified name.

| Enum          | Allowed Values                                                                                | Class                                                                                                                                                                                                                                                                                                                                                         |
| ------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Cardinality` | `set`, `single`                                                                               | [org.apache.tinkerpop.gremlin.structure.VertexProperty.Cardinality](https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/structure/VertexProperty.Cardinality.html "https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/structure/VertexProperty.Cardinality.html")                                        |
| `Barrier`     | `normSack`                                                                                    | [org.apache.tinkerpop.gremlin.process.traversal.SackFunctions.Barrier](https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/process/traversal/SackFunctions.Barrier.html "https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/process/traversal/SackFunctions.Barrier.html")                               |
| `Column`      | `keys`, `values`                                                                              | [org.apache.tinkerpop.gremlin.structure.Column](https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/structure/Column.html "https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/structure/Column.html")                                                                                                    |
| `Direction`   | `BOTH`, `IN`, `from`, `OUT`, `to`                                                             | [org.apache.tinkerpop.gremlin.structure.Direction](https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/structure/Direction.html "https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/structure/Direction.html")                                                                                           |
| `DT`          | `day`, `hour`, `minute`, `second`                                                             | [org.apache.tinkerpop.gremlin.process.traversal.DT](https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/process/traversal/DT.html "https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/process/traversal/DT.html")                                                                                        |
| `Merge`       | `inV`, `outV`, `onCreate`, `onMatch`                                                          | [org.apache.tinkerpop.gremlin.process.traversal.Merge](https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/process/traversal/Merge.html "https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/process/traversal/Merge.html")                                                                               |
| `Operator`    | `addAll`, `and`, `assign`, `div`,<br>`max`, `min`, `minus`, `mult`,<br>`or`, `sum`, `sumLong` | [org.apache.tinkerpop.gremlin.process.traversal.Operator](https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/process/traversal/Operator.html "https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/process/traversal/Operator.html")                                                                      |
| `Order`       | `asc`, `desc`, `shuffle`                                                                      | [org.apache.tinkerpop.gremlin.process.traversal.Order](https://tinkerpop.apache.org/javadocs/3.7.2/full/org/apache/tinkerpop/gremlin/process/traversal/Order.html "https://tinkerpop.apache.org/javadocs/3.7.2/full/org/apache/tinkerpop/gremlin/process/traversal/Order.html")                                                                               |
| `Pick`        | `any`, `none`                                                                                 | [org.apache.tinkerpop.gremlin.process.traversal.step.TraversalOptionParent.Pick](https://tinkerpop.apache.org/javadocs/3.7.2/full/org/apache/tinkerpop/gremlin/process/traversal/step/TraversalOptionParent.Pick.html "https://tinkerpop.apache.org/javadocs/3.7.2/full/org/apache/tinkerpop/gremlin/process/traversal/step/TraversalOptionParent.Pick.html") |
| `Pop`         | `all`, `first`, `last`, `mixed`                                                               | [org.apache.tinkerpop.gremlin.process.traversal.Pop](https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/process/traversal/Pop.html "https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/process/traversal/Pop.html")                                                                                     |
| `Scope`       | `global`, `local`                                                                             | [org.apache.tinkerpop.gremlin.process.traversal.Scope](https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/process/traversal/Scope.html "https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/process/traversal/Scope.html")                                                                               |
| `T`           | `id`, `key`, `label`, `value`                                                                 | [org.apache.tinkerpop.gremlin.structure.T](https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/structure/T.html "https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/structure/T.html")                                                                                                                   |

## Java code

Neptune does not support calls to methods defined by arbitrary Java or Java library
calls other than supported Gremlin APIs. For example, `java.lang.*`,
`Date()`, and `g.V().tryNext().**orElseGet**()` are not allowed.

## Properties on elements

Neptune does not support the `materializeProperties` flag that was introduced in TinkerPop 3.7.0 to return
properties on elements. As a result, Neptune will still only return vertices or edges as references with just their
`id` and `label`.

## Script execution

All queries must begin with `g`, the traversal object.

In String query submissions, multiple traversals can be issued separated by a semicolon
(`;`) or a newline character (`\n`). To be executed, every statement
other than the last must end with an `.iterate()` step. Only the final traversal
data is returned. Note that this does not apply to GLV ByteCode query submissions.

## Sessions

Sessions in Neptune are limited to only 10 minutes in duration. See [Gremlin script-based sessions](access-graph-gremlin-sessions.md "access-graph-gremlin-sessions.md")
and the [TinkerPop
Session Reference](https://tinkerpop.apache.org/docs/current/reference/#console-sessions "https://tinkerpop.apache.org/docs/current/reference/#console-sessions") for more information.

## Transactions

Neptune opens a new transaction at the beginning of each Gremlin traversal and closes
the transaction upon the successful completion of the traversal. The transaction is rolled
back when there is an error.

Multiple statements separated by a semicolon (`;`) or a newline character
(`\n`) are included in a single transaction. Every statement other than the last
must end with a `next()` step to be executed. Only the final traversal data is
returned.

Manual transaction logic using `tx.commit()` and `tx.rollback()`
is not supported.

###### Important

This **_only_** applies
to methods where you send the Gremlin query as a **_text
string_** (see [Gremlin transactions](access-graph-gremlin-transactions.md "access-graph-gremlin-transactions.md")).

## Vertex and edge IDs

Neptune Gremlin Vertex and Edge IDs must be of type `String`. These ID strings
support Unicode characters, and cannot exceed 55 MB in size.

User-supplied IDs are supported, but they are optional in normal usage. If you don't
provide an ID when you add a vertex or an edge, Neptune generates a UUID
and converts it to a string, in a form like this: `"48af8178-50ce-971a-fc41-8c9a954cea62"`.
These UUIDs do not conform to the RFC standard, so if you need standard UUIDs you should
generate them externally and provide them when you add vertices or edges.

###### Note

The Neptune `Load` command requires that you provide IDs, using
the **~id** field in the Neptune CSV format.

## User-supplied IDs

User-supplied IDs are allowed in Neptune Gremlin with the following
stipulations.

- Supplied IDs are optional.
- Only vertexes and edges are supported.
- Only type `String` is supported.

To create a new vertex with a custom ID, use the `property` step with the
`id` keyword: `g.addV().property(id, 'customid')`.

###### Note

Do not put quotation marks around the `id` keyword. It refers to
`T.id`.

All vertex IDs must be unique, and all edge IDs must be unique. However, Neptune does
allow a vertex and an edge to have the same ID.

If you try to create a new vertex using the `g.addV()` and a vertex with that
ID already exists, the operation fails. The exception to this is if you specify a new label
for the vertex, the operation succeeds but adds the new label and any additional properties
specified to the existing vertex. Nothing is overwritten. A new vertex is not created. The
vertex ID does not change and remains unique.

For example, the following Gremlin Console commands succeed:

```
gremlin> g.addV('label1').property(id, 'customid')
gremlin> g.addV('label2').property(id, 'customid')
gremlin> g.V('customid').label()
==>label1::label2
```

## Vertex property IDs

Vertex property IDs are generated automatically and can show up as positive or negative
numbers when queried.

## Cardinality of vertex properties

Neptune supports set cardinality and single cardinality. If it isn't specified, set
cardinality is selected. This means that if you set a property value, it adds a new value to
the property, but only if it doesn't already appear in the set of values. This is the Gremlin
enumeration value of [Set](https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/structure/VertexProperty.Cardinality.html "https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/structure/VertexProperty.Cardinality.html").

`List` is not supported. For more information about property cardinality, see
the [Vertex](https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/structure/Vertex.html#property-org.apache.tinkerpop.gremlin.structure.VertexProperty.Cardinality-java.lang.String-V-java.lang.Object...- "https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/structure/Vertex.html#property-org.apache.tinkerpop.gremlin.structure.VertexProperty.Cardinality-java.lang.String-V-java.lang.Object...-") topic in the Gremlin JavaDoc.

## Updating a vertex property

To update a property value without adding an additional value to the set of values,
specify `single` cardinality in the `property` step.

```
g.V('exampleid01').property(single, 'age', 25)
```

This removes all existing values for the property.

## Labels

Neptune supports multiple labels for a vertex. When you create a label, you can
specify multiple labels by separating them with `::`. For example,
`g.addV("Label1::Label2::Label3")` adds a vertex with three different labels.
The `hasLabel` step matches this vertex with any of those three labels:
`hasLabel("Label1")`, `hasLabel("Label2")`, and
`hasLabel("Label3")`.

###### Important

The `::` delimiter is reserved for this use only. You cannot specify multiple
labels in the `hasLabel` step. For example,
`hasLabel("Label1::Label2")` does not match anything.

## Escape characters

Neptune resolves all escape characters as described in the [Escaping Special
Characters](http://groovy-lang.org/syntax.html#_escaping_special_characters " http://groovy-lang.org/syntax.html#_escaping_special_characters") section of the Apache Groovy language documentation.

## Groovy limitations

Neptune uses the `gremlin-language` ANTLR grammar for query processing. As
such it does not support Groovy code. This includes math (for example, `1+1`),
system calls (for example, `System.nanoTime()`), fully qualified class names (for
example, `org.apache.tinkerpop.gremlin.structure.Direction.OUT`) and variable
definitions (for example, `x=1`). Scripts sent to the server must be valid Gremlin
syntax that start with `g` as in `g.V()`.

## Serialization

Neptune supports the following serializations based on the requested MIME type.

Neptune exposes all of the serializers that TinkerPop does, with support for the various versions and configurations
of GraphSON and GraphBinary. Despite there being many options present, the guidance for which to use is straightforward:

- If you are using Apache TinkerPop drivers, prefer the default for the driver without specifying one explicitly.
  Unless you have a very specific reason for doing so, you likely don’t need to specify the serializer in your driver
  initialization. In general, the default used by the drivers is `application/vnd.graphbinary-v1.0`.
- If you are connecting to Neptune over HTTP, prioritize the use of
  `application/vnd.gremlin-v3.0+json;types=false` as the embedded types in the alternative version of
  GraphSON 3 make it complicated to work with.
- The `application/vnd.graphbinary-v1.0-stringd` is generally only useful when used in conjunction with
  [Gremlin Console](access-graph-gremlin-console.md "access-graph-gremlin-console.md")
  as it converts all results to a string representation for simple display.
- The remaining formats remain present for legacy reasons and should typically not be used with drivers without clear cause.

|                                                 |                                                              |                                                                                         |
| ----------------------------------------------- | ------------------------------------------------------------ | --------------------------------------------------------------------------------------- |
| MIME type                                       | Serialization                                                | Configuration                                                                           |
| `application/vnd.gremlin-v1.0+json`             | `GraphSONMessageSerializerV1`                                | `ioRegistries: [org.apache.tinkerpop.gremlin.tinkergraph.structure.TinkerIoRegistryV1]` |
| `application/vnd.gremlin-v1.0+json;types=false` | `GraphSONUntypedMessageSerializerV1`                         | `ioRegistries: [org.apache.tinkerpop.gremlin.tinkergraph.structure.TinkerIoRegistryV1]` |
| `application/vnd.gremlin-v2.0+json`             | `GraphSONMessageSerializerV2`                                | `ioRegistries: [org.apache.tinkerpop.gremlin.tinkergraph.structure.TinkerIoRegistryV2]` |
| `application/vnd.gremlin-v2.0+json;types=false` | `GraphSONUntypedMessageSerializerV2`                         | `ioRegistries: [org.apache.tinkerpop.gremlin.tinkergraph.structure.TinkerIoRegistryV2]` |
| `application/vnd.gremlin-v3.0+json`             | `GraphSONMessageSerializerV3`                                | `ioRegistries: [org.apache.tinkerpop.gremlin.tinkergraph.structure.TinkerIoRegistryV3]` |
| `application/vnd.gremlin-v3.0+json;types=false` | `GraphSONUntypedMessageSerializerV3`                         | `ioRegistries: [org.apache.tinkerpop.gremlin.tinkergraph.structure.TinkerIoRegistryV3]` |
| `application/json`                              | `GraphSONUntypedMessageSerializerV3`                         | `ioRegistries: [org.apache.tinkerpop.gremlin.tinkergraph.structure.TinkerIoRegistryV1]` |
| `application/vnd.graphbinary-v1.0`              | `GraphBinaryMessageSerializerV1`                             |                                                                                         |
| `application/vnd.graphbinary-v1.0-stringd`      | `GraphBinaryMessageSerializerV1`                             | `serializeResultToString: true`                                                         |
| `application/vnd.gremlin-v1.0+json`             | `GraphSONMessageSerializerGremlinV1`                         | `ioRegistries: [org.apache.tinkerpop.gremlin.tinkergraph.structure.TinkerIoRegistryV1]` |
| `application/vnd.gremlin-v2.0+json`             | `GraphSONMessageSerializerV2`   (only works with WebSockets) | `ioRegistries: [org.apache.tinkerpop.gremlin.tinkergraph.structure.TinkerIoRegistryV2]` |
| `application/vnd.gremlin-v3.0+json`             | `GraphSONMessageSerializerV3`                                |                                                                                         |
| `application/json`                              | `GraphSONMessageSerializerV3`                                | `ioRegistries: [org.apache.tinkerpop.gremlin.tinkergraph.structure.TinkerIoRegistryV3]` |
| `application/vnd.graphbinary-v1.0`              | `GraphBinaryMessageSerializerV1`                             |                                                                                         |

###### Note

The serializer table shown here refers to naming as of TinkerPop 3.7.0. If you would like to know more about this change,
please see the [TinkerPop upgrade
documentation](https://tinkerpop.apache.org/docs/current/upgrade/#_serializer_renaming "https://tinkerpop.apache.org/docs/current/upgrade/#_serializer_renaming"). Gryo serialization support was deprecated in 3.4.3 and was officially removed in 3.6.0. If you
are explicitly using Gryo or on a driver version that uses it by default, then you should switch to GraphBinary or
upgrade your driver.

## Lambda steps

Neptune does not support Lambda Steps.

## Unsupported Gremlin methods

Neptune does not support the following Gremlin methods:

- `org.apache.tinkerpop.gremlin.process.traversal.dsl.graph.GraphTraversal.program(org.apache.tinkerpop.gremlin.process.computer.VertexProgram)`
- `org.apache.tinkerpop.gremlin.process.traversal.dsl.graph.GraphTraversal.sideEffect(java.util.function.Consumer)`
- `org.apache.tinkerpop.gremlin.process.traversal.dsl.graph.GraphTraversal.from(org.apache.tinkerpop.gremlin.structure.Vertex)`
- `org.apache.tinkerpop.gremlin.process.traversal.dsl.graph.GraphTraversal.to(org.apache.tinkerpop.gremlin.structure.Vertex)`

For example, the following traversal is not allowed:
`g.V().addE('something').from(__.V().next()).to(__.V().next())`.

###### Important

This **_only_**
applies to methods where you send the Gremlin query as a **_text
string_**.

## Unsupported Gremlin steps

Neptune does not support the following Gremlin steps:

- The Gremlin [io( ) Step](http://tinkerpop.apache.org/docs/3.7.2/reference/#io-step "http://tinkerpop.apache.org/docs/3.7.2/reference/#io-step")
  is only partially supported in Neptune. It can be used in a read context, as in
  `g.io(`(url)`).read()`, but not to write.

## Gremlin graph features in Neptune

The Neptune implementation of Gremlin does not expose the `graph` object.
The following tables list Gremlin features and indicate whether or not Neptune
supports them.

### Neptune support for `graph` features

The Neptune graph features, where supported, are the same as would be returned
by the `graph.features()` command.

| Graph feature          | Enabled? |
| ---------------------- | -------- |
| `Transactions`         | true     |
| `ThreadedTransactions` | false    |
| `Computer`             | false    |
| `Persistence`          | true     |
| `ConcurrentAccess`     | true     |

### Neptune support for variable features

| Variable feature     | Enabled? |
| -------------------- | -------- |
| `Variables`          | false    |
| `SerializableValues` | false    |
| `UniformListValues`  | false    |
| `BooleanArrayValues` | false    |
| `DoubleArrayValues`  | false    |
| `IntegerArrayValues` | false    |
| `StringArrayValues`  | false    |
| `BooleanValues`      | false    |
| `ByteValues`         | false    |
| `DoubleValues`       | false    |
| `FloatValues`        | false    |
| `IntegerValues`      | false    |
| `LongValues`         | false    |
| `MapValues`          | false    |
| `MixedListValues`    | false    |
| `StringValues`       | false    |
| `ByteArrayValues`    | false    |
| `FloatArrayValues`   | false    |
| `LongArrayValues`    | false    |

### Neptune support for vertex features

| Vertex feature             | Enabled? |
| -------------------------- | -------- |
| `MetaProperties`           | false    |
| `DuplicateMultiProperties` | false    |
| `AddVertices`              | true     |
| `RemoveVertices`           | true     |
| `MultiProperties`          | true     |
| `UserSuppliedIds`          | true     |
| `AddProperty`              | true     |
| `RemoveProperty`           | true     |
| `NumericIds`               | false    |
| `StringIds`                | true     |
| `UuidIds`                  | false    |
| `CustomIds`                | false    |
| `AnyIds`                   | false    |

### Neptune support for vertex property features

| Vertex property feature | Enabled? |
| ----------------------- | -------- |
| `UserSuppliedIds`       | false    |
| `AddProperty`           | true     |
| `RemoveProperty`        | true     |
| `NumericIds`            | true     |
| `StringIds`             | true     |
| `UuidIds`               | false    |
| `CustomIds`             | false    |
| `AnyIds`                | false    |
| `Properties`            | true     |
| `SerializableValues`    | false    |
| UniformListValues       | false    |
| `BooleanArrayValues`    | false    |
| `DoubleArrayValues`     | false    |
| `IntegerArrayValues`    | false    |
| `StringArrayValues`     | false    |
| `BooleanValues`         | true     |
| `ByteValues`            | true     |
| `DoubleValues`          | true     |
| `FloatValues`           | true     |
| `IntegerValues`         | true     |
| `LongValues`            | true     |
| `MapValues`             | false    |
| `MixedListValues`       | false    |
| `StringValues`          | true     |
| `ByteArrayValues`       | false    |
| `FloatArrayValues`      | false    |
| `LongArrayValues`       | false    |

### Neptune support for edge features

| Edge feature      | Enabled? |
| ----------------- | -------- |
| `AddEdges`        | true     |
| `RemoveEdges`     | true     |
| `UserSuppliedIds` | true     |
| `AddProperty`     | true     |
| `RemoveProperty`  | true     |
| `NumericIds`      | false    |
| `StringIds`       | true     |
| `UuidIds`         | false    |
| `CustomIds`       | false    |
| `AnyIds`          | false    |

### Neptune support for edge property features

| Edge property feature | Enabled? |
| --------------------- | -------- |
| `Properties`          | true     |
| `SerializableValues`  | false    |
| `UniformListValues`   | false    |
| `BooleanArrayValues`  | false    |
| `DoubleArrayValues`   | false    |
| `IntegerArrayValues`  | false    |
| `StringArrayValues`   | false    |
| `BooleanValues`       | true     |
| `ByteValues`          | true     |
| `DoubleValues`        | true     |
| `FloatValues`         | true     |
| `IntegerValues`       | true     |
| `LongValues`          | true     |
| `MapValues`           | false    |
| `MixedListValues`     | false    |
| `StringValues`        | true     |
| `ByteArrayValues`     | false    |
| `FloatArrayValues`    | false    |
| `LongArrayValues`     | false    |
