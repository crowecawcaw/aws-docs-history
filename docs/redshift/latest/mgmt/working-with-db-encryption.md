Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Amazon Redshift database encryption

In Amazon Redshift, your database is encrypted by default to protect your data at rest.
Database encryption applies to the cluster and also to its snapshots.

You can modify an unencrypted cluster to use AWS Key Management Service (AWS KMS) encryption.
To do so, you can use either an AWS-owned key or a customer managed key.
When you modify your cluster to enable AWS KMS encryption, Amazon Redshift
automatically migrates your data to a new encrypted cluster. Snapshots created from the
encrypted cluster are also encrypted. You can also migrate an encrypted cluster to an unencrypted cluster
by modifying the cluster and changing the **Encrypt
database** option. For more information, see [Changing cluster encryption](changing-cluster-encryption.md "changing-cluster-encryption.md").

Though you can still transform the default encrypted cluster to unencrypted after creating the cluster,
we recommend that you keep cluster that contains sensitive data as encrypted.
Additionally, you might be required to use encryption
depending on the guidelines or regulations that govern your data. For example, the Payment
Card Industry Data Security Standard (PCI DSS), the Sarbanes-Oxley Act (SOX), the Health
Insurance Portability and Accountability Act (HIPAA), and other such regulations provide
guidelines for handling specific types of data.

Amazon Redshift uses a hierarchy of encryption keys to encrypt the database. You can use either
AWS Key Management Service (AWS KMS) or a hardware security module (HSM) to manage the top-level encryption
keys in this hierarchy. The process that Amazon Redshift uses for encryption differs depending on
how you manage keys. Amazon Redshift automatically integrates with AWS KMS but not with an HSM. When
you use an HSM, you must use client and server certificates to configure a trusted
connection between Amazon Redshift and your HSM.

###### Important

Amazon Redshift can lose access to the KMS key for a provisioned cluster or serverless
namespace when you disable the customer-managed KMS key. In these cases, Amazon Redshift
takes a backup of the Amazon Redshift data warehouse and puts it into an `inaccessible-kms-key`
state for 14 days. If you restore the KMS key within that period, Amazon Redshift will restore access
and the warehouse will function normally. If the 14 day period ends without the KMS key
being restored, Amazon Redshift will delete the data warehouse. While a warehouse is in
`inaccessible-kms-key` state, it has the following characteristics:

- You can’t run any queries on the data warehouse.
- If the data warehouse is the producer warehouse of a datashare,
  you can’t run datasharing queries against it from consumer warehouses.
- You can’t create cross-region snapshot copies.
  For information on restoring a disabled KMS key, see
  [Enable and disable keys](../../../kms/latest/developerguide/enabling-keys.md "../../../kms/latest/developerguide/enabling-keys.md")
  in the _AWS Key Management Service Developer Guide_. If the warehouse’s KMS key was deleted,
  you can use the backup to create a new data warehouse before the
  `inaccessible-kms-key` status warehouse is deleted.

## Encryption process improvements for better

performance and availability

### Encryption with RA3 nodes

Updates to the encryption process for RA3 nodes have made the experience much
better. Both read and write queries can run during the process with less performance
impact from the encryption. Also, encryption finishes much more quickly. The updated
process steps include a restore operation and migration of cluster metadata to a
target cluster. The improved experience applies to encryption types like AWS KMS, for
example. When you have petabyte-scale data volumes, the operation has been reduced
from weeks to days.

Prior to encrypting your cluster, if you plan to continue to run database
workloads, you can improve performance and speed up the process by adding nodes with
elastic resize. You can't use elastic resize when encryption is in process, so do it
before you encrypt. Note that adding nodes typically results in higher cost.

### Encryption with other node

types

When you encrypt a cluster with DC2 nodes, you don't have the
ability to run write queries, like with RA3 nodes. Only read queries can be
run.

### Usage notes for encryption with

RA3 nodes

The following insights and resources help you prepare for encryption and monitor
the process.

- **Running queries after starting encryption**
  – After encryption is started, reads and writes are available within
  about fifteen minutes. How long it takes the full encryption process to
  complete depends on the amount of data on the cluster and the workload
  levels.
