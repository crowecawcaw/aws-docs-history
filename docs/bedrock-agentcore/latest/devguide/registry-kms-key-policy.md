# Set customer managed key policy

To use a customer managed key with AWS Agent Registry, you must configure both an IAM policy for the calling principal and a KMS key policy that allows the service to perform encryption and decryption operations.

## Prerequisites

Before creating a registry with a customer managed key, ensure the following:

- You have a symmetric encryption KMS key in the same AWS Region as the registry. For information about creating a KMS key, see [Creating keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer Guide_.
- The IAM principal calling `CreateRegistry` has the required KMS permissions. See [Required IAM permissions](#registry-encryption-iam-policy "#registry-encryption-iam-policy").

## Required IAM permissions

To interact with an encrypted registry, you must have the following permissions on the KMS key:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowRegistryCMKAccess",
      "Effect": "Allow",
      "Action": [
        "kms:DescribeKey",
        "kms:CreateGrant",
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:GenerateDataKey",
        "kms:Encrypt",
        "kms:ReEncrypt*",
        "kms:Decrypt"
      ],
      "Resource": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "agent-registry.us-east-1.amazonaws.com"
        }
      }
    }
  ]
}
```

Replace the following values:

- `Resource` — The ARN of your KMS key.
- `kms:ViaService` — Replace `us-east-1` with the AWS Region of your registry.

The `kms:ViaService` condition restricts the permissions to requests made through the AWS Agent Registry service, preventing these permissions from being used outside of AWS Agent Registry.

###### Note

You must be authorized to perform these KMS actions — either through your IAM policy or through the key policy (see [Key policy for a customer managed key](#registry-encryption-key-policy "#registry-encryption-key-policy")). If your key policy includes the [default key policy statement](../../../kms/latest/developerguide/key-policy-default.md#key-policy-default-allow-root-enable-iam "../../../kms/latest/developerguide/key-policy-default.md#key-policy-default-allow-root-enable-iam") that enables IAM policies, the IAM policy is sufficient.

## Key policy for a customer managed key

The following sections list the KMS key policy statements that AWS Agent Registry requires. Add these statements to your KMS [key policy](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") so that the service and the calling principals can use the key. Adding statements is required when your key policy does not include the [default key policy statement](../../../kms/latest/developerguide/key-policy-default.md#key-policy-default-allow-root-enable-iam "../../../kms/latest/developerguide/key-policy-default.md#key-policy-default-allow-root-enable-iam") that enables IAM policies, or when the key is in a different account.

###### Important

The JSON blocks in the following sections are **examples of individual policy statements**, not complete key policies. Do not use them to replace your existing KMS key policy. Instead, copy the statements you need — based on the personas in your organization and the service-linked role — and append them to the `Statement` array of your existing key policy. Update the values in each statement (account ID, Region, role ARN, and registry ARN) to match your environment before saving the policy.

The key policy should grant permissions based on the [registry personas](registry-concepts.md#registry-concept-personas "registry-concepts.md#registry-concept-personas") in your organization:

- **Administrator** — Creates registries and manages encryption configuration. Needs `kms:DescribeKey`, `kms:CreateGrant`, and encrypt/decrypt permissions.
- **Publisher or Approver** — Creates and updates registry records (writes and reads record descriptors). Needs encrypt and decrypt permissions.
- **Consumer** — Reads registry records and search results (reads record descriptors). Needs decrypt permissions.

In addition to the persona statements, add the [Policy statement for the service-linked role](#registry-encryption-key-policy-slr "#registry-encryption-key-policy-slr") so that AWS Agent Registry can use the key on your behalf at runtime. If you share your registry with other accounts in your AWS Organization by using AWS Resource Access Manager (AWS RAM), also add the [Policy statement for organization access via AWS RAM](#registry-encryption-key-policy-ram "#registry-encryption-key-policy-ram").

###### Note

If your role both writes and reads record descriptors (for example, a publisher who also retrieves records), grant both encrypt and decrypt permissions as shown in [Policy statement for publisher](#registry-encryption-key-policy-publisher "#registry-encryption-key-policy-publisher").

### Policy statement for administrator

```
{
  "Version": "2012-10-17",
  "Statement": [
      {
      "Sid": "AllowRegistryAdminKeyValidation",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/RegistryAdminRole"
      },
      "Action": [
        "kms:DescribeKey"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "agent-registry.us-east-1.amazonaws.com"
        }
      }
    },
    {
      "Sid": "AllowRegistryAdminGrantCreation",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/RegistryAdminRole"
      },
      "Action": [
        "kms:CreateGrant"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "agent-registry.us-east-1.amazonaws.com"
        },
        "Bool": {
          "kms:GrantIsForAWSResource": "true"
        }
      }
    },
    {
      "Sid": "AllowRegistryAdminCryptoOps",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/RegistryAdminRole"
      },
      "Action": [
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:GenerateDataKey",
        "kms:Encrypt",
        "kms:ReEncrypt*",
        "kms:Decrypt"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "agent-registry.us-east-1.amazonaws.com",
          "kms:EncryptionContext:aws:agent-registry:registry-arn": "arn:aws:agent-registry:us-east-1:111122223333:registry/my-registry-id"
        }
      }
    }
  ]
}
```

- **AllowRegistryAdminKeyValidation** — Allows the administrator to validate the key before using it with a registry.
- **AllowRegistryAdminGrantCreation** — Allows the administrator to create grants when creating a registry. The `kms:GrantIsForAWSResource` condition ensures that `kms:CreateGrant` can only be used when an AWS service initiates the grant creation on the caller’s behalf.
- **AllowRegistryAdminCryptoOps** — Allows the administrator to encrypt and decrypt record descriptors, scoped to a specific registry via encryption context.

### Policy statement for publisher

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowRegistryPublisherCryptoOps",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/RegistryPublisherRole"
      },
      "Action": [
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:GenerateDataKey",
        "kms:Encrypt",
        "kms:ReEncrypt*",
        "kms:Decrypt"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "agent-registry.us-east-1.amazonaws.com",
          "kms:EncryptionContext:aws:agent-registry:registry-arn": "arn:aws:agent-registry:us-east-1:111122223333:registry/my-registry-id"
        }
      }
    }
  ]
}
```

