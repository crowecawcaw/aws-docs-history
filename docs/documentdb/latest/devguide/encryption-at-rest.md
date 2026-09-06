

# Encrypting Amazon DocumentDB data at rest
<a name="encryption-at-rest"></a>

**Note**  
AWS KMS is replacing the term *customer master key (CMK)* with *AWS KMS key* and *KMS key*. The concept has not changed. To prevent breaking changes, AWS KMS is keeping some variations of this term.

You encrypt data at rest in your Amazon DocumentDB cluster by specifying the storage encryption option when you create your cluster. Storage encryption is enabled cluster-wide and is applied to all instances, including the primary instance and any replicas. It is also applied to your cluster’s storage volume, data, indexes, logs, automated backups, and snapshots. 

Amazon DocumentDB uses the 256-bit Advanced Encryption Standard (AES-256) to encrypt your data using encryption keys stored in AWS Key Management Service (AWS KMS). When using an Amazon DocumentDB cluster with encryption at rest enabled, you don't need to modify your application logic or client connection. Amazon DocumentDB handles encryption and decryption of your data transparently, with minimal impact on performance.

Amazon DocumentDB integrates with AWS KMS and uses a method known as envelope encryption to protect your data. When an Amazon DocumentDB cluster is encrypted with an AWS KMS, Amazon DocumentDB asks AWS KMS to use your KMS key to [ generate a ciphertext data key](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.html) to encrypt the storage volume. The ciphertext data key is encrypted using the KMS key that you define, and is stored along with the encrypted data and storage metadata. When Amazon DocumentDB needs to access your encrypted data, it requests AWS KMS to decrypt the ciphertext data key using your KMS key and caches the plaintext data key in memory to efficiently encrypt and decrypt data in the storage volume.

The storage encryption facility in Amazon DocumentDB is available for all supported instance sizes and in all AWS Regions where Amazon DocumentDB is available.

## Enabling encryption at rest for an Amazon DocumentDB cluster
<a name="encryption-at-rest-enabling"></a>

You can enable or disable encryption at rest on an Amazon DocumentDB cluster when the cluster is provisioned using either the AWS Management Console or the AWS Command Line Interface (AWS CLI). Clusters that you create using the console have encryption at rest enabled by default. Clusters that you create using the AWS CLI have encryption at rest disabled by default. Therefore, you must explicitly enable encryption at rest using the `--storage-encrypted` parameter. In either case, after the cluster is created, you can't change the encryption at rest option.

Amazon DocumentDB uses AWS KMS to retrieve and manage encryption keys, and to define the policies that control how these keys can be used. If you don't specify an AWS KMS key identifier, Amazon DocumentDB uses the default AWS managed service KMS key. Amazon DocumentDB creates a separate KMS key for each AWS Region in your AWS account. For more information, see [AWS Key Management Service Concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html). 

