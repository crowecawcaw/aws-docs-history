

# Vector indexing in Neptune Analytics
<a name="vector-index"></a>

You can only create a vector search index for a Neptune Analytics graph at the time the graph is created. Neptune Analytics lets you create only one vector index for a graph, with a fixed dimension between 1 and 65,535 inclusive.

When you [create a Neptune Analytics graph in the console](create-graph-using-console.md), you specify the index dimension under **Vector search settings** near the end of the process.

## Vector index transaction support
<a name="vector-index-transaction-support"></a>

 When using Neptune Analytics with a vector search index, it is important to understand that any updates performed on the vector index are not ACID compliant — specifically, any updates to the vector index are not atomic in nature. Atomicity in a database defines that when updates are performed, either all or none of them succeed. The changes to vector embeddings (inserts, deletes, and updates), unlike other parts of the graph, are non-atomic and not isolated. 

 Atomicity ensures that either all or no updates by a query are applied. Isolation ensures that concurrent queries do not see effects of a running query. However, changes to vector embeddings by a query become durable on write and visible to all other queries, even if that query fails later. 

 If a query updates the vector embeddings and makes other changes to the graph, then only the latter are atomic and isolated. For instance, if you are running a bulk load using a `neptune.load()` request that adds new vertices with vector embeddings and it fails midway, then the graph would contain vertex embeddings for a subset of new vertices that were written before the request failed. 

To minimize inconsistencies to vector updates, we recommend the following:

1. Avoid concurrently updating vector embeddings for any vertex.

1. Make queries that update vector embeddings idempotent and retry failed queries. For instance, a failed `neptune.load()` request can be retried to apply the remainder of the vector embedding properties and the rest of the properties for all the vertices in the input dataset. The following two example queries illustrate this. The first one finds vertices by given IDs and upserts their embeddings, and is likely to succeed on retry if the query fails. However, the second query creates vertices with given IDs and embeddings, and retries may not help if the query fails because a vertex already exists with one of the IDs. Thus the second query pattern should be avoided.

   **Example: idempotent upsert query**

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

   **Example: non-idempotent upsert query (avoid this pattern)**

   In this case, if a vertex with ID '934' already exists then the `CREATE` for the second vertex would fail even on retries, but the side effect of embeddings added to the vertex with ID "933" would remain because those embeddings were committed on insert.

   ```
   UNWIND [
     {id: "933", embedding: [1,2,3,4]},
     {id: "934", embedding: [-1,-2,-3,-4]}
   ] as entry
   CREATE (n:person {`~id`: entry.id}) WITH n, entry.embedding as embedding
   CALL neptune.algo.vectors.upsert(n, embedding)
   YIELD success
   RETURN n, embedding, success
   ```

1. Use simple queries for updating vectors and avoid chaining vector operations with other vector operations or other vertex/property/edge updates. For instance, the following query updates embeddings for a vertex and creates another vertex. Separating them into two queries should help avoid inconsistencies.

   ```
   MATCH (n {`~id`: '933'}) CALL neptune.algo.vectors.upsert(n, [1,2,3,4])
    YIELD success
   CREATE (m {`~id`: '934'})
   ```

## Loading vectors into a Neptune Analytics graph vector index
<a name="loading-vectors"></a>

Note that the nodes in your graph must have at least one user property or label in order to associate them with embeddings. Also, Neptune Analytics does not support the special positive and negative infinity (`INF`, `-INF`) and not-a-number (`NaN`) floating-point values.

Neptune Analytics supports optional embeddings in the CSV file when the vector index is enabled. This means that not every node needs to be associated with an embedding.

Neptune Analytics does not currently support loading vectors from Neptune Database or a snapshot.

There are two ways you can load vectors associated with nodes in your graph:

### Load the vectors from graph data files in Amazon S3
<a name="load-vectors-from-s3"></a>

When you're loading graph data from files in Amazon S3 using the console or the [`neptune.load{}`](batch-load.md) openCypher integration, you can add a column to your CSV data with an `embedding:vector` header. This column should contain a list of integer or floating-point values separated by semicolons (` ; `) that forms a vector of the required dimension and is the embedding for the node in question.

For example, associating a 4-dimensional vector with nodes in your graph in the openCypher CSV format would look like this:

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
<a name="load-vectors-using-upsert"></a>

You can also use the [vectors.upsert](vectors-upsert.md) algorithm to insert or update embeddings in a Neptune Analytics graph that has a vector search index. For example, in openCypher you can call the algorithm like this:

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
<a name="load-embedding-errors"></a>
+ If the embeddings you are trying to load have a different dimension than is expected by the vector index, the load fails with parsing exception and a message like the following:

  ```
  An error occurred (ParsingException) when calling the
            ExecuteOpenCypherQuery operation: Could not load vector embedding: {{(the
            embedding in question)}}. Please check the dimensionality for this vector
            when parsing line [{{(line number)}}] in [{{(file
            name)}}]
  ```
+ If the embeddings in a file are not properly formatted, Neptune Analytics reports a Parsing Exception before starting the load. For example, if the column header for the embedding column is not `embedding:vector`, Neptune Analytics would report an error like this:

  ```
  An error occurred (ParsingException) when calling the
            ExecuteOpenCypherQuery operation: Invalid data type encountered for header
            {{embedding:Vectttor}} when parsing line
            [~id, name:string, embedding:Vectttor, ~label] in [{{(file name)}}]
  ```
+ If embeddings are present in a file to be loaded but no vector index is present, Neptune Analytics simply ignores the embeddings and loads the graph data without them.

## Vector-search algorithms in Neptune Analytics
<a name="vector-algorithms"></a>

Neptune Analytics supports a variety of vector-search algorithms that are listed in the [VSS algorithms](vss-algorithms.md) section.