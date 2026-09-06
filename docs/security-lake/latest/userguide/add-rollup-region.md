

# Configuring rollup Regions in Security Lake
<a name="add-rollup-region"></a>

A rollup Region consolidates data from one or more contributing Regions. Specifying a rollup Region can help you comply with Regional compliance requirements.

Due to limitations in Amazon S3, replication from Customer Managed Key (CMK) encrypted regional data lake to S3 managed encrypted (default encryption) regional data lake is not supported.

**Important**  
If you created a custom source, to ensure that custom source data is replicated properly to the destination, Security Lake recommends following the best practices described in [Best practices for ingesting custom sources](https://docs.aws.amazon.com/security-lake/latest/userguide/custom-sources.html#custom-sources-best-practices). Replication cannot be performed on data that does not follow the S3 partition data path format as described on the page.

Before adding a rollup Region, you first need to create two different roles in AWS Identity and Access Management (IAM):
+ [IAM role for data replication](#iam-role-replication)
+ [IAM role to register AWS Glue partitions](#iam-role-partitions)

**Note**  
Security Lake creates these IAM roles or uses existing roles on your behalf when you use the Security Lake console. However, you must create these roles when using the Security Lake API or AWS CLI.

## IAM role for data replication
<a name="iam-role-replication"></a>

This IAM role grants permission to Amazon S3 to replicate source logs and events across multiple Regions.

To grant these permissions, create an IAM role that starts with the prefix `SecurityLake`, and attach the following sample policy to the role. You'll need the Amazon Resource Name (ARN) of the role when you create a rollup Region in Security Lake. In this policy, `sourceRegions` are contributing Regions, and `destinationRegions` are rollup Regions.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "AllowReadS3ReplicationSetting",
      "Action": [
        "s3:ListBucket",
        "s3:GetReplicationConfiguration",
        "s3:GetObjectVersionForReplication",
        "s3:GetObjectVersion",
        "s3:GetObjectVersionAcl",
        "s3:GetObjectVersionTagging",
        "s3:GetObjectRetention",
        "s3:GetObjectLegalHold"
      ],
      "Effect": "Allow",
      "Resource": [
        "arn:aws:s3:::aws-security-data-lake-[[{{sourceRegions}}]]*",
        "arn:aws:s3:::aws-security-data-lake-[[{{sourceRegions}}]]*/*"
      ],
      "Condition": {
        "StringEquals": {
          "s3:ResourceAccount": [
            "{{{{bucketOwnerAccountId}}}}"
          ]
        }
      }
    },
    {
      "Sid": "AllowS3Replication",
      "Action": [
        "s3:ReplicateObject",
        "s3:ReplicateDelete",
        "s3:ReplicateTags",
        "s3:GetObjectVersionTagging"
      ],
      "Effect": "Allow",
      "Resource": [
        "arn:aws:s3:::aws-security-data-lake-[[{{destinationRegions}}]]*/*"
      ],
      "Condition": {
        "StringEquals": {
          "s3:ResourceAccount": [
            "{{{{bucketOwnerAccountId}}}}"
          ]
        }
      }
    }
  ]
}
```

------

Attach the following trust policy to your role to permit Amazon S3 to assume the role:

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowS3ToAssume",
            "Effect": "Allow",
            "Principal": {
                "Service": "s3.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

------

If you use a customer managed key from AWS Key Management Service (AWS KMS) to encrypt your Security Lake data lake, you must grant the following permissions in addition to the permissions in the data replication policy.

```
{
    "Action": [
        "kms:Decrypt"
    ],
    "Effect": "Allow",
    "Condition": {
        "StringLike": {
            "kms:ViaService": [
                "s3.{sourceRegion1}.amazonaws.com",
                "s3.{sourceRegion2}.amazonaws.com"
                ],
            "kms:EncryptionContext:aws:s3:arn": [
                "arn:aws:s3:::aws-security-data-lake-{sourceRegion1}*",
                "arn:aws:s3:::aws-security-data-lake-{sourceRegion2}*"
            ]
        }
    },
    "Resource": [
        "{sourceRegion1KmsKeyArn}",
        "{sourceRegion2KmsKeyArn}"
    ]
},
{
    "Action": [
        "kms:Encrypt"
    ],
    "Effect": "Allow",
    "Condition": {
        "StringLike": {
            "kms:ViaService": [
            "s3.{destinationRegion1}.amazonaws.com",
            ],
            "kms:EncryptionContext:aws:s3:arn": [
                "arn:aws:s3:::aws-security-data-lake-{destinationRegion1}*",
            ]
        }
    },
    "Resource": [
            "{destinationRegionKmsKeyArn}"
    ]
}
```

For more information about replication roles, see [Setting up permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/setting-repl-config-perm-overview.html) in the *Amazon Simple Storage Service User Guide*.

## IAM role to register AWS Glue partitions
<a name="iam-role-partitions"></a>

This IAM role grants permissions for a partition updater AWS Lambda function used by Security Lake to register AWS Glue partitions for the S3 objects that were replicated from other regions. Without creating this role, subscribers can't query events from those objects.

To grant these permissions, create a role named `AmazonSecurityLakeMetaStoreManager` (you may have already created this role while onboarding to Security Lake). For more information about this role, including a sample policy, see [Step 1: Create IAM roles](get-started-programmatic.md#prerequisites).

In the Lake Formation console, you must also grant `AmazonSecurityLakeMetaStoreManager` permissions as a data lake administrator by following these steps:

1. Open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/).

1. Sign in as an administrative user.

1. If a **Welcome to Lake Formation** window appears, choose the user that you created or selected in Step 1, and then choose Get started.

1. If you don't see a **Welcome to Lake Formation** window, then perform the following steps to configure a Lake Formation Administrator.

   1. In the navigation pane, under **Permissions**, choose **Administrative Roles and tasks**. In the **Data lake administrators** section of the console page, choose **Choose administrators**.

   1. In the **Manage data lake administrators** dialog box, for IAM users and roles, choose the **AmazonSecurityLakeMetaStoreManager** IAM role that you created, and then choose **Save**.

For more information about changing permissions for data lake administrators, see [Create a data lake administrator](https://docs.aws.amazon.com/lake-formation/latest/dg/getting-started-setup.html#create-data-lake-admin) in the *AWS Lake Formation Developer Guide*.

## Adding rollup Regions
<a name="procedures-add-rollup-region"></a>

Choose your preferred access method, and follow these steps to add a rollup Region.

**Note**  
A Region can contribute data to multiple rollup Regions. However, a rollup Region cannot be a contributing Region for another rollup Region.

------
#### [ Console ]

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/).

1. In the navigation pane, under **Settings**, choose **Rollup Regions**.

1. Choose **Modify**, and then choose **Add rollup Region**.

1. Specify the rollup Region and contributing Regions. Repeat this step if you want to add multiple rollup Regions.

1. If this is your first time adding a rollup Region, for **Service access**, create a new IAM role or use an existing IAM role that gives Security Lake permission to replicate data across multiple Regions.

1. When you finish, choose **Save**.

You can also add a rollup Region when you onboard to Security Lake. For more information, see [Getting started with Amazon Security Lake](getting-started.md).

------
#### [ API ]

To add a rollup Region programmatically, use the [UpdateDataLake](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_UpdateDataLake.html) operation of the Security Lake API. If you're using the AWS CLI, run the [update-data-lake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/update-data-lake.html) command. In your request, use the `region` field to specify the Region that you want to contribute data to the rollup Region. In the `regions` array of the `replicationConfiguration` parameter, specify the Region code for each rollup Region. For a list of Region codes, see [Amazon Security Lake endpoints](https://docs.aws.amazon.com/general/latest/gr/securitylake.html) in the *AWS General Reference*.

For example, the following command sets `ap-northeast-2` as a rollup Region. The `us-east-1` Region will contribute data to the `ap-northeast-2` Region. This example also establishes a 365-day expiration period for objects that are added to the data lake. This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\\) line-continuation character to improve readability.

```
$ aws securitylake update-data-lake \
--configurations '[{"encryptionConfiguration": {"kmsKeyId":"{{S3_MANAGED_KEY}}"},"region":"{{us-east-1}}","replicationConfiguration": {"regions": ["{{ap-northeast-2}}"],"roleArn":"{{arn:aws:iam::123456789012:role/service-role/AmazonSecurityLakeS3ReplicationRole}}"},"lifecycleConfiguration": {"expiration":{"days":{{365}}}}}]'
```

You can also add a rollup Region when you onboard to Security Lake. To do this, use the [CreateDataLake](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateDataLake.html) operation (or, if using the AWS CLI, the [create-data-lake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/update-data-lake.html) command). For more information about configuring rollup Regions during onboarding, see [Getting started with Amazon Security Lake](getting-started.md).

------

## Updating or removing rollup Regions
<a name="procedures-update-remove-rollup-region"></a>

Choose your preferred access method, and follow these steps to update or remove rollup Regions in Security Lake.

------
#### [ Console ]

1. Open the Security Lake console at [https://console.aws.amazon.com/securitylake/](https://console.aws.amazon.com/securitylake/).

1. In the navigation pane, under **Settings**, choose **Rollup Regions**.

1. Choose **Modify**.

1. To change the contributing Regions for a rollup Region, specify the updated contributing Regions in the row for rollup Region.

1. To remove a rollup Region, choose **Remove** in the row for rollup Region.

1. When you finish, choose **Save**.

------
#### [ API ]

To configure rollup Regions programmatically, use the [UpdateDataLake](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_UpdateDataLake.html) operation of the Security Lake API. If you're using the AWS CLI, run the [update-data-lake](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securitylake/update-data-lake.html) command. In your request, use the supported parameters to specify the rollup settings:
+ To add a contributing Region, use the `region` field to specify the Region code for the Region to add. In the `regions` array of the `replicationConfiguration` object, specify the Region code for each rollup Region to contribute data to. For a list of Region codes, see [Amazon Security Lake endpoints](https://docs.aws.amazon.com/general/latest/gr/securitylake.html) in the *AWS General Reference*.
+ To remove a contributing Region, use the `region` field to specify the Region code for the Region to remove. For the `replicationConfiguration` parameters, don't specify any values.

For example, the following command configures both `us-east-1` and `us-east-2` as contributing Regions. Both Regions will contribute data to the `ap-northeast-3` rollup Region. This example is formatted for Linux, macOS, or Unix, and it uses the backslash (\\) line-continuation character to improve readability.

```
$ aws securitylake update-data-lake \
--configurations '[{"encryptionConfiguration": {"kmsKeyId":"{{S3_MANAGED_KEY}}"},"region":"{{us-east-1}}","replicationConfiguration": {"regions": ["{{ap-northeast-3}}"],"roleArn":"{{arn:aws:iam::123456789012:role/service-role/AmazonSecurityLakeS3ReplicationRole}}"},"lifecycleConfiguration": {"expiration":{"days":{{365}}}}},
{"encryptionConfiguration": {"kmsKeyId":"{{S3_MANAGED_KEY}}"},"region":"{{us-east-2}}","replicationConfiguration": {"regions": ["{{ap-northeast-3}}"],"roleArn":"{{arn:aws:iam::123456789012:role/service-role/AmazonSecurityLakeS3ReplicationRole}}"}, "lifecycleConfiguration": {"expiration":{"days":{{500}}},"transitions":[{"days":{{60}},"storageClass":"{{ONEZONE_IA}}"}]}}]'
```

------