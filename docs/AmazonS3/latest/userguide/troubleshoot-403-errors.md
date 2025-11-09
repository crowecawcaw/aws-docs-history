# Troubleshoot access denied (403

Forbidden) errors in Amazon S3

Access denied (HTTP `403 Forbidden`) errors appear when AWS explicitly or
implicitly denies an authorization request.

- An _explicit denial_ occurs when a policy
  contains a `Deny` statement for the specific AWS action.
- An _implicit denial_ occurs when there is no
  applicable `Deny` statement and also no applicable `Allow`
  statement.
  Because an AWS Identity and Access Management (IAM) policy implicitly denies an IAM principal by default, the
  policy must explicitly allow the principal to perform an action. Otherwise, the policy
  implicitly denies access. For more information, see [The difference between explicit and implicit denies](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md#AccessPolicyLanguage_Interplay "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md#AccessPolicyLanguage_Interplay") in the _IAM User Guide_. For information about the policy evaluation
  logic that determines whether an access request is allowed or denied, see [Policy evaluation logic](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md") in the _IAM User Guide_.

For more information about the permissions to S3 API operations by S3 resource types, see [Required permissions for Amazon S3 API operations](using-with-s3-policy-actions.md "using-with-s3-policy-actions.md").

The following topics cover the most common causes of access denied errors in Amazon S3.

###### Note

For access denied (HTTP `403 Forbidden`) errors, Amazon S3 doesn't charge the
bucket owner when the request is initiated outside of the bucket owner's individual
AWS account or the bucket owner's AWS organization.

###### Topics

- [Access denied message examples and how
  to troubleshoot them](#access-denied-message-examples "#access-denied-message-examples")
- [Access denied due to Requester Pays settings](#access-denied-requester-pays "#access-denied-requester-pays")
- [Bucket policies and IAM policies](#bucket-iam-policies "#bucket-iam-policies")
- [Amazon S3 ACL settings](#troubleshoot-403-acl-settings "#troubleshoot-403-acl-settings")
- [S3 Block Public Access settings](#troubleshoot-403-bpa "#troubleshoot-403-bpa")
- [Amazon S3 encryption settings](#troubleshoot-403-encryption "#troubleshoot-403-encryption")
- [S3 Object Lock settings](#troubleshoot-403-object-lock "#troubleshoot-403-object-lock")
- [VPC endpoint policies](#troubleshoot-403-vpc "#troubleshoot-403-vpc")
- [AWS Organizations policies](#troubleshoot-403-orgs "#troubleshoot-403-orgs")
- [CloudFront distribution access](#troubleshoot-403-cloudfront "#troubleshoot-403-cloudfront")
- [Access point settings](#troubleshoot-403-access-points "#troubleshoot-403-access-points")
- [Additional resources](#troubleshoot-403-additional-resources "#troubleshoot-403-additional-resources")

###### Note

If you're trying to troubleshoot a permissions issue, start with the [Access denied message examples and how
to troubleshoot them](#access-denied-message-examples "#access-denied-message-examples") section, then go to the [Bucket policies and IAM policies](#bucket-iam-policies "#bucket-iam-policies") section. Also be sure to follow the guidance in
[Tips for checking permissions](#troubleshoot-403-tips "#troubleshoot-403-tips").

## Access denied message examples and how

to troubleshoot them

Amazon S3 now includes additional context in access denied (HTTP `403 Forbidden`) errors
for requests made to resources within the same AWS account or same organization in AWS Organizations. This new
context includes the type of policy that denied access, the reason for denial, and information about the
IAM user or role that requested access to the resource.

This additional context helps you to troubleshoot access issues, identify the root cause of
access denied errors, and fix incorrect access controls by updating the relevant policies. This
additional context is also available in AWS CloudTrail logs. Enhanced access denied error messages for
same-account or same-organization requests are now available in all AWS Regions, including the
AWS GovCloud (US) Regions and the China Regions.

Most access denied error messages appear in the format `User
 `user-arn`is not authorized to perform
`action` on "`resource-arn`"
 because `context`. In this example,
 `user-arn`is the [Amazon Resource Name
 (ARN)](../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns "../../../IAM/latest/UserGuide/reference_identifiers.md#identifiers-arns") of the user that doesn't receive access,
`action`is the service action that the
 policy denies, and`resource-arn`is the ARN of
 the resource on which the policy acts. The
`context`` field represents additional context
about the policy type that explains why the policy denied access.

When a policy explicitly denies access because the policy contains a `Deny`
statement, then the access denied error message includes the phrase `with an
 explicit deny in a `type` policy`. When the policy
implicitly denies access, then the access denied error message includes the phrase
`because no `type`policy allows the
`action` action`.

###### Important

- Enhanced access denied messages are returned only for same-account requests or for
  requests within the same organization in AWS Organizations. Cross-account requests outside of the same
  organization return a generic `Access Denied` message.

For information about the policy evaluation logic that determines whether
a cross-account access request is allowed or denied, see [Cross-account policy evaluation logic](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic-cross-account.md "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic-cross-account.md") in the _IAM User Guide_. For a walkthrough that shows
how to grant cross-account access, see [Example 2: Bucket owner
granting cross-account bucket permissions](example-walkthroughs-managing-access-example2.md "example-walkthroughs-managing-access-example2.md").

- For requests within the same organization in AWS Organizations:
  - Enhanced access denied messages aren't returned if a denial occurs because of a virtual
    private cloud (VPC) endpoint policy.
  - Enhanced access denied messages are provided whenever both the bucket owner and the caller
    account belong to the same organization in AWS Organizations. Although buckets configured with the
    S3 Object Ownership **Bucket owner preferred** or **Object
    writer** settings might contain objects owned by different accounts, object
    ownership doesn't affect enhanced access denied messages. Enhanced access denied messages are
    returned for all object requests as long as the bucket owner and caller are in the same
    organization, regardless of who owns the specific object. For information about
    Object Ownership settings and configurations, see [Controlling ownership of objects and disabling ACLs
    for your bucket](about-object-ownership.md "about-object-ownership.md").

- Enhanced access denied error messages aren't returned for requests made to
  directory buckets. Directory bucket requests return a generic `Access
Denied` message.
- If multiple policies of the same policy type deny an authorization
  request, the access denied error message doesn't specify the number of
  policies.
- If multiple policy types deny an authorization request, the error message
  includes only one of those policy types.
- If an access request is denied due to multiple reasons, the error message
  includes only one of the reasons for denial.

The following examples show the format for different types of access denied error
messages and how to troubleshoot each type of message.

### Access denied due to a resource

control policy – explicit denial

1. Check for a `Deny` statement for the action in your resource
   control policies (RCPs). For the following example, the action is
   `s3:GetObject`.
2. Update your RCP by removing the `Deny` statement. For more information, see [Update a resource control policy (RCP)](../../../organizations/latest/userguide/orgs_policies_update.md#update_policy-rcp "../../../organizations/latest/userguide/orgs_policies_update.md#update_policy-rcp") in the
   _AWS Organizations User Guide_.

```
An error occurred (AccessDenied) when calling the GetObject operation:
User: arn:aws:iam::`777788889999`:user/`MaryMajor` is not authorized to perform:
s3:GetObject on resource: "arn:aws:s3:::`amzn-s3-demo-bucket1`/`object-name`"
with an explicit deny in a resource control policy
```

### Access denied due to a Service

Control Policy – implicit denial

1. Check for a missing `Allow` statement for the action in your
   service control policies (SCPs). For the following example, the action is
   `s3:GetObject`.
2. Update your SCP by adding the `Allow` statement. For more
   information, see [Updating an SCP](../../../organizations/latest/userguide/orgs_manage_policies_scps_create.md#update_policy "../../../organizations/latest/userguide/orgs_manage_policies_scps_create.md#update_policy") in the
   _AWS Organizations User Guide_.

```
User: arn:aws:iam::`777788889999`:user/`MaryMajor` is not authorized to perform:
s3:GetObject because no service control policy allows the s3:GetObject action
```

### Access denied due to a Service

Control Policy – explicit denial

1. Check for a `Deny` statement for the action in your Service
   Control Policies (SCPs). For the following example, the action is
   `s3:GetObject`.
2. Update your SCP by changing the `Deny` statement to allow the
   user the necessary access. For an example of how you can do this, see [Prevent IAM users and roles from making specified changes, with an
   exception for a specified admin role](../../../organizations/latest/userguide/orgs_manage_policies_scps_examples_general.md#example-scp-restricts-with-exception "../../../organizations/latest/userguide/orgs_manage_policies_scps_examples_general.md#example-scp-restricts-with-exception") in the
   _AWS Organizations User Guide_. For more information about
   updating your SCP, see [Updating an SCP](../../../organizations/latest/userguide/orgs_manage_policies_scps_create.md#update_policy "../../../organizations/latest/userguide/orgs_manage_policies_scps_create.md#update_policy") in the
   _AWS Organizations User Guide_.

```
User: arn:aws:iam::`777788889999`:user/`MaryMajor` is not authorized to perform:
s3:GetObject with an explicit deny in a service control policy
```

### Access denied due to

a VPC endpoint policy – implicit denial

1. Check for a missing `Allow` statement for the action in your
   virtual private cloud (VPC) endpoint policies. For the following example,
   the action is `s3:GetObject`.
2. Update your VPC endpoint policy by adding the `Allow`
   statement. For more information, see [Update a VPC endpoint policy](../../../vpc/latest/privatelink/vpc-endpoints-access.md#update-vpc-endpoint-policy "../../../vpc/latest/privatelink/vpc-endpoints-access.md#update-vpc-endpoint-policy") in the
   _AWS PrivateLink Guide_.

```
User: arn:aws:iam::`123456789012`:user/`MaryMajor` is not authorized to perform:
s3:GetObject because no VPC endpoint policy allows the s3:GetObject action
```

### Access denied due to

a VPC endpoint policy – explicit denial

1. Check for an explicit `Deny` statement for the action in your
   virtual private cloud (VPC) endpoint policies. For the following example,
   the action is `s3:GetObject`.
2. Update your VPC endpoint policy by changing the `Deny`
   statement to allow the user the necessary access. For example, you can
   update your `Deny` statement to use the
   `aws:PrincipalAccount` condition key with the
   `StringNotEquals` condition operator to allow the specific
   principal access, as shown in [Example 7: Excluding certain
   principals from a Deny statement](amazon-s3-policy-keys.md#example-exclude-principal-from-deny-statement "amazon-s3-policy-keys.md#example-exclude-principal-from-deny-statement"). For more
   information about updating your VPC endpoint policy, see [Update a VPC endpoint policy](../../../vpc/latest/privatelink/vpc-endpoints-access.md#update-vpc-endpoint-policy "../../../vpc/latest/privatelink/vpc-endpoints-access.md#update-vpc-endpoint-policy") in the
   _AWS PrivateLink Guide_.

```
User: arn:aws:iam::`123456789012`:user/`MaryMajor` is not authorized to perform:
s3:GetObject on resource: "arn:aws:s3:::`amzn-s3-demo-bucket1`/`object-name`" with
an explicit deny in a VPC endpoint policy
```

### Access denied

due to a permissions boundary – implicit denial

1. Check for a missing `Allow` statement for the action in your
   permissions boundary. For the following example, the action is
   `s3:GetObject`.
2. Update your permissions boundary by adding the `Allow`
   statement to your IAM policy. For more information, see [Permissions
   boundaries for IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") and [Editing
   IAM policies](../../../IAM/latest/UserGuide/access_policies_manage-edit.md "../../../IAM/latest/UserGuide/access_policies_manage-edit.md") in the _IAM User Guide_.

```
User: arn:aws:iam::`123456789012`:user/`MaryMajor` is not authorized to perform:
s3:GetObject on resource: "arn:aws:s3:::`amzn-s3-demo-bucket1`/`object-name`"
because no permissions boundary allows the s3:GetObject action
```

### Access denied

due to a permissions boundary – explicit denial

1. Check for an explicit `Deny` statement for the action in your
   permissions boundary. For the following example, the action is
   `s3:GetObject`.
2. Update your permissions boundary by changing the `Deny`
   statement in your IAM policy to allow the user the necessary access. For
   example, you can update your `Deny` statement to use the
   `aws:PrincipalAccount` condition key with the
   `StringNotEquals` condition operator to allow the specific
   principal access, as shown in [aws:PrincipalAccount](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalaccount") in the _IAM User Guide_. For more information, see
   [Permissions
   boundaries for IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") and [Editing
   IAM policies](../../../IAM/latest/UserGuide/access_policies_manage-edit.md "../../../IAM/latest/UserGuide/access_policies_manage-edit.md") in the _IAM User Guide_.

```
User: arn:aws:iam::`777788889999`:user/`MaryMajor` is not authorized to perform:
s3:GetObject with an explicit deny in a permissions boundary
```

### Access denied due

to session policies – implicit denial

1. Check for a missing `Allow` statement for the action in your
   session policies. For the following example, the action is
   `s3:GetObject`.
2. Update your session policy by adding the `Allow` statement. For
   more information, see [Session
   policies](../../../IAM/latest/UserGuide/access_policies.md#policies_session "../../../IAM/latest/UserGuide/access_policies.md#policies_session") and [Editing
   IAM policies](../../../IAM/latest/UserGuide/access_policies_manage-edit.md "../../../IAM/latest/UserGuide/access_policies_manage-edit.md") in the _IAM User Guide_.

```
User: arn:aws:iam::`123456789012`:user/`MaryMajor` is not authorized to perform:
s3:GetObject because no session policy allows the s3:GetObject action
```

### Access denied due

to session policies – explicit denial

1. Check for an explicit `Deny` statement for the action in your
   session policies. For the following example, the action is
   `s3:GetObject`.
2. Update your session policy by changing the `Deny` statement to
   allow the user the necessary access. For example, you can update your
   `Deny` statement to use the `aws:PrincipalAccount`
   condition key with the `StringNotEquals` condition operator to
   allow the specific principal access, as shown in [Example 7: Excluding certain
   principals from a Deny statement](amazon-s3-policy-keys.md#example-exclude-principal-from-deny-statement "amazon-s3-policy-keys.md#example-exclude-principal-from-deny-statement"). For more
   information about updating your session policy, see [Session
   policies](../../../IAM/latest/UserGuide/access_policies.md#policies_session "../../../IAM/latest/UserGuide/access_policies.md#policies_session") and [Editing
   IAM policies](../../../IAM/latest/UserGuide/access_policies_manage-edit.md "../../../IAM/latest/UserGuide/access_policies_manage-edit.md") in the _IAM User Guide_.

```
User: arn:aws:iam::`123456789012`:user/`MaryMajor` is not authorized to perform:
s3:GetObject on resource: "arn:aws:s3:::`amzn-s3-demo-bucket1`/`object-name`" with
an explicit deny in a session policy
```

### Access

denied due to resource-based policies – implicit denial

###### Note

_Resource-based policies_ means policies such
as bucket policies and access point policies.

1. Check for a missing `Allow` statement for the action in your
   resource-based policy. Also check whether the `IgnorePublicAcls`
   S3 Block Public Access setting is applied on the bucket, access point, or
   account level. For the following example, the action is
   `s3:GetObject`.
2. Update your policy by adding the `Allow` statement. For more
   information, see [Resource-based policies](../../../IAM/latest/UserGuide/access_policies.md#policies_resource-based "../../../IAM/latest/UserGuide/access_policies.md#policies_resource-based") and [Editing
   IAM policies](../../../IAM/latest/UserGuide/access_policies_manage-edit.md "../../../IAM/latest/UserGuide/access_policies_manage-edit.md") in the _IAM User Guide_.

You might also need to adjust your `IgnorePublicAcls` block
public access setting for the bucket, access point, or account. For more
information, see [Access denied due to Block Public
Access settings](#access-denied-bpa-examples "#access-denied-bpa-examples") and [Configuring block public access
settings for your S3 buckets](configuring-block-public-access-bucket.md "configuring-block-public-access-bucket.md").

```
User: arn:aws:iam::`123456789012`:user/`MaryMajor` is not authorized to perform:
s3:GetObject because no resource-based policy allows the s3:GetObject action
```

### Access

denied due to resource-based policies – explicit denial

###### Note

_Resource-based policies_ means policies such
as bucket policies and access point policies.

1. Check for an explicit `Deny` statement for the action in your
   resource-based policy. Also check whether the
   `RestrictPublicBuckets` S3 Block Public Access setting is
   applied on the bucket, access point, or account level. For the following
   example, the action is `s3:GetObject`.
2. Update your policy by changing the `Deny` statement to allow
   the user the necessary access. For example, you can update your
   `Deny` statement to use the `aws:PrincipalAccount`
   condition key with the `StringNotEquals` condition operator to
   allow the specific principal access, as shown in [Example 7: Excluding certain
   principals from a Deny statement](amazon-s3-policy-keys.md#example-exclude-principal-from-deny-statement "amazon-s3-policy-keys.md#example-exclude-principal-from-deny-statement"). For more
   information about updating your resource-based policy, see [Resource-based policies](../../../IAM/latest/UserGuide/access_policies.md#policies_resource-based "../../../IAM/latest/UserGuide/access_policies.md#policies_resource-based") and [Editing
   IAM policies](../../../IAM/latest/UserGuide/access_policies_manage-edit.md "../../../IAM/latest/UserGuide/access_policies_manage-edit.md") in the _IAM User Guide_.

You might also need to adjust your `RestrictPublicBuckets`
block public access setting for the bucket, access point, or account. For
more information, see [Access denied due to Block Public
Access settings](#access-denied-bpa-examples "#access-denied-bpa-examples") and [Configuring block public access
settings for your S3 buckets](configuring-block-public-access-bucket.md "configuring-block-public-access-bucket.md").

```
User: arn:aws:iam::`123456789012`:user/`MaryMajor` is not authorized to perform:
s3:GetObject on resource: "arn:aws:s3:::`amzn-s3-demo-bucket1`/`object-name`" with
an explicit deny in a resource-based policy
```

### Access

denied due to identity-based policies – implicit denial

1. Check for a missing `Allow` statement for the action in
   identity-based policies attached to the identity. For the following example,
   the action is `s3:GetObject` attached to the user
   `MaryMajor`.
2. Update your policy by adding the `Allow` statement. For more
   information, see [Identity-based policies](../../../IAM/latest/UserGuide/access_policies.md#policies_id-based "../../../IAM/latest/UserGuide/access_policies.md#policies_id-based") and [Editing
   IAM policies](../../../IAM/latest/UserGuide/access_policies_manage-edit.md "../../../IAM/latest/UserGuide/access_policies_manage-edit.md") in the _IAM User Guide_.

```
User: arn:aws:iam::`123456789012`:user/`MaryMajor` is not authorized to perform:
s3:GetObject because no identity-based policy allows the s3:GetObject action
```

### Access

denied due to identity-based policies – explicit denial

1. Check for an explicit `Deny` statement for the action in
   identity-based policies attached to the identity. For the following example,
   the action is `s3:GetObject` attached to the user
   `MaryMajor`.
2. Update your policy by changing the `Deny` statement to allow
   the user the necessary access. For example, you can update your
   `Deny` statement to use the `aws:PrincipalAccount`
   condition key with the `StringNotEquals` condition operator to
   allow the specific principal access, as shown in [aws:PrincipalAccount](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalaccount "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalaccount") in the _IAM User Guide_. For more information, see
   [Identity-based policies](../../../IAM/latest/UserGuide/access_policies.md#policies_id-based "../../../IAM/latest/UserGuide/access_policies.md#policies_id-based") and [Editing
   IAM policies](../../../IAM/latest/UserGuide/access_policies_manage-edit.md "../../../IAM/latest/UserGuide/access_policies_manage-edit.md") in the _IAM User Guide_.

```
User: arn:aws:iam::`123456789012`:user/`MaryMajor` is not authorized to perform:
s3:GetObject on resource: "arn:aws:s3:::`amzn-s3-demo-bucket1`/`object-name`" with
an explicit deny in an identity-based policy
```

### Access denied due to Block Public

Access settings

The Amazon S3 Block Public Access feature provides settings for access points, buckets,
and accounts to help you manage public access to Amazon S3 resources. For more
information about how Amazon S3 defines "public," see [The meaning of
"public"](access-control-block-public-access.md#access-control-block-public-access-policy-status "access-control-block-public-access.md#access-control-block-public-access-policy-status").

By default, new buckets, access points, and objects don't allow public access.
However, users can modify bucket policies, access point policies, IAM user
policies, object permissions, or access control lists (ACLs) to allow public access.
S3 Block Public Access settings override these policies, permissions, and ACLs.
Since April 2023, all Block Public Access settings are enabled by default for new
buckets.

When Amazon S3 receives a request to access a bucket or an object, it determines
whether the bucket or the bucket owner's account has a block public access setting
applied. If the request was made through an access point, Amazon S3 also checks for block
public access settings for the access point. If there is an existing block public
access setting that prohibits the requested access, Amazon S3 rejects the request.

Amazon S3 Block Public Access provides four settings. These settings are independent
and can be used in any combination. Each setting can be applied to an access point,
a bucket, or an entire AWS account. If the block public access settings for the
access point, bucket, or account differ, then Amazon S3 applies the most restrictive
combination of the access point, bucket, and account settings.

When Amazon S3 evaluates whether an operation is prohibited by a block public access
setting, it rejects any request that violates an access point, bucket, or account
setting.

The four settings provided by Amazon S3 Block Public Access are as follows:

- `BlockPublicAcls` – This setting applies to
  `PutBucketAcl`, `PutObjectAcl`,
  `PutObject`, `CreateBucket`,
  `CopyObject`, and `POST Object` requests. The
  `BlockPublicAcls` setting causes the following behavior:

      + `PutBucketAcl` and `PutObjectAcl` calls fail
       if the specified access control list (ACL) is public.
      + `PutObject` calls fail if the request includes a public
       ACL.
      + If this setting is applied to an account, then
       `CreateBucket` calls fail with an HTTP
       `400` (`Bad Request`) response if the
       request includes a public ACL.

  For example, when access is denied for a `CopyObject` request
  because of the `BlockPublicAcls` setting, you receive the
  following message:

```
An error occurred (AccessDenied) when calling the CopyObject operation:
User: arn:aws:sts::`123456789012`:user/`MaryMajor` is not authorized to
perform: s3:CopyObject on resource: "arn:aws:s3:::`amzn-s3-demo-bucket1`/`object-name`"
because public ACLs are prevented by the BlockPublicAcls setting in S3 Block Public Access.
```

- `IgnorePublicAcls` – The `IgnorePublicAcls`
  setting causes Amazon S3 to ignore all public ACLs on a bucket and any objects
  that it contains. If your request's permission is granted only by a public
  ACL, then the `IgnorePublicAcls` setting rejects the
  request.

Any denial resulting from the `IgnorePublicAcls` setting is
implicit. For example, if `IgnorePublicAcls` denies a
`GetObject` request because of a public ACL, you receive the
following message:

```
User: arn:aws:iam::`123456789012`:user/`MaryMajor` is not authorized to perform:
s3:GetObject because no resource-based policy allows the s3:GetObject action
```

- `BlockPublicPolicy` – This setting applies to
  `PutBucketPolicy` and `PutAccessPointPolicy`
  requests.

Setting `BlockPublicPolicy` for a bucket causes Amazon S3 to reject
calls to `PutBucketPolicy` if the specified bucket policy allows
public access. This setting also causes Amazon S3 to reject calls to
`PutAccessPointPolicy` for all of the bucket's same-account
access points if the specified policy allows public access.

Setting `BlockPublicPolicy` for an access point causes Amazon S3 to
reject calls to `PutAccessPointPolicy` and
`PutBucketPolicy` that are made through the access point if
the specified policy (for either the access point or the underlying bucket)
allows public access.

For example, when access is denied on a `PutBucketPolicy`
request because of the `BlockPublicPolicy` setting, you receive
the following message:

```
An error occurred (AccessDenied) when calling the PutBucketPolicy operation:
User: arn:aws:sts::`123456789012`:user/`MaryMajor` is not authorized to
perform: s3:PutBucketPolicy on resource: "arn:aws:s3:::`amzn-s3-demo-bucket1`/`object-name`"
because public policies are prevented by the BlockPublicPolicy setting in S3 Block Public Access.
```

- `RestrictPublicBuckets` – The
  `RestrictPublicBuckets` setting restricts access to an access
  point or bucket with a public policy to only AWS service principals and
  authorized users within the bucket owner's account and the access point
  owner's account. This setting blocks all cross-account access to the access
  point or bucket (except by AWS service principals), while still allowing
  users within the account to manage the access point or bucket. This setting
  also rejects all anonymous (or unsigned) calls.

Any denial resulting from the `RestrictPublicBuckets` setting
is explicit. For example, if `RestrictPublicBuckets` denies a
`GetObject` request because of a public bucket or access
point policy, you receive the following message:

```
User: arn:aws:iam::`123456789012`:user/`MaryMajor` is not authorized to perform:
s3:GetObject on resource: "arn:aws:s3:::`amzn-s3-demo-bucket1`/`object-name`" with
an explicit deny in a resource-based policy
```

For more information about these settings, see [Block public access
settings](access-control-block-public-access.md#access-control-block-public-access-options "access-control-block-public-access.md#access-control-block-public-access-options"). To review and update
these settings, see [Configuring block public
access](access-control-block-public-access.md#configuring-block-public-access "access-control-block-public-access.md#configuring-block-public-access").

## Access denied due to Requester Pays settings

If the Amazon S3 bucket you are trying to access has the Requester Pays feature enabled, you need to make sure you are passing the correct request parameters when making requests to that bucket. The Requester Pays feature in Amazon S3 allows the requester, instead of the bucket owner, to pay the data transfer and request costs for accessing objects in the bucket. When Requester Pays is enabled for a bucket, the bucket owner is not charged for requests made by other AWS accounts.

If you make a request to a Requester Pays-enabled bucket without passing the necessary parameters, you will receive an Access Denied (403 Forbidden) error. To access objects in a Requester Pays-enabled bucket, you must do the following:

1. When making requests using the AWS CLI, you must include the `--request-payer requester` parameter. For example, to copy an object with the key `object.txt` located in the `s3://`amzn-s3-demo-bucket`/` S3 bucket to a location on your local machine, you must also pass the parameter `--request-payer requester` if this bucket has Requester Pays enabled.

```
aws s3 cp s3://`amzn-s3-demo-bucket`/object.txt /local/path \
--request-payer requester
```

2. When making programmatic requests using an AWS SDK, set the `x-amz-request-payer` header to the value `requester`. For an example, see [Downloading objects from Requester Pays
   buckets](ObjectsinRequesterPaysBuckets.md "ObjectsinRequesterPaysBuckets.md").
3. Make sure that the IAM user or role making the request has the necessary permissions to access the Requester Pays bucket, such as the `s3:GetObject` and `s3:ListBucket` permissions.

By including the `--request-payer requester` parameter or setting the `x-amz-request-payer` header, you are informing Amazon S3 that you, the requester, will pay the costs associated with accessing the objects in the Requester Pays-enabled bucket. This will prevent the Access Denied (403 Forbidden) error.

## Bucket policies and IAM policies

### Bucket-level operations

If there is no bucket policy in place, then the bucket implicitly allows requests
from any AWS Identity and Access Management (IAM) identity in the bucket-owner's account. The bucket also
implicitly denies requests from any other IAM identities from any other accounts,
and anonymous (unsigned) requests. However, if there is no IAM user policy in
place, the requester (unless they're the AWS account root user) is implicitly denied
from making any requests. For more information about this evaluation logic, see
[Determining whether a request is denied or allowed within an account](../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md#policy-eval-denyallow "../../../IAM/latest/UserGuide/reference_policies_evaluation-logic.md#policy-eval-denyallow") in
the _IAM User Guide_.

### Object-level operations

If the object is owned by the bucket-owning account, the bucket policy and IAM
user policy will function in the same way for object-level operations as they do for
bucket-level operations. For example, if there is no bucket policy in place, then
the bucket implicitly allows object requests from any IAM identity in the
bucket-owner's account. The bucket also implicitly denies object requests from any
other IAM identities from any other accounts, and anonymous (unsigned) requests.
However, if there is no IAM user policy in place, the requester (unless they're
the AWS account root user) is implicitly denied from making any object
requests.

If the object is owned by an external account, then access to the object can be
granted only through object access control lists (ACLs). The bucket policy and IAM
user policy can still be used to deny object requests.

Therefore, to ensure that your bucket policy or IAM user policy isn't causing an
Access Denied (403 Forbidden) error, make sure that the following requirements are
met:

- For same-account access, there must not be an explicit `Deny`
  statement against the requester you are trying to grant permissions to, in
  either the bucket policy or the IAM user policy. If you want to grant
  permissions by using only the bucket policy and the IAM user policy, there
  must be at least one explicit `Allow` statement in one of these
  policies.
- For cross-account access, there must not be an explicit `Deny`
  statement against the requester that you're trying to grant permissions to,
  in either the bucket policy or the IAM user policy. To grant cross-account
  permissions by using only the bucket policy and IAM user policy, make sure
  that both the bucket policy and the IAM user policy of the requester
  include an explicit `Allow` statement.

###### Note

`Allow` statements in a bucket policy apply only to objects that
are [owned by the
same bucket-owning account](about-object-ownership.md "about-object-ownership.md"). However, `Deny` statements in
a bucket policy apply to all objects regardless of object ownership.

###### To review or edit your bucket

policy

###### Note

To view or edit a bucket policy, you must have the
`s3:GetBucketPolicy` permission.

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**.
3. From the **Buckets** list, choose the name of the bucket that
   you want to view or edit a bucket policy for.
4. Choose the **Permissions** tab.
5. Under **Bucket policy**, choose **Edit**.
   The **Edit bucket policy** page appears.

To review or edit your bucket policy by using the AWS Command Line Interface (AWS CLI), use the [get-bucket-policy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3api/get-bucket-policy.html") command.

###### Note

If you get locked out of a bucket because of an incorrect bucket policy, [sign in to the AWS Management Console by using your AWS account root user
credentials.](../../../signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.md "../../../signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.md") To regain access to your bucket, make sure to delete the
incorrect bucket policy by using your AWS account root user credentials.

### Tips for checking permissions

To check whether the requester has proper permissions to perform an Amazon S3
operation, try the following:

- Identify the requester. If it’s an unsigned request, then it's an
  anonymous request without an IAM user policy. If it’s a request that uses
  a presigned URL, then the user policy is the same as the one for the
  IAM user or role that signed the request.
- Verify that you're using the correct IAM user or role. You can verify
  your IAM user or role by checking the upper-right corner of the AWS Management Console
  or by using the [aws sts
  get-caller-identity](../../../cli/latest/reference/sts/get-caller-identity.md "../../../cli/latest/reference/sts/get-caller-identity.md") command.
- Check the IAM policies that are related to the IAM user or role. You
  can use one of the following methods:
  - [Test IAM policies with the IAM policy
    simulator](../../../IAM/latest/UserGuide/access_policies_testing-policies.md "../../../IAM/latest/UserGuide/access_policies_testing-policies.md").
  - Review the different [IAM policy
    types](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md").

- If needed, [edit your
  IAM user policy](../../../IAM/latest/UserGuide/access_policies_manage-edit.md "../../../IAM/latest/UserGuide/access_policies_manage-edit.md").
- Review the following examples of policies that explicitly deny or allow
  access:
  - Explicit allow IAM user policy: [IAM: Allows and denies access to multiple services
    programmatically and in the console](../../../IAM/latest/UserGuide/reference_policies_examples_iam_multiple-services-console.md "../../../IAM/latest/UserGuide/reference_policies_examples_iam_multiple-services-console.md")
  - Explicit allow bucket policy: [Granting permissions to multiple accounts to upload objects or
    set object ACLs for public access](example-bucket-policies.md#example-bucket-policies-acl-1 "example-bucket-policies.md#example-bucket-policies-acl-1")
  - Explicit deny IAM user policy: [AWS: Denies access to AWS based on the requested
    AWS Region](../../../IAM/latest/UserGuide/reference_policies_examples_aws_deny-requested-region.md "../../../IAM/latest/UserGuide/reference_policies_examples_aws_deny-requested-region.md")
  - Explicit deny bucket policy: [Require SSE-KMS for all objects written to a
    bucket](example-bucket-policies.md#example-bucket-policies-encryption-1 "example-bucket-policies.md#example-bucket-policies-encryption-1")

## Amazon S3 ACL settings

When checking your ACL settings, first [review your Object Ownership
setting](object-ownership-retrieving.md "object-ownership-retrieving.md") to check whether ACLs are enabled on the bucket. Be aware that ACL permissions can be
used only to grant permissions and can't be used to reject requests. ACLs also can't be used to grant
access to requesters that are rejected by explicit denials in bucket policies or IAM user
policies.

### The Object Ownership setting is set to Bucket

owner enforced

If the **Bucket owner enforced** setting is enabled, then ACL settings are
unlikely to cause an Access Denied (403 Forbidden) error because this setting disables all ACLs that
apply to bucket and objects. **Bucket owner enforced** is the default (and
recommended) setting for Amazon S3 buckets.

### The Object Ownership setting is set to

Bucket owner preferred or Object writer

ACL permissions are still valid with the **Bucket owner preferred** setting
or the **Object writer** setting. There are two kinds of ACLs: bucket ACLs and object
ACLs. For the differences between these two types of ACLs, see [Mapping of
ACL permissions and access policy permissions](acl-overview.md#acl-access-policy-permission-mapping "acl-overview.md#acl-access-policy-permission-mapping").

Depending on the action of the rejected request, [check the ACL permissions for
your bucket or the object](managing-acls.md "managing-acls.md"):

- If Amazon S3 rejected a `LIST`, `PUT` object,
  `GetBucketAcl`, or `PutBucketAcl` request, then
  [review the ACL
  permissions for your bucket](managing-acls.md "managing-acls.md").

###### Note

You can't grant `GET` object permissions with bucket ACL
settings.

- If Amazon S3 rejected a `GET` request on an S3 object, or a [PutObjectAcl](../API/API_PutObjectAcl.md "../API/API_PutObjectAcl.md") request, then [review the ACL permissions for the object](managing-acls.md "managing-acls.md").

###### Important

If the account that owns the object is different from the account that
owns the bucket, then access to the object isn't controlled by the
bucket policy.

### Troubleshooting an Access

Denied (403 Forbidden) error from a `GET` object request during
cross-account object ownership

Review the bucket's [Object Ownership settings](about-object-ownership.md#object-ownership-overview "about-object-ownership.md#object-ownership-overview") to determine the object owner. If you have
access to the [object ACLs](managing-acls.md "managing-acls.md"), then you
can also check the object owner's account. (To view the object owner's account,
review the object ACL setting in the Amazon S3 console.) Alternatively, you can also make
a `GetObjectAcl` request to find the object owner’s [canonical
ID](../API/API_GetObjectAcl.md "../API/API_GetObjectAcl.md") to verify the object owner account. By default, ACLs grant explicit
allow permissions for `GET` requests to the object owner’s
account.

After you've confirmed that the object owner is different from the bucket owner,
then depending on your use case and access level, choose one of the following
methods to help address the Access Denied (403 Forbidden) error:

- **Disable ACLs (recommended)** – This method
  will apply to all objects and can be performed by the bucket owner. This method automatically
  gives the bucket owner ownership and full control over every object in the bucket. Before you
  implement this method, check the [prerequisites
  for disabling ACLs](object-ownership-migrating-acls-prerequisites.md "object-ownership-migrating-acls-prerequisites.md"). For information about how to set your bucket to **Bucket
  owner enforced** (recommended) mode, see [Setting Object Ownership
  on an existing bucket](object-ownership-existing-bucket.md "object-ownership-existing-bucket.md").

###### Important

To prevent an Access Denied (403 Forbidden) error, be sure to migrate
the ACL permissions to a bucket policy before you disable ACLs. For more
information, see [Bucket policy examples for migrating from ACL
permissions](object-ownership-migrating-acls-prerequisites.md#migrate-acl-permissions-bucket-policies "object-ownership-migrating-acls-prerequisites.md#migrate-acl-permissions-bucket-policies").

- **Change the object owner to the bucket
  owner** – This method can be applied to individual
  objects, but only the object owner (or a user with the appropriate
  permissions) can change an object's ownership. Additional `PUT`
  costs might apply. (For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").)
  This method grants the bucket owner full ownership of the object, allowing
  the bucket owner to control access to the object through a bucket policy.

To change the object's ownership, do one of the following:

    + You (the bucket owner) can [copy the object](copy-object.md#CopyingObjectsExamples "copy-object.md#CopyingObjectsExamples") back to the bucket.
    + You can change the Object Ownership setting of the bucket to
     **Bucket owner preferred**. If versioning is disabled, the objects in the
     bucket are overwritten. If versioning is enabled, duplicate versions of the same object will
     appear in the bucket, which the bucket owner can [set a lifecycle
     rule to expire](lifecycle-expire-general-considerations.md "lifecycle-expire-general-considerations.md"). For instructions on how to change your Object Ownership setting, see
     [Setting Object Ownership on an
     existing bucket](object-ownership-existing-bucket.md "object-ownership-existing-bucket.md").


    ###### Note

    When you update your Object Ownership setting to **Bucket owner
     preferred**, the setting is applied only to new objects that are uploaded to the
     bucket.
    + You can have the object owner upload the object again with the
     `bucket-owner-full-control` canned object ACL.

###### Note

For cross-account uploads, you can also require the
`bucket-owner-full-control` canned object ACL in your
bucket policy. For an example bucket policy, see [Grant cross-account permissions to upload objects while ensuring
that the bucket owner has full control](example-bucket-policies.md#example-bucket-policies-acl-2 "example-bucket-policies.md#example-bucket-policies-acl-2").

- **Keep the object writer as the object
  owner** – This method doesn't change the object owner,
  but it does allow you to grant access to objects individually. To grant
  access to an object, you must have the `PutObjectAcl` permission
  for the object. Then, to fix the Access Denied (403 Forbidden) error, add
  the requester as a [grantee](acl-overview.md#specifying-grantee "acl-overview.md#specifying-grantee") to access the object in the object's ACLs. For more
  information, see [Configuring ACLs](managing-acls.md "managing-acls.md").

## S3 Block Public Access settings

If the failed request involves public access or public policies, then check the S3
Block Public Access settings on your account, bucket, or access point. For more
information about troubleshooting access denied errors related to S3 Block Public Access
settings, see [Access denied due to Block Public
Access settings](#access-denied-bpa-examples "#access-denied-bpa-examples").

## Amazon S3 encryption settings

Amazon S3 supports server-side encryption on your bucket. Server-side encryption is the
encryption of data at its destination by the application or service that receives it.
Amazon S3 encrypts your data at the object level as it writes it to disks in AWS data
centers and decrypts it for you when you access it.

By default, Amazon S3 now applies server-side encryption with Amazon S3 managed keys (SSE-S3) as
the base level of encryption for every bucket in Amazon S3. Amazon S3 also allows you to specify
the server-side encryption method when uploading objects.

###### To review your bucket's server-side encryption status and encryption

settings

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**.
3. From the **Buckets** list, choose the bucket that you want to
   check the encryption settings for.
4. Choose the **Properties** tab.
5. Scroll down to the **Default encryption** section and view
   the **Encryption type** settings.

To check your encryption settings by using the AWS CLI, use the [get-bucket-encryption](../../../cli/latest/reference/s3api/get-bucket-encryption.md "../../../cli/latest/reference/s3api/get-bucket-encryption.md") command.

###### To check the encryption status of an object

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**.
3. From the **Buckets** list, choose the name of the bucket that
   contains the object.
4. From the **Objects** list, choose the name of the object that
   you want to add or change encryption for.

The object's details page appears. 5. Scroll down to the **Server-side encryption settings**
section to view the object's server-side encryption settings.

To check your object encryption status by using the AWS CLI, use the [head-object](../../../cli/latest/reference/s3api/head-object.md#examples "../../../cli/latest/reference/s3api/head-object.md#examples") command.

### Encryption and

permissions requirements

Amazon S3 supports three types of server-side encryption:

- Server-side encryption with Amazon S3 managed keys (SSE-S3)
- Server-side encryption with AWS Key Management Service (AWS KMS) keys (SSE-KMS)
- Server-side encryption with customer-provided keys (SSE-C)

Based on your encryption settings, make sure that the following permissions
requirements are met:

- **SSE-S3** – No extra permissions are
  required.
- **SSE-KMS (with a customer managed key)** – To
  upload objects, the `kms:GenerateDataKey` permission on the
  AWS KMS key is required. To download objects and perform multipart
  uploads of objects, the `kms:Decrypt` permission on the KMS key
  is required.
- **SSE-KMS (with an AWS managed key)**
  – The requester must be from the same account that owns the
  `aws/s3` KMS key. The requester must also have the correct
  Amazon S3 permissions to access the object.
- **SSE-C (with a customer provided key)**
  – No additional permissions are required. You can configure the
  bucket policy to [require and restrict server-side encryption with customer-provided encryption keys](ServerSideEncryptionCustomerKeys.md#ssec-require-condition-key "ServerSideEncryptionCustomerKeys.md#ssec-require-condition-key") for objects in your bucket.

If the object is encrypted with a customer managed key, make sure that the KMS key policy
allows you to perform the `kms:GenerateDataKey` or
`kms:Decrypt` actions. For instructions on checking your KMS key
policy, see [Viewing a key
policy](../../../kms/latest/developerguide/key-policy-viewing.md "../../../kms/latest/developerguide/key-policy-viewing.md") in the _AWS Key Management Service Developer Guide_.

## S3 Object Lock settings

If your bucket has [S3 Object Lock](object-lock.md "object-lock.md") enabled and the object is protected by a [retention
period](object-lock-overview.md#object-lock-retention-periods "object-lock-overview.md#object-lock-retention-periods") or [legal hold](object-lock-overview.md#object-lock-legal-holds "object-lock-overview.md#object-lock-legal-holds")
and you try to delete an object, Amazon S3 returns one of the following responses, depending on how you tried
to delete the object:

- **Permanent `DELETE` request** – If you issued a
  permanent `DELETE` request (a request that specifies a version ID), Amazon S3 returns an
  Access Denied (`403 Forbidden`) error when you try to delete the object.
- **Simple `DELETE` request** – If you issued a
  simple `DELETE` request (a request that doesn't specify a version ID), Amazon S3 returns a
  `200 OK` response and inserts a [delete marker](DeleteMarker.md "DeleteMarker.md") in
  the bucket, and that marker becomes the current version of the object with a new ID.

###### To check whether the bucket has Object Lock enabled

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**.
3. From the **Buckets** list, choose the name of the bucket that
   you want to review.
4. Choose the **Properties** tab.
5. Scroll down to the **Object Lock** section. Verify whether
   the **Object Lock** setting is **Enabled** or
   **Disabled**.

To determine whether the object is protected by a retention period or legal hold,
[view the lock information](object-lock-managing.md#object-lock-managing-view "object-lock-managing.md#object-lock-managing-view") for your object.

If the object is protected by a retention period or legal hold, check the
following:

- If the object version is protected by the compliance retention mode, there is
  no way to permanently delete it. A permanent `DELETE` request from
  any requester, including the AWS account root user, will result in an Access
  Denied (403 Forbidden) error. Also, be aware that when you submit a
  `DELETE` request for an object that's protected by the compliance
  retention mode, Amazon S3 creates a [delete marker](DeleteMarker.md "DeleteMarker.md") for
  the object.
- If the object version is protected with governance retention mode and you have
  the `s3:BypassGovernanceRetention` permission, you can bypass the
  protection and permanently delete the version. For more information, see [Bypassing governance mode](object-lock-managing.md#object-lock-managing-bypass "object-lock-managing.md#object-lock-managing-bypass").
- If the object version is protected by a legal hold, then a permanent
  `DELETE` request can result in an Access Denied (403 Forbidden)
  error. To permanently delete the object version, you must remove the legal hold
  on the object version. To remove a legal hold, you must have the
  `s3:PutObjectLegalHold` permission. For more information about
  removing a legal hold, see [Configuring S3 Object Lock](object-lock-configure.md "object-lock-configure.md").

## VPC endpoint policies

If you're accessing Amazon S3 by using a virtual private cloud (VPC) endpoint, make sure
that the VPC endpoint policy isn't blocking you from accessing your Amazon S3 resources. By
default, the VPC endpoint policy allows all requests to Amazon S3. You can also configure
the VPC endpoint policy to restrict certain requests. For information about how to
check your VPC endpoint policy, see the following resources:

- [Access denied due to
  a VPC endpoint policy – implicit denial](#access-denied-vpc-endpoint-examples-implicit "#access-denied-vpc-endpoint-examples-implicit")
- [Access denied due to
  a VPC endpoint policy – explicit denial](#access-denied-vpc-endpoint-examples-explicit "#access-denied-vpc-endpoint-examples-explicit")
- [Control access to
  VPC endpoints by using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _AWS PrivateLink Guide_

## AWS Organizations policies

If your AWS account belongs to an organization, AWS Organizations policies can block you from accessing
Amazon S3 resources. By default, AWS Organizations policies don't block any requests to Amazon S3. However, make sure that
your AWS Organizations policies haven't been configured to block access to S3 buckets. For instructions on how to
check your AWS Organizations policies, see the following resources:

- [Access denied due to a Service
  Control Policy – implicit denial](#access-denied-scp-examples-implicit "#access-denied-scp-examples-implicit")
- [Access denied due to a Service
  Control Policy – explicit denial](#access-denied-scp-examples-explicit "#access-denied-scp-examples-explicit")
- [Access denied due to a resource
  control policy – explicit denial](#access-denied-rcp-examples-explicit "#access-denied-rcp-examples-explicit")
- [Listing all policies](../../../organizations/latest/userguide/orgs_manage_policies_info-operations.md#list-all-pols-in-org "../../../organizations/latest/userguide/orgs_manage_policies_info-operations.md#list-all-pols-in-org") in the _AWS Organizations User
  Guide_

Additionally, if you incorrectly configured your bucket policy for a member account to deny all
users access to your S3 bucket, you can unlock the bucket by launching a privileged session for the
member account in IAM. After you launch a privileged session, you can delete the misconfigured bucket
policy to regain access to the bucket. For more information, see [Perform a privileged
task on an AWS Organizations member account](../../../IAM/latest/UserGuide/id_root-user-privileged-task.md "../../../IAM/latest/UserGuide/id_root-user-privileged-task.md") in the _AWS Identity and Access Management User
Guide_.

## CloudFront distribution access

If you receive a Access Denied (403 Forbidden) error when trying to access your S3 static website through CloudFront, check these common issues:

- **Do you have the correct origin domain name format?**
  - Make sure you're using the S3 website endpoint format (bucket-name.s3-website-region.amazonaws.com) rather than the REST API endpoint
  - Verify that static website hosting is enabled on your bucket

- **Does your bucket policy allow CloudFront access?**
  - Ensure your bucket policy includes permissions for your CloudFront distribution's Origin Access Identity (OAI) or Origin Access Control (OAC)
  - Verify the policy includes the required s3:GetObject permissions

For additional troubleshooting steps and configurations, including error page setups and protocol settings, see [Why do I get a "403 access denied" error when I use an Amazon S3 website endpoint as the origin of my CloudFront distribution?](https://repost.aws/knowledge-center/s3-website-cloudfront-error-403 "https://repost.aws/knowledge-center/s3-website-cloudfront-error-403") in the AWS re:Post Knowledge Center.

###### Note

This error is different from 403 errors you might receive when accessing S3 directly. For CloudFront-specific issues, make sure to check both your CloudFront distribution settings and S3 configurations.

## Access point settings

If you receive an Access Denied (403 Forbidden) error while making requests through
Amazon S3 access points, you might need to check the following:

- The configurations for your access points
- The IAM user policy that's used for your access points
- The bucket policy that's used to manage or configure your cross-account
  access points

###### Access point configurations and policies

- When you create an access point, you can choose to designate
  **Internet** or **VPC** as the network
  origin. If the network origin is set to VPC only, Amazon S3 will reject any
  requests made to the access point that don't originate from the specified VPC. To
  check the network origin of your access point, see [Creating access points restricted to a virtual private
  cloud](access-points-vpc.md "access-points-vpc.md").
- With access points, you can also configure custom Block Public Access settings, which
  work similarly to the Block Public Access settings at the bucket or account
  level. To check your custom Block Public Access settings, see [Managing public access to access points for general purpose buckets](access-points-bpa-settings.md "access-points-bpa-settings.md").
- To make successful requests to Amazon S3 by using access points, make sure that the
  requester has the necessary IAM permissions. For more information, see [Configuring IAM policies for using access points](access-points-policies.md "access-points-policies.md").
- If the request involves cross-account access points, make sure that the bucket
  owner has updated the bucket policy to authorize requests from the access point. For
  more information, see [Granting permissions for cross-account access points](access-points-policies.md#access-points-cross-account "access-points-policies.md#access-points-cross-account").

If the Access Denied (403 Forbidden) error still persists after checking all the items
in this topic, [retrieve your Amazon S3 request
ID](get-request-ids.md "get-request-ids.md") and contact Support for additional guidance.

## Additional resources

For more guidance on Access Denied (403 Forbidden) errors you can check the following resources:

- [How do I troubleshoot 403 Access Denied errors from Amazon S3?](https://repost.aws/knowledge-center/s3-troubleshoot-403 "https://repost.aws/knowledge-center/s3-troubleshoot-403") in the AWS re:Post Knowledge Center.
- [Why do I get a 403 Forbidden error when I try to access an Amazon S3 bucket or object?](https://repost.aws/knowledge-center/s3-403-forbidden-error "https://repost.aws/knowledge-center/s3-403-forbidden-error") in the AWS re:Post Knowledge Center.
- [Why do I get an Access Denied error when I try to access an Amazon S3 resource in the same AWS account?](https://repost.aws/knowledge-center/s3-troubleshoot-403-resource-same-account "https://repost.aws/knowledge-center/s3-troubleshoot-403-resource-same-account") in the AWS re:Post Knowledge Center.
- [Why do I get an Access Denied error when I try to access an Amazon S3 bucket with public read access?](https://repost.aws/knowledge-center/s3-troubleshoot-403-public-read "https://repost.aws/knowledge-center/s3-troubleshoot-403-public-read") in the AWS re:Post Knowledge Center.
- [Why do I get a "signature mismatch" error when I try to use a presigned URL to upload an object to Amazon S3?](https://repost.aws/knowledge-center/s3-presigned-url-signature-mismatch "https://repost.aws/knowledge-center/s3-presigned-url-signature-mismatch") in the AWS re:Post Knowledge Center.
- [Why do I get an Access Denied error for ListObjectsV2 when I run the sync command on my Amazon S3 bucket?](https://repost.aws/knowledge-center/s3-access-denied-listobjects-sync "https://repost.aws/knowledge-center/s3-access-denied-listobjects-sync") in the AWS re:Post Knowledge Center.
- [Why do I get a "403 access denied" error when I use an Amazon S3 website endpoint as the origin of my CloudFront distribution?](https://repost.aws/knowledge-center/s3-website-cloudfront-error-403 "https://repost.aws/knowledge-center/s3-website-cloudfront-error-403") in the AWS re:Post Knowledge Center.
