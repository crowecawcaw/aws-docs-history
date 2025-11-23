# Vector search for Amazon DocumentDB

Vector search is a method used in machine learning to find similar data points to a given data point by comparing their vector representations using distance or similarity metrics.
The closer the two vectors are in the vector space, the more similar the underlying items are considered to be.
This technique helps capture the semantic meaning of the data.
This approach is useful in various applications, such as recommendation systems, natural language processing, and image recognition.

Vector search for Amazon DocumentDB combines the flexibility and rich querying capability of a JSON-based document database with the power of vector search.
If you want to use your existing Amazon DocumentDB data or a flexible document data structure to build machine learning and generative AI use cases, such as semantic search experience, product recommendation, personalization, chatbots, fraud detection, and anomaly detection, then vector search for Amazon DocumentDB is an ideal choice for you.
Vector search is available on Amazon DocumentDB 5.0 instance-based clusters.

###### Topics

- [Inserting vectors](#w2aac21c11b9 "#w2aac21c11b9")
- [Creating a vector index](#w2aac21c11c11 "#w2aac21c11c11")
- [Getting an index definition](#w2aac21c11c13 "#w2aac21c11c13")
- [Querying vectors](#w2aac21c11c15 "#w2aac21c11c15")
- [Features and limitations](#vector-limitations "#vector-limitations")
- [Best practices](#w2aac21c11c19 "#w2aac21c11c19")
- [New Operator - $vectorSearch](#w2aac21c11c21 "#w2aac21c11c21")

## Inserting vectors

To insert vectors into your Amazon DocumentDB database, you can use existing insert methods:

**Example**

In the following example, a collection of five documents within a test database is created.
Each document includes two fields: the product name and its corresponding vector embedding.

```
db.collection.insertMany([
  {"product_name": "Product A", "vectorEmbedding": [0.2, 0.5, 0.8]},
  {"product_name": "Product B", "vectorEmbedding": [0.7, 0.3, 0.9]},
  {"product_name": "Product C", "vectorEmbedding": [0.1, 0.2, 0.5]},
  {"product_name": "Product D", "vectorEmbedding": [0.9, 0.6, 0.4]},
  {"product_name": "Product E", "vectorEmbedding": [0.4, 0.7, 0.2]}
]);
```

## Creating a vector index

Amazon DocumentDB supports both Hierarchical Navigable Small World (HNSW) indexing and Inverted File with Flat Compression (IVFFlat) indexing methods.
An IVFFlat index segregates vectors into lists and subsequently searches a selected subset of those lists that are nearest to the query vector.
On the other hand, an HNSW index organizes the vector data into a multi-layered graph.
Although HNSW has slower build times compared to IVFFlat, it delivers better query performance and recall.
Unlike IVFFlat, HNSW has no training step involved, allowing the index to be generated without any initial data load.
For the majority of use cases, we recommend using the HNSW index type for vector search.

If you do not create a vector index, Amazon DocumentDB performs an exact nearest neighbor search, ensuring perfect recall.
However, in production scenarios, speed is crucial.
We recommend using vector indexes, which may trade some recall for improved speed.
It's important to note that adding a vector index can lead to different query results.

**Templates**

You can use the following `createIndex` or `runCommand` templates to build a vector index on a vector field:

Using createIndex
In certain drivers, such as mongosh and Java, using the `vectorOptions` parameters in `createIndex` may result in an error.
In such cases, we recommend using `runCommand`:

```
db.collection.createIndex(
  { "<vectorField>": "vector" },
  { "name": "<indexName>",
    "vectorOptions": {
      "type": " <hnsw> | <ivfflat> ",
      "dimensions": <number_of_dimensions>,
      "similarity": " <euclidean> | <cosine> | <dotProduct> ",
      "lists": <number_of_lists> [applicable for IVFFlat],
      "m": <max number of connections> [applicable for HNSW],
      "efConstruction": <size of the dynamic list for index build> [applicable for HNSW]
    }
  }
);
```

Using runCommand
In certain drivers, such as mongosh and Java, using the `vectorOptions` parameters in `createIndex` may result in an error.
In such cases, we recommend using `runCommand`:

```
db.runCommand(
  { "createIndexes": "<collection>",
  "indexes": [{
      key: { "<vectorField>": "vector" },
      vectorOptions: {
          type: " <hnsw> | <ivfflat> ",
          dimensions: <number of dimensions>,
          similarity: " <euclidean> | <cosine> | <dotProduct> ",
          lists: <number_of_lists> [applicable for IVFFlat],
          m: <max number of connections> [applicable for HNSW],
          efConstruction: <size of the dynamic list for index build> [applicable for HNSW]
          },
      name: "myIndex"
      }]
  }
);
```

| Parameter        | Requirement          | Data type | Description                                                                                                                                                                                                           | Value(s)                                                                                                                                          |
| ---------------- | -------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`           | optional             | string    | Specifies the name of the index.                                                                                                                                                                                      | Alphanumeric                                                                                                                                      |
| `type`           | optional             |           | Specifies the type of index.                                                                                                                                                                                          | Supported: hnsw or ivfflat<br>Default: HNSW (engine patch 3.0.4574 onwards)                                                                       |
| `dimensions`     | required             | integer   | Specifies the number of dimensions in the vector data.                                                                                                                                                                | Maximum of 2,000 dimensions.                                                                                                                      |
| `similarity`     | required             | string    | Specifies the distance metric used for the similarity calculation.                                                                                                                                                    | • `euclidean`<br>• `cosine`<br>• `dotProduct`                                                                                                     |
| `lists`          | required for IVFFlat | integer   | Specifies the number of clusters that the IVFFlat index uses to group the vector data.<br>The recommended setting is the # of documents/1000 for up to 1M documents and `sqrt(# of documents)` for over 1M documents. | Minimum: 1<br>Maximum: Refer to the lists per instance type table in [Features and limitations](#vector-limitations "#vector-limitations") below. |
| `m`              | optional             | integer   | Specifies the max number of connections for an HNSW index                                                                                                                                                             | Default: 16<br>Range [2, 100]                                                                                                                     |
| `efConstruction` | optional             | integer   | Specifies the size of the dynamic candidate list for constructing the graph for HNSW index.<br>`efConstruction` must be greater than or equal to (2 \<br>• m)                                                         | Default: 64<br>Range [4, 1000]                                                                                                                    |

It is important that you set the value of sub-parameters such as `lists` for IVFFlat and `m` and `efConstruction` for HNSW appropriately as it will affect the accuracy/recall, build time, and performance of your search.
A higher list value increases the speed of the query as it reduces the number of vectors in each list, resulting in smaller regions.
However, a smaller region size may lead to more recall errors, resulting in lower accuracy.
For HNSW, increasing the value of `m` and `efConstruction` increases the accuracy, but also increases index build time and size.
See the following examples:

**Examples**

HNSW

```
db.collection.createIndex(
  { "vectorEmbedding": "vector" },
  { "name": "myIndex",
    "vectorOptions": {
      "type": "hnsw",
      "dimensions": 3,
      "similarity": "euclidean",
      "m": 16,
      "efConstruction": 64
    }
  }
);
```

IVFFlat

```
db.collection.createIndex(
  { "vectorEmbedding": "vector" },
  { "name": "myIndex",
    "vectorOptions": {
      "type": "ivfflat",
      "dimensions": 3,
      "similarity": "euclidean",
      "lists":1
    }
  }
)
```

## Getting an index definition

You can view the details of your indexes, including vector indexes, using the `getIndexes` command:

**Example**

```
db.collection.getIndexes()
```

**Example output**

```
[
 {
  "v" : 4,
  "key" : {
   "_id" : 1
  },
  "name" : "_id_",
  "ns" : "test.collection"
 },
 {
  "v" : 4,
  "key" : {
   "vectorEmbedding" : "vector"
  },
  "name" : "myIndex",
  "vectorOptions" : {
   "type" : "ivfflat",
   "dimensions" : 3,
   "similarity" : "euclidean",
   "lists" : 1
  },
  "ns" : "test.collection"
 }
]
```

## Querying vectors

**Vector query template**

Use the following template to query a vector:

```
db.collection.aggregate([
  {
    $search: {
      "vectorSearch": {
        "vector": <query vector>,
        "path": "<vectorField>",
        "similarity": "<distance metric>",
        "k": <number of results>,
        "probes":<number of probes> [applicable for IVFFlat],
        "efSearch":<size of the dynamic list during search> [applicable for HNSW]
      }
    }
  }
]);
```

| Parameter      | Requirement | Type     | Description                                                                                                                                                                                                                                                                                                                 | Value(s)                                      |
| -------------- | ----------- | -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| `vectorSearch` | required    | operator | Used inside $search command to query the vectors.                                                                                                                                                                                                                                                                           |                                               |
| `vector`       | required    | array    | Indicates the query vector that will be used to find similar vectors.                                                                                                                                                                                                                                                       |                                               |
| `path`         | required    | string   | Defines the name of the vector field.                                                                                                                                                                                                                                                                                       |                                               |
| `k`            | required    | integer  | Specifies the number of results that the search returns.                                                                                                                                                                                                                                                                    |                                               |
| `similarity`   | required    | string   | Specifies the distance metric used for the similarity calculation.                                                                                                                                                                                                                                                          | • `euclidean`<br>• `cosine`<br>• `dotProduct` |
| `probes`       | optional    | integer  | The number of clusters you want vector search to inspect.<br>A higher value provides better recall at the cost of speed.<br>It can be set to the number of lists for exact nearest neighbor search (at which point the planner won’t use the index).<br>The recommended setting to start fine-tuning is `sqrt(# of lists)`. | Default: 1                                    |
| `efSearch`     | optional    | integer  | Specifies the size of the dynamic candidate list that HNSW index uses during search.<br>A higher value of `efSearch` provides better recall at cost of speed.                                                                                                                                                               | Default: 40<br>Range [1, 1000]                |

It is important to fine tune the value of `efSearch` (HNSW) or `probes` (IVFFlat) to achieve your desired performance and accuracy.
See the following example operations:

HNSW

```
db.collection.aggregate([
  {
    $search: {
      "vectorSearch": {
        "vector": [0.2, 0.5, 0.8],
        "path": "vectorEmbedding",
        "similarity": "euclidean",
        "k": 2,
        "efSearch": 40
      }
    }
  }
]);
```

IVFFlat

```
db.collection.aggregate([
  {
    $search: {
      "vectorSearch": {
        "vector": [0.2, 0.5, 0.8],
        "path": "vectorEmbedding",
        "similarity": "euclidean",
        "k": 2,
        "probes": 1
      }
    }
  }
]);
```

**Example output**

Output from this operation looks something like the following:

```
{ "_id" : ObjectId("653d835ff96bee02cad7323c"), "product_name" : "Product A", "vectorEmbedding" : [ 0.2, 0.5, 0.8 ] }
{ "_id" : ObjectId("653d835ff96bee02cad7323e"), "product_name" : "Product C", "vectorEmbedding" : [ 0.1, 0.2, 0.5 ] }
```

## Features and limitations

**Version compatibility**

- Vector search for Amazon DocumentDB is only available on Amazon DocumentDB 5.0 instance-based clusters.

**Vectors**

- Amazon DocumentDB can index vectors of up to 2,000 dimensions.
  However, up to 16,000 dimensions can be stored without an index.

**Indexes**

- For IVFFlat index creation, the recommended setting for lists parameter is the number of documents/1000 for up to 1M documents and `sqrt(# of documents)` for over 1M documents.
  Due to a working memory limit, Amazon DocumentDB supports a certain maximum value of the lists parameter depending on the number of dimensions.
  For your reference, the following table provides the maximum values of lists parameter for vectors of 500, 1000, and 2,000 dimensions:

| Instance type | Lists with 500 dimensions | Lists with 1000 dimensions | Lists with 2000 dimensions |
| ------------- | ------------------------- | -------------------------- | -------------------------- |
| t3.med        | 372                       | 257                        | 150                        |
| r5.l          | 915                       | 741                        | 511                        |
| r5.xl         | 1,393                     | 1,196                      | 901                        |
| r5.2xl        | 5,460                     | 5,230                      | 4,788                      |
| r5.4xl        | 7,842                     | 7,599                      | 7,138                      |
| r5.8xl        | 11,220                    | 10,974                     | 10,498                     |
| r5.12xl       | 13,774                    | 13,526                     | 13,044                     |
| r5.16xl       | 15,943                    | 15,694                     | 15,208                     |
| r5.24xl       | 19,585                    | 19,335                     | 18,845                     |

- No other index options such as `compound`, `sparse` or `partial` are supported with vector indexes.
- Parallel index build is not supported for HNSW index. It is only supported for IVFFlat index.

**Vector query**

- For vector search query, it is important to fine tune the parameters such as `probes` or `efSearch` for optimum results.
  The higher the value of `probes` or `efSearch` parameter, the higher the recall and lower the speed.
  The recommended setting to start fine tuning the probes parameter is `sqrt(# of lists)`.

## Best practices

Learn best practices for working with vector search in Amazon DocumentDB.
This section is continually updated as new best practices are identified.

- Inverted File with Flat Compression (IVFFlat) index creation involves clustering and organizing the data points based on similarities.
  Hence, in order for an index to be more effective, we recommend that you at least load some data before creating the index.
- For vector search queries, it is important to fine tune the parameters such as `probes` or `efSearch` for optimum results.
  The higher the value of the `probes` or `efSearch` parameter, the higher is the recall and lower is the speed.
  The recommended setting to start fine tuning the `probes` parameter is `sqrt(lists)`.

**Resources**

- [Vector search what's new blog post](https://aws.amazon.com/blogs/aws/vector-search-for-amazon-documentdb-with-mongodb-compatibility-is-now-generally-available "https://aws.amazon.com/blogs/aws/vector-search-for-amazon-documentdb-with-mongodb-compatibility-is-now-generally-available")
- [Semantic search code sample](https://github.com/aws-samples/amazon-documentdb-samples/tree/master/blogs/semanticsearch-docdb "https://github.com/aws-samples/amazon-documentdb-samples/tree/master/blogs/semanticsearch-docdb")
- [Amazon DocumentDB vector search code samples](https://github.com/aws-samples/amazon-documentdb-samples/tree/master/samples/vector-search "https://github.com/aws-samples/amazon-documentdb-samples/tree/master/samples/vector-search")

## New Operator - $vectorSearch

Amazon DocumentDB 8.0 supports the MongoDB compatible $vectorSearch operator. Maximum dimension size you can use with $vectorSearch is 2000.

**Key Capabilities**

- HNSW (Hierarchical Navigable Small Worlds): HNSW builds a multi-layered graph where the top layers have fewer nodes for fast navigation, while lower layers have more nodes for precise searches.
  Searches start at the top layer and quickly narrow down the search space. The graph structure connects data points based on proximity, with denser connections in lower layers.
- Improved Performance: HNSW provides better query performance, logarithmic search time scaling, robustness to data distribution, and efficient insertions for dynamic datasets.
  HNSW is a good choice for dynamic datasets or applications needing the fastest searches and accepting higher memory usage.
- IVFF (Inverted File with Flat Compression): IVFFlat divides the vector space into clusters using algorithms like k-means clustering.
  It finds the closest clusters to a query vector and searches within them to find the nearest vectors.
  IVFFlat offers faster build times and lower memory usage than HNSW, and its searches are easier to parallelize. However, its query performance might be lower for high-recall searches, as it's more sensitive to data distribution and doesn't handle incremental updates as well as HNSW. It is best suited for static datasets or scenarios prioritizing faster build times and lower memory usage

**Syntax**

```

   db.collection.aggregate([
  {
    $search: {
      "vectorSearch": {
        "vector": query vector,
        "path": name of the vector_field,
        "similarity": distance metric,
        "k": number of results,
        "probes":number of probes [applicable for IVFFlat],
        "efSearch":size of the dynamic list during search [applicable for HNSW]
      }
    }
  }
]);


```
