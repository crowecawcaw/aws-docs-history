# Access control

To create, update, delete, or list AWS Data Exchange resources, you need permissions to perform
the operation and to access the corresponding resources. To perform the operation
programmatically, you also need valid access keys.

## Overview of managing access permissions to

your AWS Data Exchange resources

Every AWS resource is owned by an AWS account, and permissions to create or
access a resource are governed by permissions policies. An account administrator can
attach permissions policies to users, groups, and roles. Some services (such as
AWS Lambda) also support attaching permissions policies to resources.

###### Note

An _account administrator_ (or administrator) is a user
with administrator privileges. For more information, see [IAM Best Practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md").

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

###### Topics

- [AWS Data Exchange resources and
  operations](#access-control-resources "#access-control-resources")
- [Understanding resource ownership](#access-control-owner "#access-control-owner")
- [Managing access to
  resources](#access-control-manage-access-intro "#access-control-manage-access-intro")
- [Specifying policy
  elements: actions, effects, and principals](#access-control-specify-control-tower-actions "#access-control-specify-control-tower-actions")
- [Specifying conditions in a
  policy](#specifying-conditions "#specifying-conditions")

### AWS Data Exchange resources and

operations

In AWS Data Exchange, there are two different kinds of primary resources with different
control planes:

- The primary resources for AWS Data Exchange are _data sets_ and
  _jobs_. AWS Data Exchange also supports
  _revisions_ and
  _assets_.
- To facilitate transactions between providers and subscribers, AWS Data Exchange
  also uses AWS Marketplace concepts and resources, including products, offers, and
  subscriptions. You can use the AWS Marketplace Catalog API or the AWS Data Exchange console to
  manage your products, offers, subscription requests, and
  subscriptions.

### Understanding resource ownership

The AWS account owns the resources that are created in the account,
regardless of who created the resources. Specifically, the resource owner is the
AWS account of the [principal entity](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md") (that is, the AWS account root user, a user, or
a role) that authenticates the resource creation request. The following examples
illustrate how this works.

#### Resource ownership

Any IAM entity in an AWS account with the correct permissions can
create AWS Data Exchange data sets. When an IAM entity creates a data set, their
AWS account owns the data set. Published data products can contain data
sets that are owned only by the AWS account that created them.

To subscribe to an AWS Data Exchange product, the IAM entity needs permissions to
use AWS Data Exchange, in addition to the `aws-marketplace:subscribe`,
`aws-marketplace:aws-marketplace:CreateAgreementRequest`, and
`aws-marketplace:AcceptAgreementRequest` IAM permissions
for AWS Marketplace (assuming they pass any related subscription verifications). As a
subscriber, your account has read access to entitled data sets; however, it
does not own the entitled data sets. Any entitled data sets that are
exported to Amazon S3 are owned by the subscriber's AWS account.

### Managing access to

resources

This section discusses using IAM in the context of AWS Data Exchange. It doesn't provide
detailed information about the IAM service. For complete IAM documentation,
see [What Is IAM?](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") in the
_IAM User Guide_. For information about IAM policy
syntax and descriptions, see [AWS Identity and Access Management Policy Reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md") in the
_IAM User Guide_.

A _permissions policy_ describes who has access to what.
The following section explains the options for creating permissions
policies.

Policies attached to an IAM identity are referred to as
_identity-based_ policies (IAM policies). Policies
attached to a resource are referred to as _resource-based_
policies. AWS Data Exchange supports only identity-based policies (IAM policies).

###### Topics

- [Identity-based policies and permissions](#access-control-manage-access-intro-iam-policies "#access-control-manage-access-intro-iam-policies")
- [Resource-based policies](#access-control-manage-access-intro-resource-policies "#access-control-manage-access-intro-resource-policies")

#### Identity-based policies and permissions

AWS Data Exchange provides a set of managed policies. For more information about them
and their permissions, see [AWS managed policies for AWS Data Exchange](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

##### Amazon S3 permissions

When importing assets from Amazon S3 to AWS Data Exchange, you need permissions to
write to the AWS Data Exchange service S3 buckets. Similarly, when exporting assets
from AWS Data Exchange to Amazon S3, you need permissions to read from the AWS Data Exchange service
S3 buckets. These permissions are included in the policies mentioned
previously, but you can also create your own policy to allow just what
you want your users to be able to do. You can scope these permissions to
buckets that contain `aws-data-exchange` in their name and
use the [CalledVia](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-calledvia "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-calledvia") permission to restrict the usage of the
permission to requests made by AWS Data Exchange on behalf of the principal.

For example, you could create a policy to allow importing and
exporting to AWS Data Exchange that includes these permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "s3:GetObject",
 "Resource": "arn:aws:s3:::*aws-data-exchange*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": [
 "dataexchange.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject",
 "s3:PutObjectAcl"
 ],
 "Resource": "arn:aws:s3:::*aws-data-exchange*",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "aws:CalledVia": [
 "dataexchange.amazonaws.com"
 ]
 }
 }
 }
 ]
}`

```

These permissions allow providers to import and export with AWS Data Exchange. The
policy includes the following permissions and restrictions:

- **s3:PutObject** and **s3:PutObjectAcl** – These
  permissions are restricted only to S3 buckets that contain
  `aws-data-exchange` in their name. These
  permissions allows providers to write to AWS Data Exchange service buckets
  when importing from Amazon S3.
- **s3:GetObject** – This
  permission is restricted to S3 buckets that contain
  `aws-data-exchange` in their name. This
  permission allows customers to read from AWS Data Exchange service buckets
  when exporting from AWS Data Exchange to Amazon S3.
- These permissions are restricted to requests made by using
  AWS Data Exchange with the IAM `CalledVia` condition. This
  allows the S3 `PutObject` permissions to only be used
  in the context of the AWS Data Exchange console or API.
- **AWS Lake Formation** **and**
  **AWS Resource Access Manager**
  **(AWS RAM)**
  **–** To use AWS Lake Formation data sets you'll
  need to accept the AWS RAM share invitation for each net new
  provider that you have a subscription with. In order to accept
  the AWS RAM share invitation you will need to assume a role that
  has permission to accept a AWS RAM share invitation. To learn more
  about how AWS managed policies for AWS RAM, see [Managed policies for AWS RAM.](../../../ram/latest/userguide/security-iam-managed-policies.md "../../../ram/latest/userguide/security-iam-managed-policies.md")
- To create AWS Lake Formation data sets, you'll need to create the data
  set with an assumed role that allows IAM to pass a role to
  AWS Data Exchange. This will allow AWS Data Exchange to grant and revoke
  permissions to Lake Formation resources on your behalf. See an example
  policy below:

```
{
    "Effect": "Allow",
    "Action": "iam:PassRole",
    "Resource": "*",
    "Condition": {
        "StringEquals": {
             "iam:PassedToService": "dataexchange.amazonaws.com"
        }
    }
}
```

###### Note

Your users may also need additional permissions to read to or
write from your own S3 buckets and objects that are not covered in
this example.

For more information about users, groups, roles, and permissions, see
[Identities (Users, Groups, and
Roles)](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md") in the _IAM User Guide_.

#### Resource-based policies

AWS Data Exchange does not support resource-based policies.

Other services, such as Amazon S3, do support resource-based permissions
policies. For example, you can attach a policy to an S3 bucket to manage
access permissions to that bucket.

### Specifying policy

elements: actions, effects, and principals

To use AWS Data Exchange, your user permissions must be defined in an IAM policy.

The following are the most basic policy elements:

- **Resource** – In a policy, you
  use an Amazon Resource Name (ARN) to identify the resource to which the
  policy applies. All AWS Data Exchange API operations support resource level
  permissions (RLP), but AWS Marketplace actions don't support RLP. For more
  information, see [AWS Data Exchange resources and
  operations](#access-control-resources "#access-control-resources").
- **Action** – You use action
  keywords to identify resource operations that you want to allow or
  deny.
- **Effect** – You specify the
  effect (allow or deny) when the user requests the specific action. If
  you don't explicitly grant access to (allow) a resource, access is
  implicitly denied. You can also explicitly deny access to a resource,
  which you might do to make sure that a user cannot access it, even if a
  different policy grants access.
- **Principal** – In identity-based
  policies (IAM policies), the user that the policy is attached to is
  the implicit principal. For resource-based policies, you specify the
  user, account, service, or other entity that you want to receive
  permissions (applies to resource-based policies only). AWS Data Exchange doesn't
  support resource-based policies.

For more information about IAM policy syntax and descriptions, see [AWS Identity and Access Management Policy Reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md")
in the _IAM User Guide_.

### Specifying conditions in a

policy

When you grant permissions, you can use the IAM policy language to specify
the conditions when a policy should take effect. With AWS Data Exchange, the
`CreateJob`, `StartJob`, `GetJob`, and
`CancelJob` API operations support conditional permissions. You
can provide permissions at the `JobType` level.

| AWS Data Exchange condition key reference                                          | Condition key                                                                   | Description | Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `"dataexchange:JobType":"IMPORT_ASSETS_FROM_S3"`                                   | Scopes permissions to jobs that import assets from Amazon S3.                   | String      |
| ``"dataexchange:JobType":IMPORT_ASSETS_FROM_LAKE_FORMATION_TAG_POLICY"` (Preview)` | Scopes permissions to jobs that import assets from AWS Lake Formation (Preview) | String      |
| `"dataexchange:JobType":"IMPORT_ASSET_FROM_SIGNED_URL"`                            | Scopes permissions to jobs that import assets from a signed URL.                | String      |
| `"dataexchange:JobType":"IMPORT_ASSET_FROM_REDSHIFT_DATA_SHARES"`                  | Scopes permissions to jobs that import assets from Amazon Redshift.             | String      |
| `"dataexchange:JobType":"IMPORT_ASSET_FROM_API_GATEWAY_API"`                       | Scopes permissions to jobs that import assets from Amazon API Gateway.          | String      |
| `"dataexchange:JobType":"EXPORT_ASSETS_TO_S3"`                                     | Scopes permissions to jobs that export assets to Amazon S3.                     | String      |
| `"dataexchange:JobType":"EXPORT_ASSETS_TO_SIGNED_URL"`                             | Scopes permissions to jobs that export assets to a signed URL.                  | String      |
| `"dataexchange:JobType":EXPORT_REVISIONS_TO_S3"`                                   | Scopes permissions to jobs that export revisions to Amazon S3.                  | String      | For more information about specifying conditions in a policy language, see [Condition](../../../IAM/latest/UserGuide/reference_policies_elements.md#Condition "../../../IAM/latest/UserGuide/reference_policies_elements.md#Condition") in the _IAM User Guide_. To express conditions, you use predefined condition keys. AWS Data Exchange has the `JobType` condition for API operations. However, there are AWS wide condition keys that you can use, as appropriate. For a complete list of AWS wide keys, see the [_IAM User Guide_](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md"). |
