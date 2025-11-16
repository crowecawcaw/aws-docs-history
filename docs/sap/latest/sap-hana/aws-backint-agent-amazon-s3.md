# Backup and restore SAP HANA workloads to Amazon S3

This section provides information about setting up and using AWS Backint agent to backup and restore your SAP HANA workloads to Amazon S3.

###### Topics

- [Prerequisites](#aws-backint-agent-s3-prerequisites "#aws-backint-agent-s3-prerequisites")
- [Install and configure AWS Backint Agent for SAP HANA](aws-backint-agent-s3-installing-configuring.md "aws-backint-agent-s3-installing-configuring.md")
- [Back up and restore your SAP HANA system with the AWS Backint Agent for SAP HANA](aws-backint-agent-s3-backup-restore.md "aws-backint-agent-s3-backup-restore.md")

## Prerequisites

After your SAP HANA system is successfully running on an Amazon EC2 instance, verify the following prerequisites to install AWS Backint agent using the Amazon EC2 Systems Manager document or using AWS Backint installer.

###### Topics

- [AWS Identity and Access Management](#aws-backint-agent-iam "#aws-backint-agent-iam")
- [AWS Systems Manager Agent (SSM Agent)](#aws-backint-agent-ssm "#aws-backint-agent-ssm")
- [Amazon S3 bucket](#s3-bucket "#s3-bucket")
- [Data perimeter](#data-perimeter "#data-perimeter")
- [AWS CLI](#install-aws-cli "#install-aws-cli")

### AWS Identity and Access Management

1. To access the AWS resources required to install AWS Backint agent with AWS Systems Manager, you must attach the `AmazonSSMManagedInstanceCore` managed policy to your IAM role.

###### Note

If you choose to install the AWS Backint agent using the AWS Backint installer, you can skip this step. 2. To allow your Amazon EC2 instance to access your target Amazon S3 bucket, you must create or update an inline IAM policy with the following permissions and attach it to your EC2 service role. Replace the resource names, such as the S3 bucket name, to match your resource name. You must provide the AWS Region and Amazon S3 bucket owner account ID along with the Amazon S3 bucket name.

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "s3:GetBucketPolicyStatus",
                "s3:GetBucketLocation",
                "s3:ListBucket",
                "s3:GetBucketAcl",
                "s3:GetBucketPolicy"
            ],
            "Resource": [
                "arn:aws:s3:::bucket-name/*",
                "arn:aws:s3:::bucket-name"
            ]
        },
        {
            "Sid": "VisualEditor2",
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        },
          {
              "Sid": "VisualEditor0",
              "Effect": "Allow",
              "Action": [
                  "s3:PutObjectTagging",
                  "s3:PutObject",
                  "s3:GetObject",
                  "s3:DeleteObject"
              ],
              "Resource": "arn:aws:s3:::bucket-name/folder-name/*"
          }
    ]
}
```

###### Note

If you want to allow cross-account backup and restore, you must add your account details under a principal element in your policy. For more information about principal policies, see [AWS JSON Policy Elements: Principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in the _AWS Identity and Access Management User Guide_. In addition, you must ensure that the S3 bucket policies allow your account to perform the actions specified in the IAM policy example above. For more information, see the example for [Bucket owner granting cross-account bucket permissions](../../../AmazonS3/latest/dev/example-walkthroughs-managing-access-example2.md "../../../AmazonS3/latest/dev/example-walkthroughs-managing-access-example2.md") in the _Amazon S3 Developer Guide_.

For more information about managed and inline policies, see the [IAM User Guide](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md").

### AWS Systems Manager Agent (SSM Agent)

To install the AWS Backint agent with the AWS Systems Manager Agent (SSM Agent) document, you must install the [AWS Systems Manager Agent (SSM Agent)](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md") version 2.3.274.0 or later, and your instance must be a managed instance that is configured for AWS Systems Manager. If you want to install AWS Backint agent using AWS Backint installer, you can skip this step. For more information about managed instances, see [AWS Systems Manager Managed Instances](../../../systems-manager/latest/userguide/managed_instances.md "../../../systems-manager/latest/userguide/managed_instances.md"). To update the SSM Agent, see [Update SSM Agent by using Run Command](../../../systems-manager/latest/userguide/rc-console.md#rc-console-agentexample "../../../systems-manager/latest/userguide/rc-console.md#rc-console-agentexample").

###### Note

The SSM Agent will not work if you do not attach the `AmazonSSMManagedInstanceCore` policy to your EC2 instance role.

### Amazon S3 bucket

When you install the AWS Backint agent, you must provide the name of the S3 bucket where you want to store your SAP HANA backups. Only Amazon S3 buckets created after May 2019 are compatible with AWS Backint agent. If you do not own a bucket created after May 2019, create a new S3 bucket in your target Region. Additionally, ensure that the Amazon S3 bucket where you want to store your backups doesn’t have public access enabled. If the S3 bucket has public access enabled, backups will fail.

AWS Backint agent supports backing up to Amazon S3 with VPC endpoints. Amazon S3 gateway endpoint can improve performance, and help potentially avoid timeouts. It increases security while reducing cost. For more information, see [VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md").

**S3 storage classes** — AWS Backint agent supports backing up your SAP HANA database to an Amazon S3 bucket with the S3 Standard, S3 Standard-IA, S3 One Zone-IA, and S3 Intelligent-Tiering storage classes. S3 Reduced Redundancy, Deep Archive, and Glacier storage classes are not supported by AWS Backint agent. By default, the S3 Standard storage class is used to store your backups. You can change the storage class to use for backups by modifying the AWS Backint agent configuration file. Alternatively, you can change your backup files to one of the supported storage classes through [S3 LifeCycle configuration](../../../AmazonS3/latest/dev/object-lifecycle-mgmt.md "../../../AmazonS3/latest/dev/object-lifecycle-mgmt.md") or directly using APIs. To learn more about Amazon S3 storage classes, see [Amazon S3 Storage Classes](../../../AmazonS3/latest/dev/storage-class-intro.md "../../../AmazonS3/latest/dev/storage-class-intro.md") in the _Amazon S3 Developer Guide_.

###### Note

S3 Intelligent-Tiering storage class enables movement of objects between four access tiers. It can also move objects to the archival tiers. However, **AWS Backint agent for SAP HANA does not support backup and recovery from archival tiers.** To recover or delete objects from the archival tiers, you must first [restore the archived S3 objects](../../../AmazonS3/latest/userguide/restoring-objects.md "../../../AmazonS3/latest/userguide/restoring-objects.md") before initiating a recovery or deletion with the AWS Backint agent.

**Encryption** — AWS Backint agent supports encrypting your SAP HANA backup files while storing them in Amazon S3, using server-side encryption with AWS KMS (KMS). You can encrypt your backups with a `aws-managed-key` called `aws/s3` or you can use your own custom symmetrical AWS KMS key stored in KMS. To encrypt your backup files with keys stored in KMS (AWS-managed or custom), you must provide the KMS ARN during the install, or update the AWS Backint agent configuration file at a later time. To learn more about encrypting your S3 objects using AWS KMS, see [How Amazon S3 uses AWS KMS](../../../kms/latest/developerguide/services-s3.md "../../../kms/latest/developerguide/services-s3.md") in the _AWS Key Management Service Developer Guide_. Alternatively, you can enable default encryption for your Amazon S3 bucket using keys managed by Amazon S3. To learn more about enabling default encryption for your bucket, see [How do I enable default encryption for an Amazon S3 bucket?](../../../AmazonS3/latest/user-guide/default-bucket-encryption.md "../../../AmazonS3/latest/user-guide/default-bucket-encryption.md") in the _Amazon S3 Console User Guide_.

**Object locking** — You can store objects using a _write-once-read-many_ (WORM) model with S3 Object Lock. Use S3 Object Lock if you want to prevent your SAP HANA backup files from being accidentally deleted or overwritten for a specific time period or indefinitely. If S3 Object Lock is enabled, you can’t delete your SAP HANA backups stored in Amazon S3 using SAP HANA Cockpit, SAP HANA Studio, or SQL commands until the retention period expires. To learn about S3 Object Lock, see [Locking objects using S3 Object Lock](../../../AmazonS3/latest/dev/object-lock.md "../../../AmazonS3/latest/dev/object-lock.md") in the _Amazon S3 Developer Guide_.

**Object tagging** — By default, AWS Backint agent adds a tag called `AWSBackintAgentVersion` when it stores your SAP HANA backup files in your S3 bucket. This tag helps to identify the AWS Backint version and the SAP HANA version used when backing up your SAP HANA database. You can [list the value of the tags from S3 console](../../../AmazonS3/latest/user-guide/view-object-properties.md "../../../AmazonS3/latest/user-guide/view-object-properties.md") or [using APIs](../../../AmazonS3/latest/dev/object-tagging.md "../../../AmazonS3/latest/dev/object-tagging.md"). To disable default tagging, modify the AWS Backint agent configuration file.

### Data perimeter

AWS Backint Agent must be installed on your Amazon EC2 instance. To download the installation binary, your EC2 instance needs access to the AWS-managed S3 buckets where the installer packages are hosted. If your organization uses data perimeter policies to control access to Amazon S3 in your environment, you might need to explicitly allow these service-owned buckets so that the EC2 instance can retrieve the required installer.
The following policy shows an example Service control policy to permit access to service-owned resources through the resource perimeter, relevant service owned buckets are listed in the NotResource element of the policy.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "EnforceResourcePerimeterAWSResources",
      "Effect": "Deny",
      "Action": "*",
      "NotResource": [
        "arn:aws:s3:::awssap-backint-agent",
        "arn:aws:s3:::awssap-backint-agent/*"
      ],
      "Condition": {
        "StringNotEqualsIfExists": {
          "aws:ResourceOrgID": "<organization id>",
          "aws:PrincipalTag/dp:exclude:resource": "true"
        }
      }
    }
  ]
}
```

The following policy shows an example VPC endpoint policy allowing access to specific service-owned resources through a VPC endpoint. Relevant service owned buckets are listed in the Resource element of the statement.

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Sid": "AllowRequestsToAWSOwnedResources",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::awssap-backint-agent",
                "arn:aws:s3:::awssap-backint-agent/*"
            ]
        }
    ]
}
```

For AWS GovCloud, replace the bucket name with s3://awssap-backint-agent-us-gov-east-1 or s3://awssap-backint-agent-us-gov-west-1.

### AWS CLI

AWS Backint agent installation leverages the AWS CLI to validate S3 bucket properties. To install or update to the AWS CLI, see [Install or update to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
