#

Migrate from AWS Fargate to Amazon ECS Managed Instances

You can migrate existing workloads from Fargate to Amazon ECS Managed Instances. This migration
allows you to access the full range of Amazon EC2 instance types, capacity reservations, and
advanced capabilities while maintaining AWS-managed infrastructure.

## Migration considerations

Keep the following considerations in mind when migrating from Fargate to Amazon ECS Managed Instances:

Task compatibility

Existing task definitions configured for Fargate are mostly compatible with Amazon ECS Managed Instances. For more information about task definition differences, see [Amazon ECS task definition differences for
Amazon ECS Managed Instances](managed-instances-tasks-services.md "managed-instances-tasks-services.md").

Security model changes

Amazon ECS Managed Instances allows multiple tasks per instance by default. Consider enabling single-task mode if your workloads require stronger isolation.

Instance lifecycle

Amazon ECS Managed Instances have a maximum lifetime of 14 days. Plan for task replacement and use Amazon ECS services for automatic task management.

Pricing changes

With Amazon ECS Managed Instances, you pay for the entire instance plus a management fee, rather than per-task resources as with Fargate.

Maintenance windows

Configure maintenance windows using Amazon EC2 event windows to control when Amazon ECS Managed Instances are replaced for patching.

## Prerequisites

Before migrating to Amazon ECS Managed Instances, ensure you have:

- Existing Fargate tasks running on platform version 1.4.0 or later
- You have the required IAM roles for Amazon ECS Managed Instances. This includes:
  - **Infrastructure role** - Allows Amazon ECS to make
    calls to AWS services on your behalf to manage Amazon ECS Managed Instances
    infrastructure.

  For more information, see [Amazon ECS infrastructure IAM role](infrastructure_IAM_role.md "infrastructure_IAM_role.md").
  - **Instance profile** - Provides permissions for
    the Amazon ECS container agent and Docker daemon running on managed instances.

  For more information, see [Amazon ECS Managed Instances instance profile](managed-instances-instance-profile.md "managed-instances-instance-profile.md").

- Understanding of the security model differences between Fargate and Amazon ECS Managed Instances

###### Important

Amazon ECS Managed Instances uses a different security model than Fargate. By default,
multiple tasks can run on the same instance, which might expose tasks to
vulnerabilities from other tasks. Review your security requirements before
migrating.

## Step 1: Update the cluster to use Amazon ECS Managed Instances

Create a capacity provider. When you create a capacity provider with Amazon ECS Managed Instances, it becomes available only within the specified cluster.

For more information, see [Creating a capacity provider
for Amazon ECS Managed Instances](create-capacity-provider-managed-instances.md "create-capacity-provider-managed-instances.md").

## Step 2: Update the task definition to have the Amazon ECS Managed Instances capability

Update the task definition so that it has the requiresCapabilities for Amazon ECS Managed Instances.

For more information, see [Updating an Amazon ECS task definition using
the console](update-task-definition-console-v2.md "update-task-definition-console-v2.md").

## Step 3: Update the service to use the

Amazon ECS Managed Instances capacity provider

Update your existing Amazon ECS service to use the Amazon ECS Managed Instances capacity provider.

For more information, see [Updating an Amazon ECS service to use a capacity provider](update-service-managed-instances.md "update-service-managed-instances.md").

## Step 4: Migrate standalone tasks

For standalone tasks, specify the Amazon ECS Managed Instances capacity provider when running the task.

For more information, see [Running an application as an Amazon ECS task](standalone-task-create.md "standalone-task-create.md").