To get started on creating your own KMS key, see [ Getting Started](https://docs.aws.amazon.com/kms/latest/developerguide/getting-started.html) in the *AWS Key Management Service Developer Guide*. 

**Important**  
You must use a symmetric encryption KMS key to encrypt your cluster as Amazon DocumentDB supports only symmetric encryption KMS keys. Do not use an asymmetric KMS key to attempt to encrypt the data in your Amazon DocumentDB clusters. For more information, see [ Asymmetric keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *AWS Key Management Service Developer Guide*. 

If Amazon DocumentDB can no longer access the KMS key for a cluster — for example, when the AWS account that owns the key is suspended, the key is disabled, the key is scheduled for deletion, or the key policy or grant that Amazon DocumentDB relies on is removed — the cluster first transitions to the `inaccessible-encryption-credentials-recoverable` status. While the cluster is in this status, Amazon DocumentDB stops the cluster's instances and you can't read from or write to the cluster, but the cluster can still be recovered if access to the KMS key is restored within 7 days. If access is not restored within 7 days, the cluster transitions to the terminal `inaccessible-encryption-credentials` status. From the terminal status, the cluster is no longer available and the current state of the database can't be recovered — you can only restore from a backup or perform a point-in-time restore using the original KMS key. For Amazon DocumentDB, backups are always enabled for at least 1 day.

**Note**  
Clusters that are part of a global cluster behave differently. When Amazon DocumentDB detects that it can no longer access the KMS key, all clusters in the global cluster transition directly to the terminal `inaccessible-encryption-credentials` status, skipping the recoverable status. This is because a cluster that is part of a global cluster can be stopped and started only when it is the only cluster in the global cluster. To recover, you must restore from a snapshot or perform a point-in-time restore. To delete the original clusters, you must first remove each cluster from the global cluster and then delete it.

**Important**  
You cannot change the KMS key for an encrypted cluster after you have already created it. Be sure to determine your encryption key requirements before you create your encrypted cluster.

------
#### [ Using the AWS Management Console ]

You specify the encryption at rest option when you create a cluster. Encryption at rest is enabled by default when you create a cluster using the AWS Management Console. It can't be changed after the cluster is created. 

**To specify the encryption at rest option when creating your cluster**

1. Create an Amazon DocumentDB cluster as described in the [Getting Started](https://docs.aws.amazon.com/documentdb/latest/devguide/connect-ec2.launch-cluster.html) section. However, in step 6, do not choose **Create cluster**. 

1. Under the **Authentication** section, choose **Show advanced settings**.

1. Scroll down to the **Encryption-at-rest** section.

1. Choose the option that you want for encryption at rest. Whichever option you choose, you can't change it after the cluster is created.
   + To encrypt data at rest in this cluster, choose **Enable encryption**.
   + If you don't want to encrypt data at rest in this cluster, choose **Disable encryption**. 

1. Choose the primary key that you want. Amazon DocumentDB uses the AWS Key Management Service (AWS KMS) to retrieve and manage encryption keys, and to define the policies that control how these keys can be used. If you don't specify an AWS KMS key identifier, Amazon DocumentDB uses the default AWS managed service KMS key. For more information, see [AWS Key Management Service Concepts](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html). 
**Note**  
After you create an encrypted cluster, you can't change the KMS key for that cluster. Be sure to determine your encryption key requirements before you create your encrypted cluster.

1. Complete the other sections as needed, and create your cluster.

------
#### [ Using the AWS CLI ]

To encrypt an Amazon DocumentDB cluster using the AWS CLI, run the [`create-db-cluster`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-clusters.html) command and specify the `--storage-encrypted` option. Amazon DocumentDB clusters created using the AWS CLI do not enable storage encryption by default.

The following example creates an Amazon DocumentDB cluster with storage encryption enabled.

In the following examples, replace each {{user input placeholder}} with your cluster's information.

**Example**  
For Linux, macOS, or Unix:  

```
aws docdb create-db-cluster \
  --db-cluster-identifier {{mydocdbcluster}} \
  --port 27017 \
  --engine docdb \
  --master-username {{SampleUser1}} \
  --master-user-password {{primaryPassword}} \
  --storage-encrypted
```
For Windows:  

```
aws docdb create-db-cluster ^
  --db-cluster-identifier {{SampleUser1}} ^
  --port 27017 ^
  --engine docdb ^
  --master-username {{SampleUser1}} ^
  --master-user-password {{primaryPassword}} ^
  --storage-encrypted
```

When you create an encrypted Amazon DocumentDB cluster, you can specify an AWS KMS key identifier, as in the following example.

**Example**  
For Linux, macOS, or Unix:  

```
aws docdb create-db-cluster \
  --db-cluster-identifier {{SampleUser1}} \
  --port 27017 \
  --engine docdb \
  --master-username {{primaryUsername}} \
  --master-user-password {{yourPrimaryPassword}} \
  --storage-encrypted \
  --kms-key-id {{key-arn-or-alias}}
```
For Windows:  

```
aws docdb create-db-cluster ^
  --db-cluster-identifier {{SampleUser1}} ^
  --port 27017 ^
  --engine docdb ^
  --master-username {{SampleUser1}} ^
  --master-user-password {{primaryPassword}} ^
  --storage-encrypted ^
  --kms-key-id {{key-arn-or-alias}}
```

**Note**  
After you create an encrypted cluster, you can't change the KMS key for that cluster. Be sure to determine your encryption key requirements before you create your encrypted cluster.

------

## Resolving an Amazon DocumentDB cluster in an inaccessible encryption state
<a name="encryption-at-rest-inaccessible"></a>

An Amazon DocumentDB cluster moves to an inaccessible encryption status when Amazon DocumentDB can't access the KMS key that the cluster was encrypted with. There are two such statuses, and the recovery path depends on which one the cluster is in.

### `inaccessible-encryption-credentials-recoverable` status
<a name="encryption-at-rest-inaccessible-recoverable"></a>

While the cluster is in the `inaccessible-encryption-credentials-recoverable` status, you can return the cluster to `available` by restoring Amazon DocumentDB's access to the KMS key and then starting the cluster. To resolve this status, do the following:

1. Confirm that the AWS account that owns the KMS key is active. If the account is suspended, reactivate it.

1. Confirm that the KMS key is enabled. For more information, see [Enabling and disabling keys](https://docs.aws.amazon.com/kms/latest/developerguide/enabling-keys.html) in the *AWS Key Management Service Developer Guide*.

1. Check whether the KMS key is scheduled for deletion. If it is, cancel the scheduled key deletion. For more information, see [Scheduling and canceling key deletion](https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys-scheduling-key-deletion.html) in the *AWS Key Management Service Developer Guide*.

1. Confirm that the KMS key policy and any grants that Amazon DocumentDB relies on still permit Amazon DocumentDB to use the key.

1. After access to the KMS key is restored, start the cluster by using the AWS Management Console or by running the `start-db-cluster` AWS CLI command.  
**Example**  

   For Linux, macOS, or Unix:

   ```
   aws docdb start-db-cluster \
     --db-cluster-identifier {{example-cluster}}
   ```

   For Windows:

   ```
   aws docdb start-db-cluster ^
     --db-cluster-identifier {{example-cluster}}
   ```

**Important**  
If access to the KMS key is not restored within 7 days, the cluster transitions to the terminal `inaccessible-encryption-credentials` status, from which it can't be started.

### `inaccessible-encryption-credentials` status
<a name="encryption-at-rest-inaccessible-terminal"></a>

The `inaccessible-encryption-credentials` status is terminal. The cluster can't be started, and the running state of the database can't be recovered. To recover your data, restore from a snapshot or perform a point-in-time restore to a new cluster. You must still have access to the original KMS key to perform the restore. If the KMS key was deleted, the data can't be recovered.

For more information, see [Restoring from a cluster snapshot](backup_restore-restore_from_snapshot.md) and [Restoring to a point in time](backup_restore-point_in_time_recovery.md).

**Note**  
Clusters that are part of a global cluster transition directly to the `inaccessible-encryption-credentials` status when access to the KMS key is lost, because a cluster that is part of a global cluster can be stopped and started only when it is the only cluster in the global cluster. To delete a cluster that is in this status, first remove each cluster from the global cluster, and then delete the clusters individually.

If you can't delete a cluster that is in the `inaccessible-encryption-credentials` status because deletion protection is enabled, turn off deletion protection by using the AWS CLI before retrying the delete.

**Example**  
For Linux, macOS, or Unix:  

```
aws docdb modify-db-cluster \
  --db-cluster-identifier {{example-cluster}} \
  --no-deletion-protection
```
For Windows:  

```
aws docdb modify-db-cluster ^
  --db-cluster-identifier {{example-cluster}} ^
  --no-deletion-protection
```

You can then delete the cluster by using the `delete-db-cluster` command.

**Example**  
For Linux, macOS, or Unix:  

```
aws docdb delete-db-cluster \
  --db-cluster-identifier {{example-cluster}} \
  --skip-final-snapshot
```
For Windows:  

```
aws docdb delete-db-cluster ^
  --db-cluster-identifier {{example-cluster}} ^
  --skip-final-snapshot
```

If the cluster does not delete after you run the preceding commands, contact [AWS Support](https://aws.amazon.com/support).

## Limitations for Amazon DocumentDB encrypted clusters
<a name="encryption-at-rest-limits"></a>

The following limitations exist for Amazon DocumentDB encrypted clusters.
+ You can enable or disable encryption at rest for an Amazon DocumentDB cluster only at the time that it is created, not after the cluster has been created. However, you can create an encrypted copy of an unencrypted cluster by creating a snapshot of the unencrypted cluster, and then restoring the unencrypted snapshot as a new cluster while specifying the encryption at rest option.

  For more information, see the following topics:
  + [Creating a manual cluster snapshot](backup_restore-create_manual_cluster_snapshot.md)
  + [Restoring from a cluster snapshot](backup_restore-restore_from_snapshot.md)
  + [Copying Amazon DocumentDB cluster snapshots](backup_restore-copy_cluster_snapshot.md)
+ Amazon DocumentDB clusters with storage encryption enabled can't be modified to disable encryption.
+ All instances, automated backups, snapshots, and indexes in an Amazon DocumentDB cluster are encrypted with the same KMS key.