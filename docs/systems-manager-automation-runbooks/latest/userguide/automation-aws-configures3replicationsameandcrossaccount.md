# `AWSSupport-ConfigureS3ReplicationSameAndCrossAccount`

**Description**

The `AWSSupport-ConfigureS3ReplicationSameAndCrossAccount` automation runbook configures Amazon Simple Storage Service (Amazon S3) bucket replication between a source and destination bucket for same or cross accounts. This automation supports replication of buckets encrypted with Server-Side Encryption with Amazon S3-Managed Keys (SSE-S3) and Server-Side Encryption with AWS Key Management Service (SSE-KMS). It also supports prefix and tag-based selective replication filtering, Amazon S3 Replication Time Control (Amazon S3 RTC) with 15-minute SLA, and delete marker replication. The automation performs the following actions:

- Validates input parameters and bucket configurations for compatibility.
- Checks encryption settings on both source and destination buckets.
- Creates a new AWS Identity and Access Management (IAM) role with appropriate permissions for replication if not provided as an input.
- Configures replication rules based on specified parameters (prefix, tags, or entire bucket).
- Enables bucket versioning if not already enabled.
- Sets up replication configuration with optional features like Replication Time Control (RTC) and delete marker replication.

###### Important

- **This automation does not support buckets with existing replication rules.** The source bucket must not have any existing replication configuration.
- **This automation creates a new IAM role** with appropriate permissions for replication if S3ReplicationRole input is not provided.
- **This automation does not replicate existing objects.** Amazon S3 replication only applies to objects uploaded/created after the replication configuration is enabled.
- For cross-account replication, you must provide an IAM role in the destination account with appropriate permissions for Amazon S3 operations and AWS KMS operations (if bucket uses AWS KMS encryption).
- This automation uses the `aws:approve` action, which temporarily pauses execution until the designated principals approve the configuration changes. See [Running an automation with approvers](../../../systems-manager/latest/userguide/running-automations-require-approvals.md "../../../systems-manager/latest/userguide/running-automations-require-approvals.md") for more information.

**How does it work?**

The runbook performs the following steps:

- **ValidateInputParameters**: Validates all input parameters for correctness and compatibility to ensure proper replication configuration.
- **PrepareApprovalMessage**: Prepares an approval message with all replication configuration parameters for user review.
- **RequestApproval**: Requests approval from authorized users before adding Amazon S3 replication configuration on the source bucket.
- **CheckBucketEncryption**: Checks encryption configuration for both source and destination Amazon S3 buckets to determine compatible replication settings.
- **BranchOnEncryptionType**: Branches execution based on Amazon S3 bucket encryption type to apply appropriate replication configuration for SSE-S3 or SSE-KMS encrypted buckets.
- **ConfigureSSES3Replication**: Configures Amazon S3 replication for buckets encrypted with Server-Side Encryption with Amazon S3-Managed Keys (SSE-S3), including IAM roles and replication rules.
- **ConfigureSSEKMSReplication**: Configures Amazon S3 replication for buckets encrypted with Server-Side Encryption with AWS KMS (SSE-KMS), including IAM roles, KMS key permissions, and replication rules.
- **CleanupResources**: Cleans up IAM role created during failed replication configuration when S3ReplicationRole is not provided as an input.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-ConfigureS3ReplicationSameAndCrossAccount "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-ConfigureS3ReplicationSameAndCrossAccount")

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- s3:ListBucket
- s3:GetBucketVersioning
- s3:GetEncryptionConfiguration
- s3:GetBucketLocation
- s3:GetReplicationConfiguration
- s3:PutBucketVersioning
- s3:PutReplicationConfiguration
- iam:ListRoles
- iam:GetRole
- iam:GetRolePolicy
- iam:ListRoleTags
- iam:ListAttachedRolePolicies
- iam:ListRolePolicies
- iam:SimulatePrincipalPolicy
- iam:CreateRole
- iam:TagRole
- iam:PassRole
- iam:DeleteRole
- iam:DeleteRolePolicy
- iam:DetachRolePolicy
- iam:PutRolePolicy
- sts:GetCallerIdentity
- sns:Publish
- kms:GetKeyPolicy (when buckets use SSE-KMS, same-account replication)
- kms:DescribeKey (when buckets use SSE-KMS, same-account replication)
- kms:PutKeyPolicy (when buckets use SSE-KMS, same-account replication)
- sts:AssumeRole (for cross-account replication)
  **CrossAccountReplicationRole (for cross-account scenarios):**

