

# Understanding split cost allocation data

Split cost allocation data splits the cost of a shared AWS resource across the workloads and resources that use it. The shared resource's own line item keeps its total usage and cost, and additional line items show how the usage and cost are allocated in your Cost and Usage Reports (AWS CUR).

For column definitions, see [Split line item details](https://docs.aws.amazon.com/cur/latest/userguide/split-line-item-columns.html) for legacy CUR and [Split line item columns](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-split-line-item.html) for CUR 2.0.

## Split cost allocation data for Amazon ECS, Amazon EKS, and AWS PCS
<a name="split-cost-allocation-data-containers"></a>

Using split cost allocation data, you can allocate your container costs to individual business units and teams, based on how your container workloads consume shared compute and memory resources. Split cost allocation data introduces cost and usage data for new container-level resources (that is, ECS tasks and Kubernetes pods) to AWS CUR. Previously, AWS CUR only supported costs at the EC2 instance level. Split cost allocation data generates container-level costs by looking at each container’s EC2 instance resource consumption, and generates cost based on the amortized cost of the instance and the percentage of CPU and memory resources consumed by the containers that ran on the instance.

You can also use split cost allocation data to allocate your AWS Parallel Computing Service (AWS PCS) costs to individual Slurm jobs that run on your AWS PCS clusters. For AWS PCS, the Slurm job is the split cost allocation sub-resource, and the EC2 instance is the parent resource. Split cost allocation data generates job-level costs based on the CPU, memory, and GPUs that each job requests on its EC2 instance.

For accelerated computing instances used with Amazon EKS, split cost allocation data includes resource allocation for specialized processors alongside CPU and memory. This covers NVIDIA and AMD GPUs, AWS Trainium, and AWS Inferentia accelerators. The feature is available for Amazon EKS and AWS PCS environments and provides pod-level (Amazon EKS) or job-level (AWS PCS) resource reservation data. For AWS PCS, this includes the GPUs that each Slurm job requests as `gpu` generic resources (GRES). This allows you to track and allocate costs for workloads that use these specialized processors, such as AI/ML applications and other computationally intensive tasks. For a current list of accelerated computing instances, see [Accelerated Computing](https://aws.amazon.com/ec2/instance-types/#Accelerated_Computing).

To receive split cost allocation data for containers, turn on Amazon ECS, Amazon EKS, or both in **Cost Management preferences**, and configure your legacy CUR or CUR 2.0 export to include split cost allocation data. For setup instructions, see [Enabling split cost allocation data](enabling-split-cost-allocation-data.md).

Split cost allocation data introduces new usage records and new cost metric columns for each containerized resource ID (that is, ECS task and Kubernetes pod) in AWS CUR. For more information, see [Split line item details](https://docs.aws.amazon.com/cur/latest/userguide/split-line-item-columns.html).

## Split cost allocation data for networking
<a name="split-cost-allocation-data-networking"></a>

For networking, split cost allocation data allocates supported NAT gateway, Amazon EC2 instance, and VPC peering connection charges to the resources that generated the usage. A networking flexible cost allocation policy specifies which charges to allocate and the reporting granularity, such as by Amazon EC2 instance, VPC, or AWS account. For policy setup and supported Regions, see [Allocate shared networking costs with networking flexible cost allocation](https://docs.aws.amazon.com/vpc/latest/userguide/networking-flexible-cost-allocation.html) in the *Amazon Virtual Private Cloud User Guide*.

To receive networking split cost allocation data, associate a networking flexible cost allocation policy with the resource and turn on showback. Select **Networking flexible cost allocation** in **Cost Management preferences**, and configure your legacy CUR or CUR 2.0 export to include split cost allocation data and resource IDs. For setup instructions, see [Enabling split cost allocation data](enabling-split-cost-allocation-data.md).

Split cost allocation data introduces new usage records for each resource that generated networking usage and for unattributed usage in AWS CUR. For more information, see [Example of split cost allocation data for networking](https://docs.aws.amazon.com/cur/latest/userguide/example-split-cost-allocation-data-networking.html) and [Split line item details](https://docs.aws.amazon.com/cur/latest/userguide/split-line-item-columns.html).

## Split cost allocation data for Amazon S3
<a name="split-cost-allocation-data-s3"></a>

For Amazon S3, split cost allocation data divides the storage and request charges of a general purpose bucket among the prefixes in that bucket. It allocates storage charges for all storage classes and Tier 1 and Tier 2 request charges.

Amazon S3 Storage Lens publishes prefix-level storage and request metrics to Billing and Cost Management, and you choose which buckets and prefix levels to publish in an S3 Storage Lens dashboard configuration. To receive this data, enable Billing and Cost Management publishing on an S3 Storage Lens advanced tier dashboard, select **Amazon S3** in **Cost Management preferences**, and configure your legacy CUR or CUR 2.0 export to include split cost allocation data and resource IDs. For setup instructions, see [Enabling split cost allocation data](enabling-split-cost-allocation-data.md).

Split cost allocation data introduces a usage record for each prefix that has usage and for unattributed usage in AWS CUR. For more information, see [Example of split cost allocation data for Amazon S3](https://docs.aws.amazon.com/cur/latest/userguide/example-split-cost-allocation-data-s3.html), and [Split line item details](https://docs.aws.amazon.com/cur/latest/userguide/split-line-item-columns.html) for legacy CUR and [Split line item columns](https://docs.aws.amazon.com/cur/latest/userguide/table-dictionary-cur2-split-line-item.html) for CUR 2.0.

## Cost allocation tags
<a name="split-cost-allocation-data-tags"></a>

**Note**  
For ECS: When it comes to AWS cost allocation tags, you can use Amazon ECS-managed tags or user-added tags for your Cost and Usage Reports. These tags apply to all new ECS split cost allocation data usage records. For more information, see [Tagging your ECS resources for billing](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-using-tags.html#tag-resources-for-billing).  
For EKS: Split cost allocation data creates new cost allocation tags for some Kubernetes attributes. These tags include `aws:eks:cluster-name`, `aws:eks:deployment`, `aws:eks:namespace`, `aws:eks:node`, `aws:eks:workload-name`, and `aws:eks:workload-type`.  
`aws:eks:cluster-name`, `aws:eks:namespace`, and `aws:eks:node` are populated retrospectively with the name of the cluster, namespace, and node.
`aws:eks:workload-type` is only populated if there is exactly one workload managing the pod, and is one of the built in workloads. Workload types include `ReplicaSet`, `StatefulSet`, `Job`, `DaemonSet`, or `ReplicationController`, and `aws:eks:workload-name` includes the name of the workload. For more information, see [Workloads](https://kubernetes.io/docs/concepts/workloads/) in the *Kubernetes Documentation*.
`aws:eks:deployment` is only populated for the workload type `ReplicaSet`. It is the deployment that creates a `ReplicaSet`.
These tags apply to all new EKS split cost allocation data usage records. These tags are enabled for cost allocation by default. If you previously used and disabled the `aws:eks:cluster-name` tag, then split cost allocation data keeps this setting and doesn't enable the tag. You can enable it from the [Cost allocation tags](https://console.aws.amazon.com/billing/home#/tags) console page.  
For networking: Split cost allocation data adds the following AWS-generated tags:  
`aws:networking-fca:allocated-account` identifies the AWS account that owns the resource that generated the usage. On the unattributed line item, its value is `(unattributed)`.
`aws:networking-fca:allocation-policy` identifies the allocation policy and version, for example `fcap-0123456789abcdef0:2`. On the unattributed line item, it's empty.
These tags apply to allocated and unattributed networking split cost allocation data usage records.  
For PCS: Split cost allocation data creates new cost allocation tags for some Slurm job attributes. These tags include `aws:pcs:cluster-name`, `aws:pcs:slurm-account`, `aws:pcs:slurm-job-id`, `aws:pcs:username`, `aws:pcs:queue`, `aws:pcs:compute-node-group`, and `aws:pcs:node-name`.  
`aws:pcs:cluster-name` is the ID of the AWS PCS cluster.
`aws:pcs:slurm-account` is the Slurm scheduler account, such as your organization, group, or project. It is not your AWS account.
`aws:pcs:slurm-job-id` is the Slurm job ID.
`aws:pcs:username` is the user who submitted the job.
`aws:pcs:queue` is the queue, or Slurm partition, that the job ran in.
`aws:pcs:compute-node-group` is the compute node group that provided the instance.
`aws:pcs:node-name` is the Slurm node name.
These tags apply to all new PCS split cost allocation data usage records. These tags are enabled for cost allocation by default. If you previously used and disabled one of these tag keys, then split cost allocation data keeps this setting and doesn't enable the tag. You can enable it from the [Cost allocation tags](https://console.aws.amazon.com/billing/home#/tags) console page.  
For Amazon S3: Split cost allocation data adds the following AWS-generated tags to prefix line items:  
`aws:s3:PrefixLevel1` through `aws:s3:PrefixLevel15` hold the segments of the prefix path through the deepest matched level. On the unattributed line item, `aws:s3:PrefixLevel1` is `(unattributed)`.
`aws:s3:BucketName` holds the bucket name.
These tags are inactive by default. To include them in your reports, activate them on the [Cost allocation tags](https://console.aws.amazon.com/billing/home#/tags) page in the Billing and Cost Management console. It can take up to 24 hours for activated tags to appear.

**Note**  
For PCS, split cost allocation data has the following behaviors:  
Costs are based on the resources that each job requests. The splitLineItem/ActualUsage column is empty for AWS PCS.
Multi-Instance GPU (MIG) is not currently supported. On an instance with MIG enabled on any GPU, all of the instance's GPU cost appears as unused cost.
GPU sharing is not currently supported. GPUs that jobs share through Slurm `shard` or `mps` resources, instead of requesting whole GPUs as `gpu` generic resources (GRES), appear as unused cost.
Suspended time is not billed.
Some AWS PCS cluster configurations aren't currently supported. For more information, see [Limitations](https://docs.aws.amazon.com/pcs/latest/userguide/monitoring-cost-allocation.html#monitoring-cost-allocation_limitations) in the *AWS PCS User Guide*.

## Estimating the number of line items
<a name="split-cost-allocation-data-estimating"></a>

When including split cost allocation data in AWS CUR, two new usage records are added for each ECS task and Kubernetes pod per hour, and for each Slurm job per instance per hour, in order to reflect the CPU and memory costs. To estimate the number of new line items in AWS CUR per day, use the following formula:

For ECS: `(number of tasks * average task lifetime * 2) * 24`

For EKS: `(number of pods * average pod lifetime * 2) * 24`

For PCS: `(number of jobs * average number of instances per job * average job lifetime * 2) * 24`

For example, if you have 1,000 pods running each hour across a cluster of 10 EC2 instances and the lifetime for the pod is less than 1 hour, then: 

`(1000 * 1 * 2) * 24 = 48,000 new usage records in AWS CUR`

For accelerated computing instances in Amazon EKS and AWS PCS, three new usage records are added per hour for each Kubernetes pod in Amazon EKS and for each Slurm job per instance in AWS PCS. These records reflect the accelerator, CPU, and memory costs. To estimate the number of new line items in AWS CUR per day, use the following formula:

For EKS with accelerated computing: `(number of pods * average pod lifetime * 3) * 24`

For PCS with accelerated computing: `(number of jobs * average number of instances per job * average job lifetime * 3) * 24`

For example, if you have 1,000 pods running each hour across a cluster of 10 EC2 instances and the lifetime for each pod is less than one hour, then: `(1000 * 1 * 3) * 24 = 72,000 new usage records in AWS CUR`

For each usage type and operation that the policy allocates on a shared networking resource, split cost allocation data adds one line item for each resource that generated usage.

To estimate the number of new line items in AWS CUR per day, use the following formula:

For networking: `(number of shared networking resources * number of usage types and operations the policy allocates per resource * number of resources that generated usage) * 24`

For example, if 200 instances use one NAT gateway and the policy allocates one usage type and operation for the gateway, the report adds `(1 * 1 * 200) * 24 = 4,800` line items per day. Reporting at a broader level, such as VPC or account, reduces the number of line items.

For Amazon S3, split cost allocation data adds daily prefix line items for storage and requests. To estimate the number of new line items that Amazon S3 adds to AWS CUR in a month, use the following formula:

For Amazon S3: `(number of prefixes with usage + 1) * number of usage types with usage (up to 2) * days in the month`

For example, a bucket with 2,000 prefixes at the deepest level in your range that has storage and request usage every day adds up to `(2,000 + 1) * 2 * 30 = 120,060` line items in a 30-day month. Prefix line items are daily, not hourly. A prefix with no usage of a type on a day has no line item for that type.