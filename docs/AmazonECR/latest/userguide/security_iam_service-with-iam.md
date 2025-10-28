# How Amazon Elastic Container Registry works with IAM

Before you use IAM to manage access to Amazon ECR, you should understand what IAM
features are available to use with Amazon ECR. To get a high-level view of how Amazon ECR and
other AWS services work with IAM, see [AWS Services
That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [Amazon ECR
  Identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [Amazon ECR
  resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Authorization based on Amazon ECR
  tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [Amazon ECR IAM roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## Amazon ECR

Identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied. Amazon ECR
supports specific actions, resources, and condition keys. To learn about all of the
elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Amazon ECR use the following prefix before the action:
`ecr:`. For example, to grant someone permission to create an
Amazon ECR repository with the Amazon ECR `CreateRepository` API operation, you
include the `ecr:CreateRepository` action in their policy. Policy
statements must include either an `Action` or `NotAction`
element. Amazon ECR defines its own set of actions that describe tasks that you can
perform with this service.

To specify multiple actions in a single statement, separate them with commas
as follows:

```
"Action": [
      "ecr:*action1*",
      "ecr:*action2*"
```

You can specify multiple actions using wildcards (\*). For example, to specify
all actions that begin with the word `Describe`, include the
following action:

```
`"Action": "ecr:Describe*"`
```

To see a list of Amazon ECR actions, see [Actions,
Resources, and Condition Keys for Amazon Elastic Container Registry](../../../IAM/latest/UserGuide/list_amazonelasticcontainerregistry.md "../../../IAM/latest/UserGuide/list_amazonelasticcontainerregistry.md") in the
_IAM User Guide_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

An Amazon ECR repository resource has the following ARN:

```
arn:${Partition}:ecr:${Region}:${Account}:repository/${Repository-name}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

For example, to specify the `my-repo` repository in the
`us-east-1` Region in your statement, use the following
ARN:

```
"Resource": "arn:aws:ecr:`us-east-1`:`123456789012`:repository/my-repo"
```

To specify all repositories that belong to a specific account, use the
wildcard (\*):

```
"Resource": "arn:aws:ecr:`us-east-1`:`123456789012`:repository/*"
```

To specify multiple resources in a single statement, separate the ARNs with
commas.

```
"Resource": [
      "*resource1*",
      "*resource2*"
```

To see a list of Amazon ECR resource types and their ARNs, see [Resources Defined by Amazon Elastic Container Registry](../../../IAM/latest/UserGuide/list_amazonelasticcontainerregistry.md#amazonelasticcontainerregistry-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_amazonelasticcontainerregistry.md#amazonelasticcontainerregistry-resources-for-iam-policies") in the
_IAM User Guide_. To learn with which actions you can
specify the ARN of each resource, see [Actions Defined by Amazon Elastic Container Registry](../../../IAM/latest/UserGuide/list_amazonelasticcontainerregistry.md#amazonelasticcontainerregistry-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonelasticcontainerregistry.md#amazonelasticcontainerregistry-actions-as-permissions").

### Condition keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

Amazon ECR defines its own set of condition keys and also supports using some
global condition keys. To see all AWS global condition keys, see [AWS Global
Condition Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

Most Amazon ECR actions support the `aws:ResourceTag` and
`ecr:ResourceTag` condition keys. For more information, see [Using Tag-Based Access Control](ecr-supported-iam-actions-tagging.md "ecr-supported-iam-actions-tagging.md").

To see a list of Amazon ECR condition keys, see [Condition Keys Defined by Amazon Elastic Container Registry](../../../IAM/latest/UserGuide/list_amazonelasticcontainerregistry.md#amazonelasticcontainerregistry-policy-keys "../../../IAM/latest/UserGuide/list_amazonelasticcontainerregistry.md#amazonelasticcontainerregistry-policy-keys") in the
_IAM User Guide_. To learn with which actions and
resources you can use a condition key, see [Actions Defined by Amazon Elastic Container Registry](../../../IAM/latest/UserGuide/list_amazonelasticcontainerregistry.md#amazonelasticcontainerregistry-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonelasticcontainerregistry.md#amazonelasticcontainerregistry-actions-as-permissions").

### Examples

To view examples of Amazon ECR identity-based policies, see [Amazon Elastic Container Registry Identity-based policy
examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Amazon ECR

resource-based policies

Resource-based policies are JSON policy documents that specify what actions a
specified principal can perform on an Amazon ECR resource and under what conditions.
Amazon ECR supports resource-based permissions policies for Amazon ECR repositories.
Resource-based policies let you grant usage permission to other accounts on a
per-resource basis. You can also use a resource-based policy to allow an AWS
service to access your Amazon ECR repositories.

To enable cross-account access, you can specify an entire account or IAM
entities in another account as the [principal in a
resource-based policy](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md"). Adding a cross-account principal to a
resource-based policy is only half of establishing the trust relationship. When the
principal and the resource are in different AWS accounts, you must also grant the
principal entity permission to access the resource. Grant permission by attaching an
identity-based policy to the entity. However, if a resource-based policy grants
access to a principal in the same account, you don't need additional Amazon ECR
repository permissions in the identity-based policy. For more information, see
[How IAM
Roles Differ from Resource-based Policies](../../../IAM/latest/UserGuide/id_roles_compare-resource-policies.md "../../../IAM/latest/UserGuide/id_roles_compare-resource-policies.md") in the
_IAM User Guide_.

The Amazon ECR service supports only one type of resource-based policy called a
_repository policy_, which is attached to a
_repository_. This policy defines which principal entities
(accounts, users, roles, and federated users) can perform actions on the repository.
To learn how to attach a resource-based policy to a repository, see [Private repository policies in Amazon ECR](repository-policies.md "repository-policies.md").

###### Note

In an Amazon ECR repository policy, the policy element `Sid` supports
additional characters and spacing not supported in IAM policies.

### Examples

To view examples of Amazon ECR resource-based policies, see [Private repository policy examples in Amazon ECR](repository-policy-examples.md "repository-policy-examples.md"),

## Authorization based on Amazon ECR

tags

You can attach tags to Amazon ECR resources or pass tags in a request to Amazon ECR. To
control access based on tags, you provide tag information in the [condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the
`ecr:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or
`aws:TagKeys` condition keys. For more information about tagging
Amazon ECR resources, see [Tagging a private repository in Amazon ECR](ecr-using-tags.md "ecr-using-tags.md").

To view an example identity-based policy for limiting access to a resource based
on the tags on that resource, see [Using Tag-Based Access Control](ecr-supported-iam-actions-tagging.md "ecr-supported-iam-actions-tagging.md").

## Amazon ECR IAM roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within
your AWS account that has specific permissions.

### Using Temporary

Credentials with Amazon ECR

You can use temporary credentials to sign in with federation, assume an IAM
role, or to assume a cross-account role. You obtain temporary security
credentials by calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

Amazon ECR supports using temporary credentials.

### Service-linked roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in
other services to complete an action on your behalf. Service-linked roles appear
in your IAM account and are owned by the service. An IAM administrator can
view but not edit the permissions for service-linked roles.

Amazon ECR supports service-linked roles. For more information, see [Using service-linked roles for
Amazon ECR](using-service-linked-roles.md "using-service-linked-roles.md").
