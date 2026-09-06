# Data encryption

Data encryption typically falls into two categories: encryption at rest and encryption in transit.

## Encryption at rest

We encrypt data at rest in AWS Agent Registry in accordance with industry standards.

By default, we encrypt your data in registries with AWS owned keys at no additional charge. You cannot view, manage, or audit the use of this key.

You can optionally encrypt record descriptors with a customer managed AWS KMS key when you create a registry. Using a customer managed key gives you more control over the encryption process, including the ability to:

- Create and manage the key, including setting key policies
- Rotate the key automatically using AWS KMS automatic key rotation
- Disable or delete the key to control access to encrypted data
- Audit key usage through AWS CloudTrail

For more information, see [Customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the _AWS Key Management Service Developer Guide_.

###### Note

AWS KMS charges apply when you use a customer managed key. For more information, see [AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/").

## What is encrypted

When you specify a customer managed key, AWS Agent Registry encrypts **record descriptors** at rest. Record descriptors are the resource-type-specific metadata stored within each registry record — this is the detailed configuration that describes what a resource is and how to use it:

- **MCP server records** — The server definition and tool definitions (including input parameters and output formats).
- **Agent records** — The agent card describing capabilities, skills, and communication interface.
- **Skill records** — Package or repository details and markdown documentation.
- **Custom resource records** — The custom JSON metadata structure.

The search index that powers `SearchDiscoverableRegistryRecords` is also encrypted with the same key.

The following data is **not** encrypted with your customer managed key (it remains encrypted with the AWS owned key):

- Registry name and description
- Record name, description, protocol, and external version
- Registry and record identifiers (IDs, ARNs)

###### Note

`ListRegistryRecords` returns record summaries (name, description, protocol, external version) without making any KMS calls. This operation works even if your KMS key is unavailable.

## Considerations

Consider the following when you configure encryption for your registries:

- You can only specify a customer managed key at registry creation. You cannot add, change, or remove encryption configuration after the registry is created.
- If you want to change the KMS key for a registry, you must create a new registry with the desired key and migrate your records.
- AWS Agent Registry supports only symmetric encryption KMS keys. You cannot use an asymmetric KMS key or a multi-Region key.
- The KMS key must be in the same AWS Region as the registry.
- If you choose a customer managed key, we recommend that you enable [automatic key rotation](../../../kms/latest/developerguide/rotate-keys.md "../../../kms/latest/developerguide/rotate-keys.md").
- Registries without a customer managed key continue to use the AWS owned key. No behavioral changes occur for existing registries.

## How AWS Agent Registry uses grants in AWS KMS

AWS Agent Registry requires a [grant](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md") to use your customer managed key.

When you create a registry with a customer managed key, AWS Agent Registry creates a grant on your behalf by sending a [CreateGrant](../../../kms/latest/APIReference/API_CreateGrant.md "../../../kms/latest/APIReference/API_CreateGrant.md") request to AWS KMS. The grant is scoped to your specific registry using an encryption context constraint.

AWS Agent Registry requires the grant to use your customer managed key for the following internal operations:

- Send [GenerateDataKey](../../../kms/latest/APIReference/API_GenerateDataKey.md "../../../kms/latest/APIReference/API_GenerateDataKey.md") requests to create data keys for encrypting record descriptors.
- Send [Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") requests to decrypt encrypted data keys so that they can be used to decrypt your data.
- Send [DescribeKey](../../../kms/latest/APIReference/API_DescribeKey.md "../../../kms/latest/APIReference/API_DescribeKey.md") requests to verify the key is valid.

You can revoke access to the grant, or remove the service’s access to the customer managed key at any time. If you do, AWS Agent Registry won’t be able to access any of the data encrypted by the customer managed key, which affects all operations that read or write record descriptors.

AWS Agent Registry retires grants when you delete a registry.

## KMS permissions used by each API operation

The following table shows which KMS operations AWS Agent Registry calls for each API. For synchronous API calls (CreateRegistryRecord, GetRegistryRecord, UpdateRegistryRecord, SearchDiscoverableRegistryRecords), your credentials are forwarded to AWS KMS through [Forward Access Sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md") (FAS).

| API operation                       | KMS operations                       | Notes                                              |
| ----------------------------------- | ------------------------------------ | -------------------------------------------------- |
| `CreateRegistry`                    | `kms:DescribeKey`, `kms:CreateGrant` | Validates key and creates grant                    |
| `CreateRegistryRecord`              | `kms:GenerateDataKey`, `kms:Decrypt` | Encrypts record descriptors                        |
| `GetRegistryRecord`                 | `kms:Decrypt`                        | Decrypts record descriptors                        |
| `UpdateRegistryRecord`              | `kms:Decrypt`, `kms:GenerateDataKey` | Decrypts existing, encrypts updated descriptors    |
| `ListRegistryRecords`               | None                                 | No KMS calls — uses unencrypted summary attributes |
| `SearchDiscoverableRegistryRecords` | `kms:Decrypt`                        | Decrypts record descriptors for search results     |
| `DeleteRegistryRecord`              | None                                 | No KMS calls required                              |
| `DeleteRegistry`                    | None                                 | No KMS calls required                              |

## Encryption context

An [encryption context](../../../kms/latest/developerguide/concepts.md#encrypt_context "../../../kms/latest/developerguide/concepts.md#encrypt_context") is a set of key-value pairs that contain additional contextual information about the data. AWS KMS uses the encryption context as [additional authenticated data](../../../crypto/latest/userguide/cryptography-concepts.md#term-aad "../../../crypto/latest/userguide/cryptography-concepts.md#term-aad") to support authenticated encryption.

AWS Agent Registry includes the following encryption context in all KMS cryptographic operations:

```
{
  "aws:agent-registry:registry-arn": "arn:aws:agent-registry:us-east-1:111122223333:registry/my-registry-id"
}
```

You can use this encryption context in AWS CloudTrail logs to identify which registry a KMS operation was performed for.

## Behavior when a key becomes unavailable

If you disable or delete your customer managed KMS key, revoke the grant, or if the caller’s IAM policy no longer grants the required KMS permissions:

- **CreateRegistryRecord** — Fails. The service cannot encrypt the record descriptors.
- **GetRegistryRecord** — Fails. The service cannot decrypt the record descriptors.
- **UpdateRegistryRecord** — Fails. The service cannot decrypt or encrypt the record descriptors.
- **ListRegistryRecords** — **Succeeds**. This operation does not make KMS calls.
- **SearchDiscoverableRegistryRecords** — Fails. The service cannot decrypt the record descriptors for search results.
- **DeleteRegistry** — **Succeeds**. Deletion does not require access to the KMS key.
- **DeleteRegistryRecord** — **Succeeds**. Record deletion does not require KMS access.

To restore access, re-enable the key or update the IAM policy to grant the required permissions.

## Encryption in transit

AWS Agent Registry uses TLS (Transport Layer Security) to encrypt all data in transit between your clients and the service endpoints. All API calls to AWS Agent Registry require HTTPS.

## Key management

AWS Agent Registry supports two key management options for encryption at rest:

- **AWS owned key (default)** — We own and manage the key on your behalf. You don’t need to create or manage a key, and there’s no additional charge. You can’t view, rotate, or audit this key.
- **Customer managed key** — You create and manage a symmetric encryption KMS key in AWS KMS. You have full control over key policies, rotation schedules, and key deletion. You can audit key usage through AWS CloudTrail.

You select the key management option when you create a registry. You cannot change the encryption key after the registry is created. For configuration steps, see [Set customer managed key policy](registry-kms-key-policy.md "registry-kms-key-policy.md").
