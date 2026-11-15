

# Limitations and notes for the Harness connector
<a name="harness-connector-limitations"></a>

The following are limitations and notes for the Harness connector:
+ Harness is supported as a source only. Writing to Harness is not supported.
+ The connector reads only the first page of each Harness entity, with a page size of 100. If an entity has more than 100 records, or more than 100 records match your filter, the connector doesn't read the remaining records. To stay within this limit, filter by `orgIdentifier` or `projectIdentifier` on the entities that support them.
+ The connector connects to Harness SaaS at `https://app.harness.io/gateway`. Harness Self-Managed Enterprise Edition installations are not supported.
+ Job bookmarks are not supported.