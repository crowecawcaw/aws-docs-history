

# Encrypting OpenSearch UI application metadata with customer managed keys

Visual assets and configurations are stored as metadata for your OpenSearch UI applications. This includes saved queries, visualizations, and dashboards. Data from the associated data sources is not stored in the metadata. For information about encrypting data in your data sources, see [Data protection in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/data-protection.html) for OpenSearch domains and [Encryption in Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html) for serverless collections.

Your OpenSearch UI metadata is protected with encryption at rest. This prevents unauthorized access. The encryption uses AWS Key Management Service (AWS KMS) to store and manage the encryption keys. By default, OpenSearch UI metadata is encrypted with AWS owned keys.

You can also use the customer managed key (CMK) feature to manage your own encryption keys. This helps you meet regulatory and compliance requirements. To use CMK, you must create a new OpenSearch UI application and enable CMK in the creation process. It is not currently supported to update an existing OpenSearch UI application from AWS owned key to CMK.

When to use customer managed keys:
+ Your organization has regulatory compliance requirements for key management
+ You need audit trails for encryption key usage
+ You want to control key rotation schedules
+ You need to integrate with existing key management workflows

When you use a customer managed key, you have full control over the key. This includes the ability to:
+ Establish and maintain key policies
+ Establish and maintain IAM policies and grants
+ Enable and disable the key
+ Rotate the key's cryptographic material
+ Add tags to the key
+ Create key aliases
+ Schedule the key for deletion

**Note**  
The customer managed key must be in the same AWS Region as the OpenSearch UI application. You cannot use a key from a different Region.

