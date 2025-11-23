# Identity and Access Management for

Amazon OpenSearch Serverless

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control access
to AWS resources. IAM administrators control who can be _authenticated_ (signed in) and _authorized_
(have permissions) to use OpenSearch Serverless resources. IAM is an AWS service that you can
use with no additional charge.

###### Topics

- [Identity-based policies for
  OpenSearch Serverless](#security-iam-serverless-id-based-policies "#security-iam-serverless-id-based-policies")
- [Policy actions for
  OpenSearch Serverless](#security-iam-serverless-id-based-policies-actions "#security-iam-serverless-id-based-policies-actions")
- [Policy resources
  for OpenSearch Serverless](#security-iam-serverless-id-based-policies-resources "#security-iam-serverless-id-based-policies-resources")
- [Policy condition keys for
  Amazon OpenSearch Serverless](#security_iam_serverless-conditionkeys "#security_iam_serverless-conditionkeys")
- [ABAC with OpenSearch Serverless](#security_iam_serverless-with-iam-tags "#security_iam_serverless-with-iam-tags")
- [Using temporary credentials with
  OpenSearch Serverless](#security_iam_serverless-tempcreds "#security_iam_serverless-tempcreds")
- [Service-linked roles for OpenSearch Serverless](#security_iam_serverless-slr "#security_iam_serverless-slr")
- [Other policy types](#security_iam_access-manage-other-policies "#security_iam_access-manage-other-policies")
- [Identity-based policy
  examples for OpenSearch Serverless](#security_iam_serverless_id-based-policy-examples "#security_iam_serverless_id-based-policy-examples")
- [IAM Identity Center support for Amazon OpenSearch Serverless](serverless-iam-identity-center.md "serverless-iam-identity-center.md")

## Identity-based policies for

OpenSearch Serverless

**Supports identity-based policies:**

Yes

Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These
policies control what actions users and roles can perform, on which resources, and under what conditions. To learn how to create an identity-based
policy, see [Define custom IAM permissions with customer managed policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the
_IAM User Guide_.

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied. To learn about all of the elements that you can use in a
JSON policy, see [IAM JSON
policy elements reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the
_IAM User Guide_.

### Identity-based policy

examples for OpenSearch Serverless

To view examples of OpenSearch Serverless identity-based policies, see [Identity-based policy
examples for OpenSearch Serverless](#security_iam_serverless_id-based-policy-examples "#security_iam_serverless_id-based-policy-examples").

## Policy actions for

OpenSearch Serverless

**Supports policy actions:**

Yes

The `Action` element of a JSON policy describes the actions that you can
use to allow or deny access in a policy. Policy actions usually have the same name as
the associated AWS API operation. There are some exceptions, such as
_permission-only actions_ that don't have a matching API
operation. There are also some operations that require multiple actions in a policy.
These additional actions are called _dependent actions_.

Include actions in a policy to grant permissions to perform the associated
operation.

Policy actions in OpenSearch Serverless use the following prefix before the action:

```
aoss
```

To specify multiple actions in a single statement, separate them with commas.

```
"Action": [
      "aoss:`action1`",
      "aoss:`action2`"
         ]
```

You can specify multiple actions using wildcard characters (\*). For example, to
specify all actions that begin with the word `Describe`, include the
following action:

```
"Action": "aoss:List*"
```

To view examples of OpenSearch Serverless identity-based policies, see [Identity-based policy
examples for OpenSearch Serverless](#security_iam_id-based-policy-examples "#security_iam_id-based-policy-examples").

## Policy resources

for OpenSearch Serverless

**Supports policy resources:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

## Policy condition keys for

Amazon OpenSearch Serverless

**Supports service-specific policy condition keys:**

Yes

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

In addition to attribute-based access control (ABAC), OpenSearch Serverless supports the following
condition keys:

- `aoss:collection`
- `aoss:CollectionId`
- `aoss:index`

You can use these condition keys even when providing permissions for access policies
and security policies. For example:

```
[
   {
      "Effect":"Allow",
      "Action":[
         "aoss:CreateAccessPolicy",
         "aoss:CreateSecurityPolicy"
      ],
      "Resource":"*",
      "Condition":{
         "StringLike":{
            "aoss:collection":"`log`"
         }
      }
   }
]
```

In this example, the condition applies to policies that contain
_rules_ that match a collection name or pattern. The conditions
have the following behavior:

- `StringEquals` - Applies to policies with rules that contain the
  _exact_ resource string "log" (i.e.
  `collection/log`).
- `StringLike` - Applies to policies with rules that contain a
  resource string that _includes_ the string "log" (i.e.
  `collection/log` but also
  `collection/logs-application` or
  `collection/applogs123`).

###### Note

_Collection_ condition keys don't apply at the index level. For
example, in the policy above, the condition wouldn't apply to an access or security
policy containing the resource string `index/logs-application/*`.

To see a list of OpenSearch Serverless condition keys, see [Condition keys for Amazon OpenSearch Serverless](../../../service-authorization/latest/reference/list_amazonopensearchserverless.md#amazonopensearchserverless-policy-keys "../../../service-authorization/latest/reference/list_amazonopensearchserverless.md#amazonopensearchserverless-policy-keys") in the _Service Authorization Reference_.
To learn with which actions and resources you can use a condition key, see [Actions defined by Amazon OpenSearch Serverless](../../../service-authorization/latest/reference/list_amazonopensearchserverless.md#amazonopensearchserverless-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonopensearchserverless.md#amazonopensearchserverless-actions-as-permissions").

## ABAC with OpenSearch Serverless

**Supports ABAC (tags in policies):**

Yes

Attribute-based access control (ABAC) is an authorization strategy that defines permissions
based on attributes called tags. You can attach tags to IAM entities and AWS resources, then design ABAC policies to allow operations when the principal's tag matches the tag on the resource.

To control access based on tags, you provide tag information in the [condition element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the `aws:ResourceTag/`key-name``, 
 `aws:RequestTag/`key-name``, or `aws:TagKeys` condition keys.

If a service supports all three condition keys for every resource type, then the value is **Yes** for the service. If a service supports all three condition keys for only some resource types, then the value is **Partial**.

For more information about ABAC, see [Define permissions with ABAC authorization](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. To view a tutorial with steps for setting up ABAC, see
[Use attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md") in the _IAM User Guide_.

For more information about tagging OpenSearch Serverless resources, see [Tagging Amazon OpenSearch Serverless collections](tag-collection.md "tag-collection.md").

## Using temporary credentials with

OpenSearch Serverless

**Supports temporary credentials:**

Yes

Temporary credentials provide short-term access to AWS resources and are automatically created when you use federation or switch roles. AWS recommends that you
dynamically generate temporary credentials instead of using long-term access keys. For
more information, see [Temporary
security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") and [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

## Service-linked roles for OpenSearch Serverless

**Supports service-linked roles:**

Yes

A service-linked role is a type of service role that is linked to an AWS service. The service can assume the role to perform an action on your behalf.
Service-linked roles appear in your AWS account and are owned by the service. An IAM administrator can view,
but not edit the permissions for service-linked roles.

For details about creating and managing OpenSearch Serverless service-linked roles, see [Using service-linked roles to create
OpenSearch Serverless collections](serverless-service-linked-roles.md "serverless-service-linked-roles.md").

## Other policy types

AWS supports additional, less-common policy types. These policy types can set the
maximum permissions granted to you by the more common policy types.

- Service control policies (SCPs) – SCPs
  are JSON policies that specify the maximum permissions for an organization or
  organizational unit (OU) in AWS Organizations. AWS Organizations is a service for grouping and
  centrally managing multiple AWS accounts that your business owns. If you
  enable all features in an organization, then you can apply service control
  policies (SCPs) to any or all of your accounts. The SCP limits permissions for
  entities in member accounts, including each AWS account root user. For more
  information about Organizations and SCPs, see [Service
  control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") in the _AWS Organizations User Guide_.
- Resource control policies (RCPs) – RCPs
  are JSON policies that you can use to set the maximum available permissions for
  resources in your accounts without updating the IAM policies attached to each
  resource that you own. The RCP limits permissions for resources in member
  accounts and can impact the effective permissions for identities, including the
  AWS account root user, regardless of whether they belong to your organization.
  For more information about Organizations and RCPs, including a list of AWS services
  that support RCPs, see [Resource
  control policies (RCPs)](../../../organizations/latest/userguide/orgs_manage_policies_rcps.md "../../../organizations/latest/userguide/orgs_manage_policies_rcps.md") in the
  _AWS Organizations User Guide_.

## Identity-based policy

examples for OpenSearch Serverless

By default, users and roles don't have permission to create or modify OpenSearch Serverless
resources. To grant users permission to perform actions on the
resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy
documents, see [Create IAM policies (console)](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") in the
_IAM User Guide_.

For details about actions and resource types defined by Amazon OpenSearch Serverless, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon OpenSearch Serverless](../../../service-authorization/latest/reference/list_amazonopensearchserverless.md "../../../service-authorization/latest/reference/list_amazonopensearchserverless.md") in the _Service Authorization Reference_.

###### Topics

- [Policy best
  practices](#security_iam_serverless-policy-best-practices "#security_iam_serverless-policy-best-practices")
- [Using
  OpenSearch Serverless in the console](#security_iam_serverless_id-based-policy-examples-console "#security_iam_serverless_id-based-policy-examples-console")
- [Administering OpenSearch Serverless collections](#security_iam_id-based-policy-examples-collection-admin "#security_iam_id-based-policy-examples-collection-admin")
- [Viewing
  OpenSearch Serverless collections](#security_iam_id-based-policy-examples-view-collections "#security_iam_id-based-policy-examples-view-collections")
- [Using OpenSearch
  API operations](#security_iam_id-based-policy-examples-data-plane "#security_iam_id-based-policy-examples-data-plane")
- [ABAC for
  OpenSearch API operations](#security_iam_id-based-policy-examples-data-plane-abac "#security_iam_id-based-policy-examples-data-plane-abac")

### Policy best

practices

Identity-based policies are very powerful. They determine whether someone can
create, access, or delete OpenSearch Serverless resources in your account. These actions
can incur costs for your AWS account. When you create or edit identity-based
policies, follow these guidelines and recommendations:

Identity-based policies determine whether someone can create, access, or delete OpenSearch Serverless resources in your
account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Get started with AWS managed policies and move toward least-privilege permissions**
  – To get started granting permissions to your users and workloads, use the _AWS
  managed policies_ that grant permissions for many common use cases. They are
  available in your AWS account. We recommend that you reduce permissions further by
  defining AWS customer managed policies that are specific to your use cases. For more information, see
  [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.
- **Apply least-privilege permissions** –
  When you set permissions with IAM policies, grant only the permissions required to
  perform a task. You do this by defining the actions that can be taken on specific resources
  under specific conditions, also known as _least-privilege permissions_.
  For more information about using IAM to apply permissions, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.
- **Use conditions in IAM policies to further restrict access**
  – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must
  be sent using SSL. You can also use conditions to grant access to service actions
  if they are used through a specific AWS service, such as CloudFormation. For more information, see
  [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
- **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions**
  – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices.
  IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help
  you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_.
- **Require multi-factor authentication (MFA)** –
  If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require
  MFA when API operations are called, add MFA conditions to your policies. For
  more information, see [Secure API access with MFA](../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md "../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md") in the _IAM User Guide_.

For more information about best practices in IAM, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

### Using

OpenSearch Serverless in the console

To access OpenSearch Serverless within the OpenSearch Service console, you must have a minimum set of
permissions. These permissions must allow you to list and view details about the
OpenSearch Serverless resources in your AWS account. If you create an identity-based
policy that is more restrictive than the minimum required permissions, the console
won't function as intended for entities (such as IAM roles) with that
policy.

You don't need to allow minimum console permissions for users that are making
calls only to the AWS CLI or the AWS API. Instead, allow access to only the actions
that match the API operation that you're trying to perform.

The following policy allows a user to access OpenSearch Serverless within the OpenSearch Service
console:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Resource": "*",
 "Effect": "Allow",
 "Action": [
 "aoss:ListCollections",
 "aoss:BatchGetCollection",
 "aoss:ListAccessPolicies",
 "aoss:ListSecurityConfigs",
 "aoss:ListSecurityPolicies",
 "aoss:ListTagsForResource",
 "aoss:ListVpcEndpoints",
 "aoss:GetAccessPolicy",
 "aoss:GetAccountSettings",
 "aoss:GetSecurityConfig",
 "aoss:GetSecurityPolicy"
 ]
 }
 ]
}`

```

### Administering OpenSearch Serverless collections

This policy is an example of a "collection admin" policy that allows a user to
manage and administer Amazon OpenSearch Serverless collections. The user can create, view, and delete
collections.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Resource": "arn:aws:aoss:`us-east-1`:`111122223333`:collection/*",
 "Action": [
 "aoss:CreateCollection",
 "aoss:DeleteCollection",
 "aoss:UpdateCollection"
 ],
 "Effect": "Allow"
 },
 {
 "Resource": "*",
 "Action": [
 "aoss:BatchGetCollection",
 "aoss:ListCollections",
 "aoss:CreateAccessPolicy",
 "aoss:CreateSecurityPolicy"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

### Viewing

OpenSearch Serverless collections

This example policy allows a user to view details for all Amazon OpenSearch Serverless collections
in their account. The user can't modify the collections or any associated security
policies.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Resource": "*",
 "Action": [
 "aoss:ListAccessPolicies",
 "aoss:ListCollections",
 "aoss:ListSecurityPolicies",
 "aoss:ListTagsForResource",
 "aoss:BatchGetCollection"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

### Using OpenSearch

API operations

Data plane API operations consist of the functions you use in OpenSearch Serverless to derive
realtime value from the service. Control plane API operations consist of the
functions you use to set up the environment.

To access Amazon OpenSearch Serverless data plane APIs and OpenSearch Dashboards from the browser, you
need to add two IAM permissions for collection resources. These permissions are
`aoss:APIAccessAll` and `aoss:DashboardsAccessAll`.

###### Note

Starting May 10, 2023, OpenSearch Serverless requires these two new IAM permissions for
collection resources. The `aoss:APIAccessAll` permission allows data
plane access, and the `aoss:DashboardsAccessAll` permission allows
OpenSearch Dashboards from the browser. Failure to add the two new IAM permissions
results in a 403 error.

This example policy allows a user to access data plane APIs for a specified
collection in their account, and to access OpenSearch Dashboards for all collections in
their account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "aoss:APIAccessAll",
 "Resource": "arn:aws:aoss:`us-east-1`:`111122223333`:collection/`collection-id`"
 },
 {
 "Effect": "Allow",
 "Action": "aoss:DashboardsAccessAll",
 "Resource": "arn:aws:aoss:`us-east-1`:`111122223333`:dashboards/default"
 }
 ]
}`

```

Both `aoss:APIAccessAll` and `aoss:DashboardsAccessAll` give
full IAM permission to the collection resources, while the Dashboards permission
also provides OpenSearch Dashboards access. Each permission works independently, so an
explicit deny on `aoss:APIAccessAll` doesn't block
`aoss:DashboardsAccessAll` access to the resources, including Dev
Tools. The same is true for a deny on `aoss:DashboardsAccessAll`. OpenSearch Serverless
supports the following global condition keys:

- `aws:CalledVia`
- `aws:CalledViaAWSService`
- `aws:CalledViaFirst`
- `aws:CalledViaLast`
- `aws:CurrentTime`
- `aws:EpochTime`
- `aws:PrincipalAccount`
- `aws:PrincipalArn`
- `aws:PrincipallsAWSService`
- `aws:PrincipalOrgID`
- `aws:PrincipalOrgPaths`
- `aws:PrincipalType`
- `aws:PrincipalServiceName`
- `aws:PrincipalServiceNamesList`
- `aws:ResourceAccount`
- `aws:ResourceOrgID`
- `aws:ResourceOrgPaths`
- `aws:RequestedRegion`
- `aws:ResourceTag`
- `aws:SourceIp`
- `aws:SourceVpce`
- `aws:SourceVpc`
- `aws:userid`
- `aws:username`
- `aws:VpcSourceIp`

The following is an example of using `aws:SourceIp` in the condition
block in your principal's IAM policy for data plane calls:

```
"Condition": {
    "IpAddress": {
         "aws:SourceIp": "203.0.113.0"
    }
}
```

The following is an example of using `aws:SourceVpc` in the condition
block in your principal's IAM policy for data plane calls:

```
"Condition": {
    "StringEquals": {
        "aws:SourceVpc": "vpc-0fdd2445d8EXAMPLE"
    }
}
```

Additonally, support is offered for the following OpenSearch Serverless specific keys:

- `aoss:CollectionId`
- `aoss:collection`

The following is an example of using `aoss:collection` in the condition
block in your principal's IAM policy for data plane calls:

```
"Condition": {
    "StringLike": {
         "aoss:collection": "log-*"
    }
}
```

### ABAC for

OpenSearch API operations

Identity-based policies let you use tags to control access to Amazon OpenSearch Serverless data
plane APIs. The following policy is an example to allow attached principals to
access data plane APIs if the collection has the `team:devops`
tag:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "aoss:APIAccessAll",
 "Resource": "arn:aws:aoss:`us-east-1`:`111122223333`:collection/`collection-id`",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/team": "devops"
 }
 }
 }
 ]
}`

```

The following policy is an example to deny attached principals to access data
plane APIs and Dashboards access if the collection has the
`environment:production` tag:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "aoss:APIAccessAll",
 "aoss:DashboardsAccessAll"
 ],
 "Resource": "arn:aws:aoss:`us-east-1`:`111122223333`:collection/`collection-id`"
 }
 ]
}`

```

Amazon OpenSearch Serverless do not support `RequestTag` and `TagKeys` global
condition keys for data plane APIs.
