

# View costs by job in AWS billing with split cost allocation data

You can use AWS split cost allocation data for AWS PCS to get job-level cost visibility for your clusters that run Slurm. You can analyze, optimize, and charge back the cost of the Amazon EC2 CPU, memory, and GPU resources that your Slurm jobs request. You can attribute cost to an individual job and aggregate the cost by job, user, Slurm account, queue, compute node group, node, and cluster. For more information about split cost allocation data, see [Understanding split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html) in the *AWS Cost and Usage Report User Guide*.

When you opt in, AWS PCS activates the following job attributes automatically as cost allocation tags. You can analyze your cost allocation data using these tags:
+ `aws:pcs:cluster-name` is the ID of the AWS PCS cluster.
+ `aws:pcs:slurm-account` is the Slurm account that the job ran under.
+ `aws:pcs:slurm-job-id` is the Slurm job ID.
+ `aws:pcs:username` is the user who submitted the job.
+ `aws:pcs:queue` is the queue that the job ran in.
+ `aws:pcs:compute-node-group` is the compute node group that provided the node.
+ `aws:pcs:node-name` is the Slurm node name that ran the job.

**Contents**
+ [Prerequisites](#monitoring-cost-allocation_prerequisites)
+ [Set up Cost and Usage Reports](#monitoring-cost-allocation_setup)
+ [Region availability](#monitoring-cost-allocation_regions)
+ [How jobs appear in your cost data](#monitoring-cost-allocation_behaviors)
+ [Limitations](#monitoring-cost-allocation_limitations)

## Prerequisites
<a name="monitoring-cost-allocation_prerequisites"></a>

Your cluster must run Slurm 25.11 or later.

## Set up Cost and Usage Reports
<a name="monitoring-cost-allocation_setup"></a>

To get split cost allocation data for AWS PCS, complete the following steps.

1. Opt in to split cost allocation data for AWS PCS. For more information, see [Enabling split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/enabling-split-cost-allocation-data.html) in the *AWS Cost and Usage Report User Guide*.

1. Include the split cost allocation data in a new or existing report.

1. View the report. For a description of the split cost allocation columns, see [Split line item details](https://docs.aws.amazon.com/cur/latest/userguide/split-line-item-columns.html) in the *AWS Cost and Usage Report User Guide*.

## Region availability
<a name="monitoring-cost-allocation_regions"></a>

Split cost allocation data for AWS PCS is available in all AWS Regions where AWS PCS is available, except the AWS GovCloud (US) Regions. For the Regions where AWS PCS is available, see [Service endpoints](service-endpoints-quotas.md#service-endpoints-quotas_endpoints).

## How jobs appear in your cost data
<a name="monitoring-cost-allocation_behaviors"></a>

Note the following about how AWS PCS jobs appear in your cost data.
+ Costs are based on the resources that a job requests.
+ Time that a job spends suspended is not billed.
+ Split cost allocation data for AWS PCS covers usage starting November 17, 2026. A job that was already running then is billed from that date.
+ There is no minimum job duration.

## Limitations
<a name="monitoring-cost-allocation_limitations"></a>

AWS PCS doesn't currently support split cost allocation data in the following situations. When one occurs, AWS PCS doesn't produce split cost allocation data for the affected instance for any hour in which it occurs. The Amazon EC2 instance's cost for those hours appears in your Cost and Usage Report without job-level split line items.
+ You change MemSpecLimit, CpuSpecList, or RealMemory for a compute node group while jobs are running on it.
+ A suspended job resumes on CPUs that another job is now using.
+ Jobs that use the `--oversubscribe` option on a queue whose Slurm partition uses `OverSubscribe=YES` request more resources than the instance has. Split cost allocation data supports oversubscription only for partitions that use `OverSubscribe=FORCE`.

AWS PCS also doesn't currently support the following GPU configurations. Split cost allocation data is still produced, but the GPU cost appears as unused cost.
+ Multi-Instance GPU (MIG) is not currently supported. On an instance with MIG enabled on any GPU, all of the instance's GPU cost appears as unused cost.
+ GPU sharing is not currently supported. GPUs that jobs share through Slurm `shard` or `mps` resources, instead of requesting whole GPUs as `gpu` generic resources (GRES), appear as unused cost.