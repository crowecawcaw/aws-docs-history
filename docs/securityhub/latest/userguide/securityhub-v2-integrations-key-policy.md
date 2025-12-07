# KMS key policies for Security Hub ticketing integrations

When using customer-managed KMS keys with Security Hub ticketing integrations, additional policies need to be added to the KMS key to allow Security Hub to interact with the key.
Additionally, policies need to be added which allow the principal who is adding the key to the Security Hub connector permissions to access the key.

## Security Hub permissions policy

The following policy outlines the permissions that Security Hub needs to be able to access and use the KMS key that is associated with your Jira and ServiceNow connectors.
This policy needs to be added to each KMS key that is associated with a Security Hub connector.

The policy contains the following permissions:

- Permits Security Hub to protect, temporary access or refresh tokens used to communicate with your ticketing integrations, using the key.
  The permissions are restricted to operations related to specific Security Hub connectors through the condition block that checks the source ARN and encryption context.
- Permits Security Hub to read metadata about the KMS key by allowing the `DescribeKey` operation.
  This permission is necessary for Security Hub to verify the key's status and configuration.
  The access is limited to specific Security Hub connectors through the source ARN condition.

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
            "aws:SourceArn": "arn:aws:securityhub:`Region`:`AccountId`:connectorv2/*"
        },
        "StringLike": {
            "kms:EncryptionContext:aws:securityhub:connectorV2Arn": "arn:aws:securityhub:`Region`:`AccountId`:connectorv2/*",
            "kms:EncryptionContext:aws:securityhub:providerName": "`CloudProviderName`"
        }
    }
},
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
            "aws:SourceArn": "arn:aws:securityhub:`Region`:`AccountId`:connectorv2/*"
        }
    }
}

```

Edit the policy by replacing the following values in the policy example:

- Replace `CloudProviderName` with `JIRA_CLOUD` or `SERVICENOW`
- Replace `AccountId` with the account ID where you are creating the Security Hub connector.
- Replace `Region` with your AWS region (for example, `us-east-1`).

## IAM principal access for Security Hub operations

Any principal that will be assigning customer-managed KMS keys to a Security Hub connector needs to have permissions to perform key operations (describe, generate, decrypt, re-encrypt, and list aliases) for the key being added to the connector.
This applies to the [`CreateConnectorV2`](../../1.0/APIReference/API_CreateConnectorV2.md "../../1.0/APIReference/API_CreateConnectorV2.md") and [`CreateTicketV2`](../../1.0/APIReference/API_CreateTicketV2.md "../../1.0/APIReference/API_CreateTicketV2.md") APIs.
The following policy statement should be included as part of the policy for any principal that will be interacting with these APIs.

```

{
    "Sid": "Allow permissions to access key through Security Hub",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::`AccountId`:role/`RoleName`"
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
                "securityhub.`Region`.amazonaws.com"
            ]
        },
        "StringLike": {
            "kms:EncryptionContext:aws:securityhub:providerName": "`CloudProviderName`"
        }
    }
},
{
    "Sid": "Allow read permissions to access key through Security Hub",
    "Effect": "Allow",
    "Principal": {
        "AWS": "arn:aws:iam::`AccountId`:role/`RoleName`"
    },
    "Action": [
        "kms:DescribeKey"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:ViaService": [
                "securityhub.`Region`.amazonaws.com"
            ]
        }
    }
}

```

Edit the policy by replacing the following values in the policy example:

- Replace `RoleName` with the name of the IAM role that's making calls to Security Hub.
- Replace `CloudProviderName` with `JIRA_CLOUD` or `SERVICENOW`.
- Replace `AccountId` with the account ID where you are creating the Security Hub connector.
- Replace `Region` with your AWS region (for example, `us-east-1`).