For cross-account replication, you must provide a CrossAccountReplicationRole in the destination account with the following permissions:

- s3:ListBucket
- s3:GetBucketVersioning
- s3:GetBucketLocation
- s3:GetBucketPolicy
- s3:GetEncryptionConfiguration
- s3:PutBucketVersioning
- s3:PutBucketPolicy
- kms:GetKeyPolicy (when cross-account destination bucket use SSE-KMS)
- kms:DescribeKey (when cross-account destination bucket use SSE-KMS)
- kms:PutKeyPolicy (when cross-account destination bucket use SSE-KMS)
  **S3ReplicationRole (customer-provided role):**

If you provide an existing S3ReplicationRole, it must have the following permissions:

- s3:ListBucket
- s3:GetBucketLocation
- s3:GetReplicationConfiguration
- s3:GetObjectVersionAcl
- s3:GetObjectVersionTagging
- s3:GetObjectVersionForReplication
- s3:GetObjectTagging
- s3:ReplicateObject
- s3:ReplicateDelete
- s3:ReplicateTags
- s3:ObjectOwnerOverrideToBucketOwner
- kms:Decrypt (for SSE-KMS scenarios, source KMS key)
- kms:Encrypt (for SSE-KMS scenarios, destination KMS key)
- kms:GenerateDataKey (for SSE-KMS scenarios, destination KMS key)
- kms:ReEncrypt\* (for SSE-KMS scenarios, destination KMS key)
  Example **AutomationAssumeRole** policy for **same-account replication**:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3Permissions",
            "Effect": "Allow",
            "Action": [
                "s3:GetBucketVersioning",
                "s3:GetEncryptionConfiguration",
                "s3:GetBucketLocation",
                "s3:GetReplicationConfiguration",
                "s3:ListBucket",
                "s3:PutBucketVersioning",
                "s3:PutReplicationConfiguration"
            ],
            "Resource": [
                "arn:aws:s3:::SOURCE_BUCKET",
                "arn:aws:s3:::DESTINATION_BUCKET"
            ]
        },
        {
            "Sid": "IAMReadOperations",
            "Effect": "Allow",
            "Action": [
                "iam:GetRole",
                "iam:GetRolePolicy",
                "iam:ListRoleTags",
                "iam:ListAttachedRolePolicies",
                "iam:ListRolePolicies",
                "iam:SimulatePrincipalPolicy"
            ],
            "Resource": "*"
        },
        {
            "Sid": "IAMListRolesForCleanup",
            "Effect": "Allow",
            "Action": "iam:ListRoles",
            "Resource": "*"
        },
        {
            "Sid": "IAMCreateAndTagRole",
            "Effect": "Allow",
            "Action": [
                "iam:CreateRole",
                "iam:TagRole"
            ],
            "Resource": "arn:aws:iam::ACCOUNT_ID:role/S3RepRole-*",
            "Condition": {
                "StringLike": {
                    "aws:RequestTag/AWSSupport-ConfigureS3ReplicationSameAndCrossAccount": "*"
                }
            }
        },
        {
            "Sid": "IAMPassRole",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::ACCOUNT_ID:role/S3RepRole-*",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "s3.amazonaws.com"
                }
            }
        },
        {
            "Sid": "TaggedIAMRoleModifyAndDeleteOperations",
            "Effect": "Allow",
            "Action": [
                "iam:DeleteRole",
                "iam:DeleteRolePolicy",
                "iam:DetachRolePolicy",
                "iam:PutRolePolicy"
            ],
            "Resource": "arn:aws:iam::ACCOUNT_ID:role/S3RepRole-*",
            "Condition": {
                "StringLike": {
                    "aws:ResourceTag/AWSSupport-ConfigureS3ReplicationSameAndCrossAccount": "*"
                }
            }
        },
        {
            "Sid": "STSGetCallerIdentity",
            "Effect": "Allow",
            "Action": "sts:GetCallerIdentity",
            "Resource": "*"
        },
        {
            "Sid": "SNSPublish",
            "Effect": "Allow",
            "Action": "sns:Publish",
            "Resource": "SNS_TOPIC_ARN"
        },
        {
            "Sid": "KMSKeyReadOperations",
            "Effect": "Allow",
            "Action": [
                "kms:GetKeyPolicy",
                "kms:DescribeKey"
            ],
            "Resource": [
                "arn:aws:kms:REGION:ACCOUNT_ID:key/SOURCE_KMS_KEY_ID",
                "arn:aws:kms:REGION:ACCOUNT_ID:key/DESTINATION_KMS_KEY_ID"
            ]
        },
        {
            "Sid": "KMSKeyMutatingOperations",
            "Effect": "Allow",
            "Action": "kms:PutKeyPolicy",
            "Resource": [
                "arn:aws:kms:REGION:ACCOUNT_ID:key/SOURCE_KMS_KEY_ID",
                "arn:aws:kms:REGION:ACCOUNT_ID:key/DESTINATION_KMS_KEY_ID"
            ],
            "Condition": {
                "StringEquals": {
                    "kms:CallerAccount": "ACCOUNT_ID"
                }
            }
        }
    ]
}

