# Vector-similarity search (VSS) algorithms in Neptune Analytics

Vector simlarity search algorithms identify similar vectors based on the vector
distance between them.

Neptune Analytics supports the following vector-similarity search algorithms:

###### Note

The following special floating-point values are not supported in Neptune Analytics
vector-similarity search algorithms:

- **INF**  (infinity)
- **-INF**  (negative infinity)
- **NaN**  (not-a-number)

###### Contents

- [The  .vectors.distance  algorithm (deprecated)](vectors-distance.md "vectors-distance.md")
  - [.vectors.distance  syntax](vectors-distance.md#vectors-distance-syntax "vectors-distance.md#vectors-distance-syntax")
  - [.vectors.distance  inputs](vectors-distance.md#vectors-distance-inputs "vectors-distance.md#vectors-distance-inputs")
  - [.vectors.distance  outputs](vectors-distance.md#vectors-distance-outputs "vectors-distance.md#vectors-distance-outputs")
  - [.vectors.distance  query examples](vectors-distance.md#vectors-distance-query-example "vectors-distance.md#vectors-distance-query-example")
  - [Sample  .vectors.distance  output](vectors-distance.md#vectors-distance-sample-output "vectors-distance.md#vectors-distance-sample-output")

- [The  .vectors.distance.byNode  algorithm](vectors.distance.md "vectors.distance.md")
  - [.vectors.distance.byNode  syntax](vectors.distance.md#vectors.distance.byNode-syntax "vectors.distance.md#vectors.distance.byNode-syntax")
  - [.vectors.distance.byNode  inputs](vectors.distance.md#vectors.distance.byNode-inputs "vectors.distance.md#vectors.distance.byNode-inputs")
  - [.vectors.distance.byNode  outputs](vectors.distance.md#vectors.distance.byNode-outputs "vectors.distance.md#vectors.distance.byNode-outputs")
  - [.vectors.distance.byNode  query examples](vectors.distance.md#vectors.distance.byNode-query-example "vectors.distance.md#vectors.distance.byNode-query-example")
  - [Sample  .vectors.distance.byNode  output](vectors.distance.md#vectors.distance.byNode-sample-output "vectors.distance.md#vectors.distance.byNode-sample-output")

- [The  .vectors.distanceByEmbedding  algorithm (deprecated)](vectors-distance-embedding.md "vectors-distance-embedding.md")
  - [.vectors.distanceByEmbedding  syntax](vectors-distance-embedding.md#vectors-distance-embedding-syntax "vectors-distance-embedding.md#vectors-distance-embedding-syntax")
  - [.vectors.distanceByEmbedding  inputs](vectors-distance-embedding.md#vectors-distance-embedding-inputs "vectors-distance-embedding.md#vectors-distance-embedding-inputs")
  - [.vectors.distanceByEmbedding  outputs](vectors-distance-embedding.md#vectors-distance-embedding-outputs "vectors-distance-embedding.md#vectors-distance-embedding-outputs")
  - [.vectors.distanceByEmbedding  query examples](vectors-distance-embedding.md#vectors-distance-embedding-query-example "vectors-distance-embedding.md#vectors-distance-embedding-query-example")
  - [Sample  .vectors.distanceByEmbedding  output](vectors-distance-embedding.md#vectors-distance-embedding-sample-output "vectors-distance-embedding.md#vectors-distance-embedding-sample-output")

- [The  .vectors.distance.byEmbedding  algorithm](vectors.distance.md "vectors.distance.md")
  - [.vectors.distance.byEmbedding  syntax](vectors.distance.md#vectors.distance.byEmbedding-syntax "vectors.distance.md#vectors.distance.byEmbedding-syntax")
  - [.vectors.distance.byEmbedding  inputs](vectors.distance.md#vectors.distance.byEmbedding-inputs "vectors.distance.md#vectors.distance.byEmbedding-inputs")
  - [.vectors.distance.byEmbedding  outputs](vectors.distance.md#vectors.distance.byEmbedding-outputs "vectors.distance.md#vectors.distance.byEmbedding-outputs")
  - [.vectors.distance.byEmbedding  query examples](vectors.distance.md#vectors.distance.byEmbedding-query-example "vectors.distance.md#vectors.distance.byEmbedding-query-example")
  - [Sample  .vectors.distance.byEmbedding  output](vectors.distance.md#vectors.distance.byEmbedding-sample-output "vectors.distance.md#vectors.distance.byEmbedding-sample-output")

- [The  .vectors.get  algorithm](vectors-get.md "vectors-get.md")
  - [.vectors.get  syntax](vectors-get.md#vectors-get-syntax "vectors-get.md#vectors-get-syntax")
  - [.vectors.get  input](vectors-get.md#vectors-get-inputs "vectors-get.md#vectors-get-inputs")
  - [.vectors.get  outputs](vectors-get.md#vectors-get-outputs "vectors-get.md#vectors-get-outputs")
  - [.vectors.get  query example](vectors-get.md#vectors-get-query-example "vectors-get.md#vectors-get-query-example")
  - [Sample  .vectors.get  output](vectors-get.md#vectors-get-sample-output "vectors-get.md#vectors-get-sample-output")

- [.vectors.topKByEmbedding algorithm (deprecated)](vectors-topKByEmbedding.md "vectors-topKByEmbedding.md")
  - [.vectors.topKByEmbedding  syntax](vectors-topKByEmbedding.md#vectors-topKByEmbedding-syntax "vectors-topKByEmbedding.md#vectors-topKByEmbedding-syntax")
  - [.vectors.topKByEmbedding  input](vectors-topKByEmbedding.md#vectors-topKByEmbedding-inputs "vectors-topKByEmbedding.md#vectors-topKByEmbedding-inputs")
  - [.vectors.topKByEmbedding  outputs](vectors-topKByEmbedding.md#vectors-topKByEmbedding-outputs "vectors-topKByEmbedding.md#vectors-topKByEmbedding-outputs")
  - [.vectors.topKByEmbedding  query example](vectors-topKByEmbedding.md#vectors-topKByEmbedding-query-example "vectors-topKByEmbedding.md#vectors-topKByEmbedding-query-example")
  - [Sample  .vectors.topKByEmbedding  output](vectors-topKByEmbedding.md#vectors-topKByEmbedding-sample-output "vectors-topKByEmbedding.md#vectors-topKByEmbedding-sample-output")

- [.vectors.topK.byEmbedding algorithm](vectors.topK.md "vectors.topK.md")
  - [.vectors.topK.byEmbedding  syntax](vectors.topK.md#vectors.topK.byEmbedding-syntax "vectors.topK.md#vectors.topK.byEmbedding-syntax")
  - [.vectors.topK.byEmbedding  input](vectors.topK.md#vectors.topK.byEmbedding-inputs "vectors.topK.md#vectors.topK.byEmbedding-inputs")
  - [.vectors.topK.byEmbedding  outputs](vectors.topK.md#vectors.topK.byEmbedding-outputs "vectors.topK.md#vectors.topK.byEmbedding-outputs")
  - [.vectors.topK.byEmbedding  query example](vectors.topK.md#vectors.topK.byEmbedding-query-example "vectors.topK.md#vectors.topK.byEmbedding-query-example")
  - [Sample  .vectors.topKByEmbedding  output](vectors.topK.md#vectors-topKByEmbedding-sample-output "vectors.topK.md#vectors-topKByEmbedding-sample-output")

- [.vectors.topKByNode algorithm (deprecated)](vectors-topKByNode.md "vectors-topKByNode.md")
  - [.vectors.topKByNode  syntax](vectors-topKByNode.md#vectors-topKByNode-syntax "vectors-topKByNode.md#vectors-topKByNode-syntax")
  - [.vectors.topKByNode  input](vectors-topKByNode.md#vectors-topKByNode-inputs "vectors-topKByNode.md#vectors-topKByNode-inputs")
  - [.vectors.topKByNode  outputs](vectors-topKByNode.md#vectors-topKByNode-outputs "vectors-topKByNode.md#vectors-topKByNode-outputs")
  - [.vectors.topKByNode  query example](vectors-topKByNode.md#vectors-topKByNode-query-example "vectors-topKByNode.md#vectors-topKByNode-query-example")
  - [Sample  .vectors.topKByNode  output](vectors-topKByNode.md#vectors-topKByNode-sample-output "vectors-topKByNode.md#vectors-topKByNode-sample-output")

- [.vectors.topK.byNode algorithm](vectors.topK.md "vectors.topK.md")
  - [.vectors.topK.byNode  syntax](vectors.topK.md#vectors.topK.byNode-syntax "vectors.topK.md#vectors.topK.byNode-syntax")
  - [.vectors.topK.byNode  input](vectors.topK.md#vectors.topK.byNode-inputs "vectors.topK.md#vectors.topK.byNode-inputs")
  - [.vectors.topK.byNode  outputs](vectors.topK.md#vectors.topK.byNode-outputs "vectors.topK.md#vectors.topK.byNode-outputs")
  - [.vectors.topK.byNode  query example](vectors.topK.md#vectors.topK.byNode-query-example "vectors.topK.md#vectors.topK.byNode-query-example")
  - [Sample  .vectors.topK.byNode  output](vectors.topK.md#vectors.topK.byNode-sample-output "vectors.topK.md#vectors.topK.byNode-sample-output")

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
