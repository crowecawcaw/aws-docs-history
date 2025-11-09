# Controlling ownership of objects and disabling ACLs

for your bucket

S3 Object Ownership is an Amazon S3 bucket-level setting that you can use to control ownership
of objects uploaded to your bucket and to disable or enable [access control lists (ACLs)](acl-overview.md "acl-overview.md"). By default, Object Ownership is set to the Bucket
owner enforced setting and all ACLs are disabled. When ACLs are disabled, the bucket owner
owns all the objects in the bucket and manages access to data exclusively using access
management policies.

A majority of modern use cases in Amazon S3 no longer require the use of ACLs, and we recommend
that you keep ACLs disabled except in circumstances where you must control access for each
object individually. With ACLs disabled, you can use policies to more easily control access to every object in your bucket, regardless
of who uploaded the objects in your bucket.

Object Ownership has three settings that you can use to control ownership of objects
uploaded to your bucket and to disable or enable ACLs:

###### ACLs disabled

- **Bucket owner enforced (default)** – ACLs
  are disabled, and the bucket owner automatically owns and has full control over
  every object in the bucket. ACLs no longer affect permissions to data in the S3
  bucket. The bucket uses policies to define access control.

###### ACLs enabled

- **Bucket owner preferred** – The bucket owner
  owns and has full control over new objects that other accounts write to the bucket
  with the `bucket-owner-full-control` canned ACL.
- **Object writer** – The
  AWS account that uploads an object owns the object, has full control over it, and
  can grant other users access to it through ACLs.
  For the majority of modern use cases in S3, we recommend that you keep ACLs disabled by
  applying the Bucket owner enforced setting and using your bucket policy to share data with
  users outside of your account as needed. This approach simplifies permissions management.
  You can disable ACLs on both newly created and already existing buckets. For newly created
  buckets, ACLs are disabled by default. In the case of an existing bucket that already has
  objects in it, after you disable ACLs, the object and bucket ACLs are no longer part of an
  access evaluation, and access is granted or denied on the basis of policies. For existing
  buckets, you can re-enable ACLs at any time after you disable them, and your preexisting
  bucket and object ACLs are restored.

Before you disable ACLs, we recommend that you review your bucket policy to ensure that it
covers all the ways that you intend to grant access to your bucket outside of your account.
After you disable ACLs, your bucket accepts only `PUT` requests that do not
specify an ACL or `PUT` requests with bucket owner full control ACLs, for
example, the `bucket-owner-full-control` canned ACL or equivalent forms of this
ACL expressed in XML. Existing applications that support bucket owner full control ACLs see
no impact. `PUT` requests that contain other ACLs (for example, custom grants to
certain AWS accounts) fail and return a `400` error with the error code
`AccessControlListNotSupported`.

