

# Data encryption

Data encryption typically falls into two categories: encryption at rest and encryption in transit.

## Encryption at rest
<a name="registry-encryption-at-rest"></a>

We encrypt data at rest in AWS Agent Registry in accordance with industry standards.

By default, we encrypt your data in registries with AWS owned keys at no additional charge. You cannot view, manage, or audit the use of this key.

You can optionally encrypt record descriptors and skill packages with a customer managed AWS KMS key when you create a registry. Using a customer managed key gives you more control over the encryption process, including the ability to:
+ Create and manage the key, including setting key policies
+ Rotate the key automatically using AWS KMS automatic key rotation
+ Disable or delete the key to control access to encrypted data
+ Audit key usage through AWS CloudTrail

For more information, see [Customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) in the * AWS Key Management Service Developer Guide*.

**Note**  
 AWS KMS charges apply when you use a customer managed key. For more information, see [AWS Key Management Service pricing](https://aws.amazon.com/kms/pricing/).

## What is encrypted
<a name="registry-encryption-what-is-encrypted"></a>

When you specify a customer managed key, AWS Agent Registry encrypts **record descriptors** and **custom metadata** at rest. Record descriptors are the resource-type-specific metadata stored within each registry record — this is the detailed configuration that describes what a resource is and how to use it:
+  **MCP server records** — The server definition and tool definitions (including input parameters and output formats).
+  **Agent records** — The agent card describing capabilities, skills, and communication interface.
+  **Skill records** — Package or repository details and markdown documentation.
+  **Custom resource records** — The custom JSON metadata structure.

If the registry has a custom metadata schema, the following are also encrypted:
+  **Custom metadata schema** — The JSON Schema definition stored on the registry.
+  **Custom metadata values** — The per-record metadata values set by record authors.

For skill records, the following are also encrypted:
+  **Skill packages** — The `.zip` package of a skill record, whether you upload it or AWS Agent Registry synchronizes it from Amazon S3 or GitHub, and the `SKILL.md` that AWS Agent Registry reads from the package when it validates it. Packages are stored in Amazon S3 buckets that AWS Agent Registry owns. For more information, see [How AWS Agent Registry encrypts skill packages](#registry-encryption-skill-packages).
+  **Synchronized source** — The location and version that a skill record was last synchronized from (`synchronizedSource`).

The search index that powers `SearchDiscoverableRegistryRecords` is also encrypted with the same key.

The following data is **not** encrypted with your customer managed key (it remains encrypted with the AWS owned key):
+ Registry name and description
+ Record name, description, protocol, and external version. A record that synchronizes takes its name and description from what it synchronizes, such as an A2A agent card or a skill’s SKILL.md, so those values aren’t encrypted with your key either.
+ Registry and record identifiers (IDs, ARNs)
+ The SHA-256 checksum of a skill package (`sha256`)

## Considerations
<a name="registry-encryption-considerations"></a>

Consider the following when you configure encryption for your registries:
+ You can only specify a customer managed key at registry creation. You cannot add, change, or remove encryption configuration after the registry is created.
+ If you want to change the KMS key for a registry, you must create a new registry with the desired key and migrate your records.
+  AWS Agent Registry supports only symmetric encryption KMS keys. You cannot use an asymmetric KMS key or a multi-Region key.
+ The KMS key must be in the same AWS Region as the registry.
+ If you choose a customer managed key, we recommend that you enable [automatic key rotation](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html).
+ Registries without a customer managed key continue to use the AWS owned key. No behavioral changes occur for existing registries.
+ Skill packages stay encrypted under the key that the registry was created with. You can’t move a registry’s skill packages to a different key. Automatic key rotation needs no action from you, because AWS KMS keeps the earlier key material to decrypt packages that were encrypted with it.
+ Each request that returns a skill package download URL calls AWS KMS with your key, with the credentials of AWS Agent Registry and, for a caller that signs requests with IAM credentials, with the caller’s credentials, to confirm that the registry can still use the key. If your key is in a custom key store, these requests count toward the key store’s request quota, which your other uses of the key share. For more information, see [Request quotas](https://docs.aws.amazon.com/kms/latest/developerguide/requests-per-second.html) in the * AWS Key Management Service Developer Guide*.

## How AWS Agent Registry uses grants in AWS KMS
<a name="registry-encryption-how-it-works"></a>

 AWS Agent Registry requires a [grant](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html) to use your customer managed key.

When you create a registry with a customer managed key, AWS Agent Registry creates a grant on your behalf by sending a [CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html) request to AWS KMS. The grant is scoped to your specific registry using an encryption context constraint.

 AWS Agent Registry requires the grant to use your customer managed key for internal operations, including the following:
+ Send [GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html) requests to create data keys for encrypting record descriptors and skill packages.
+ Send [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) requests to decrypt encrypted data keys so that they can be used to decrypt your data.
+ Send [DescribeKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html) requests to verify the key is valid.

You can revoke access to the grant, or remove the service’s access to the customer managed key at any time. If you do, AWS Agent Registry can’t store or synchronize skill packages, return download URLs, or process records asynchronously. Requests that use your credentials still decrypt record descriptors, but a read that would return a download URL fails.

 AWS Agent Registry retires grants when you delete a registry.

## How AWS Agent Registry encrypts skill packages
<a name="registry-encryption-skill-packages"></a>

When a registry has a customer managed key, AWS Agent Registry stores each skill package with server-side encryption with AWS KMS keys (SSE-KMS) under that key. Registries without a customer managed key store packages under an AWS owned key.
+  **Encryption context** — Every package is written with the encryption context `{"aws:agent-registry:registry-arn": "<registry ARN>"}`, the same context as the rest of the registry’s data. Amazon S3 stores it with the object and uses it on every read. For more information, see [Encryption context](#registry-encryption-context).
+  **S3 Bucket Keys** — AWS Agent Registry enables [S3 Bucket Keys](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-key.html) for packages. Amazon S3 uses a short-lived bucket-level key, derived from your key, to encrypt and decrypt packages, so it makes fewer requests to AWS KMS. Because of this, AWS CloudTrail shows fewer KMS events than package reads and writes.
+  **Grant** — Amazon S3 uses your key through the grant that AWS Agent Registry created when you created the registry (see [How AWS Agent Registry uses grants in AWS KMS](#registry-encryption-how-it-works)). That grant is constrained to the registry’s encryption context. Skill packages need no additional grant and no additional key policy statement.
+  **Downloads** — `GetRegistryRecord`, `BatchGetDiscoverableRegistryRecord`, and the batch get tool on the registry’s MCP endpoint return a download URL for the package. The URL is a presigned Amazon S3 URL that is valid for up to 5 minutes. When someone uses the URL, Amazon S3 decrypts the package under the registry’s grant, so whoever uses the URL needs no KMS permission.

Because Amazon S3 uses your key on behalf of AWS Agent Registry, AWS Agent Registry first checks that the caller can use the key:
+ When you upload a package, or create or update a record so that it synchronizes a skill package from Amazon S3 or GitHub (including with `triggerSynchronization`), AWS Agent Registry makes a `GenerateDataKey` dry-run request with your credentials and the registry’s encryption context. If the request is denied, the API call fails with a `ValidationException`, and the registry doesn’t store the package. A record that synchronizes only its `SKILL.md` stores no package and makes no such request.
+ Before it returns a download URL to a caller that uses IAM credentials, AWS Agent Registry makes sure that the caller’s credentials decrypted the record with your key in the same request, which needs `kms:Decrypt`. It also confirms that the registry’s grant still allows AWS Agent Registry to use the key. If either check fails, the call fails with a `ValidationException` (the batch get tool on the MCP endpoint returns an error result), and the registry doesn’t return a URL.

For the key policy permissions, see [Set customer managed key policy](registry-kms-key-policy.md).

## KMS permissions used by each API operation
<a name="registry-encryption-per-api"></a>

The following table shows which KMS operations AWS Agent Registry calls for each API. For synchronous API calls (CreateRegistryRecord, GetRegistry, GetRegistryRecord, ListRegistryRecords, UpdateRegistry, UpdateRegistryRecord, SearchDiscoverableRegistryRecords, BatchGetDiscoverableRegistryRecord) that you sign with IAM credentials, your credentials are forwarded to AWS KMS through [Forward Access Sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_forward_access_sessions.html) (FAS).


| API operation | KMS operations | Notes | 
| --- | --- | --- | 
|  `CreateRegistry`  |  `kms:DescribeKey`, `kms:CreateGrant`, `kms:Decrypt`, `kms:GenerateDataKey`  | Validates key, creates grant, and encrypts custom metadata schema (when provided) | 
|  `GetRegistry`  |  `kms:Decrypt`  | Decrypts custom metadata schema (only when the registry has a custom metadata schema) | 
|  `UpdateRegistry`  |  `kms:Decrypt`, `kms:GenerateDataKey`  | Decrypts existing schema on every call when the registry has a schema. Also encrypts the updated schema when the schema is changed | 
|  `CreateRegistryRecord`  |  `kms:GenerateDataKey`, `kms:Decrypt`  | Encrypts record descriptors and custom metadata. For a skill record that uploads a package or synchronizes a skill package, also makes a `GenerateDataKey` dry-run request with your credentials. Amazon S3 then calls `GenerateDataKey` under the registry’s grant to store the package. | 
|  `GetRegistryRecord`  |  `kms:Decrypt`  | Decrypts record descriptors. For a skill record with a package, the decryption happens before the registry returns the download URL. | 
|  `UpdateRegistryRecord`  |  `kms:Decrypt`, `kms:GenerateDataKey`  | Decrypts existing, encrypts updated descriptors. A package upload, a new skill package source, or `triggerSynchronization` of a skill package also makes the `GenerateDataKey` dry-run request. | 
|  `BatchGetDiscoverableRegistryRecord`  |  `kms:Decrypt`  | Decrypts record descriptors. For a skill record with a package, the decryption happens before the registry returns the download URL. The batch get tool on the registry’s MCP endpoint does the same. | 
| Skill package download (presigned URL) | None for the caller | Amazon S3 calls `kms:Decrypt` under the registry’s grant. | 
|  `ListRegistryRecords`  |  `kms:Decrypt`  | Decrypts schema and per-record custom metadata for compliance computation (only when the registry has a custom metadata schema). If KMS is unavailable, the compliance status field is omitted but the operation still succeeds. | 
|  `SearchDiscoverableRegistryRecords`  |  `kms:Decrypt`  | Decrypts record descriptors for search results | 
|  `DeleteRegistryRecord`  | None | No KMS calls required. Deletes every stored version of the record’s skill package. | 
|  `DeleteRegistry`  | None | No KMS calls required | 

## Encryption context
<a name="registry-encryption-context"></a>

An [encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context) is a set of key-value pairs that contain additional contextual information about the data. AWS KMS uses the encryption context as [additional authenticated data](https://docs.aws.amazon.com/crypto/latest/userguide/cryptography-concepts.html#term-aad) to support authenticated encryption.

 AWS Agent Registry includes the following encryption context in all KMS cryptographic operations:

```json
{
  "aws:agent-registry:registry-arn": "arn:aws:agent-registry:us-east-1:111122223333:registry/my-registry-id"
}
```

You can use this encryption context in AWS CloudTrail logs to identify which registry a KMS operation was performed for.

## Behavior when a key becomes unavailable
<a name="registry-encryption-key-unavailable"></a>

If you disable or delete your customer managed KMS key, revoke the grant, or if the caller’s IAM policy no longer grants the required KMS permissions:
+  **CreateRegistryRecord** — Fails. The service cannot encrypt the record descriptors.
+  **GetRegistry** — Fails if the registry has a custom metadata schema. The service cannot decrypt the schema. Registries without a custom metadata schema are unaffected.
+  **UpdateRegistry** — Fails if the registry has a custom metadata schema. The service cannot decrypt the existing schema for additive-only validation.
+  **GetRegistryRecord** — Fails. The service cannot decrypt the record descriptors.
+  **UpdateRegistryRecord** — Fails. The service cannot decrypt or encrypt the record descriptors.
+  **ListRegistryRecords** — **Succeeds** with degraded compliance status. When the registry has a custom metadata schema, the compliance status field is omitted from each record summary, but the summaries themselves are still returned.
+  **SearchDiscoverableRegistryRecords** — Fails. The service cannot decrypt the record descriptors for search results.
+  **DeleteRegistry** — **Succeeds**. Deletion does not require access to the KMS key.
+  **DeleteRegistryRecord** — **Succeeds**. Record deletion does not require KMS access.

For skill packages:
+  **If you disable the key, schedule it for deletion, or deny a caller that signs requests with IAM credentials** — Package uploads, package synchronizations, and reads that return a download URL fail for that caller with a `ValidationException`. No new download URL is returned.
+  **If you revoke the registry’s grant, or your key policy denies AWS Agent Registry** — Package uploads fail with a `ValidationException`. Package synchronizations fail, and the record’s status becomes `CREATE_FAILED` or `UPDATE_FAILED` with a status reason about the KMS key. Reads that would return a download URL fail with a `ValidationException`, and no URL is returned.
+  **Download URLs that were already returned** might keep working until they expire, within 5 minutes. Amazon S3 decrypts the package each time someone uses a URL, so after you disable the key or revoke the grant, a download can fail before the URL expires. Because of S3 Bucket Keys, Amazon S3 might also continue to serve packages for a period after you disable the key or revoke the grant.

To stop the registry from returning new download URLs to a caller that signs requests with IAM credentials, remove that caller’s permission on the key or on the registry’s records. URLs that were already returned still work until they expire.

To restore access, re-enable the key or update the IAM policy to grant the required permissions.

## Monitoring how AWS Agent Registry uses your key
<a name="registry-encryption-monitoring"></a>

You can use AWS CloudTrail to see the requests that AWS Agent Registry and Amazon S3 make to AWS KMS for your registry. For more information, see [Logging AWS KMS API calls with AWS CloudTrail](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html). Each of these events includes the encryption context `"aws:agent-registry:registry-arn": "<registry ARN>"`. For skill packages, expect the following events:
+  `GenerateDataKey` dry-run requests, made with your credentials, when AWS Agent Registry checks a package upload or a skill package synchronization.
+  `Decrypt` requests, made with your credentials, when AWS Agent Registry reads or writes a record, including before it returns a skill package download URL.
+  `Decrypt` requests that AWS Agent Registry makes under the registry’s grant before it returns a download URL.
+  `GenerateDataKey` and `Decrypt` requests that Amazon S3 makes under the registry’s grant when packages are stored, validated, and downloaded. Because of S3 Bucket Keys, there are fewer of these events than package reads and writes.

## Encryption in transit
<a name="registry-encryption-in-transit"></a>

 AWS Agent Registry uses TLS (Transport Layer Security) to encrypt all data in transit between your clients and the service endpoints. All API calls to AWS Agent Registry require HTTPS.

Skill package download URLs also require HTTPS, with TLS 1.2 or later.

## Key management
<a name="registry-key-management"></a>

 AWS Agent Registry supports two key management options for encryption at rest:
+  ** AWS owned key (default)** — We own and manage the key on your behalf. You don’t need to create or manage a key, and there’s no additional charge. You can’t view, rotate, or audit this key.
+  **Customer managed key** — You create and manage a symmetric encryption KMS key in AWS KMS. You have full control over key policies, rotation schedules, and key deletion. You can audit key usage through AWS CloudTrail.

You select the key management option when you create a registry. You cannot change the encryption key after the registry is created. For configuration steps, see [Set customer managed key policy](registry-kms-key-policy.md).