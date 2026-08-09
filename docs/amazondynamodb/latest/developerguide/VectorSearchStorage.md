# Storage considerations for vector indexes

A vector index consumes storage separately from its base table. The storage a vector
index uses is determined by the following factors:

- **Vector data** – Each indexed item stores its
  vector as 32-bit floating point (f32) values. Storage for the vector portion of an
  item scales with the number of dimensions in the index. For example, a
  1,536-dimension vector uses roughly four times the vector storage of a
  384-dimension vector.
- **Projected attributes** – The projection you
  choose controls which base table attributes are copied into the index.
  `KEYS_ONLY` stores the least data, `INCLUDE` stores the
  key attributes plus the non-key attributes you name, and `ALL` stores
  every attribute. A broader projection increases index storage.
- **Number of indexed items** – Only items that
  contain a valid vector attribute (and, if the index defines a partition key, that
  partition key attribute) are replicated to the index. Items that are missing the
  vector attribute do not consume vector index storage.
  To control vector index storage, choose the smallest number of dimensions that meets
  your relevance needs and project only the attributes your application reads directly from
  search results. For current storage pricing, see the [Amazon DynamoDB pricing](https://aws.amazon.com/dynamodb/pricing/ "https://aws.amazon.com/dynamodb/pricing/") on the AWS website.
