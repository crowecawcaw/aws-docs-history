# AOSSUS03-BP02 Reduce unnecessary or redundant data from your

domain

Reduce storage costs, improve resource utilization, and enhance
resource management by removing unnecessary or redundant data from
your domain.

**Level of risk exposed if this best practice
is not established:** Medium

**Desired outcome:** You have removed
unnecessary or redundant data from your domain to support
sustainability goals.

**Benefits of establishing this best
practice:**

- Reduced storage costs and increased cost efficiency
- Improved resource utilization and reduced waste
- Enhanced ability to manage and optimize resources

## Implementation guidance

You can reduce unneeded and redundant data through various
methods, like using indexing strategies, implementing ISM, and
archiving data.

- Run `_cat/indices?v` to list your indices
- Use `DELETE /<index-name>` to remove unnecessary or
  redundant indices

## Resources

- [Index
  State Management in Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/ism.md "../../../opensearch-service/latest/developerguide/ism.md")
- [Cat
  Indices](https://opensearch.org/docs/latest/api-reference/cat/cat-indices/ "https://opensearch.org/docs/latest/api-reference/cat/cat-indices/")
- [Delete
  Index](https://opensearch.org/docs/latest/api-reference/index-apis/delete-index/ "https://opensearch.org/docs/latest/api-reference/index-apis/delete-index/")
