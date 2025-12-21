# Replicating encrypted objects (SSE-S3,

SSE-KMS, DSSE-KMS, SSE-C)

###### Important

Amazon S3 now applies server-side encryption with Amazon S3 managed keys (SSE-S3) as the base level of encryption for every bucket in Amazon S3. Starting January 5, 2023, all new object uploads to Amazon S3 are automatically encrypted at no additional cost and with no impact on performance. The automatic encryption status for S3 bucket default encryption configuration and for new object uploads is available in CloudTrail logs, S3 Inventory, S3 Storage Lens, the Amazon S3 console, and as an additional Amazon S3 API response header in the AWS CLI and AWS SDKs. For more information, see [Default encryption FAQ](default-encryption-faq.md "default-encryption-faq.md").

There are some special
considerations when you're replicating objects that have been encrypted by using server-side
encryption. Amazon S3 supports the following types of server-side encryption:

- Server-side encryption with Amazon S3 managed keys (SSE-S3)
- Server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS)
- Dual-layer server-side encryption with AWS KMS keys (DSSE-KMS)
- Server-side encryption with customer-provided keys (SSE-C)
  For more information about server-side encryption, see [Protecting data with server-side encryption](serv-side-encryption.md "serv-side-encryption.md").

This topic explains the permissions that you
need to direct Amazon S3 to replicate
objects that have been encrypted by using server-side encryption. This topic also provides additional configuration elements that you can add and
example AWS Identity and Access Management (IAM) policies that grant the necessary permissions for
replicating encrypted objects.

