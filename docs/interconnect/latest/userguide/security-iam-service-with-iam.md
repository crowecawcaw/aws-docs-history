

# How AWS Interconnect works with IAM
<a name="security-iam-service-with-iam"></a>

Before you use IAM to manage access to AWS Interconnect, learn what IAM features are available to use with AWS Interconnect. To get a high-level view of how AWS Interconnect and other AWS services work with IAM, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

**Topics**
+ [AWS Interconnect Identity-based policies](#security-iam-service-with-iam-id-based-policies)
+ [Authorization based on AWS Interconnect tags](#security-iam-service-with-iam-tags)
+ [AWS Interconnect IAM roles](#security-iam-service-with-iam-roles)

## AWS Interconnect Identity-based policies
<a name="security-iam-service-with-iam-id-based-policies"></a>

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. You can’t specify the principal in an identity-based policy because it applies to the user or role to which it is attached. To learn about all of the elements that you use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

### Actions
<a name="security-iam-service-with-iam-id-based-policies-actions"></a>

The `Action` element of an IAM identity-based policy describes the specific action or actions that will be allowed or denied by the policy. Policy actions usually have the same name as the associated AWS API operation. The action is used in a policy to grant permissions to perform the associated operation.

Policy actions in AWS Interconnect use the following prefix before the action: `interconnect:`. For example, to grant someone permission to run an Amazon EC2 instance with the Amazon EC2 `RunInstances` API operation, you include the `ec2:RunInstances` action in their policy. Policy statements must include either an `Action` or `NotAction` element. AWS Interconnect defines its own set of actions that describe tasks that you can perform with this service.

To specify multiple actions in a single statement, separate them with commas as follows:

```
"Action": [
    "interconnect:CreateConnection",
    "interconnect:ListEnvironments"
]
```

You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `Describe`, include the following action:

```
"Action": "interconnect:Create*"
```

To see a list of AWS Interconnect actions, see [Actions Defined by AWS Interconnect](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsinterconnect.html#awsinterconnect-actions-as-permissions) in the *IAM User Guide*.

### Resources
<a name="security-iam-service-with-iam-id-based-policies-resources"></a>

The `Resource` element specifies the object or objects to which the action applies. Statements must include either a `Resource` or a `NotResource` element. You specify a resource using an ARN or using the wildcard (\*) to indicate that the statement applies to all resources.

The AWS Interconnect Connection resource has the following ARN:

```
arn:${Partition}:interconnect:${Region}:${Account}:connection/${ConnectionId}
```

For more information about the format of ARNs, see [Amazon Resource Names (ARNs) and AWS service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html).

For example, to specify the `mcc-12345678` connection in your statement, use the following ARN:

```
"Resource": "arn:aws:interconnect:us-east-1:123456789012:connection/mcc-12345678"
```

To specify all instances that belong to a specific account, use the wildcard (\*):

```
"Resource": "arn:aws:interconnect:us-east-1:123456789012:connection/*"
```

Some AWS Interconnect actions, such as those for creating resources, cannot be performed on a specific resource. In those cases, you must use the wildcard (\*).

```
"Resource": "*"
```

To see a list of AWS Interconnect resource types and their ARNs, see [Resources Defined by AWS Interconnect](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsinterconnect.html#awsinterconnect-resources-for-iam-policies) in the *IAM User Guide*. To learn with which actions you can specify the ARN of each resource, see [Actions Defined by AWS Interconnect](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsinterconnect.html#awsinterconnect-actions-as-permissions).

### Condition keys
<a name="security-iam-service-with-iam-id-based-policies-conditionkeys"></a>

The `Condition` element (or `Condition` *block*) lets you specify conditions in which a statement is in effect. The `Condition` element is optional. You can create conditional expressions that use [condition operators](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition_operators.html), such as equals or less than, to match the condition in the policy with values in the request.

If you specify multiple `Condition` elements in a statement, or multiple keys in a single `Condition` element, AWS evaluates them using a logical `AND` operation. If you specify multiple values for a single condition key, AWS evaluates the condition using a logical `OR` operation. All of the conditions must be met before the statement’s permissions are granted.

You can also use placeholder variables when you specify conditions. For example, you can grant an IAM user permission to access a resource only if it is tagged with their IAM user name. For more information, see [IAM policy elements: variables and tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html) in the *IAM User Guide*.

 AWS Interconnect defines its own set of condition keys and also supports using some global condition keys. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

All Amazon EC2 actions support the `aws:RequestedRegion` and `ec2:Region` condition keys. For more information, see [Example: Restricting access to a specific region](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ExamplePolicies_EC2.html#iam-example-region).

To see a list of AWS Interconnect condition keys, see [Condition Keys for AWS Interconnect](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsinterconnect.html#awsinterconnect-policy-keys) in the *IAM User Guide*. To learn with which actions and resources you can use a condition key, see [Actions defined by AWS Interconnect](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsinterconnect.html#awsinterconnect-actions-as-permissions).

### Examples
<a name="security-iam-service-with-iam-id-based-policies-examples"></a>

To view examples of AWS Interconnect identity-based policies, see [AWS Interconnect identity-based policy examples](security-iam-id-based-policy-examples.md).

## Authorization based on AWS Interconnect tags
<a name="security-iam-service-with-iam-tags"></a>

You can attach tags to AWS Interconnect resources or pass tags in a request to AWS Interconnect. To control access based on tags, you provide tag information in the [condition element](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) of a policy using the `interconnect:ResourceTag/key-name`, `aws:RequestTag/key-name`, or `aws:TagKeys` condition keys. For more information about tagging AWS Interconnect resources, see [AWS Interconnect TagResource API](https://docs.aws.amazon.com/interconnect/latest/api/API_TagResource.html).

To view an example identity-based policy for limiting access to a resource based on the tags on that resource, see [Viewing AWS Interconnect connections based on tags](security-iam-id-based-policy-examples.md#security-iam-id-based-policy-examples-view-connection-tags).

## AWS Interconnect IAM roles
<a name="security-iam-service-with-iam-roles"></a>

An [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) is an entity within your AWS account that has specific permissions.

### Using temporary credentials with AWS Interconnect
<a name="security-iam-service-with-iam-roles-tempcreds"></a>

You can use temporary credentials to sign in with federation, assume an IAM role, or to assume a cross-account role. You obtain temporary security credentials by calling AWS STS API operations such as [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) or [GetFederationToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetFederationToken.html).

 AWS Interconnect supports using temporary credentials.