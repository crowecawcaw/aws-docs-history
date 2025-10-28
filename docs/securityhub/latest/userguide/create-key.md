# Create an KMS key to encrypt credentials

The integration procedures in this section provide you with an option to encrypt your credentials with an AWS owned key or customer managed key.
An AWS owned key is a KMS key not in your AWS account because the AWS service that encrypts your credentials owns and manages the KMS key.
If you want total control over the KMS key used to encrypt your credentials, [create a customer managed key](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md").
A customer managed key is a KMS key that you own and manage.

###### Security Hub encryption operations access

This policy statement allows Security Hub to use the AWS KMS key for encryption operations.
It permits Security Hub to protect your client secrets using this key.
The permissions are restricted to operations related to specific Security Hub connectors through the condition block that checks the source ARN and encryption context.

```
{
    "Sid": "Allow Security Hub access to the customer managed key",
    "Effect": "Allow",
    "Principal": {
        "Service": "connector.securityhub.amazonaws.com"
    },
    "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt",
        "kms:ReEncrypt*"
    ],
    "Resource": "*",
    "Condition": {
        "ArnLike": {
            "aws:SourceArn": "arn:aws:securityhub:${`Region`}:${`AccountId`}:connectorv2/*"
        },
        "StringLike": {
            "kms:EncryptionContext:aws:securityhub:connectorV2Arn": "arn:aws:securityhub:${`Region`}:${`AccountId`}:connectorv2/*",
            "kms:EncryptionContext:aws:securityhub:providerName": "${CloudProviderName}"
        }
    }
}
```

###### Note

For `CloudProviderName`, enter `JIRA_CLOUD` or `SERVICENOW`.
For `Region` and `AccountId`, enter your AWS Region and AWS account ID.

###### Security Hub key read access

This policy statement enables Security Hub to read metadata about the KMS key by allowing the `DescribeKey` operation.
This permission is necessary for Security Hub to verify the key's status and configuration.
The access is limited to specific Security Hub connectors through the source ARN condition.

```
{
    "Sid": "Allow Security Hub read access to the customer managed key",
    "Effect": "Allow",
    "Principal": {
        "Service": "connector.securityhub.amazonaws.com"
    },
    "Action": [
        "kms:DescribeKey"
    ],
    "Resource": "*",
    "Condition": {
        "ArnLike": {
            "aws:SourceArn": "arn:aws:securityhub:${`Region`}:${`AccountId`}:connectorv2/*"
        }
    }
}
```

###### Note

For `Region` and `AccountId`, enter your AWS Region and AWS account ID.

###### IAM principal access for Security Hub operations

This policy statement grants the specified IAM role permissions to perform key operations (describe, generate, decrypt, re-encrypt, and list aliases) when interacting with Security Hub using the [CreateConnectorV2](../../1.0/APIReference/API_CreateConnectorV2.md "../../1.0/APIReference/API_CreateConnectorV2.md") and [CreateTicketV2](../../1.0/APIReference/API_CreateTicketV2.md "../../1.0/APIReference/API_CreateTicketV2.md") APIs.
The condition ensures these operations can only be performed through the Security Hub service in the specified region.

```
{
    "Sid": "Allow permissions to access key through Security Hub",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::${`AccountId`}:role/${`RoleName`}"
    },
    "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt",
        "kms:ReEncrypt*"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:ViaService": [
                "securityhub.${`Region`}.amazonaws.com"
            ]
        },
        StringLike": {
            "kms:EncryptionContext:aws:securityhub:providerName": "SERVICENOW"
        }
    }
}

{
    "Sid": "Allow read permissions to access key through Security Hub",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::${`AccountId`}:role/${`RoleName`}"
    },
    "Action": [
        "kms:DescribeKey"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:ViaService": [
                "securityhub.${`Region`}.amazonaws.com"
            ]
        }
    }
}


```

###### Note

For `RoleName`, enter the name of the IAM role that's making calls to Security Hub.
For `Region` and `AccountId`, enter your AWS Region and AWS account ID.