For an example with step-by-step instructions, see [Enabling replication for encrypted
objects](#replication-walkthrough-4 "#replication-walkthrough-4"). For
information about creating a replication configuration, see [Replicating objects within and across Regions](replication.md "replication.md").

###### Note

You can use multi-Region AWS KMS keys in Amazon S3. However, Amazon S3 currently treats multi-Region keys
as though they were single-Region keys, and does not use the multi-Region features of the key. For more
information, see
[Using multi-Region keys](../../../kms/latest/developerguide/multi-region-keys-overview.md "../../../kms/latest/developerguide/multi-region-keys-overview.md") in the _AWS Key Management Service Developer Guide_.

###### Topics

- [How default bucket encryption
  affects replication](#replication-default-encryption "#replication-default-encryption")
- [Replicating
  objects encrypted with SSE-C](#replicationSSEC "#replicationSSEC")
- [Replicating objects encrypted with SSE-S3, SSE-KMS, or
  DSSE-KMS](#replications "#replications")
- [Enabling replication for encrypted
  objects](#replication-walkthrough-4 "#replication-walkthrough-4")

## How default bucket encryption

affects replication

When you enable default encryption for a replication destination bucket, the following
encryption behavior applies:

- If objects in the source bucket are not encrypted, the replica objects in the
  destination bucket are encrypted by using the default encryption settings of the destination
  bucket. As a result, the entity tags (ETags) of the source objects differ from
  the ETags of the replica objects. If you have applications that use ETags, you must update
  those applications to account for this difference.
- If objects in the source bucket are encrypted by using server-side encryption with Amazon S3
  managed keys (SSE-S3), server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS), or dual-layer
  server-side encryption with AWS KMS keys (DSSE-KMS), the replica
  objects in the destination bucket use the same type of encryption as the source objects.
  The default encryption settings of the destination bucket are not used.

## Replicating

objects encrypted with SSE-C

By using server-side encryption with customer-provided keys (SSE-C), you can manage
your own proprietary encryption keys. With SSE-C, you manage the keys while Amazon S3 manages
the encryption and decryption process. You must provide an encryption key as part of
your request, but you don't need to write any code to perform object encryption or
decryption. When you upload an object, Amazon S3 encrypts the object by using the key that
you provided. Amazon S3 then purges that key from memory. When you retrieve an object, you
must provide the same encryption key as part of your request. For more information, see
[Using server-side encryption with
customer-provided keys (SSE-C)](ServerSideEncryptionCustomerKeys.md "ServerSideEncryptionCustomerKeys.md").

S3 Replication supports objects that are encrypted with SSE-C. You can configure
SSE-C object replication in the Amazon S3 console or with the AWS SDKs in the same way that
you configure replication for unencrypted objects. There aren't additional SSE-C
permissions beyond what are currently required for replication.

S3 Replication automatically replicates newly uploaded SSE-C encrypted objects if
they are eligible, as specified in your S3 Replication configuration. To replicate
existing objects in your buckets, use S3 Batch Replication. For more information about
replicating objects, see [Setting up live replication overview](replication-how-setup.md "replication-how-setup.md") and [Replicating existing objects with
Batch Replication](s3-batch-replication-batch.md "s3-batch-replication-batch.md").

There are no additional charges for replicating SSE-C objects. For details about
replication pricing, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

## Replicating objects encrypted with SSE-S3, SSE-KMS, or

DSSE-KMS

By default, Amazon S3 doesn't replicate objects that are encrypted with SSE-KMS or
DSSE-KMS. This section explains the additional configuration elements that you can add
to direct Amazon S3 to replicate these objects.

For an example with step-by-step instructions, see [Enabling replication for encrypted
objects](#replication-walkthrough-4 "#replication-walkthrough-4"). For
information about creating a replication configuration, see [Replicating objects within and across Regions](replication.md "replication.md").

### Specifying additional information in the

replication configuration

In the replication configuration, you do the following:

- In the `Destination`
  element in your replication configuration, add the ID of
  the symmetric AWS KMS customer managed key that you want Amazon S3 to use
  to encrypt object replicas,
  as shown in the following example replication configuration.
- Explicitly opt in by enabling replication of objects encrypted by using
  KMS keys (SSE-KMS or DSSE-KMS). To opt in, add the
  `SourceSelectionCriteria` element, as shown in the following
  example replication configuration.

```
<ReplicationConfiguration>
   <Rule>
      ...
      <SourceSelectionCriteria>
         <SseKmsEncryptedObjects>
           <Status>Enabled</Status>
         </SseKmsEncryptedObjects>
      </SourceSelectionCriteria>

      <Destination>
          ...
          <EncryptionConfiguration>
             <ReplicaKmsKeyID>`AWS KMS key ARN or Key Alias ARN that's in the same AWS Region as the destination bucket.`</ReplicaKmsKeyID>
          </EncryptionConfiguration>
       </Destination>
      ...
   </Rule>
</ReplicationConfiguration>
```

###### Important

- The KMS key must have been created in the same AWS Region as the
  destination bucket.
- The KMS key _must_ be valid. The
  `PutBucketReplication` API operation doesn't check the
  validity of KMS keys. If you use a KMS key that isn't valid, you
  will receive the HTTP `200 OK` status code in response, but
  replication fails.

The following example shows a replication configuration that includes optional
configuration elements. This replication configuration has one rule. The rule
applies to objects with the `Tax` key prefix.
Amazon S3 uses the specified AWS KMS key ID to encrypt these object replicas.

```
<?xml version="1.0" encoding="UTF-8"?>
<ReplicationConfiguration>
   <Role>arn:aws:iam::`account-id`:role/`role-name`</Role>
   <Rule>
      <ID>`Rule-1`</ID>
      <Priority>1</Priority>
      <Status>Enabled</Status>
      <DeleteMarkerReplication>
         <Status>Disabled</Status>
      </DeleteMarkerReplication>
      <Filter>
         <Prefix>Tax</Prefix>
      </Filter>
      <Destination>
         <Bucket>arn:aws:s3:::``amzn-s3-demo-destination-bucket``</Bucket>
         <EncryptionConfiguration>
            <ReplicaKmsKeyID>`AWS KMS key ARN or Key Alias ARN that's in the same AWS Region as the destination bucket.`</ReplicaKmsKeyID>
         </EncryptionConfiguration>
      </Destination>
      <SourceSelectionCriteria>
         <SseKmsEncryptedObjects>
            <Status>Enabled</Status>
         </SseKmsEncryptedObjects>
      </SourceSelectionCriteria>
   </Rule>
</ReplicationConfiguration>
```

### Granting additional permissions for the

IAM role

To replicate objects that are encrypted at rest by using SSE-S3, SSE-KMS, or DSSE-KMS, grant
the following additional permissions to the AWS Identity and Access Management (IAM) role that you specify
in the replication configuration. You grant these permissions by updating the
permissions policy that's associated with the IAM role.

- **`s3:GetObjectVersionForReplication` action
  for source objects** – This action allows Amazon S3 to
  replicate both unencrypted objects and objects created with server-side
  encryption by using SSE-S3, SSE-KMS, or DSSE-KMS.

###### Note

We recommend that you use the
`s3:GetObjectVersionForReplication` action instead of the
`s3:GetObjectVersion` action because
`s3:GetObjectVersionForReplication` provides Amazon S3 with
only the minimum permissions necessary for replication. In addition, the
`s3:GetObjectVersion` action allows replication of
unencrypted and SSE-S3-encrypted objects, but not of objects that are
encrypted by using KMS keys (SSE-KMS or DSSE-KMS).

- **`kms:Decrypt` and `kms:Encrypt`
  AWS KMS actions for the KMS keys**
  - You must grant `kms:Decrypt` permissions for the
    AWS KMS key that's used to decrypt the source object.
  - You must grant `kms:Encrypt` permissions for the
    AWS KMS key that's used to encrypt the object replica.

- **`kms:GenerateDataKey` action for
  replicating plaintext objects** – If you're replicating
  plaintext objects to a bucket with SSE-KMS or DSSE-KMS encryption enabled by
  default, you must include the `kms:GenerateDataKey` permission
  for the destination encryption context and the KMS key in the IAM
  policy.

We recommend that you restrict these permissions only to the destination
buckets and objects by using AWS KMS condition keys. The AWS account that owns the
IAM role must have permissions for the `kms:Encrypt` and
`kms:Decrypt` actions for the KMS keys that are listed in the
policy. If the KMS keys are owned by another AWS account, the owner of the
KMS keys must grant these permissions to the AWS account that owns the IAM
role. For more information about managing access to these KMS keys, see [Using IAM policies with AWS KMS](../../../kms/latest/developerguide/iam-policies.md "../../../kms/latest/developerguide/iam-policies.md") in
the _AWS Key Management Service Developer Guide_.

### S3 Bucket Keys and replication

To use replication with an S3 Bucket Key, the AWS KMS key policy for the
KMS key that's used to encrypt the object replica must include the
`kms:Decrypt` permission for the calling principal. The call to
`kms:Decrypt` verifies the integrity of the S3 Bucket Key before using
it. For more information, see [Using an S3 Bucket Key with replication](bucket-key.md#bucket-key-replication "bucket-key.md#bucket-key-replication").

When an S3 Bucket Key is enabled for the source or destination bucket, the
encryption context will be the bucket's Amazon Resource Name (ARN), not the object's
ARN (for example,
`arn:aws:s3:::`bucket_ARN``). You must
update your IAM policies to use the bucket ARN for the encryption context:

```
"kms:EncryptionContext:aws:s3:arn": [
"arn:aws:s3:::`bucket_ARN`"
]
```

For more information, see [Encryption context
(x-amz-server-side-encryption-context)](specifying-kms-encryption.md#s3-kms-encryption-context "specifying-kms-encryption.md#s3-kms-encryption-context") (in the "Using the REST API"
section) and [Changes to note before enabling an S3 Bucket Key](bucket-key.md#bucket-key-changes "bucket-key.md#bucket-key-changes").

### Example policies: Using SSE-S3 and

SSE-KMS with replication

The following example IAM policies show statements for using SSE-S3 and SSE-KMS
with replication.

###### Example – Using SSE-KMS with separate destination buckets

The following example policy shows statements for using SSE-KMS with separate
destination buckets.

###### Example – Replicating objects created with SSE-S3 and SSE-KMS

The following is a complete IAM policy that grants the necessary permissions
to replicate unencrypted objects, objects created with SSE-S3, and objects
created with SSE-KMS.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "s3:GetReplicationConfiguration",
 "s3:ListBucket"
 ],
 "Resource":[
 "arn:aws:s3:::`amzn-s3-demo-source-bucket`"
 ]
 },
 {
 "Effect":"Allow",
 "Action":[
 "s3:GetObjectVersionForReplication",
 "s3:GetObjectVersionAcl"
 ],
 "Resource":[
 "arn:aws:s3:::`amzn-s3-demo-source-bucket`/`key-prefix1`*"
 ]
 },
 {
 "Effect":"Allow",
 "Action":[
 "s3:ReplicateObject",
 "s3:ReplicateDelete"
 ],
 "Resource":"arn:aws:s3:::`amzn-s3-demo-destination-bucket`/`key-prefix1`*"
 },
 {
 "Action":[
 "kms:Decrypt"
 ],
 "Effect":"Allow",
 "Condition":{
 "StringLike":{
 "kms:ViaService":"s3.`us-east-1`.amazonaws.com",
 "kms:EncryptionContext:aws:s3:arn":[
 "arn:aws:s3:::`amzn-s3-demo-source-bucket`/`key-prefix1`*"
 ]
 }
 },
 "Resource":[
 "arn:aws:kms:`us-east-1`:`111122223333`:key/`key-id`"
 ]
 },
 {
 "Action":[
 "kms:Encrypt"
 ],
 "Effect":"Allow",
 "Condition":{
 "StringLike":{
 "kms:ViaService":"s3.`us-east-1`.amazonaws.com",
 "kms:EncryptionContext:aws:s3:arn":[
 "arn:aws:s3:::`amzn-s3-demo-destination-bucket`/`prefix1`*"
 ]
 }
 },
 "Resource":[
 "arn:aws:kms:`us-east-1`:`111122223333`:key/`key-id`"
 ]
 }
 ]
}`

```

###### Example – Replicating objects with S3 Bucket Keys

The following is a complete IAM policy that grants the necessary permissions
to replicate objects with S3 Bucket Keys.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "s3:GetReplicationConfiguration",
 "s3:ListBucket"
 ],
 "Resource":[
 "arn:aws:s3:::`amzn-s3-demo-source-bucket`"
 ]
 },
 {
 "Effect":"Allow",
 "Action":[
 "s3:GetObjectVersionForReplication",
 "s3:GetObjectVersionAcl"
 ],
 "Resource":[
 "arn:aws:s3:::`amzn-s3-demo-source-bucket`/`key-prefix1`*"
 ]
 },
 {
 "Effect":"Allow",
 "Action":[
 "s3:ReplicateObject",
 "s3:ReplicateDelete"
 ],
 "Resource":"arn:aws:s3:::`amzn-s3-demo-destination-bucket`/`key-prefix1`*"
 },
 {
 "Action":[
 "kms:Decrypt"
 ],
 "Effect":"Allow",
 "Condition":{
 "StringLike":{
 "kms:ViaService":"s3.us-east-1.amazonaws.com",
 "kms:EncryptionContext:aws:s3:arn":[
 "arn:aws:s3:::`amzn-s3-demo-source-bucket`"
 ]
 }
 },
 "Resource":[
 "arn:aws:kms:us-east-1:111122223333:key/`key-id`"
 ]
 },
 {
 "Action":[
 "kms:Encrypt"
 ],
 "Effect":"Allow",
 "Condition":{
 "StringLike":{
 "kms:ViaService":"s3.us-east-1.amazonaws.com",
 "kms:EncryptionContext:aws:s3:arn":[
 "arn:aws:s3:::`amzn-s3-demo-destination-bucket`"
 ]
 }
 },
 "Resource":[
 "arn:aws:kms:us-east-1:111122223333:key/`key-id`"
 ]
 }
 ]
}`

```

### Granting additional

permissions for cross-account scenarios

In a cross-account scenario, where the source and destination buckets are owned by
different AWS accounts, you can use a KMS key to encrypt object replicas.
However, the KMS key owner must grant the source bucket owner permission to use
the KMS key.

###### Note

If you need to replicate SSE-KMS data cross-account, then your replication
rule must specify a [customer managed key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") from AWS KMS for the destination account. [AWS managed keys](../../../kms/latest/developerguide/concepts.md#aws-managed-cmk "../../../kms/latest/developerguide/concepts.md#aws-managed-cmk") don't allow cross-account use, and therefore
can't be used to perform cross-account replication.

###### To grant the source bucket owner permission to use the KMS key (AWS KMS

console)

1. Sign in to the AWS Management Console and open the AWS KMS console at
   [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms").
2. To change the AWS Region, use the Region selector in the upper-right corner of the page.
3. To view the keys in your account that you create and manage, in the navigation
   pane choose **Customer managed keys**.
4. Choose the KMS key.
5. Under the **General configuration** section, choose the
   **Key policy** tab.
6. Scroll down to **Other AWS accounts**.
7. Choose **Add other AWS accounts**.

The **Other AWS accounts** dialog box appears. 8. In the dialog box, choose **Add another AWS account**.
For **arn:aws:iam::**, enter the source
bucket account ID. 9. Choose **Save changes**.

###### To grant the source bucket owner permission to use the KMS key

(AWS CLI)

- For information about the `put-key-policy` AWS Command Line Interface (AWS CLI)
  command, see [put-key-policy](../../../cli/latest/reference/kms/put-key-policy.md "../../../cli/latest/reference/kms/put-key-policy.md") in the _AWS CLI Command Reference_. For information about the
  underlying `PutKeyPolicy` API operation, see [PutKeyPolicy](../../../kms/latest/APIReference/API_PutKeyPolicy.md "../../../kms/latest/APIReference/API_PutKeyPolicy.md") in the [AWS Key Management Service API Reference](../../../kms/latest/APIReference.md "../../../kms/latest/APIReference.md").

### AWS KMS transaction quota

considerations

When you add many new objects with AWS KMS encryption after enabling Cross-Region
Replication (CRR), you might experience throttling (HTTP `503 Service
 Unavailable` errors). Throttling occurs when the number of AWS KMS
transactions per second exceeds the current quota. For more information, see [Quotas](../../../kms/latest/developerguide/limits.md "../../../kms/latest/developerguide/limits.md") in the _AWS Key Management Service Developer Guide_.

To request a quota increase, use Service Quotas. For more information, see [Requesting a
quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md"). If Service Quotas isn't supported in your Region, [open an AWS Support case](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

## Enabling replication for encrypted

objects

By default, Amazon S3 doesn't replicate objects that are encrypted by using server-side
encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS) or dual-layer server-side encryption with
AWS KMS keys (DSSE-KMS). To replicate objects encrypted with SSE-KMS or DSS-KMS, you must
modify the bucket replication configuration to tell Amazon S3 to replicate these objects. This
example explains how to use the Amazon S3 console and the AWS Command Line Interface (AWS CLI) to change the bucket
replication configuration to enable replicating encrypted objects.

###### Note

When an S3 Bucket Key is enabled for the source or destination bucket, the encryption
context will be the bucket's Amazon Resource Name (ARN), not the object's ARN. You must
update your IAM policies to use the bucket ARN for the encryption context. For more information, see
[S3 Bucket Keys and replication](#bk-replication "#bk-replication").

###### Note

You can use multi-Region AWS KMS keys in Amazon S3. However, Amazon S3 currently treats multi-Region keys
as though they were single-Region keys, and does not use the multi-Region features of the key. For more
information, see
[Using multi-Region keys](../../../kms/latest/developerguide/multi-region-keys-overview.md "../../../kms/latest/developerguide/multi-region-keys-overview.md") in the _AWS Key Management Service Developer Guide_.

For step-by-step instructions, see [Configuring replication for buckets in the same
account](replication-walkthrough1.md "replication-walkthrough1.md"). This topic provides instructions for
setting a replication configuration when the source and destination buckets are
owned by the same and different AWS accounts.

To replicate encrypted objects with the AWS CLI, you do the following:

- Create source and destination buckets and enable versioning on these
  buckets.
- Create an AWS Identity and Access Management (IAM) service role that gives Amazon S3 permission to
  replicate objects. The IAM role's permissions include the necessary
  permissions to replicate the encrypted objects.
- Add a replication configuration to the source bucket. The replication
  configuration provides information related to replicating objects that are
  encrypted by using KMS keys.
- Add encrypted objects to the source bucket.
- Test the setup to confirm that your encrypted objects are being replicated
  to the destination bucket.
  The following procedures walk you through this process.

###### To replicate server-side encrypted objects (AWS CLI)

To use the examples in this procedure, replace the `user
 input placeholders` with your own
information.

1. In this example, you create both the source
   (`amzn-s3-demo-source-bucket`)
   and destination
   (`amzn-s3-demo-destination-bucket`)
   buckets in the same AWS account. You also set a credentials profile for
   the AWS CLI. This example uses the profile name
   `acctA`.

For information about setting credential profiles and using named
profiles, see [Configuration and
credential file settings](../../../cli/latest/userguide/cli-configure-files.md "../../../cli/latest/userguide/cli-configure-files.md") in the _AWS Command Line Interface User Guide_. 2. Use the following commands to create the
`amzn-s3-demo-source-bucket` bucket and enable versioning on
it. The following example commands create the
`amzn-s3-demo-source-bucket` bucket in the US East (N. Virginia)
(`us-east-1`) Region.

```
aws s3api create-bucket \
--bucket `amzn-s3-demo-source-bucket` \
--region `us-east-1` \
--profile `acctA`
```

```
aws s3api put-bucket-versioning \
--bucket `amzn-s3-demo-source-bucket` \
--versioning-configuration Status=Enabled \
--profile `acctA`
```

3. Use the following commands to create the
   `amzn-s3-demo-destination-bucket` bucket and enable
   versioning on it. The following example commands create the
   `amzn-s3-demo-destination-bucket` bucket in the
   US West (Oregon) (`us-west-2`) Region.

###### Note

To set up a replication configuration when both
`amzn-s3-demo-source-bucket` and
`amzn-s3-demo-destination-bucket` buckets are in the same
AWS account, you use the same profile. This example uses
`acctA`. To configure
replication when the buckets are owned by different AWS accounts, you
specify different profiles for each.

```
aws s3api create-bucket \
--bucket `amzn-s3-demo-destination-bucket` \
--region `us-west-2` \
--create-bucket-configuration LocationConstraint=`us-west-2` \
--profile `acctA`
```

```
aws s3api put-bucket-versioning \
--bucket `amzn-s3-demo-destination-bucket` \
--versioning-configuration Status=Enabled \
--profile `acctA`
```

4. Next, you create an IAM service role. You will specify this role in the
   replication configuration that you add to the
   `amzn-s3-demo-source-bucket` bucket later. Amazon S3 assumes this
   role to replicate objects on your behalf. You create an IAM role in two
   steps:
   - Create a service role.
   - Attach a permissions policy to the role.
   1. To create an IAM service role, do the following:
      1. Copy the following trust policy and save it to a file
         called
         ``s3-role-trust-policy-kmsobj`.json`
         in the current directory on your local computer. This policy
         grants the Amazon S3 service principal permissions to assume the
         role so that Amazon S3 can perform tasks on your behalf.

      JSON

      ```
      `{
       "Version":"2012-10-17",
       "Statement":[
       {
       "Effect":"Allow",
       "Principal":{
       "Service":"s3.amazonaws.com"
       },
       "Action":"sts:AssumeRole"
       }
       ]
      }`

      ```

      2. Use the following command to create the role:

      ```
      `$` aws iam create-role \
      --role-name `replicationRolekmsobj` \
      --assume-role-policy-document file://`s3-role-trust-policy-kmsobj`.json  \
      --profile `acctA`
      ```

   2. Next, you attach a permissions policy to the role. This policy
      grants permissions for various Amazon S3 bucket and object actions.
      1. Copy the following permissions policy and save it to a
         file named
         ``s3-role-permissions-policykmsobj`.json`
         in the current directory on your local computer. You will
         create an IAM role and attach the policy to it later.

      ###### Important

      In the permissions policy, you specify the AWS KMS key
      IDs that will be used for encryption of the
      `amzn-s3-demo-source-bucket` and
      `amzn-s3-demo-destination-bucket`
      buckets. You must create two separate KMS keys for the
      `amzn-s3-demo-source-bucket` and
      `amzn-s3-demo-destination-bucket`
      buckets. AWS KMS keys aren't shared outside the
      AWS Region in which they were created.

      JSON

      ```
      `{
       "Version":"2012-10-17",
       "Statement":[
       {
       "Action":[
       "s3:ListBucket",
       "s3:GetReplicationConfiguration",
       "s3:GetObjectVersionForReplication",
       "s3:GetObjectVersionAcl",
       "s3:GetObjectVersionTagging"
       ],
       "Effect":"Allow",
       "Resource":[
       "arn:aws:s3:::`amzn-s3-demo-source-bucket`",
       "arn:aws:s3:::`amzn-s3-demo-source-bucket`/*"
       ]
       },
       {
       "Action":[
       "s3:ReplicateObject",
       "s3:ReplicateDelete",
       "s3:ReplicateTags"
       ],
       "Effect":"Allow",
       "Condition":{
       "StringLikeIfExists":{
       "s3:x-amz-server-side-encryption":[
       "aws:kms",
       "AES256",
       "aws:kms:dsse"
       ],
       "s3:x-amz-server-side-encryption-aws-kms-key-id":[
       "`AWS KMS key IDs(in ARN format) to use for encrypting object replicas`"
       ]
       }
       },
       "Resource":"arn:aws:s3:::`amzn-s3-demo-destination-bucket`/*"
       },
       {
       "Action":[
       "kms:Decrypt"
       ],
       "Effect":"Allow",
       "Condition":{
       "StringLike":{
       "kms:ViaService":"s3.`us-east-1`.amazonaws.com",
       "kms:EncryptionContext:aws:s3:arn":[
       "arn:aws:s3:::`amzn-s3-demo-source-bucket`/*"
       ]
       }
       },
       "Resource":[
       "arn:aws:kms:`us-east-1`:`111122223333`:key/`key-id`"
       ]
       },
       {
       "Action":[
       "kms:Encrypt"
       ],
       "Effect":"Allow",
       "Condition":{
       "StringLike":{
       "kms:ViaService":"s3.`us-west-2`.amazonaws.com",
       "kms:EncryptionContext:aws:s3:arn":[
       "arn:aws:s3:::`amzn-s3-demo-destination-bucket`/*"
       ]
       }
       },
       "Resource":[
       "arn:aws:kms:`us-west-2`:`111122223333`:key/`key-id`"
       ]
       }
       ]
      }`

      ```

      2. Create a policy and attach it to the role.

      ```
      `$` aws iam put-role-policy \
      --role-name `replicationRolekmsobj` \
      --policy-document file://`s3-role-permissions-policykmsobj`.json \
      --policy-name `replicationRolechangeownerPolicy` \
      --profile `acctA`
      ```

5. Next, add the following replication configuration to the
   `amzn-s3-demo-source-bucket`
   bucket. It tells Amazon S3 to replicate objects with the
   `Tax/` prefix to the
   `amzn-s3-demo-destination-bucket`
   bucket.

###### Important

In the replication configuration, you specify the IAM role that Amazon S3
can assume. You can do this only if you have the
`iam:PassRole` permission. The profile that you specify
in the CLI command must have this permission. For more information, see
[Granting a
user permissions to pass a role to an AWS service](../../../IAM/latest/UserGuide/id_roles_use_passrole.md "../../../IAM/latest/UserGuide/id_roles_use_passrole.md") in the
_IAM User Guide_.

```
 <ReplicationConfiguration>
  <Role>`IAM-Role-ARN`</Role>
  <Rule>
    <Priority>1</Priority>
    <DeleteMarkerReplication>
       <Status>Disabled</Status>
    </DeleteMarkerReplication>
    <Filter>
       <Prefix>Tax</Prefix>
    </Filter>
    <Status>Enabled</Status>
    <SourceSelectionCriteria>
      <SseKmsEncryptedObjects>
        <Status>Enabled</Status>
      </SseKmsEncryptedObjects>
    </SourceSelectionCriteria>
    <Destination>
      <Bucket>arn:aws:s3:::``amzn-s3-demo-destination-bucket``</Bucket>
      <EncryptionConfiguration>
        <ReplicaKmsKeyID>`AWS KMS key IDs to use for encrypting object replicas`</ReplicaKmsKeyID>
      </EncryptionConfiguration>
    </Destination>
  </Rule>
</ReplicationConfiguration>
```

To add a replication configuration to the
`amzn-s3-demo-source-bucket`
bucket, do the following:

    1. The AWS CLI requires you to specify the replication configuration as
     JSON. Save the following JSON in a file
     (``replication`.json`)
     in the current directory on your local computer.



    ```
    {
       "Role":"`IAM-Role-ARN`",
       "Rules":[
          {
             "Status":"Enabled",
             "Priority":1,
             "DeleteMarkerReplication":{
                "Status":"Disabled"
             },
             "Filter":{
                "Prefix":"`Tax`"
             },
             "Destination":{
                "Bucket":"arn:aws:s3:::``amzn-s3-demo-destination-bucket``",
                "EncryptionConfiguration":{
                   "ReplicaKmsKeyID":"`AWS KMS key IDs (in ARN format) to use for encrypting object replicas`"
                }
             },
             "SourceSelectionCriteria":{
                "SseKmsEncryptedObjects":{
                   "Status":"Enabled"
                }
             }
          }
       ]
    }
    ```
    2. Edit the JSON to provide values for the
     ```amzn-s3-demo-destination-bucket```
     bucket, ``AWS KMS key IDs (in ARN
     format)``, and
     ``IAM-role-ARN``. Save
     the changes.
    3. Use the following command to add the replication configuration to
     your
     ```amzn-s3-demo-source-bucket```
     bucket. Be sure to provide the
     ```amzn-s3-demo-source-bucket```
     bucket name.



    ```
    `$` aws s3api put-bucket-replication \
    --replication-configuration file://`replication`.json \
    --bucket ``amzn-s3-demo-source-bucket`` \
    --profile `acctA`
    ```

6.  Test the configuration to verify that encrypted objects are replicated. In
    the Amazon S3 console, do the following:

        1. Sign in to the AWS Management Console and open the Amazon S3 console at
         [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
        2. In the
         ```amzn-s3-demo-source-bucket```
         bucket, create a folder named
         ``Tax``.
        3. Add sample objects to the folder. Be sure to choose the encryption
         option and specify your KMS key to encrypt the objects.
        4. Verify that the
         ```amzn-s3-demo-destination-bucket```
         bucket contains the object replicas and that they are encrypted by
         using the KMS key that you specified in the configuration. For
         more information, see [Getting replication status information](replication-status.md "replication-status.md").

    For a code example that shows how to add a replication configuration, see [Using the AWS SDKs](replication-walkthrough1.md#replication-ex1-sdk "replication-walkthrough1.md#replication-ex1-sdk"). You must
    modify the replication configuration appropriately.
