

# Gremlin standards compliance in Amazon Neptune
<a name="access-graph-gremlin-differences"></a>

The following sections provide an overview of the Neptune implementation of Gremlin and how it differs from the Apache TinkerPop implementation.

Neptune implements some Gremlin steps natively in its engine, and uses the Apache TinkerPop Gremlin implementation to process others (see [Native Gremlin step support in Amazon Neptune](gremlin-step-support.md)).

**Note**  
For some concrete examples of these implementation differences shown in Gremlin Console and Amazon Neptune, see the [Using Gremlin to access graph data in Amazon Neptune](get-started-graph-gremlin.md) section of the Quick Start.

**Topics**
+ [Applicable Standards for Gremlin](#feature-gremlin-applicable-standards)
+ [Variables and parameters in scripts](#feature-gremlin-differences-variables)
+ [Script execution](#feature-gremlin-differences-script)
+ [Properties on elements](#feature-gremlin-differences-properties-on-elements)
+ [Sessions](#feature-gremlin-differences-sessions)
+ [Transactions](#feature-gremlin-differences-transactions)
+ [Vertex and edge IDs](#feature-gremlin-differences-vertex-edge-ids)
+ [User-supplied IDs](#feature-gremlin-differences-user-supplied-ids)
+ [Vertex property IDs](#feature-gremlin-differences-vertex-property-ids)
+ [Cardinality of vertex properties](#feature-gremlin-differences-vertex-property-cardinality)
+ [Updating a vertex property](#feature-gremlin-differences-vertex-property-update)
+ [Labels](#feature-gremlin-differences-labels)
+ [Escape characters](#feature-gremlin-differences-escapes)
+ [Serialization](#feature-gremlin-differences-serialization)
+ [Lambda steps](#feature-gremlin-differences-lambda)
+ [Unsupported Gremlin steps](#feature-gremlin-differences-unsupported-steps)
+ [Gremlin graph features in Neptune](#gremlin-api-reference-features)

## Applicable Standards for Gremlin
<a name="feature-gremlin-applicable-standards"></a>
+ The Gremlin language is defined by [Apache TinkerPop Documentation](http://tinkerpop.apache.org/docs/current/reference/) and the Apache TinkerPop implementation of Gremlin rather than by a formal specification.
+ For numeric formats, Gremlin follows the IEEE 754 standard ([IEEE 754-2019 - IEEE Standard for Floating-Point Arithmetic](https://standards.ieee.org/content/ieee-standards/en/standard/754-2019.html). For more information, also see the [Wikipedia IEEE 754 page](https://en.wikipedia.org/wiki/IEEE_754)).

## Variables and parameters in scripts
<a name="feature-gremlin-differences-variables"></a>

Where pre-bound variables are concerned, the traversal object `g` is Pre-bound in Neptune, and the `graph` object is not supported.

Although Neptune does not support Gremlin variables or parameterization in scripts, you may often encounter sample scripts for Gremlin Server on the Internet that contain variable declarations, such as:

```
String query = "x = 1; g.V(x)";
List<Result> results = client.submit(query).all().get();
```

There are also many examples that make use of [parameterization](https://tinkerpop.apache.org/docs/current/reference/#parameterized-scripts) (or bindings) when submitting queries, such as:

```
Map<String,Object> params = new HashMap<>();
params.put("x",1);
String query = "g.V(x)";
List<Result> results = client.submit(query).all().get();
```

The parameter examples are usually associated with warnings about performance penalties for not parameterizing when possible. There are a great many such examples for TinkerPop that you may encounter, and they all sound quite convincing about the need to parameterize.

However, both the variables declarations feature and the parameterization feature (along with the warnings) only apply to TinkerPop's Gremlin Server when it is using the `GremlinGroovyScriptEngine`. They do not apply when Gremlin Server uses Gremlin's `gremlin-language` ANTLR grammar to parse queries. The ANTLR grammar doesn't support either variable declarations or parameterization, so when using ANTLR, you don't have to worry about failing to parameterize. Because the ANTLR grammar is a newer component of TinkerPop, older content you may encounter on the Internet doesn't generally reflect this distinction.

Neptune uses the ANTLR grammar in its query processing engine rather than the `GremlinGroovyScriptEngine`, so it does not support variables or parameterization or the `bindings` property. As a result, the problems related to failing to parameterize do not apply in Neptune. Using Neptune, it's perfectly safe simply to submit the query as-is where one would normally parameterize. As a result, the previous example can be simplified without any performance penalty as follows:

```
String query = "g.V(1)";
List<Result> results = client.submit(query).all().get();
```

## Script execution
<a name="feature-gremlin-differences-script"></a>

Neptune's Gremlin engine parses queries using TinkerPop's `gremlin-language` ANTLR grammar. It does *not* run a `GremlinGroovyScriptEngine` (as some TinkerPop-based Gremlin Server deployments do), so scripts submitted to Neptune must contain only the Gremlin language — not arbitrary Groovy or Java code.

Scripts can be sent to Neptune in a variety of ways, such as through the [Gremlin REST endpoint](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin-rest.html), the [Gremlin Console](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin-console.html), or via TinkerPop language drivers (for example, the [Java driver's script client](https://tinkerpop.apache.org/docs/current/reference/#gremlin-java-scripts)). The constraints described in this section apply to any of these text-string submission paths.

It's important not to confuse the Gremlin language itself with the syntactic sugar or general-purpose functions of whatever programming language you may have seen wrapping Gremlin examples elsewhere. Where such code appears in TinkerPop tutorials or online samples, it depends on a Groovy or Java runtime that Neptune does not provide.

**Important**  
Everything in this section applies to text-string Gremlin submissions. GLV (Gremlin Language Variant) bytecode submissions built in a host language such as Java, Python, or .NET are not subject to these constraints, because the host-language traversal builder produces bytecode that Neptune's engine consumes directly.

### What a script may contain
<a name="feature-gremlin-differences-script-contents"></a>
+ All queries must begin with `g`, the traversal object.
+ Multiple traversals can be issued in a single submission separated by a semicolon (`;`) or a newline character (`\n`). Every statement other than the last must end with an `.iterate()` step to be executed; only the final traversal's data is returned.

### Referencing TinkerPop enumeration values
<a name="feature-gremlin-differences-script-enumerations"></a>

Where a TinkerPop enumeration value is expected as a step argument (for example, a cardinality on `property()` or an order on `by()`), use the short-form values recognized by the ANTLR grammar. Neptune does not resolve fully qualified Java class names in this position — for example, `org.apache.tinkerpop.gremlin.structure.VertexProperty.Cardinality.single` is not accepted; use `single` instead.

The following table lists the allowed short-form values and the underlying TinkerPop class each one belongs to.

| Allowed Values | Class | 
| --- |--- |
| id, key, label, value | [org.apache.tinkerpop.gremlin.structure.T](https://tinkerpop.apache.org/javadocs/current/core/org/apache/tinkerpop/gremlin/structure/T.html) | 
| T.id, T.key, T.label, T.value | [org.apache.tinkerpop.gremlin.structure.T](https://tinkerpop.apache.org/javadocs/current/core/org/apache/tinkerpop/gremlin/structure/T.html) | 
| set, single | [org.apache.tinkerpop.gremlin.structure.VertexProperty.Cardinality](https://tinkerpop.apache.org/javadocs/current/core/org/apache/tinkerpop/gremlin/structure/VertexProperty.Cardinality.html) | 
| asc, desc, shuffle | [org.apache.tinkerpop.gremlin.process.traversal.Order](https://tinkerpop.apache.org/javadocs/3.7.2/full/org/apache/tinkerpop/gremlin/process/traversal/Order.html) | 
| Order.asc, Order.desc, Order.shuffle | [org.apache.tinkerpop.gremlin.process.traversal.Order](https://tinkerpop.apache.org/javadocs/3.7.2/full/org/apache/tinkerpop/gremlin/process/traversal/Order.html) | 
| global, local | [org.apache.tinkerpop.gremlin.process.traversal.Scope](https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/process/traversal/Scope.html) | 
| Scope.global, Scope.local | [org.apache.tinkerpop.gremlin.process.traversal.Scope](https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/process/traversal/Scope.html) | 
| all, first, last, mixed | [org.apache.tinkerpop.gremlin.process.traversal.Pop](https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/process/traversal/Pop.html) | 
| normSack | [org.apache.tinkerpop.gremlin.process.traversal.SackFunctions.Barrier](https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/process/traversal/SackFunctions.Barrier.html) | 
| addAll, and, assign, div, max, min, minus, mult, or, sum, sumLong | [org.apache.tinkerpop.gremlin.process.traversal.Operator](https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/process/traversal/Operator.html) | 
| keys, values | [org.apache.tinkerpop.gremlin.structure.Column](https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/structure/Column.html) | 
| BOTH, IN, OUT | [org.apache.tinkerpop.gremlin.structure.Direction](https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/structure/Direction.html) | 
| any, none | [org.apache.tinkerpop.gremlin.process.traversal.step.TraversalOptionParent.Pick](https://tinkerpop.apache.org/javadocs/current/full/org/apache/tinkerpop/gremlin/process/traversal/Pick.html) | 

### What a script may not contain
<a name="feature-gremlin-differences-script-not-contents"></a>

The following are **not** supported in text-string Gremlin queries to Neptune, because they rely on Groovy or Java runtime support that Neptune does not provide:
+ **Groovy statements that don't begin with `g`.** This includes:
  + Arithmetic expressions such as `1 + 1`
  + System calls such as `System.nanoTime()`
  + Variable declarations such as `x = 1; g.V(x)`
+ **Java method or library calls other than supported Gremlin APIs.** For example, `java.lang.*`, `Date()`, and `g.V().tryNext().orElseGet(...)` are not allowed.
+ **Gremlin methods that take a Java type as an argument.** These are only reachable from a JVM-language host, not from a text-string submission. Examples:
  + `org.apache.tinkerpop.gremlin.process.traversal.dsl.graph.GraphTraversal.program(org.apache.tinkerpop.gremlin.process.computer.VertexProgram)`
  + `org.apache.tinkerpop.gremlin.process.traversal.dsl.graph.GraphTraversal.sideEffect(java.util.function.Consumer)`
  + `org.apache.tinkerpop.gremlin.process.traversal.dsl.graph.GraphTraversal.from(org.apache.tinkerpop.gremlin.structure.Vertex)`
  + `org.apache.tinkerpop.gremlin.process.traversal.dsl.graph.GraphTraversal.to(org.apache.tinkerpop.gremlin.structure.Vertex)`

  For example, the following traversal cannot be submitted as a text string: `g.V().addE('something').from(__.V().next()).to(__.V().next())`.

## Properties on elements
<a name="feature-gremlin-differences-properties-on-elements"></a>

 Neptune does not support the `materializeProperties` flag that was introduced in TinkerPop 3.7.0 to return properties on elements. As a result, Neptune will still only return vertices or edges as references with just their `id` and `label`.

## Sessions
<a name="feature-gremlin-differences-sessions"></a>

Sessions in Neptune are limited to only 10 minutes in duration. See [Gremlin script-based sessions](access-graph-gremlin-sessions.md) and the [TinkerPop Session Reference](https://tinkerpop.apache.org/docs/current/reference/#console-sessions) for more information.

## Transactions
<a name="feature-gremlin-differences-transactions"></a>

Neptune opens a new transaction at the beginning of each Gremlin traversal and closes the transaction upon the successful completion of the traversal. The transaction is rolled back when there is an error. 

 Multiple statements separated by a semicolon (`;`) or a newline character (`\n`) are included in a single transaction. Every statement other than the last must end with a `next()` step to be executed. Only the final traversal data is returned.

Manual transaction logic using `tx.commit()` and `tx.rollback()` is not supported.

**Important**  
This ***only*** applies to methods where you send the Gremlin query as a ***text string*** (see [Gremlin transactions](access-graph-gremlin-transactions.md)).

## Vertex and edge IDs
<a name="feature-gremlin-differences-vertex-edge-ids"></a>

Neptune Gremlin Vertex and Edge IDs must be of type `String`. These ID strings support Unicode characters, and cannot exceed 55 MB in size.

User-supplied IDs are supported, but they are optional in normal usage. If you don't provide an ID when you add a vertex or an edge, Neptune generates a UUID and converts it to a string, in a form like this: `"48af8178-50ce-971a-fc41-8c9a954cea62"`. These UUIDs do not conform to the RFC standard, so if you need standard UUIDs you should generate them externally and provide them when you add vertices or edges.

**Note**  
The Neptune `Load` command requires that you provide IDs, using the **\~id** field in the Neptune CSV format.

## User-supplied IDs
<a name="feature-gremlin-differences-user-supplied-ids"></a>

User-supplied IDs are allowed in Neptune Gremlin with the following stipulations.
+ Supplied IDs are optional.
+ Only vertexes and edges are supported.
+ Only type `String` is supported.

To create a new vertex with a custom ID, use the `property` step with the `id` keyword: `g.addV().property(id, 'customid')`.

**Note**  
 Do not put quotation marks around the `id` keyword. It refers to `T.id`.

All vertex IDs must be unique, and all edge IDs must be unique. However, Neptune does allow a vertex and an edge to have the same ID.

If you try to create a new vertex using the `g.addV()` and a vertex with that ID already exists, the operation fails. The exception to this is if you specify a new label for the vertex, the operation succeeds but adds the new label and any additional properties specified to the existing vertex. Nothing is overwritten. A new vertex is not created. The vertex ID does not change and remains unique.

For example, the following Gremlin Console commands succeed:

```
gremlin> g.addV('label1').property(id, 'customid')
gremlin> g.addV('label2').property(id, 'customid')
gremlin> g.V('customid').label()
==>label1::label2
```

## Vertex property IDs
<a name="feature-gremlin-differences-vertex-property-ids"></a>

Vertex property IDs are generated automatically and can show up as positive or negative numbers when queried.

## Cardinality of vertex properties
<a name="feature-gremlin-differences-vertex-property-cardinality"></a>

Neptune supports set cardinality and single cardinality. If it isn't specified, set cardinality is selected. This means that if you set a property value, it adds a new value to the property, but only if it doesn't already appear in the set of values. This is the Gremlin enumeration value of [Set](https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/structure/VertexProperty.Cardinality.html). 

`List` is not supported. For more information about property cardinality, see the [Vertex](https://tinkerpop.apache.org/javadocs/3.7.2/core/org/apache/tinkerpop/gremlin/structure/Vertex.html#property-org.apache.tinkerpop.gremlin.structure.VertexProperty.Cardinality-java.lang.String-V-java.lang.Object...-) topic in the Gremlin JavaDoc.

## Updating a vertex property
<a name="feature-gremlin-differences-vertex-property-update"></a>

To update a property value without adding an additional value to the set of values, specify `single` cardinality in the `property` step.

```
g.V('exampleid01').property(single, 'age', 25)
```

This removes all existing values for the property.

## Labels
<a name="feature-gremlin-differences-labels"></a>

Neptune supports multiple labels for a vertex. When you create a label, you can specify multiple labels by separating them with `::`. For example, `g.addV("Label1::Label2::Label3")` adds a vertex with three different labels. The `hasLabel` step matches this vertex with any of those three labels: `hasLabel("Label1")`, `hasLabel("Label2")`, and `hasLabel("Label3")`. 

**Important**  
The `::` delimiter is reserved for this use only. You cannot specify multiple labels in the `hasLabel` step. For example, `hasLabel("Label1::Label2")` does not match anything.

## Escape characters
<a name="feature-gremlin-differences-escapes"></a>

Neptune resolves all escape characters as described in the [Escaping Special Characters]( http://groovy-lang.org/syntax.html#_escaping_special_characters) section of the Apache Groovy language documentation.

## Serialization
<a name="feature-gremlin-differences-serialization"></a>

Neptune supports the following serializations based on the requested MIME type.

 With Neptune, you can use many of the serializers that TinkerPop offers, with support for the various versions and configurations of GraphSON and GraphBinary. See the following table for the currently supported serializers. Despite there being many options present, the guidance for which to use is straightforward: 
+  If you are using Apache TinkerPop drivers, prefer the default for the driver without specifying one explicitly. Unless you have a very specific reason for doing so, you likely don’t need to specify the serializer in your driver initialization. In general, the default used by the drivers is `application/vnd.graphbinary-v1.0`. 
+  If you are connecting to Neptune over HTTP, prioritize the use of `application/vnd.gremlin-v3.0+json;types=false` as the embedded types in the alternative version of GraphSON 3 make it complicated to work with. 
+  The `application/vnd.graphbinary-v1.0-stringd` is generally only useful when used in conjunction with [Gremlin Console](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin-console.html) as it converts all results to a string representation for simple display. 
+  The remaining formats remain present for legacy reasons and should typically not be used with drivers without clear cause. 

|  |  |  | 
| --- |--- |--- |
| MIME type | Serialization | Configuration | 
| `application/vnd.gremlin-v1.0+json;types=false` | GraphSONUntypedMessageSerializerV1 | ioRegistries: [org.apache.tinkerpop.gremlin.tinkergraph.structure.TinkerIoRegistryV1] | 
| `application/vnd.gremlin-v2.0+json` | GraphSONMessageSerializerV2 | ioRegistries: [org.apache.tinkerpop.gremlin.tinkergraph.structure.TinkerIoRegistryV2] | 
| `application/vnd.gremlin-v2.0+json;types=false` | GraphSONUntypedMessageSerializerV2 | ioRegistries: [org.apache.tinkerpop.gremlin.tinkergraph.structure.TinkerIoRegistryV2] | 
| `application/vnd.gremlin-v3.0+json` | GraphSONMessageSerializerV3 | ioRegistries: [org.apache.tinkerpop.gremlin.tinkergraph.structure.TinkerIoRegistryV3] | 
| `application/vnd.gremlin-v3.0+json;types=false` | GraphSONUntypedMessageSerializerV3 | ioRegistries: [org.apache.tinkerpop.gremlin.tinkergraph.structure.TinkerIoRegistryV3] | 
| `application/json` | GraphSONUntypedMessageSerializerV3 | ioRegistries: [org.apache.tinkerpop.gremlin.tinkergraph.structure.TinkerIoRegistryV1] | 
| `application/vnd.graphbinary-v1.0` | GraphBinaryMessageSerializerV1 |  | 
| `application/vnd.graphbinary-v1.0-stringd` | GraphBinaryMessageSerializerV1 | serializeResultToString: true | 
| `application/vnd.gremlin-v1.0+json` | GraphSONMessageSerializerGremlinV1 | ioRegistries: [org.apache.tinkerpop.gremlin.tinkergraph.structure.TinkerIoRegistryV1] | 
| `application/vnd.gremlin-v2.0+json` | GraphSONMessageSerializerV2   (only works with WebSockets) | ioRegistries: [org.apache.tinkerpop.gremlin.tinkergraph.structure.TinkerIoRegistryV2] | 
| `application/vnd.gremlin-v3.0+json` | GraphSONMessageSerializerV3 |  | 
| `application/json` | GraphSONMessageSerializerV3 | ioRegistries: [org.apache.tinkerpop.gremlin.tinkergraph.structure.TinkerIoRegistryV3] | 
| `application/vnd.graphbinary-v1.0` | GraphBinaryMessageSerializerV1 |  | 

**Note**  
 The serializer table shown here refers to naming as of TinkerPop 3.7.0. If you would like to know more about this change, please see the [TinkerPop upgrade documentation](https://tinkerpop.apache.org/docs/current/upgrade/#_serializer_renaming). Gryo serialization support was deprecated in 3.4.3 and was officially removed in 3.6.0. If you are explicitly using Gryo or on a driver version that uses it by default, then you should switch to GraphBinary or upgrade your driver. 

## Lambda steps
<a name="feature-gremlin-differences-lambda"></a>

Neptune does not support Lambda Steps.

## Unsupported Gremlin steps
<a name="feature-gremlin-differences-unsupported-steps"></a>

Neptune does not support the following Gremlin steps:
+ The Gremlin [io( ) Step](http://tinkerpop.apache.org/docs/3.7.2/reference/#io-step) is only partially supported in Neptune. You can use it in a read context, as in `g.io("https://example.com/data/my-graph.graphml").read()`, but you cannot use it to write. To read a file that you store as an Amazon S3 object, first generate a presigned URL. Then pass that HTTPS URL to `g.io()`. For more information about presigned URLs, see [Download and upload objects with presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html) in the *Amazon S3 User Guide*.

## Gremlin graph features in Neptune
<a name="gremlin-api-reference-features"></a>

The Neptune implementation of Gremlin does not expose the `graph` object. The following tables list Gremlin features and indicate whether or not Neptune supports them.

### Neptune support for `graph` features
<a name="gremlin-api-graph-features"></a>

The Neptune graph features, where supported, are the same as would be returned by the `graph.features()` command.


| 
| 
| Graph feature | Enabled? | 
| --- |--- |
| Transactions |  true | 
| ThreadedTransactions |  false | 
| Computer |  false | 
| Persistence |  true | 
| ConcurrentAccess |  true | 

### Neptune support for variable features
<a name="gremlin-api-variable-features"></a>


| 
| 
| Variable feature | Enabled? | 
| --- |--- |
| Variables |  false | 
| SerializableValues |  false | 
| UniformListValues |  false | 
| BooleanArrayValues |  false | 
| DoubleArrayValues |  false | 
| IntegerArrayValues |  false | 
| StringArrayValues |  false | 
| BooleanValues |  false | 
| ByteValues |  false | 
| DoubleValues |  false | 
| FloatValues |  false | 
| IntegerValues |  false | 
| LongValues |  false | 
| MapValues |  false | 
| MixedListValues |  false | 
| StringValues |  false | 
| ByteArrayValues |  false | 
| FloatArrayValues |  false | 
| LongArrayValues |  false | 

### Neptune support for vertex features
<a name="gremlin-api-vertex-features"></a>


| 
| 
| Vertex feature | Enabled? | 
| --- |--- |
| MetaProperties |  false | 
| DuplicateMultiProperties |  false | 
| AddVertices |  true | 
| RemoveVertices |  true | 
| MultiProperties |  true | 
| UserSuppliedIds |  true | 
| AddProperty |  true | 
| RemoveProperty |  true | 
| NumericIds |  false | 
| StringIds |  true | 
| UuidIds |  false | 
| CustomIds |  false | 
| AnyIds |  false | 

### Neptune support for vertex property features
<a name="gremlin-api-vertex-property-features"></a>


| 
| 
| Vertex property feature | Enabled? | 
| --- |--- |
| UserSuppliedIds |  false | 
| AddProperty |  true | 
| RemoveProperty |  true | 
| NumericIds |  true | 
| StringIds |  true | 
| UuidIds |  false | 
| CustomIds |  false | 
| AnyIds |  false | 
| Properties |  true | 
| SerializableValues |  false | 
|  UniformListValues |  false | 
| BooleanArrayValues |  false | 
| DoubleArrayValues |  false | 
| IntegerArrayValues |  false | 
| StringArrayValues |  false | 
| BooleanValues |  true | 
| ByteValues |  true | 
| DoubleValues |  true | 
| FloatValues |  true | 
| IntegerValues |  true | 
| LongValues |  true | 
| MapValues |  false | 
| MixedListValues |  false | 
| StringValues |  true | 
| ByteArrayValues |  false | 
| FloatArrayValues |  false | 
| LongArrayValues |  false | 

### Neptune support for edge features
<a name="gremlin-api-edge-features"></a>


| 
| 
| Edge feature | Enabled? | 
| --- |--- |
| AddEdges |  true | 
| RemoveEdges |  true | 
| UserSuppliedIds |  true | 
| AddProperty |  true | 
| RemoveProperty |  true | 
| NumericIds |  false | 
| StringIds |  true | 
| UuidIds |  false | 
| CustomIds |  false | 
| AnyIds |  false | 

### Neptune support for edge property features
<a name="gremlin-api-edge-property-features"></a>


| 
| 
| Edge property feature | Enabled? | 
| --- |--- |
| Properties |  true | 
| SerializableValues |  false | 
| UniformListValues |  false | 
| BooleanArrayValues |  false | 
| DoubleArrayValues |  false | 
| IntegerArrayValues |  false | 
| StringArrayValues |  false | 
| BooleanValues |  true | 
| ByteValues |  true | 
| DoubleValues |  true | 
| FloatValues |  true | 
| IntegerValues |  true | 
| LongValues |  true | 
| MapValues |  false | 
| MixedListValues |  false | 
| StringValues |  true | 
| ByteArrayValues |  false | 
| FloatArrayValues |  false | 
| LongArrayValues |  false | 