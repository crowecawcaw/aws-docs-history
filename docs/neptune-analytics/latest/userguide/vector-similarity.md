# Working with vector similarity in Neptune Analytics

You can answer complex questions about your data by transforming data shapes into
embeddings (that is, vectors). Using a vector search index lets you answer
questions about the your data's context and its similarity and connection to other data.

For example, a support agent could translate a question that they receive into a
vector and use it to search the support knowledge base for articles that are similar
to the words in the question (implicit similarity). For the most applicable articles,
they could then collect metadata about the author, previous cases, runbooks, and so
on so as to provide additional context when answering the question (explicit data).

Vector similarity search in Neptune Analytics makes it easy for you to build machine learning
(ML) augmented search experiences and generative artificial intelligence (GenAI)
applications. It also gives you an overall lower total cost of ownership
and simpler management overhead because you no longer need to manage separate data
stores, build pipelines, or worry about keep the data stores in sync. You can
use vector similarity search in Neptune Analytics to augment your LLMs by integrating graph
queries for domain-specific context with the results from low-latency, nearest-neighbor
similarity search on embeddings imported from LLMs hosted in Amazon Bedrock,
Graph Neural Networks (GNNs) in GraphStorm, or other sources.

As an example, Bioinformatics researchers who are interested in re-purposing
existing blood pressure drugs for other treatable diseases, want to use vector
similarity search over in-house knowledge graphs to find patterns in protein
interaction networks.

For another example, a large online book retailer may need to use known pirated
material to quickly identify similar media in conjunction with a knowledge graph
to identify patterns of deceptive listing behaviours and find malicious sellers.

In both cases, vector search over a knowledge graph increases accuracy and
speed when building the solution. It reduces the operational overhead and complexity
using the tools available today.

You can create a vector index for your graph to try out this feature.
Neptune Analytics supports associating embeddings generated from LLMs with the nodes of your
graphs.

###### Contents

