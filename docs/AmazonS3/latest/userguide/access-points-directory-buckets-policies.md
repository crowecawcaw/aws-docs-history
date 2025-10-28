# Configuring IAM policies for using access points for directory buckets

Access points support AWS Identity and Access Management (IAM) resource policies that allow you to control the use
of the access point by resource, user, or other conditions. For an application or user to
access objects through an access point, both the access point and the underlying bucket policy must permit the
request.

###### Important

Adding an access point to a directory bucket doesn't change the bucket's behavior when the bucket is
accessed directly through the bucket's name. All existing
operations against the bucket will continue to work as before. Restrictions that you
include in an access point policy or access point scope apply only to requests made through that access point.

When using IAM resource policies, make sure to resolve security warnings, errors,
general warnings, and suggestions from AWS Identity and Access Management Access Analyzer before you save your policy.
IAM Access Analyzer runs policy checks to validate your policy against IAM [policy grammar](../../../IAM/latest/UserGuide/reference_policies_grammar.md "../../../IAM/latest/UserGuide/reference_policies_grammar.md") and [best practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md"). These checks generate
findings and provide recommendations to help you author policies that are functional and
conform to security best practices.

To learn more about validating policies by using IAM Access Analyzer, see [IAM Access Analyzer policy
validation](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_. To view a
list of the warnings, errors, and suggestions that are returned by IAM Access Analyzer, see [IAM Access Analyzer policy
check reference](../../../IAM/latest/UserGuide/access-analyzer-reference-policy-checks.md "../../../IAM/latest/UserGuide/access-analyzer-reference-policy-checks.md").

## Access points for directory buckets policy examples

The following access point policies demonstrate how to control requests to a directory bucket. Access point policies require
bucket ARNs or access point ARNs. Access point aliases are not supported in policies. Following is an example of an access point ARN:

```

  arn:aws:s3express:`region`:`account-id`:accesspoint/`myaccesspoint`--`zoneID`--xa-s3

```

You can view the access point ARN in the details of an access point. For more information,
see [View details for your access points for directory buckets](access-points-directory-buckets-details.md "access-points-directory-buckets-details.md").

###### Note

Permissions granted in an access point policy are effective only if the underlying bucket
also allows the same access. You can accomplish this in two ways:

1. **(Recommended)** Delegate access control
   from the bucket to the access point, as described in [Delegating access control to
   access points](#access-points-directory-buckets-delegating-control "#access-points-directory-buckets-delegating-control").
2. Add the same permissions contained in the access point policy to the underlying
   bucket's policy.

###### Example 1 – Service control policy to limit access points to VPC network origins

The following service control policy requires all new access points are to be created with a
virtual private cloud (VPC) network origin. With this policy in place, users in your
organization can't create any access point that is accessible from the internet.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "s3express:CreateAccessPoint",
 "Resource": "*",
 "Condition": {
 "StringNotEquals": {
 "s3express:AccessPointNetworkOrigin": "VPC"
 }
 }
 }
 ]
}`

```

###### Example 2 – Access point policy to limit bucket access to access points with VPC network origin

The following access point policy limits all access to the bucket `amzn-s3-demo-bucket--zoneID--x-s3` to
an access point with a VPC networking origin.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyCreateSessionFromNonVPC",
 "Principal": "*",
 "Action": "s3express:CreateSession",
 "Effect": "Deny",
 "Resource": "arn:aws:s3express:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-bucket--usw2-az1--x-s3`"
 }
 ]
}`

```

## Condition keys

