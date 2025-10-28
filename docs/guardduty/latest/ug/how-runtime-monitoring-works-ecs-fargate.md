# How Runtime Monitoring works with Fargate

(Amazon ECS only)

When you enable Runtime Monitoring, GuardDuty becomes ready to consume the runtime events from a task.
These tasks run within the Amazon ECS clusters, which in turn run on the AWS Fargate instances.
For GuardDuty to receive these runtime events, you must use the fully-managed, dedicated security
agent.

###### Note

Runtime Monitoring doesn't support applications running on [Amazon ECS Managed Instances](../../../AmazonECS/latest/developerguide/ManagedInstances.md "../../../AmazonECS/latest/developerguide/ManagedInstances.md").

You can allow GuardDuty to manage the GuardDuty security agent on your behalf, by using Automated
agent configuration for an AWS account or an organization. GuardDuty will start deploying the
security agent to the new Fargate tasks that are launched in your Amazon ECS clusters. The
following list specifies what to expect when you enable the GuardDuty security agent.

###### **Impact of enabling GuardDuty security agent**

**GuardDuty creates a virtual private cloud (VPC) endpoint and security
group**

- When you deploy the GuardDuty security agent, GuardDuty will create a VPC endpoint through
  which the security agent delivers the runtime events to GuardDuty.

Along with the VPC endpoint, GuardDuty also creates a new security group. The inbound
(ingress) rules control the traffic that's allowed to reach the resources, that are
associated with the security group. GuardDuty adds inbound rules that match the VPC CIDR range
for your resource, and also adapts to it when the CIDR range changes. For more information,
see [VPC CIDR
range](../../../vpc/latest/userguide/vpc-cidr-blocks.md "../../../vpc/latest/userguide/vpc-cidr-blocks.md") in the _Amazon VPC User Guide_.

- Working with centralized VPC with automated agent – When you use GuardDuty
  automated agent configuration for a resource type, GuardDuty will create a VPC endpoint on your
  behalf for all the VPCs. This includes the centralized VPC and spoke VPCs. GuardDuty
  doesn't support creating a VPC endpoint only for the centralized VPC. For more
  information about how the centralized VPC works, see [Interface VPC endpoints](../../../whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-access-to-vpc-private-endpoints.md#interface-vpc-endpoints "../../../whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/centralized-access-to-vpc-private-endpoints.md#interface-vpc-endpoints") in the _AWS Whitepaper - Building a Scalable
  and Secure Multi-VPC AWS Network Infrastructure_.
- There is no additional cost for the usage of the VPC endpoint.

**GuardDuty adds a sidecar container**

For a new Fargate task or service that starts running, a GuardDuty container (sidecar)
attaches itself to each container within the Amazon ECS Fargate task. The GuardDuty security agent
runs within the attached GuardDuty container. This helps GuardDuty to collect the runtime events of
each container running within these tasks.

The GuardDuty sidecar container image is stored in Amazon Elastic Container Registry (Amazon ECR),
with its image layers stored in Amazon S3. When your task starts, it needs to pull this
image from ECR. Depending on your network configuration, this may require specific settings
to ensure access to both ECR and S3. For example, if you're using security groups with
restricted access, you'll need to allow access to the
S3 managed prefix list. For more information on how to do this, see
[Prerequisites for container image access](prereq-runtime-monitoring-ecs-support.md#before-enable-runtime-monitoring-ecs "prereq-runtime-monitoring-ecs-support.md#before-enable-runtime-monitoring-ecs").

When you start a Fargate task, should the GuardDuty container (sidecar) be unable to
launch in a healthy state, Runtime Monitoring is designed to not prevent the tasks from running.

By default, a Fargate task is immutable. GuardDuty will not deploy the sidecar when a task
is already in a running state. If you want to monitor a container in an already running task,
you can stop the task and start it again.

## Approaches to manage

GuardDuty security agent in Amazon ECS-Fargate resources

Runtime Monitoring provides you the option to detect potential security threats on either all of the
Amazon ECS clusters (account level) or selective clusters (cluster level) in your account. When you
enable Automated agent configuration for each Amazon ECS Fargate task that will run, GuardDuty will
add a sidecar container for each container workload within that task. The GuardDuty security agent
gets deployed to this sidecar container. This is how GuardDuty gets visibility into the runtime
behavior of the containers inside the Amazon ECS tasks.

Runtime Monitoring supports managing the security agent for your Amazon ECS clusters (AWS Fargate) only through GuardDuty. There is
no support for managing the security agent manually on Amazon ECS clusters.

Before you configure your accounts, assess if you want to monitor the runtime behavior of
all the containers that belong to the Amazon ECS tasks, or include or exclude specific resources.
Consider the following approaches.

**Monitor for all Amazon ECS clusters**

This approach will help you detect potential security threats at account level. Use
this approach when you want GuardDuty to detect potential security threats for all the Amazon ECS
clusters that belong to your account.

**Exclude specific Amazon ECS clusters**

Use this approach when you want GuardDuty to detect potential security threats for most of
the Amazon ECS clusters in your AWS environment but exclude some of the clusters. This approach
helps you monitor the runtime behavior of the containers within your Amazon ECS tasks at the
cluster level. For example, the number of Amazon ECS clusters that belong to your account are 1000. However, you want to monitor only 930 Amazon ECS clusters.

This approach requires you to add a pre-defined GuardDuty tag to the Amazon ECS clusters that
you don't want to monitor. For more information, see [Managing automated security agent for
Fargate (Amazon ECS only)](managing-gdu-agent-ecs-automated.md "managing-gdu-agent-ecs-automated.md").

**Include specific Amazon ECS clusters**

Use this approach when you want GuardDuty to detect potential security threats for some of
the Amazon ECS clusters. This approach helps you monitor the runtime behavior of the containers
within your Amazon ECS tasks at the cluster level. For example, the number of Amazon ECS clusters that
belong to your account are 1000. However, you want to monitor 230 clusters only.

This approach requires you to add a pre-defined GuardDuty tag to the Amazon ECS clusters that
you want to monitor. For more information, see [Managing automated security agent for
Fargate (Amazon ECS only)](managing-gdu-agent-ecs-automated.md "managing-gdu-agent-ecs-automated.md").
