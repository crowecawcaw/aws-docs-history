# Configuration notes

As shared in the previous section, there are different options and a non-exhaustive list
of tools that you can choose from to implement an operational analytics pipeline. A list of
configuration parameters to take into consideration for a well-architected operational
pipeline is provided.

**Define operational goals and business requirements:** As a best
practice, you should always start by identifying your operational goals, and what business
outcome you must reach. Think about who are your end users, what are the insights to help
drive their decisions, and how they will access these insights. After you define the business
requirements, you can start designing your technical pipeline, establishing the integration
options in your environment, and reviewing the skill sets you have, to choose the right
option.

**Choose a data model before ingestion:** When bringing data in
from disparate sources, especially from structured systems into structureless systems such as
OpenSearch, special care must be taken to ensure that the chosen data model provides a
frictionless search experience for users.

**Ingestion pipeline:** You should make sure that your ingestion
framework is reusable and extensible to be able to scale and include new use cases on the long
term, otherwise, check which parts of your infrastructure would require modernization. 

**Production ready tools and services:** AWS offers a set of
managed services that are production ready and which eliminate the operational overhead of
managing the infrastructure, such as Amazon OpenSearch Service. As shared in the reference architecture, you
can also integrate open source tools, such as OpenSearch Data Prepper, to transform and
aggregate the operational data for downstream analytics and visualizations.

**Sizing OpenSearch domain:** The first step in sizing an
OpenSearch cluster is to check your data size, and identify your storage and query
requirements. Estimate the number of active shards you will have per index based on your input
data, and the shard size that you identify. Then, estimate your vCPU requirements and choose
the type of instances that will be able to handle both storage and vCPUs. Plan for time to
benchmark the domain with a realistic dataset using [OpenSearch
Benchmark](https://github.com/opensearch-project/opensearch-benchmark "https://github.com/opensearch-project/opensearch-benchmark"), tune the configuration and iterate until you meet the performances
required in terms of Throughout, Search Latency, and Index Latency. For more information, see
[Sizing Amazon OpenSearch Service
domains](../../../opensearch-service/latest/developerguide/sizing-domains.md "../../../opensearch-service/latest/developerguide/sizing-domains.md") and [Best practices for configuring your Amazon OpenSearch Service domain](https://aws.amazon.com/blogs/big-data/best-practices-for-configuring-your-amazon-opensearch-service-domain/ "https://aws.amazon.com/blogs/big-data/best-practices-for-configuring-your-amazon-opensearch-service-domain/").

**Use tiered storage:** The value of operational data or any
timestamped data generally decreases with the age of the data. Moving aged data into tiered
storage can save significant operational cost. Summarized rollups that can condense the data
can also help address storage cost.

**Performance:** There are multiple parameters to consider when
thinking about performance and it is always specific to each workload. However, Amazon OpenSearch Service
offers features that you can already enable in your domain, such as [Auto-Tune](../../../opensearch-service/latest/developerguide/auto-tune.md "../../../opensearch-service/latest/developerguide/auto-tune.md") that automatically deploys optional changes to improve cluster speed and
stability. Other items to take into consideration include using the `_bulk` API to
load data into OpenSearch, and only indexing data fields that need be searchable.

**Define security requirements:** Make sure to set up your domain
inside a virtual Private Cloud (VPC) to secure the traffic to your domain. Apply the least
privilege access approach with restrictive access policies, or with fine-grained access
control for OpenSearch dashboards. OpenSearch Service also offers encryption of data at rest and in
transit.

**Monitor all involved components:** Monitor all involved
components with metrics in Amazon CloudWatch. With the CloudWatch metrics available for Amazon OpenSearch Service, you can
monitor the overall cluster health, you can also check the performance of individuals nodes
and monitor EBS volume metrics. It is also a best practice to set [CloudWatch alarms](../../../opensearch-service/latest/developerguide/cloudwatch-alarms.md "../../../opensearch-service/latest/developerguide/cloudwatch-alarms.md")to
get notified about any issues that your production domain encounters. You can start by setting
the following alarms:

- `CPUUtilization` maximum is >= 80% for 15 minutes, 3 consecutive times
- `ClusterStatus.yellow` maximum is >= 1 for 1 minute, 1 consecutive time
- `JVMMemoryPressure` maximum is >= 80% for 5 minutes, 3 consecutive times
- `FreeStorageSpace` minimum is <= 25% of the storage space for 1 minute, 1
  consecutive time