Access points for directory buckets have condition keys that you can use in IAM policies to control access to
your resources. The following condition keys represent only part of an IAM policy. For full policy examples,
see [Access points for directory buckets policy examples](#access-points-directory-buckets-policy-examples "#access-points-directory-buckets-policy-examples"), [Delegating access control to
access points](#access-points-directory-buckets-delegating-control "#access-points-directory-buckets-delegating-control"), and [Granting permissions for cross-account access points](#access-points-directory-buckets-cross-account "#access-points-directory-buckets-cross-account").

**`s3express:DataAccessPointArn`**

This example shows how to filter access by the Amazon resource name (ARN) of an access point and matches all access points for AWS account
`111122223333` in Region
`region`:

```
"Condition" : {
    "StringLike": {
        "s3express:DataAccessPointArn": "arn:aws:s3express:`region`:`111122223333`:accesspoint/*"
    }
}
```

**`s3express:DataAccessPointAccount`**

This example shows a string operator that you can use to match on the
account ID of the owner of an access point. The following example matches all access points
that are owned by the AWS account
`111122223333`.

```
"Condition" : {
    "StringEquals": {
        "s3express:DataAccessPointAccount": "`111122223333`"
    }
}
```

**`s3express:AccessPointNetworkOrigin`**

This example shows a string operator that you can use to match on the
network origin, either `Internet` or `VPC`. The
following example matches only access points with a VPC origin.

```
"Condition" : {
    "StringEquals": {
        "s3express:AccessPointNetworkOrigin": "VPC"
    }
}
```

**`s3express:Permissions`**

You can use `s3express:Permissions` to restrict access to specific API operations in access point scope. The following API operations are supported:

- `PutObject`
- `GetObject`
- `DeleteObject`
- `ListBucket` (required for `ListObjectsV2`)
- `GetObjectAttributes`
- `AbortMultipartUpload`
- `ListBucketMultipartUploads`
- `ListMultipartUploadParts`

###### Note

When using multi-value condition keys, we recommend you use `ForAllValues` with `Allow` statements and `ForAnyValue` with `Deny` statements.
For more information, see [Multivalued context keys](../../../IAM/latest/UserGuide/reference_policies_condition-single-vs-multi-valued-context-keys.md#reference_policies_condition-multi-valued-context-keys "../../../IAM/latest/UserGuide/reference_policies_condition-single-vs-multi-valued-context-keys.md#reference_policies_condition-multi-valued-context-keys") in the IAM User Guide.

For more information about using condition keys with Amazon S3, see [Actions, resources, and condition keys for Amazon S3](../../../service-authorization/latest/reference/list_amazons3.md "../../../service-authorization/latest/reference/list_amazons3.md") in the _Service Authorization
Reference_.

For more information about the required permissions to S3 API operations by S3 resource types, see [Required permissions for Amazon S3 API operations](using-with-s3-policy-actions.md "using-with-s3-policy-actions.md").

## Delegating access control to

access points

You can delegate access control from the bucket policy to the access point policy. The following
example bucket policy allows full access to all access points that are owned by the bucket
owner's account. After applying the policy, all access to this bucket is controlled by access point policies. We recommend configuring your buckets this way for all use cases that
don't require direct access to the bucket.

###### Example bucket policy that delegates access control to access points

```
{
    "Version": "2012-10-17",
    "Statement" : [
    {
        "Effect": "Allow",
        "Principal" : { "AWS": "*" },
        "Action" : "*",
        "Resource" : [ "`Bucket ARN`",
        "Condition": {
            "StringEquals" : { "s3express:DataAccessPointAccount" : "`Bucket owner's account ID`" }
        }
    }]
}
```

## Granting permissions for cross-account access points

To create an access point to a bucket that's owned by another account, you must first create
the access point by specifying the bucket name and account owner ID. Then, the bucket owner must
update the bucket policy to authorize requests from the access point. Creating an access point is
similar to creating a DNS CNAME in that the access point doesn't provide access to the bucket
contents. All bucket access is controlled by the bucket policy. The following example
bucket policy allows `GET` and `LIST` requests on the bucket from
an access point that's owned by a trusted AWS account.

Replace `Bucket ARN` with the ARN of the bucket.

###### Example of bucket policy delegating permissions to another AWS account

JSON

```
`{
 "Version":"2012-10-17",
 "Statement" : [
 {
 "Sid": "AllowCreateSessionForDirectoryBucket",
 "Effect": "Allow",
 "Principal" : { "AWS": "*" },
 "Action" : "s3express:CreateSession",
 "Resource" : [ "`arn:aws:s3express:us-west-2:111122223333:bucket/amzn-s3-demo-bucket--usw2-az1--x-s3`" ],
 "Condition": {
 "ForAllValues:StringEquals": {
 "s3express:Permissions": [
 "GetObject",
 "ListBucket"
 ]
 }
 }
 }]
}`

```
