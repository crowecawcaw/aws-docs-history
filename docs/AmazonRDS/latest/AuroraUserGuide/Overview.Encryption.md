

# Encrypting Amazon Aurora resources
<a name="Overview.Encryption"></a>

Amazon Aurora protects your data both at rest and in transit—whether moving between on-premises clients and Amazon Aurora, or between Amazon Aurora and other AWS resources. Amazon Aurora encrypts all user data in your Amazon Aurora DB clusters including logs, automated backups, and snapshots.

After your data is encrypted, Amazon Aurora handles authentication of access and decryption of your data transparently with a minimal impact on performance. You don't need to modify your database client applications to use encryption.

**Note**  
For encrypted and unencrypted DB clusters, data that is in transit between the source and the read replicas is encrypted, even when replicating across AWS Regions.

**Topics**
+ [Overview of encryption in Amazon Aurora resources](#Overview.Encryption.Overview)
+ [Encrypting an Amazon Aurora DB cluster](#Overview.Encryption.Enabling)
+ [Determining whether encryption is turned on for a DB cluster](#Overview.Encryption.Determining)
+ [Availability of Amazon Aurora encryption](#Overview.Encryption.Availability)
+ [Encryption in transit](#Overview.Encryption.InTransit)
+ [Limitations of Amazon Aurora encrypted DB clusters](#Overview.Encryption.Limitations)

## Overview of encryption in Amazon Aurora resources
<a name="Overview.Encryption.Overview"></a>

Amazon Aurora encrypted DB clusters provide an additional layer of data protection by securing your data from unauthorized access to the underlying storage. All new database clusters created on or after  February 18, 2026 , in Amazon Aurora are encrypted at rest using industry standard AES-256 encryption. This encryption happens automatically in the background, securing your data without requiring any action from you. It also helps reduce the operational burden and complexity involved in protecting sensitive data. With encryption at rest, you can secure compliance-sensitive and security-critical applications against both accidental and malicious threats while meeting regulatory requirements.

Amazon Aurora uses an AWS Key Management Service key to encrypt these resources. AWS KMS combines secure, highly available hardware and software to provide a key management system scaled for the cloud. When creating a new database cluster, Amazon Aurora uses Server-Side Encryption (SSE) with an [AWS-owned key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-key) by default. However, you can choose from three encryption types based on your security and compliance needs:
+ **AWS owned key (SSE-RDS)** – A fully AWS-controlled encryption key that you cannot view or manage, used automatically by Aurora for default encryption.
+ **AWS managed key (AMK)** – This key is created and managed by AWS and is visible in your account but not customizable. There is no monthly fee, but AWS KMS API charges will apply.
+ **Customer managed key (CMK)** – The key is stored in your account and is created, owned, and managed by you. You have full control over the KMS key (AWS KMS charges apply).

AWS managed keys are a legacy encryption option that remains available for backward compatibility. Amazon Aurora uses AWS-owned keys by default to encrypt your data, providing strong security protection without additional charges or management overhead. For most use cases, we recommend using either the default AWS-owned key for simplicity and cost efficiency, or a customer managed key (CMK) if you require full control over your encryption keys. For more information about key types, see [ customer managed keys and AWS managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt).

**Note**  
**Important:** For source database instances or clusters created before February 18, 2026 , where you did not opt in for encryption, snapshots, clones, and Amazon Aurora replicas (read instance) created from those sources will remain unencrypted. However, restore operations and logical replication outside the Amazon Aurora cluster will produce encrypted instances.

 For an Amazon Aurora encrypted DB cluster, all DB instances, logs, backups, and snapshots are encrypted. For more information about the availability and limitations of encryption, see [Availability of Amazon Aurora encryption](#Overview.Encryption.Availability) and [Limitations of Amazon Aurora encrypted DB clusters](#Overview.Encryption.Limitations).

When you create an encrypted DB cluster, you can choose a customer managed key or the AWS managed key for Amazon Aurora to encrypt your DB cluster, if you don't specify the key identifier for a customer managed key, Amazon Aurora uses the AWS managed key for your new DB cluster. Amazon Aurora creates an AWS managed key for Amazon Aurora for your AWS account. Your AWS account has a different AWS managed key for Amazon Aurora for each AWS Region.

To manage the customer managed keys used for encrypting and decrypting your Amazon Aurora resources, you use the [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/). 

Using AWS KMS, you can create customer managed keys and define the policies to control the use of these customer managed keys. AWS KMS supports CloudTrail, so you can audit KMS key usage to verify that customer managed keys are being used appropriately. You can use your customer managed keys with Amazon Aurora and supported AWS services such as Amazon S3, Amazon EBS, and Amazon Redshift. For a list of services that are integrated with AWS KMS, see [AWS Service Integration](https://aws.amazon.com/kms/features/#AWS_Service_Integration). Some considerations about using KMS keys: 
+ Once you create an encrypted DB instance, you cannot change the KMS key used by that instance. Be sure to determine your KMS key requirements before creating your encrypted DB instance. If you need to change the encryption key for your DB cluster, follow these steps:
  + Create a manual snapshot of your cluster. 
  + Restore the snapshot and enable encryption with your desired KMS key during the restore operation. You cannot enable encryption with an AWS owned key if your cluster was originally encrypted with an AWS managed key or a customer managed key. 
+ If you restore an unencrypted snapshot and choose no encryption, the database cluster created will be encrypted using the default encryption at rest (AWS-owned key).
+ You can't share a snapshot that has been encrypted using the AWS managed key of the AWS account that shared the snapshot.
+ Each DB instance in the DB cluster shares the same storage encrypted with the same KMS key.

**Important**  
Amazon Aurora can lose access to the KMS key for a DB cluster when you disable the KMS key. In these cases, the encrypted DB cluster goes into `inaccessible-encryption-credentials-recoverable` state. The DB cluster remains in this state for seven days, during which the instance is stopped. API calls made to the DB cluster during this time might not succeed. To recover the DB cluster, enable the KMS key and restart this DB cluster. You can enable the KMS key from the AWS Management Console, AWS CLI, or RDS API. Restart the DB cluster using the AWS CLI command [start-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/start-db-cluster.html) or AWS Management Console.  
The `inaccessible-encryption-credentials-recoverable` state only applies to DB clusters that can stop. This recoverable state is not applicable to instances that can't stop, such as clusters with cross-Region read replicas. For more information, see [Limitations for stopping and starting Aurora DB clusters](aurora-cluster-stop-start.md#aurora-cluster-stop-limitations).  
If the DB cluster isn't recovered within seven days, it goes into the terminal `inaccessible-encryption-credentials` state. In this state, the DB cluster is not usable anymore and you can only restore the DB cluster from a backup. We strongly recommend that you always turn on backups to guard against the loss of data in your databases.  
During the creation of a DB cluster, Aurora checks if the calling principal has access to the KMS key and generates a grant from the KMS key that it uses for the entire lifetime of the DB cluster. Revoking the calling principals access to the KMS key does not affect a running database. When using KMS keys in cross-account scenarios, such as copying a snapshot to another account, the KMS key needs to be shared with the other account. If you create a DB cluster from the snapshot without specifying a different KMS key, the new cluster uses the KMS key from the source account. Revoking access to the key after you create the DB cluster does not affect the cluster. However, disabling the key impacts all DB clusters encrypted with that key. To prevent this, specify a different key during the snapshot copy operation.

For more information about KMS keys, see [AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms_keys) in the *AWS Key Management Service Developer Guide* and [AWS KMS key management](Overview.Encryption.Keys.md). 

## Encrypting an Amazon Aurora DB cluster
<a name="Overview.Encryption.Enabling"></a>

All new DB clusters created on or after February 18, 2026, are encrypted by default with an AWS owned key.

To encrypt a new DB cluster, using AWS managed key or customer managed key, choose the option on the console. For information on creating a DB cluster, see [Creating an Amazon Aurora DB cluster](Aurora.CreateInstance.md).

If you use the [create-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-cluster.html) AWS CLI command to create an encrypted DB cluster, set the `--storage-encrypted` parameter. If you use the [CreateDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBCluster.html) API operation, set the `StorageEncrypted` parameter to true.

Once you have created an encrypted DB cluster, you can't change the KMS key used by that DB cluster. Therefore, be sure to determine your KMS key requirements before you create your encrypted DB cluster.

If you use the AWS CLI `create-db-cluster` command to create an encrypted DB cluster with a customer managed key, set the `--kms-key-id` parameter to any key identifier for the KMS key. If you use the Amazon RDS API `CreateDBInstance` operation, set the `KmsKeyId` parameter to any key identifier for the KMS key. To use a customer managed key in a different AWS account, specify the key ARN or alias ARN.

## Determining whether encryption is turned on for a DB cluster
<a name="Overview.Encryption.Determining"></a>

You can use the AWS Management Console, AWS CLI, or RDS API to determine whether encryption at rest is turned on for a DB cluster.

### Console
<a name="Overview.Encryption.Determining.CON"></a>

**To determine whether encryption at rest is turned on for a DB cluster**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**.

1. Choose the name of the DB cluster that you want to check to view its details.

1. Choose the **Configuration** tab and check the **Encryption** value.  
![Checking encryption at rest for a DB cluster.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/encryption-aurora-instance.png)

### AWS CLI
<a name="Overview.Encryption.Determining.CLI"></a>

To determine whether encryption at rest is turned on for a DB cluster by using the AWS CLI, call the [describe-db-clusters](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-clusters.html) command with the following option: 
+ `--db-cluster-identifier` – The name of the DB cluster.

The following example uses a query to return either `TRUE` or `FALSE` regarding encryption at rest for the `mydb` DB cluster.

**Example**  

```
1. aws rds describe-db-clusters --db-cluster-identifier {{mydb}} --query "*[].{StorageEncrypted:StorageEncrypted}" --output text
```

### RDS API
<a name="Overview.Encryption.Determining.API"></a>

To determine whether encryption at rest is turned on for a DB cluster by using the Amazon RDS API, call the [DescribeDBClusters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusters.html) operation with the following parameter: 
+ `DBClusterIdentifier` – The name of the DB cluster.

## Availability of Amazon Aurora encryption
<a name="Overview.Encryption.Availability"></a>

Amazon Aurora encryption is currently available for all database engines and storage types.

**Note**  
Amazon Aurora encryption is not available for the db.t2.micro DB instance class.

## Encryption in transit
<a name="Overview.Encryption.InTransit"></a>

**Encryption at the physical layer**  
All data flowing accross AWS Regions over the AWS global network is automatically encrypted at the physical layer before it leaves AWS secured facilities. All traffic between AZs is encrypted. Additional layers of encryption, including those listed in this section may provide additional protections.

**Encryption provided by Amazon VPC peering and Transit Gateway cross-Region peering**  
All cross-Region traffic that uses Amazon VPC and Transit Gateway peering is automatically bulk-encrypted when it exits a Region. An additional layer of encryption is automatically provided at the physical layer for all traffic before it leaves AWS secured facilities.

**Encryption between instances**  
AWS provides secure and private connectivity between DB instances of all types. In addition, some instance types use the offload capabilities of the underlying Nitro System hardware to automatically encrypt in-transit traffic between instances. This encryption uses Authenticated Encryption with Associated Data (AEAD) algorithms, with 256-bit encryption. There is no impact on network performance. To support this additional in-transit traffic encryption between instances, the following requirements must be met:  
+ The instances use the following instance types:
  + **General purpose**: M6i, M6id, M6in, M6idn, M7g
  + **Memory optimized**: R6i, R6id, R6in, R6idn, R7g, X2idn, X2iedn, X2iezn
+ The instances are in the same AWS Region.
+ The instances are in the same VPC or peered VPCs, and the traffic does not pass through a virtual network device or service, such as a load balancer or a transit gateway.

## Limitations of Amazon Aurora encrypted DB clusters
<a name="Overview.Encryption.Limitations"></a>

The following limitations exist for Amazon Aurora encrypted DB clusters:
+ You can't turn off encryption on an encrypted DB cluster.
+ If you have an existing unencrypted cluster, all snapshots created from that cluster will also be unencrypted. To create an encrypted snapshot from an unencrypted cluster, you must copy the snapshot and specify a customer managed key during the copy operation. You cannot create an encrypted snapshot from an unencrypted snapshot without specifying a customer managed key.
+ You can't create an encrypted snapshot of an unencrypted DB .
+ A snapshot of an encrypted DB cluster must be encrypted using the same KMS key as the DB cluster.
+ You can't convert an unencrypted DB cluster to an encrypted one. However, you can restore an unencrypted snapshot to an encrypted Aurora DB cluster. To do this, specify a KMS key when you restore from the unencrypted snapshot.
+ If you have an existing unencrypted cluster, any Amazon Aurora replica (read instance) created from that cluster will also be unencrypted. To create an encrypted cluster from an unencrypted cluster, you need to restore the database cluster. The restored cluster will be encrypted by default after the restore operation.
+ To copy an encrypted snapshot from one AWS Region to another, you must specify the KMS key in the destination AWS Region. This is because KMS keys are specific to the AWS Region that they are created in.

  The source snapshot remains encrypted throughout the copy process. Amazon Aurora uses envelope encryption to protect data during the copy process. For more information about envelope encryption, see [ Envelope encryption](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#enveloping) in the *AWS Key Management Service Developer Guide*.
+ You can't unencrypt an encrypted DB cluster. However, you can export data from an encrypted DB cluster and import the data into an unencrypted DB cluster.