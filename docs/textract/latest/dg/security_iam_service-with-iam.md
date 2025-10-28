# How Amazon Textract Works with

IAM

Before you use IAM to manage access to Amazon Textract, you should understand what
IAM features are available to use with Amazon Textract. To get a high-level view of how
Amazon Textract and other AWS services work with IAM, see [AWS Services That
Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [Amazon Textract
  Identity-Based Policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [Amazon Textract
  Resource-Based Policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Authorization Based on
  Amazon Textract Tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [Amazon Textract IAM
  Roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## Amazon Textract

Identity-Based Policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources and the conditions under which actions are allowed or denied.
Amazon Textract supports specific actions, resources, and condition keys. To learn
about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Asynchronous actions in Amazon Textract require two action permissions to be given,
one for Start actions and one for Get actions. Additionally, if you are using an Amazon S3 bucket to
pass documents, you will need to grant your account read access.

In Amazon Textract, all policy actions start with:
`textract:`. For example, to grant someone permission to run
an Amazon Textract operation with the Amazon Textract `AnalyzeDocument` operation, you include
the `textract:AnalyzeDocument` action in their policy. Policy statements must
include either an `Action` or `NotAction` element.
Amazon Textract defines its own set of actions that describe tasks that you can
perform with this service.

To specify multiple actions in a single statement, separate them with commas as
follows.

```
"Action": [
      "textract:*action1*",
      "textract:*action2*"
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `Describe`, include the following
action.

```
`"Action": "textract:Describe*"`
```

For a list of Amazon Textract actions, see [Actions Defined by Amazon Textract](../../../IAM/latest/UserGuide/list_amazontextract.md#amazontextract-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazontextract.md#amazontextract-actions-as-permissions") in the
_IAM User Guide_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

For actions that supports resource-level permission, such as the [AnalyzeDocument](API_AnalyzeDocument.md "API_AnalyzeDocument.md") and [GetAdapter](API_GetAdapter.md "API_GetAdapter.md")operations, use the
ARN to indicate the resources:

```
"Resource": [
  # Adapter ARN
  "arn:aws:textract:<region>:<account-id>:/adapters/<adapter-id>",
  # Adapter version ARN
  "arn:aws:textract:<region>:<account-id>:/adapters/<adapter-id>/versions/<version>",
  # Use wildcard to indicate all versions under an adapter
  "arn:aws:textract:<region>:<account-id>:/adapters/<adapter-id>/versions/*"
]
```

### Condition Keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

Amazon Textract
does not provide any service-specific condition keys, but it does support using some
global condition keys. For a list of all AWS global condition keys, see [AWS Global Condition
Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

### Examples

To view examples of Amazon Textract identity-based policies, see [Amazon Textract Identity-Based
Policy Examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Amazon Textract

Resource-Based Policies

Amazon Textract does not support resource-based policies.

## Authorization Based on

Amazon Textract Tags

Amazon Textract resources supports tagging resources and controlling access based on tags.
You can use the [TagResource](../../../STS/latest/APIReference/API_TagResource.md "../../../STS/latest/APIReference/API_TagResource.md"),
[UntagResource](../../../STS/latest/APIReference/API_UntagResource.md "../../../STS/latest/APIReference/API_UntagResource.md"), and [ListTagsForResource](../../../STS/latest/APIReference/API_ListTagsForResource.md "../../../STS/latest/APIReference/API_ListTagsForResource.md")
operations to manage resource tags.

For access control based on tags, you can refer to [AccessTags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md").

## Amazon Textract IAM

Roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within
your AWS account that has specific permissions.

### Using Temporary

Credentials with Amazon Textract

You can use temporary credentials to sign in with federation, assume an IAM
role, or to assume a cross-account role. You obtain temporary security credentials by
calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

Amazon Textract supports using temporary credentials.

### Service-Linked

Roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other
services to complete an action on your behalf. Service-linked roles appear in your
IAM account and are owned by the service. An IAM administrator can view but not
edit the permissions for service-linked roles.

Amazon Textract does not support service-linked roles.

###### Note

Because Amazon Textract does not support service-linked roles, it does not support
AWS service principals. For more information about service principals, see
[AWS service principals](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-services "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md#principal-services") in the
_IAM User Guide_.

### Service Roles

This feature allows a service to assume a [service
role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") on your behalf. This role allows the service to access resources in
other services to complete an action on your behalf. Service roles appear in your
IAM account and are owned by the account. This means that an IAM administrator
can change the permissions for this role. However, doing so might break the
functionality of the service.

Amazon Textract supports service roles.

If you are using a service role, you should ensure that your account is secure by
limiting the scope of Amazon Textract access to only the resources that you're using. To
do this, attach a trust policy to your IAM service role. For more information, see
[Cross-service confused deputy prevention](cross-service-confused-deputy-prevention.md "cross-service-confused-deputy-prevention.md").
