# AOSCOST01-BP03 Evaluate manager nodes

Improve domain stability, reduce risk of data loss, and prevent
over-provisioning by using an appropriate instance type for
dedicated leader nodes.

**Level of risk exposed if this best practice
is not established:** High

**Desired outcome**: The correct
instance type is used for dedicated leader nodes in OpenSearch Service to gain optimal resource utilization and performance.

**Benefits of establishing this best
practice:**

- Enhanced domain stability, as the leader role is handled by a
  dedicated node. This practice avoids unnecessary resource
  utilization and potential over-provisioning of data nodes.
- Reduced risk of data loss or corruption due to inadequate
  resource allocation or leader failure.

## Implementation guidance

Consider dedicated manager nodes size correlated with data node
instance sizes, number of instances, indexes, and shards they can
manage. For production clusters, we recommend, at a minimum, the
following instance types for dedicated leading nodes:

| Instance count | Manager node RAM size | Maximum supported shard count | Recommended minimum dedicated leader instance type |
| -------------- | --------------------- | ----------------------------- | -------------------------------------------------- |
| 1–10           | 8 GiB                 | 10K                           | m5.large.search or m6g.large.search                |
| 11–30          | 16 GiB                | 30K                           | c5.2xlarge.search or c6g.2xlarge.search            |
| 31–75          | 32 GiB                | 40K                           | r5.xlarge.search or r6g.xlarge.search              |
| 76–125         | 64 GiB                | 75K                           | r5.2xlarge.search or r6g.2xlarge.search            |
| 126–200        | 128 GiB               | 75K                           | r5.4xlarge.search or r6g.4xlarge.search            |

## Resources

- [Dedicated
  manager nodes in Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/managedomains-dedicatedmasternodes.md#dedicatedmasternodes-instance "../../../opensearch-service/latest/developerguide/managedomains-dedicatedmasternodes.md#dedicatedmasternodes-instance")
