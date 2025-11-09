# Permissions for data access using Amazon S3 URIs

You can access sequence store data using HealthOmics API operations or Amazon S3 API operations.

For HealthOmics API access, HealthOmics permissions are managed through an IAM policy. However, S3 Access requires two
levels of configuration: explicit allow in the Store’s S3 Access Policy and an IAM policy. To learn more about
using IAM policies with HealthOmics, see [Service roles for HealthOmics](permissions-service.md "permissions-service.md").

There are three ways to share the capability of reading objects using the Amazon S3 APIs:

1. Policy based sharing – This sharing requires enabling the IAM principal both in the S3 Access policy
   and writing an IAM policy and attaching it to the IAM principal. See the next topic for more details.
2. Presigned URLs – You can also generate a shareable pre-signed URL for a file in the sequence store.
   To learn more about creating presigned URLs using Amazon S3, see [Using presigned
   URLs](../../../AmazonS3/latest/userguide/using-presigned-url.md "../../../AmazonS3/latest/userguide/using-presigned-url.md") in the Amazon S3 documentation. The sequence store S3 access policy supports statements for [limiting presigned URL capabilities](../../../AmazonS3/latest/userguide/using-presigned-url.md#PresignedUrlUploadObject-LimitCapabilities "../../../AmazonS3/latest/userguide/using-presigned-url.md#PresignedUrlUploadObject-LimitCapabilities").
3. Assumed roles – Create a role within the data owner's account that has an access policy that allows
   users to assume that role.

###### Topics

- [Policy based sharing](#policy-based-sharing "#policy-based-sharing")
- [Example Restriction](#example-restriction "#example-restriction")

## Policy based sharing

If you access sequence store data using a direct S3 URI, HealthOmics provides enhanced security measures for
the associated S3 bucket access policy.

The following rules apply to new S3 access policies. For existing policies, the rules apply when you next
update the policy:

- The S3 access policies support the following [policy elements](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md")
  - Version, Id, Statement, Sid, Effect, Principal, Action, Resource, Condition

- The S3 access policies support the following [condition keys](../../../service-authorization/latest/reference/list_amazons3.md#amazons3-policy-keys "../../../service-authorization/latest/reference/list_amazons3.md#amazons3-policy-keys"):
  - s3:ExistingObjectTag/<key>, s3:prefix, s3:signatureversion,
    s3:TlsVersion
  - Policies also support aws:PrincipalArn with the following condition operators: ArnEquals and ArnLike

If you try to add or update a policy to include an unsupported element or condition, the system rejects the
request.

###### Topics

- [Default S3 access policy](#default-access-policy "#default-access-policy")
- [Customizing the access policy](#customize-access-policy "#customize-access-policy")
- [IAM policy](#iam-policy "#iam-policy")
- [Tag-based access control](#tag-based-access "#tag-based-access")

### Default S3 access policy

When you create a sequence store, HealthOmics creates a default S3 access policy granting the data store
owner’s root account the following permissions for all accessible objects in the sequence store: S3:GetObject,
S3GetObjectTagging, and S3:ListBucket. The default created policy is:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":
 [
 {
 "Effect": "Allow",
 "Principal":
 {
 "AWS": "arn:aws:iam::111111111111:root"
 },
 "Action":
 [
 "s3:GetObject",
 "s3:GetObjectTagging"
 ],
 "Resource": "arn:aws:s3:us-west-2:222222222222:accesspoint/111111111111-1234567890/object/111111111111/sequenceStore/1234567890/*"
 },
 {
 "Effect": "Allow",
 "Principal":
 {
 "AWS": "arn:aws:iam::111111111111:root"
 },
 "Action": "s3:ListBucket",
 "Resource": "arn:aws:s3:us-west-2:222222222222:accesspoint/111111111111-1234567890/111111111111/sequenceStore/1234567890/*"
 }
 ]
}`

```

### Customizing the access policy

If the S3 access policy is blank, no S3 access is allowed. If there is an existing policy and you need to
remove s3 access, use `deleteS3AccessPolicy` to remove all access.

To add restrictions on the sharing or to grant access to other accounts, you can update the policy using the
`PutS3AccessPolicy` API. Updates to the policy can't go beyond the prefix for the sequence store or
the actions specified.

### IAM policy

To allow a user or IAM principal access using Amazon S3 APIs, in addition to permission in the S3 access policy,
an IAM policy needs to be created and attached to the principal to grant access. A policy allowing Amazon S3 API
access can be applied at the sequence store level or at a read set level. At the read set level, permission can be
restricted either through the prefix or using resource tag filters for sample or subject ID patterns.

If the sequence store uses a customer managed key (CMK), the principal must also have rights to use the
KMS key for decryption. For more information, see [Cross-account KMS access](../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md "../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md")
in the AWS Key Management Service Developer Guide.

The following example gives a user access to a sequence store. You can fine-tune the access with additional
conditions or resource-based filters.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::111111111111:root"
 },
 "Action":
 [
 "s3:GetObject",
 "s3:GetObjectTagging"
 ],
 "Resource": "arn:aws:s3:us-west-2:222222222222:accesspoint/111111111111-1234567890/object/111111111111/sequenceStore/1234567890/*",
 "Condition": {
 "StringEquals": {
 "s3:ExistingObjectTag/omics:readSetStatus": "ACTIVE"
 }
 }
 },
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::111111111111:root"
 },
 "Action": "s3:ListBucket",
 "Resource": "arn:aws:s3:us-west-2:222222222222:accesspoint/111111111111-1234567890",
 "Condition": {
 "StringLike": {
 "s3:prefix": "111111111111/sequenceStore/1234567890/*"
 }
 }
 }
 ]
}`

```

### Tag-based access control

To use tag based access control, the sequence store must first be updated to propagate the tag keys that will
be used. This configuration is set during sequence store creation or updating. Once the tags are propagated, tag
conditions can be used to further add restrictions. The restrictions can be placed in the S3 Access policy or on
the IAM policy. The following is an example of a tab based S3 access policy that would be set:

```
{
    "Sid": "tagRestrictedGets",
    "Effect": "Allow",
    "Principal":
    {
        "AWS": "arn:aws:iam::<target_restricted_account_id>:root"
    },
    "Action":
    [
        "s3:GetObject",
        "s3:GetObjectTagging"
    ],
    "Resource": "arn:aws:s3:us-west-2:222222222222:accesspoint/111111111111-1234567890/object/111111111111/sequenceStore/1234567890/*",
    "Condition":
    {
        "StringEquals":
        {
            "s3:ExistingObjectTag/tagKey1": "tagValue1",
            "s3:ExistingObjectTag/tagKey2": "tagValue2"
        }
    }
}
```

## Example Restriction

Scenario: Creating a share where the data owner can restrict a user’s ability to download “withdrawn” data.

In this scenario, a data owner (account #111111111111) managed a data store. This data owner shares the data
with a broad range of third party users, including a researcher (account #999999999999). As part of managing the
data, the data owner periodically get requests to withdraw a participants data. To manage this withdrawal, the
data owner first restricts direct download access on receiving the request and eventually deletes the data per
their requirements.

To meet this need, the data owner sets up a sequence store and each read set receives a tag for “status” that
will be set to “withdrawn” if the withdrawal request comes through. For data with the tag set to this value, they
want to make sure no user can run “getObject” on this file. To do this setup, the data owner will need to ensure
two steps are taken.

Step 1. For the sequence store, ensure that the status tag is updated to be propagated. This is done by adding
the “status” key into the `propogatedSetLevelTags` when calling `createSequenceStore` or
`updateSequenceStore.`

Step 2. Update the store’s s3 Access Policy to restrict getObject on objects with the status tag set
to withdrawn. This is done by updating the stores access policy using the
`PutS3AccesPolicy` API. The following policy would allow customers to still see
the withdrawn files when listing objects but prevent them from accessing them:

- Statement 1 (restrictedGetWithdrawal): Account 999999999999 can't retrieve objects that are withdrawn.
- Statement 2 (ownerGetAll): Account 111111111111, the data owner, can retrieve all objects, including objects that
  are withdrawn.
- Statement 3 (everyoneListAll): All shared accounts, 111111111111 and 999999999999, can run the **ListBucket**
  operation on the whole prefix.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":
 [
 {
 "Sid": "restrictedGetWithdrawal",
 "Effect": "Allow",
 "Principal":
 {
 "AWS": "arn:aws:iam::999999999999:root"
 },
 "Action":
 [
 "s3:GetObject",
 "s3:GetObjectTagging"
 ],
 "Resource": "arn:aws:s3:us-west-2:222222222222:accesspoint/111111111111-1234567890/object/111111111111/sequenceStore/1234567890/*",
 "Condition":
 {
 "StringNotEquals":
 {
 "s3:ExistingObjectTag/status": "withdrawn"
 }
 }
 },
 {
 "Sid": "ownerGetAll",
 "Effect": "Allow",
 "Principal":
 {
 "AWS": "arn:aws:iam::111111111111:root"
 },
 "Action":
 [
 "s3:GetObject",
 "s3:GetObjectTagging"
 ],
 "Resource": "arn:aws:s3:us-west-2:222222222222:accesspoint/111111111111-1234567890/object/111111111111/sequenceStore/1234567890/*",
 "Condition":
 {
 "StringEquals":
 {
 "s3:ExistingObjectTag/omics:readSetStatus": "ACTIVE"
 }
 }
 },
 {
 "Sid": "everyoneListAll",
 "Effect": "Allow",
 "Principal":
 {
 "AWS": [
 "arn:aws:iam::111111111111:root",
 "arn:aws:iam::999999999999:root"
 ]
 },
 "Action": "s3:ListBucket",
 "Resource": "arn:aws:s3:us-west-2:222222222222:accesspoint/111111111111-1234567890",
 "Condition":
 {
 "StringLike":
 {
 "s3:prefix": "111111111111/sequenceStore/1234567890/*"
 }
 }
 }
 ]
}`

```
