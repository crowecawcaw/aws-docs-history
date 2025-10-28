# AOSPERF04-BP02 Use static mapping for your index

Improve indexing performance and query efficiency by using fixed,
static mappings instead of dynamic ones.

**Level of risk exposed if this best practice
is not established:** Medium

**Desired outcome**: You use static
mappings instead of dynamic mappings, employing efficient and
optimized indexing and querying strategies.

**Benefits of establishing this best
practice:**

- **Improve indexing performance:**
  Using static mappings for your index in OpenSearch Service domains can improve indexing performance by defining a
  fixed mapping at creation time, which is more efficient than
  dynamic mappings.
- **Enhance query efficiency:** By
  using static mappings, you can also enhance query efficiency and
  reduce the risk of slower query performance associated with
  dynamic mappings.

## Implementation guidance

To improve indexing and query performance in OpenSearch Service domains, consider switching from dynamic to static
mappings. Understand the difference between static and dynamic
mappings to choose the best approach for your data.

- **Static mappings:** Define a
  fixed mapping for an index at creation time. This approach is
  more efficient and can provide better performance.
- **Dynamic mappings:** Allow
  OpenSearch to detect and create mappings automatically based
  on the data being indexed. While convenient, this approach can
  lead to slower query performance and increased storage and
  resources, such as CPU and memory, usage.

### Implementation steps

- Mappings are defined at index level. The following is an
  example of a static mapping:

```
PUT sample-index1
        {
        "mappings": {
        "properties": {
        "year": { "type" : "text" },
        "age": { "type" : "integer" },
        "director":{ "type" : "text" }
        }
        }
        }
```

- Mappings can be either created using `PUT HTTP verb` or
  added to an existing mapping using `POST HTTP`. But you
  cannot change the mapping of an existing field. If you need
  to change existing field types, consider using the `_reindex` API
  to copy the data to a new index.

## Resources

- [Mappings
  and field types](https://opensearch.org/docs/latest/field-types/ "https://opensearch.org/docs/latest/field-types/")
