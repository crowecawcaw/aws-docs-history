

# `AWSSupport-CollectEKSLinuxNodeStatistics`
<a name="automation-awssupport-collectekslinuxnodestatistics"></a>

 **Description** 

The `AWSSupport-CollectEKSLinuxNodeStatistics` runbook collects Linux statistics from an Amazon EC2 instance that is part of an Amazon EKS cluster, and from a container running on the instance if a `containerd` container ID is specified. The Amazon EC2 instance has to be managed by AWS Systems Manager.

The host-level Linux statistics collected include:
+ OS information.
+ Network interface statistics - from `ethtool` and `/sys/class/net/interface/statistics` directory.
+ File descriptors counts.
+ Ephemeral ports counts.
+ A dump of `iptables` rules.
+ Check for a full conntrack table.

The container-level Linux statistics include:
+ Identifier information - image URI and labels.
+ Network interface statistics - from `ethtool` and `/sys/class/net/interface/statistics` directory.
+ Traceroute and DNS results if the `NetworkTargets` parameter is populated.
+ Packet capture analysis counts - TCP Retransmissions, Out of Order packets etc.

The runbook collects data from various Linux distributions including Amazon Linux 2, Amazon Linux 2023 and Debian/Ubuntu. It uses the latest versions of the following images from the Amazon ECR public gallery:
+ `amazon-ecs-network-sidecar` image to gain access to troubleshooting tools.
+ `aws-cli` image to upload the statistics report JSON file and packet capture files to the specified Amazon S3 bucket.

**Important**  
This runbook does not support Fargate instances. This runbook may fail if the instance is shutdown or disconnected during execution.

 **How does it work?** 

The runbook performs the following actions:
+ Verifies the target Amazon S3 bucket does not grant public read or write access.
+ Ensures the target Amazon EC2 instance is managed by Systems Manager and is in a running state.
+ Verifies the instance is running a Linux operating system.
+ Collects comprehensive Linux statistics from the Amazon EC2 instance and optionally from a specified container.
+ Uploads the collected statistics to the specified Amazon S3 bucket.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-CollectEKSLinuxNodeStatistics) 

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.

The `AutomationAssumeRole` parameter requires the following actions:
+ `s3:GetAccountPublicAccessBlock`
+ `s3:GetBucketPublicAccessBlock`
+ `s3:GetBucketAcl`
+ `s3:GetBucketPolicyStatus`
+ `s3:GetBucketLocation`
+ `s3:GetEncryptionConfiguration`
+ `s3:PutObject`
+ `ssm:DescribeInstanceInformation`
+ `ssm:SendCommand`
+ `ssm:GetCommandInvocation`
+ `ec2:DescribeInstances`

Example IAM policy:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetAccountPublicAccessBlock"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetBucketPublicAccessBlock",
                "s3:GetBucketAcl",
                "s3:GetBucketPolicyStatus",
                "s3:GetBucketLocation",
                "s3:GetEncryptionConfiguration"
            ],
            "Resource": "arn:aws:s3:::S3_BUCKET_NAME"
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject"
            ],
            "Resource": "arn:aws:s3:::S3_BUCKET_NAME/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:DescribeInstanceInformation"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:SendCommand"
            ],
            "Resource": [
                "arn:aws:ssm:*:*:document/AWS-RunShellScript",
                "arn:aws:ec2:*:111122223333:instance/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:GetCommandInvocation"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances"
            ],
            "Resource": "*"
        }
    ]
}
```

 **Instructions** 

Follow these steps to configure the automation:

1. Navigate to [`AWSSupport-CollectEKSLinuxNodeStatistics`](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-CollectEKSLinuxNodeStatistics/description) in Systems Manager under Documents.

1. Select Execute automation.

1. For the input parameters, enter the following:
   + **AutomationAssumeRole (Optional):**

     The Amazon Resource Name (ARN) of the IAM role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
   + **InstanceId (Required):**

     The ID of the Amazon EC2 Instance to collect statistics.
   + **S3BucketName (Required):**

     Name of the Amazon S3 bucket to export the JSON output from the Amazon EC2 instance as a file.
   + **S3KeyPrefix (Optional):**

     The Amazon S3 key prefix (sub-folder) to export the JSON output from the Amazon EC2 instance as a file. Default: `AWSSupport-CollectEKSLinuxNodeStatistics`.
   + **S3BucketOwnerRoleArn (Optional):**

     The ARN of the IAM role with permissions to get the Amazon S3 bucket and account block public access settings, bucket encryption configuration, the bucket ACLs, the bucket policy status, and upload objects to the bucket. If this parameter is not specified, the runbook uses the `AutomationAssumeRole` (if specified) or user that starts this runbook (if `AutomationAssumeRole` is not specified).
   + **S3BucketOwnerAccount (Optional):**

     The AWS account that owns the Amazon S3 bucket. If you do not specify this parameter, the runbook assumes that the bucket is in this account.
   + **ContainerId (Optional):**

     The ID of a container running on the specified Amazon EC2 instance.
   + **NetworkTargets (Optional):**

     A comma-separated list of IPv4 addresses and/or DNS names to test DNS resolution, and connectivity using traceroute.

1. Select Execute.

1. The automation initiates.

1. The document performs the following steps:
   + **`CheckBucketAccess`**:

     Checks if the target Amazon S3 bucket potentially grants read and/or write public access to its objects.
   + **`AssertInstanceIsSSMManaged`**:

     Ensures the target Amazon EC2 instance is managed by Systems Manager, otherwise the automation ends.
   + **`VerifyInstanceState`**:

     Verifies that the Amazon EC2 instance is in a running state before attempting to collect statistics.
   + **`BranchOnVerifyLinuxInstance`**:

     Verifies that the instance is a Linux instance before proceeding.
   + **`BranchOnVerifyInstanceRunning`**:

     Verifies that the instance is in a running state before proceeding.
   + **`CollectEKSLinuxNodeStatistics`**:

     Collects comprehensive Linux statistics from the Amazon EC2 instance including OS information, network interface statistics, file descriptors, ephemeral ports, firewall rules, and optionally container-level statistics.
   + **`GenerateStatisticsOutputS3Uri`**:

     Generates the full Amazon S3 URI to the Linux statistics files to be used as the automation document's output.

1. After completed, review the Outputs section for the detailed results of the execution.

**References**

Systems Manager Automation
+ [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-CollectEKSLinuxNodeStatistics/description)
+ [Run an automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing.html)
+ [Setting up an Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-setup.html)
+ [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/)