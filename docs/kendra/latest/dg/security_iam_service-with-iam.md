# How Amazon Kendra works with

IAM

Before you use IAM to manage access to Amazon Kendra, you should understand what
IAM features are available to use with Amazon Kendra. To get a high-level view of how
Amazon Kendra and other AWS services work with IAM, see [AWS Services That
Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [Amazon Kendra
  identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [Amazon Kendra
  Resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Access control lists (ACLs)](#security_iam_service-with-iam-acls "#security_iam_service-with-iam-acls")
- [Authorization based on
  Amazon Kendra tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [Amazon Kendra IAM
  Roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## Amazon Kendra

identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied.
Amazon Kendra supports specific actions, resources, and condition keys. To learn
about all of the elements that you use in a JSON policy, see [IAM JSON Policy Elements
Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in Amazon Kendra use the following prefix before the action:
`kendra:`. For example, to grant someone permission to list
Amazon Kendra indexes with the [ListIndices](API_ListIndices.md "API_ListIndices.md") API operation, you
include the `kendra:ListIndices` action in their policy.
Policy statements must include either an `Action` or
`NotAction` element. Amazon Kendra defines its own set of actions
that describe tasks that you can perform with this service.

To specify multiple actions in a single statement, separate them with commas as
follows:

```
"Action": [
      "kendra:*action1*",
      "kendra:*action2*"
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `Describe`, include the following
action:

```
`"Action": "kendra:Describe*"`
```

To see a list of Amazon Kendra actions, see [Actions Defined by Amazon Kendra](../../../IAM/latest/UserGuide/list_kendra.md#kendra-actions-as-permissions "../../../IAM/latest/UserGuide/list_kendra.md#kendra-actions-as-permissions") in the
_IAM User Guide_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

The Amazon Kendra index resource has the following ARN:

```
arn:${Partition}:kendra:${Region}:${Account}:index/${IndexId}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS Service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

For example, to specify an index in your statement, use the GUID of the index in
the following ARN:

```
"Resource": "arn:aws:kendra:${Region}:${Account}:index/${GUID}"
```

To specify all indexes that belong to a specific account, use the wildcard
(\*):

```
"Resource": "arn:aws:${Region}:${Account}:index/*"
```

Some Amazon Kendra actions, such as those for creating resources, cannot be
performed on a specific resource. In those cases, you must use the wildcard
(\*).

```
"Resource": "*"
```

To see a list of Amazon Kendra resource types and their ARNs, see
[Resources Defined by Amazon Kendra](../../../IAM/latest/UserGuide/list_kendra.md#kendra-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_kendra.md#kendra-resources-for-iam-policies") in the _IAM User Guide_. To learn
with which actions you can specify the ARN of each resource, see
[Actions Defined by Amazon Kendra](../../../IAM/latest/UserGuide/list_kendra.md#kendra-actions-as-permissions "../../../IAM/latest/UserGuide/list_kendra.md#kendra-actions-as-permissions").

### Condition keys

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Condition` element specifies when statements execute based on defined criteria. You can create conditional expressions that use [condition
operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the
policy with values in the request. To see all AWS global
condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

Amazon Kendra does not provide any service-specific condition keys, but it does
support using some global condition keys. To see all AWS global condition keys, see
[AWS Global
Condition Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the
_IAM User Guide_.

### Examples

To view examples of Amazon Kendra identity-based policies, see [Amazon Kendra Identity-based
policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## Amazon Kendra

Resource-based policies

Amazon Kendra does not support resource-based policies.

## Access control lists (ACLs)

Amazon Kendra does not support access control lists (ACLs) for access to AWS
services and resources.

## Authorization based on

Amazon Kendra tags

You can associate tags with certain types of Amazon Kendra resources to authorize
access to those resources. To control access based on tags, provide tag information in
the condition element of a policy by using the
`aws:RequestTag/`key-name``, or
 `aws:TagKeys` condition keys.

The following table lists the actions, corresponding resource types, and condition
keys for tag-based access control. Each action is authorized based on the tags
associated with the corresponding resource type.

| Action                                                                             | Resource type           | Condition keys                  |
| ---------------------------------------------------------------------------------- | ----------------------- | ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [CreateDataSource](API_CreateDataSource.md "API_CreateDataSource.md")              |                         | `aws:RequestTag`, `aws:TagKeys` |
| [CreateFaq](API_CreateFaq.md "API_CreateFaq.md")                                   |                         | `aws:RequestTag`, `aws:TagKeys` |
| [CreateIndex](API_CreateIndex.md "API_CreateIndex.md")                             |                         | `aws:RequestTag`, `aws:TagKeys` |
| [API_ListTagsForResource](API_ListTagsForResource.md "API_ListTagsForResource.md") | data source, FAQ, index |                                 |
| [TagResource](API_TagResource.md "API_TagResource.md")                             | data source, FAQ, index | `aws:RequestTag`, `aws:TagKeys` |
| [UntagResource](API_UntagResource.md "API_UntagResource.md")                       | data source, FAQ, index | `aws:TagKeys`                   | For information about tagging Amazon Kendra resources, see [Tags](tagging.md "tagging.md"). For an example identity-based policy that limits access to a resource based on resource tags, see [Tag-based policy examples](security_iam_id-based-policy-examples.md#examples-tagging "security_iam_id-based-policy-examples.md#examples-tagging"). For more information about using tags to limit access to resources, see [Controlling access using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md") in the _IAM User Guide_. ## Amazon Kendra IAM Roles An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within your AWS account that has specific permissions. ### Using temporary credentials with Amazon Kendra You can use temporary credentials to sign in with federation, assume an IAM role, or to assume a cross-account role. You obtain temporary security credentials by calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md"). Amazon Kendra supports using temporary credentials. ### Service roles This feature allows a service to assume a [service role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") on your behalf. This role allows the service to access resources in other services to complete an action on your behalf. Service roles appear in your IAM account and are owned by the account. This means that an IAM administrator can change the permissions for this role. However, doing so might break the functionality of the service. Amazon Kendra supports service roles. ### Choosing an IAM role in Amazon Kendra When you create an index, call the `BatchPutDocument` operation, create a data source or create an FAQ, you must provide an access role Amazon Resource Name (ARN) that Amazon Kendra uses to access the required resources on your behalf. If you have previously created a role, then the Amazon Kendra console provides you with a list of roles to choose from. It's important to choose a role that allows access to the resources that you require. For more information, see [IAM access roles for Amazon Kendra](iam-roles.md "iam-roles.md"). |
