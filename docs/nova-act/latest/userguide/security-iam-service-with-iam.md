

# How Amazon Nova Act works with IAM
<a name="security-iam-service-with-iam"></a>

## How Amazon Nova Act works with IAM
<a name="_how_amazon_nova_act_works_with_iam"></a>

Before you use IAM to manage access to Nova Act, learn what IAM features are available to use with Nova Act.


| IAM Feature | Amazon Nova Act Support | 
| --- | --- | 
|  [Identity-based policies](#security-iam-service-with-iam-id-based-policies)  | Yes | 
|  [Resource-based policies](#security_iam_service-with-iam-resource-based-policies)  | No | 
|  [Policy actions](#security-iam-service-with-iam-id-based-policies-actions)  | Yes | 
|  [Policy resources](#security-iam-service-with-iam-id-based-policies-resources)  | Yes | 
|  [Policy condition keys](#security-iam-service-with-iam-id-based-policies-conditionkeys)  | Yes | 
|  [ACLs](#security-iam-service-with-iam-acls)  | No | 
|  [ABAC (tags in policies)](#security_iam_service-with-iam-tags)  | No | 
|  [Temporary credentials](#security-iam-service-with-iam-roles-tempcreds)  | Yes | 
|  [Principal permissions](#security-iam-service-with-iam-roles-tempcreds)  | Yes | 
|  [Service roles](#security-iam-service-with-iam-roles)  | No | 
|  [Service-linked roles](#security-iam-service-with-iam-roles-service-linked)  | Yes | 

## Identity-based policies for Nova Act
<a name="security-iam-service-with-iam-id-based-policies"></a>

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. You can’t specify the principal in an identity-based policy because it applies to the user or role to which it is attached. To learn about all of the elements that you use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

## Resource-based Policies
<a name="security_iam_service-with-iam-resource-based-policies"></a>

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM role trust policies and Amazon S3 bucket policies. In services that support resource-based policies, service administrators can use them to control access to a specific resource.

Amazon Nova Act does not support resource-based policies

## Policy Actions for Nova Act
<a name="security-iam-service-with-iam-id-based-policies-actions"></a>

The `Action` element of an IAM identity-based policy describes the specific action or actions that will be allowed or denied by the policy. Policy actions usually have the same name as the associated AWS API operation. The action is used in a policy to grant permissions to perform the associated operation.

Policy actions in Amazon Nova Act use the following prefix before the action: `nova-act:`. For example, to grant someone permission to create a workflow definition with the Amazon Nova Act `CreateWorkflowDefinition` API operation, you include the `nova-act:CreateWorkflowDefinition` action in their policy. Policy statements must include either an `Action` or `NotAction` element. Amazon Nova Act defines its own set of actions that describe tasks that you can perform with this service.

To specify multiple actions in a single statement, separate them with commas as follows:

```
"Action": [
      "nova-act:CreateWorkflowDefinition",
      "nova-act:GetWorkflowDefinition"
]
```

You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `List`, include the following action:

```
"Action": "nova-act:List*"
```

To see the complete list of Amazon Nova Act actions, see [Actions Defined by Amazon Nova Act](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonnovaact.html#amazonnovaact-actions-as-permissions) in the *IAM User Guide*.

## Policy Resources for Nova Act
<a name="security-iam-service-with-iam-id-based-policies-resources"></a>

The `Resource` element specifies the object or objects to which the action applies. Statements must include either a `Resource` or a `NotResource` element. You specify a resource using an ARN or using the wildcard (\*) to indicate that the statement applies to all resources.

The following resource types are defined by this service and can be used in the Resource element of IAM permission policy statements. Each action in the Actions table identifies the resource types that can be specified with that action. A resource type can also define which condition keys you can include in a policy. These keys are displayed in the last column of the Resource types table. For details about the columns in the following table, see [Resource types](https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html#resources_table) table.


| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
| workflow-definition | arn:${Partition}:nova-act:${Region}:${Account}:workflow-definition/${WorkflowDefinitionName} | N/A | 
| workflow-run | arn:${Partition}:nova-act:${Region}:${Account}:workflow-definition/${WorkflowDefinitionName}/workflow-run/${WorkflowRunId} | N/A | 

Amazon Nova Act workflow definition resources have the following ARN:

```
arn:${Partition}:nova-act:${Region}:${Account}:workflow-definition/${WorkflowDefinitionId}
```

Amazon Nova Act workflow run resources have the following ARN:

```
arn:${Partition}:nova-act:${Region}:${Account}:workflow-definition/${WorkflowDefinitionId}/workflow-run/${WorkflowRunId}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).

For example, to specify a specific workflow definition in your statement, use the following ARN:

```
"Resource": "arn:aws:nova-act:us-east-1:123456789012:workflow-definition/my-workflow-123"
```

To specify a specific workflow run in your statement, use the following ARN:

```
"Resource": "arn:aws:nova-act:us-east-1:123456789012:workflow-run/a1b2c3d4-e5f6-7890-abcd-ef1234567890"
```

To specify all workflow definitions that belong to a specific account, use the wildcard (\*):

```
"Resource": "arn:aws:nova-act:us-east-1:123456789012:workflow-definition/*"
```

Some Amazon Nova Act actions, such as those for creating resources, cannot be performed on a specific resource. In those cases, you must use the wildcard (\*).

```
"Resource": "*"
```

Some Amazon Nova Act API actions may be used across multiple resources. For example, an IAM user may need permissions to access multiple workflow runs. To specify multiple resources in a single statement, separate the ARNs with commas.

```
"Resource": [
      "arn:aws:nova-act:us-east-1:123456789012:workflow-run/a1b2c3d4-e5f6-7890-abcd-ef1234567890",
      "arn:aws:nova-act:us-east-1:123456789012:workflow-run/b2c3d4e5-f6a7-8901-bcde-f12345678901"
]
```

## Policy condition keys for Nova Act
<a name="security-iam-service-with-iam-id-based-policies-conditionkeys"></a>

The `Condition` element (or `Condition`block) lets you specify conditions in which a statement is in effect. The `Condition` element is optional. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request.

If you specify multiple `Condition` elements in a statement, or multiple keys in a single `Condition` element, AWS evaluates them using a logical `AND` operation. If you specify multiple values for a single condition key, AWS evaluates the condition using a logical `OR` operation. All of the conditions must be met before the statement’s permissions are granted.

You can also use placeholder variables when you specify conditions. For example, you can grant an IAM user permission to access a resource only if it is tagged with their IAM user name. For more information, see [IAM policy elements: variables and tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html) in the *IAM User Guide*.

Amazon Nova Act does not define any service-specific condition keys. However, you can use standard AWS global condition keys with Amazon Nova Act resources and actions. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

Amazon Nova Act actions support the `aws:RequestedRegion` condition key. You can use this condition key to restrict access to Amazon Nova Act operations to specific AWS Regions.

### Examples
<a name="security-iam-service-with-iam-id-based-policies-examples"></a>

To view examples of Amazon Nova Act identity-based policies, see [Amazon Nova Act identity-based policy examples](security-iam-id-based-policy-examples.md).

## Access control lists (ACLs)
<a name="security-iam-service-with-iam-acls"></a>

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

Amazon Nova Act does not support ACLs.

## ABAC (tags in policies)
<a name="security_iam_service-with-iam-tags"></a>

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes called tags.

Amazon Nova Act does not support ABAC.

## Amazon Nova Act IAM roles
<a name="security-iam-service-with-iam-roles"></a>

An [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) is an entity within your AWS account that has specific permissions.

### Using temporary credentials with Amazon Nova Act
<a name="security-iam-service-with-iam-roles-tempcreds"></a>

You can use temporary credentials to sign in with federation, assume an IAM role, or to assume a cross-account role. You obtain temporary security credentials by calling AWS STS API operations such as [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) or [GetFederationToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetFederationToken.html).

Amazon Nova Act supports using temporary credentials.

## Service-linked roles for Nova Act
<a name="security-iam-service-with-iam-roles-service-linked"></a>

 [Service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role) allow AWS services to access resources in other services to complete an action on your behalf. Service-linked roles appear in your IAM account and are owned by the service. An IAM administrator can view but not edit the permissions for service-linked roles.

Amazon Nova Act supports service-linked roles. The service uses the NovaActServiceRolePolicy to publish operational metrics to CloudWatch. The service-linked role is automatically created when you start using Amazon Nova Act, and it uses the permissions defined in the NovaActServiceRolePolicy managed policy described in the [AWS managed policies for Amazon Nova Act](security-iam-awsmanpol.md) section.

## Service roles for Nova Act
<a name="security-iam-service-with-iam-roles-service"></a>

This feature allows a service to assume a [service role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-role) on your behalf. This role allows the service to access resources in other services to complete an action on your behalf.

Amazon Nova Act does not support service roles.