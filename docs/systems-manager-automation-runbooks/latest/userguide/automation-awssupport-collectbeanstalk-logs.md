# `AWSSupport-CollectElasticBeanstalkLogs`

**Description**

The `AWSSupport-CollectElasticBeanstalkLogs` runbook gathers AWS Elastic Beanstalk
related log files from an Amazon Elastic Compute Cloud (Amazon EC2) Windows Server instance launched by Elastic Beanstalk to
help you troubleshoot common issues. While the automation is gathering the
associated log files, changes are made to the file system structure including the
creation of temporary directories, the copying of log files to the temporary
directories, and compressing the log files into an archive. This activity can result
in increased `CPUUtilization` on the Amazon EC2 instance. For more information
about `CPUUtilization` , see [Instance metrics](../../../AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.md#ec2-cloudwatch-metrics "../../../AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.md#ec2-cloudwatch-metrics") in the _Amazon CloudWatch User Guide_ .

If you specify a value for the `S3BucketName` parameter, the
automation evaluates the policy status of the Amazon Simple Storage Service (Amazon S3) bucket you specify. To
help with the security of the logs gathered from your Amazon EC2 instance, if the policy
status `isPublic` is set to `true` , or if the access control
list (ACL) grants `READ|WRITE` permissions to the `All Users`
Amazon S3 predefined group, the logs are not uploaded. For more information about Amazon S3
predefined groups, see [Amazon S3
predefined groups](../../../AmazonS3/latest/userguide/acl-overview.md#specifying-grantee-predefined-groups "../../../AmazonS3/latest/userguide/acl-overview.md#specifying-grantee-predefined-groups") in the _Amazon Simple Storage Service User Guide_ .

If you do not specify a value for the `S3BucketName` parameter, the
automation uploads the log bundle to the default Elastic Beanstalk Amazon S3 bucket in the
AWS Region where you run the automation. The directory is named according to the
following structure, `elasticbeanstalk- `region`-
`accountID`` . The `region` and
 `accountID` values will differ based on the Region and
 AWS account you run the automation in. The log bundle will be saved to the `resources/environments/logs/bundle/ `environmentID` /
 `instanceID`` directory. The `environmentID` and
`instanceID` values will differ based on your Elastic Beanstalk
environment and the Amazon EC2 instance you're gathering logs from.

By default, the AWS Identity and Access Management (IAM) instance profile attached to the Amazon EC2
instances of the Elastic Beanstalk environment has the required permissions to upload the bundle
to the default Elastic Beanstalk Amazon S3 bucket for your environment. If you specify a value for
the `S3BucketName` parameter, the instance profile attached to the Amazon EC2
instance must allow the `s3:GetBucketAcl` ,
`s3:GetBucketPolicy` , `s3:GetBucketPolicyStatus` , and
`s3:PutObject` actions for the specified Amazon S3 bucket and path.

###### Note

This automation requires at least 500 MB of available disk space on the root
Amazon Elastic Block Store (Amazon EBS) volume attached to your Amazon EC2 instance. If there is not enough
available disk space on the root volume, the automation stops.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-CollectElasticBeanstalkLogs "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-CollectElasticBeanstalkLogs")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- EnvironmentId

Type: String

Description: (Required) The ID of your Elastic Beanstalk environment you want to
collect the log bundle from.

- InstanceId

Type: String

(Required) The ID of the Amazon EC2 instance in your Elastic Beanstalk environment you want
to collect the log bundle from.

- S3BucketName

Type: String

(Optional) The Amazon S3 bucket you want to upload the archived logs to.

- S3BucketPath

Type: String

(Optional) The Amazon S3 bucket path you want to upload the log bundle to.
This parameter is ignored if you do not specify a value for the
`S3BucketName` parameter.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `ssm:SendCommand`
- `ssm:DescribeInstanceInformation`
- `ec2:DescribeInstances`

**Document Steps**

- `aws:assertAwsResourceProperty` - Confirms the Amazon EC2 instance you
  specify in the `InstanceId` parameter is managed by AWS Systems Manager.
- `aws:assertAwsResourceProperty` - Confirms the Amazon EC2 instance you
  specify in the `InstanceId` parameter is a Windows Server instance.
- `aws:runCommand` - Checks whether the instance is part of an
  Elastic Beanstalk environment, if there is sufficient disk space to bundle the logs, and
  whether the Amazon S3 bucket to which the logs would be uploaded to is public.
- `aws:runCommand` - Collects the log files and uploads the archive
  to the Amazon S3 bucket specified in the `S3BucketName` parameter or
  to the default bucket for your Elastic Beanstalk environment if a value is not
  specified.