- **AllowRegistryPublisherCryptoOps** — Allows publishers and approvers to encrypt and decrypt record descriptors. Required for `CreateRegistryRecord` and `UpdateRegistryRecord`.

### Policy statement for consumer

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowRegistryConsumerDecrypt",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/RegistryConsumerRole"
      },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "agent-registry.us-east-1.amazonaws.com",
          "kms:EncryptionContext:aws:agent-registry:registry-arn": "arn:aws:agent-registry:us-east-1:111122223333:registry/my-registry-id"
        }
      }
    }
  ]
}
```

- **AllowRegistryConsumerDecrypt** — Allows consumers to decrypt record descriptors. Required for `GetRegistryRecord` and `SearchDiscoverableRegistryRecords`.

### Policy statement for the service-linked role

Grant AWS Agent Registry’s service-linked role permission to use the key at runtime. The service uses this role to encrypt and decrypt record descriptors on your behalf.

Adding this statement requires two ordered steps:

1. **Create the service-linked role in your account first.**
   AWS Agent Registry does not create the role for you — you must create it yourself before adding the KMS key policy statement. Use the AWS CLI:

```
aws iam create-service-linked-role --aws-service-name agent-registry.amazonaws.com
```

This creates the `AWSServiceRoleForAgentRegistry` role at `arn:aws:iam::<account-id>:role/aws-service-role/agent-registry.amazonaws.com/AWSServiceRoleForAgentRegistry`. You only need to do this once per account. 2. **Then add the following statement to your KMS key policy.** IAM rejects any key policy that references a principal that does not yet exist, so the role must be present before you paste in a statement that names it.

Scope the statement to the registries in your account using an encryption context wildcard.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowRegistrySlrCryptoOps",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:role/aws-service-role/agent-registry.amazonaws.com/AWSServiceRoleForAgentRegistry"
      },
      "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey",
        "kms:GenerateDataKeyWithoutPlaintext",
        "kms:Encrypt",
        "kms:ReEncryptFrom",
        "kms:ReEncryptTo"
      ],
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "kms:EncryptionContext:aws:agent-registry:registry-arn": "arn:aws:agent-registry:us-east-1:111122223333:registry/*"
        }
      }
    }
  ]
}
```

- **AllowRegistrySlrCryptoOps** — Allows AWS Agent Registry’s service-linked role (`AWSServiceRoleForAgentRegistry`) to encrypt and decrypt record descriptors on your behalf, scoped to registries in your account via the `kms:EncryptionContext:aws:agent-registry:registry-arn` condition.

### Policy statement for organization access via AWS RAM

Add this statement if you share a customer-managed-key-encrypted registry with other accounts in your AWS Organization by using AWS Resource Access Manager (AWS RAM). It grants any principal in your organization the ability to decrypt record descriptors from a registry shared with them. If you do not share the registry via AWS RAM, this statement is not required.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowOrganizationDecrypt",
      "Effect": "Allow",
      "Principal": {
        "AWS": "*"
      },
      "Action": "kms:Decrypt",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:PrincipalOrgID": "o-EXAMPLE1234"
        }
      }
    }
  ]
}
```

- **AllowOrganizationDecrypt** — Allows any principal in your AWS Organization to decrypt record descriptors from registries you share via AWS RAM. The `aws:PrincipalOrgID` condition scopes this permission strictly to member accounts of the named organization; without a matching organization ID the `"Principal": "*"` grants nothing. Callers still need the corresponding service-level IAM permission on the shared registry itself.

### Replace values in key policy statements

Replace the following values in each key policy statement:

- `Principal` — The ARN of the IAM user or role for each persona. Replace `111122223333` with your account ID and the role names with your actual IAM roles. For the service-linked role statement, replace `111122223333` with your account ID; keep the role path and name (`aws-service-role/agent-registry.amazonaws.com/AWSServiceRoleForAgentRegistry`) as shown — it is a fixed, service-managed value.
- `kms:ViaService` — Replace `us-east-1` with the AWS Region of your registry.
- `kms:EncryptionContext:aws:agent-registry:registry-arn` — Replace with the ARN of your registry. To allow access to all registries in your account, use `StringLike` with a wildcard: `arn:aws:agent-registry:us-east-1:111122223333:registry/*`.
- `aws:PrincipalOrgID` — In the AWS RAM sharing statement, replace `o-EXAMPLE1234` with your AWS Organization ID. You can find it in the AWS Organizations console, or run `aws organizations describe-organization --query 'Organization.Id' --output text`.
