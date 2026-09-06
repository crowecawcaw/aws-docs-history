

# Updating storage capacity dynamically
<a name="automate-storage-capacity-increase"></a>

You can use the following solution to dynamically increase the SSD storage capacity of an FSx for ONTAP file system when the amount of used SSD storage capacity exceeds a threshold that you specify. This AWS CloudFormation template automatically deploys all of the components that are required to define the storage capacity threshold, the Amazon CloudWatch alarm based on this threshold, and the AWS Lambda function that increases the file system’s storage capacity.

The solution automatically deploys all of the components needed, and uses the following parameters:
+ Your FSx for ONTAP file system ID.
+ The used SSD storage capacity threshold (numerical value). This is the percentage at which the CloudWatch alarm will be triggered.
+ The percentage by which to increase the storage capacity (%).
+ The email address used to receive scaling notifications.

**Topics**
+ [Architecture overview](#storage-inc-architecture)
+ [CloudFormation template](#storage-capacity-CFN-template)
+ [Automated deployment with CloudFormation](#fsx-dynamic-storage-increase-deployment)

## Architecture overview
<a name="storage-inc-architecture"></a>

Deploying this solution builds the following resources in the AWS Cloud.

![Architecture diagram of the solution to automatically increase the storage capacity of an FSx for ONTAP file system.](http://docs.aws.amazon.com/fsx/latest/ONTAPGuide/images/dynamic-storage-scaling-architecture.png)


The diagram illustrates the following steps:

1. The CloudFormation template deploys a CloudWatch alarm, an AWS Lambda function, an Amazon Simple Notification Service (Amazon SNS) queue, and all required AWS Identity and Access Management (IAM) roles. The IAM role gives the Lambda function permission to invoke the Amazon FSx API operations.

1. CloudWatch triggers an alarm when the file system’s used storage capacity exceeds the specified threshold, and sends a message to the Amazon SNS queue. An alarm is triggered only when the file system’s used capacity exceeds the threshold continuously for a 5-minute period.

1. The solution then triggers the Lambda function that is subscribed to this Amazon SNS topic.

1. The Lambda function calculates the new file system storage capacity based on the specified percent increase value and sets the new file system storage capacity.

1. The original CloudWatch alarm state and results of the Lambda function operations are sent to the Amazon SNS queue.

To receive notifications about the actions that are performed as a response to the CloudWatch alarm, you must confirm the Amazon SNS topic subscription by following the link provided in the **Subscription Confirmation** email.

## CloudFormation template
<a name="storage-capacity-CFN-template"></a>

This solution uses CloudFormation to automate deploying the components that are used to automatically increase the storage capacity of an FSx for ONTAP file system. To use this solution, download the [FSxOntapDynamicStorageScaling](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/samples/FSxOntapDynamicStorageScaling.zip) CloudFormation template.

The template adjusts the storage capacity increment based on the file system's recent usage growth rate rather than applying a fixed percentage on every alarm. Scheduler automatically retries storage scaling that the cooldown window blocks.

The template uses the **Parameters** described as follows. Review the template parameters and their default values, and modify them for the needs of your file system.



**FileSystemId**  
No default value. The ID of the file system for which you want to automatically increase the storage capacity.

**LowFreeDataStorageCapacityThreshold**  
No default value. Specifies the used storage capacity threshold at which to trigger an alarm and automatically increase the file system's storage capacity, specified in percentage (%) of the file system's current storage capacity. The file system is considered to have low free storage capacity when the used storage exceeds this threshold.

**EmailAddress**  
No default value. Specifies the email address to use for the SNS subscription and receives the storage capacity threshold alerts.

**LambdaS3Bucket**  
No default value. The name of the Amazon S3 bucket in your account that hosts the Lambda deployment package (`lambda_function.zip`) for the scaling function. You must upload the Lambda code to this bucket before you deploy the stack.

**LambdaS3Key**  
Default is **fsx/DynamicScaling/lambda\_function.zip**. The Amazon S3 object key of the Lambda deployment package within `LambdaS3Bucket`.

**PercentIncrease**  
Default is **20%** (allowed range **10%** to **100%**). Specifies the base percentage by which to increase the storage capacity, expressed as a percentage of the current storage capacity. When `EnableIntelligentScaling` is `true`, the template adjusts the increment up or down based on the file system's recent growth rate, and clamps the result to the value of `MaxIncrementPercent`.

**EnableIntelligentScaling**  
Default is **true**. When `true`, the Lambda function computes the storage growth rate from CloudWatch metrics and scales the increment up for fast-growing file systems and down for slow-growing ones. When `false`, the template applies the flat `PercentIncrease` value on every alarm.

**MaxIncrementPercent**  
Default is **100%** (allowed range **10%** to **500%**). Specifies the maximum percentage increment that intelligent scaling can apply. Adjusted increments are clamped between 10% and this value.

**GrowthThresholds**  
No default value. Optional JSON array of growth-rate tiers in the form `[[threshold_percent_per_day, multiplier, "label"], ...]` that overrides the built-in defaults that intelligent scaling uses. Leave empty to use the built-in tiers.

**MinHoursBetweenScaling**  
Default is **6** hours (allowed range **1** to **24**). Specifies the minimum time between two scaling operations on the same file system. Alarms that fire during the cooldown are deferred and retried automatically.

**MaxRetryAttempts**  
Default is **12** (allowed range **1** to **50**). Specifies the maximum number of retries when scaling is blocked by the cooldown window.

**RetryDelayMinutes**  
Default is **5** minutes (allowed range **1** to **60**). Specifies the delay between two consecutive retries.

**RetryBufferMinutes**  
Default is **5** minutes (allowed range **0** to **60**). Specifies the buffer time added after the cooldown expires before the first retry runs.

**ScheduleCleanupAgeDays**  
Default is **7** days (allowed range **1** to **30**). Specifies the age at which old Scheduler retry schedules are cleaned up.

## Automated deployment with CloudFormation
<a name="fsx-dynamic-storage-increase-deployment"></a>

The following procedure configures and deploys an CloudFormation stack to automatically increase the storage capacity of an FSx for ONTAP file system. It takes a few minutes to deploy. For more information about creating a CloudFormation stack, see [Creating a stack on the AWS CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) in the *AWS CloudFormation User Guide*.

**Note**  
Implementing this solution incurs billing for the associated AWS services. For more information, see the pricing details pages for those services.

Before you start, you must have the ID of the Amazon FSx file system that's running in the Amazon Virtual Private Cloud (Amazon VPC) in your AWS account. For more information about creating Amazon FSx resources, see [Getting started with Amazon FSx for NetApp ONTAP](getting-started.md).

You must also host the Lambda deployment package in an Amazon S3 bucket in your account before you deploy the stack. Download the [lambda\_function.zip](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/samples/lambda_function.zip) deployment package and upload it to your bucket without unpacking it. You provide the bucket name and object key to the stack by using the `LambdaS3Bucket` and `LambdaS3Key` parameters.

**To launch the automatic storage capacity increase solution stack**

1. Download the [FSxOntapDynamicStorageScaling](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/samples/FSxOntapDynamicStorageScaling.zip) CloudFormation template archive.
**Note**  
Amazon FSx is currently only available in specific AWS Regions. You must launch this solution in an AWS Region where Amazon FSx is available. For more information, see [Amazon FSx endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/fsxn.html) in the *AWS General Reference*.

1. Extract `FSxOntapDynamicStorageScaling.yaml` from the downloaded archive. You upload the extracted YAML template file to CloudFormation in the following steps.

1. From the CloudFormation console, choose **Create stack > With new resources**.

1. Choose **Template is ready**. In the **Specify template** section, choose **Upload a template file** and upload the template that you downloaded.

1. In **Specify stack details**, enter the values for your automatic storage capacity increase solution.  
![The values entered for the Specify stack details page for the CloudFormation template](http://docs.aws.amazon.com/fsx/latest/ONTAPGuide/images/dynamic-storage-capacity-increase-cfn-stack.png)

1. Enter a **Stack name**.

1. For **Parameters**, review the parameters for the template and modify them to meet the needs of your file system. Then choose **Next**.
**Note**  
To receive email notifications when scaling is attempted by this CloudFormation template, confirm the SNS subscription email that you receive after deploying the template.

1. Enter the **Options** settings that you want for your custom solution, and then choose **Next**.

1. For **Review**, review and confirm the solution settings. You must select the check box acknowledging that the template creates IAM resources.

1. Choose **Create** to deploy the stack.

You can view the status of the stack in the CloudFormation console in the **Status** column. You should see a status of **CREATE\_COMPLETE** in a few minutes.

### Updating the stack
<a name="automate-storage-capacity-increase-update"></a>

After the stack is created, you can update it by using the same template and providing new values for the parameters. For more information, see [Updating stacks directly](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-direct.html) in the *AWS CloudFormation User Guide*.