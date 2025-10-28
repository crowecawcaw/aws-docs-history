# How Amazon WorkMail works with

IAM

Before you use IAM to manage access to Amazon WorkMail, you should understand what
IAM features are available to use with Amazon WorkMail. To get a high-level view of how
Amazon WorkMail and other AWS services work with IAM, see [AWS services that
work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [Amazon WorkMail
  identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [Amazon WorkMail
  resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Authorization based on
  Amazon WorkMail tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [Amazon WorkMail IAM
  roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## Amazon WorkMail

identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied.
Amazon WorkMail supports specific actions, resources, and condition keys. To learn
about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Amazon WorkMail use the following prefix before the action:
`workmail:`. For example, to grant someone permission to retrieve a list of users with the Amazon WorkMail `ListUsers` API operation, you include
the `workmail:ListUsers` action in their policy. Policy statements must
include either an `Action` or `NotAction` element.
Amazon WorkMail defines its own set of actions that describe tasks that you can
perform with this service.

To specify multiple actions in a single statement, separate them with commas as
follows:

```
"Action": [
      "workmail:*ListUsers*",
      "workmail:*DeleteUser*"
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `List`, include the following
action:

```
`"Action": "workmail:List*"`
```

To see a list of Amazon WorkMail actions, see [Actions defined by Amazon WorkMail](../../../IAM/latest/UserGuide/list_amazonworkmail.md#amazonworkmail-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonworkmail.md#amazonworkmail-actions-as-permissions") in the _IAM User Guide_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

Amazon WorkMail supports resource-level permissions for Amazon WorkMail organizations.

The Amazon WorkMail organization resource has the following ARN:

```
arn:aws:workmail:${Region}:${Account}:organization/${OrganizationId}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS service namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

For example, to specify the `m-n1pq2345678r901st2u3vx45x6789yza`
organization in your statement, use the following ARN.

```
"Resource": "arn:aws:workmail:us-east-1:111122223333:organization/m-n1pq2345678r901st2u3vx45x6789yza"
```

To specify all organizations that belong to a specific account, use the wildcard
(\*):

```
"Resource": "arn:aws:workmail:us-east-1:111122223333:organization/*"
```

Some Amazon WorkMail actions, such as those for creating resources, can't be
performed on a specific resource. In those cases, you must use the wildcard
(\*).

```
"Resource": "*"
```

To see a list of Amazon WorkMail resource types and their ARNs, see
[Resources defined by Amazon WorkMail](../../../IAM/latest/UserGuide/list_amazonworkmail.md#amazonworkmail-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonworkmail.md#amazonworkmail-resources-for-iam-policies") in the _IAM User Guide_. To learn
with which actions you can specify for the ARN of each resource, see
[Actions, resources, and condition keys for Amazon WorkMail](../../../IAM/latest/UserGuide/list_amazonworkmail.md "../../../IAM/latest/UserGuide/list_amazonworkmail.md").

### Condition keys

Amazon WorkMail supports the following global condition keys.

- `aws:CurrentTime`
- `aws:EpochTime`
- `aws:MultiFactorAuthAge`
- `aws:MultiFactorAuthPresent`
- `aws:PrincipalOrgID`
- `aws:PrincipalArn`
- `aws:RequestedRegion`
- `aws:SecureTransport`
- `aws:UserAgent`

The following example policy grants access to the Amazon WorkMail console only from MFA authenticated IAM principals in the `eu-west-1` AWS Region.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ses:Describe*",
 "ses:Get*",
 "workmail:Describe*",
 "workmail:Get*",
 "workmail:List*",
 "workmail:Search*",
 "lambda:ListFunctions",
 "iam:ListRoles",
 "logs:DescribeLogGroups",
 "cloudwatch:GetMetricData"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:RequestedRegion": [
 "eu-west-1"
 ]
 },
 "Bool": {
 "aws:MultiFactorAuthPresent": true
 }
 }
 }
 ]
}`

```

To see all AWS global condition keys, see [AWS global condition
context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

`workmail:ImpersonationRoleId` is the only service-specific condition key supported by Amazon WorkMail.

The following example policy scopes-down `AssumeImpersonationRole` action to a particular WorkMail organization and impersonation role.

### Examples

To view examples of Amazon WorkMail identity-based policies, see [Amazon WorkMail identity-based
policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Amazon WorkMail

resource-based policies

Amazon WorkMail does not support resource-based policies.

## Authorization based on

Amazon WorkMail tags

You can attach tags to Amazon WorkMail resources or pass tags in a request to
Amazon WorkMail. To control access based on tags, you provide tag information in the
[condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the
`aws:ResourceTag/key-name`,
`aws:RequestTag/key-name`, or
`aws:TagKeys` condition keys. For more information about tagging
Amazon WorkMail resources, see [Tagging an organization](org-tag.md "org-tag.md").

## Amazon WorkMail IAM

roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within
your AWS account that has specific permissions.

### Using temporary

credentials with Amazon WorkMail

You can use temporary credentials to sign in with federation, assume an IAM
role, or to assume a cross-account role. You obtain temporary security credentials by
calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

Amazon WorkMail supports using temporary credentials.

### Service-linked

roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other
services to complete an action on your behalf. Service-linked roles appear in your
IAM account and are owned by the service. An IAM administrator can view but not
edit the permissions for service-linked roles.

Amazon WorkMail supports service-linked roles. For details about creating or
managing Amazon WorkMail service-linked roles, see [Using service-linked roles for
Amazon WorkMail](using-service-linked-roles.md "using-service-linked-roles.md").

### Service roles

This feature allows a service to assume a [service
role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") on your behalf. This role allows the service to access resources in
other services to complete an action on your behalf. Service roles appear in your
IAM account and are owned by the account. This means that an IAM administrator
can change the permissions for this role. However, doing so might break the
functionality of the service.

Amazon WorkMail supports service roles.