**Topics**
+ [Prerequisites for using customer managed keys](#application-encryption-cmk-prerequisites)
+ [Enabling customer managed key encryption for AI Assistant Memory](#application-encryption-cmk-agentic-memory)
+ [Creating an application with customer managed key encryption using the console](#application-encryption-cmk-create-console)
+ [Creating an application with customer managed key encryption using the AWS CLI](#application-encryption-cmk-create-cli)
+ [Monitoring customer managed key usage](#application-encryption-cmk-monitoring)
+ [Updating encryption settings](#application-encryption-cmk-update)

## Prerequisites for using customer managed keys
<a name="application-encryption-cmk-prerequisites"></a>

Before you can use a customer managed key to encrypt your OpenSearch UI application metadata, you must create a symmetric encryption key in AWS KMS. For instructions on creating keys, see [Creating keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS KMS Developer Guide*.

The key policy for your customer managed key must grant OpenSearch UI permission to use the key. Use the following key policy, replacing the {{placeholder values}} with your own information:

```json
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowOpenSearchUIToUseKey",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "application.opensearchservice.amazonaws.com"
                ]
            },
            "Action": [
                "kms:Encrypt",
                "kms:Decrypt",
                "kms:GenerateDataKey",
                "kms:DescribeKey"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AllowOpenSearchUIToCreateGrantForAIAssistantMemory",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "application.opensearchservice.amazonaws.com"
                ]
            },
            "Action": "kms:CreateGrant",
            "Resource": "*",
            "Condition": {
                "Bool": {
                    "kms:GrantIsForAWSResource": "true"
                },
                "ForAllValues:StringEquals": {
                    "kms:GrantOperations": [
                        "Decrypt",
                        "GenerateDataKey"
                    ]
                }
            }
        },
        {
            "Sid": "AllowKeyAdministration",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:root"
            },
            "Action": "kms:*",
            "Resource": "*"
        }
    ]
}
```

The policy includes three statements:
+ The first statement allows OpenSearch UI to use the key for encryption operations.
+ The second statement allows OpenSearch UI to create an AWS KMS grant on the key so that it can encrypt AI Assistant Memory data for the agentic AI features. For more information, see [Enabling customer managed key encryption for AI Assistant Memory](#application-encryption-cmk-agentic-memory).
+ The third statement allows users in your AWS account to administer the key. This includes permissions to update the key policy, enable or disable the key, and schedule the key for deletion. You can further restrict these permissions by replacing the root principal with specific IAM users or roles.

For more information about key policies, see [Using key policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the *AWS KMS Developer Guide*.

## Enabling customer managed key encryption for AI Assistant Memory
<a name="application-encryption-cmk-agentic-memory"></a>

If you use a customer managed key to encrypt your OpenSearch UI application, your key policy must also allow OpenSearch UI to create an AWS KMS grant for AI Assistant Memory. The key policy in [Prerequisites for using customer managed keys](#application-encryption-cmk-prerequisites) includes this permission in the `AllowOpenSearchUIToCreateGrantForAIAssistantMemory` statement. This section explains why the statement is required and how to recover an application that you created without it.

AI Assistant Memory is a service-managed memory layer that powers Agentic Chat and the Investigation Agent in OpenSearch UI. It saves your past conversations so that ongoing conversations can persist across feature pages. For more information, see [AI Assistant Memory in Amazon OpenSearch Service](application-agentic-memory.md).

Amazon OpenSearch Service enables the agentic AI features by default for new OpenSearch UI applications. You can turn them off by using the console or the API. For more information, see [Enabling and disabling agentic AI features](application-ai-assistant.md#application-ai-assistant-enable-disable). When the features are enabled, OpenSearch UI creates a collection in a service-managed Amazon OpenSearch Serverless account to store the memory data.

To encrypt the memory data with your customer managed key, OpenSearch UI must create an AWS KMS grant on your key. The `AllowOpenSearchUIToUseKey` statement grants permissions only for metadata encryption. It doesn't include the `kms:CreateGrant` permission that AI Assistant Memory requires.

**Note**  
If your key policy doesn't include the grant permission, creating the application succeeds, but registering the AI Assistant Memory capability fails with a `KMS_KEY_INSUFFICIENT_PERMISSION` error. Add the following statement before you create the application.

If your key policy already contains the other two statements shown in [Prerequisites for using customer managed keys](#application-encryption-cmk-prerequisites), add the following statement to the `Statement` array:

```json
{
    "Sid": "AllowOpenSearchUIToCreateGrantForAIAssistantMemory",
    "Effect": "Allow",
    "Principal": {
        "Service": [
            "application.opensearchservice.amazonaws.com"
        ]
    },
    "Action": "kms:CreateGrant",
    "Resource": "*",
    "Condition": {
        "Bool": {
            "kms:GrantIsForAWSResource": "true"
        },
        "ForAllValues:StringEquals": {
            "kms:GrantOperations": [
                "Decrypt",
                "GenerateDataKey"
            ]
        }
    }
}
```

This statement uses the following conditions:
+ `kms:GrantIsForAWSResource` allows the grant only when an AWS service creates it on your behalf, not when a principal creates one directly.
+ `kms:GrantOperations` limits the grant to the `Decrypt` and `GenerateDataKey` operations that AI Assistant Memory requires.

**Important**  
Add this as a separate statement in your key policy. Don't merge it into the existing `AllowOpenSearchUIToUseKey` statement. If you combine them, the `kms:GrantIsForAWSResource` condition applies to the `kms:Encrypt`, `kms:Decrypt`, `kms:GenerateDataKey`, and `kms:DescribeKey` actions and breaks metadata encryption.

If you already created an application and the AI Assistant Memory capability failed to register, you don't need to create a new application. Add the statement to your key policy, and then call the [DeregisterCapability](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeregisterCapability.html) API followed by the [RegisterCapability](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_RegisterCapability.html) API on the existing application. The capability status changes from `create_failed` to `active`. This differs from changing the key itself, which requires a new application, as described in [Updating encryption settings](#application-encryption-cmk-update).

## Creating an application with customer managed key encryption using the console
<a name="application-encryption-cmk-create-console"></a>

When you create an OpenSearch UI application in the console, you can specify a customer managed key for encrypting the application's metadata.

**To create an OpenSearch UI application with customer managed key encryption using the console**

1. Sign in to the Amazon OpenSearch Service console at [https://console.aws.amazon.com/aos/home](https://console.aws.amazon.com/aos/home).

1. In the left navigation pane, choose **OpenSearch UI (Dashboards)**.

1. Choose **Create application**.

1. For **Application name**, enter a name for the application.

1. Configure authentication and administrator settings as needed. For more information, see [Getting started with the OpenSearch user interface in Amazon OpenSearch Service](application-getting-started.md).

1. In the **Encryption** section, for **Encryption at rest**, choose **Use customer managed key**.

1. Select an existing customer managed key from the list, or choose **Create a key** to create a new key in AWS KMS.
**Note**  
The key must be in the same AWS Region as the application you are creating.

1. (Optional) Add tags to the application.

1. Choose **Create**.

## Creating an application with customer managed key encryption using the AWS CLI
<a name="application-encryption-cmk-create-cli"></a>

To create an OpenSearch UI application with customer managed key encryption using the AWS CLI, use the [create-application](https://docs.aws.amazon.com/cli/latest/reference/opensearch/create-application.html) command with the `--kms-key-arn` parameter.

Replace the {{placeholder values}} with your own information.

```sh
aws opensearch create-application \
    --name {{my-application}} \
    --kms-key-arn arn:aws:kms:{{us-east-1}}:{{123456789012}}:key/{{12345678-1234-1234-1234-123456789012}}
```

If you don't specify the `--kms-key-arn` parameter, OpenSearch uses an AWS-managed key to encrypt the application's metadata.

## Monitoring customer managed key usage
<a name="application-encryption-cmk-monitoring"></a>

When you use a customer managed key with an OpenSearch UI application, AWS KMS records every use of the key in AWS CloudTrail logs. You can use these logs to monitor how and when your key is used. The logs show which user or service accessed the key.

AWS AWS KMS automatically rotates customer managed keys every year. You can also manually rotate keys as needed. For more information about key rotation, see [Rotating KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html) in the *AWS KMS Developer Guide*.

For more information about monitoring key usage, see [Logging AWS KMS API calls with AWS CloudTrail](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html) in the *AWS KMS Developer Guide*.

**Note**  
Using customer managed keys incurs AWS KMS charges. Charges are based on the number of API requests and keys stored. For pricing details, see [AWS Key Management Service Pricing](https://aws.amazon.com/kms/pricing/).

## Updating encryption settings
<a name="application-encryption-cmk-update"></a>

After you create an OpenSearch UI application, you cannot change its encryption settings. If you need to use a different customer managed key, you must create a new application. If you need to switch between AWS-managed and customer managed keys, you must also create a new application with the desired encryption settings.

**Important**  
Before you disable or delete a customer managed key, consider the following:  
If you disable the key, the application will lose access to its encrypted metadata. You must re-enable the same key to restore access.
If you delete the key, the application's saved objects become permanently inaccessible. This includes queries, visualizations, and dashboards. Deleted keys cannot be recovered.
We recommend documenting your key ARN before making any changes to the key status.

**Next steps**  
After you configure CMK encryption for your application, you can:
+ Associate data sources with your application. For more information, see [Managing data source associations and Virtual Private Cloud access permissions](application-data-sources-and-vpc.md).
+ Create workspaces for your team. For more information, see [Using Amazon OpenSearch Service workspaces](application-workspaces.md).
+ Set up AWS CloudTrail monitoring for key usage. For more information, see [Monitoring customer managed key usage](#application-encryption-cmk-monitoring).