```

###### Note

The Policy statements (KMSKeyReadOperations and KMSKeyMutatingOperations) are only required when buckets use SSE-KMS encryption.

Example **AutomationAssumeRole** policy for **cross-account replication**:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3SourceBucketOperations",
            "Effect": "Allow",
            "Action": [
                "s3:GetBucketVersioning",
                "s3:GetEncryptionConfiguration",
                "s3:GetBucketLocation",
                "s3:GetReplicationConfiguration",
                "s3:ListBucket",
                "s3:PutBucketVersioning",
                "s3:PutReplicationConfiguration"
            ],
            "Resource": "arn:aws:s3:::SOURCE_BUCKET"
        },
        {
            "Sid": "IAMReadOperations",
            "Effect": "Allow",
            "Action": [
                "iam:GetRole",
                "iam:GetRolePolicy",
                "iam:ListRoleTags",
                "iam:ListAttachedRolePolicies",
                "iam:ListRolePolicies",
                "iam:SimulatePrincipalPolicy"
            ],
            "Resource": "*"
        },
        {
            "Sid": "IAMListRolesForCleanup",
            "Effect": "Allow",
            "Action": "iam:ListRoles",
            "Resource": "*"
        },
        {
            "Sid": "IAMCreateAndTagRole",
            "Effect": "Allow",
            "Action": [
                "iam:CreateRole",
                "iam:TagRole"
            ],
            "Resource": "arn:aws:iam::SOURCE_ACCOUNT_ID:role/S3RepRole-*",
            "Condition": {
                "StringLike": {
                    "aws:RequestTag/AWSSupport-ConfigureS3ReplicationSameAndCrossAccount": "*"
                }
            }
        },
        {
            "Sid": "IAMPassRole",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::SOURCE_ACCOUNT_ID:role/S3RepRole-*",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "s3.amazonaws.com"
                }
            }
        },
        {
            "Sid": "TaggedIAMRoleModifyAndDeleteOperations",
            "Effect": "Allow",
            "Action": [
                "iam:DeleteRole",
                "iam:DeleteRolePolicy",
                "iam:DetachRolePolicy",
                "iam:PutRolePolicy"
            ],
            "Resource": "arn:aws:iam::SOURCE_ACCOUNT_ID:role/S3RepRole-*",
            "Condition": {
                "StringLike": {
                    "aws:ResourceTag/AWSSupport-ConfigureS3ReplicationSameAndCrossAccount": "*"
                }
            }
        },
        {
            "Sid": "CrossAccountRoleAssumption",
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": "CROSS_ACCOUNT_REPLICATION_ROLE_ARN"
        },
        {
            "Sid": "STSGetCallerIdentity",
            "Effect": "Allow",
            "Action": "sts:GetCallerIdentity",
            "Resource": "*"
        },
        {
            "Sid": "SNSPublish",
            "Effect": "Allow",
            "Action": "sns:Publish",
            "Resource": "SNS_TOPIC_ARN"
        },
        {
            "Sid": "KMSSourceKeyReadOperations",
            "Effect": "Allow",
            "Action": [
                "kms:GetKeyPolicy",
                "kms:DescribeKey"
            ],
            "Resource": "arn:aws:kms:SOURCE_REGION:SOURCE_ACCOUNT_ID:key/SOURCE_KMS_KEY_ID"
        },
        {
            "Sid": "KMSSourceKeyMutatingOperations",
            "Effect": "Allow",
            "Action": "kms:PutKeyPolicy",
            "Resource": "arn:aws:kms:SOURCE_REGION:SOURCE_ACCOUNT_ID:key/SOURCE_KMS_KEY_ID",
            "Condition": {
                "StringEquals": {
                    "kms:CallerAccount": "SOURCE_ACCOUNT_ID"
                }
            }
        }
    ]
}

```

