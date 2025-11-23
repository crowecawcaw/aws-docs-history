# Non-string OpenSearch indexing in Amazon Neptune

Non-string OpenSearch indexing in Amazon Neptune allows replicating non-string
values for predicates to OpenSearch using the stream poller. All predicate values
that can safely be converted to a corresponding OpenSearch mapping or datatype is
then replicated to OpenSearch.

For non-string indexing to be enabled on a new stack, the `Enable Non-String Indexing`
flag in the CloudFormation template must be set to `true`. This is the default
setting. To update an existing stack to support non-string indexing, see [Updating an existing stack](full-text-search-non-string-indexing-update.md "full-text-search-non-string-indexing-update.md") below.

###### Note

- It is best not to enable non-string indexing on engine versions earlier
  than **`1.0.4.2`**.
- OpenSearch queries using regular expressions for field names
  that match multiple fields, some of which contain string values and others of
  which contain non-string values, fail with an error. The same thing happens if
  full-text search queries in Neptune are of that type.
- When sorting by a non-string field, append ".value" to the field
  name to differentiate it from a string field.

###### Contents

- [Updating an existing Neptune full-text search stack to support non-string indexing](full-text-search-non-string-indexing-update.md "full-text-search-non-string-indexing-update.md")
- [Filtering what fields are indexed in Neptune full-text search](full-text-search-non-string-indexing-filters.md "full-text-search-non-string-indexing-filters.md")
  - [Filter by property or predicate name](full-text-search-non-string-indexing-filters.md#full-text-search-non-string-indexing-filters-name "full-text-search-non-string-indexing-filters.md#full-text-search-non-string-indexing-filters-name")
  - [Filter by property or predicate value type](full-text-search-non-string-indexing-filters.md#full-text-search-non-string-indexing-filters-datatype "full-text-search-non-string-indexing-filters.md#full-text-search-non-string-indexing-filters-datatype")

- [Mapping of SPARQL and Gremlin datatypes to OpenSearch](full-text-search-non-string-indexing-mapping.md "full-text-search-non-string-indexing-mapping.md")
- [Validation of data mappings](full-text-search-data-validation.md "full-text-search-data-validation.md")
- [Sample non-string OpenSearch queries in Neptune](full-text-search-non-string-examples.md "full-text-search-non-string-examples.md")
  - [Get all vertices with age greater than 30 and name starting with "Si"](full-text-search-non-string-examples.md#full-text-search-non-string-example-1 "full-text-search-non-string-examples.md#full-text-search-non-string-example-1")
  - [Get all nodes with age between 10 and 50 and a name with a fuzzy match with "Ronka"](full-text-search-non-string-examples.md#full-text-search-non-string-example-2 "full-text-search-non-string-examples.md#full-text-search-non-string-example-2")
  - [Get all nodes with a timestamp that falls within the last 25 days](full-text-search-non-string-examples.md#full-text-search-non-string-example-3 "full-text-search-non-string-examples.md#full-text-search-non-string-example-3")
  - [Get all nodes with a timestamp that falls within a given year and month](full-text-search-non-string-examples.md#full-text-search-non-string-example-4 "full-text-search-non-string-examples.md#full-text-search-non-string-example-4")
