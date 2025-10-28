# AOSCOST01-BP02 Employ the appropriate instance type and

count

Improve query performance, enhance domain stability, and reduce risk
by selecting the appropriate instance type and count for your
workload.

**Level of risk exposed if this best practice
is not established**: High

**Desired outcome**: The correct
instance type and count is used for OpenSearch Service workloads for
optimal resource utilization and improved performance.

**Benefits of establishing this best
practice:**

- Improved query performance through optimized data retrieval
- Enhanced domain stability by avoiding unnecessary resource
  utilization and potential over-provisioning
- Reduced risk of data loss or corruption due to inadequate
  resource allocation

## Implementation guidance

Hardware requirements vary depending on the workload, with some
workloads requiring more memory and others more processing power.
OpenSearch is a CPU-intensive application that requires enough
vCPU cores for efficient handling, with indexing-heavy workloads
typically requiring more cores and searching or aggregating
workloads requiring fewer cores with higher clock speeds.

Your sharding strategy plays a significant role in determine the
instance type and count for your OpenSearch Service domain. For more
detail see [AOSPERF01](architecture-selection.md "architecture-selection.md"). The following summary explores the main
factors that impact your choice of the number of instances and the
instance type you need:

- **Review your shards:** A
  general guideline is to try to keep shard size between 10-30
  GiB for workloads where search latency is a key performance
  objective, and 30-50 GiB for write-heavy workloads such as log
  analytics. You can use `_cat/shards` to review shard size. For
  more detail, see
  [Choosing
  the number of shards](../../../opensearch-service/latest/developerguide/bp-sharding.md "../../../opensearch-service/latest/developerguide/bp-sharding.md")
- **Avoid shard skewness:** We
  recommended that you have a balanced shard distribution across
  your OpenSearch Service domain. Verify that the total number of shards
  is a multiple of the number of data nodes or that the total is
  divisible by the number of data nodes.
- **Shard to CPU ratio:** As a
  starting point, use a 1.5 multiplicator to calculate the ratio
  between shard number and CPUs in the domain. For example, if
  you have 10 shards, you will need 15 vCPUs in your OpenSearch Service domain. Another way to look at this is at data node level. For
  instance, if your data node instance has eight vCPUs, you
  should not have more than six shards on that node.
- **Search for suitable instance
  types:** For instances that align with your workload
  and financial requirements, see
  [Choosing
  instance types and testing](../../../opensearch-service/latest/developerguide/bp-instances.md "../../../opensearch-service/latest/developerguide/bp-instances.md").

## Resources

- [Sizing
  OpenSearch Service domains](../../../opensearch-service/latest/developerguide/sizing-domains.md "../../../opensearch-service/latest/developerguide/sizing-domains.md")
- [Choosing
  instance types and testing](../../../opensearch-service/latest/developerguide/bp-instances.md "../../../opensearch-service/latest/developerguide/bp-instances.md")