###### Note

- The Policy statements (KMSSourceKeyReadOperations and KMSSourceKeyMutatingOperations) are only required when the source bucket uses SSE-KMS encryption.
- Replace CROSS_ACCOUNT_REPLICATION_ROLE_ARN with the actual CrossAccountReplicationRole parameter value you provide to the automation.
  Example **CrossAccountReplicationRole** policy:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3DestinationBucketReadOperations",
            "Effect": "Allow",
            "Action": [
                "s3:GetBucketVersioning",
                "s3:GetBucketLocation",
                "s3:GetBucketPolicy",
                "s3:GetEncryptionConfiguration",
                "s3:ListBucket",
                "s3:PutBucketVersioning",
                "s3:PutBucketPolicy"
            ],
            "Resource": "arn:aws:s3:::DESTINATION_BUCKET"
        },
        {
            "Sid": "KMSDestinationKeyReadOperations",
            "Effect": "Allow",
            "Action": [
                "kms:GetKeyPolicy",
                "kms:DescribeKey"
            ],
            "Resource": "arn:aws:kms:DESTINATION_REGION:DESTINATION_ACCOUNT_ID:key/DESTINATION_KMS_KEY_ID"
        },
        {
            "Sid": "KMSDestinationKeyMutatingOperations",
            "Effect": "Allow",
            "Action": "kms:PutKeyPolicy",
            "Resource": "arn:aws:kms:DESTINATION_REGION:DESTINATION_ACCOUNT_ID:key/DESTINATION_KMS_KEY_ID",
            "Condition": {
                "StringEquals": {
                    "kms:CallerAccount": "DESTINATION_ACCOUNT_ID"
                }
            }
        }
    ]
}

```

###### Note

The KMS statements (KMSDestinationKeyReadOperations and KMSDestinationKeyMutatingOperations) are only required when the destination bucket uses SSE-KMS encryption. Remove these statements for SSE-S3 scenarios.

Example CrossAccountReplicationRole trust policy:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "AUTOMATION_ASSUME_ROLE_ARN"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

```

###### Note

Replace AUTOMATION_ASSUME_ROLE_ARN with the actual AutomationAssumeRole parameter value you provide to the automation.

Example **S3ReplicationRole** policy:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3SourceBucketPermissions",
            "Effect": "Allow",
            "Action": [
                "s3:ListBucket",
                "s3:GetBucketLocation",
                "s3:GetReplicationConfiguration",
                "s3:GetObjectVersionAcl",
                "s3:GetObjectVersionTagging",
                "s3:GetObjectVersionForReplication",
                "s3:GetObjectTagging"
            ],
            "Resource": [
                "arn:aws:s3:::SOURCE_BUCKET",
                "arn:aws:s3:::SOURCE_BUCKET/*"
            ]
        },
        {
            "Sid": "S3DestinationBucketPermissions",
            "Effect": "Allow",
            "Action": [
                "s3:ReplicateObject",
                "s3:ReplicateDelete",
                "s3:ReplicateTags"
            ],
            "Resource": "arn:aws:s3:::DESTINATION_BUCKET/*"
        },
        {
            "Sid": "S3CrossAccountPermissions",
            "Effect": "Allow",
            "Action": "s3:ObjectOwnerOverrideToBucketOwner",
            "Resource": "arn:aws:s3:::DESTINATION_BUCKET/*"
        },
        {
            "Sid": "KMSSourceKeyPermissions",
            "Effect": "Allow",
            "Action": "kms:Decrypt",
            "Resource": "arn:aws:kms:SOURCE_REGION:SOURCE_ACCOUNT_ID:key/SOURCE_KMS_KEY_ID"
        },
        {
            "Sid": "KMSDestinationKeyPermissions",
            "Effect": "Allow",
            "Action": [
                "kms:Encrypt",
                "kms:GenerateDataKey",
                "kms:ReEncrypt*"
            ],
            "Resource": "arn:aws:kms:DESTINATION_REGION:DESTINATION_ACCOUNT_ID:key/DESTINATION_KMS_KEY_ID"
        }
    ]
}

