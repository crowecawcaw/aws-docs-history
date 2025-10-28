# Encrypting Amazon DocumentDB data at rest

###### Note

AWS KMS is replacing the term _customer master key (CMK)_ with
_AWS KMS key_ and _KMS key_. The concept has
not changed. To prevent breaking changes, AWS KMS is keeping some variations of this
term.

You encrypt data at rest in your Amazon DocumentDB cluster by specifying the storage encryption
option when you create your cluster. Storage encryption is enabled cluster-wide and is applied
to all instances, including the primary instance and any replicas. It is also applied to your
cluster’s storage volume, data, indexes, logs, automated backups, and snapshots.

Amazon DocumentDB uses the 256-bit Advanced Encryption Standard (AES-256) to encrypt your data using
encryption keys stored in AWS Key Management Service (AWS KMS). When using an Amazon DocumentDB cluster with encryption at
rest enabled, you don't need to modify your application logic or client connection. Amazon DocumentDB
handles encryption and decryption of your data transparently, with minimal impact on
performance.

Amazon DocumentDB integrates with AWS KMS and uses a method known as envelope encryption to protect
your data. When an Amazon DocumentDB cluster is encrypted with an AWS KMS, Amazon DocumentDB asks AWS KMS to use your KMS key to [generate a ciphertext data key](../../../kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.md "../../../kms/latest/APIReference/API_GenerateDataKeyWithoutPlaintext.md") to encrypt the storage volume. The ciphertext data
key is encrypted using the KMS key that you define, and is stored along with the encrypted data
and storage metadata. When Amazon DocumentDB needs to access your encrypted data, it requests AWS KMS to
decrypt the ciphertext data key using your KMS key and caches the plaintext data key in memory to
efficiently encrypt and decrypt data in the storage volume.

The storage encryption facility in Amazon DocumentDB is available for all supported instance sizes
and in all AWS Regions where Amazon DocumentDB is available.

## Enabling encryption at rest for an Amazon DocumentDB cluster

You can enable or disable encryption at rest on an Amazon DocumentDB cluster when the cluster is
provisioned using either the AWS Management Console or the AWS Command Line Interface (AWS CLI). Clusters that you create
using the console have encryption at rest enabled by default. Clusters that you create
using the AWS CLI have encryption at rest disabled by default. Therefore, you must explicitly
enable encryption at rest using the `--storage-encrypted` parameter. In either
case, after the cluster is created, you can't change the encryption at rest option.

