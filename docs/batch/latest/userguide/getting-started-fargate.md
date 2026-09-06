

# Getting started with AWS Batch and Fargate orchestration using the Wizard
<a name="getting-started-fargate"></a>

AWS Fargate launches and scales the compute to closely match the resource requirements that you specify for the container. With Fargate, you don't need to over-provision or pay for additional servers. For more information, see [Fargate](https://docs.aws.amazon.com/batch/latest/userguide/fargate.html#when-to-use-fargate).

## Overview
<a name="getting-started-fargate-contextual"></a>

This tutorial demonstrates how to setup AWS Batch with the Wizard to configure AWS Fargate and run `Hello World`. 

**Intended Audience**  
This tutorial is designed for system administrators and developers responsible for setting up, testing, and deploying AWS Batch.

**Features Used**  
This tutorial shows you how to use the AWS Batch console wizard to:  
+ Create and configure an AWS Fargate compute environment
+ Create a job queue.
+ Create a job definition
+ Create and submit a job to run
+ View the output of the job in CloudWatch

**Time Required**  
It should take about 10–15 minutes to complete this tutorial.

**Regional Restrictions**  
There are no country or regional restrictions associated with using this solution.

**Resource Usage Costs**  
There's no charge for creating an AWS account. However, by implementing this solution, you might incur some or all of the costs that are listed in the following table.      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/batch/latest/userguide/getting-started-fargate.html)

## Prerequisites
<a name="getting-started-fargate-prerequisite"></a>

Before you begin: 
+ Create an AWS account if you don't have one.
+ Create the task execution role. If you haven't already created the [Task Execution Role](create-execution-role.md) then you can create it as part of this tutorial.

## Step 1: Create a compute environment
<a name="create-ce-2"></a>

**Important**  
To get started as simply and quickly as possible, this tutorial includes steps with default settings. Before creating for production use, we recommend that you familiarize yourself with all settings and deploy with the settings that meet your requirements.

To create a compute environment for a Fargate orchestration, do the following:

1. Open the [AWS Batch console first-run wizard](https://console.aws.amazon.com/batch/home#wizard).

1. For **Configure job and orchestration type**, choose **Fargate**.

1. Choose** Next**.

1. In the **Compute environment configuration** section for **Name**, specify a unique name for your compute environment. The name can be up to 128 characters in length. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_).

1. For all other configuration options you can leave the default value.

1. Choose **Next**.

## Step 2: Create a job queue
<a name="create-job-queue-2"></a>

A job queue stores your submitted jobs until the AWS Batch Scheduler runs the job on a resource in your compute environment. To create a job queue:

To create a job queue for a Fargate orchestration, do the following:

1. In the **Job queue configuration** section for **Name**, specify a unique name for your job queue. The name can be up to 128 characters in length. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_).

1. For **Priority**, enter 900 for the job queue. 

1. For all other configuration options you can leave the default value.

1. Choose **Next**.

## Step 3: Create a job definition
<a name="create-job-definition-2"></a>

To create the job definition:

1. In the **General configuration** section:

   1. In the **General configuration** section for **Name**, specify a unique name for your job definition. The name can be up to 128 characters in length. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_).

1. In the **Fargate platform configuration** section:

   1. Turn on **Assign public IP** to assign a public IP address. You need a public IP to download the container image unless you've setup a private image repository.

   1. For **Execution role**, choose a task execution role that lets Amazon Elastic Container Service (Amazon ECS) agents make AWS calls on your behalf. Choose either **ecsTaskExecutionRole** or **BatchEcsTaskExecutionRole**. 

      To create the **Execution role** choose **Create an execution role**. In the **Create IAM role** modal choose **Create IAM role**. 

      1. The IAM console has the permission setting already configured for creating the execution role. 

      1. For **Trusted entity type** verify that **AWS service** is selected.

      1. For **Service or user case** verify that **Elastic Container Service** is selected.

      1. Choose **Next**.

      1. For **Permissions policies** verify that **AmazonECSTaskExecutionRolePolicy** is selected.

      1. Choose **Next**.

      1. For **Name, review, and create** verify that the role name is **BatchEcsTaskExecutionRole**. 

      1. Choose **Create role**.

      1. In the AWS Batch console choose the refresh button next to **Execution role**. Choose the **BatchEcsTaskExecutionRole** execution role.

1. In the **Container configuration** section:

   1. For **Command**, you can change `hello world` to a custom message or leave it as is.

1. For all other configuration options you can leave the default value.

1. Choose **Next**.

## Step 4: Create a job
<a name="create-job-2"></a>

To create a Fargate job, do the following:

1. In the **Job configuration** section for **Name**, specify a unique name for the job. The name can be up to 128 characters in length. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_).

1. For all other configuration options you can leave the default value.

1. Choose** Next**.

## Step 5: Review and create
<a name="review-create-2"></a>

On the **Review and create** page, review the configuration steps. If you need to make changes, choose **Edit**. When you're finished, choose **Create resources**.

## Step 6: View the Job's output
<a name="view-job-fargate"></a>

To view the Job's output, do the following:

1. In the navigation pane choose **Jobs**. 

1. In the **Job queue** drop down choose the Job queue you created for the tutorial.

1. The **Jobs** table lists all of your Jobs and what their current status is. Once the Job's **Status** is **Succeeded** choose the **Name** of the Job to view the Job's details. 

1. In the **Details** pane choose **Log stream name**. The CloudWatch console for the Job will open and there should be one event with the **Message** of `hello world` or your custom message.

## Step 7: Clean up your tutorial resources
<a name="delete-fargate"></a>

You are charged for the Amazon EC2 instance while it is enabled. You can delete the instance to stop incurring charges.

To delete the resources you created, do the following:

1. In the navigation pane choose **Job queue**. 

1. In the **Job queue** table choose the Job queue you created for the tutorial.

1. Choose **Disable**. Once the Job queue **State** is Disabled you can choose **Delete**.

1. Once the Job queue is deleted, in the navigation pane choose **Compute environments**.

1. Choose the compute environment you created for this tutorial and then choose **Disable**. It may take 1–2 minuets for the compute environment to complete being disabled.

1. Once the compute environment’s **State** is Disabled, choose **Delete**. It may take 1–2 minuets for the compute environment to be deleted.

## Additional resources
<a name="fargate-additional-resources"></a>

After you complete the tutorial, you might want to explore the following topics::
+ Learn more about the [Best practices](best-practices.md).
+ Explore the AWS Batch core components. For more information, see [Components of AWS Batch](batch_components.md).
+ Learn more about the different [Compute Environments](compute_environments.md) available in AWS Batch.
+ Learn more about [Job queues](job_queues.md) and their different scheduling options.
+ Learn more about [Job definitions](job_definitions.md) and the different configuration options.
+ Learn more about the different types of [Jobs](jobs.md).