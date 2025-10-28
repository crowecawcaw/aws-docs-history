# How AWS CodeDeploy works with

IAM

Before you use IAM to manage access to CodeDeploy, you should understand which
IAM features are available to use with CodeDeploy. For more information, see
[AWS
services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the
_IAM User Guide_.

###### Topics

- [CodeDeploy
  identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [CodeDeploy resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Authorization based on
  CodeDeploy tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [CodeDeploy IAM
  roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## CodeDeploy

identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources and the conditions under which actions are allowed or denied.
CodeDeploy supports actions, resources, and condition keys. For information
about the elements that you use in a JSON policy, see [IAM JSON policy elements
reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in CodeDeploy use the `codedeploy:`
prefix before the action. For example, the
`codedeploy:GetApplication` permission grants the user
permissions to perform the `GetApplication` operation. Policy
statements must include either an `Action` or `NotAction`
element. CodeDeploy defines its own set of actions that describe tasks
that you can perform with this service.

To specify multiple actions in a single statement, separate them with commas
as follows:

```
"Action": [
      "codedeploy:*action1*",
      "codedeploy:*action2*"
```

You can specify multiple actions using wildcards (\*). For example, include the
following action to specify all actions that begin with the word
`Describe`:

```
`"Action": "ec2:Describe*"`
```

For a list of CodeDeploy actions, see [Actions Defined by AWS CodeDeploy](../../../IAM/latest/UserGuide/list_awscodedeploy.md#awscodedeploy-actions-as-permissions "../../../IAM/latest/UserGuide/list_awscodedeploy.md#awscodedeploy-actions-as-permissions") in the
_IAM User Guide_.

For a table that lists all of the CodeDeploy API actions and the resources
they apply to, see [CodeDeploy
permissions reference](auth-and-access-control-permissions-reference.md "auth-and-access-control-permissions-reference.md").

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

For example, you can indicate a deployment group
(`myDeploymentGroup`) in your statement using its
ARN as follows:

```
"Resource": "arn:aws:codedeploy:`us-west-2`:`123456789012`:deploymentgroup:`myApplication`/`myDeploymentGroup`"
```

You can also specify all deployment groups that belong to an account by using
the wildcard character (\*) as follows:

```
"Resource": "arn:aws:codedeploy:`us-west-2`:`123456789012`:deploymentgroup:`*`"
```

To specify all resources, or if an API action does not support ARNs, use the
wildcard character (\*) in the `Resource` element as follows:

```
"Resource": "`*`"
```

Some CodeDeploy API actions accept multiple resources (for example,
`BatchGetDeploymentGroups`). To specify multiple resources in a
single statement, separate their ARNs with commas, as follows:

```
"Resource": ["arn1", "arn2"]
```

CodeDeploy provides a set of operations to work with the CodeDeploy
resources. For a list of available operations, see [CodeDeploy
permissions reference](auth-and-access-control-permissions-reference.md "auth-and-access-control-permissions-reference.md").

For a list of CodeDeploy resource types and their ARNs, see
[Resources Defined by AWS CodeDeploy](../../../IAM/latest/UserGuide/list_awscodedeploy.md "../../../IAM/latest/UserGuide/list_awscodedeploy.md") in the _IAM User Guide_. For
information about the actions in which you can specify the ARN of each resource,
see [Actions Defined by AWS CodeDeploy](../../../IAM/latest/UserGuide/list_awscodedeploy.md#awscodedeploy-actions-as-permissions "../../../IAM/latest/UserGuide/list_awscodedeploy.md#awscodedeploy-actions-as-permissions").

#### CodeDeploy resources and operations

In CodeDeploy, the primary resource is a
deployment group. In a policy, you use an Amazon Resource
Name (ARN) to identify the resource that the policy applies to.
CodeDeploy supports other resources that can be used with
deployment groups, including applications, deployment configurations, and
instances. These are referred to as subresources. These resources and
subresources have unique ARNs associated with them. For more information,
see [Amazon resource
names (ARNs)](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md") in the _Amazon Web Services General Reference_.

| Resource type                                                                   | ARN format                                                                                            |
| ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Deployment group                                                                | `arn:aws:codedeploy:`region`:`account-id`:deploymentgroup:`application-name`/`deployment-group-name`` |
| Application                                                                     | `arn:aws:codedeploy:`region`:`account-id`:application:`application-name``                             |
| Deployment configuration                                                        | `arn:aws:codedeploy:`region`:`account-id`:deploymentconfig:`deployment-configuration-name``           |
| Instance                                                                        | `arn:aws:codedeploy:`region`:`account-id`:instance/`instance-ID``                                     |
| All CodeDeploy resources                                                        | `arn:aws:codedeploy:*`                                                                                |
| All CodeDeploy resources owned by the specified account in the specified Region | `arn:aws:codedeploy:`region`:`account-id`:*`                                                          | ###### Note Most services in AWS treat a colon (:) or a forward slash (/) as the same character in ARNs. However, CodeDeploy uses an exact match in resource patterns and rules. Be sure to use the correct ARN characters when you create event patterns so that they match the ARN syntax in the resource. ### Condition keys CodeDeploy does not provide any service-specific condition keys, but it does support the use of some global condition keys. For more information, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_. ### Examples To view examples of CodeDeploy identity-based policies, see [AWS CodeDeploy identity-based policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md"). ## CodeDeploy resource-based policies CodeDeploy does not support resource-based policies. To view an example of a detailed resource-based policy page, see [Using resource-based policies for AWS Lambda](../../../lambda/latest/dg/access-control-resource-based.md "../../../lambda/latest/dg/access-control-resource-based.md"). ## Authorization based on CodeDeploy tags CodeDeploy does not support tagging resources or controlling access based on tags. ## CodeDeploy IAM roles An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity in your AWS account that has specific permissions. ### Using temporary credentials with CodeDeploy You can use temporary credentials to sign in with federation, assume an IAM role, or to assume a cross-account role. You obtain temporary security credentials by calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md"). CodeDeploy supports the use of temporary credentials. ### Service-linked roles CodeDeploy does not support service-linked roles. ### Service roles This feature allows a service to assume a [service role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") on your behalf. This role allows the service to access resources in other services to complete an action on your behalf. Service roles appear in your AWS account and are owned by the account. This means that a user can change the permissions for this role. However, doing so might break the functionality of the service. CodeDeploy supports service roles. ### Choosing an IAM role in CodeDeploy When you create a deployment group resource in CodeDeploy, you must choose a role to allow CodeDeploy to access Amazon EC2 on your behalf. If you have previously created a service role or service-linked role, CodeDeploy provides you with a list of roles to choose from. It's important to choose a role that allows access to start and stop EC2 instances. |
