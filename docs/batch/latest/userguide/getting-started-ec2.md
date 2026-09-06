

# Getting started with Amazon EC2 orchestration using the Wizard
<a name="getting-started-ec2"></a>

Amazon Elastic Compute Cloud (Amazon EC2) provides scalable computing capacity in the AWS Cloud. Using Amazon EC2 eliminates your need to invest in hardware up front, so you can develop and deploy applications faster. 

You can use Amazon EC2 to launch as many or as few virtual servers as you need, configure security and networking, and manage storage. Amazon EC2 enables you to scale up or down to handle changes in requirements or spikes in popularity, reducing your need to forecast traffic.

## Overview
<a name="getting-started-ec2-context"></a>

This tutorial demonstrates how to setup AWS Batch with the Wizard to configure Amazon EC2 and run `Hello World`. 

**Intended Audience**  
This tutorial is designed for system administrators and developers responsible for setting up, testing, and deploying AWS Batch.

**Features Used**  
This tutorial shows you how to use the AWS Batch console wizard to:  
+ Create and configure an Amazon EC2 compute environment
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
[See the AWS documentation website for more details](http://docs.aws.amazon.com/batch/latest/userguide/getting-started-ec2.html)

## Prerequisites
<a name="getting-started-ec2-prerequisite"></a>

Before you begin:
+ Create an AWS account if you don't have one.
+ Create the [`ecsInstanceRole` Instance role](batch-check-ecsinstancerole.md).

## Step 1: Create a compute environment
<a name="create-ce-1"></a>

**Important**  
To get started as simply and quickly as possible, this tutorial includes steps with default settings. Before creating for production use, we recommend that you familiarize yourself with all settings and deploy with the settings that meet your requirements.

To create a compute environment for an Amazon EC2 orchestration, do the following:

1. Open the [AWS Batch console first-run wizard](https://console.aws.amazon.com/batch/home#wizard).

1. For **Configure job and orchestration type**, choose **Amazon Elastic Compute Cloud(Amazon EC2)**.

1. Choose** Next**.

1. In the **Compute environment configuration** section for **Name**, specify a unique name for your compute environment. The name can be up to 128 characters in length. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_). 

1. For **Instance role**, choose an existing instance role that has the required IAM permissions attached. This instance role allows the Amazon ECS container instances in your compute environment to make calls to the required AWS API operations. For more information, see [Amazon ECS instance role](instance_IAM_role.md). 

   The default name of the **Instance role** is `ecsInstanceRole`. 

1. For **Instance configuration** you can leave the default settings.

1. For **Network configuration** use your default VPC for the AWS Region.

1. Choose **Next**.

## Step 2: Create a job queue
<a name="create-job-queue-1"></a>

A job queue stores your submitted jobs until the AWS Batch Scheduler runs the job on a resource in your compute environment. For more information, see [Job queues](job_queues.md)

To create a job queue for an Amazon EC2 orchestration, do the following:

1. For **Job queue configuration** for **Name**, specify a unique name for your job queue. The name can be up to 128 characters in length. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_). 

1. For all other configuration options you can leave the default value.

1. Choose **Next**.

## Step 3: Create a job definition
<a name="create-job-definition-1"></a>

AWS Batch job definitions specify how jobs are to be run. Even though each job must reference a job definition, many of the parameters that are specified in the job definition can be overridden at runtime. 

To create the job definition:

1. For **Create a job definition**

   1. for **Name**, specify a unique name for your job queue. The name can be up to 128 characters in length. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_).

   1. For **Command - *optional*** you can change `hello world` to a custom message or leave it as is.

1. For all other configuration options you can leave the default value.

1. Choose **Next**.

## Step 4: Create a job
<a name="create-job-1"></a>

To create a job, do the following:

1. In the **Job configuration** section for **Name**, specify a unique name for the job. The name can be up to 128 characters in length. It can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_).

1. For all other configuration options you can leave the default value.

1. Choose** Next**.

## Step 5: Review and create
<a name="review-create-1"></a>

On the **Review and create** page, review the configuration steps. If you need to make changes, choose **Edit**. When you're finished, choose **Create resources**.

1. For **Review and create** choose **Create resources**.

1. A window opens as AWS Batch starts to allocate your resources. Once complete choose **Go to dashboard**. On the dashboard you should see all of your allocated resources and that the job is in the `Runnable` state. Your job is scheduled to run and should complete in 2–3 minuets.

## Step 6: View the Job's output
<a name="view-job-1"></a>

To view the Job's output, do the following:

1. In the navigation pane choose **Jobs**. 

1. In the **Job queue** drop down choose the Job queue you created for the tutorial.

1. The **Jobs** table lists all of your Jobs and what their current status is. Once the Job's **Status** is **Succeeded** choose the **Name** of the Job to view the Job's details. 

1. In the **Details** pane choose **Log stream name**. The CloudWatch console for the Job will open and there should be one event with the **Message** of `hello world` or your custom message.

## Step 7: Clean up your tutorial resources
<a name="delete-1"></a>

You are charged for the Amazon EC2 instance while it is enabled. You can delete the instance to stop incurring charges.

To delete the resources you created, do the following:

1. In the navigation pane choose **Job queue**. 

1. In the **Job queue** table choose the Job queue you created for the tutorial.

1. Choose **Disable**. Once the Job queue **State** is Disabled you can choose **Delete**.

1. Once the Job queue is deleted, in the navigation pane choose **Compute environments**.

1. Choose the compute environment you created for this tutorial and then choose **Disable**. It may take 1–2 minuets for the compute environment to complete being disabled.

1. Once the compute environment’s **State** is Disabled, choose **Delete**. It may take 1–2 minuets for the compute environment to be deleted.

## Additional resources
<a name="procedure_additional_resources"></a>

After you complete the tutorial, you might want to explore the following topics::
+ Explore the AWS Batch core components. For more information, see [Components of AWS Batch](batch_components.md).
+ Learn more about the different [Compute Environments](compute_environments.md) available in AWS Batch.
+ Learn more about [Job queues](job_queues.md) and their different scheduling options.
+ Learn more about [Job definitions](job_definitions.md) and the different configuration options.
+ Learn more about the different types of [Jobs](jobs.md).