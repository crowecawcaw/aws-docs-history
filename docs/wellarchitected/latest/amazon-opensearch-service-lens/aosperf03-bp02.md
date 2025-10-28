# AOSPERF03-BP02 Evenly distribute data across data nodes in your

OpenSearch Service domain

Maintain efficient resource utilization and optimal query
performance by distributing data evenly across data nodes.

**Level of risk exposed if this best practice
is not established:** High

**Desired outcome**: Data is evenly
distributed across data nodes in the OpenSearch Service domain,
ensuring efficient resource utilization and optimal query
performance.

**Benefits of establishing this best
practice:**

- **Prevent bottlenecks and
  hotspots:** Evenly distributing data across data nodes
  in your OpenSearch Service domain helps prevent bottlenecks and
  hotspots, reducing the risk of node overload.
- **Improves availability:** When
  shards are distributed evenly across data nodes, can also help
  maintain high availability within your domain, as no single node
  will be overwhelmed with shards or storage, minimizing the risk
  of full node failure.

## Implementation guidance

_Node shard skew_ is when one or more nodes within a domain has
significantly more shards than the other nodes. _Node storage skew_
is when one or more nodes within a cluster has significantly more
storage (`disk.indices`) than the other nodes. While both conditions
can occur temporarily, like when a domain has replaced a node and
is still allocating shards to it, you should address them if they
persist because uneven distribution can lead to bottlenecks and
hotspots, causing queries to slow down or even fail. In some
cases, you can have a full node failure when it has a very high
density of shards compared to other nodes in the domain.

You need to identify node shard and index shard skewness, and use
shard counts that are multiples of the data node count to
distribute each index evenly across data nodes.

### Implementation steps

- Run the `GET _cat/allocation` API operation in OpenSearch Service to
  retrieve shard allocation information.
- Compare the `shards` and `disk.indices` entries in the response
  to identify skew.
- Note the average storage usage across all shards and nodes.
- Determine if storage skew is normal (within 10% of the
  average) or significant (over 10% above the average).
- Use shard counts that are multiples of the data node count
  to evenly distribute each index across data nodes. If you
  still see index storage or shard skew, you might need to
  force a shard reallocation, which occurs with every
  [blue/green
  deployment](../../../opensearch-service/latest/developerguide/managedomains-configuration-changes.md "../../../opensearch-service/latest/developerguide/managedomains-configuration-changes.md") of your OpenSearch Service domain.

## Resources

- [Node
  shard and storage skew](../../../opensearch-service/latest/developerguide/handling-errors.md#handling-errors-node-skew "../../../opensearch-service/latest/developerguide/handling-errors.md#handling-errors-node-skew")
- [Blue/Green
  Deployment](../../../opensearch-service/latest/developerguide/managedomains-configuration-changes.md "../../../opensearch-service/latest/developerguide/managedomains-configuration-changes.md")
