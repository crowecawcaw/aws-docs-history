# AOSPERF05-BP01 Enable a dedicated leader node for OpenSearch Service domain

Configure dedicated leader nodes with appropriate instance types to
improve cluster stability and performance. This separation of
cluster management tasks helps prevent split-brain scenarios and
optimizes resource utilization as your OpenSearch Service domain grows.

**Level of risk exposed if this best practice
is not established**: High

**Desired outcome**: Your OpenSearch Service domain has dedicated leader nodes with appropriately sized
instances to handle cluster management tasks. This configuration
improves cluster stability, prevents split-brain scenarios, and
maintains performance as your workload grows.

**Benefits of establishing this best
practice:**

- Improved cluster stability through isolated cluster management
  tasks
- Enhanced reliability by preventing split-brain scenarios and
  reducing election times
- Better resource utilization with workload separation from data
  nodes
- Increased scalability and performance as your domain grows
- Reduced risk of operational disruptions

## Implementation guidance

Dedicated manager nodes' size is directly tied to instance size,
number of instances, indexes, and shards they manage. For
production clusters, we recommend, at a minimum, the following
instance types for dedicated managing nodes.

| Instance count | Manager node RAM Size | Maximum supported shard count | Recommended minimum dedicated manager instance type |
| -------------- | --------------------- | ----------------------------- | --------------------------------------------------- |
| 1–10           | 8 GiB                 | 10K                           | m5.large.search or m6g.large.search                 |
| 11–30          | 16 GiB                | 30K                           | c5.2xlarge.search or c6g.2xlarge.search             |
| 31–75          | 32 GiB                | 40K                           | r5.xlarge.search or r6g.xlarge.search               |
| 76–125         | 64 GiB                | 75K                           | r5.2xlarge.search or r6g.2xlarge.search             |
| 126–200        | 128 GiB               | 75K                           | r5.4xlarge.search or r6g.4xlarge.search             |

### Implementation steps

- Log in to the
  [AWS Management Console](https://console.aws.amazon.com "https://console.aws.amazon.com").
- Navigate to the Amazon OpenSearch Service console.
- Create a new domain or modify an existing domain:
  - For a new domain, choose **Create domain**. For an existing domain, select the domain name and choose **Actions**, then **Edit cluster configuration**.

- Enable dedicated leader nodes:
  - In the Cluster configuration section, under Dedicated
    master nodes, toggle on the option to enable dedicated
    leader nodes.

- Choose leader node instance type and count:
  - **Instance type:** Select
    an instance type that fits the workload needs. For
    detailed information on choosing the right instance type
    for leader roles, see
    [AOSPERF05-BP02](aosperf05-bp02.md "aosperf05-bp02.md").
  - **Instance count:**
    Select three or five. Three is usually more than enough
    for the majority of workloads.

- After configuring the settings, review your setup and choose **Create** (for a new domain) or **Save changes** (for an existing domain).

## Resources

- For information about how certain configuration changes can
  affect dedicated leader nodes, see
  [Making
  configuration changes in Amazon OpenSearch Service.](../../../opensearch-service/latest/developerguide/managedomains-configuration-changes.md "../../../opensearch-service/latest/developerguide/managedomains-configuration-changes.md")
- [Learn
  how to add dedicated manager nodes in your OpenSearch Service
  domain](../../../opensearch-service/latest/developerguide/managedomains-dedicatedmasternodes.md "../../../opensearch-service/latest/developerguide/managedomains-dedicatedmasternodes.md")
- For clarification on instance count limits, see
  [OpenSearch Service domain and instance quotas](../../../general/latest/gr/opensearch-service.md#opensearch-limits-domain "../../../general/latest/gr/opensearch-service.md#opensearch-limits-domain").
- For more information about specific instance types, including
  vCPU, memory, and pricing, see
  [Amazon OpenSearch Service prices](https://aws.amazon.com/opensearch-service/pricing/ "https://aws.amazon.com/opensearch-service/pricing/").