- **How long does encryption take?** –
  The time to encrypt your data depends on several factors: These include the
  number of workloads running, the compute resources being used, the number of
  nodes, and the type of nodes. We recommend that you initially perform
  encryption in a test environment. As a rule of thumb, if you're working with
  data volumes in petabytes, it likely can take 1-3 days for encryption to
  complete.
- **How do I know encryption is finished?**
  – After you enable encryption, the completion of the first snapshot
  confirms that encryption is completed.
- **Rolling back encryption** – If you
  need to roll back the encryption operation, the best way to do this is to
  restore from the most recent backup taken prior to when encryption was
  initiated. You will have to re-apply any new updates
  (updates/deletes/inserts) following the last-backup.
- **Performing a table restore** – Note
  that you can't restore a table from an unencrypted cluster to an encrypted
  cluster.
- **Encrypting a single-node cluster** –
  Encrypting a single-node cluster has performance limitations. It takes
  longer than encryption for a multi-node cluster.
- **Creating a backup after encryption**
  – When you encrypt the data in your cluster, a backup isn't created
  until the cluster is fully encrypted. The amount of time this takes can
  vary. The time taken for backup can be hours to days, depending on the
  cluster size. After encryption completes, there can be a delay before you
  can create a backup.

Note that because a backup-and-restore operation occurs during the
encryption process, any tables or materialized views created with
`BACKUP NO` aren't retained. For more information, see [CREATE TABLE](../dg/r_CREATE_TABLE_NEW.md "../dg/r_CREATE_TABLE_NEW.md") or [CREATE
MATERIALIZED VIEW](../dg/materialized-view-create-sql-command.md "../dg/materialized-view-create-sql-command.md").

###### Topics

