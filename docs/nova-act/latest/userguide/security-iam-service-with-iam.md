# How Amazon Nova Act works with IAM

## How Amazon Nova Act works with IAM

Before you use IAM to manage access to Nova Act, learn what IAM features are available to use with Nova Act.

| IAM Feature                                                                                                                                              | Amazon Nova Act Support |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| [Identity-based policies](#security-iam-service-with-iam-id-based-policies "#security-iam-service-with-iam-id-based-policies")                           | Yes                     |
| [Resource-based policies](#security_iam_service-with-iam-resource-based-policies "#security_iam_service-with-iam-resource-based-policies")               | No                      |
| [Policy actions](#security-iam-service-with-iam-id-based-policies-actions "#security-iam-service-with-iam-id-based-policies-actions")                    | Yes                     |
| [Policy resources](#security-iam-service-with-iam-id-based-policies-resources "#security-iam-service-with-iam-id-based-policies-resources")              | Yes                     |
| [Policy condition keys](#security-iam-service-with-iam-id-based-policies-conditionkeys "#security-iam-service-with-iam-id-based-policies-conditionkeys") | Yes                     |
| [ACLs](#security-iam-service-with-iam-acls "#security-iam-service-with-iam-acls")                                                                        | No                      |
| [ABAC (tags in policies)](#security_iam_service-with-iam-tags "#security_iam_service-with-iam-tags")                                                     | No                      |
| [Temporary credentials](#security-iam-service-with-iam-roles-tempcreds "#security-iam-service-with-iam-roles-tempcreds")                                 | Yes                     |
| [Principal permissions](#security-iam-service-with-iam-roles-tempcreds "#security-iam-service-with-iam-roles-tempcreds")                                 | Yes                     |
| [Service roles](#security-iam-service-with-iam-roles "#security-iam-service-with-iam-roles")                                                             | No                      |
| [Service-linked roles](#security-iam-service-with-iam-roles-service-linked "#security-iam-service-with-iam-roles-service-linked")                        | Yes                     |

## Identity-based policies for Nova Act

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. You can’t specify the principal in an identity-based policy because it applies to the user or role to which it is attached. To learn about all of the elements that you use in a JSON policy, see [IAM JSON policy elements reference](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_.

## Resource-based Policies

Resource-based policies are JSON policy documents that you attach to a resource. Examples of resource-based policies are IAM role trust policies and Amazon S3 bucket policies. In services that support resource-based policies, service administrators can use them to control access to a specific resource.

Amazon Nova Act does not support resource-based policies

## Policy Actions for Nova Act

The `Action` element of an IAM identity-based policy describes the specific action or actions that will be allowed or denied by the policy. Policy actions usually have the same name as the associated AWS API operation. The action is used in a policy to grant permissions to perform the associated operation.

Policy actions in Amazon Nova Act use the following prefix before the action: `nova-act:`. For example, to grant someone permission to run an Amazon EC2 instance with the Amazon EC2
`RunInstances` API operation, you include the `ec2:RunInstances` action in their policy. Policy statements must include either an `Action` or `NotAction` element. Amazon Nova Act defines its own set of actions that describe tasks that you can perform with this service.

To specify multiple actions in a single statement, separate them with commas as follows:

```
"Action": [
      "ec2:action1",
      "ec2:action2"
]
```

You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `Describe`, include the following action:

```
"Action": "ec2:Describe*"
```

## Policy Resources for Nova Act

The `Resource` element specifies the object or objects to which the action applies. Statements must include either a `Resource` or a `NotResource` element. You specify a resource using an ARN or using the wildcard (\*) to indicate that the statement applies to all resources.

The Amazon EC2 instance resource has the following ARN:

```
arn:${Partition}:ec2:${Region}:${Account}:instance/${InstanceId}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS service Namespaces](../../../general/latest/gr/aws-arns-and-namespaces.md "../../../general/latest/gr/aws-arns-and-namespaces.md").

For example, to specify the `i-1234567890abcdef0` instance in your statement, use the following ARN:

```
"Resource": "arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0"
```

To specify all instances that belong to a specific account, use the wildcard (\*):

```
"Resource": "arn:aws:ec2:us-east-1:123456789012:instance/*"
```

Some Amazon Nova Act actions, such as those for creating resources, cannot be performed on a specific resource. In those cases, you must use the wildcard (\*).

```
"Resource": "*"
```

Many Amazon EC2 API actions involve multiple resources. For example, `AttachVolume` attaches an Amazon EBS volume to an instance, so an IAM user must have permissions to use the volume and the instance. To specify multiple resources in a single statement, separate the ARNs with commas.

```
"Resource": [
      "resource1",
      "resource2"
]
```

## Policy condition keys for Nova Act

The `Condition` element (or `Condition`_block_) lets you specify conditions in which a statement is in effect. The `Condition` element is optional. You can create conditional expressions that use [condition operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md"), such as equals or less than, to match the condition in the policy with values in the request.

If you specify multiple `Condition` elements in a statement, or multiple keys in a single `Condition` element, AWS evaluates them using a logical `AND` operation. If you specify multiple values for a single condition key, AWS evaluates the condition using a logical `OR` operation. All of the conditions must be met before the statement’s permissions are granted.

You can also use placeholder variables when you specify conditions. For example, you can grant an IAM user permission to access a resource only if it is tagged with their IAM user name. For more information, see [IAM policy elements: variables and tags](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md") in the _IAM User Guide_.

Amazon Nova Act defines its own set of condition keys and also supports using some global condition keys. To see all AWS global condition keys, see [AWS global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") in the _IAM User Guide_.

All Amazon EC2 actions support the `aws:RequestedRegion` and `ec2:Region` condition keys. For more information, see [Example: Restricting access to a specific region](../../../AWSEC2/latest/UserGuide/ExamplePolicies_EC2.md#iam-example-region "../../../AWSEC2/latest/UserGuide/ExamplePolicies_EC2.md#iam-example-region").

### Examples

To view examples of Amazon Nova Act identity-based policies, see [Amazon Nova Act identity-based policy examples](security-iam-id-based-policy-examples.md "security-iam-id-based-policy-examples.md").

## Access control lists (ACLs)

Access control lists (ACLs) control which principals (account members, users, or roles) have permissions to access a resource. ACLs are similar to resource-based policies, although they do not use the JSON policy document format.

Amazon Nova Act does not support ACLs.

## ABAC (tags in policies)

Attribute-based access control (ABAC) is an authorization strategy that defines permissions based on attributes called tags.

Amazon Nova Act does not support ABAC.

## Amazon Nova Act IAM roles

An [IAM role](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") is an entity within your AWS account that has specific permissions.

### Using temporary credentials with Amazon Nova Act

You can use temporary credentials to sign in with federation, assume an IAM role, or to assume a cross-account role. You obtain temporary security credentials by calling AWS STS API operations such as [AssumeRole](../../../STS/latest/APIReference/API_AssumeRole.md "../../../STS/latest/APIReference/API_AssumeRole.md") or [GetFederationToken](../../../STS/latest/APIReference/API_GetFederationToken.md "../../../STS/latest/APIReference/API_GetFederationToken.md").

Amazon Nova Act supports using temporary credentials.

## Service-linked roles for Nova Act

[Service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") allow AWS services to access resources in other services to complete an action on your behalf. Service-linked roles appear in your IAM account and are owned by the service. An IAM administrator can view but not edit the permissions for service-linked roles.

Amazon Nova Act supports service-linked roles. The service uses the NovaActServiceRolePolicy to publish operational metrics to CloudWatch. The service-linked role is automatically created when you start using Amazon Nova Act, and it uses the permissions defined in the NovaActServiceRolePolicy managed policy described in the [AWS managed policies for Amazon Nova Act](security-iam-awsmanpol.md "security-iam-awsmanpol.md") section.

## Service roles for Nova Act

This feature allows a service to assume a [service role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-role") on your behalf. This role allows the service to access resources in other services to complete an action on your behalf.

Amazon Nova Act does not support service roles.
