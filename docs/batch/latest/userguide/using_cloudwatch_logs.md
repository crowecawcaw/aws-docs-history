

# Using CloudWatch Logs with AWS Batch
<a name="using_cloudwatch_logs"></a>

You can configure your AWS Batch jobs on EC2 resources to send detailed log information and metrics to CloudWatch Logs. Doing this, you can view different logs from your jobs in one convenient location. For more information about CloudWatch Logs, see [What is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchLogs.html) in the *Amazon CloudWatch User Guide*.

**Note**  
By default, CloudWatch Logs is turned on for AWS Fargate containers.

To turn on and customize CloudWatch Logs logging, review the following one-time configuration tasks:
+ For AWS Batch compute environments that are based on EC2 resources, add an IAM policy to the `ecsInstanceRole` role. For more information, see [Tutorial: Add a CloudWatch Logs IAM policy](cwl_iam_policy.md).
+ Create an Amazon EC2 launch template that includes detailed CloudWatch monitoring, then specify the template when you create your AWS Batch compute environment. You can also install the CloudWatch agent on an existing image and then specify the image in the AWS Batch first-run wizard.
+ (Optional) Configure the awslogs driver. You can add parameters that change the default behavior on both EC2 and Fargate resources. For more information, see [Use the awslogs log driver](using_awslogs.md).

**Topics**
+ [Tutorial: Add a CloudWatch Logs IAM policy](cwl_iam_policy.md)
+ [Install and configure the CloudWatch agent](installing_cwl_agent.md)
+ [Tutorial: View CloudWatch Logs](viewing_cwlogs.md)