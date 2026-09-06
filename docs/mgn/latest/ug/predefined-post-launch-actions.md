

NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](https://docs.aws.amazon.com/transform/latest/userguide/getting-started.html) in the *AWS Transform User Guide*.

# Predefined post-launch actions reference
<a name="predefined-post-launch-actions"></a>

AWS Transform MGN allows you to execute various predefined post-launch actions on your Amazon EC2 launch instance. Use these out-of-the-box actions to modernize your servers while you're migrating: Change existing license, upgrade your operating system, configure disaster recovery, and more.

**Topics**
+ [Install the SSM agent](#predefined-ssm-agent)
+ [Configure AWS Elastic Disaster Recovery](#predefined-elastic-disaster-recovery)
+ [Convert operating systems](#predefined-operating-systems)
+ [Replace SUSE subscription](#predefined-license-and-subscription)
+ [Conduct Amazon EC2 connectivity checks](#predefined-ec2-connectivity-check)
+ [Validate volume integrity](#predefined-volume-integrity-validation)
+ [Verify process status](#predefined-process-status-validation)
+ [Convert MS-SQL license](#predefined-windows-ms-sql-conversion)
+ [Install a CloudWatch Agent](#predefined-cloudwatch-agent-installation)
+ [Upgrade Windows](#predefined-windows-upgrade)
+ [Create AMI from instance](#predefined-create-ami-from-instance)
+ [Join Directory Service domain](#predefined-joined-domain)
+ [Configure Time Sync](#predefined-time-sync)
+ [Validate disk space](#predefined-validate-disk-space)
+ [Verify HTTP/HTTPS response](#predefined-verify-http-https-response)
+ [Enable Amazon Inspector Classic](#predefined-inspector)
+ [Verify Tags](#predefined-verify-tags)
+ [Auto Scaling group setting](#predefined-autoscaling-group-setting)
+ [Dynatrace](#predefined-dynatrace)
+ [New Relic](#predefined-new-relic)
+ [TrendMicro](#predefined-trend-micro)

## Install the SSM agent
<a name="predefined-ssm-agent"></a>

The SSM allows AWS Transform MGN to execute modernization actions on your servers after they are launched.

When you activate the post-launch actions, AWS Transform MGN installs the **SSM agent** and creates the required IAM roles.

The SSM agent must be installed for any other post-launch action to run. Therefore, this is the only post-launch action that is activated by default and cannot be deactivated.

 [Learn more about SSM.](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) 

## Configure AWS Elastic Disaster Recovery
<a name="predefined-elastic-disaster-recovery"></a>

**Note**  
This feature is supported on operating systems that are supported by AWS Elastic Disaster Recovery (AWS DRS). [See the AWS DRS documentation.](https://docs.aws.amazon.com/drs/latest/userguide/Supported-Operating-Systems.html)   
This action is not supported in MGN GovCloud regions (US-East, US-West).

Use the **DR after migration** feature to configure disaster recovery using AWS Elastic Disaster Recovery.

This action installs the AWS Elastic Disaster Recovery Replication Agent on your Amazon EC2 instance.

You must select the target disaster recovery region, which is the AWS Region in which the Recovery instances are deployed. AWS Elastic Disaster Recovery must be available in the selected Region and initiated in your account. You must initialize Elastic Disaster Recovery for this action to work. 

**Note**  
Ensure that you review the costs associated with AWS Elastic Disaster Recovery in the [service pricing documentation](https://aws.amazon.com/disaster-recovery/pricing/). 

 [Learn more about Elastic Disaster Recovery AWS Regions.](https://docs.aws.amazon.com/drs/latest/userguide/supported-regions.html) 

 [Learn more about initializing Elastic Disaster Recovery.](https://docs.aws.amazon.com/drs/latest/userguide/getting-started-initializing.html) 



## Convert operating systems
<a name="predefined-operating-systems"></a>

**Note**  
This feature is supported on CentOS version 8.x.

Use the **CentOS to Rocky** feature to perform changes to the target machine operating system. It allows you to convert any of your source servers that are running CentOS to [Rocky Linux](https://rockylinux.org/). 

## Replace SUSE subscription
<a name="predefined-license-and-subscription"></a>

**Note**  
This feature is supported on SUSE Linux versions 12 SP 1 and later.
This action is not supported on SLES4SAP servers.

Use the **Replace SUSE subscription** feature to choose whether you want to change the SUSE Linux subscription of any source server that runs SUSE to an AWS-provided SUSE subscription.

 An AWS-provided SUSE subscription allows AWS to manage your licenses, including renewal handling, saving you time and simplifying your billing and license management processes 

## Conduct Amazon EC2 connectivity checks
<a name="predefined-ec2-connectivity-check"></a>

Use the **EC2 connectivity check** feature to conduct network connectivity checks to a predefined list of ports and hosts. 

**Note**  
Up to 5 Port:IP couples can be checked in a single action.

## Validate volume integrity
<a name="predefined-volume-integrity-validation"></a>

Use the **Volume integrity validation** feature to ensure that Amazon EBS volumes on the launched instance are:
+ The same size as the source (rounded up)
+ Properly mounted on the Amazon EC2 instance
+ Accessible

For FSx for ONTAP migrations using iSCSI, this action additionally validates that:
+ iSCSI sessions are established to the ONTAP SVM
+ Multipath paths are active (when MPIO is configured)

This feature allows you to conduct the required validations automatically and saves the time of manual validations.

**Note**  
Up to 50 volumes can be checked in a single action.

## Verify process status
<a name="predefined-process-status-validation"></a>

Use the **Process status validation** feature to ensure that processes are in running state following instance launch. You need to provide a list of processes that you want to verify, and define how long the service should wait before testing begins.

To check a specific process that should run multiple times, include it several times in the list.

## Convert MS-SQL license
<a name="predefined-windows-ms-sql-conversion"></a>

Use the **Windows MS-SQL license conversion** feature to easily convert Windows MS-SQL BYOL to an AWS license. MGN detects SQL Server installed as either the default instance (MSSQLSERVER) or as a named instance (for example, MSSQL$SQLPROD).

MGN:
+ Checks the SQL edition (Enterprise, Standard, or Web) as part of the launch process 
+ Uses the right AMI with the right billing code to launch from

The SSM document runs and verifies that the right billing code is used post launch.

The action uses these APIs:
+ [DescribeImages](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImages.html)
+ [DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html)

To allow the SSM document to run these APIs, you need the required permissions or have access to a role with those permissions and then provide the role’s ARN as an input parameter to the SSM automation document.

## Install a CloudWatch Agent
<a name="predefined-cloudwatch-agent-installation"></a>

Use the **CloudWatch agent installation** feature to install and configure the CloudWatch Agent and Application Insights.

You need the AWSApplicationMigrationSSMAccess policy, or a user-defined policy that allows the SSM document to run, to run this post-launch action. This is in addition to the [full access policy](security-iam-awsmanpol-AWSApplicationMigrationFullAccess.md):

The launched instance requires these policies:
+ CloudWatchAgentServerPolicy – The permissions required to use AmazonCloudWatchAgent on servers
+ AmazonSSMManagedInstanceCore – The policy for Amazon EC2 Role to enable AWS Systems Manager service core functionality

To ensure that the launch instance has the right policies, create a role that has the required permissions as per the policies above or has access to a role with those permissions.
+ Go to **Launch settings > EC2 launch template > Modify > Advance > IAM instance profile**.
+ Use an existing profile or create a new one using the **Create new IAM profile** link.

**Note**  
You must attach both policies to the template for the CloudWatch agent to operate. Without the CloudWatchAgentServerPolicy, the action is still marked as successful but the CloudWatch Agent is not active.
Configuring the Application Insights is optional. You can choose to skip the Application Insights agent configuration and only install the CloudWatch agent. To do so provide the required parameterStoreName parameter and leave the other parameters empty.

 [Learn more about the CloudWatch Agent.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html) 

## Upgrade Windows
<a name="predefined-windows-upgrade"></a>

Use the **Windows upgrade** feature to upgrade your migrated server to a more recent version of Windows Server ([see the full list of available OS versions](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awsec2-CloneInstanceAndUpgradeWindows.html)). 

You need the AWSApplicationMigrationSSMAccess policy, or a user-defined policy that allows the SSM document to run, to run this post-launch action. This is in addition to the [full access policy](security-iam-awsmanpol-AWSApplicationMigrationFullAccess.md):

To allow the SSM document to run these APIs, you must have the required permissions (including [CreateImages](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage.html), [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html), [DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html), and more) or have access to a role with those permissions and then provide the role’s ARN as an input parameter to the SSM automation document.

Learn more about the permissions required to perform the upgrade in [AWSEC2-CloneInstanceAndUpgradeWindows.](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awsec2-CloneInstanceAndUpgradeWindows.html) 

The SSM document:
+ Creates an Amazon Machine Image (AMI) from the instance using the [CreateImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage.html) API.
+ Uses the AMI to create a new instance and then upgrades that instance.
+ Creates an AMI from the upgraded instance and terminates the upgraded instance.

**Note**  
This operation may run for several hours.
All other post-launch actions run on the instance launched by MGN and not on the upgraded instance. 

 [Learn more about upgrading Windows.](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-awsec2-CloneInstanceAndUpgradeWindows.html) 

## Create AMI from instance
<a name="predefined-create-ami-from-instance"></a>

Use the **Create AMI from Instance** feature to create a new Amazon Machine Image (AMI) from your MGN launched instance.

You need the AWSApplicationMigrationSSMAccess policy, or a user-defined policy that allows the SSM document to run, to run this post-launch action. This is in addition to the [full access policy](security-iam-awsmanpol-AWSApplicationMigrationFullAccess.md):

The action uses these APIs:
+ [CreateImages](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage.html)
+ [DescribeImages](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImages.html)

To allow the SSM document to run these APIs, you need the required permissions or have access to a role with those permissions and then provide the role’s ARN as an input parameter to the SSM automation document.

 [Learn more about creating AMI from instance.](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-createimage.html) 

## Join Directory Service domain
<a name="predefined-joined-domain"></a>

Use this **Join domain** feature to simplify the AWS Join Domain process. If you activate this action, your instance is managed by the AWS Cloud Directory (instead of on-premises).

You need the AWSApplicationMigrationSSMAccess policy, or a user-defined policy that allows the SSM document to run, to run this post-launch action. This is in addition to the [full access policy](security-iam-awsmanpol-AWSApplicationMigrationFullAccess.md):

The launched instance requires these policies:
+ AmazonSSMManagedInstanceCore – The policy for Amazon EC2 Role to enable AWS Systems Manager service core functionality.
+ AmazonSSMDirectoryServiceAccess – This policy allows the SSM Agent to access Directory Service on behalf of the customer for domain-join the managed instance.

To ensure that the launched instance has the right policies, create a role that has the required permissions as per the policies above or has access to a role with those permissions.
+ Go to **Launch settings > EC2 launch template > Modify > Advance > IAM instance profile**.
+ Use an existing profile or create a new one using the **Create new IAM profile** link.

## Configure Time Sync
<a name="predefined-time-sync"></a>

Use the **Time Sync** feature to set the time for your Linux instance using ATSS.

[Learn more about Amazon Time Sync.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-time.html)

## Validate disk space
<a name="predefined-validate-disk-space"></a>

Use the **Disk space validation** feature to obtain visibility into the disc space that you have at your disposal, as well as logs with actionable insights.

## Verify HTTP/HTTPS response
<a name="predefined-verify-http-https-response"></a>

Use the **Verify HTTP/HTTPS response** feature to conduct HTTP/HTTPS connectivity checks to a predefined list of URLs. The feature verifies that HTTP/HTTPS requests (for example, https://localhost) receive the correct response.

## Enable Amazon Inspector Classic
<a name="predefined-inspector"></a>

The **Enable Inspector** feature allows you to run security scans on your Amazon EC2 resources. The Amazon Inspector service is enabled at the account level.

**Note**  
Amazon Inspector is a paid AWS service. For additional information, [refer to the full Inspector pricing documentation](https://aws.amazon.com/inspector/pricing).

This action uses these APIs:
+ [ Enable](https://docs.aws.amazon.com/inspector/v2/APIReference/API_Enable.html)
+ [BatchGetAccountStatus](https://docs.aws.amazon.com/inspector/v2/APIReference/API_BatchGetAccountStatus.html)
+ [CreateServiceLinkedRole](https://docs.aws.amazon.com/IAM/latest/APIReference/API_CreateServiceLinkedRole.html)

To allow the SSM document to run these APIs, you need the required permissions or have access to a role with those permissions and then provide the role’s ARN as an input parameter to the SSM automation document.

## Verify Tags
<a name="predefined-verify-tags"></a>

Use the **Verify tags** feature to validate that tags that have been defined in the launch template and on the source server are copied to the migrated server. 

## Auto Scaling group setting
<a name="predefined-autoscaling-group-setting"></a>

Use the **Auto Scaling group setting** when you would like to create an Auto Scaling group for a migrated stateless web application. 

## Dynatrace
<a name="predefined-dynatrace"></a>

**Note**  
This action is provided by a third party vendor, and is not available in the GovCloud Regions.

This action installs Dynatrace OneAgent on your launched instance.

To configure this action, you need an existing Dynatrace account and configure the required additionalArguments for your particular usage.

 Learn more about Dynatrace in [Deploy OneAgent using AWS Systems Manager Distributor ](https://www.dynatrace.com/support/help/setup-and-configuration/setup-on-cloud-platforms/amazon-web-services/amazon-web-services-integrations/aws-ec2/deploy-oneagent-using-aws-systems-manager-distributor) 

## New Relic
<a name="predefined-new-relic"></a>

**Note**  
This action is provided by a third party vendor, and is not available in the GovCloud Regions.

This action installs New Relic Infrastructure agent on your launched Amazon EC2 instance.

To configure this action, you need an existing New Relic account and configure the required additionalArguments for your particular usage. You must use an original account license key for this action to succeed.

 [Learn more about New Relic](https://docs.newrelic.com/docs/infrastructure/amazon-integrations/aws-integrations-list/aws-sys-dist/) 

## TrendMicro
<a name="predefined-trend-micro"></a>

**Note**  
This action is provided by a third party vendor, and is not available in the GovCloud Regions.

This action installs the Trend Micro agent on your launched instance.

 [Learn more about Trend Micro](https://docs.trendmicro.com/en-us/documentation/article/trend-vision-one-aws-systems-manager-distributor) 