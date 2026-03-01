# Policies and permissions in Amazon S3

This page provides an overview of bucket and user policies in Amazon S3 and describes the basic
elements of an AWS Identity and Access Management (IAM) policy. Each listed element links to more details about
that element and examples of how to use it.

For a complete list of Amazon S3 actions, resources, and conditions, see [Actions, resources, and condition keys for Amazon S3](../../../service-authorization/latest/reference/list_amazons3.md "../../../service-authorization/latest/reference/list_amazons3.md") in the _Service Authorization
Reference_.

For more information about the permissions to S3 API operations by S3 resource types, see [Required permissions for Amazon S3 API operations](using-with-s3-policy-actions.md "using-with-s3-policy-actions.md").

In its most basic sense, a policy contains the following elements:

- [Resource](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-resources "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-resources") – The Amazon S3 bucket, object, access point, or
  job that the policy applies to. Use the Amazon Resource Name (ARN) of the bucket,
  object, access point, or job to identify the resource.

An example for bucket-level operations:

`"Resource":
 "arn:aws:s3:::`bucket_name`"`

Examples for object-level operations:

    + `"Resource":
     "arn:aws:s3:::`bucket_name/*`"`
     for all objects in the bucket.
    + `"Resource":
     "arn:aws:s3:::`bucket_name/prefix/*`"`
     for objects under a certain prefix in the bucket.

For more information, see [Policy resources for Amazon S3](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-resources "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-resources").

- [Actions](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-actions "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-actions") – For each resource, Amazon S3 supports a
  set of operations. You identify resource operations that you will allow (or deny) by
  using action keywords.

For example, the `s3:ListBucket` permission allows the user to use the
Amazon S3 [ListObjectsV2](../API/API_ListObjectsV2.md "../API/API_ListObjectsV2.md") operation. (The
`s3:ListBucket` permission is a case where the action name doesn't
map directly to the operation name.) For more information about using Amazon S3 actions,
see [Policy actions for Amazon S3](security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-actions "security_iam_service-with-iam.md#security_iam_service-with-iam-id-based-policies-actions"). For a
complete list of Amazon S3 actions, see [Actions](../API/API_Operations.md "../API/API_Operations.md") in the _Amazon Simple Storage Service API Reference_.

- [Effect](../../../IAM/latest/UserGuide/reference_policies_elements_effect.md "../../../IAM/latest/UserGuide/reference_policies_elements_effect.md") – What the effect will be when the user
  requests the specific action—this can be either `Allow` or
  `Deny`.

If you don't explicitly grant access to (allow) a resource, access is implicitly
denied. You can also explicitly deny access to a resource. You might do this to make
sure that a user can't access the resource, even if a different policy grants
access. For more information, see [IAM JSON
Policy Elements: Effect](../../../IAM/latest/UserGuide/reference_policies_elements_effect.md "../../../IAM/latest/UserGuide/reference_policies_elements_effect.md") in the
_IAM User Guide_.

- [Principal](security_iam_service-with-iam.md#s3-bucket-user-policy-specifying-principal-intro "security_iam_service-with-iam.md#s3-bucket-user-policy-specifying-principal-intro") – The account or user who is allowed
  access to the actions and resources in the statement. In a bucket policy, the
  principal is the user, account, service, or other entity that is the recipient of
  this permission. For more information, see [Principals for bucket policies](security_iam_service-with-iam.md#s3-bucket-user-policy-specifying-principal-intro "security_iam_service-with-iam.md#s3-bucket-user-policy-specifying-principal-intro").
- [Condition](amazon-s3-policy-keys.md "amazon-s3-policy-keys.md") –
  Conditions for when a policy is in effect. You can use AWS‐wide keys and
  Amazon S3‐specific keys to specify conditions in an Amazon S3 access policy. For more
  information, see [Bucket policy examples using condition keys](amazon-s3-policy-keys.md "amazon-s3-policy-keys.md").
  The following example bucket policy shows the `Effect`, `Principal`,
  `Action`, and `Resource` elements. This policy allows
  `Akua`, a user in account
  `123456789012`, `s3:GetObject`,
  `s3:GetBucketLocation`, and `s3:ListBucket` Amazon S3 permissions on
  the `amzn-s3-demo-bucket1` bucket.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "ExamplePolicy01",
 "Statement": [
 {
 "Sid": "ExampleStatement01",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`123456789012`:user/`Akua`"
 },
 "Action": [
 "s3:GetObject",
 "s3:GetBucketLocation",
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::amzn-s3-demo-bucket1/*",
 "arn:aws:s3:::amzn-s3-demo-bucket1"
 ]
 }
 ]
}`

```

For complete policy language information, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") and
[IAM JSON policy reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md")
in the _IAM User Guide_.

## Permission delegation

If an AWS account owns a resource, it can grant those permissions to another
AWS account. That account can then delegate those permissions, or a subset of them, to
users in the account. This is referred to as _permission
delegation_. But an account that receives permissions from another account
can't delegate permission cross-account to another AWS account.

## Amazon S3 bucket and object ownership

Buckets and objects are Amazon S3 resources. By default, only the resource owner can access
these resources. The resource owner refers to the AWS account that creates the
resource. For example:

- The AWS account that you use to create buckets and upload objects owns those
  resources.
- If you upload an object using AWS Identity and Access Management (IAM) user or role credentials, the
  AWS account that the user or role belongs to owns the object.
- A bucket owner can grant cross-account permissions to another AWS account
  (or users in another account) to upload objects. In this case, the AWS account
  that uploads objects owns those objects. The bucket owner doesn't have
  permissions on the objects that other accounts own, with the following
  exceptions:
  - The bucket owner pays the bills. The bucket owner can deny access to
    any objects, or delete any objects in the bucket, regardless of who owns
    them.
  - The bucket owner can archive any objects or restore archived objects
    regardless of who owns them. Archival refers to the storage class used
    to store the objects. For more information, see [Managing the lifecycle of objects](object-lifecycle-mgmt.md "object-lifecycle-mgmt.md").

### Ownership and request authentication

All requests to a bucket are either authenticated or unauthenticated.
Authenticated requests must include a signature value that authenticates the request
sender, and unauthenticated requests do not. For more information about request
authentication, see [Making requests](../API/MakingRequests.md "../API/MakingRequests.md") in the
_Amazon S3 API Reference_.

A bucket owner can allow unauthenticated requests. For example, unauthenticated
[PutObject](../API/RESTObjectPUT.md "../API/RESTObjectPUT.md")
requests are allowed when a bucket has a public bucket policy, or when a bucket ACL
grants `WRITE` or `FULL_CONTROL` access to the `All
 Users` group or the anonymous user specifically. For more information
about public bucket policies and public access control lists (ACLs), see [The meaning of "public"](access-control-block-public-access.md#access-control-block-public-access-policy-status "access-control-block-public-access.md#access-control-block-public-access-policy-status").

All unauthenticated requests are made by the anonymous user. This user is
represented in ACLs by the specific canonical user ID
`65a011a29cdf8ec533ec3d1ccaae921c`. If an object is uploaded to a
bucket through an unauthenticated request, the anonymous user owns the object. The
default object ACL grants `FULL_CONTROL` to the anonymous user as the
object's owner. Therefore, Amazon S3 allows unauthenticated requests to retrieve the
object or modify its ACL.

To prevent objects from being modified by the anonymous user, we recommend that
you do not implement bucket policies that allow anonymous public writes to your
bucket or use ACLs that allow the anonymous user write access to your bucket. You
can enforce this recommended behavior by using Amazon S3 Block Public Access.

For more information about blocking public access, see [Blocking public access to your Amazon S3 storage](access-control-block-public-access.md "access-control-block-public-access.md"). For more information about
ACLs, see [Access control list (ACL) overview](acl-overview.md "acl-overview.md").

###### Important

We recommend that you don't use the AWS account root user credentials to make
authenticated requests. Instead, create an IAM role and grant that role full
access. We refer to users with this role as _administrator users_. You can use credentials assigned to the
administrator role, instead of AWS account root user credentials, to interact
with AWS and perform tasks, such as create a bucket, create users, and grant
permissions. For more information, see [AWS security credentials](../../../general/latest/gr/root-vs-iam.md "../../../general/latest/gr/root-vs-iam.md") and
[Security best practices in
IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.
