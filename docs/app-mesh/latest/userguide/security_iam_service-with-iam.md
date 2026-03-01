# How AWS App Mesh works with IAM

###### Important

End of support notice: On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources. For more information, visit this blog post [Migrating from AWS App Mesh to Amazon ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect "https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect").

Before you use IAM to manage access to App Mesh, you should understand what
IAM features are available to use with App Mesh. To get a high-level view of how
App Mesh and other AWS services work with IAM, see [AWS Services
That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_.

###### Topics

- [App Mesh identity-based policies](#security_iam_service-with-iam-id-based-policies "#security_iam_service-with-iam-id-based-policies")
- [App Mesh resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")
- [Authorization based on App Mesh tags](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")
- [App Mesh IAM roles](#security_iam_service-with-iam-roles "#security_iam_service-with-iam-roles")

## App Mesh identity-based policies

With IAM identity-based policies, you can specify allowed or denied actions and
resources as well as the conditions under which actions are allowed or denied.
App Mesh supports specific actions, resources, and condition keys. To learn
about all of the elements that you use in a JSON policy, see [IAM JSON Policy
Elements Reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

### Actions

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the
actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Policy actions in App Mesh use the following prefix before the action:
`appmesh:`. For example, to grant someone permission to list
meshes in an account with the `appmesh:ListMeshes` API
operation, you include the `appmesh:ListMeshes` action in their
policy. Policy statements must include either an `Action` or
`NotAction` element.

To specify multiple actions in a single statement, separate them with commas as
follows.

```
"Action": [
      "appmesh:*ListMeshes*",
      "appmesh:*ListVirtualNodes*"
]
```

You can specify multiple actions using wildcards (\*). For example, to specify all
actions that begin with the word `Describe`, include the following
action.

```
`"Action": "appmesh:Describe*"`
```

To see a list of App Mesh actions, see [Actions Defined by AWS App Mesh](../../../IAM/latest/UserGuide/list_awsappmesh.md#awsappmesh-actions-as-permissions "../../../IAM/latest/UserGuide/list_awsappmesh.md#awsappmesh-actions-as-permissions") in the
_IAM User Guide_.

### Resources

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform
**actions** on what **resources**, and under what **conditions**.

The `Resource` JSON policy element specifies the object or objects to which the action applies. As a best practice, specify a resource using its [Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md"). For actions that don't support resource-level permissions, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

The App Mesh `mesh` resource has the following ARN.

```
arn:${Partition}:appmesh:${Region}:${Account}:mesh/${MeshName}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs)
and AWS Service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

For example, to specify the mesh named `apps` in the
`Region-code` Region in your statement, use the following
ARN.

```
arn:aws:appmesh:`Region-code`:`111122223333`:mesh/`apps`
```

To specify all instances that belong to a specific account, use the wildcard
(\*).

```
"Resource": "arn:aws:appmesh:`Region-code`:`111122223333`:mesh/*"
```

Some App Mesh actions, such as those for creating resources, cannot be
performed on a specific resource. In those cases, you must use the wildcard
(\*).

```
"Resource": "*"
```

Many App Mesh API actions involve multiple resources. For example,
`CreateRoute` creates a route with a virtual node target, so an
IAM user must have permissions to use the route and the virtual node. To specify
multiple resources in a single statement, separate the ARNs with commas.

```
"Resource": [
      "*arn:aws:appmesh:`Region-code`:`111122223333`:mesh/`apps`/virtualRouter/`serviceB`/route/\**",
      "*arn:aws:appmesh:`Region-code`:`111122223333`:mesh/`apps`/virtualNode/`serviceB`*"
]
```

To see a list of App Mesh resource types and their ARNs, see
[Resources Defined by AWS App Mesh](../../../IAM/latest/UserGuide/list_awsappmesh.md#awsappmesh-resources-for-iam-policies "../../../IAM/latest/UserGuide/list_awsappmesh.md#awsappmesh-resources-for-iam-policies") in the _IAM User Guide_. To learn
with which actions you can specify the ARN of each resource, see
[Actions Defined by AWS App Mesh](../../../IAM/latest/UserGuide/list_awsappmesh.md#awsappmesh-actions-as-permissions "../../../IAM/latest/UserGuide/list_awsappmesh.md#awsappmesh-actions-as-permissions").

### Condition keys

App Mesh supports using some global condition keys. To see all AWS
global condition keys, see [AWS Global
Condition Context Keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_. To
see a list of the global condition keys that App Mesh supports, see
[Condition Keys for AWS App Mesh](../../../IAM/latest/UserGuide/list_awsappmesh.md#awsappmesh-policy-keys "../../../IAM/latest/UserGuide/list_awsappmesh.md#awsappmesh-policy-keys") in the _IAM User Guide_. To learn
with which actions and resources you can use with a condition key, see
[Actions Defined by AWS App Mesh](../../../IAM/latest/UserGuide/list_awsappmesh.md#awsappmesh-actions-as-permissions "../../../IAM/latest/UserGuide/list_awsappmesh.md#awsappmesh-actions-as-permissions").

### Examples

To view examples of App Mesh identity-based policies, see [AWS App Mesh identity-based policy examples](security_iam_id-based-policy-examples.md "security_iam_id-based-policy-examples.md").

## App Mesh resource-based policies

App Mesh doesn't support resource-based policies. However, if you use the
AWS Resource Access Manager (AWS RAM) service to share a mesh across AWS services, a resource-based policy
is applied to your mesh by the AWS RAM service. For more information, see [Granting permissions for a mesh](sharing.md#sharing-permissions-resource "sharing.md#sharing-permissions-resource").

## Authorization based on App Mesh tags

You can attach tags to App Mesh resources or pass tags in a request to
App Mesh. To control access based on tags, you provide tag information in the
[condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the
`appmesh:ResourceTag/`key-name``,
 `aws:RequestTag/`key-name``, or
`aws:TagKeys` condition keys. For more information about tagging
App Mesh resources, see [Tagging AWS Resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md").

To view an example identity-based policy for limiting access to a resource based on
the tags on that resource, see [Creating App Mesh meshes with restricted tags](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-view-widget-tags "security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-view-widget-tags").

## App Mesh IAM roles

An [IAM
role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within your AWS account that has specific
permissions.

### Using temporary credentials with App Mesh

You can use temporary credentials to sign in with federation, assume an IAM
role, or to assume a cross-account role. You obtain temporary security credentials by
calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

App Mesh supports using temporary credentials.

### Service-linked roles

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other
services to complete an action on your behalf. Service-linked roles appear in your
IAM account and are owned by the service. An IAM administrator can view but not
edit the permissions for service-linked roles.

App Mesh supports service-linked roles. For details about creating or
managing App Mesh service-linked roles, see [Using service-linked roles for App Mesh](using-service-linked-roles.md "using-service-linked-roles.md").

### Service roles

This feature allows a service to assume a [service role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") on your behalf. This role allows the service to access
resources in other services to complete an action on your behalf. Service roles
appear in your IAM account and are owned by the account. This means that an IAM
administrator can change the permissions for this role. However, doing so might break
the functionality of the service.

App Mesh does not support service roles.
