# Encryption at rest for AWS DevOps Agent

AWS DevOps Agent encrypts all customer data at rest. By default, AWS DevOps Agent uses AWS owned keys to automatically encrypt your data at no additional charge. You cannot view, manage, or audit the use of AWS owned keys. However, you do not need to take any action to protect these keys. Your data is automatically secured.

You can choose to encrypt your data using a symmetric customer managed key that you create, own, and manage in AWS Key Management Service (AWS KMS). Because you have full control of this layer of encryption, you can perform tasks such as the following:

- Establishing and maintaining key policies
- Enabling and disabling key policies
- Rotating key cryptographic material
- Adding tags
- Creating key aliases
- Scheduling keys for deletion
  For more information, see [Customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the _AWS Key Management Service Developer Guide_.

###### Note

AWS DevOps Agent automatically enables encryption at rest using AWS owned keys to protect customer data at no charge. Standard AWS KMS charges apply when you use a customer managed key. For more information about pricing, see [AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

## Customer managed keys

Customer managed keys are KMS keys in your AWS account that you create, own, and manage. You have full control over these KMS keys, including establishing and maintaining their key policies.

When you configure a customer managed key, AWS DevOps Agent uses it to protect sensitive resource data. AWS DevOps Agent uses [envelope encryption](../../../encryption-sdk/latest/developer-guide/concepts.md#envelope-encryption "../../../encryption-sdk/latest/developer-guide/concepts.md#envelope-encryption") with the AWS Encryption SDK hierarchical keyring. Your KMS key is used to generate branch keys, which in turn protect your data.

You can specify a customer managed key when you create the following resources:

- **Agent Space** — Encrypts Agent Space details and content created from the DevOps Agent Web App related to investigations, skills, and chat.
- **Service** — Encrypts third-party service credentials at rest.

To configure a customer managed key in AWS DevOps Agent, follow these steps.

### Step 1: Create a customer managed key

You can create a symmetric customer managed key by using the AWS KMS console or the AWS KMS API. The key must meet the following requirements:

| Property  | Requirement         |
| --------- | ------------------- |
| Key type  | Symmetric           |
| Key spec  | `SYMMETRIC_DEFAULT` |
| Key usage | `ENCRYPT_DECRYPT`   |

###### Note

AWS DevOps Agent only supports symmetric encryption KMS keys with the `SYMMETRIC_DEFAULT` key spec and the `ENCRYPT_DECRYPT` key usage. Multi-Region keys and asymmetric keys are not currently supported.

For more information, see [Creating a symmetric customer managed key](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the _AWS Key Management Service Developer Guide_.

### Step 2: Set the key policy

Key policies control access to your customer managed key. Every customer managed key must have exactly one key policy, which contains statements that determine who can use the key and how they can use it.

Your key policy must grant permissions to both the calling principal (your IAM identity) and the AWS DevOps Agent service. AWS DevOps Agent accesses your key using two sets of credentials:

1. **Your caller credentials** — Used for all synchronous operations, including key validation, encryption at resource creation time, and any API call that returns a direct response to the caller.
2. **AWS DevOps Agent service principal** — Used for asynchronous operations that run in the background, such as operational investigations, incident analysis, event correlation, and root cause analysis generation.

The following table lists the required KMS actions:

| KMS action            | Description                                           |
| --------------------- | ----------------------------------------------------- |
| `kms:DescribeKey`     | Validate key configuration at resource creation time  |
| `kms:GenerateDataKey` | Generate data encryption keys for envelope encryption |
| `kms:Decrypt`         | Decrypt data                                          |
| `kms:Encrypt`         | Encrypt data                                          |
| `kms:ReEncrypt`       | Re-encrypt data under the same or different key       |

AWS DevOps Agent validates all of these permissions at configuration time using dry-run operations. If any permission is missing, the request fails with an exception.

The following is an example key policy. Replace the placeholder values with your own.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowCallerAccessViaService",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/DevOpsAgentUserRole"
      },
      "Action": [
        "kms:DescribeKey",
        "kms:GenerateDataKey*",
        "kms:Decrypt",
        "kms:Encrypt",
        "kms:ReEncrypt*"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "aidevops.us-east-1.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AllowDevOpsAgentServiceDescribeKeyAccess",
      "Effect": "Allow",
      "Principal": {
        "Service": "aidevops.amazonaws.com"
      },
      "Action": [
        "kms:DescribeKey"
      ],
      "Resource": "*"
    },
    {
      "Sid": "AllowDevOpsAgentAccessForAgentSpace",
      "Effect": "Allow",
      "Principal": {
        "Service": "aidevops.amazonaws.com"
      },
      "Action": [
        "kms:GenerateDataKey*",
        "kms:Decrypt",
        "kms:Encrypt",
        "kms:ReEncrypt*"
      ],
      "Resource": "*",
      "Condition": {
        "ArnLike": {
          "aws:SourceArn": "arn:aws:aidevops:us-east-1:111122223333:agentspace/*"
        },
        "StringLike": {
          "kms:EncryptionContext:aws-crypto-ec:aws:aidevops:arn": "arn:aws:aidevops:us-east-1:111122223333:agentspace/*"
        }
      }
    },
    {
      "Sid": "AllowDevOpsAgentAccessForService",
      "Effect": "Allow",
      "Principal": {
        "Service": "aidevops.amazonaws.com"
      },
      "Action": [
        "kms:GenerateDataKey*",
        "kms:Decrypt",
        "kms:Encrypt",
        "kms:ReEncrypt*"
      ],
      "Resource": "*",
      "Condition": {
        "ArnLike": {
          "aws:SourceArn": "arn:aws:aidevops:us-east-1:111122223333:service/*"
        },
        "StringLike": {
          "kms:EncryptionContext:aws-crypto-ec:aws:aidevops:arn": "arn:aws:aidevops:us-east-1:111122223333:service/*"
        }
      }
    }
  ]
}
```

The policy contains the following statements:

- **AllowKeyAdministration** — Grants the account root full administrative access to the key. Replace `111122223333` with your AWS account ID.
- **AllowCallerAccessViaService** — Grants your IAM principals the KMS permissions required for all synchronous AWS DevOps Agent operations. This includes key validation at resource creation time, as well as encrypt and decrypt operations for any API call that returns a direct response to the caller. The `kms:ViaService` condition ensures that you can use the key only through the AWS DevOps Agent service. Replace `111122223333` with your AWS account ID and `us-east-1` with your AWS Region.
- **AllowDevOpsAgentServiceAccessForAgentSpace** / **AllowDevOpsAgentServiceAccessForService** — Grants the `aidevops.amazonaws.com` service principal the KMS permissions required for asynchronous operations. AWS DevOps Agent uses this service principal to encrypt and decrypt your data when performing background operations such as operational investigations, analyzing incidents, correlating events across services, and generating root cause analyses. Without this access, AWS DevOps Agent cannot read the encrypted data needed to carry out investigations on your behalf. The `aws:SourceArn` condition restricts access to requests originating from your AWS DevOps Agent resources, and the `kms:EncryptionContext` condition ensures that the encryption context matches your resource ARNs. Replace `111122223333` with your AWS account ID and `us-east-1` with your AWS Region.

For more information about key policies, see [Key policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the _AWS Key Management Service Developer Guide_.

### Step 3: Specify the key when creating a resource

After you create your key and configure the key policy, you can specify the key when creating AWS DevOps Agent resources.

#### Console

To configure a customer managed key when creating an Agent Space in the console:

1. Open the AWS DevOps Agent console.
2. Choose **Create Agent Space** or **Register Service**.
3. Enter the agent space details (name, description, and IAM role).
4. Expand the **Advanced Configuration** section.
5. Under **Encryption key type**, select **Customer managed key**.
6. Choose a KMS key from the dropdown list, or enter a KMS key ARN.
7. Review the key policy displayed in the **Key policy** expandable section. Ensure that you have attached this policy to your KMS key. You can use the copy button to copy the policy.
8. Complete the remaining configuration and choose **Create**.

###### Note

If you do not see your KMS key in the dropdown list, verify that the key meets the requirements in [Step 1](#step-1-create-a-customer-managed-key "#step-1-create-a-customer-managed-key") and that you have `kms:ListKeys` and `kms:DescribeKey` permissions.

#### API

##### Creating an Agent Space with a customer managed key

Specify the `kmsKeyArn` parameter when creating an agent space. The value must be the full KMS key ARN.

```
{
  "name": "my-agent-space",
  "description": "An encrypted agent space",
  "kmsKeyArn": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
}
```

##### Registering a Service with a customer managed key

Specify the `kmsKeyArn` parameter when registering a service. The value must be the full KMS key ARN. This parameter is supported across all service types, including Dynatrace, ServiceNow, PagerDuty, GitLab, GitHub, and MCP Servers.

```
{
  "service": "dynatrace",
  "kmsKeyArn": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
  "serviceDetails": { ... }
}
```

###### Note

You must specify the customer managed key at resource creation time. You cannot add or change the customer managed key for an existing resource.

## AWS DevOps Agent encryption context

An [encryption context](../../../kms/latest/developerguide/concepts.md#encrypt_context "../../../kms/latest/developerguide/concepts.md#encrypt_context") is a set of non-secret key-value pairs that contain additional contextual information about the data. AWS KMS uses the encryption context as [additional authenticated data](../../../crypto/latest/userguide/cryptography-concepts.md#term-aad "../../../crypto/latest/userguide/cryptography-concepts.md#term-aad") to support authenticated encryption. When you include an encryption context in a request to encrypt data, AWS KMS binds the encryption context to the encrypted data. To decrypt data, you must include the same encryption context in the request.

AWS DevOps Agent uses the following encryption context on all cryptographic operations:

```
{
  "aws-crypto-ec:aws:aidevops:arn": "arn:aws:aidevops:{region}:{accountId}:{resourceType}/{resourceId}"
}
```

The encryption context value is the ARN of the AWS DevOps Agent resource being encrypted. You can use this encryption context in your key policy conditions and in AWS CloudTrail logs to audit how your key is being used.

## Key management

If you disable or schedule deletion of your KMS key, AWS DevOps Agent cannot decrypt your data. This results in `AccessDeniedException` errors on operations that read encrypted data.

###### Important

If you choose to use a customer managed key, you are responsible for managing the key and its permissions. If the key is disabled or deleted, or if AWS DevOps Agent loses permission to use the key, you lose access to the encrypted data.

The following table describes common failure scenarios:

| Action                            | Impact                                                       |
| --------------------------------- | ------------------------------------------------------------ |
| Key policy permissions revoked    | `AccessDeniedException` on encrypt and decrypt operations    |
| KMS key is disabled               | `DisabledException` on encrypt and decrypt operations        |
| KMS key is scheduled for deletion | `KMSInvalidStateException` on encrypt and decrypt operations |
| KMS key is deleted                | Permanent data loss — encrypted data cannot be recovered     |

Before disabling or deleting a key:

1. Verify that no active AWS DevOps Agent resources depend on the key.
2. Consider disabling the key first to test the impact before scheduling deletion.
3. AWS KMS enforces a minimum waiting period before key deletion, giving you time to cancel if needed.

## Monitoring your encryption keys

When you use a customer managed key with AWS DevOps Agent, you can use [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") to track requests that AWS DevOps Agent sends to AWS KMS.

You can filter CloudTrail events by:

- **Event source** — `kms.amazonaws.com`
- **Encryption context key** — `aws-crypto-ec:aws:aidevops:arn`
- **Key ARN** — Your customer managed key ARN in the request parameters

For more information, see [Logging AWS KMS API calls with AWS CloudTrail](../../../kms/latest/developerguide/logging-using-cloudtrail.md "../../../kms/latest/developerguide/logging-using-cloudtrail.md") in the _AWS Key Management Service Developer Guide_.
