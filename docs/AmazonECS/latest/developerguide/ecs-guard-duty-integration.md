# Identify unauthorized behavior using

Runtime Monitoring

Amazon GuardDuty is a threat detection service that helps protect your accounts, containers,
workloads, and the data within your AWS environment. Using machine learning (ML) models,
and anomaly and threat detection capabilities, GuardDuty continuously monitors different log
sources and runtime activity to identify and prioritize potential security risks and
malicious activities in your environment.

Runtime Monitoring in GuardDuty protects workloads running on Fargate and EC2 container instances
by continuously monitoring AWS log and networking activity to identify malicious or
unauthorized behavior. Runtime Monitoring uses a lightweight, fully managed GuardDuty security agent
that analyzes on-host behavior, such as file access, process execution, and network
connections. This covers issues including escalation of privileges, use of exposed
credentials, or communication with malicious IP addresses, domains, and the presence of
malware on your Amazon EC2 instances and container workloads. For more information, see [GuardDuty
Runtime Monitoring](../../../guardduty/latest/ug/runtime-monitoring.md "../../../guardduty/latest/ug/runtime-monitoring.md") in the _GuardDuty User Guide_.

Your security administrator enables Runtime Monitoring for a single or multiple accounts in
AWS Organizations for GuardDuty. They also select whether GuardDuty automatically deploys the GuardDuty security
agent when you use Fargate. All your clusters are automatically protected, and GuardDuty
manages the security agent on your behalf.

You can also manually configure the GuardDuty security agent in the following cases:

- You use EC2 container instances
- You need granular control to enable Runtime Monitoring at the cluster level
  To use Runtime Monitoring, you must configure the clusters that are protected, and install and
  manage the GuardDuty security agent on your EC2 container instances.

## How Runtime Monitoring works with Amazon ECS

Runtime Monitoring uses a lightweight GuardDuty security agent that monitors Amazon ECS workload activity for how applications are requesting, gaining access and consuming underlying system resources.

For Fargate tasks, the GuardDuty security agent runs as a sidecar container for each
task.

For EC2 container instances, the GuardDuty security agent runs as a process on the
instance.

The GuardDuty security agent collects data from the following resources, and then sends
the data to GuardDuty to process. You can view the findings in the GuardDuty console. You can
also send them to other AWS services such as AWS Security Hub, or a third-party security
vendor for aggregation and remediation. For information about how to view and manage
findings, see [Managing
Amazon GuardDuty findings](../../../guardduty/latest/ug/findings_management.md "../../../guardduty/latest/ug/findings_management.md") in the _Amazon GuardDuty User Guide_.

- Responses from the following Amazon ECS API calls:
  - [DescribeClusters](../APIReference/API_DescribeClusters.md "../APIReference/API_DescribeClusters.md")

  The response parameters include the Runtime Monitoring tag (when the tag is
  set) when you use the `--include TAGS` option.
  - [DescribeTasks](../APIReference/API_DescribeTasks.md "../APIReference/API_DescribeTasks.md")

  For Fargate, the response parameters include the
  GuardDuty sidecar container.
  - [ListAccountSettings](../APIReference/API_ListAccountSettings.md "../APIReference/API_ListAccountSettings.md")

  The response parameters include the Runtime Monitoring account setting, which
  is set by your security administrator.

- The container agent introspection data. For more information, see [Amazon ECS container introspection](ecs-agent-introspection.md "ecs-agent-introspection.md").
- The task metadata endpoint for the compute option:
  - [Amazon ECS task metadata endpoint version 4](task-metadata-endpoint-v4.md "task-metadata-endpoint-v4.md")
  - [Amazon ECS task metadata endpoint version 4 for
    tasks on Fargate](task-metadata-endpoint-v4-fargate.md "task-metadata-endpoint-v4-fargate.md")

## Considerations

Consider the following when using Runtime Monitoring:

- Runtime Monitoring has a cost associated with it. For more information, see [Amazon GuardDuty Pricing](https://aws.amazon.com/guardduty/pricing/ "https://aws.amazon.com/guardduty/pricing/").
- Runtime Monitoring is not supported on Amazon ECS Anywhere.
- Runtime Monitoring is not supported for the Windows operating system.
- When you use Amazon ECS Exec on Fargate, you must specify the container name
  because the GuardDuty security agent runs as a sidecar container.
- You cannot use Amazon ECS Exec on the GuardDuty security agent sidecar
  container.
- The IAM user that controls Runtime Monitoring at the cluster level, must have the
  appropriate IAM permissions for tagging. For more information, see [IAM tutorial: Define permissions to access AWS resources based on
  tags](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md") in the _IAM User
  Guide_.
- Fargate tasks must use a task execution role. This role grants the tasks
  permission to retrieve, update, and manage the GuardDuty security agent, which is
  stored in an Amazon ECR private repository, on your behalf.
- Runtime Monitoring is not supported for applications running on Amazon ECS Managed Instances.

## Resource utilization

The tag that you add to the cluster counts toward the cluster tag quota.

The GuardDuty agent sidecar container does not count toward the containers per task
definition quota.

As with most security software, there is a slight overhead for GuardDuty. For information
about the Fargate memory limits, see [CPU and memory limits](../../../guardduty/latest/ug/prereq-runtime-monitoring-ecs-support.md#ecs-runtime-agent-cpu-memory-limits "../../../guardduty/latest/ug/prereq-runtime-monitoring-ecs-support.md#ecs-runtime-agent-cpu-memory-limits") in the _GuardDuty User
Guide_. For information about the Amazon EC2 memory limits, see [CPU and memory limit for GuardDuty agent](../../../guardduty/latest/ug/prereq-runtime-monitoring-ec2-support.md#ec2-cpu-memory-limits-gdu-agent "../../../guardduty/latest/ug/prereq-runtime-monitoring-ec2-support.md#ec2-cpu-memory-limits-gdu-agent").
