# AOSREL04-BP03 Enable index replication for your critical

indices

Provide high availability and improved performance in Amazon OpenSearch Service by enabling index replication for critical indices,
allowing replicas to handle read operations alongside primaries.
This setup maintains access to data and minimizes downtime in case
of primary shard unavailability.

**Level of risk exposed if this best practice
is not established:** High

**Desired outcome:** Your critical
indices are enabled with replication for improved availability.

**Benefits of establishing this best
practice:**

- **Improved performance:** Index
  replication for critical indices distributes read requests
  across the OpenSearch Service domain, improving performance and
  throughput by allowing replicas to handle read operations
  alongside primaries.
- **Enhanced data availability:**
  If a primary shard becomes unavailable, replicas can
  automatically take over, providing continued access to your data
  and minimizing downtime.

## Implementation guidance

For high-priority use cases, you can replicate critical indices in
real-time using index replication, which maintains an up to date
copy of your data. By doing this, you can distribute read requests
across your OpenSearch Service domain, improving performance and
throughput by allowing replicas to handle read operations
alongside primaries. Additionally, if a primary shard becomes
unavailable, replicas can automatically take over, providing
continued access to your data.

### Implementation steps

- To update the number of replicas for an existing index run
  the following:

```
PUT /my-index/_settings
          {
          "index" : {
          "number_of_replicas" : 2
          }
          }
```

- You can also use the auto_expand_replicas feature to
  dynamically adjust the number of replicas in your OpenSearch Service domain based on changes to the cluster, such as adding or
  removing data nodes. As a result, your replica count will
  match the number of data nodes you have at any specific
  moment.

###### Note

Adding multiple
replicas may not necessarily enhance performance; in some
cases, it can cause performance degradation. Therefore, use
this feature with caution, and thoroughly test its effects
before implementing it in your OpenSearch Service domain.

```
PUT /my-index/_settings
          {
          "index" : {
          "auto_expand_replicas" : "0-all"
          }
          }
```

## Resources

- [Update
  index settings](https://opensearch.org/docs/latest/api-reference/index-apis/update-settings/ "https://opensearch.org/docs/latest/api-reference/index-apis/update-settings/")
- [Create
  Index](https://opensearch.org/docs/latest/api-reference/index-apis/create-index/ "https://opensearch.org/docs/latest/api-reference/index-apis/create-index/")
