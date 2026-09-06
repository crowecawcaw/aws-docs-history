

# Storage or throughput capacity updates fail
<a name="admin-actions-ts"></a>

There are a number of potential causes for file system storage and throughput capacity update requests to fail, each with their own resolution.

## Storage capacity increase fails because Amazon FSx can't access the file system's AWS KMS key
<a name="w2aac37c17b5"></a>

A storage capacity increase request failed because Amazon FSx was unable to access the KMS key used to encrypt file system.

You need to ensure that Amazon FSx has access to the KMS key used to encrypt the file system in order to run the administrative action. Use the following information to resolve the key access issue. 
+ If the KMS key has been deleted, the file system and any of its backups using the deleted KMS key are unrecoverable. For more information, see [Deleting AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html) in the AWS Key Management Service Developer Guide.
+ If the KMS key is disabled, and it is a customer managed key, you will need to re-enable it, and then retry the storage capacity increase request. For more information, see [Enabling and disabling keys](https://docs.aws.amazon.com/kms/latest/developerguide/enabling-keys.html) in the AWS Key Management Service Developer Guide.
+ If the key is invalid because of its pending deletion, you must [cancel the key deletion](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-scheduling-key-deletion.html) while it is still in a `PendingDeletion` state. You can retry the request once the KMS key is `Enabled`.
+ If the key is invalid because of its pending import, you must wait until the import has completed, and then retry the storage increase request.
+ If the key's grant limit has been exceeded, you must request an increase in the number of grants for the key. For more information, see [Resource quotas](https://docs.aws.amazon.com/kms/latest/developerguide/resource-limits.html) in the AWS Key Management Service Developer Guide. When the quota increase is granted, retry the storage increase request.

## Storage or throughput capacity update fails because the self-managed Active Directory is misconfigured
<a name="w2aac37c17b7"></a>

The storage capacity or throughput capacity update request failed because your file system's self-managed Active Directory is in a misconfigured state.

To resolve the specific misconfigured state, see [File system is in a misconfigured state](misconfigured-ad-config.md).

## Storage capacity increase fails because of insufficient throughput capacity
<a name="w2aac37c17b9"></a>

The storage capacity increase request failed because the file system's throughput capacity is set to 8 MBps.

Increase the file system's throughput capacity to a minimum of 16 MBps, then retry the request. For more information, see [Managing throughput capacity](managing-throughput-capacity.md).

## Throughput capacity update to 8 MBps fails
<a name="w2aac37c17c11"></a>

A request to modify a file system's throughput capacity to 8 MBps failed.

This can occur when a storage capacity increase request is pending or in progress. Storage capacity increases require a minimum throughput of 16 MBps. Wait until the storage capacity increase request has completed, and then retry the throughput capacity modification request.