

# Actions, resources, and condition keys for AWS Tiros
<a name="list_tiros"></a>

AWS Tiros (service prefix: `tiros`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/vpc/latest/reachability/identity-access-management.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/tiros/tiros.json) for this service.

**Topics**
+ [Actions defined by AWS Tiros](#list_tiros-actions-as-permissions)
+ [Permission-only actions for AWS Tiros](#list_tiros-permission-only-actions)
+ [Resource types defined by AWS Tiros](#list_tiros-resources-for-iam-policies)
+ [Condition keys for AWS Tiros](#list_tiros-policy-keys)

## Actions defined by AWS Tiros
<a name="list_tiros-actions-as-permissions"></a>

AWS Tiros has no API operations that can be used in the `Actions` element of an IAM policy statement.

## Permission-only actions for AWS Tiros
<a name="list_tiros-permission-only-actions"></a>

The following actions are defined by AWS Tiros but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CreateQuery](https://docs.aws.amazon.com/vpc/latest/reachability/security_iam_required-API-permissions.html)  | Grants permission to create a VPC reachability query |  |   | Write | 
|   [ExtendQuery](https://docs.aws.amazon.com/vpc/latest/reachability/security_iam_required-API-permissions.html)  | Grants permission to extend a VPC reachability query to include the calling principals account |  |   | Write | 
|   [GetQueryAnswer](https://docs.aws.amazon.com/vpc/latest/reachability/security_iam_required-API-permissions.html)  | Grants permission to get VPC reachability query answers |  |   | Read | 
|   [GetQueryExplanation](https://docs.aws.amazon.com/vpc/latest/reachability/security_iam_required-API-permissions.html)  | Grants permission to get VPC reachability query explanations |  |   | Read | 
|   [GetQueryExtensionAccounts](https://docs.aws.amazon.com/vpc/latest/reachability/security_iam_required-API-permissions.html)  | Grants permission to list accounts that might be useful in a new query |  |   | Read | 

## Resource types defined by AWS Tiros
<a name="list_tiros-resources-for-iam-policies"></a>

AWS Tiros does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Tiros
<a name="list_tiros-policy-keys"></a>

AWS Tiros has no service-specific condition keys that can be used in the `Condition` element of policy statements.