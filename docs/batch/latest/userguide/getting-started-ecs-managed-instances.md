# Getting started with AWS Batch and Amazon ECS Managed Instances using the wizard

Amazon ECS Managed Instances provides fully managed Amazon EC2 capacity with broader compute
flexibility than Fargate, including GPU instances, bare metal, and arbitrary vCPU/memory
combinations. Amazon ECS handles instance provisioning, scaling, and termination on your behalf. For
more information, see [Amazon ECS Managed Instances compute environments](ecs_managed_instances.md "ecs_managed_instances.md").

## Overview

This tutorial demonstrates how to set up AWS Batch with the wizard to configure Amazon ECS Managed
Instances and run `Hello World`.

**Intended Audience**

This tutorial is for you if you set up, test, or deploy AWS Batch
workloads.

**Features Used**

This tutorial shows you how to use the AWS Batch console wizard to:

- Create and configure an Amazon ECS Managed Instances compute environment
- Create a job queue
- Create a job definition
- Create and submit a job to run
- View the output of the job in CloudWatch

**Time Required**

It should take about 10–15 minutes to complete this tutorial.

**Regional Restrictions**

There are no country or regional restrictions associated with using this
solution.

**Resource Usage Costs**

There's no charge for creating an AWS account. However, by implementing this
solution, you might incur some or all of the costs that are listed in the following
table.

