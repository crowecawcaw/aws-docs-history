# How AWS Glue DataBrew works with

IAM

Before you use IAM to manage access to DataBrew, you should understand what
IAM features are available to use with DataBrew. To get a high-level view of how
DataBrew and other AWS services work with IAM, see [AWS Services That
Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [DataBrew
  identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [Resource-based
  policies in DataBrew](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [DataBrew IAM
  Roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## DataBrew

identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources, and also the conditions under which actions are allowed or denied.
DataBrew supports specific actions, resources, and condition keys. To learn
about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is,
an AWS JSON policy can specify which principal can perform actions on what resources,
and under what conditions.

The Action element of a JSON policy describes the actions to which you can allow or
deny access in a policy. Policy actions usually have the same name as the associated AWS
API operation. There are some exceptions, such as permission-only actions that don't have
a matching API operation. There are also some operations that require multiple actions in
a policy. These additional actions are called dependent actions.

Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in DataBrew use the following prefix before the action:
`databrew:`. For example, to grant someone permission to run
an Amazon EC2 instance with the Amazon EC2 `RunInstances` API operation, you include
the `ec2:RunInstances` action in their policy. Policy statements must
include either an `Action` or `NotAction` element.
DataBrew defines its own set of actions that describe tasks that you can
perform with it.

To specify multiple actions in a single statement, separate them with commas as
follows.

```
"Action": [
      "databrew:*CreateRecipeJob*",
      "databrew:*UpdateSchedule*"
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `Describe`, include the following
action.

```
`"Action": "databrew:Describe*"`
```

To see a list of DataBrew actions, see [Actions Defined by AWS Glue DataBrew](../../../service-authorization/latest/reference/list_databrew.md#databrew-actions-as-permissions "../../../service-authorization/latest/reference/list_databrew.md#databrew-actions-as-permissions") in the
_IAM User Guide_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

The following are the DataBrew APIs that don't support resource level permissions:

- ListDatasets
- ListJobs
- ListProjects
- ListRecipes
- ListRulesets
- ListSchedules

The DataBrew dataset resource has the following Amazon Resource Name (ARN).

```
arn:${Partition}:databrew:${Region}:${Account}:dataset/${Name}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

For example, to specify the `i-1234567890abcdef0` instance in your
statement, use the following ARN.

```
"Resource": "arn:aws:databrew:us-east-1:123456789012:dataset/my-chess-dataset"
```

To specify all instances that belong to a specific account, use the wildcard
(\*).

```
"Resource": "arn:aws:databrew:us-east-1:123456789012:dataset/*"
```

You can't perform some DataBrew actions, such as those for creating
resources, on a specific resource. In those cases, you must use the wildcard
(\*).

```
"Resource": "*"
```

To see a list of DataBrew resource types and their ARNs, see
[Resources Defined by AWS Glue DataBrew](../../../service-authorization/latest/reference/list_databrew.md#databrew-resources-for-iam-policies "../../../service-authorization/latest/reference/list_databrew.md#databrew-resources-for-iam-policies") in the _IAM User Guide_. To learn
with which actions you can specify the ARN of each resource, see
[Actions Defined by AWS Glue DataBrew](../../../service-authorization/latest/reference/list_databrew.md#databrew-actions-as-permissions "../../../service-authorization/latest/reference/list_databrew.md#databrew-actions-as-permissions").

### Condition keys

DataBrew doesn't provide any service-specific condition keys, but it does support
using some global condition keys. To see all AWS global condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User
Guide_.

### Examples

To view examples of DataBrew identity-based policies, see [Identity-based policy examples for
AWS Glue DataBrew](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Resource-based

policies in DataBrew

DataBrew doesn't support resource-based policies.

## DataBrew IAM

Roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within
your AWS account that has specific permissions.

### Using temporary

credentials with DataBrew

You can use temporary credentials to sign in with federation, assume an IAM
role, or to assume a cross-account role. You get temporary security credentials by
calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

DataBrew supports using temporary credentials.

### Service-linked

roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other
services to complete an action on your behalf. Service-linked roles appear in your
IAM account and are owned by the service. An administrator can view but not
edit the permissions for service-linked roles.

### Choosing an IAM role

in DataBrew

When you create a dataset resource in DataBrew, you choose an IAM role to
allow DataBrew access on your behalf. If you have previously created a
service role or service-linked role, then DataBrew provides you with a list
of roles to choose from. Make sure to choose a role that allows read access to an
Amazon S3 bucket or AWS Glue Data Catalog resource, as appropriate.
