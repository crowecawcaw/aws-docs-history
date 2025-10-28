# How Amazon Redshift uses AWS KMS

This topic discusses how Amazon Redshift uses AWS KMS to encrypt data.

###### Topics

- [Amazon Redshift encryption](#rs-encryption "#rs-encryption")
- [Encryption context](#rs-encryptioncontext "#rs-encryptioncontext")

## Amazon Redshift encryption

An Amazon Redshift data warehouse is a collection of computing resources called nodes, which are
organized into a group called a cluster. Each cluster runs an Amazon Redshift engine and contains
one or more databases.

Amazon Redshift uses a four-tier, key-based architecture for encryption. The architecture
consists of data encryption keys, a database key, a cluster key, and a root key. You can
use an AWS KMS key as the root key.

Data encryption keys encrypt data blocks in the cluster. Each data block is assigned a
randomly-generated AES-256 key. These keys are encrypted by using the database key for the
cluster.

The database key encrypts data encryption keys in the cluster. The database key is a
randomly-generated AES-256 key. It is stored on disk in a separate network from the Amazon Redshift
cluster and passed to the cluster across a secure channel.

The cluster key encrypts the database key for the Amazon Redshift cluster. You can use
AWS KMS, AWS CloudHSM, or an external hardware security module (HSM) to manage the cluster
key. See the
[Amazon Redshift Database Encryption](../../../redshift/latest/mgmt/working-with-db-encryption.md "../../../redshift/latest/mgmt/working-with-db-encryption.md") documentation for more details.

You can request encryption by checking the appropriate box in the Amazon Redshift console. You
can specify a [customer managed key](concepts.md#customer-mgn-key "concepts.md#customer-mgn-key") by choosing
one from the list that appears below the encryption box. If you do not specify a
customer managed key, Amazon Redshift uses the [AWS managed key](concepts.md#aws-managed-key "concepts.md#aws-managed-key") for Amazon Redshift under your account.

###### Important

Amazon Redshift supports only symmetric encryption KMS keys. You cannot use an asymmetric KMS key in an Amazon Redshift encryption workflow. For help determining whether a KMS key is symmetric or asymmetric, see [Identify different key types](identify-key-types.md "identify-key-types.md").

## Encryption context

Each service that is integrated with AWS KMS specifies an [encryption context](encrypt_context.md "encrypt_context.md") when requesting data keys,
encrypting, and decrypting. The encryption context is additional authenticated
data (AAD) that AWS KMS uses to check for data integrity. That is, when an
encryption context is specified for an encryption operation, the service also specifies
it for the decryption operation or decryption will not succeed. Amazon Redshift uses the cluster ID
and the creation time for the encryption context. In the `requestParameters`
field of a CloudTrail log file, the encryption context will look similar to this.

```

"encryptionContext": {
    "aws:redshift:arn": "arn:aws:redshift:`region`:`account_ID`:cluster:`cluster_name`",
    "aws:redshift:createtime": "20150206T1832Z"
},

```

You can search on the cluster name in your CloudTrail logs to understand what operations were
performed by using an AWS KMS key (KMS key). The operations include cluster encryption,
cluster decryption, and generating data keys.
