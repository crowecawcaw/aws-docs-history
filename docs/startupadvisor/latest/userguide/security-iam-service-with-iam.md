

# How AWS Startups works with IAM
<a name="security-iam-service-with-iam"></a>

Before you use IAM to manage access to AWS Startups, learn what IAM features are available to use with AWS Startups. To get a high-level view of how AWS Startups and other AWS services work with IAM, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) in the *IAM User Guide*.

 AWS Startups exposes the operation `startups:GetSpendSummary`, which the IDE extension calls to power the AWS credits and cost tracker widget. The IDE extension calls this operation with your own AWS profile credentials. AWS Startups then uses a forward-access session to call AWS Cost Explorer and AWS Billing and Cost Management on your behalf.

Because the operation runs with your identity rather than a separate service role, your identity must have permission for both `startups:GetSpendSummary` and the downstream actions that the operation calls on your behalf: `ce:GetCostAndUsage`, `ce:GetCostForecast`, `billing:GetCredits`, and `aws-portal:ViewBilling`. The `aws-portal:ViewBilling` permission is required in addition to the other three.

No AWS Startups action supports resource-level permissions, so you must set the `Resource` element to ` ` (an asterisk). In this case, `Resource: "` is expected. The least-privilege control is the scoped `Action` element. Grant only the specific actions that the operation requires. Do not use wildcard actions such as `startups:*` or `ce:*`.

There is no AWS managed policy for this feature. Use a customer managed or inline identity-based policy that grants only the required actions. For an example, see [AWS Startups identity-based policy examples](security-iam-id-based-policy-examples.md).

**Topics**
+ [AWS Startups Identity-based policies](#security-iam-service-with-iam-id-based-policies)
+ [AWS Startups IAM roles](#security-iam-service-with-iam-roles)

## AWS Startups Identity-based policies
<a name="security-iam-service-with-iam-id-based-policies"></a>

With IAM identity-based policies, you can specify allowed or denied actions and resources as well as the conditions under which actions are allowed or denied. You can’t specify the principal in an identity-based policy because it applies to the user or role to which it is attached. To learn about all of the elements that you use in a JSON policy, see [IAM JSON policy elements reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html) in the *IAM User Guide*.

### Actions
<a name="security-iam-service-with-iam-id-based-policies-actions"></a>

The `Action` element of an IAM identity-based policy describes the specific action or actions that will be allowed or denied by the policy. Policy actions usually have the same name as the associated AWS API operation. The action is used in a policy to grant permissions to perform the associated operation.

Policy actions in AWS Startups use the `startups:` prefix before the action. For example, to grant permission to call the GetSpendSummary operation, include the `startups:GetSpendSummary` action in your policy. Policy statements must include either an `Action` or `NotAction` element. AWS Startups defines its own set of actions that describe tasks that you can perform with this service.

To specify multiple actions in a single statement, separate them with commas as follows:

```
"Action": [
      "startups:GetSpendSummary",
      "ce:GetCostAndUsage",
      "billing:GetCredits",
      "aws-portal:ViewBilling"
]
```

To see a list of AWS Startups actions, see [Actions Defined by AWS Startups](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_awskeymanagementservice.html#awskeymanagementservice-actions-as-permissions) in the *IAM User Guide*.

### Resources
<a name="security-iam-service-with-iam-id-based-policies-resources"></a>

No AWS Startups action can be performed on a specific resource. For this reason, you must set the `Resource` element to `*` (an asterisk) in your policies.

### Condition keys
<a name="security-iam-service-with-iam-id-based-policies-conditionkeys"></a>

 AWS Startups does not define any service-specific condition keys. You can use the global condition context keys that are available to all AWS services. For the list, see [AWS global condition context keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html) in the *IAM User Guide*.

### Examples
<a name="security-iam-service-with-iam-id-based-policies-examples"></a>

To view examples of AWS Startups identity-based policies, see [AWS Startups identity-based policy examples](security-iam-id-based-policy-examples.md).

## AWS Startups IAM roles
<a name="security-iam-service-with-iam-roles"></a>

An [IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) is an entity within your AWS account that has specific permissions.

### Using temporary credentials with AWS Startups
<a name="security-iam-service-with-iam-roles-tempcreds"></a>

You can use temporary credentials to sign in with federation, assume an IAM role, or to assume a cross-account role. You obtain temporary security credentials by calling AWS STS API operations such as [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) or [GetFederationToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetFederationToken.html).

 AWS Startups supports using temporary credentials.

### Service roles and service-linked roles
<a name="security-iam-service-with-iam-roles-service"></a>

 AWS Startups does not use service roles or service-linked roles. When AWS Startups calls downstream services, such as AWS Cost Explorer and AWS Billing and Cost Management, it uses your own credentials through a forward-access session rather than a role that the service owns.