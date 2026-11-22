

# Key management in Amazon Managed Service for Apache Flink

In Amazon MSF, you can choose to use either [AWS managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) or your own [customer managed keys (CMKs)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-mgn-key) to encrypt data. CMKs in AWS Key Management Service (AWS KMS) are encryption keys that you create, own, and manage yourself.

**Topics**
+ [Transparent encryption in Amazon MSF](#transparent-encryption-flink)
+ [Customer managed keys in Amazon MSF](#cmk-flink)
+ [Using customer managed keys in Amazon MSF](use-cmk-flink.md)
+ [Managing CMK using AWS Management Console](manage-cmk-console.md)
+ [Managing CMK using APIs](manage-cmk-api.md)

## Transparent encryption in Amazon MSF
<a name="transparent-encryption-flink"></a>

By default, Amazon MSF uses AWS owned keys (AOKs) to encrypt your data in ephemeral (running application storage) and durable (durable application storage) storage. This means all data subject to a Flink [checkpoint](how-fault.md) or [snapshot](how-snapshots.md) will be encrypted by default. AOKs are the default encryption method in Amazon MSF and no additional set up is required. To encrypt data in transit, Amazon MSF uses TLS and HTTP\+SSL by default and requires no additional set up or configuration.

## Customer managed keys in Amazon MSF
<a name="cmk-flink"></a>

In Amazon MSF, CMK is a feature where you can encrypt your application's data with a key that you create, own, and manage on AWS KMS.

**Topics**
+ [What is encrypted with CMKs?](#what-is-encrypted-cmk)
+ [What isn't encrypted with CMKs?](#what-is-not-encrypted-cmk)
+ [Supported KMS key types](#supported-kms-key-types)
+ [KMS key permissions](#kms-key-permissions)
+ [KMS encryption context and constraints](#kms-encryption-context-constraints)
+ [Key transition](#kms-key-transition)
+ [Least-privileged key policy statements](#kms-least-privilege-policy-examples)
+ [AWS CloudTrail log entries](#kms-cloudtrail-log-entries)

### What is encrypted with CMKs?
<a name="what-is-encrypted-cmk"></a>

In an Amazon MSF application, data subject to a Flink checkpoint or snapshot will be encrypted with a CMK you define for that application. Consquently, your CMK will encrypt data stored in either running application storage or durable application storage. The [following sections](manage-cmk-api.md) describe the procedure to set up CMKs for your Amazon MSF applications.

The following rules set the key that encrypts an enhanced snapshot and its exported objects:
+ **Enhanced snapshots**: Managed Service for Apache Flink encrypts each enhanced snapshot with the key that the application uses when Managed Service for Apache Flink creates the enhanced snapshot. This rule applies to snapshots that you create with [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html) and to system snapshots. `CreateSnapshot` always uses the key of the application.
+ **Imported enhanced snapshots**: Managed Service for Apache Flink encrypts the new enhanced snapshot with the key in `DestinationEncryptionConfiguration` of the [`ImportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ImportSnapshot.html) request. If you omit `DestinationEncryptionConfiguration`, Managed Service for Apache Flink uses an AWS owned key.
+ **Exported enhanced snapshots**: Managed Service for Apache Flink encrypts the exported Amazon S3 objects with the key in `DestinationEncryptionConfiguration` of the [`ExportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ExportSnapshot.html) request. If the key type in `DestinationEncryptionConfiguration` is `AWS_OWNED_KEY`, or if you omit `DestinationEncryptionConfiguration`, Managed Service for Apache Flink specifies no key. Amazon S3 encrypts the exported objects with the default encryption of the destination bucket, which is SSE-S3 or a customer managed key of the bucket. Managed Service for Apache Flink does not encrypt the exported objects with an AWS owned key.

For more information, see [Encryption for imported and exported snapshots](snapshots-import-export.md#snapshots-import-export-encryption-for-imported-and-exported-snapshots).

**Key transition**  
When you change the CMK of an application to a different key, the operator (API caller) needs permissions for both the previous key and the new key. For more information, see [Key transition](#kms-key-transition).

### What isn't encrypted with CMKs?
<a name="what-is-not-encrypted-cmk"></a>

**Sources and sinks**  
Encryption of data sources and sinks isn't managed by Amazon MSF. It's managed by your source or sink configuration or application connector configuration.

**Retroactive application of encryption**  
CMK in Amazon MSF doesn't provide support to retroactively apply CMKs to an existing historic snapshot.

**Log encryption**  
Currently, Amazon MSF doesn't support log encryption using KMS CMK for logs generated by your application code jar. You'll need to make sure logs don't contain data that require CMK encryption.

**Encryption of data in transit**  
You can't use CMK to encrypt data in transit. By default, Amazon MSF encrypts all data in transit using TLS or HTTP and SSL.

### Supported KMS key types
<a name="supported-kms-key-types"></a>

CMK in Amazon MSF supports [symmetric keys](https://docs.aws.amazon.com/kms/latest/developerguide/symm-asymm-choose-key-spec.html#symmetric-cmks).

### KMS key permissions
<a name="kms-key-permissions"></a>

CMK in Amazon MSF requires permission to perform the following KMS actions. These permissions are necessary to validate access, create CMK encrypted running application storage, and store CMK encrypted application state in durable application storage.
+ 

**[kms:DescribeKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_DescribeKey.html)**  
Grants permission to resolve a KMS key alias to the key ARN.
+ 

**[kms:Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html)**  
Grants permission to accesses durable application state and provision running application storage.
+ 

**[kms:GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey.html)**  
Grants permission to store durable application state.
+ 

**[kms:GenerateDataKeyWithoutPlaintext](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html)**  
Grants permission to provision running application storage.
+ 

**[kms:CreateGrant](https://docs.aws.amazon.com/kms/latest/APIReference/API_CreateGrant.html)**  
Grants permission to access running application storage.

Enhanced snapshot operations need the following AWS KMS permissions when a customer managed key encrypts the data. Managed Service for Apache Flink checks the caller permissions when it validates the request. Managed Service for Apache Flink does not check them for an AWS owned key. The following table lists the AWS KMS permissions for each enhanced snapshot operation.


| Operation | Principal | Permissions on the key | 
| --- | --- | --- | 
| [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html) | The caller | kms:Decrypt and kms:GenerateDataKey on the key of the application. | 
| Restore with [`StartApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_StartApplication.html), [`UpdateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.html), or [`RollbackApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_RollbackApplication.html) | The caller | kms:DescribeKey, kms:Decrypt, and kms:GenerateDataKey on the key that encrypts the enhanced snapshot. | 
| [`ImportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ImportSnapshot.html) and [`ExportSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_ExportSnapshot.html) | The caller | For ExportSnapshot, kms:DescribeKey, kms:Decrypt, and kms:GenerateDataKey on the key of the enhanced snapshot. For ImportSnapshot, kms:Decrypt and kms:GenerateDataKey on the key in DestinationEncryptionConfiguration. | 
| ImportSnapshot and ExportSnapshot | The IAM role that you pass in the ImportSnapshot or ExportSnapshot request, and the caller | kms:Decrypt, kms:GenerateDataKey, and kms:DescribeKey on the key that encrypts the imported source or exported destination Amazon S3 objects. For the role policies and their conditions, see [IAM role for import and export](security-iam-snapshots.md#security-iam-snapshots-transfer-role). | 
| ImportSnapshot and ExportSnapshot | kinesisanalytics.amazonaws.com and infrastructure.kinesisanalytics.amazonaws.com | For ImportSnapshot, kinesisanalytics.amazonaws.com needs kms:Decrypt and kms:GenerateDataKey on the key in DestinationEncryptionConfiguration. For ExportSnapshot, both principals need kms:DescribeKey, and kinesisanalytics.amazonaws.com also needs kms:Decrypt and kms:GenerateDataKey, on the key of the enhanced snapshot. For the key policy, see [Key policy for enhanced snapshot import and export](manage-cmk-api.md#create-cmk-kms-key-policy-snapshot-transfer). | 

Grant each principal in the table the permissions in its row to avoid an `AccessDeniedException`. For more information, see [Encryption for imported and exported snapshots](snapshots-import-export.md#snapshots-import-export-encryption-for-imported-and-exported-snapshots).

### KMS encryption context and constraints
<a name="kms-encryption-context-constraints"></a>

CMK in Amazon MSF provides encryption context when accessing keys to read or write encrypted data, that is, `kms:EncryptionContext:aws:kinesisanalytics:arn`. In addition to encryption context, source contexts [aws:SourceArn](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn) and [aws:SourceAccount](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount) are provided when reading or writing durable application storage.

When creating grant to provision encrypted running application storage, Amazon MSF CMK creates grants with constraint type [EncryptionContextSubset](https://docs.aws.amazon.com/kms/latest/developerguide/create-grant-overview.html#grant-constraints) ensuring that only [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt.html) operation is allowed through `"kms:GrantOperations": "Decrypt"`.

For enhanced snapshots, the value of `kms:EncryptionContext:aws:kinesisanalytics:arn` depends on the operation:
+ **Create**: For [`CreateSnapshot`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateSnapshot.html) and system snapshots, the value is the ARN of the application.
+ **Restore**: Allow both the ARN of the application that restores the enhanced snapshot and the source ARN of the enhanced snapshot. The source ARN is the ARN of the application that created the enhanced snapshot, or the snapshot ARN for an imported enhanced snapshot. The same two values apply to `aws:SourceArn`.
+ **Import**: The value is the ARN of the new enhanced snapshot.
+ **Export**: To read the enhanced snapshot, the value is the same as for a restore. To encrypt the exported objects with the customer managed key in `DestinationEncryptionConfiguration`, the value is the ARN of the enhanced snapshot that you export.

The key policy must allow each value that your operations use. Keep the ARN of the application that created an enhanced snapshot in the key policy after you delete that application. Without that ARN, you cannot restore or export the enhanced snapshots of that application.

### Key transition
<a name="kms-key-transition"></a>

A key transition is a change from one CMK to a different CMK. When you change the CMK of an application to a different key, make sure that the operator (API caller) has permissions for both the previous key and the new key.

**Note**  
An application can start from a snapshot which was encrypted with AOK after it's configured to use CMK. An application can also start from a snapshot which was encrypted with an older CMK. To start an application from a snapshot, the operator (API caller) must have permissions for both the old and new key.

If you're changing the AWS KMS key ARN used for CMK you should use [UpdateApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_UpdateApplication.html) in Amazon MSF. This will ensure your Flink application will restart as part of `UpdateApplication` applying the CMK changes.

**Note**  
When you provide an alias or alias ARN, Amazon MSF resolves the alias to key ARN and stores the key ARN as the configured key for the application.

### Least-privileged key policy statements
<a name="kms-least-privilege-policy-examples"></a>

For information about key policy statements, see [Create a KMS key policy](manage-cmk-api.md#create-cmk-kms-key-policy) and [Application lifecycle operator (API caller) permissions](manage-cmk-api.md#create-cmk-kms-api-caller-permissions).

### AWS CloudTrail log entries
<a name="kms-cloudtrail-log-entries"></a>

When Amazon MSF uses CMKs in AWS KMS, AWS CloudTrail logs the AWS KMS API calls. The log entries show the AWS service that made the request, the KMS key ARN, the API action, and the timestamp. They don't include the encrypted data.

To find the calls that Amazon MSF makes, look for AWS KMS events where `userIdentity.invokedBy` is `kinesisanalytics.amazonaws.com`. The `aws:kinesisanalytics:arn` value in the encryption context of the event identifies the application or the enhanced snapshot. For more information, see [Logging AWS KMS API calls with AWS CloudTrail](https://docs.aws.amazon.com/kms/latest/developerguide/logging-using-cloudtrail.html) in the *AWS Key Management Service Developer Guide*.