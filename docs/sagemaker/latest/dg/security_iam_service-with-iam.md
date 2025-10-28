# How Amazon SageMaker AI works with

IAM

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

Before you use IAM to manage access to SageMaker AI, you should understand what
IAM features are available to use with SageMaker AI. To get a high-level view of
how SageMaker AI and other AWS services work with IAM, see [AWS Services
That Work with IAM](../../../service-authorization/latest/reference/reference_aws-services-that-work-with-iam.md "../../../service-authorization/latest/reference/reference_aws-services-that-work-with-iam.md") in the _Service Authorization Reference_.

###### Topics

- [Identity-based
  policies for Amazon SageMaker AI](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [Resource-based policies within Amazon SageMaker AI](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Policy
  actions for Amazon SageMaker AI](#security_iam_service-with-iam-id-based-policies-actions "#security_iam_service-with-iam-id-based-policies-actions")
- [Policy resources for Amazon SageMaker AI](#security_iam_service-with-iam-id-based-policies-resources "#security_iam_service-with-iam-id-based-policies-resources")
- [Policy condition keys for Amazon SageMaker AI](#security_iam_service-with-iam-id-based-policies-conditionkeys "#security_iam_service-with-iam-id-based-policies-conditionkeys")
- [Authorization based on
  SageMaker AI tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [SageMaker AI IAM
  roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## Identity-based

policies for Amazon SageMaker AI

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied.
SageMaker AI supports specific actions, resources, and condition keys. To learn
about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../service-authorization/latest/reference/reference_policies_elements.md "../../../service-authorization/latest/reference/reference_policies_elements.md") in the _Service Authorization Reference_.

## Resource-based policies within Amazon SageMaker AI

**Supports resource-based policies:** No

Resource-based policies are JSON policy documents that you attach to a resource.
Examples of resource-based policies are IAM _role trust
policies_ and Amazon S3 _bucket policies_.
In services that support resource-based policies, service administrators can use
them to control access to a specific resource. For the resource where the policy is
attached, the policy defines what actions a specified principal can perform on that
resource and under what conditions. You must [specify a principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in a resource-based policy. Principals can include
accounts, users, roles, federated users, or AWS services.

To enable cross-account access, you can specify an entire account or IAM
entities in another account as the principal in a resource-based policy. Adding a
cross-account principal to a resource-based policy is only half of establishing the
trust relationship. When the principal and the resource are in different AWS
accounts, an IAM administrator in the trusted account must also grant the
principal entity (user or role) permission to access the resource. They grant
permission by attaching an identity-based policy to the entity. However, if a
resource-based policy grants access to a principal in the same account, no
additional identity-based policy is required. For more information, see [Cross account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the _IAM User Guide_.

###### Note

Use [AWS Resource Access Manager](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md") for securely sharing supported SageMaker AI resources. To find the list
of sharable resources, see [shareable Amazon SageMaker AI resources](../../../ram/latest/userguide/shareable.md#shareable-sagemaker "../../../ram/latest/userguide/shareable.md#shareable-sagemaker").

## Policy

actions for Amazon SageMaker AI

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in SageMaker AI use the following prefix before the action:
`sagemaker:`. For example, to grant someone permission
to run a SageMaker AI training job with the SageMaker AI
`CreateTrainingJob` API operation, you include the
`sagemaker:CreateTrainingJob` action in their policy. Policy
statements must include either an `Action` or `NotAction`
element. SageMaker AI defines its own set of actions that describe tasks
that you can perform with this service.

To specify multiple actions in a single statement, separate them with commas
as follows:

```
"Action": [
      "sagemaker:*action1*",
      "sagemaker:*action2*"
]
```

You can specify multiple actions using wildcards (\*). For example, to specify
all actions that begin with the word `Describe`, include the
following action:

```
"Action": "sagemaker:Describe*"
```

To see a list of SageMaker AI actions, see [Actions, resources, and condition keys for Amazon SageMaker AI](../../../service-authorization/latest/reference/list_amazonsagemaker.md "../../../service-authorization/latest/reference/list_amazonsagemaker.md") in the
_Service Authorization Reference_.

## Policy resources for Amazon SageMaker AI

**Supports policy resources:** Yes

Administrators can use AWS JSON policies to specify who has access to what. That
is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to
which the action applies. Statements must include either a `Resource` or
a `NotResource` element. As a best practice, specify a resource using its
[Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). You can do this for actions that support a
specific resource type, known as _resource-level
permissions_.

For actions that don't support resource-level permissions, such as listing
operations, use a wildcard (\*) to indicate that the statement applies to all
resources.

```
"Resource":  "*"
```

To see a list of Amazon SageMaker AI resource types and their ARNs, see the following
references for actions, resource types, and condition keys defined by Amazon SageMaker AI in
the _Service Authorization Reference_.

- [Amazon SageMaker AI](../../../service-authorization/latest/reference/list_amazonsagemaker.md "../../../service-authorization/latest/reference/list_amazonsagemaker.md")
- [Amazon SageMaker geospatial capabilities](../../../service-authorization/latest/reference/list_amazonsagemakergeospatialcapabilities.md "../../../service-authorization/latest/reference/list_amazonsagemakergeospatialcapabilities.md")
- [Amazon SageMaker Ground Truth Synthetic](../../../service-authorization/latest/reference/list_amazonsagemakergroundtruthsynthetic.md "../../../service-authorization/latest/reference/list_amazonsagemakergroundtruthsynthetic.md")
- [Amazon SageMaker AI with MLflow](../../../service-authorization/latest/reference/list_amazonsagemakerwithmlflow.md "../../../service-authorization/latest/reference/list_amazonsagemakerwithmlflow.md")

To learn with which actions you can specify the ARN of each resource, see [Actions defined by Amazon SageMaker AI](../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-actions-as-permissions").

## Policy condition keys for Amazon SageMaker AI

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

SageMaker AI defines its own set of condition keys and also supports using
some global condition keys. To see all AWS global condition keys, see [AWS Global
Condition Context Keys](../../../service-authorization/latest/reference/reference_policies_condition-keys.md "../../../service-authorization/latest/reference/reference_policies_condition-keys.md") in the
_Service Authorization Reference_.

SageMaker AI supports a number of service-specific condition keys that you can use for
fine-grained access control for the following operations:

- [`CreateProcessingJob`](../APIReference/API_CreateProcessingJob.md "../APIReference/API_CreateProcessingJob.md")
- [`CreateTrainingJob`](../APIReference/API_CreateTrainingJob.md "../APIReference/API_CreateTrainingJob.md")
- [`CreateModel`](../APIReference/API_CreateModel.md "../APIReference/API_CreateModel.md")
- [`CreateEndpointConfig`](../APIReference/API_CreateEndpointConfig.md "../APIReference/API_CreateEndpointConfig.md")
- [`CreateTransformJob`](../APIReference/API_CreateTransformJob.md "../APIReference/API_CreateTransformJob.md")
- [`CreateHyperParameterTuningJob`](../APIReference/API_CreateHyperParameterTuningJob.md "../APIReference/API_CreateHyperParameterTuningJob.md")
- [`CreateLabelingJob`](../APIReference/API_CreateLabelingJob.md "../APIReference/API_CreateLabelingJob.md")
- [`CreateNotebookInstance`](../APIReference/API_CreateNotebookInstance.md "../APIReference/API_CreateNotebookInstance.md")
- [`UpdateNotebookInstance`](../APIReference/API_UpdateNotebookInstance.md "../APIReference/API_UpdateNotebookInstance.md")

To see a list of SageMaker AI condition keys, see [Condition keys for Amazon SageMaker AI](../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-policy-keys "../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-policy-keys") in the
_Service Authorization Reference_. To learn with which actions and
resources you can use a condition key, see [Actions defined by Amazon SageMaker AI](../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-actions-as-permissions "../../../service-authorization/latest/reference/list_amazonsagemaker.md#amazonsagemaker-actions-as-permissions").

For examples of using SageMaker AI condition keys, see the following: [Control creation of SageMaker AI resources
with condition keys](security_iam_id-based-policy-examples.md#sagemaker-condition-examples "security_iam_id-based-policy-examples.md#sagemaker-condition-examples").

### Examples

To view examples of SageMaker AI identity-based policies, see [Amazon SageMaker AI
identity-based policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Authorization based on

SageMaker AI tags

You can attach tags to SageMaker AI resources or pass tags in a request to
SageMaker AI. To control access based on tags, you provide tag information
in the [condition element](../../../service-authorization/latest/reference/reference_policies_elements_condition.md "../../../service-authorization/latest/reference/reference_policies_elements_condition.md") of a policy using the
`sagemaker:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or
`aws:TagKeys` condition keys. For more information about tagging
SageMaker AI resources, see [Control access to SageMaker AI resources by using
tags](security_iam_id-based-policy-examples.md#access-tag-policy "security_iam_id-based-policy-examples.md#access-tag-policy").

To view an example identity-based policy for limiting access to a resource
based on the tags on that resource, see [Control access to SageMaker AI resources by using
tags](security_iam_id-based-policy-examples.md#access-tag-policy "security_iam_id-based-policy-examples.md#access-tag-policy").

## SageMaker AI IAM

roles

An [IAM role](../../../service-authorization/latest/reference/id_roles.md "../../../service-authorization/latest/reference/id_roles.md") is an entity
within your AWS account that has specific permissions.

### Using

temporary credentials with SageMaker AI

You can use temporary credentials to sign in with federation, assume an
IAM role, or to assume a cross-account role. You obtain temporary security
credentials by calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

SageMaker AI supports using temporary credentials.

### Service-linked roles

SageMaker AI partially supports [service-linked roles](../../../service-authorization/latest/reference/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../service-authorization/latest/reference/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). Service-linked roles are currently
available for SageMaker Studio Classic.

### Service

roles

This feature allows a service to assume a [service role](../../../service-authorization/latest/reference/id_roles_terms-and-concepts.md#iam-term-service-role "../../../service-authorization/latest/reference/id_roles_terms-and-concepts.md#iam-term-service-role") on your behalf. This role allows the service to
access resources in other services to complete an action on your behalf.
Service roles appear in your IAM account and are owned by the account.
This means that an IAM administrator can change the permissions for this
role. However, doing so might break the functionality of the service.

SageMaker AI supports service roles.

### Choosing an

IAM role in SageMaker AI

When you create a notebook instance, processing job, training job, hosted
endpoint, or batch transform job resource in SageMaker AI, you must
choose a role to allow SageMaker AI to access SageMaker AI on your behalf. If
you have previously created a service role or service-linked role, then
SageMaker AI provides you with a list of roles to choose from. It's
important to choose a role that allows access to the AWS operations and
resources you need. For more information, see [How to use SageMaker AI execution roles](sagemaker-roles.md "sagemaker-roles.md").