- [Encryption using
  AWS KMS](#working-with-aws-kms "#working-with-aws-kms")
- [Encryption using hardware security
  modules](#working-with-HSM "#working-with-HSM")
- [Encryption key rotation](#working-with-key-rotation "#working-with-key-rotation")
- [Changing cluster encryption](changing-cluster-encryption.md "changing-cluster-encryption.md")
- [Migrating to an HSM-encrypted
  cluster](migrating-to-an-encrypted-cluster.md "migrating-to-an-encrypted-cluster.md")
- [Rotating encryption keys](manage-key-rotation-console.md "manage-key-rotation-console.md")

## Encryption using

AWS KMS

When you choose AWS KMS for key management with Amazon Redshift, there is a four-tier hierarchy
of encryption keys. These keys, in hierarchical order, are the root key, a cluster
encryption key (CEK), a database encryption key (DEK), and data encryption keys.

When you launch your cluster, Amazon Redshift returns a list of the AWS KMS keys that Amazon Redshift or your
AWS account has created or has permission to use in AWS KMS. You select a KMS key to
use as your root key in the encryption hierarchy.

By default, Amazon Redshift selects an automatically generated AWS-owned key as the root key
for your AWS account to use in Amazon Redshift.

If you don't want to use the default key, you must have (or create) a customer
managed KMS key separately in AWS KMS before you launch your cluster in Amazon Redshift.
Customer managed keys give you more flexibility, including the ability to create, rotate,
disable, define access control for, and audit the encryption keys used to help protect
your data. For more information about creating KMS keys, see [Creating Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the
_AWS Key Management Service Developer Guide_.

If you want to use a AWS KMS key from another AWS account, you must have permission to
use the key and specify its Amazon Resource Name (ARN) in Amazon Redshift. For more information
about access to keys in AWS KMS, see [Controlling Access to Your Keys](../../../kms/latest/developerguide/control-access.md "../../../kms/latest/developerguide/control-access.md") in the
_AWS Key Management Service Developer Guide_.

After you choose a root key, Amazon Redshift requests that AWS KMS generate a data key and
encrypt it using the selected root key. This data key is used as the CEK in Amazon Redshift.
AWS KMS exports the encrypted CEK to Amazon Redshift, where it is stored internally on disk in a
separate network from the cluster along with the grant to the KMS key and the
encryption context for the CEK. Only the encrypted CEK is exported to Amazon Redshift; the
KMS key remains in AWS KMS. Amazon Redshift also passes the encrypted CEK over a secure channel
to the cluster and loads it into memory. Then, Amazon Redshift calls AWS KMS to decrypt the CEK
and loads the decrypted CEK into memory. For more information about grants, encryption
context, and other AWS KMS-related concepts, see [Concepts](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md") in the _AWS Key Management Service Developer Guide_.

Next, Amazon Redshift randomly generates a key to use as the DEK and loads it into memory in
the cluster. The decrypted CEK is used to encrypt the DEK, which is then passed over a
secure channel from the cluster to be stored internally by Amazon Redshift on disk in a
separate network from the cluster. Like the CEK, both the encrypted and decrypted
versions of the DEK are loaded into memory in the cluster. The decrypted version of the
DEK is then used to encrypt the individual encryption keys that are randomly generated
for each data block in the database.

When the cluster reboots, Amazon Redshift starts with the internally stored, encrypted
versions of the CEK and DEK, reloads them into memory, and then calls AWS KMS to decrypt
the CEK with the KMS key again so it can be loaded into memory. The decrypted CEK is
then used to decrypt the DEK again, and the decrypted DEK is loaded into memory and used
to encrypt and decrypt the data block keys as needed.

For more information about creating Amazon Redshift clusters that are encrypted with AWS KMS
keys, see [Creating a cluster](create-cluster.md "create-cluster.md").

### Copying AWS KMS–encrypted

snapshots to another AWS Region

AWS KMS keys are specific to an AWS Region.
If you want to enable copying of Amazon Redshift snapshots from an encrypted source cluster
to another AWS Region, but want to use your own AWS KMS key for snapshots in the destination,
you need to configure a grant for Amazon Redshift to use a root key in your account in the destination AWS Region.
This grant enables Amazon Redshift to encrypt snapshots in the destination AWS Region.
If you want snapshots in destination encrypted by an AWS Region-owned key, you don't
need to configure any grants in the destination AWS Region. For more information about
cross-Region snapshot copy, see [Copying a snapshot to another AWS
Region](cross-region-snapshot-copy.md "cross-region-snapshot-copy.md").

###### Note

If you enable copying of snapshots from an encrypted cluster and use AWS KMS for
your root key, you cannot rename your cluster because the cluster name is part
of the encryption context. If you must rename your cluster, you can disable
copying of snapshots in the source AWS Region, rename the cluster, and then
configure and enable copying of snapshots again.

The process to configure the grant for copying snapshots is as follows.

1. In the destination AWS Region, create a snapshot copy grant by doing the
   following:
   - If you do not already have an AWS KMS key to use, create one. For
     more information about creating AWS KMS keys, see [Creating Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the
     _AWS Key Management Service Developer Guide_.
   - Specify a name for the snapshot copy grant. This name must be
     unique in that AWS Region for your AWS account.
   - Specify the AWS KMS key ID for which you are creating the grant. If
     you do not specify a key ID, the grant applies to your default
     key.

2. In the source AWS Region, enable copying of snapshots and specify the
   name of the snapshot copy grant that you created in the destination AWS
   Region.

This preceding process is only necessary if you enable copying of snapshots using
the AWS CLI, the Amazon Redshift API, or SDKs. If you use the console, Amazon Redshift provides the
proper workflow to configure the grant when you enable cross-Region snapshot copy.
For more information about configuring cross-Region snapshot copy for
AWS KMS-encrypted clusters by using the console, see [Configuring cross-Region snapshot copy
for an AWS KMS–encrypted cluster](xregioncopy-kms-encrypted-snapshot.md "xregioncopy-kms-encrypted-snapshot.md").

Before the snapshot is copied to the destination AWS Region, Amazon Redshift decrypts
the snapshot using the root key in the source AWS Region and re-encrypts it
temporarily using a randomly generated RSA key that Amazon Redshift manages internally.
Amazon Redshift then copies the snapshot over a secure channel to the destination AWS
Region, decrypts the snapshot using the internally managed RSA key, and then
re-encrypts the snapshot using the root key in the destination AWS Region.

## Encryption using hardware security

modules

If you don't use AWS KMS for key management, you can use a hardware security module
(HSM) for key management with Amazon Redshift.

###### Important

HSM encryption is not supported for DC2 and RA3 node types.

HSMs are devices that provide direct control of key generation and management. They
provide greater security by separating key management from the application and database
layers. Amazon Redshift supports AWS CloudHSM Classic for key management. The encryption process is
different when you use HSM to manage your encryption keys instead of AWS KMS.

###### Important

Amazon Redshift supports only AWS CloudHSM Classic. We don't support the newer AWS CloudHSM service.

AWS CloudHSM Classic is closed to new customers. For more information, see [CloudHSM Classic
Pricing](https://aws.amazon.com/cloudhsm/pricing-classic/ "https://aws.amazon.com/cloudhsm/pricing-classic/"). AWS CloudHSM Classic isn't available in all AWS Regions. For more
information about available AWS Regions, see [AWS Region Table](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/").

When you configure your cluster to use an HSM, Amazon Redshift sends a request to the HSM to
generate and store a key to be used as the CEK. However, unlike AWS KMS, the HSM doesn’t
export the CEK to Amazon Redshift. Instead, Amazon Redshift randomly generates the DEK in the cluster
and passes it to the HSM to be encrypted by the CEK. The HSM returns the encrypted DEK
to Amazon Redshift, where it is further encrypted using a randomly-generated, internal root key
and stored internally on disk in a separate network from the cluster. Amazon Redshift also
loads the decrypted version of the DEK in memory in the cluster so that the DEK can be
used to encrypt and decrypt the individual keys for the data blocks.

If the cluster is rebooted, Amazon Redshift decrypts the internally-stored, double-encrypted
DEK using the internal root key to return the internally stored DEK to the CEK-encrypted
state. The CEK-encrypted DEK is then passed to the HSM to be decrypted and passed back
to Amazon Redshift, where it can be loaded in memory again for use with the individual data
block keys.

### Configuring a trusted connection

between Amazon Redshift and an HSM

When you opt to use an HSM for management of your cluster key, you need to
configure a trusted network link between Amazon Redshift and your HSM. Doing this requires
configuration of client and server certificates. The trusted connection is used to
pass the encryption keys between the HSM and Amazon Redshift during encryption and
decryption operations.

Amazon Redshift creates a public client certificate from a randomly generated private and
public key pair. These are encrypted and stored internally. You download and
register the public client certificate in your HSM, and assign it to the applicable
HSM partition.

You provide Amazon Redshift with the HSM IP address, HSM partition name, HSM partition
password, and a public HSM server certificate, which is encrypted by using an
internal root key. Amazon Redshift completes the configuration process and verifies that it
can connect to the HSM. If it cannot, the cluster is put into the INCOMPATIBLE_HSM
state and the cluster is not created. In this case, you must delete the incomplete
cluster and try again.

###### Important

When you modify your cluster to use a different HSM partition, Amazon Redshift verifies
that it can connect to the new partition, but it does not verify that a valid
encryption key exists. Before you use the new partition, you must replicate your
keys to the new partition. If the cluster is restarted and Amazon Redshift cannot find a
valid key, the restart fails. For more information, see [Replicating Keys Across HSMs](../../../cloudhsm/latest/userguide/cli-clone-hapg.md "../../../cloudhsm/latest/userguide/cli-clone-hapg.md").

After initial configuration, if Amazon Redshift fails to connect to the HSM, an event is
logged. For more information about these events, see [Amazon Redshift Event
Notifications](working-with-event-notifications.md "working-with-event-notifications.md").

## Encryption key rotation

In Amazon Redshift, you can rotate encryption keys for encrypted clusters. When you start the
key rotation process, Amazon Redshift rotates the CEK for the specified cluster and for any
automated or manual snapshots of the cluster. Amazon Redshift also rotates the DEK for the
specified cluster, but cannot rotate the DEK for the snapshots while they are stored
internally in Amazon Simple Storage Service (Amazon S3) and encrypted using the existing DEK.

While the rotation is in progress, the cluster is put into a ROTATING_KEYS state until
completion, at which time the cluster returns to the AVAILABLE state. Amazon Redshift handles
decryption and re-encryption during the key rotation process.

###### Note

You cannot rotate keys for snapshots without a source cluster. Before you delete a
cluster, consider whether its snapshots rely on key rotation.

Because the cluster is momentarily unavailable during the key rotation process, you
should rotate keys only as often as your data needs require or when you suspect the keys
might have been compromised. As a best practice, you should review the type of data that
you store and plan how often to rotate the keys that encrypt that data. The frequency
for rotating keys varies depending on your corporate policies for data security, and any
industry standards regarding sensitive data and regulatory compliance. Ensure that your
plan balances security needs with availability considerations for your cluster.

For more information about rotating keys, see [Rotating encryption keys](manage-key-rotation-console.md "manage-key-rotation-console.md").