```

###### Note

- The KMS statements (KMSSourceKeyPermissions and KMSDestinationKeyPermissions) are only required when buckets use SSE-KMS encryption.
- The S3CrossAccountPermissions statement is only required for cross-account bucket replication.
  Example S3ReplicationRole trust policy:

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "s3.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

```

**Instructions**

Follow these steps to configure the automation:

1. Navigate to [`AWSSupport-ConfigureS3ReplicationSameAndCrossAccount`](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-ConfigureS3ReplicationSameAndCrossAccount/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-ConfigureS3ReplicationSameAndCrossAccount/description") in Systems Manager under Documents.
2. Select **Execute automation.**
3. For the input parameters, enter the following:
   - **AutomationAssumeRole (Required):**
     - Description: (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.
     - Type: `AWS::IAM::Role::Arn`

   - **SourceBucket (Required):**
     - Description: (Required) The name of the source Amazon S3 bucket where replication rules will be created or updated.
     - Type: `AWS::S3::Bucket::Name`

   - **DestinationBucket (Required):**
     - Description: (Required) The name of the destination Amazon S3 bucket where objects will be replicated to.
     - Type: `String`
     - Allowed Pattern: `^[0-9a-z][a-z0-9\\-\\.]{3,63}$`

   - **SourceAccountId (Required):**
     - Description: (Required) The AWS Account ID where the source bucket is located.
     - Type: `String`
     - Allowed Pattern: `^[0-9]{12,13}$`

   - **DestinationAccountId (Required):**
     - Description: (Required) The AWS Account ID where the destination bucket is located.
     - Type: `String`
     - Allowed Pattern: `^[0-9]{12,13}$`

   - **SnsNotificationArn (Required):**
     - Description: (Required) The ARN of an Amazon Simple Notification Service (Amazon SNS) topic for Automation approvals.
     - Type: `String`
     - Allowed Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso(-[a-z])?):sns:[a-z]{2}(-gov)?(-iso[a-z]?)?-[a-z]{2,10}-[0-9]{1,2}:\\d{12}:[0-9a-zA-Z-_]{1,256}(.fifo)?$`

   - **Approvers (Required):**
     - Description: (Required) The list of IAM user/role ARNs authorized to approve the automation execution.
     - Type: `StringList`
     - Allowed Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-iso(-[a-z])?):iam::\\d{12}:(user|role)/[\\w+=,.@\\-/]+$`

   - **S3ReplicationRole (Optional):**
     - Description: (Optional) The ARN of an existing IAM role to use for Amazon S3 replication operations. This role must have permissions to read from the source bucket and write to the destination bucket, including KMS permissions if buckets use SSE-KMS encryption. If not provided, the automation will create a new role with appropriate permissions.
     - Type: `String`
     - Allowed Pattern: `^$|^arn:(aws|aws-cn|aws-us-gov|aws-iso(-[a-z])?):iam::\\d{12}:role/[\\w+=,.@\\-/]+$`
     - Default: `""`

   - **CrossAccountReplicationRole (Optional):**
     - Description: (Optional) The ARN of an IAM role in the destination account that the automation can assume. This is required for cross-account replication. For same-account replication, leave this empty.
     - Type: `String`
     - Allowed Pattern: `^$|^arn:(aws|aws-cn|aws-us-gov|aws-iso(-[a-z])?):iam::\\d{12}:role/[\\w+=,.@\\-/]+$`
     - Default: `""`

   - **ReplicateEntireBucket (Optional):**
     - Description: (Optional) If set to `true`, the entire bucket will be replicated and both Prefix and Tags must be empty. If false, replication will be based on specified prefix or tags.
     - Type: `Boolean`
     - Allowed Values: `[true, false]`
     - Default: `true`

   - **ReplicationRuleStatus (Optional):**
     - Description: (Optional) If set to `true`, replication rules created will be enabled. If set to `false`, replication rules created will be set to **Disabled**.
     - Type: `Boolean`
     - Allowed Values: `[true, false]`
     - Default: `true`

   - **DeleteMarkerReplicationStatus (Optional):**
     - Description: (Optional) If set to `true`, the automation enables delete marker replication.
     - Type: `Boolean`
     - Allowed Values: `[true, false]`
     - Default: `false`

   - **ReplicationTimeControl (Optional):**
     - Description: (Optional) If set to `true`, enables Amazon S3 Replication Time Control (Amazon S3 RTC) with 15-minute SLA for predictable replication times.
     - Type: `Boolean`
     - Allowed Values: `[true, false]`
     - Default: `false`

   - **ReplicaModifications (Optional):**
     - Description: (Optional) If set to `true`, enables replication of metadata changes made to replica objects, allowing modifications to replicated objects to be synchronized back to the source.
     - Type: `Boolean`
     - Allowed Values: `[true, false]`
     - Default: `false`

   - **Prefix (Optional):**
     - Description: (Optional) Prefix filter for selective replication of objects with specific key prefixes. Prefix must end with a trailing slash (/) for proper Amazon S3 prefix filtering.
     - Type: `String`
     - Allowed Pattern: `^$|^[a-zA-Z0-9!_'()\\-]*/+$`
     - Default: `""`

   - **Tags (Optional):**
     - Description: (Optional) JSON array of tags for filtering objects to replicate. Format for single tag: [{"Key":"TagKey","Value":"TagValue"}] and for multiple tags: [{"Key":"TagKey1","Value":"TagValue1"},{"Key":"TagKey2","Value":"TagValue2"}].
     - Type: `String`
     - Allowed Pattern: `^\\[((\\{\"Key\":\"[a-zA-Z0-9+\\-=.:/ @\\s]{1,128}\",\"Value\":\"[a-zA-Z0-9+\\-=.:/@\\s]{0,256}\"\\})(,\\{\"Key\":\"[a-zA-Z0-9+\\-=.:/ @\\s]{1,128}\",\"Value\":\"[a-zA-Z0-9+\\-=.:/@\\s]{0,256}\"\\})*)?\\]$`
     - Default: `[]`

4. Select **Execute.**
5. The automation initiates.
6. The document performs the following steps:
   - **ValidateInputParameters**:

   Validates all input parameters for correctness and compatibility to ensure proper replication configuration.
   - **PrepareApprovalMessage**:

   Prepares the approval message with all replication configuration parameters for user review.
   - **RequestApproval**:

   Requests approval from authorized users before proceeding with Amazon S3 replication configuration changes.
   - **CheckBucketEncryption**:

   Checks encryption configuration for both source and destination Amazon S3 buckets to determine compatible replication settings.
   - **BranchOnEncryptionType**:

   Branches execution based on Amazon S3 bucket encryption type to apply appropriate replication configuration for SSE-S3 or SSE-KMS encrypted buckets.
   - **ConfigureSSES3Replication**:

   Configures Amazon S3 replication for buckets encrypted with Server-Side Encryption with Amazon S3-Managed Keys (SSE-S3), including IAM roles and replication rules.
   - **ConfigureSSEKMSReplication**:

   Configures Amazon S3 replication for buckets encrypted with Server-Side Encryption with AWS KMS (SSE-KMS), including IAM roles, KMS key permissions, and replication rules.
   - **CleanupResources**:

   Cleans up IAM roles created during failed replication configuration when S3ReplicationRole was not provided by the customer.

7. After completion, review the outputs from the **ConfigureSSES3Replication** step (for SSE-S3 encrypted buckets) or the **ConfigureSSEKMSReplication** step (for SSE-KMS encrypted buckets) for the results of the execution, including replication configuration status along with the IAM role used for Replication.
   **References**

Systems Manager Automation

- [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-ConfigureS3ReplicationSameAndCrossAccount/description "https://console.aws.amazon.com/systems-manager/documents/AWSSupport-ConfigureS3ReplicationSameAndCrossAccount/description")
- [Run an automation](../../../systems-manager/latest/userguide/automation-working-executing.md "../../../systems-manager/latest/userguide/automation-working-executing.md")
- [Setting up an Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md")
- [Support Automation Workflows](https://aws.amazon.com/premiumsupport/technology/saw/ "https://aws.amazon.com/premiumsupport/technology/saw/")