In contrast, a bucket with the Bucket owner preferred setting continues to accept and
honor bucket and object ACLs. With this setting, new objects that are written with the
`bucket-owner-full-control` canned ACL are automatically owned by the bucket
owner rather than the object writer. All other ACL behaviors remain in place. To require all
Amazon S3 `PUT` operations to include the `bucket-owner-full-control`
canned ACL, you can [add a bucket
policy](ensure-object-ownership.md#ensure-object-ownership-bucket-policy "ensure-object-ownership.md#ensure-object-ownership-bucket-policy") that allows only object uploads using this ACL.

To see which Object Ownership settings are applied to your buckets, you can use
Amazon S3 Storage Lens metrics. S3 Storage Lens is a cloud-storage analytics feature that you can use to gain organization-wide
visibility into object-storage usage and activity. For more information, see [Using S3 Storage Lens to find Object Ownership settings](storage-lens-access-management.md "storage-lens-access-management.md").

###### Note

For more information about using the Amazon S3 Express One Zone storage class with directory buckets, see [S3 Express One Zone](directory-bucket-high-performance.md#s3-express-one-zone "directory-bucket-high-performance.md#s3-express-one-zone") and [Working with directory buckets](directory-buckets-overview.md "directory-buckets-overview.md").

## Object Ownership settings

This table shows the impact that each Object Ownership setting has on ACLs, objects,
object ownership, and object uploads.

| Setting                         | Applies to                   | Effect on object ownership                                                                                                                                                             | Effect on ACLs                                                                                                                                                                                                                                                                | Uploads accepted                                                                    |
| ------------------------------- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Bucket owner enforced (default) | All new and existing objects | Bucket owner owns every object.                                                                                                                                                        | ACLs are disabled and no longer affect access permissions to your<br>bucket. Requests to set or update ACLs fail. However, requests to<br>read ACLs are supported.<br>Bucket owner has full ownership and control.<br>Object writer no longer has full ownership and control. | Uploads with bucket owner full control ACLs or uploads that don't<br>specify an ACL |
| Bucket owner preferred          | New objects                  | If an object upload includes the<br>`bucket-owner-full-control` canned ACL, the bucket owner<br>owns the object. Objects uploaded with other ACLs are owned by the<br>writing account. | ACLs can be updated and can grant permissions.<br>If an object upload includes the<br>`bucket-owner-full-control` canned ACL, the bucket<br>owner has full control access, and the object writer no longer has<br>full control access.                                        | All uploads                                                                         |
| Object writer                   | New objects                  | Object writer owns the object.                                                                                                                                                         | ACLs can be updated and can grant permissions.<br>Object writer has full control access.                                                                                                                                                                                      | All uploads                                                                         |

## Changes introduced by disabling ACLs

When the Bucket owner enforced setting for Object Ownership is applied, ACLs are disabled and you automatically own and take full
control over every object in the bucket without taking any additional actions. Bucket owner enforced is the default setting for all newly created buckets.
After the Bucket owner enforced setting is applied, you will see three changes:

- All bucket ACLs and object ACLs are disabled, which gives full access to you,
  as the bucket owner. When you perform a read ACL request on your bucket or
  object, you will see that full access is given only to the bucket owner.
- You, as the bucket owner, automatically own and have full control over every
  object in your bucket.
- ACLs no longer affect access permissions to your bucket. As a result, access
  control for your data is based on policies, such as AWS Identity and Access Management (IAM) [identity-based policies](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md"), Amazon S3 [bucket policies](bucket-policies.md "bucket-policies.md"), VPC endpoint policies, and Organizations [service control policies (SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") or [resource control policies (RCPs)](../../../organizations/latest/userguide/orgs_manage_policies_rcps.md "../../../organizations/latest/userguide/orgs_manage_policies_rcps.md").

![Diagram showing what happens when you apply the Bucket owner enforced setting to disable ACLs.](images/bucket-owner-enforced.png)

If you use S3 Versioning, the bucket owner owns and has full control over all object
versions in your bucket. Applying the Bucket owner enforced setting does not add a new
version of an object.

New objects can be uploaded to your bucket only if they use bucket owner full control
ACLs or don't specify an ACL. Object uploads fail if they specify any other ACL. For
more information, see [Troubleshooting](object-ownership-error-responses.md "object-ownership-error-responses.md").

Because the following example `PutObject` operation using the AWS Command Line Interface
(AWS CLI) includes the `bucket-owner-full-control` canned ACL, the object can
be uploaded to a bucket with disabled ACLs.

```
aws s3api put-object --bucket `amzn-s3-demo-bucket` --key `key-name` --body `path-to-file` --acl bucket-owner-full-control
```

Because the following `PutObject` operation doesn't specify an ACL, it also
succeeds for a bucket with disabled ACLs.

```
aws s3api put-object --bucket `amzn-s3-demo-bucket` --key `key-name` --body `path-to-file`
```

###### Note

If other AWS accounts need access to objects after uploading, you must grant
additional permissions to those accounts through bucket policies. For more
information, see [Walkthroughs that use policies to
manage access to your Amazon S3 resources](example-walkthroughs-managing-access.md "example-walkthroughs-managing-access.md").

###### Re-enabling ACLs

You can re-enable ACLs by changing from the Bucket owner enforced setting to
another Object Ownership setting at any time. If you used object ACLs for
permissions management before you applied the Bucket owner enforced setting and you
didn't migrate these object ACL permissions to your bucket policy, after you
re-enable ACLs, these permissions are restored. Additionally, objects written to the
bucket while the Bucket owner enforced setting was applied are still owned by the
bucket owner.

For example, if you change from the Bucket owner enforced setting back to the Object
writer setting, you, as the bucket owner, no longer own and have full control over objects
that were previously owned by other AWS accounts. Instead, the uploading accounts
again own these objects. Objects owned by other accounts use ACLs for permissions,
so you can't use policies to grant permissions to these objects. However, you, as
the bucket owner, still own any objects that were written to the bucket while the
Bucket owner enforced setting was applied. These objects are not owned by the object
writer, even if you re-enable ACLs.

For instructions on enabling and managing ACLs using the AWS Management Console, AWS Command Line Interface (CLI),
REST API, or AWS SDKs, see [Configuring ACLs](managing-acls.md "managing-acls.md").

## Prerequisites for disabling

ACLs

Before you disable ACLs for an existing bucket, complete the following
prerequisites.

- [Review bucket and object ACLs and
  migrate ACL permissions](object-ownership-migrating-acls-prerequisites.md#object-ownership-acl-permissions "object-ownership-migrating-acls-prerequisites.md#object-ownership-acl-permissions")
- [Identify requests that required an
  ACL for authorization](object-ownership-migrating-acls-prerequisites.md#object-ownership-acl-identify "object-ownership-migrating-acls-prerequisites.md#object-ownership-acl-identify")
- [Review and update bucket policies
  that use ACL-related condition keys](object-ownership-migrating-acls-prerequisites.md#object-ownership-bucket-policies "object-ownership-migrating-acls-prerequisites.md#object-ownership-bucket-policies")

## Object Ownership permissions

To apply, update, or delete an Object Ownership setting for a bucket, you need the
`s3:PutBucketOwnershipControls` permission. To return the
Object Ownership setting for a bucket, you need the
`s3:GetBucketOwnershipControls` permission. For more information, see
[Setting Object Ownership when you create
a bucket](object-ownership-new-bucket.md "object-ownership-new-bucket.md") and [Viewing the Object Ownership setting for
an S3 bucket](object-ownership-retrieving.md "object-ownership-retrieving.md").

## Disabling ACLs for all new

buckets

By default, all new buckets are created with the Bucket owner enforced setting applied and
ACLs are disabled. We recommend keeping ACLs disabled. As a general rule, we recommend
using S3 resource-based policies (bucket policies and access point policies) or IAM
policies for access control instead of ACLs. Policies are a simplified and more flexible
access control option. With bucket policies and access point policies, you can define
rules that apply broadly across all requests to your Amazon S3 resources.

## Replication and Object Ownership

When you use S3 replication and the source and destination buckets are owned by
different AWS accounts, you can disable ACLs (with the Bucket owner enforced setting
for Object Ownership) to change replica ownership to the AWS account that owns the
destination bucket. This setting mimics the existing owner override behavior without the
need of the `s3:ObjectOwnerOverrideToBucketOwner` permission. All objects
that are replicated to the destination bucket with the Bucket owner enforced setting are
owned by the destination bucket owner. For more information about the owner override
option for replication configurations, see [Changing the replica owner](replication-change-owner.md "replication-change-owner.md").

## Setting Object Ownership

You can apply an Object Ownership setting by using the Amazon S3 console, AWS CLI, AWS SDKs,
Amazon S3 REST API, or AWS CloudFormation. The following REST API and AWS CLI commands support
Object Ownership:

| REST API                                                                                                                   | AWS CLI                                                                                                                                                                                                                                                             | Description                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| [PutBucketOwnershipControls](../API/API_PutBucketOwnershipControls.md "../API/API_PutBucketOwnershipControls.md")          | [put-bucket-ownership-controls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-ownership-controls.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/put-bucket-ownership-controls.html")          | Creates or modifies the Object Ownership setting for an existing S3<br>bucket.                                 |
| [CreateBucket](../API/API_CreateBucket.md "../API/API_CreateBucket.md")                                                    | [create-bucket](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/create-bucket.html")                                                          | Creates a bucket using the `x-amz-object-ownership`<br>request header to specify the Object Ownership setting. |
| [GetBucketOwnershipControls](../API/API_GetBucketOwnershipControls.md "../API/API_GetBucketOwnershipControls.md")          | [get-bucket-ownership-controls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-ownership-controls.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-ownership-controls.html")          | Retrieves the Object Ownership setting for an Amazon S3 bucket.                                                |
| [DeleteBucketOwnershipControls](../API/API_DeleteBucketOwnershipControls.md "../API/API_DeleteBucketOwnershipControls.md") | [delete-bucket-ownership-controls](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-ownership-controls.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/delete-bucket-ownership-controls.html") | Deletes the Object Ownership setting for an Amazon S3 bucket.                                                  |

For more information about applying and working with Object Ownership settings, see
the following topics.

###### Topics

- [Prerequisites for
  disabling ACLs](object-ownership-migrating-acls-prerequisites.md "object-ownership-migrating-acls-prerequisites.md")
- [Setting Object Ownership when you create
  a bucket](object-ownership-new-bucket.md "object-ownership-new-bucket.md")
- [Setting Object Ownership on an
  existing bucket](object-ownership-existing-bucket.md "object-ownership-existing-bucket.md")
- [Viewing the Object Ownership setting for
  an S3 bucket](object-ownership-retrieving.md "object-ownership-retrieving.md")
- [Disabling ACLs for all new buckets and
  enforcing Object Ownership](ensure-object-ownership.md "ensure-object-ownership.md")
- [Troubleshooting](object-ownership-error-responses.md "object-ownership-error-responses.md")
