Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Overview of managing access permissions

to your Amazon Redshift resources

Every AWS resource is owned by an AWS account, and permissions to create or access the
resources are governed by permissions policies. An account administrator can attach
permissions policies to IAM identities (that is, users, groups, and roles), and some
services (such as AWS Lambda) also support attaching permissions policies to resources.

###### Note

An _account administrator_ (or administrator user) is a user with
administrator privileges. For more information, see [IAM best practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the
_IAM User Guide_.

When granting permissions, you decide who is getting the permissions, which resources they
get permissions for, and the specific actions that you want to allow on those resources.

## Amazon Redshift resources and

operations

Amazon Redshift provides service-specific resources, actions, and condition context keys for use in
IAM permission policies.

### Amazon Redshift, Amazon Redshift Serverless,

Amazon Redshift Data API, and Amazon Redshift query editor v2 access permissions

When you set up [Access control](redshift-iam-authentication-access-control.md#redshift-iam-accesscontrol "redshift-iam-authentication-access-control.md#redshift-iam-accesscontrol"), you write permission policies that you can
attach to an IAM identity (identity-based policies). For detailed reference information,
see the following topics in the _Service Authorization Reference_:

- For Amazon Redshift, see [Actions,
  resources, and condition keys for Amazon Redshift](../../../service-authorization/latest/reference/list_amazonredshift.md "../../../service-authorization/latest/reference/list_amazonredshift.md") that use the `redshift:`
  prefix.
- For Amazon Redshift Serverless, see [Actions, resources, and condition keys for Amazon Redshift Serverless](../../../service-authorization/latest/reference/list_amazonredshiftserverless.md "../../../service-authorization/latest/reference/list_amazonredshiftserverless.md") that use the
  `redshift-serverless:` prefix.
- For Amazon Redshift Data API, see [Actions, resources, and condition keys for Amazon Redshift Data API](../../../service-authorization/latest/reference/list_amazonredshiftdataapi.md "../../../service-authorization/latest/reference/list_amazonredshiftdataapi.md") that use the
  `redshift-data:` prefix.
- For Amazon Redshift query editor v2, see [Actions,
  resources, and condition keys for AWS SQL Workbench (Amazon Redshift query editor v2)](../../../service-authorization/latest/reference/list_awssqlworkbench.md "../../../service-authorization/latest/reference/list_awssqlworkbench.md") that use
  the `sqlworkbench:` prefix.

The query editor v2 includes permission-only actions that don't directly correspond to an
API operation. These actions are indicated in the
_Service Authorization Reference_ with `[permission only]`.

The _Service Authorization Reference_ contains information about which API
operations can be used in an IAM policy. It also includes the AWS resource for which
you can grant the permissions, and condition keys that you can include for fine-grained
access control. For more information about conditions, see [Using IAM policy conditions for
fine-grained access control](#redshift-policy-resources.conditions "#redshift-policy-resources.conditions").

You specify the actions in the policy's `Action` field, the resource value
in the policy's `Resource` field, and conditions in the policy's
`Condition` field. To specify an action for Amazon Redshift, use the
`redshift:` prefix followed by the API operation name (for example,
`redshift:CreateCluster`).

## Understanding resource

ownership

A _resource owner_ is the AWS account that created a resource. That
is, the resource owner is the AWS account of the _principal entity_
(the root account, an IAM user, or an IAM role) that authenticates the request that
creates the resource. The following examples illustrate how this works:

- If you use the root account credentials of your AWS account to create a DB
  cluster, your AWS account is the owner of the Amazon Redshift resource.
- If you create an IAM role in your AWS account with permissions to create
  Amazon Redshift resources, anyone who can assume the role can create Amazon Redshift resources. Your
  AWS account, to which the role belongs, owns the Amazon Redshift resources.
- If you create an IAM user in your AWS account and grant permissions to create
  Amazon Redshift resources to that user, the user can create Amazon Redshift resources. However, your
  AWS account, to which the user belongs, owns the Amazon Redshift resources. In most cases
  this method isn't recommended. We recommend creating an IAM role and attaching
  permissions to the role, then assigning the role to a user.

## Managing access to

resources

A _permissions policy_ describes who has access to what. The
following section explains the available options for creating permissions policies.

###### Note

This section discusses using IAM in the context of Amazon Redshift. It doesn't provide
detailed information about the IAM service. For complete IAM documentation, see [What is IAM?](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") in the
_IAM User Guide_. For information about IAM policy syntax and
descriptions, see [AWS IAM policy
reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md") in the _IAM User Guide_.

Policies attached to an IAM identity are referred to as
_identity-based_ policies (IAM policies) and policies attached to a
resource are referred to as _resource-based_ policies. Amazon Redshift supports
only identity-based policies (IAM policies).

### Identity-based policies (IAM

policies)

You can assign permissions by attaching polices to an IAM role and then assigning
that role to a user or group. The following is an example policy that containing
permissions to create, delete, modify, and reboot Amazon Redshift clusters for your AWS
account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid":"AllowManageClusters",
 "Effect":"Allow",
 "Action": [
 "redshift:CreateCluster",
 "redshift:DeleteCluster",
 "redshift:ModifyCluster",
 "redshift:RebootCluster"
 ],
 "Resource":"*"
 }
 ]
}`

```

For more information about using identity-based policies with Amazon Redshift, see [Using identity-based policies
(IAM policies) for Amazon Redshift](redshift-iam-access-control-identity-based.md "redshift-iam-access-control-identity-based.md"). For more information about
users, groups, roles, and permissions, see [Identities
(users, groups, and roles)](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md") in the _IAM User Guide_.

### Resource-based

policies

Other services, such as Amazon S3, also support resource-based permissions policies. For
example, you can attach a policy to an S3 bucket to manage access permissions to that
bucket. Amazon Redshift doesn't support resource-based policies.

## Specifying policy elements:

Actions, effects, resources, and principals

For each Amazon Redshift resource (see [Amazon Redshift resources and
operations](#redshift-iam-accesscontrol.actions-and-resources "#redshift-iam-accesscontrol.actions-and-resources")), the service defines a
set of API operations (see [Actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md")). To
grant permissions for these API operations, Amazon Redshift defines a set of actions that you can
specify in a policy. Performing an API operation can require permissions for more than one
action.

The following are the basic policy elements:

- **Resource** – In a policy, you use an Amazon
  Resource Name (ARN) to identify the resource to which the policy applies. For more
  information, see [Amazon Redshift resources and
  operations](#redshift-iam-accesscontrol.actions-and-resources "#redshift-iam-accesscontrol.actions-and-resources").
- **Action** – You use action keywords to identify
  resource operations that you want to allow or deny. For example, the
  `redshift:DescribeClusters` permission allows the user permissions to
  perform the Amazon Redshift `DescribeClusters` operation.
- **Effect** – You specify the effect when the user
  requests the specific action—this can be either allow or deny. If you don't
  explicitly grant access to (allow) a resource, access is implicitly denied. You can also
  explicitly deny access to a resource, which you might do to make sure that a user cannot
  access it, even if a different policy grants access.
- **Principal** – In identity-based policies (IAM
  policies), the user that the policy is attached to is the implicit principal. For
  resource-based policies, you specify the user, account, service, or other entity that
  you want to receive permissions (applies to resource-based policies only). Amazon Redshift
  doesn't support resource-based policies.

To learn more about IAM policy syntax and descriptions, see [AWS IAM policy reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md") in the
_IAM User Guide_.

For a table showing all of the Amazon Redshift API actions and the resources that they apply
to, see [Amazon Redshift, Amazon Redshift Serverless,
Amazon Redshift Data API, and Amazon Redshift query editor v2 access permissions](#redshift-policy-resources.resource-permissions "#redshift-policy-resources.resource-permissions").

## Specifying conditions in a

policy

When you grant permissions, you can use the access policy language to specify the
conditions when a policy should take effect. For example, you might want a policy to be
applied only after a specific date. For more information about specifying conditions in an
access policy language, see [IAM JSON policy elements:
Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.

To identify conditions where a permissions policy applies, include a
`Condition` element in your IAM permissions policy. For example, you can
create a policy that permits a user to create a cluster using the
`redshift:CreateCluster` action, and you can add a `Condition`
element to restrict that user to only create the cluster in a specific region. For details,
see [Using IAM policy conditions for
fine-grained access control](#redshift-policy-resources.conditions "#redshift-policy-resources.conditions"). For a list showing all of
condition key values and the Amazon Redshift actions and resources that they apply to, see [Amazon Redshift, Amazon Redshift Serverless,
Amazon Redshift Data API, and Amazon Redshift query editor v2 access permissions](#redshift-policy-resources.resource-permissions "#redshift-policy-resources.resource-permissions").

### Using IAM policy conditions for

fine-grained access control

In Amazon Redshift, you can use condition keys to restrict access to resources based on the tags
for those resources. The following are common Amazon Redshift condition keys.

| Condition key     | Description                                                                                                                                                                                                                                                                                                                                                |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `aws:RequestTag`  | Requires users to include a tag key (name) and value whenever they<br>create a resource. For more information, see [aws:RequestTag](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-requesttag") in the _IAM User Guide_.  |
| `aws:ResourceTag` | Restricts user access to resources based on specific tag keys and<br>values. For more information, see [aws:ResourceTag](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-resourcetag") in the _IAM User Guide_.           |
| `aws:TagKeys`     | Use this key to compare the tag keys in a request with the keys that<br>you specify in the policy. For more information, see [aws:TagKeys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-tagkeys") in the _IAM User Guide_. |

For information on tags, see [Tag resources in Amazon Redshift](amazon-redshift-tagging.md "amazon-redshift-tagging.md").

For a list of the API actions that support the `redshift:RequestTag` and
`redshift:ResourceTag` condition keys, see [Amazon Redshift, Amazon Redshift Serverless,
Amazon Redshift Data API, and Amazon Redshift query editor v2 access permissions](#redshift-policy-resources.resource-permissions "#redshift-policy-resources.resource-permissions").

The following condition keys can be used with the Amazon Redshift GetClusterCredentials
action.

| Condition key              | Description                                                      |
| -------------------------- | ---------------------------------------------------------------- |
| `redshift:DurationSeconds` | Limits the number of seconds that can be specified for duration. |
| `redshift:DbName`          | Restricts database names that can be specified.                  |
| `redshift:DbUser`          | Restricts database user names that can be specified.             |

#### Example 1:

Restricting access by using the aws:ResourceTag condition key

Use the following IAM policy to let a user modify an Amazon Redshift cluster only for a
specific AWS account in the `us-west-2` region with a tag named
`environment` with a tag value of `test`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Sid":"AllowModifyTestCluster",
 "Effect": "Allow",
 "Action": "redshift:ModifyCluster",
 "Resource": "arn:aws:redshift:us-west-2:123456789012:cluster:*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/environment": "test"
 }
 }
 }
}`

```

#### Example 2:

Restricting access by using the aws:RequestTag condition key

Use the following IAM policy to let a user create an Amazon Redshift cluster only if the
command to create the cluster includes a tag named `usage` and a tag value of
`production`. The condition with `aws:TagKeys` and the
`ForAllValues` modifier specifies that only the keys
`costcenter` and `usage` can be specified in the request.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Sid":"AllowCreateProductionCluster",
 "Effect": "Allow",
 "Action": [
 "redshift:CreateCluster",
 "redshift:CreateTags"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestTag/usage": "production"
 },
 "ForAllValues:StringEquals": {
 "aws:TagKeys": [
 "costcenter",
 "usage"
 ]
 }
 }
 }
}`

```
