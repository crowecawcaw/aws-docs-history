# DRHCSUS03-BP02 Monitor both workload resource utilization and Amazon EC2 instance consumption to maximize the use of AWS Outpost resources and improve sustainability

Portable workloads can be migrated from AWS Regions onto unused or
underutilized compute resources on AWS Outposts to minimize energy
consumption and maximize the use of fixed AWS Outposts resources.

**Desired outcome:** Outpost
capacity is aligned to workload requirements and desired
resiliency objectives. If, over time, an Outpost becomes
underutilized, suitable workloads can be migrated from the Region
to use the Outpost's capacity (while maintaining capacity for
resiliency), reducing consumption in AWS Regions to support
sustainability objectives.

**Benefits of establishing this best
practice:** You can maximize utilization of your fixed,
underutilized AWS Outposts compute resources by migrating portable
workloads out of AWS Regions to minimize overall energy
consumption.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

AWS Outposts provide a long-term, fixed, and finite pool of
compute resources for addressing data residency and low latency
use cases. Because AWS Outposts capacity is both fixed and
purchased for terms spanning one to five years, it is critical
that it be used to the fullest extent possible.

Use services such as
[Amazon CloudWatch metrics](../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md "../../../AmazonCloudWatch/latest/monitoring/working_with_metrics.md") and
[AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/ "https://aws.amazon.com/compute-optimizer/") to monitor workload and instance
metrics such as CPU utilization, memory utilization, network
connections, and network throughput. Identify instances that
have been over-provisioned and adjust as necessary to match
instance type and size to the workload requirements. By matching
instance type and size to workload requirements, you can free
capacity on an Outpost to support workloads that would otherwise
be deployed in the parent Region, which provides maximum value
from the capacity already purchased on the Outpost.

When moving workloads to AWS Outposts, maintain spare capacity
to absorb workloads if hardware in the Outpost fails. An Amazon EC2 server to spare ratio of eight to one is commonly used when
planning for instance resiliency and potential hardware
failures.