Amazon DocumentDB uses AWS KMS to retrieve and manage encryption keys, and to define the policies
that control how these keys can be used. If you don't specify an AWS KMS key identifier,
Amazon DocumentDB uses the default AWS managed service KMS key.
Amazon DocumentDB creates a separate KMS key for each AWS Region in your AWS account. For more
information, see [AWS Key Management Service Concepts](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md").

To get started on creating your own KMS key, see [Getting
Started](../../../kms/latest/developerguide/getting-started.md "../../../kms/latest/developerguide/getting-started.md") in the _AWS Key Management Service Developer Guide_.

###### Important

You must use a symmetric encryption KMS key to encrypt your cluster as Amazon DocumentDB supports only
symmetric encryption KMS keys. Do not use an asymmetric KMS key to attempt to encrypt the data in your
Amazon DocumentDB clusters. For more information, see [Asymmetric keys in AWS KMS](../../../kms/latest/developerguide/symmetric-asymmetric.md "../../../kms/latest/developerguide/symmetric-asymmetric.md") in the _AWS Key Management Service Developer Guide_.

If Amazon DocumentDB can no longer gain access to the encryption key for a cluster — for
example, when access to a key is revoked — the encrypted cluster goes into a
terminal state. In this case, you can only restore the cluster from a backup. For Amazon DocumentDB,
backups are always enabled for 1 day.

In addition, if you disable the key for an encrypted Amazon DocumentDB cluster, you will
eventually lose read and write access to that cluster. When Amazon DocumentDB encounters a cluster
that is encrypted by a key that it doesn't have access to, it puts the cluster into a
terminal state. In this state, the cluster is no longer available, and the current state of
the database can't be recovered. To restore the cluster, you must re-enable access to the
encryption key for Amazon DocumentDB, and then restore the cluster from a backup.

###### Important

You cannot change the KMS key for an encrypted cluster after you have already created it.
Be sure to determine your encryption key requirements before you create your encrypted
cluster.

Using the AWS Management Console
You specify the encryption at rest option when you create a cluster. Encryption at
rest is enabled by default when you create a cluster using the AWS Management Console. It can't be
changed after the cluster is created.

###### To specify the encryption at rest option when creating your cluster

1. Create an Amazon DocumentDB cluster as described in the [Getting Started](connect-ec2.md "connect-ec2.md") section. However, in step 6, do not choose
   **Create cluster**.
2. Under the **Authentication** section, choose **Show
   advanced settings**.
3. Scroll down to the **Encryption-at-rest** section.
4. Choose the option that you want for encryption at rest. Whichever option you
   choose, you can't change it after the cluster is created.
   - To encrypt data at rest in this cluster, choose **Enable
     encryption**.
   - If you don't want to encrypt data at rest in this cluster, choose
     **Disable encryption**.

5. Choose the primary key that you want. Amazon DocumentDB uses the AWS Key Management Service (AWS KMS) to
   retrieve and manage encryption keys, and to define the policies that control
   how these keys can be used. If you don't specify an AWS KMS key identifier,
   Amazon DocumentDB uses the default AWS managed service KMS key. For more
   information, see [AWS Key Management Service
   Concepts](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md").

###### Note

After you create an encrypted cluster, you can't change the KMS key for that
cluster. Be sure to determine your encryption key requirements before you
create your encrypted cluster. 6. Complete the other sections as needed, and create your cluster.

Using the AWS CLI
To encrypt an Amazon DocumentDB cluster using the AWS CLI, run the [`create-db-cluster`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-clusters.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb/describe-db-clusters.html") command and specify the
`--storage-encrypted` option. Amazon DocumentDB
clusters created using the AWS CLI do not enable storage encryption by default.

The following example creates an Amazon DocumentDB cluster with storage encryption
enabled.

In the following examples, replace each `user input placeholder` with your cluster's information.

For Linux, macOS, or Unix:

```
aws docdb create-db-cluster \
  --db-cluster-identifier `mydocdbcluster` \
  --port 27017 \
  --engine docdb \
  --master-username `SampleUser1` \
  --master-user-password `primaryPassword` \
  --storage-encrypted
```

For Windows:

```
aws docdb create-db-cluster ^
  --db-cluster-identifier `SampleUser1` ^
  --port 27017 ^
  --engine docdb ^
  --master-username `SampleUser1` ^
  --master-user-password `primaryPassword` ^
  --storage-encrypted
```

When you create an encrypted Amazon DocumentDB cluster, you can specify an AWS KMS key
identifier, as in the following example.

For Linux, macOS, or Unix:

```
aws docdb create-db-cluster \
  --db-cluster-identifier `SampleUser1` \
  --port 27017 \
  --engine docdb \
  --master-username `primaryUsername` \
  --master-user-password `yourPrimaryPassword` \
  --storage-encrypted \
  --kms-key-id `key-arn-or-alias`
```

For Windows:

```
aws docdb create-db-cluster ^
  --db-cluster-identifier `SampleUser1` ^
  --port 27017 ^
  --engine docdb ^
  --master-username `SampleUser1` ^
  --master-user-password `primaryPassword` ^
  --storage-encrypted ^
  --kms-key-id `key-arn-or-alias`
```

###### Note

After you create an encrypted cluster, you can't change the KMS key for that
cluster. Be sure to determine your encryption key requirements before you create
your encrypted cluster.

## Limitations for Amazon DocumentDB encrypted clusters

The following limitations exist for Amazon DocumentDB encrypted clusters.

- You can enable or disable encryption at rest for an Amazon DocumentDB cluster only at the
  time that it is created, not after the cluster has been created. However, you can
  create an encrypted copy of an unencrypted cluster by creating a snapshot of the
  unencrypted cluster, and then restoring the unencrypted snapshot as a new cluster
  while specifying the encryption at rest option.

For more information, see the following topics:

    + [Creating a manual cluster snapshot](backup_restore-create_manual_cluster_snapshot.md "backup_restore-create_manual_cluster_snapshot.md")
    + [Restoring from a cluster snapshot](backup_restore-restore_from_snapshot.md "backup_restore-restore_from_snapshot.md")
    + [Copying Amazon DocumentDB cluster snapshots](backup_restore-copy_cluster_snapshot.md "backup_restore-copy_cluster_snapshot.md")

- Amazon DocumentDB clusters with storage encryption enabled can't be modified to disable
  encryption.
- All instances, automated backups, snapshots, and indexes in an Amazon DocumentDB cluster are
  encrypted with the same KMS key.
