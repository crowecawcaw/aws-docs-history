# Get compute capacity for SageMaker Training Jobs

Before you request compute capacity, confirm that your AWS account meets the following
prerequisites. Addressing these requirements in order helps you avoid common provisioning
failures.

## Step 1: Verify instance availability in your Region

Not all instance types are available in every AWS Region. Before selecting an instance
type for your training workload, verify that it is available in your target Region.

- To view instance availability and pricing per Region, see [SageMaker AI Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/"). Select the
  **Training** tab and choose your Region to see available instance types,
  specifications, and per-hour pricing.

If the instance type is not available in your Region:

- Choose an alternative instance type that is available in your Region. For
  GPU-accelerated training, identify instance families with comparable GPU memory and
  networking capabilities.
- If your workload requires a specific instance type and your data residency and
  compliance requirements allow it, consider running the training job in a different Region
  where that instance type is available. Ensure that your training data is accessible from
  the target Region, or plan for cross-Region data transfer.

### Verify instance availability per Availability Zone

Instance availability also varies by Availability Zone within a Region. An instance type
that is offered in your Region is not necessarily offered in every Availability Zone of that
Region. This matters when you run training jobs in a private VPC, because the subnets that
you specify determine which Availability Zones SageMaker AI can use to provision instances. For more
information, see [Step 3: Configure your VPC and subnets (optional)](#train-get-capacity-vpc "#train-get-capacity-vpc").

To list the Availability Zones that offer an instance type in a Region, use the Amazon Elastic Compute Cloud
`DescribeInstanceTypeOfferings` API:

```
aws ec2 describe-instance-type-offerings \
    --location-type availability-zone \
    --filters Name=instance-type,Values=p5.48xlarge \
    --region us-east-1 \
    --query 'InstanceTypeOfferings[].Location' \
    --output table
```

###### Note

Specify the Amazon Elastic Compute Cloud instance type (`p5.48xlarge`), not the SageMaker AI instance
type (`ml.p5.48xlarge`). SageMaker AI training instance types map to the equivalent
Amazon Elastic Compute Cloud instance type with the `ml.` prefix removed.

## Step 2: Check and request service quotas

Your AWS account has default quotas that limit the number of instances you can use
concurrently for SageMaker Training Jobs. Each instance type has its own quota.

- To view your current quotas, open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/sagemaker/quotas "https://console.aws.amazon.com/servicequotas/home/services/sagemaker/quotas") and
  filter for the instance type you plan to use.
- If your quota is insufficient for the number of instances your training job requires,
  request a quota increase. Quota increases are not immediate — submit your request in
  advance of your planned training run.

###### Tip

For Flexible Training Plans, your service quota must be equal to or greater than the
number of instances in your plan. For more information, see [View SageMaker training plans quotas using the AWS management console](training-plan-quotas.md "training-plan-quotas.md").

## Step 3: Configure your VPC and subnets (optional)

This step applies only if you run training jobs in a private VPC. By default, SageMaker
Training Jobs run in a SageMaker AI-managed network environment and do not require VPC configuration.
If your organization requires training jobs to access resources in a private VPC — for example,
data stored in Amazon S3 through a VPC endpoint, or file systems — you must specify
`Subnets` and `SecurityGroupIds` in the `VpcConfig`
parameter of the `CreateTrainingJob` API.

When you configure a VPC, the subnets you specify determine which Availability Zones SageMaker AI
can use to provision instances.

- **Provide subnets across multiple Availability Zones.**
  SageMaker AI provisions training instances from per-Availability-Zone capacity pools. Including
  subnets in more Availability Zones increases the capacity pool that SageMaker AI can draw from,
  which improves the likelihood of successful instance provisioning and reduces wait times.
  Specify subnets in at least three Availability Zones where possible.

SageMaker AI still launches all instances for a given job within a single subnet (a single
Availability Zone) to keep them physically close and minimize inter-node latency. The
additional subnets only broaden the options SageMaker AI can choose from. They do not spread one
job's instances across Availability Zones.

- **For Flexible Training Plans, align subnets with your Reserved
  Capacity.** Each Reserved Capacity block is provisioned in a specific
  Availability Zone. The `Subnets` in your `VpcConfig` must include
  the Availability Zones where your Reserved Capacity blocks are provisioned. For plans with
  multiple blocks that span different Availability Zones, include subnets in all relevant
  zones.
- **Align data sources with training instance Availability
  Zones.** If your training data resides in an Availability-Zone-specific storage
  service such as or Amazon EFS, verify that the file system is accessible from the same
  Availability Zones where your training instances will run.

## Choose a capacity option

### On-Demand Instances

On-Demand is the default capacity option for SageMaker Training Jobs. Instances are
provisioned when a training job starts and released when it completes. You pay per second of
compute, with no upfront commitment to run ad-hoc jobs. The required capacity for the jobs is
allocated on a best-effort basis, based on the availability in the Region during the
submission of the job.

If On-Demand capacity is not available for your requested instance type, the training
job enters a waiting state. You can configure the wait period from 2 hours to 28 days by
setting `MaxPendingTimeInSeconds`. If capacity does not become available within
that period, the job fails with an `InsufficientCapacityError`.

###### Tip

To preserve On-Demand capacity between consecutive training jobs, enable Managed Warm
Pools. Warm Pools retain provisioned instances after a job completes, so subsequent jobs
reuse the same instances without re-acquiring capacity. This is useful for iterative
workloads such as hyperparameter tuning or debugging distributed training.

### Managed Spot Training

Managed Spot Training uses spare Amazon EC2 Spot capacity at up to 90% cost savings compared
to On-Demand pricing. SageMaker AI manages the Spot lifecycle, including interruptions and automatic
restarts. With Spot Training, workloads can be subject to interruption, and checkpointing
strategies are recommended to resume jobs from the last saved state.

Spot capacity pools are defined per instance type and Availability Zone. To maximize Spot
availability, specify subnets across multiple Availability Zones in
`VpcConfig.Subnets`. Set `StoppingCondition.MaxWaitTimeInSeconds` to
control how long SageMaker AI waits for Spot capacity before stopping the job.

For more information, see [Managed Spot Training in Amazon SageMaker AI](model-managed-spot-training.md "model-managed-spot-training.md").

### Flexible Training Plans

Flexible Training Plans allow you to reserve GPU capacity in advance for a specific date
and duration. By reserving capacity, you get predictable access to high-demand GPU instance
types, plan and budget your training costs in advance, and benefit from automated resource
management and fault tolerance. Pricing depends on the instance type, number of instances,
reservation duration, and start date. To view pricing for your specific configuration, use
the `SearchTrainingPlanOfferings` API or the SageMaker AI console. For supported instance
types, see [Reserve Flexible Training Plans for ML workloads](reserve-capacity-with-training-plans.md "reserve-capacity-with-training-plans.md").

Before purchasing a plan, search for available training plan offerings from the SageMaker AI
console in your AWS account, or by using the `SearchTrainingPlanOfferings` API.
Available offerings include instance types, durations, pricing, and the Availability Zones
where capacity is provisioned.

###### Note

To search for and purchase Flexible Training Plans, your IAM identity must have the
appropriate permissions, including `sagemaker:SearchTrainingPlanOfferings` and
`sagemaker:CreateTrainingPlan`. For the full list of required actions, see
[Actions defined by
Amazon SageMaker](../../../service-authorization/latest/reference/list_amazonsagemaker.md "../../../service-authorization/latest/reference/list_amazonsagemaker.md").

###### Tip

If your training jobs run in a private VPC, each Reserved Capacity block is provisioned
in a specific Availability Zone. The `Subnets` in your `VpcConfig`
must include the Availability Zones where your Reserved Capacity blocks are provisioned.
For plans with multiple blocks that span different Availability Zones, include subnets in
all relevant zones.

Flexible Training Plans support a specific set of instance types and are available in
select AWS Regions. For supported configurations, see [Reserve Flexible Training Plans for ML workloads](reserve-capacity-with-training-plans.md "reserve-capacity-with-training-plans.md"). For pricing, see [SageMaker AI Pricing](https://aws.amazon.com/sagemaker/pricing/ "https://aws.amazon.com/sagemaker/pricing/").

###### Tip

For best practices on distributed training workloads with SageMaker Training Jobs,
see [Training large language models on Amazon SageMaker: Best practices](https://aws.amazon.com/blogs/machine-learning/training-large-language-models-on-amazon-sagemaker-best-practices/ "https://aws.amazon.com/blogs/machine-learning/training-large-language-models-on-amazon-sagemaker-best-practices/").
