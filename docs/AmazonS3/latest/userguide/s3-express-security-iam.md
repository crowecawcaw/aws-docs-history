# Authorizing Regional endpoint API operations with IAM

AWS Identity and Access Management (IAM) is an AWS service that helps administrators securely control access to
AWS resources. IAM administrators control who can be authenticated (signed in) and
authorized (have permissions) to use Amazon S3 resources in directory buckets and S3 Express One Zone operations. You can use IAM for no
additional charge.

By default, users don't have permissions for directory buckets. To grant access permissions for directory buckets, you can use IAM to create
users, groups, or roles and attach permissions to those identities. For more information
about IAM, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

To provide access, you can add permissions to your users, groups, or roles through the
following means:

- **Users and groups in AWS IAM Identity Center** – Create a
  permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User
  Guide_.
- **Users managed in IAM through an identity
  provider** – Create a role for identity federation. Follow the
  instructions in [Creating a role for a
  third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md") in the _IAM User Guide_.
- **IAM roles and users** – Create a role that
  your user can assume. Follow the instructions in [Creating a role to
  delegate permissions to an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  For more information about IAM for S3 Express One Zone, see the following topics.

###### Topics

- [Principals](#s3-express-security-iam-principals "#s3-express-security-iam-principals")
- [Resources](#s3-express-security-iam-resources "#s3-express-security-iam-resources")
- [Actions for directory buckets](#s3-express-security-iam-actions "#s3-express-security-iam-actions")
- [IAM identity-based policies
  for directory buckets](s3-express-security-iam-identity-policies.md "s3-express-security-iam-identity-policies.md")
- [Example bucket
  policies for directory buckets](s3-express-security-iam-example-bucket-policies.md "s3-express-security-iam-example-bucket-policies.md")

## Principals

When you create a resource-based policy to grant access to your buckets, you must use
the `Principal` element to specify the person or application that can make a
request for an action or operation on that resource. For directory bucket policies, you
can use the following principals:

- An AWS account
- An IAM user
- An IAM role
- A federated user

For more information, see [Principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in the _IAM User
Guide_.

## Resources

Amazon Resource Names (ARNs) for directory buckets contain the `s3express`
namespace, the AWS Region, the AWS account ID, and the directory bucket name,
which includes the AWS Zone ID. (an Availability Zone or Local Zone ID).

To access and perform actions on your
directory bucket, you must use the following ARN format:

```
arn:aws:s3express:`region`:`account-id`:bucket/`base-bucket-name`--`zone-id`--x-s3
```

To access and perform actions on your access point for a directory bucket, you must use the following ARN format:

```
arn:aws::s3express:`region`:`account-id`:accesspoint/`accesspoint-basename`--`zone-id`--xa-s3
```

For more information about ARNs, see [Amazon Resource Names (ARNs)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md") in the _IAM User Guide_. For more information about resources, see
[IAM JSON
Policy Elements: Resource](../../../IAM/latest/UserGuide/reference_policies_elements_resource.md "../../../IAM/latest/UserGuide/reference_policies_elements_resource.md") in the _IAM User Guide_.

## Actions for directory buckets

In an IAM identity-based policy or resource-based policy, you define which S3
actions are allowed or denied. Actions correspond to specific API
operations. With directory buckets, you must use the S3 Express One Zone namespace to grant permissions, called `s3express`.

When you allow the `s3express:CreateSession` permission, the
`CreateSession` API operation retrieves a temporary session token for all
Zonal endpoint API (object level) operations. The session token returns
credentials that are used for all other Zonal endpoint API
operations. As a result, you don't grant access permissions to Zonal API
operations with IAM policies. Instead, `CreateSession` enables access for all object level operations.
For the list of Zonal API operations and permissions, see
[Authenticating and authorizing requests](s3-express-authenticating-authorizing.md "s3-express-authenticating-authorizing.md").

To learn more
about the `CreateSession` API operation, see [CreateSession](../API/API_CreateSession.md "../API/API_CreateSession.md") in the _Amazon Simple Storage Service API Reference_.

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS.
When you use an action in a policy, you usually allow or deny access to the API
operation with the same name. However, in some cases, a single action controls access to
more than one API operation. Access to bucket-level actions can be granted in only IAM
identity-based policies (user or role) and not bucket policies.

For more information about how to configure access point policies, see [Configuring IAM policies for using access points for directory buckets](access-points-directory-buckets-policies.md "access-points-directory-buckets-policies.md").

For more information, see [Actions, resources, and condition keys for Amazon S3 Express](../../../service-authorization/latest/reference/list_amazons3express.md "../../../service-authorization/latest/reference/list_amazons3express.md").
