

# Actions, resources, and condition keys for AWS User Subscriptions
<a name="list_user-subscriptions"></a>

AWS User Subscriptions (service prefix: `user-subscriptions`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-admin-setup-subscribe-management-account.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/user-subscriptions/user-subscriptions.json) for this service.

**Topics**
+ [Actions defined by AWS User Subscriptions](#list_user-subscriptions-actions-as-permissions)
+ [Resource types defined by AWS User Subscriptions](#list_user-subscriptions-resources-for-iam-policies)
+ [Condition keys for AWS User Subscriptions](#list_user-subscriptions-policy-keys)

## Actions defined by AWS User Subscriptions
<a name="list_user-subscriptions-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [CreateClaim](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_permissions.html)  | Grants permission to create a User subscription Claim |  | [user-subscriptions:CreateForSelf](#list_user-subscriptions-user-subscriptions_CreateForSelf) | Write | 
|   [CreateClaimAddOn](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_permissions.html)  | Grants permission to create a User subscription Claim add-on |  |   | Write | 
|   [DeleteAutoTopUpRule](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_permissions.html)  | Grants permission to delete a User subscription auto-top-up rule |  |   | Write | 
|   [DeleteClaim](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_permissions.html)  | Grants permission to delete a User subscription Claim |  |   | Write | 
|   [GetAutoTopUpRule](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_permissions.html)  | Grants permission to get a User subscription auto-top-up rule |  |   | Read | 
|   [GetEffectiveUsageLimit](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_permissions.html)  | Grants permission to get a User subscription effective usage limit |  |   | Read | 
|   [GetUsageLimitHistory](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_permissions.html)  | Grants permission to get User subscription usage limit history |  |   | Read | 
|   [ListApplicationClaims](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_permissions.html)  | Grants permission to list all User subscription Claims for Application |  |   | List | 
|   [ListClaimAddOns](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_permissions.html)  | Grants permission to list all User subscription Claim add-ons |  |   | List | 
|   [ListClaims](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_permissions.html)  | Grants permission to list all User subscription Claims |  |   | List | 
|   [ListEntitlements](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_permissions.html)  | Grants permission to list all User subscription entitlements |  |   | List | 
|   [ListUsageLimits](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_permissions.html)  | Grants permission to list all User subscription usage limits |  |   | List | 
|   [ListUserSubscriptions](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_permissions.html)  | Grants permission to list all User subscriptions |  |   | List | 
|   [SetAutoTopUpRule](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_permissions.html)  | Grants permission to set a User subscription auto-top-up rule |  |   | Write | 
|   [SetOverageConfig](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_permissions.html)  | Grants permission to set a User subscription overage configuration |  |   | Write | 
|   [SetUsageLimit](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_permissions.html)  | Grants permission to set a User subscription usage limit |  |   | Write | 
|   [UpdateClaim](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security_iam_permissions.html)  | Grants permission to update a User subscription Claim |  |   | Write | 

## Resource types defined by AWS User Subscriptions
<a name="list_user-subscriptions-resources-for-iam-policies"></a>

AWS User Subscriptions does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS User Subscriptions
<a name="list_user-subscriptions-policy-keys"></a>

AWS User Subscriptions defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [user-subscriptions:CreateForSelf](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by only allowing creation of User subscription Claims for the caller | Bool | 