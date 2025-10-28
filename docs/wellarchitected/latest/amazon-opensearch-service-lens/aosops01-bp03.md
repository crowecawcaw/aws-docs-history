# AOSOPS01-BP03 Remove unused indexes

Regularly review and remove unused indexes to optimize your
OpenSearch Service domain's performance and reduce costs. Unused indexes,
even when inactive, continue to consume domain resources including
memory, CPU, and storage.

**Level of risk exposed if this best practice
is not established:** Medium

**Desired outcome:** Unused indexes
are removed to optimize performance and reduce costs.

**Benefits of establishing this best
practice:**

- **Improve query performance:**
  Removing unused indexes can help reduce the computational
  resources needed to manage your OpenSearch infrastructure,
  leading to improved query performance and faster search results.
- **Lower costs:** By reducing the
  number of indices that need to be managed, you can also lower
  costs associated with storing and processing data in Amazon OpenSearch Service.
- **Enhance domain efficiency:**
  Regularly reviewing and pruning unused indexes helps improve
  your OpenSearch Service domain efficiency, scalability, and
  cost-effectiveness, making it easier to manage and maintain your
  OpenSearch infrastructure.

## Implementation guidance

To optimize the performance and cost-effectiveness of your
OpenSearch Service domains, remove any unused indexes that are no
longer required. This can help reduce the computational resources
needed to manage your OpenSearch Service infrastructure, leading to
improved query performance and lower costs. By regularly reviewing
and pruning unused indexes, you improve your OpenSearch Service domain
efficiency, scalability, and cost-effectiveness.

### Implementation steps

- **Identify unused indexes:**
  Unused indexes are typically those that haven't been updated
  or queried for a specified period. To identify them, you can
  use OpenSearch Dashboards or the OpenSearch API.
- **Option 1:** Use OpenSearch
  Dashboards by going to Index Management, then Indexes,
  then Indexes.
- **Option 2:** Use the
  OpenSearch API:
  - Use the `_cat/indices` API to list all indexes along
    with their name, status and size.

```
GET _cat/indices?v
```

- Once you identify unneeded indices, delete them using the
  Dashboard or with the API command:

```
DELETE /<index_name
```

- You can also create an ISM policy to delete indexes after
  they reach a certain age. For details on how to create an
  ISM policy, see [AOSOPS01-BP01](aosops01-bp01.md "aosops01-bp01.md").

## Resources

- [Delete
  index](https://opensearch.org/docs/latest/api-reference/index-apis/delete-index/ "https://opensearch.org/docs/latest/api-reference/index-apis/delete-index/")
