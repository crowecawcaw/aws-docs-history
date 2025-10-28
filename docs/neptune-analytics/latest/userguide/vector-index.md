# Vector indexing in Neptune Analytics

You can only create a vector search index for a Neptune Analytics graph at the time the graph
is created. Neptune Analytics lets you create only one vector index for a graph, with a fixed
dimension between 1 and 65,535 inclusive.

When you [create a Neptune Analytics graph in the console](create-graph-using-console.md "create-graph-using-console.md"),
you specify the index dimension under **Vector search settings** near
the end of the process.

## Vector index transaction support

When using Neptune Analytics with a vector search index, it is important to understand that any updates performed on the vector
index are not ACID compliant - specifically, any updates to the vector index are not atomic in nature. Atomicity in
a database defines that when updates are performed, either all or none of them succeed. There are situations with the
vector index where updating the embeddings may succeed, even when the remainder of the transaction fails:

- When one or more concurrent queries are executed against different vertices, then atomicity is guaranteed.
- When one or more concurrent queries are executed against the same vertex, then there is no serializable guarantee
  of the resulting stored data.
- If one or more queries, including `neptune.load()` updates, fail to complete then the resulting
  index may contain partial updates.

To minimize the potential for this issue to occur, it is recommended that you either run a single query on a single
vertex at a time, or if you are running concurrent queries, that the set of vertices being updated are distinct.

## Loading vectors into a Neptune Analytics graph vector index

Note that the nodes in your graph must have at least one user property or label
in order to associate them with embeddings. Also, Neptune Analytics does not support the special
positive and negative infinity (`INF`, `-INF`) and not-a-number
(`NaN`) floating-point values.

Neptune Analytics supports optional embeddings in the CSV file when the vector index is enabled. This means that not every node
needs to be associated with an embedding.

Neptune Analytics does not currently support loading vectors from Neptune Database or a snapshot.

There are two ways you can load vectors associated with nodes in your graph:

### Load the vectors from graph data files Amazon S3

When you're loading graph data from files in Amazon S3 using the console or the
[neptune.load{}](batch-load.md "batch-load.md") openCypher integration,
you can add a column to your CSV data with an `embedding:vector` header.
This column should contain a list of integer or floating-point values separated by
semicolons ( `;` ) that forms a vector of the required dimension and
is the embedding for the node in question.

For example, associating a 4-dimensional vector with nodes in your graph
in the openCypher CSV format would look like this:

```
:ID, name:String, embedding:Vector, :LABEL
v1,"ABC",0.1;0.5;0.8;-1.32,person
v2,"DEF",8.1;-0.2;0.432;-1.02,person
v3,"GHI",12323343;24324;2433554;-4343434,person
v4,"JKL",121.12213;3223.212;265;-1.32,person
```

In the Gremlin CSV format, the same thing would look like this:

```
~id, name, embedding:vector, ~label
v1,"ABC",0.1;0.5;0.8;-1.32,person
v2,"DEF",8.1;-0.2;0.432;-1.02,person
v3,"GHI",12323343;24324;2433554;-4343434,person
v4,"JKL",121.12213;3223.212;265;-1.32,person
```

### Using the `vectors.upsert` algorithm to load vectors for your graph

You can also use the [vectors.upsert](vectors-upsert.md "vectors-upsert.md") algorithm
to insert or update embeddings in a Neptune Analytics graph that has a vector search index. For example,
in openCypher you can call the algorithm like this:

```
CALL neptune.algo.vectors.upsert(
  "person933",
  [0.1, 0.2, 0.3, ..]
)
YIELD node, embedding, success
RETURN node, embedding, success
```

Another example is:

```
UNWIND [
  {id: "933", embedding: [1,2,3,4]},
  {id: "934", embedding: [-1,-2,-3,-4]}
] as entry
MATCH (n:person) WHERE id(n)=entry.id WITH n, entry.embedding as embedding
CALL neptune.algo.vectors.upsert(n, embedding)
YIELD success
RETURN n, embedding, success
```

## Common errors you may encounter when loading embeddings

- If the embeddings you are trying to load have a different dimension
  than is expected by the vector index, the load fails with parsing exception and
  a message like the following:

```
An error occurred (ParsingException) when calling the
          ExecuteOpenCypherQuery operation: Could not load vector embedding: `(the
 embedding in question)`. Please check the dimensionality for this vector
          when parsing line [`(line number)`] in [`(file
 name)`]
```

- If the embeddings in a file are not properly formatted, Neptune Analytics reports a Parsing
  Exception before starting the load. For example, if the column header
  for the embedding column is not `embedding:vector`, Neptune Analytics would report
  an error like this:

```
An error occurred (ParsingException) when calling the
          ExecuteOpenCypherQuery operation: Invalid data type encountered for header
          `embedding:Vectttor` when parsing line
          [~id, name:string, embedding:Vectttor, ~label] in [`(file name)`]
```

- If embeddings are present in a file to be loaded but no vector index
  is present, Neptune Analytics simply ignores the embeddings and loads the graph data without them.

## Vector-search algorithms in Neptune Analytics

Neptune Analytics supports a variety of vector-search algorithms that are listed in the [VSS algorithms](vss-algorithms.md "vss-algorithms.md") section.
