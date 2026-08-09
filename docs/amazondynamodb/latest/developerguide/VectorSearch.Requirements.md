# Requirements and limitations

Keep the following requirements and limitations in mind when you work with vector
indexes:

- Vector indexes are supported only on tables that use on-demand capacity
  mode.
- Vector embeddings are stored in the index at 32-bit floating point (f32)
  precision. Higher-precision values are accepted but lose precision when
  replicated to the index.
- Fine-grained access control (FGAC) is not supported for the
  `SearchVectors` API.
- `SearchVectors` responses are limited to 16 MB. Pagination is
  not supported. Because each result includes the projected attributes, using
  `ProjectionType: ALL` with large items and a high
  `TopK` value can approach this limit. If your items are large,
  use a narrower projection or reduce `TopK`.
- Vector indexes do not support `Query` or `Scan`
  operations. Use the `SearchVectors` API to read from vector
  indexes.
- Vector indexes are not accessible through PartiQL. Use the
  `SearchVectors` API to run similarity searches.
  For numeric limits including maximum dimensions, TopK range, inline filters per
  index, indexes per table, and base table size thresholds, see
  [Vector indexes](ServiceQuotas.md#limits-vector-indexes "ServiceQuotas.md#limits-vector-indexes") in
  [Quotas in Amazon DynamoDB](ServiceQuotas.md "ServiceQuotas.md").
