# Encrypting Amazon RDS

resources

Amazon RDS can encrypt your Amazon RDS DB instances. Data that is encrypted at rest includes the underlying
storage for DB instances, its automated backups, read replicas,
and snapshots.

Amazon RDS encrypted DB instances use the
industry standard AES-256 encryption algorithm to encrypt your data on the
server that hosts your Amazon RDS DB instances. After your
data is encrypted, Amazon RDS handles authentication of access and
decryption of your data transparently with a minimal impact on performance. You
don't need to modify your database client applications to use encryption.

###### Note

For encrypted and unencrypted DB instances, data
that is in transit between the source and the read replicas is encrypted,
even when replicating across AWS Regions.

###### Topics

- [Overview of encrypting Amazon RDS
  resources](#Overview.Encryption.Overview "#Overview.Encryption.Overview")
- [Encrypting a DB
  instance](#Overview.Encryption.Enabling "#Overview.Encryption.Enabling")
- [Determining whether
  encryption is turned on for a DB instance](#Overview.Encryption.Determining "#Overview.Encryption.Determining")
- [Availability of Amazon RDS encryption](#Overview.Encryption.Availability "#Overview.Encryption.Availability")
- [Encryption in
  transit](#Overview.Encryption.InTransit "#Overview.Encryption.InTransit")
- [Limitations of Amazon RDS encrypted DB instances](#Overview.Encryption.Limitations "#Overview.Encryption.Limitations")

## Overview of encrypting Amazon RDS

resources

Amazon RDS encrypted DB instances provide an additional layer of data
protection by securing your data from unauthorized access to the underlying storage. You
can use Amazon RDS encryption to increase data protection of your applications deployed in
the cloud, and to fulfill compliance requirements for encryption at rest. For an Amazon RDS
encrypted DB instance, all logs, backups, and snapshots are encrypted. For more
information about the availability and limitations of encryption, see [Availability of Amazon RDS encryption](#Overview.Encryption.Availability "#Overview.Encryption.Availability") and [Limitations of Amazon RDS encrypted DB instances](#Overview.Encryption.Limitations "#Overview.Encryption.Limitations").

Amazon RDS uses an AWS Key Management Service key to encrypt these resources. AWS KMS combines
secure, highly available hardware and software to provide a key management system scaled
for the cloud. You can use an AWS managed key, or you can create customer managed keys.

When you create an encrypted DB instance, you can choose a customer managed key or the
AWS managed key for Amazon RDS to encrypt your DB instance. If you don't specify the
key identifier for a customer managed key, Amazon RDS uses the AWS managed key for your new DB
instance. Amazon RDS creates an AWS managed key for Amazon RDS for your AWS account. Your
AWS account has a different AWS managed key for Amazon RDS for each AWS Region.

To manage the customer managed keys used for encrypting and decrypting your Amazon RDS resources, you
use the [AWS Key Management Service (AWS KMS)](../../../kms/latest/developerguide.md "../../../kms/latest/developerguide.md").

Using AWS KMS, you can create customer managed keys and define the policies that control the use
of these customer managed keys. AWS KMS supports CloudTrail, so you can audit KMS key usage to verify
that customer managed keys are being used appropriately. You can use your customer managed keys with
Amazon Aurora and supported AWS services such as Amazon S3, Amazon EBS, and Amazon Redshift. For a list of
services that are integrated with AWS KMS, see [AWS Service Integration](https://aws.amazon.com/kms/features/#AWS_Service_Integration "https://aws.amazon.com/kms/features/#AWS_Service_Integration"). Some
considerations about using KMS keys:

- Once you have created an encrypted DB instance, you can't change the
  KMS key used by that DB instance. Therefore, be sure to determine your
  KMS key requirements before you create your encrypted DB instance.

If you must change the encryption key for your DB instance, create a manual snapshot
of your instance and enable encryption while copying the snapshot. For more
information, see [re:Post
Knowledge article](https://repost.aws/knowledge-center/update-encryption-key-rds "https://repost.aws/knowledge-center/update-encryption-key-rds").

- If you copy an encrypted snapshot, you can use a different KMS key to
  encrypt the target snapshot than the one that was used to encrypt the source
  snapshot.
- A read replica of an Amazon RDS encrypted instance must be encrypted using the same
  KMS key as the primary DB instance when both are in the same AWS Region.
- If the primary DB instance and read replica are in different AWS Regions,
  you encrypt the read replica using the KMS key for that AWS Region.
- You can't share a snapshot that has been encrypted using the
  AWS managed key of the AWS account that shared the snapshot.
- Amazon RDS also supports encrypting an Oracle or SQL Server DB instance with
  Transparent Data Encryption (TDE). TDE can be used with RDS encryption at rest,
  although using TDE and RDS encryption at rest simultaneously might slightly
  affect the performance of your database. You must manage different keys for each
  encryption method. For more information on TDE, see [Oracle Transparent Data Encryption](Appendix.Oracle.Options.md "Appendix.Oracle.Options.md") or [Support for Transparent Data Encryption in SQL Server](Appendix.SQLServer.Options.md "Appendix.SQLServer.Options.md").

###### Important

Amazon RDS loses access to the KMS key for a DB instance when you disable the KMS key.
If you lose access to a KMS key, the encrypted DB instance goes into the
`inaccessible-encryption-credentials-recoverable` state
2 hours after detection in instances where backups are enabled. The DB instance
remains in this state for seven days, during which the instance is stopped. API
calls made to the DB instance during this time might not succeed. To recover the DB instance,
enable the KMS key and restart this DB instance. Enable the KMS key from the
AWS Management Console, AWS CLI, or RDS API. Restart the DB instance using the AWS CLI command [start-db-instance](../../../cli/latest/reference/rds/start-db-instance.md "../../../cli/latest/reference/rds/start-db-instance.md") or
AWS Management Console.

The `inaccessible-encryption-credentials-recoverable` state only
applies to DB instances that can stop. This recoverable state is not applicable to instances
that can't stop, such as read replicas and instances with read replicas.
For more information, see [Limitations of stopping your DB instance](USER_StopInstance.md#USER_StopInstance.Limitations "USER_StopInstance.md#USER_StopInstance.Limitations").

If the DB instance isn't recovered within seven days, it goes into the terminal
`inaccessible-encryption-credentials` state. In this state, the DB instance
is not usable anymore and you can only restore the DB instance from a backup. We strongly
recommend that you always turn on backups for encrypted DB instances to guard against the
loss of encrypted data in your databases.

During the creation of a DB instance, Amazon RDS checks if the calling principal has access
to the KMS key and generates a grant from the KMS key that it uses for the
entire lifetime of the DB instance. Revoking the calling principal's access to the
KMS key does not affect a running database. When using KMS keys in cross-account
scenarios, such as copying a snapshot to another account, the KMS key needs to be
shared with the other account. If you create a DB instance from the snapshot without
specifying a different KMS key, the new instance uses the KMS key from the
source account. Revoking access to the key after you create the DB instance does not
affect the instance. However, disabling the key impacts all DB instances encrypted with
that key. To prevent this, specify a different key during the snapshot copy
operation.

DB instances with disabled backups remain available until the volumes are detached from
the host during an instance modification or a recovery.
RDS moves the instances into `inaccessible-encryption-credentials-recoverable`
state or `inaccessible-encryption-credentials` state as applicable.

For more information about KMS keys, see [AWS KMS keys](../../../kms/latest/developerguide/concepts.md#kms_keys "../../../kms/latest/developerguide/concepts.md#kms_keys") in the
_AWS Key Management Service Developer Guide_ and [AWS KMS key management](Overview.Encryption.md "Overview.Encryption.md").

## Encrypting a DB

instance

To encrypt a new DB instance, choose **Enable
encryption** on the Amazon RDS console. For information on creating
a DB instance, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").

If you use the [create-db-instance](../../../cli/latest/reference/rds/create-db-instance.md "../../../cli/latest/reference/rds/create-db-instance.md") AWS CLI command to create an encrypted DB
instance, set the `--storage-encrypted` parameter. If you use the
[CreateDBInstance](../APIReference/API_CreateDBInstance.md "../APIReference/API_CreateDBInstance.md") API operation, set the
`StorageEncrypted` parameter to true.

If you use the AWS CLI `create-db-instance` command to create an
encrypted DB instance with a customer managed key, set the `--kms-key-id`
parameter to any key identifier for the KMS key. If you use the Amazon RDS API
`CreateDBInstance` operation, set the `KmsKeyId`
parameter to any key identifier for the KMS key. To use a customer managed key in a
different AWS account, specify the key ARN or alias ARN.

## Determining whether

encryption is turned on for a DB instance

You can use the AWS Management Console, AWS CLI, or RDS API to determine whether
encryption at rest is turned on for a DB instance.

###### To determine whether encryption at rest is turned on for a DB

instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose
   **Databases**.
3. Choose the name of the DB instance that you want to check
   to view its details.
4. Choose the **Configuration** tab, and
   check the **Encryption** value under
   **Storage**.

It shows either **Enabled** or
**Not enabled**.

![Checking encryption at rest for a DB instance](images/encryption-check-db-instance.png)
To determine whether encryption at rest is turned on for a DB
instance by using the AWS CLI, call the [describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md") command with the following
option:

- `--db-instance-identifier` – The name of
  the DB instance.
  The following example uses a query to return either
  `TRUE` or `FALSE` regarding encryption at
  rest for the `mydb` DB instance.

###### Example

```
aws rds describe-db-instances --db-instance-identifier `mydb` --query "*[].{StorageEncrypted:StorageEncrypted}" --output text
```

To determine whether encryption at rest is turned on for a DB
instance by using the Amazon RDS API, call the [DescribeDBInstances](../APIReference/API_DescribeDBInstances.md "../APIReference/API_DescribeDBInstances.md") operation with the following
parameter:

- `DBInstanceIdentifier` – The name of the
  DB instance.

## Availability of Amazon RDS encryption

Amazon RDS encryption is currently available for all database
engines and storage types.

Amazon RDS encryption is available for most DB instance
classes. The following table lists DB instance classes that _don't
support_ Amazon RDS encryption:

| Instance type         | Instance class                                             |
| --------------------- | ---------------------------------------------------------- |
| General purpose (M1)  | db.m1.small<br>db.m1.medium<br>db.m1.large<br>db.m1.xlarge |
| Memory optimized (M2) | db.m2.xlarge<br>db.m2.2xlarge<br>db.m2.4xlarge             |
| Burstable (T2)        | db.t2.micro                                                |

## Encryption in

transit

**Encryption at the physical layer**

All data flowing accross AWS Regions over the AWS global network
is automatically encrypted at the physical layer before it leaves AWS
secured facilities. All traffic between AZs is encrypted. Additional layers of encryption,
including those listed in this section may provide additional protections.

**Encryption provided by Amazon VPC peering and Transit Gateway cross-Region peering**

All cross-Region traffic that uses Amazon VPC and Transit Gateway peering is automatically bulk-encrypted
when it exits a Region. An additional layer of encryption is automatically provided at the physical layer
for all traffic before it leaves AWS secured facilities.

**Encryption between instances**

AWS provides secure and private connectivity between DB instances of all
types. In addition, some instance types use the offload capabilities of the
underlying Nitro System hardware to automatically encrypt in-transit traffic
between instances. This encryption uses Authenticated Encryption with
Associated Data (AEAD) algorithms, with 256-bit encryption. There is no
impact on network performance. To support this additional in-transit traffic
encryption between instances, the following requirements must be met:

- The instances use the following instance types:
  - **General purpose**: M6i,
    M6id, M6in, M6idn, M7g
  - **Memory optimized**: R6i,
    R6id, R6in, R6idn, R7g, X2idn, X2iedn, X2iezn

- The instances are in the same AWS Region.
- The instances are in the same VPC or peered VPCs, and the traffic
  does not pass through a virtual network device or service, such as a
  load balancer or a transit gateway.

## Limitations of Amazon RDS encrypted DB instances

The following limitations exist for Amazon RDS encrypted
DB instances:

- You can only encrypt an Amazon RDS DB instance when you create it, not
  after the DB instance is created.

However, because you can encrypt a copy of an unencrypted
snapshot, you can effectively add encryption to an unencrypted DB
instance. That is, you can create a snapshot of your DB instance,
and then create an encrypted copy of that snapshot. You can then
restore a DB instance from the encrypted snapshot, and thus you have
an encrypted copy of your original DB instance. For more
information, see [Copying a DB snapshot for Amazon RDS](USER_CopySnapshot.md "USER_CopySnapshot.md").

- You can't turn off encryption on an encrypted DB instance.
- You can't create an encrypted snapshot of an unencrypted DB
  instance.
- A snapshot of an encrypted DB instance
  must be encrypted using the same KMS key as the DB instance.
- You can't have an encrypted read replica of an unencrypted DB
  instance or an unencrypted read replica of an encrypted DB
  instance.
- Encrypted read replicas must be encrypted with the same KMS key
  as the source DB instance when both are in the same AWS
  Region.
- You can't restore an unencrypted backup or snapshot to an
  encrypted DB instance.
- To copy an encrypted snapshot from one AWS Region to another,
  you must specify the KMS key in the destination AWS Region. This
  is because KMS keys are specific to the AWS Region that they are
  created in.

The source snapshot remains encrypted throughout the copy process.
Amazon RDS uses envelope encryption
to protect data during the copy process. For more information about
envelope encryption, see [Envelope encryption](../../../kms/latest/developerguide/concepts.md#enveloping "../../../kms/latest/developerguide/concepts.md#enveloping") in the _AWS Key Management Service
Developer Guide_.

- You can't unencrypt an encrypted DB instance. However, you can export
  data from an encrypted DB instance
  and import the data into an unencrypted DB instance.
