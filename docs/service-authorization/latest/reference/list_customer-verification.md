# Actions, resources, and condition keys for AWS Customer Verification Service

AWS Customer Verification Service (service prefix: `customer-verification`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../awsaccountbilling/latest/aboutv2.md "../../../awsaccountbilling/latest/aboutv2.md").
- View a list of the [API operations available for
  this service](../../../awsaccountbilling/latest/aboutv2.md "../../../awsaccountbilling/latest/aboutv2.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md#user-permissions "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md#user-permissions") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/customer-verification/customer-verification.json "https://servicereference.us-east-1.amazonaws.com/v1/customer-verification/customer-verification.json") for this service.

###### Topics

- [Actions defined by AWS Customer Verification Service](#list_customer-verification-actions-as-permissions "#list_customer-verification-actions-as-permissions")
- [Permission-only actions for AWS Customer Verification Service](#list_customer-verification-permission-only-actions "#list_customer-verification-permission-only-actions")
- [Resource types defined by AWS Customer Verification Service](#list_customer-verification-resources-for-iam-policies "#list_customer-verification-resources-for-iam-policies")
- [Condition keys for AWS Customer Verification Service](#list_customer-verification-policy-keys "#list_customer-verification-policy-keys")

## Actions defined by AWS Customer Verification Service

AWS Customer Verification Service has no API operations that can be used in the
`Actions` element of an IAM policy statement.

## Permission-only actions for AWS Customer Verification Service

The following actions are defined by AWS Customer Verification Service but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                                                                                             | Description                                                | Resource types (\*required) | Condition keys | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [CreateCustomerVerificationDetails](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md#user-permissions "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md#user-permissions")  | Grants permission to create customer verification data     |                             |                | Write        |
| [CreateUploadUrls](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md#user-permissions "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md#user-permissions")                   | Grants permission to create upload URLs                    |                             |                | Write        |
| [GetCustomerVerificationDetails](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md#user-permissions "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md#user-permissions")     | Grants permission to get customer verification data        |                             |                | Read         |
| [GetCustomerVerificationEligibility](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md#user-permissions "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md#user-permissions") | Grants permission to get customer verification eligibility |                             |                | Read         |
| [UpdateCustomerVerificationDetails](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md#user-permissions "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md#user-permissions")  | Grants permission to update customer verification data     |                             |                | Write        |

## Resource types defined by AWS Customer Verification Service

AWS Customer Verification Service does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Customer Verification Service

AWS Customer Verification Service has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
