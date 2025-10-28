# Multi-Region keys in AWS KMS

AWS KMS supports _multi-Region keys_, which are AWS KMS keys in
different AWS Regions that can be used interchangeably – as though you had the same key in
multiple Regions. Each set of _related_ multi-Region keys
has the same key material and [key ID](concepts.md#key-id-key-id "concepts.md#key-id-key-id"), so you can
encrypt data in one AWS Region and decrypt it in a different AWS Region without
re-encrypting or making a cross-Region call to AWS KMS.

Like all KMS keys, multi-Region keys never leave AWS KMS unencrypted. You can create
symmetric or asymmetric multi-Region keys for encryption or signing, create HMAC
multi-Region keys for generating and verifying HMAC tags, and create multi-Region keys with
[imported key material](importing-keys.md "importing-keys.md") or key material that AWS KMS
generates. You must manage each multi-Region key independently, including creating aliases
and tags, setting their key policies and grants, and enabling and disabling them
selectively. You can use multi-Region keys in all cryptographic operations that you can do
with single-Region keys.

Multi-Region keys are a flexible and powerful solution for many common data security
scenarios.

**Disaster recovery**

In a backup and recovery architecture, multi-Region keys let you process
encrypted data without interruption even in the event of an AWS Region outage.
Data maintained in backup Regions can be decrypted in the backup Region, and
data newly encrypted in the backup Region can be decrypted in the primary Region
when that Region is restored.

**Global data management**

Businesses that operate globally need globally distributed data that is
available consistently across AWS Regions. You can create multi-Region keys in
all Regions where your data resides, then use the keys as though they were a
single-Region key without the latency of a cross-Region call or the cost of
re-encrypting data under a different key in each Region.

**Distributed signing applications**

Applications that require cross-Region signature capabilities can use
multi-Region asymmetric signing keys to generate identical digital signatures
consistently and repeatedly in different AWS Regions.

If you use certificate chaining with a single global trust store (for a single
root certificate authority (CA), and Regional intermediate CAs signed by the
root CA, you don't need multi-Region keys. However, if your system doesn't
support intermediate CAs, such as application signing, you can use multi-Region
keys to bring consistency to Regional certifications.

**Active-active applications that span multiple Regions**

Some workloads and applications can span multiple Regions in active-active
architectures. For these applications, multi-Region keys can reduce complexity
by providing the same key material for concurrent encrypt and decrypt operations
on data that might be moving across Region boundaries.

You can use multi-Region keys with client-side encryption libraries, such as the [AWS Encryption SDK](../../../encryption-sdk/latest/developer-guide.md "../../../encryption-sdk/latest/developer-guide.md"), the [AWS
Database Encryption SDK](../../../dynamodb-encryption-client/latest/devguide.md "../../../dynamodb-encryption-client/latest/devguide.md"), and [Amazon S3
client-side encryption](../../../AmazonS3/latest/userguide/UsingClientSideEncryption.md "../../../AmazonS3/latest/userguide/UsingClientSideEncryption.md").

[AWS services that integrate with
AWS KMS](https://aws.amazon.com/kms/features/ "https://aws.amazon.com/kms/features/") for encryption at rest or digital signatures currently treat multi-Region
keys as though they were single-Region keys. They might re-wrap or re-encrypt data moved
between Regions. For example, Amazon S3 cross-region replication decrypts and re-encrypts data
under a KMS key in the destination Region, even when replicating objects protected by a
multi-Region key.

Multi-Region keys are not global. You create a multi-Region primary key and then replicate
it into Regions that you select within an [AWS partition](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md"). Then you manage
the multi-Region key in each Region independently. Neither AWS nor AWS KMS ever
automatically creates or replicates multi-Region keys into any Region on your behalf. [AWS managed keys](concepts.md#aws-managed-key "concepts.md#aws-managed-key"), the KMS keys that AWS services
create in your account for you, are always single-Region keys.

In China Regions, you can use the multi-Region key feature to replicate
KMS keys within the China Regions partition (`aws-cn`). For example, you can replicate a key from
the China (Beijing) Region to the China (Ningxia) Region, or the reverse. By replicating a key from
one China region to another, you agree to use the AWS Key Management Service of the destination region and comply with
all applicable terms of agreement for the destination region. You cannot replicate a key from the
Beijing and Ningxia Regions into an AWS Region outside of the China Regions partition. Similarly, you
cannot replicate a key from a region outside of the China Regions partition into the
Beijing and Ningxia Regions.

You cannot convert an existing single-Region key to a multi-Region key. This design
ensures that all data protected with existing single-Region keys maintain the same data
residency and data sovereignty properties.

For most data security needs, the Regional isolation and fault tolerance of Regional
resources make standard AWS KMS single-Region keys a best-fit solution. However, when you need
to encrypt or sign data in client-side applications across multiple Regions, multi-Region
keys might be the solution.

**Regions**

Multi-Region keys are supported in all AWS Regions that AWS KMS
supports.

**Pricing and quotas**

Every key in a set of related multi-Region keys counts as one KMS key for pricing and
quotas. [AWS KMS quotas](limits.md "limits.md") are calculated separately for each Region
of an account. Use and management of the multi-Region keys in each Region count toward the
quotas for that Region.

**Supported KMS key types**

You can create the following types of multi-Region KMS keys:

- Symmetric encryption KMS keys
- Asymmetric KMS keys
- HMAC KMS keys
- KMS keys with imported key material
  You cannot create multi-Region keys in a custom key store.

**Learn more**

- To learn how to control access to multi-Region KMS keys, see [Control access to multi-Region keys](multi-region-keys-auth.md "multi-region-keys-auth.md").
- To create multi-Region primary KMS keys of any type, see [Create multi-Region primary keys](create-primary-keys.md "create-primary-keys.md").
- To create multi-Region replica KMS keys, see [Create multi-Region replica keys](multi-region-keys-replicate.md "multi-region-keys-replicate.md").
- To update the primary Region, see [Change the primary key in a set of multi-Region
  keys](multi-region-update.md "multi-region-update.md").
- To identify and view multi-Region KMS keys, see [Identify HMAC KMS keys](identify-key-types.md#hmac-view "identify-key-types.md#hmac-view").
- To learn about special considerations for deleting multi-Region KMS keys, see
  [Deleting multi-Region keys](deleting-keys.md#deleting-mrks "deleting-keys.md#deleting-mrks").

## Terminology and concepts

The following terms and concepts are used with multi-Region keys.

### Multi-Region key

A _multi-Region key_ is one of a set of
KMS keys with the same key ID and key material (and other [shared properties](#mrk-replica-key "#mrk-replica-key")) in different AWS Regions.
Each multi-Region key is a fully functioning KMS key that can be used entirely
independently of its related multi-Region keys. Because all _related_ multi-Region keys have the same key ID and key material,
they are _interoperable_, that is, any related
multi-Region key in any AWS Region can decrypt ciphertext encrypted by any other
related multi-Region key.

You set the multi-Region property of a KMS key when you create it. You cannot
change the multi-Region property on an existing key. You cannot convert a
single-Region key to multi-Region key or a convert a multi-Region key to a
single-Region key. To move existing workloads into multi-Region scenarios, you must
re-encrypt your data or create new signatures with new multi-Region keys.

A multi-Region key can be [symmetric or
asymmetric](symmetric-asymmetric.md "symmetric-asymmetric.md") and it can use AWS KMS key material or [imported key material](importing-keys.md "importing-keys.md"). You cannot create
multi-Region keys in a [custom key
store](key-store-overview.md#custom-key-store-overview "key-store-overview.md#custom-key-store-overview").

In a set of related multi-Region keys, there is exactly one [primary key](#mrk-primary-key "#mrk-primary-key") at any time. You can create [replica keys](#mrk-replica-key "#mrk-replica-key") of that primary key in other
AWS Regions. You can also [update the
primary region](multi-region-update.md#update-primary-console "multi-region-update.md#update-primary-console"), which changes the primary key to a replica key and
changes a specified replica key to the primary key. However, you can maintain only
one primary key or replica key in each AWS Region. All of the Regions must be in
the same [AWS
partition](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

You can have multiple sets of related multi-Region keys in the same or different
AWS Regions. Although related multi-Region keys are interoperable, unrelated
multi-Region keys are not interoperable.

### Primary key

A multi-Region _primary key_ is a KMS key that
can be replicated into other AWS Regions in the same partition. Each set of
multi-Region keys has just one primary key.

A primary key differs from a replica key in the following ways:

- Only a primary key can be [replicated](multi-region-keys-replicate.md "multi-region-keys-replicate.md").
- The primary key is the source for [shared
  properties](#mrk-replica-key "#mrk-replica-key") of its [replica
  keys](#mrk-replica-key "#mrk-replica-key"), including the key material and key ID.
- You can enable and disable [automatic key
  rotation](rotate-keys.md "rotate-keys.md") only on a primary key.
- You can [schedule the deletion of a primary
  key](deleting-keys.md#deleting-mrks "deleting-keys.md#deleting-mrks") at any time. But AWS KMS will not delete a primary key until
  all of its replica keys are deleted.

However, primary and replica keys don't differ in any cryptographic properties.
You can use a primary key and its replica keys interchangeably.

You are not required to replicate a primary key. You can use it just as you would
any KMS key and replicate it if and when it is useful. However, because
multi-Region keys have different security properties than single-Region keys, we
recommend that you create a multi-Region key only when you plan to replicate
it.

### Replica key

A multi-Region _replica key_ is a KMS key that
has the same [key ID](concepts.md#key-id-key-id "concepts.md#key-id-key-id") and key material as its
[primary key](#mrk-primary-key "#mrk-primary-key") and related replica keys, but
exists in a different AWS Region.

A replica key is a fully functional KMS key with it own key policy, grants,
alias, tags, and other properties. It is not a copy of or pointer to the primary key
or any other key. You can use a replica key even if its primary key and all related
replica keys are disabled. You can also convert a replica key to a primary key and a
primary key to a replica key. Once it is created, a replica key relies on its
primary key only for [key rotation](rotate-keys.md#multi-region-rotate "rotate-keys.md#multi-region-rotate") and
[updating the primary Region](multi-region-update.md "multi-region-update.md").

Primary and replica keys don't differ in any cryptographic properties. You can use
a primary key and its replica keys interchangeably. Data encrypted by a primary or
replica key can be decrypted by the same key, or by any related primary or replica
key.

### Replicate

You can _replicate_ a multi-Region [primary key](#mrk-primary-key "#mrk-primary-key") into a different AWS Region in
the same partition. When you do, AWS KMS creates a multi-Region [replica key](#mrk-replica-key "#mrk-replica-key") in the specified Region with the
same [key ID](concepts.md#key-id-key-id "concepts.md#key-id-key-id") and other [shared properties](#mrk-sync-properties "#mrk-sync-properties") as its primary key. Then
it securely transports the key material across the Region boundary and associates it
with the new replica key, all within AWS KMS.

### Shared properties

_Shared properties_ are properties of a
multi-Region primary key that are shared with its replica keys. AWS KMS creates the
replica keys with the same shared property values as those of the primary key. Then,
it periodically synchronizes the shared property values of the primary key to its
replica keys. You cannot set these properties on a replica key.

The following are the shared properties of multi-Region keys.

- [Key ID](concepts.md#key-id-key-id "concepts.md#key-id-key-id") — (The
  `Region` element of the [key
  ARN](concepts.md#key-id-key-ARN "concepts.md#key-id-key-ARN") differs.)
- [Key material](create-keys.md#key-origin "create-keys.md#key-origin")
- [Key material origin](create-keys.md#key-origin "create-keys.md#key-origin")
- [Key spec](create-keys.md#key-spec "create-keys.md#key-spec") and encryption algorithms
- [Key usage](create-keys.md#key-usage "create-keys.md#key-usage")
- [Automatic key rotation](rotating-keys-enable.md "rotating-keys-enable.md")
  — You can enable and disable automatic key rotation only on the
  primary key. New replica keys are created with all versions of the shared
  key material. For details, see [Rotating multi-Region keys](rotate-keys.md#multi-region-rotate "rotate-keys.md#multi-region-rotate").
- [On-demand rotation](rotating-keys-on-demand.md "rotating-keys-on-demand.md") —
  You can perform on-demand rotation only on the primary key. New replica keys
  are created with all versions of the shared key material. For details, see
  [Rotating multi-Region keys](rotate-keys.md#multi-region-rotate "rotate-keys.md#multi-region-rotate").

You can also think of the primary and replica designations of related multi-Region
keys as shared properties. When you [create new
replica keys](#mrk-replica-key "#mrk-replica-key") or [update the primary
key](multi-region-update.md#update-primary-console "multi-region-update.md#update-primary-console"), AWS KMS synchronizes the change to all related multi-Region keys. When
these changes are complete, all related multi-Region keys list their primary key and
replica keys accurately.

All other properties of multi-Region keys are _independent
properties_, including the description, [key policy](key-policies.md "key-policies.md"), [grants](grants.md "grants.md"), [enabled and disabled key states](enabling-keys.md "enabling-keys.md"), [aliases](kms-alias.md "kms-alias.md"), and [tags](tagging-keys.md "tagging-keys.md"). You can set the same values for these properties on all related
multi-Region keys, but if you change the value of an independent property, AWS KMS
does not synchronize it.

You can track the synchronization of the shared properties of your multi-Region
keys. In your AWS CloudTrail log, look for the [SynchronizeMultiRegionKey](ct-synchronize-multi-region-key.md "ct-synchronize-multi-region-key.md")
event.
