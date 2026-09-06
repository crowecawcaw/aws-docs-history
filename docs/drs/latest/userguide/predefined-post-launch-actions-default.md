

# Predefined post-launch actions
<a name="predefined-post-launch-actions-default"></a>

 AWS Elastic Disaster Recovery allows you to run various predefined post-launch actions on your EC2 launched instance. Use these out-of-the-box actions to validate your launch or improve your launch flexibility. 

***Choose from a variety of predefined post-launch actions***
+  [Enable SSM](#enable-ssm) 
+  [Install a CloudWatch Agent](#install-cloudwatch-agent) 
+  [Create AMI from instance](#create-ami-form-instance) 
+  [Configure Time Sync](#configure-time-sync) 
+  [Volume integrity validation](#volume-integrity-validation) 
+  [Process status validation](#process-status-validation) 
+  [Validate disk space](post-launch-action-settings-overview.md#validate-disk-space) 
+  [EC2 connectivity check](post-launch-action-settings-overview.md#ec2-connectivity-checks) 
+  [HTTP/HTTPS response validation](post-launch-action-settings-overview.md#verify-http-response) 
+  [Verify tags](post-launch-action-settings-overview.md#verify-tags) 

**Note**  
These predefined post-launch actions are supported in the Middle East (UAE) Region:  
Enable SSM
CloudWatch agent installation
Create AMI from instance
Volume integrity validation
Process status validation
Validate disk space
EC2 connectivity check
HTTP/HTTPS response validation
Verify tags

## Enable SSM
<a name="enable-ssm"></a>

 The AWS Systems Manager (AWS SSM) allows AWS Elastic Disaster Recovery to run post-launch actions on your recovery instances after they are launched. When you activate the post-launch actions, AWS Elastic Disaster Recovery installs the **AWS SSM agent**. 

 The AWS SSM agent must be installed for any other post-launch action to run. Therefore, this is the only post-launch action that is activated by default and cannot be deactivated. [Learn more about SSM](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html). 

## Install a CloudWatch Agent
<a name="install-cloudwatch-agent"></a>

 Use the **CloudWatch agent installation** feature to install and configure the CloudWatch Agent and Application Insights. The launched instance requires these policies: 

**CloudWatchAgentServerPolicy** – The permissions required to use AmazonCloudWatchAgent on servers

**AmazonSSMManagedInstanceCore** – The policy for Amazon EC2 Role to enable AWS Systems Manager service core functionality

 To ensure that the launched instance has the right policies, create a role that has the required permissions as per the policies above or have access to a role with those permissions. Go to **Launch settings > EC2 launch template > Modify > Advanced > IAM instance profile**. Use an existing profile or create a new one using the **Create new IAM profile** link. 

**Note**  
 You must attach both policies to the template for the CloudWatch agent to operate. Without the **CloudWatchAgentServerPolicy**, the action is still marked as successful but the CloudWatch Agent will not be active. Configuring the Application Insights is optional. You can choose to skip the Application Insights agent configuration and only install the CloudWatch agent. To do so, simply provide the required parameterStoreName parameter and leave the other parameters empty. 

[Learn more about the CloudWatch Agent.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)

## Create AMI from instance
<a name="create-ami-form-instance"></a>

Use the Create AMI from Instance feature to create a new Amazon Machine Image (AMI) from your AWS DRS launched instance.

The action uses these APIs:
+ [CreateImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage.html)
+ [DescribeImages](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImages.html)

 To allow the SSM document to run these APIs, you need to have the required permissions or have access to a role with those permissions and then provide the role’s ARN as an input parameter to the SSM automation document. [Learn more about creating AMI from instance.](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-createimage.html) 

## Configure Time Sync
<a name="configure-time-sync"></a>

Use the **Time Sync** feature to set the time for your Linux instance using ATSS.

[Learn more about Amazon Time Sync.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-time.html)

## Volume integrity validation
<a name="volume-integrity-validation"></a>

Use the **Volume integrity validation** to ensure that EBS volumes on the launched instance are:
+ The same size as the source (rounded up)
+ Properly mounted on the Amazon EC2 instance
+ Accessible

This feature allows you to conduct the required validations automatically and saves the time of manual validations.

**Note**  
Up to 50 volumes can be checked in a single action.

## Process status validation
<a name="process-status-validation"></a>

Use the **Process status validation** feature to ensure that processes are in running state following instance launch. You need to provide a list of processes that you want to verify, and define how long the service should wait before testing begins.

To check a specific process that should run multiple times, include it several times in the list.