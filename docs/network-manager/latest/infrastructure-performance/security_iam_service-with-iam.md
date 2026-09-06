

# How Infrastructure Performance works with IAM
<a name="security_iam_service-with-iam"></a>

The following sections describe how Infrastructure Performance works with IAM.

**Topics**
+ [Infrastructure Performance identity-based policies](#security_iam_service-with-iam-id-based-policies)
+ [Infrastructure Performance IAM roles](#security_iam_service-with-iam-roles)

## Infrastructure Performance identity-based policies
<a name="security_iam_service-with-iam-id-based-policies"></a>

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. Infrastructure Performance supports specific actions and resources. There are no Infrastructure Performance service-specific condition keys that can be used in the `Condition` element of policy statements. To learn about all of the elements that you use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

### Actions
<a name="security_iam_service-with-iam-id-based-policies-actions"></a>

Administrators can use AWS JSON policies to specify who has access to what. That is, which **principal** can perform **actions** on what **resources**, and under what **conditions**.

The `Action` element of a JSON policy describes the actions that you can use to allow or deny access in a policy. Include actions in a policy to grant permissions to perform the associated operation.

Infrastructure Performance shares its API namespace with Amazon EC2. Policy actions in Infrastructure Performance use the following prefix before the action: `ec2`:. For example, to grant someone permission to create a path with the `GetAwsNetworkPerformanceData` API operation, you include the `ec2:GetAwsNetworkPerformanceData` action in their policy. Policy statements must include either an `Action` or `NotAction` element. 

To specify multiple actions in a single statement, separate them with commas as shown in the following example.

```
"Action": [
      "ec2:action1",
      "ec2:action2"
]
```

You can specify multiple actions using wildcards (\*). For example, to specify all actions that begin with the word `Describe`, include the following action.

```
"Action": "ec2:Describe*"
```

The following actions are supported by Infrastructure Performance:
+ `DescribeAwsNetworkPerformanceMetricSubscriptions`
+ `DisableAwsNetworkPerformanceMetricSubscription`
+ `EnableAwsNetworkPerformanceMetricSubscription`
+ `GetAwsNetworkPerformanceData`

### Resources
<a name="security_iam_service-with-iam-id-based-policies-resources"></a>

 Infrastructure Performance does not support resource-level permissions. 

For actions that don't support resource-level permissions, such as listing operations, use a wildcard (\*) to indicate that the statement applies to all resources.

```
"Resource": "*"
```

### Condition keys
<a name="security_iam_service-with-iam-id-based-policies-conditionkeys"></a>

The `Condition` element (or `Condition` *block*) lets you specify conditions in which a statement is in effect. For example, you might want a policy to be applied only after a specific date. To express conditions, use predefined condition keys.

Infrastructure Performance does not provide any service-specific condition keys, but it does support using some global condition keys. To see all AWS global condition keys, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*. 

All Amazon EC2 actions support the `aws:RequestedRegion` and `ec2:Region` condition keys. For more information, see [Example: Restricting Access to a Specific Region](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ExamplePolicies_EC2.html#iam-example-region). 

The `Condition` element is optional. 

## Infrastructure Performance IAM roles
<a name="security_iam_service-with-iam-roles"></a>

An [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) is an entity within your AWS account that has specific permissions.

### Using temporary credentials with Infrastructure Performance
<a name="security_iam_service-with-iam-roles-tempcreds"></a>

You can use temporary credentials to sign in with federation, to assume an IAM role, or to assume a cross-account role. You obtain temporary security credentials by calling AWS STS API operations such as [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) or [GetFederationToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetFederationToken.html).

Infrastructure Performance supports using temporary credentials.

### Service-linked roles
<a name="security_iam_service-with-iam-roles-service-linked"></a>

Infrastructure Performance has no service-linked roles.

### Service roles
<a name="security_iam_service-with-iam-roles-service"></a>

Infrastructure Performance has no service roles.