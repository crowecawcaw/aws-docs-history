# Actions, resources, and condition keys for AWS User Subscriptions

AWS User Subscriptions (service prefix: `user-subscriptions`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../amazonq/latest/qdeveloper-ug/q-admin-setup-subscribe-management-account.md "../../../amazonq/latest/qdeveloper-ug/q-admin-setup-subscribe-management-account.md").
- View a list of the [API operations available for
  this service](../../../amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.md "../../../amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.md "../../../amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/user-subscriptions/user-subscriptions.json "https://servicereference.us-east-1.amazonaws.com/v1/user-subscriptions/user-subscriptions.json") for this service.

###### Topics

- [Actions defined by AWS User Subscriptions](#list_user-subscriptions-actions-as-permissions "#list_user-subscriptions-actions-as-permissions")
- [Resource types defined by AWS User Subscriptions](#list_user-subscriptions-resources-for-iam-policies "#list_user-subscriptions-resources-for-iam-policies")
- [Condition keys for AWS User Subscriptions](#list_user-subscriptions-policy-keys "#list_user-subscriptions-policy-keys")

## Actions defined by AWS User Subscriptions

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                         | Description                                                            | Resource types (\*required) | Condition keys                                                                                                                                            | Access level |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| [CreateClaim](../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md "../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md")            | Grants permission to create a User subscription Claim                  |                             | [user-subscriptions:CreateForSelf](#list_user-subscriptions-user-subscriptions_CreateForSelf "#list_user-subscriptions-user-subscriptions_CreateForSelf") | Write        |
| [CreateClaimAddOn](../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md "../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md")       | Grants permission to create a User subscription Claim add-on           |                             |                                                                                                                                                           | Write        |
| [DeleteAutoTopUpRule](../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md "../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md")    | Grants permission to delete a User subscription auto-top-up rule       |                             |                                                                                                                                                           | Write        |
| [DeleteClaim](../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md "../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md")            | Grants permission to delete a User subscription Claim                  |                             |                                                                                                                                                           | Write        |
| [GetAutoTopUpRule](../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md "../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md")       | Grants permission to get a User subscription auto-top-up rule          |                             |                                                                                                                                                           | Read         |
| [GetEffectiveUsageLimit](../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md "../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md") | Grants permission to get a User subscription effective usage limit     |                             |                                                                                                                                                           | Read         |
| [GetUsageLimitHistory](../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md "../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md")   | Grants permission to get User subscription usage limit history         |                             |                                                                                                                                                           | Read         |
| [ListApplicationClaims](../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md "../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md")  | Grants permission to list all User subscription Claims for Application |                             |                                                                                                                                                           | List         |
| [ListClaimAddOns](../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md "../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md")        | Grants permission to list all User subscription Claim add-ons          |                             |                                                                                                                                                           | List         |
| [ListClaims](../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md "../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md")             | Grants permission to list all User subscription Claims                 |                             |                                                                                                                                                           | List         |
| [ListEntitlements](../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md "../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md")       | Grants permission to list all User subscription entitlements           |                             |                                                                                                                                                           | List         |
| [ListUsageLimits](../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md "../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md")        | Grants permission to list all User subscription usage limits           |                             |                                                                                                                                                           | List         |
| [ListUserSubscriptions](../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md "../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md")  | Grants permission to list all User subscriptions                       |                             |                                                                                                                                                           | List         |
| [SetAutoTopUpRule](../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md "../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md")       | Grants permission to set a User subscription auto-top-up rule          |                             |                                                                                                                                                           | Write        |
| [SetOverageConfig](../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md "../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md")       | Grants permission to set a User subscription overage configuration     |                             |                                                                                                                                                           | Write        |
| [SetUsageLimit](../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md "../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md")          | Grants permission to set a User subscription usage limit               |                             |                                                                                                                                                           | Write        |
| [UpdateClaim](../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md "../../../amazonq/latest/qdeveloper-ug/security_iam_permissions.md")            | Grants permission to update a User subscription Claim                  |                             |                                                                                                                                                           | Write        |

## Resource types defined by AWS User Subscriptions

AWS User Subscriptions does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS User Subscriptions

AWS User Subscriptions defines the following condition keys that can be used in the
`Condition` element of an IAM policy.

| Condition keys                                                                                                                                                                                                                                                                                                  | Description                                                                         | Type |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ---- |
| [user-subscriptions:CreateForSelf](../../../amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.md#security_iam_service-with-iam-id-based-policies-conditionkeys "../../../amazonq/latest/qdeveloper-ug/security-iam-service-with-iam.md#security_iam_service-with-iam-id-based-policies-conditionkeys") | Filters access by only allowing creation of User subscription Claims for the caller | Bool |
