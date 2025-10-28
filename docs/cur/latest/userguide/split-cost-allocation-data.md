# Understanding split cost allocation

data

You can use Cost and Usage Reports (AWS CUR) to track your Amazon ECS and Amazon EKS container costs.
Using split cost allocation data, you can allocate your container costs to individual
business units and teams, based on how your container workloads consume shared compute
and memory resources. Split cost allocation data introduces cost and usage data for new
container-level resources (that is, ECS tasks and Kubernetes pods) to AWS CUR.
Previously, AWS CUR only supported costs at the EC2 instance level. Split cost
allocation data generates container-level costs by looking at each container’s EC2
instance resource consumption, and generates cost based on the amortized cost of the
instance and the percentage of CPU and memory resources consumed by the containers that
ran on the instance.

For accelerated computing instances used with Amazon EKS, split cost allocation data
includes resource allocation for specialized processors alongside CPU and memory. This
covers NVIDIA and AMD GPUs, AWS Trainium, and AWS Inferentia accelerators. The
feature is available only for Amazon EKS environments and provides pod-level resource
reservation data for these accelerated computing resources. This allows you to track and
allocate costs for workloads that use these specialized processors, such as AI/ML
applications and other computationally intensive tasks. For a current list of
accelerated computing instances, see [Accelerated
Computing](https://aws.amazon.com/ec2/instance-types/#Accelerated_Computing "https://aws.amazon.com/ec2/instance-types/#Accelerated_Computing").

Split cost allocation data introduces new usage records and new cost metric columns
for each containerized resource ID (that is, ECS task and Kubernetes pod) in AWS CUR.
For more information, see [Split line item
details](split-line-item-columns.md "split-line-item-columns.md").

When including split cost allocation data in AWS CUR, two new usage records are
added for each ECS task and Kubernetes pod per hour in order to reflect the CPU and
memory costs. To estimate the number of new line items in AWS CUR per day, use the
following formula:

For ECS: `(number of tasks * average task lifetime * 2) * 24`

For EKS: `(number of pods * average pod lifetime * 2) * 24`

For example, if you have 1,000 pods running each hour across a cluster of 10 EC2
instances and the lifetime for the pod is less than 1 hour, then:

`(1000 * 1 * 2) * 24 = 48,000 new usage records in AWS CUR`

For accelerated computing instances in Amazon EKS, three new usage records are added for
each Kubernetes pod per hour in order to reflect the accelerator, CPU, and memory costs.
To estimate the number of new line items in AWS CUR per day, use the following
formula:

For EKS with accelerated computing: `(number of pods _ average pod lifetime _ 3)

- 24`

For example, if you have 1,000 pods running each hour across a cluster of 10 EC2
instances and the lifetime for each pod is less than one hour, then: `(1000 * 1 *
 3) * 24 = 72,000 new usage records in AWS CUR`

###### Note

For ECS: When it comes to AWS cost allocation tags, you can use Amazon
ECS-managed tags or user-added tags for your Cost and Usage Reports. These tags apply to all
new ECS split cost allocation data usage records. For more information, see [Tagging your ECS resources for billing](../../../AmazonECS/latest/developerguide/ecs-using-tags.md#tag-resources-for-billing "../../../AmazonECS/latest/developerguide/ecs-using-tags.md#tag-resources-for-billing").

For EKS: Split cost allocation data creates new cost allocation tags for some
Kubernetes attributes. These tags include `aws:eks:cluster-name`,
`aws:eks:deployment`, `aws:eks:namespace`,
`aws:eks:node`, `aws:eks:workload-name`, and
`aws:eks:workload-type`.

- `aws:eks:cluster-name`, `aws:eks:namespace`, and `aws:eks:node` are populated retrospectively with the name of the cluster, namespace, and node.
- `aws:eks:workload-type` is only populated if there is exactly one workload managing the pod, and is one of the built in workloads. Workload types include `ReplicaSet`, `StatefulSet`, `Job`, `DaemonSet`, or `ReplicationController`, and `aws:eks:workload-name` includes the name of the workload. For more information, see [Workloads](https://kubernetes.io/docs/concepts/workloads/ "https://kubernetes.io/docs/concepts/workloads/") in the _Kubernetes Documentation_.
- `aws:eks:deployment` is only populated for the workload type `ReplicaSet`. It is the deployment that creates a `ReplicaSet`.
  These tags apply to all new EKS split cost allocation data usage records. These
  tags are enabled for cost allocation by default. If you previously used and disabled
  the `aws:eks:cluster-name` tag, then split cost allocation data keeps
  this setting and doesn't enable the tag. You can enable it from the [Cost allocation tags](https://console.aws.amazon.com/billing/home#/tags "https://console.aws.amazon.com/billing/home#/tags") console
  page.
