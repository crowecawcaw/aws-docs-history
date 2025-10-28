# How Amazon EMR uses AWS KMS

When you use an [Amazon EMR](https://aws.amazon.com/emr/ "https://aws.amazon.com/emr/") cluster, you can configure
the cluster to encrypt data _at rest_ before saving it to a persistent
storage location. You can encrypt data at rest on the EMR File System (EMRFS), on the storage
volumes of cluster nodes, or both. To encrypt data at rest, you can use an AWS KMS key. The
following topics explain how an Amazon EMR cluster uses a KMS key to encrypt data at rest.

###### Important

Amazon EMR supports only [symmetric KMS keys](symm-asymm-choose-key-spec.md#symmetric-cmks "symm-asymm-choose-key-spec.md#symmetric-cmks"). You cannot use
an [asymmetric KMS key](symmetric-asymmetric.md "symmetric-asymmetric.md") to encrypt data at rest in an Amazon EMR
cluster. For help determining whether a KMS key is symmetric or asymmetric, see [Identify different key types](identify-key-types.md "identify-key-types.md").

Amazon EMR clusters also encrypt data _in transit_, which means the cluster
encrypts data before sending it through the network. You cannot use a KMS key to encrypt data in
transit. For more information, see [In-Transit Data Encryption](../../../emr/latest/ManagementGuide/emr-data-encryption-options.md#emr-encryption-intransit "../../../emr/latest/ManagementGuide/emr-data-encryption-options.md#emr-encryption-intransit") in the _Amazon EMR Management Guide_.

For more information about all the encryption options available in Amazon EMR, see [Encryption Options](../../../emr/latest/ManagementGuide/emr-data-encryption-options.md "../../../emr/latest/ManagementGuide/emr-data-encryption-options.md") in the
_Amazon EMR Management Guide_.

###### Topics

- [Encrypting data on the EMR file system (EMRFS)](#emrfs-encryption "#emrfs-encryption")
- [Encrypting data on the storage volumes of cluster
  nodes](#emr-local-disk-encryption "#emr-local-disk-encryption")
- [Encryption context](#emr-encryption-context "#emr-encryption-context")

## Encrypting data on the EMR file system (EMRFS)

Amazon EMR clusters use two distributed files systems:

- The Hadoop Distributed File System (HDFS). HDFS encryption does not use a KMS key in
  AWS KMS.
- The EMR File System (EMRFS). EMRFS is an implementation of HDFS that allows Amazon EMR
  clusters to store data in Amazon Simple Storage Service (Amazon S3). EMRFS supports four encryption options, two of
  which use a KMS key in AWS KMS. For more information about all four of the EMRFS encryption
  options, see [Encryption
  Options](../../../emr/latest/ManagementGuide/emr-data-encryption-options.md "../../../emr/latest/ManagementGuide/emr-data-encryption-options.md")
  in the _Amazon EMR Management Guide_.

The two EMRFS encryption options that use a KMS key use the following encryption features
offered by Amazon S3:

- [Protecting data using server-side encryption
  with AWS Key Management Service (SSE-KMS)](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md"). The Amazon EMR cluster sends data to Amazon S3. Amazon S3 uses a
  KMS key to encrypt the data before saving it to an S3 bucket. For more information about
  how this works, see [Process for encrypting data on EMRFS with
  SSE-KMS](#emrfs-encryption-sse-kms "#emrfs-encryption-sse-kms").
- [Protecting data using client-side
  encryption](../../../AmazonS3/latest/userguide/UsingClientSideEncryption.md "../../../AmazonS3/latest/userguide/UsingClientSideEncryption.md") (CSE-KMS). Data in an Amazon EMR is encrypted under an AWS KMS key
  before it's sent to Amazon S3 for storage. For more information about how this works, see [Process for encrypting data on EMRFS with
  CSE-KMS](#emrfs-encryption-cse-kms "#emrfs-encryption-cse-kms").

When you configure an Amazon EMR cluster to encrypt data on EMRFS with a KMS key, you choose
the KMS key that you want Amazon S3 or the Amazon EMR cluster to use. With SSE-KMS, you can choose the
AWS managed key for Amazon S3 with the alias **aws/s3**, or a
symmetric customer managed key that you create. With client-side encryption, you must choose a symmetric
customer managed key that you create. When you choose a customer managed key, you must ensure that your Amazon EMR
cluster has permission to use the KMS key. For more information, see [Using AWS KMS keys for
encryption](../../../emr/latest/ManagementGuide/emr-encryption-enable.md#emr-awskms-keys "../../../emr/latest/ManagementGuide/emr-encryption-enable.md#emr-awskms-keys") in the _Amazon EMR Management Guide_.

For both server-side and client-side encryption, the KMS key you choose is the root key
in an [envelope encryption](kms-cryptography.md#enveloping "kms-cryptography.md#enveloping") workflow. The data is encrypted
with a unique [data key](data-keys.md "data-keys.md") that is encrypted under the KMS key
in AWS KMS. The encrypted data and an encrypted copy of its data key are stored together as a
single encrypted object in an S3 bucket. For more information about how this works, see the
following topics.

###### Topics

- [Process for encrypting data on EMRFS with
  SSE-KMS](#emrfs-encryption-sse-kms "#emrfs-encryption-sse-kms")
- [Process for encrypting data on EMRFS with
  CSE-KMS](#emrfs-encryption-cse-kms "#emrfs-encryption-cse-kms")

### Process for encrypting data on EMRFS with

SSE-KMS

When you configure an Amazon EMR cluster to use SSE-KMS, the encryption process works like
this:

1. The cluster sends data to Amazon S3 for storage in an S3 bucket.
2. Amazon S3 sends a [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md") request to AWS KMS, specifying the key ID of the KMS key that you
   chose when you configured the cluster to use SSE-KMS. The request includes encryption
   context; for more information, see [Encryption context](#emr-encryption-context "#emr-encryption-context").
3. AWS KMS generates a unique data encryption key (data key) and then sends two copies of
   this data key to Amazon S3. One copy is unencrypted (plaintext), and the other copy is
   encrypted under the KMS key.
4. Amazon S3 uses the plaintext data key to encrypt the data that it received in step 1, and
   then removes the plaintext data key from memory as soon as possible after use.
5. Amazon S3 stores the encrypted data and the encrypted copy of the data key together as a
   single encrypted object in an S3 bucket.

The decryption process works like this:

1. The cluster requests an encrypted data object from an S3 bucket.
2. Amazon S3 extracts the encrypted data key from the S3 object, and then sends the
   encrypted data key to AWS KMS with a [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md") request. The request includes an [encryption context](encrypt_context.md "encrypt_context.md").
3. AWS KMS decrypts the encrypted data key using the same KMS key that was used to encrypt
   it, and then sends the decrypted (plaintext) data key to Amazon S3.
4. Amazon S3 uses the plaintext data key to decrypt the encrypted data, and then removes the
   plaintext data key from memory as soon as possible after use.
5. Amazon S3 sends the decrypted data to the cluster.

### Process for encrypting data on EMRFS with

CSE-KMS

When you configure an Amazon EMR cluster to use CSE-KMS, the encryption process works like
this:

1. When it's ready to store data in Amazon S3, the cluster sends a [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md") request to AWS KMS,
   specifying the key ID of the KMS key that you chose when you configured the cluster to use
   CSE-KMS. The request includes encryption context; for more information, see [Encryption context](#emr-encryption-context "#emr-encryption-context").
2. AWS KMS generates a unique data encryption key (data key) and then sends two copies of
   this data key to the cluster. One copy is unencrypted (plaintext), and the other copy is
   encrypted under the KMS key.
3. The cluster uses the plaintext data key to encrypt the data, and then removes the
   plaintext data key from memory as soon as possible after use.
4. The cluster combines the encrypted data and the encrypted copy of the data key
   together into a single encrypted object.
5. The cluster sends the encrypted object to Amazon S3 for storage.

The decryption process works like this:

1. The cluster requests the encrypted data object from an S3 bucket.
2. Amazon S3 sends the encrypted object to the cluster.
3. The cluster extracts the encrypted data key from the encrypted object, and then
   sends the encrypted data key to AWS KMS with a [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md") request. The request includes [encryption context](encrypt_context.md "encrypt_context.md").
4. AWS KMS decrypts the encrypted data key using the same KMS key that was used to encrypt
   it, and then sends the decrypted (plaintext) data key to the cluster.
5. The cluster uses the plaintext data key to decrypt the encrypted data, and then
   removes the plaintext data key from memory as soon as possible after use.

## Encrypting data on the storage volumes of cluster

nodes

An Amazon EMR cluster is a collection of Amazon Elastic Compute Cloud (Amazon EC2) instances. Each instance in the
cluster is called a _cluster node_ or _node_. Each node
can have two types of storage volumes: instance store volumes, and Amazon Elastic Block Store (Amazon EBS) volumes.
You can configure the cluster to use [Linux Unified Key Setup
(LUKS)](https://gitlab.com/cryptsetup/cryptsetup/blob/master/README.md "https://gitlab.com/cryptsetup/cryptsetup/blob/master/README.md") to encrypt both types of storage volumes on the nodes (but not the boot
volume of each node). This is called _local disk encryption_.

When you enable local disk encryption for a cluster, you can choose to encrypt the LUKS key with a KMS key in AWS KMS. You must choose a [customer managed key](concepts.md#customer-mgn-key "concepts.md#customer-mgn-key") that you create; you cannot use an [AWS managed key](concepts.md#aws-managed-key "concepts.md#aws-managed-key"). If you choose a customer managed key, you must ensure that your Amazon EMR
cluster has permission to use the KMS key. For more information, see [Using AWS KMS keys for encryption](../../../emr/latest/ManagementGuide/emr-encryption-enable.md#emr-awskms-keys "../../../emr/latest/ManagementGuide/emr-encryption-enable.md#emr-awskms-keys") in the _Amazon EMR Management Guide_.

When you enable local disk encryption using a KMS key, the encryption process works like
this:

1. When each cluster node launches, it sends a [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md") request to AWS KMS,
   specifying the key ID of the KMS key that you chose when you enabled local disk encryption for
   the cluster.
2. AWS KMS generates a unique data encryption key (data key) and then sends two copies of
   this data key to the node. One copy is unencrypted (plaintext), and the other copy is
   encrypted under the KMS key.
3. The node uses a base64-encoded version of the plaintext data key as the password that
   protects the LUKS key. The node saves the encrypted copy of the data key on its
   boot volume.
4. If the node reboots, the rebooted node sends the encrypted data key to AWS KMS with a
   [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md") request.
5. AWS KMS decrypts the encrypted data key using the same KMS key that was used to encrypt it,
   and then sends the decrypted (plaintext) data key to the node.
6. The node uses the base64-encoded version of the plaintext data key as the password to
   unlock the LUKS key.

## Encryption context

Each AWS service integrated with AWS KMS can specify an [encryption context](encrypt_context.md "encrypt_context.md") when the service uses AWS KMS to generate data keys or to encrypt
or decrypt data. Encryption context is additional authenticated information that AWS KMS uses to
check for data integrity. When a service specifies encryption context for an encryption
operation, it must specify the same encryption context for the corresponding decryption
operation or decryption will fail. Encryption context is also written to AWS CloudTrail log files,
which can help you understand why a specific KMS key was used.

The following section explain the encryption context that is used in each Amazon EMR encryption
scenario that uses a KMS key.

### Encryption context for EMRFS encryption with

SSE-KMS

With SSE-KMS, the Amazon EMR cluster sends data to Amazon S3, and then Amazon S3 uses a KMS key to encrypt
the data before saving it to an S3 bucket. In this case, Amazon S3 uses the Amazon Resource Name
(ARN) of the S3 object as encryption context with each [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md") and [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md") request that it sends to AWS KMS. The
following example shows a JSON representation of the encryption context that Amazon S3
uses.

```
{ "aws:s3:arn" : "arn:aws:s3:::`S3_bucket_name`/`S3_object_key`" }
```

### Encryption context for EMRFS encryption with

CSE-KMS

With CSE-KMS, the Amazon EMR cluster uses a KMS key to encrypt data before sending it to Amazon S3 for
storage. In this case, the cluster uses the Amazon Resource Name (ARN) of the KMS key as
encryption context with each [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md") and [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md")
request that it sends to AWS KMS. The following example shows a JSON representation of the
encryption context that the cluster uses.

```
{ "kms_cmk_id" : "`arn:aws:kms:us-east-2:111122223333:key/0987ab65-43cd-21ef-09ab-87654321cdef`" }
```

### Encryption context for local disk encryption

with LUKS

When an Amazon EMR cluster uses local disk encryption with LUKS, the cluster nodes do not
specify encryption context with the [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md") and [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md")
requests that they send to AWS KMS.
