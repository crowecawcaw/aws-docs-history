# `AWSSupport-CollectEKSInstanceLogs`

**Description**

The `AWSSupport-CollectEKSInstanceLogs` runbook gathers operating
system and Amazon Elastic Kubernetes Service (Amazon EKS) related log files from an Amazon Elastic Compute Cloud (Amazon EC2) instance to
help you troubleshoot common issues. While the automation is gathering the
associated log files, changes are made to the file system structure including the
creation of temporary directories, the copying of log files to the temporary
directories, and compressing the log files into an archive. This activity can result
in increased `CPUUtilization` on the Amazon EC2 instance. For more information
about `CPUUtilization` , see [Instance metrics](../../../AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.md#ec2-cloudwatch-metrics "../../../AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.md#ec2-cloudwatch-metrics") in the _Amazon CloudWatch User Guide_ .

If you specify a value for the `LogDestination` parameter, the
automation evaluates the policy status of the Amazon Simple Storage Service (Amazon S3) bucket you specify. To
help with the security of the logs gathered from your Amazon EC2 instance, if the policy
status `isPublic` is set to `true` , or if the access control
list (ACL) grants `READ|WRITE` permissions to the `All Users`
Amazon S3 predefined group, the logs are not uploaded. For more information about Amazon S3
predefined groups, see [Amazon S3
predefined groups](../../../AmazonS3/latest/userguide/acl-overview.md#specifying-grantee-predefined-groups "../../../AmazonS3/latest/userguide/acl-overview.md#specifying-grantee-predefined-groups") in the _Amazon Simple Storage Service User Guide_ .

###### Note

This automation requires at least 10 percent of available disk space on the
root Amazon Elastic Block Store (Amazon EBS) volume attached to your Amazon EC2 instance. If there is not
enough available disk space on the root volume, the automation stops.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-CollectEKSInstanceLogs "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-CollectEKSInstanceLogs")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- EKSInstanceId

Type: String

Description: (Required) ID of the Amazon EKS Amazon EC2 instance you want to collect
logs from.

- LogDestination

Type: String

Description: (Optional) The Amazon Simple Storage Service (Amazon S3) bucket in your account to upload the
archived logs to.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `ssm:SendCommand`

**Required IAM permissions for the Amazon EC2 instance profile**

The instance profile used by the `EKSInstanceId` must have the
**AmazonSSMManagedInstanceCore** Amazon managed policy attached to it.

It also has to be able to access the `LogDestination` Amazon S3 bucket so that it could upload the
collected logs.
Below is an example of an IAM policy that could be attached to that instance profile:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetBucketPolicyStatus",
        "s3:GetBucketAcl"
      ],
      "Resource": [
        "arn:aws:s3:::LogDestination/*",
        "arn:aws:s3:::LogDestination"
      ]
    }
  ]
}
```

If `LogDestination` uses AWS KMS encryption, then an additional statement must be added to the
IAM policy, granting access to the AWS KMS key used in the encryption:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetBucketPolicyStatus",
        "s3:GetBucketAcl"
      ],
      "Resource": [
        "arn:aws:s3:::LogDestination/*",
        "arn:aws:s3:::LogDestination"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey"
      ],
      "Resource": "arn:aws:kms:REGION:ACCOUNT:key/KMS-KEY-ID"
    }
  ]
}
```

**Document Steps**

- `aws:assertAwsResourceProperty` - Confirms the operating system
  of the value specified in the `EKSInstanceId` parameter is Linux.
- `aws:runCommand` - Gathers operating system and Amazon EKS related log
  files, compressing them into an archive in the `/var/log`
  directory.
- `aws:branch` - Confirms whether a value was specified for the
  `LogDestination` parameter.
- `aws:runCommand` - Uploads the log archive to the Amazon S3 bucket you
  specify in the `LogDestination` parameter.
