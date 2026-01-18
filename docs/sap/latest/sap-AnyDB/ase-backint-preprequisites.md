# Prerequisites

This section provides information on mandatory prerequisites for AWS Backint Agent for SAP ASE.

###### Topics

- [AWS Identity and Access Management (IAM)](#ase-backint-iam "#ase-backint-iam")
- [Amazon S3 Bucket](#ase-backint-s3-bucket "#ase-backint-s3-bucket")

## AWS Identity and Access Management (IAM)

To enable S3 bucket access for your Amazon EC2 instance, create or update an inline IAM policy with the following permissions and attach it to your EC2 service role.
Replace the resource names, such as the S3 bucket name, to match your setup.
You must provide the AWS Region and Amazon S3 bucket owner account ID along with the Amazon S3 bucket name and KMS Key for Encryption.

```
 {
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetBucketPolicyStatus",
                "s3:GetBucketLocation",
                "s3:ListBucket",
                "s3:GetBucketAcl",
                "s3:GetBucketPolicy"
            ],
            "Resource": [
                "arn:aws:s3:::your-bucket-name/*",
                "arn:aws:s3:::your-bucket-name"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:us-east-1:123456789012:key/your-kms-key-id"
        },
          {
              "Effect": "Allow",
              "Action": [
                  "s3:PutObjectTagging",
                  "s3:PutObject",
                  "s3:GetObject",
                  "s3:DeleteObject"
              ],
              "Resource": "arn:aws:s3:::your-bucket-name/your-folder-name/*"
          }
    ]
}
```

###### Note

If you want to allow cross-account backup and restore, you must add your account details under a principal element in your policy.
For more information about principal policies, see [AWS JSON Policy Elements: Principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in the _AWS Identity and Access Management User Guide_.
In addition, you must ensure that the S3 bucket policies allow your account to perform the actions specified in the IAM policy example above.
For more information, see the example for [Bucket owner granting cross-account bucket permissions](../../../AmazonS3/latest/dev/example-walkthroughs-managing-access-example2.md "../../../AmazonS3/latest/dev/example-walkthroughs-managing-access-example2.md") in the _Amazon S3 Developer Guide_.

For more information about managed and inline policies, see the [IAM User Guide](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md").

## Amazon S3 Bucket

In preparation for installation of the AWS Backint agent, identify or create an S3 bucket in the target Region where SAP ASE backups will be stored.
The bucket must have been created after May 2019 in order to be compatible with AWS Backint agent and must have public access blocked, as backups will fail if public access is enabled.

AWS Backint agent supports backing up to Amazon S3 with VPC endpoints.
Using an Amazon S3 gateway endpoint can improve performance, help prevent timeouts, enhance security, and reduce costs.
For more information, see [VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md").

### S3 storage classes

AWS Backint agent supports storing SAP ASE database backups in S3 Standard, S3 Standard-IA, S3 One Zone-IA, and S3 Intelligent-Tiering storage classes.
By default, backups use the S3 Standard storage class, but this can be changed through the AWS Backint agent configuration file, [S3 Lifecycle rules](../../../AmazonS3/latest/dev/object-lifecycle-mgmt.md "../../../AmazonS3/latest/dev/object-lifecycle-mgmt.md"), or directly via APIs.

AWS Backint Agent for SAP ASE does not support the following storage classes:
. Reduced Redundancy
. Deep Archive
. Glacier

While S3 Intelligent-Tiering can automatically move objects to archival tiers, AWS Backint agent requires objects to be in standard access tiers for recovery or deletion operations.
For more information, see [Amazon S3 Storage Classes](../../../AmazonS3/latest/dev/storage-class-intro.md "../../../AmazonS3/latest/dev/storage-class-intro.md") in the _Amazon S3 Developer Guide_.

### Encryption

AWS Backint agent supports encrypting your SAP ASE backup files while storing them in Amazon S3, using server-side encryption with AWS Key Management Service (KMS).
You can encrypt your backups with an AWS managed key (aws/s3) or you can use your own customer managed key stored in AWS KMS.
To encrypt your backup files with AWS KMS keys (AWS managed or customer managed), you must provide the KMS key ARN during installation or update the AWS Backint agent configuration file later.
To learn more about encrypting your S3 objects using AWS KMS, see [How Amazon S3 uses AWS KMS](../../../kms/latest/developerguide/services-s3.md "../../../kms/latest/developerguide/services-s3.md") in the _AWS Key Management Service Developer Guide_.
Alternatively, you can enable default encryption for your Amazon S3 bucket using either AWS KMS keys or keys managed by Amazon S3 (SSE-S3).
To learn more about enabling default encryption for your bucket, see [How do I enable default encryption for an Amazon S3 bucket?](../../../AmazonS3/latest/user-guide/default-bucket-encryption.md "../../../AmazonS3/latest/user-guide/default-bucket-encryption.md") in the _Amazon S3 Console User Guide_.

### Object locking

You can store objects using a _write-once-read-many_ (WORM) model with S3 Object Lock.
Use S3 Object Lock if you want to prevent your SAP ASE backup files from being accidentally deleted or overwritten for a specific time period or indefinitely.
If S3 Object Lock is enabled, you can’t delete your SAP ASE backups stored in Amazon S3 using SAP ASE Cockpit, SAP ASE Studio, or SQL commands until the retention period expires.
To learn about S3 Object Lock, see [Locking objects using S3 Object Lock](../../../AmazonS3/latest/dev/object-lock.md "../../../AmazonS3/latest/dev/object-lock.md") in the _Amazon S3 Developer Guide_.

### Object tagging

By default, AWS Backint agent adds a tag called `AWSBackintAgentVersion` when it stores your SAP ASE backup files in your S3 bucket.
This tag helps to identify the AWS Backint version and the SAP ASE version used when backing up your SAP ASE database.
You can [list the value of the tags from S3 console](../../../AmazonS3/latest/user-guide/view-object-properties.md "../../../AmazonS3/latest/user-guide/view-object-properties.md") or [using APIs](../../../AmazonS3/latest/dev/object-tagging.md "../../../AmazonS3/latest/dev/object-tagging.md").
To disable default tagging, modify the AWS Backint agent configuration file.
See [Additional Parameters](ase-backint-install.md#ase-backint-additional-parameters "ase-backint-install.md#ase-backint-additional-parameters") for more information.

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
        "arn:aws:s3:::awssap-backint-agent-ase",
        "arn:aws:s3:::awssap-backint-agent-ase/*"
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
                "arn:aws:s3:::awssap-backint-agent-ase",
                "arn:aws:s3:::awssap-backint-agent-ase/*"
            ]
        }
    ]
}
```

### AWS Command Line Interface (CLI)

AWS Backint agent installation leverages the AWS CLI to validate S3 bucket properties. To install or update to the AWS CLI, see [Install or update to the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
