# At-Rest Encryption in MemoryDB

To help keep your data secure, MemoryDB and Amazon S3 provide different ways to restrict access
to data in your clusters. For more information, see [MemoryDB and Amazon VPC](vpcs.md "vpcs.md")
and [Identity and access management in MemoryDB](iam.md "iam.md").

MemoryDB at-rest encryption is always enabled to increase data security by encrypting persistent data. It encrypts the following aspects:

- Data in the transaction log
- Disk during sync, snapshot and swap operations
- Snapshots stored in Amazon S3

MemoryDB offers default (service managed) encryption at rest, as well as ability to use your own symmetric customer managed customer root keys in [AWS Key Management Service (KMS)](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md").

Data stored on SSDs (solid-state drives) in data-tiering enabled clusters is always encrypted by default.

For information on encryption in transit, see [In-transit encryption (TLS) in MemoryDB](in-transit-encryption.md "in-transit-encryption.md")

###### Topics

- [Using Customer Managed Keys from AWS KMS](#using-customer-managed-keys-for-memorydb-security "#using-customer-managed-keys-for-memorydb-security")
- [See Also](#at-rest-encryption-see-also "#at-rest-encryption-see-also")

## Using Customer Managed Keys from AWS KMS

MemoryDB supports symmetric customer managed root keys (KMS key) for encryption at rest. Customer-managed KMS keys are encryption keys that you create, own and manage in your AWS account. For more information,
see [Customer Root Keys](../../../kms/latest/developerguide/concepts.md#root_keys "../../../kms/latest/developerguide/concepts.md#root_keys") in the _AWS Key Management Service Developer Guide_. The keys must be created in AWS KMS before they can be used
with MemoryDB.

To learn how to create AWS KMS root keys, see [Creating Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer Guide_.

MemoryDB allows you to integrate with AWS KMS. For more information, see [Using Grants](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md")
in the _AWS Key Management Service Developer Guide_. No customer action is needed to enable MemoryDB integration with AWS KMS.

The `kms:ViaService` condition key limits use of an AWS KMS key to requests from specified AWS services. To use `kms:ViaService` with MemoryDB, include both ViaService names in the condition key value:
`memorydb.amazon_region.amazonaws.com`. For more information, see
[kms:ViaService](../../../kms/latest/developerguide/policy-conditions.md#conditions-kms-via-service "../../../kms/latest/developerguide/policy-conditions.md#conditions-kms-via-service").

You can use [AWS CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") to track the requests that MemoryDB sends to AWS Key Management Service
on your behalf. All API calls to AWS Key Management Service related to customer managed keys have corresponding CloudTrail logs.
You can also see the grants that MemoryDB creates by calling the [ListGrants](../../../kms/latest/APIReference/API_ListGrants.md "../../../kms/latest/APIReference/API_ListGrants.md") KMS API call.

Once a cluster is encrypted using a customer managed key, all snapshots for the cluster are encrypted as follows:

- Automatic daily snapshots are encrypted using the customer managed key associated with the cluster.
- Final snapshot created when cluster is deleted, is also encrypted using the customer managed key associated with the cluster.
- Manually created snapshots are encrypted by default to use the KMS key associated with the cluster. You may override this by choosing another customer managed key.
- Copying a snapshot defaults to using customer managed key associated with the source snapshot. You may override this by choosing another customer managed key.

###### Note

- Customer managed keys cannot be used when exporting snapshots to your selected Amazon S3 bucket. However, all snapshots exported to Amazon S3 are encrypted using
  [Server side encryption.](../../../AmazonS3/latest/dev/UsingServerSideEncryption.md "../../../AmazonS3/latest/dev/UsingServerSideEncryption.md") You may choose to copy the snapshot file to a new S3 object and encrypt using a customer managed
  KMS key, copy the file to another S3 bucket that is set up with default encryption using a KMS key or change an encryption option in the file itself.
- You can also use customer managed keys to encrypt manually-created snapshots that do not use customer managed keys for encryption. With this option, the snapshot file stored in Amazon S3 is encrypted using
  a KMS key, even though the data is not encrypted on the original cluster.
  Restoring from a snapshot allows you to choose from available encryption options, similar to encryption choices available when creating a new cluster.

- If you delete the key or [disable](../../../kms/latest/developerguide/enabling-keys.md "../../../kms/latest/developerguide/enabling-keys.md") the key and [revoke grants](../../../kms/latest/APIReference/API_RevokeGrant.md "../../../kms/latest/APIReference/API_RevokeGrant.md") for the key that you used to encrypt a cluster,
  the cluster becomes irrecoverable. In other words, it cannot be modified or recovered after a hardware failure. AWS KMS deletes root keys only after a waiting period of at least seven days.
  After the key is deleted, you can use a different customer managed key to create a snapshot for archival purposes.
- Automatic key rotation preserves the properties of your AWS KMS root keys, so the rotation has no effect on your ability to access your MemoryDB data.
  Encrypted MemoryDB clusters don't support manual key rotation, which involves creating a new root key and updating
  any references to the old key. To learn more, see [Rotating Customer root Keys](../../../kms/latest/developerguide/rotate-keys.md "../../../kms/latest/developerguide/rotate-keys.md") in the _AWS Key Management Service Developer Guide_.
- Encrypting a MemoryDB cluster using KMS key requires one grant per cluster.
  This grant is used throughout the lifespan of the cluster. Additionally, one grant per snapshot is used during snapshot creation.
  This grant is retired once the snapshot is created.
- For more information on AWS KMS grants and limits, see [Quotas](../../../kms/latest/developerguide/limits.md "../../../kms/latest/developerguide/limits.md") in the _AWS Key Management Service Developer Guide_.

## See Also

- [In-transit encryption (TLS) in MemoryDB](in-transit-encryption.md "in-transit-encryption.md")
- [MemoryDB and Amazon VPC](vpcs.md "vpcs.md")
- [Identity and access management in MemoryDB](iam.md "iam.md")