- [Vector indexing in Neptune Analytics](vector-index.md "vector-index.md")
  - [Vector index transaction support](vector-index.md#vector-index-transaction-support "vector-index.md#vector-index-transaction-support")
  - [Loading vectors into a Neptune Analytics graph vector index](vector-index.md#loading-vectors "vector-index.md#loading-vectors")
    - [Load the vectors from graph data files Amazon S3](vector-index.md#load-vectors-from-s3 "vector-index.md#load-vectors-from-s3")
    - [Using the vectors.upsert algorithm to load vectors for your graph](vector-index.md#load-vectors-using-upsert "vector-index.md#load-vectors-using-upsert")

  - [Common errors you may encounter when loading embeddings](vector-index.md#load-embedding-errors "vector-index.md#load-embedding-errors")
  - [Vector-search algorithms in Neptune Analytics](vector-index.md#vector-algorithms "vector-index.md#vector-algorithms")

- [Vector-similarity search (VSS) algorithms in Neptune Analytics](vss-algorithms.md "vss-algorithms.md")
  - [The  .vectors.distance  algorithm](vectors-distance.md "vectors-distance.md")
    - [.vectors.distance  syntax](vectors-distance.md#vectors-distance-syntax "vectors-distance.md#vectors-distance-syntax")
    - [.vectors.distance  inputs](vectors-distance.md#vectors-distance-inputs "vectors-distance.md#vectors-distance-inputs")
    - [.vectors.distance  outputs](vectors-distance.md#vectors-distance-outputs "vectors-distance.md#vectors-distance-outputs")
    - [.vectors.distance  query examples](vectors-distance.md#vectors-distance-query-example "vectors-distance.md#vectors-distance-query-example")
    - [Sample  .vectors.distance  output](vectors-distance.md#vectors-distance-sample-output "vectors-distance.md#vectors-distance-sample-output")

  - [The  .vectors.distanceByEmbedding  algorithm](vectors-distance-embedding.md "vectors-distance-embedding.md")
    - [.vectors.distanceByEmbedding  syntax](vectors-distance-embedding.md#vectors-distance-embedding-syntax "vectors-distance-embedding.md#vectors-distance-embedding-syntax")
    - [.vectors.distanceByEmbedding  inputs](vectors-distance-embedding.md#vectors-distance-embedding-inputs "vectors-distance-embedding.md#vectors-distance-embedding-inputs")
    - [.vectors.distanceByEmbedding  outputs](vectors-distance-embedding.md#vectors-distance-embedding-outputs "vectors-distance-embedding.md#vectors-distance-embedding-outputs")
    - [.vectors.distanceByEmbedding  query examples](vectors-distance-embedding.md#vectors-distance-embedding-query-example "vectors-distance-embedding.md#vectors-distance-embedding-query-example")
    - [Sample  .vectors.distanceByEmbedding  output](vectors-distance-embedding.md#vectors-distance-embedding-sample-output "vectors-distance-embedding.md#vectors-distance-embedding-sample-output")

  - [The  .vectors.get  algorithm](vectors-get.md "vectors-get.md")
    - [.vectors.get  syntax](vectors-get.md#vectors-get-syntax "vectors-get.md#vectors-get-syntax")
    - [.vectors.get  input](vectors-get.md#vectors-get-inputs "vectors-get.md#vectors-get-inputs")
    - [.vectors.get  outputs](vectors-get.md#vectors-get-outputs "vectors-get.md#vectors-get-outputs")
    - [.vectors.get  query example](vectors-get.md#vectors-get-query-example "vectors-get.md#vectors-get-query-example")
    - [Sample  .vectors.get  output](vectors-get.md#vectors-get-sample-output "vectors-get.md#vectors-get-sample-output")

  - [.vectors.topKByEmbedding algorithm](vectors-topKByEmbedding.md "vectors-topKByEmbedding.md")
    - [.vectors.topKByEmbedding  syntax](vectors-topKByEmbedding.md#vectors-topKByEmbedding-syntax "vectors-topKByEmbedding.md#vectors-topKByEmbedding-syntax")
    - [.vectors.topKByEmbedding  input](vectors-topKByEmbedding.md#vectors-topKByEmbedding-inputs "vectors-topKByEmbedding.md#vectors-topKByEmbedding-inputs")
    - [.vectors.topKByEmbedding  outputs](vectors-topKByEmbedding.md#vectors-topKByEmbedding-outputs "vectors-topKByEmbedding.md#vectors-topKByEmbedding-outputs")
    - [.vectors.topKByEmbedding  query example](vectors-topKByEmbedding.md#vectors-topKByEmbedding-query-example "vectors-topKByEmbedding.md#vectors-topKByEmbedding-query-example")
    - [Sample  .vectors.topKByEmbedding  output](vectors-topKByEmbedding.md#vectors-topKByEmbedding-sample-output "vectors-topKByEmbedding.md#vectors-topKByEmbedding-sample-output")

  - [.vectors.topKByNode algorithm](vectors-topKByNode.md "vectors-topKByNode.md")
    - [.vectors.topKByNode  syntax](vectors-topKByNode.md#vectors-topKByNode-syntax "vectors-topKByNode.md#vectors-topKByNode-syntax")
    - [.vectors.topKByNode  input](vectors-topKByNode.md#vectors-topKByNode-inputs "vectors-topKByNode.md#vectors-topKByNode-inputs")
    - [.vectors.topKByNode  outputs](vectors-topKByNode.md#vectors-topKByNode-outputs "vectors-topKByNode.md#vectors-topKByNode-outputs")
    - [.vectors.topKByNode  query example](vectors-topKByNode.md#vectors-topKByNode-query-example "vectors-topKByNode.md#vectors-topKByNode-query-example")
    - [Sample  .vectors.topKByNode  output](vectors-topKByNode.md#vectors-topKByNode-sample-output "vectors-topKByNode.md#vectors-topKByNode-sample-output")

  - [.vectors.upsert algorithm](vectors-upsert.md "vectors-upsert.md")
    - [.vectors.upsert  syntax](vectors-upsert.md#vectors-upsert-syntax "vectors-upsert.md#vectors-upsert-syntax")
    - [.vectors.upsert  input](vectors-upsert.md#vectors-upsert-inputs "vectors-upsert.md#vectors-upsert-inputs")
    - [.vectors.upsert  outputs](vectors-upsert.md#vectors-upsert-outputs "vectors-upsert.md#vectors-upsert-outputs")
    - [.vectors.upsert  query examples](vectors-upsert.md#vectors-upsert-query-example "vectors-upsert.md#vectors-upsert-query-example")
    - [Sample  .vectors.upsert  output](vectors-upsert.md#vectors-upsert-sample-output "vectors-upsert.md#vectors-upsert-sample-output")

  - [.vectors.remove algorithm](vectors-remove.md "vectors-remove.md")
    - [.vectors.remove  syntax](vectors-remove.md#vectors-remove-syntax "vectors-remove.md#vectors-remove-syntax")
    - [.vectors.remove  input](vectors-remove.md#vectors-remove-inputs "vectors-remove.md#vectors-remove-inputs")
    - [.vectors.remove  outputs](vectors-remove.md#vectors-remove-outputs "vectors-remove.md#vectors-remove-outputs")
    - [.vectors.remove  query examples](vectors-remove.md#vectors-remove-query-example "vectors-remove.md#vectors-remove-query-example")
    - [Sample  .vectors.remove  output](vectors-remove.md#vectors-remove-sample-output "vectors-remove.md#vectors-remove-sample-output")