| Description                                                                                                                                                                                    | Cost (US dollars)                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Pricing is based on the Amazon EC2 instance types launched by Amazon ECS Managed<br>Instances. You are charged standard Amazon EC2 On-Demand or Spot pricing for the<br>instances provisioned. | For more information about pricing, see [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/"). |

## Prerequisites

Before you begin:

- Create an AWS account if you don't have one.
- Create an Amazon ECS infrastructure role — an IAM role with a trust policy for
  `ecs.amazonaws.com`. For more information, see [Amazon ECS infrastructure
  IAM role](../../../AmazonECS/latest/developerguide/infrastructure-iam-roles.md "../../../AmazonECS/latest/developerguide/infrastructure-iam-roles.md") in the _Amazon Elastic Container Service Developer Guide_.
- Create an Amazon EC2 instance profile that uses the
  `AmazonECSInstanceRolePolicyForManagedInstances` managed policy with a trust
  policy for `ec2.amazonaws.com`.
- Your IAM principal must have `iam:PassRole` permission for the
  infrastructure role with the condition `iam:PassedToService:
 ecs.amazonaws.com`.
- A VPC with subnets that have outbound internet access (either public IP assignment or a
  NAT gateway).
- Create an Amazon ECS task execution role — an IAM role with the
  `AmazonECSTaskExecutionRolePolicy` managed policy and a trust policy for
  `ecs-tasks.amazonaws.com`. This role allows Amazon ECS agents to make AWS calls on
  your behalf, such as pulling container images from Amazon ECR. For more information, see [Amazon ECS task execution
  IAM role](../../../AmazonECS/latest/developerguide/task_execution_IAM_role.md "../../../AmazonECS/latest/developerguide/task_execution_IAM_role.md") in the _Amazon Elastic Container Service Developer Guide_.

## Step 1: Create a compute environment

###### Important

To get started as simply and quickly as possible, this tutorial includes steps with
default settings. Before creating for production use, we recommend that you familiarize
yourself with all settings. Deploy with the settings that meet your requirements.

To create a compute environment for Amazon ECS Managed Instances, do the following:

1. Open the [AWS Batch console first-run
   wizard](https://console.aws.amazon.com/batch/home#wizard "https://console.aws.amazon.com/batch/home#wizard").
2. For **Configure job and orchestration type**, choose **ECS
   Managed Instances**.
3. Choose **Next**.
4. In the **Compute environment configuration** section for
   **Name**, specify a unique name for your compute environment. The name can
   be up to 128 characters in length. It can contain uppercase and lowercase letters, numbers,
   hyphens (-), and underscores (\_).
5. For **Infrastructure role**, choose the Amazon ECS infrastructure role you
   created in the prerequisites.
6. For **Instance profile**, choose the Amazon EC2 instance profile you
   created in the prerequisites.
7. For **Maximum vCPUs**, enter the maximum number of vCPUs that the
   compute environment can scale to. The default is 256.
8. For **Subnets**, choose one or more subnets where Amazon ECS launches
   managed instances. The subnets must have outbound internet access (either public IP
   assignment or a NAT gateway).
9. For **Security groups**, choose one or more security groups to
   associate with the managed instances.
10. ###### Note

For all other configuration options, you can leave the default values.

Choose **Next**.

## Step 2: Create a job queue

A job queue stores your submitted jobs until the AWS Batch Scheduler runs the job on a
resource in your compute environment. To create a job queue:

1. In the **Job queue configuration** section for
   **Name**, specify a unique name for your job queue. The name can be up to
   128 characters in length. It can contain uppercase and lowercase letters, numbers, hyphens
   (-), and underscores (\_).
2. For **Priority**, enter 900 for the job queue.
3. ###### Note

For all other configuration options, you can leave the default values.

Choose **Next**.

## Step 3: Create a job definition

To create the job definition:

1. In the **General configuration** section:

   1. For **Name**, specify a unique name for your job definition. The
      name can be up to 128 characters in length. It can contain uppercase and lowercase
      letters, numbers, hyphens (-), and underscores (\_).

2. In the **Container configuration** section:

   1. For **Image**, leave the default
      `public.ecr.aws/amazonlinux/amazonlinux:2023` image or specify your own
      container image.
   2. For **Command**, you can change `hello world` to a
      custom message or leave it as is.
   3. For **vCPUs**, specify the number of vCPUs for the container. The
      default is 1.
   4. For **Memory**, specify the amount of memory (in MiB) for the
      container. The default is 2048.

3. For **Execution role**, choose a task execution role that lets Amazon ECS
   agents make AWS calls on your behalf, such as pulling container images from Amazon ECR.
4. ###### Note

For all other configuration options, you can leave the default values.

Choose **Next**.

## Step 4: Create a job

To create a job, do the following:

1. In the **Job configuration** section for **Name**,
   specify a unique name for the job. The name can be up to 128 characters in length. It can
   contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_).
2. ###### Note

For all other configuration options, you can leave the default values.

Choose **Next**.

## Step 5: Review and create

On the **Review and create** page, review the configuration
steps. If you need to make changes, choose **Edit**. When you're
finished, choose **Create resources**.

## Step 6: View the job's output

To view the job's output, do the following:

1. In the navigation pane choose **Jobs**.
2. In the **Job queue** drop down choose the job queue you created for
   the tutorial.
3. The **Jobs** table lists all of your jobs and their current status.
   After the job's **Status** is **Succeeded**, choose the
   **Name** of the job to view its details.
4. In the **Details** pane choose **Log stream name**.
   The CloudWatch console for the job will open and there should be one event with the
   **Message** of `hello world` or your custom message.

###### Note

Amazon ECS Managed Instances might take a few minutes to provision capacity when launching
instances for the first time. This is expected behavior — subsequent jobs typically
start faster when instances are already available.

## Step 7: Clean up your tutorial resources

You are charged for the Amazon EC2 instances while they are running. You can delete the
resources to stop incurring charges.

To delete the resources you created, do the following:

1. In the navigation pane choose **Job queue**.
2. In the **Job queue** table choose the job queue you created for the
   tutorial.
3. Choose **Disable**. After the job queue **State** is
   Disabled you can choose **Delete**.
4. After the job queue is deleted, in the navigation pane choose **Compute
   environments**.
5. Choose the compute environment you created for this tutorial and then choose
   **Disable**. It might take 1–2 minutes for the compute environment to
   complete being disabled.
6. After the compute environment's **State** is Disabled, choose
   **Delete**. It might take 1–2 minutes for the compute environment to
   be deleted.

## Additional resources

After you complete the tutorial, you might want to explore the following topics:

- Learn more about [Amazon ECS Managed Instances compute environments](ecs_managed_instances.md "ecs_managed_instances.md").
- Learn more about the [Best practices](best-practices.md "best-practices.md").
- Explore the AWS Batch core components. For more information, see [Components of AWS Batch](batch_components.md "batch_components.md").
- Learn more about the different [Compute
  Environments](compute_environments.md "compute_environments.md") available in AWS Batch.
- Learn more about [Job queues](job_queues.md "job_queues.md") and their different
  scheduling options.
- Learn more about [Job definitions](job_definitions.md "job_definitions.md") and the
  different configuration options.
