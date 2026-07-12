# Actions, resources, and condition keys for AWS Consolidated Billing

AWS Consolidated Billing (service prefix: `consolidatedbilling`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../awsaccountbilling/latest/aboutv2/billing-what-is.md "../../../awsaccountbilling/latest/aboutv2/billing-what-is.md").
- View a list of the [API operations available for
  this service](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../awsaccountbilling/latest/aboutv2/security-iam.md "../../../awsaccountbilling/latest/aboutv2/security-iam.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/consolidatedbilling/consolidatedbilling.json "https://servicereference.us-east-1.amazonaws.com/v1/consolidatedbilling/consolidatedbilling.json") for this service.

###### Topics

- [Actions defined by AWS Consolidated Billing](#list_consolidatedbilling-actions-as-permissions "#list_consolidatedbilling-actions-as-permissions")
- [Permission-only actions for AWS Consolidated Billing](#list_consolidatedbilling-permission-only-actions "#list_consolidatedbilling-permission-only-actions")
- [Resource types defined by AWS Consolidated Billing](#list_consolidatedbilling-resources-for-iam-policies "#list_consolidatedbilling-resources-for-iam-policies")
- [Condition keys for AWS Consolidated Billing](#list_consolidatedbilling-policy-keys "#list_consolidatedbilling-policy-keys")

## Actions defined by AWS Consolidated Billing

AWS Consolidated Billing has no API operations that can be used in the
`Actions` element of an IAM policy statement.

## Permission-only actions for AWS Consolidated Billing

The following actions are defined by AWS Consolidated Billing but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                                              | Description                                                    | Resource types (\*required) | Condition keys | Access level |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [GetAccountBillingRole](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md") | Grants permission to get account role (Payer, Linked, Regular) |                             |                | Read         |
| [ListLinkedAccounts](../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md "../../../awsaccountbilling/latest/aboutv2/billing-permissions-ref.md")    | Grants permission to get list of member/linked accounts        |                             |                | List         |

## Resource types defined by AWS Consolidated Billing

AWS Consolidated Billing does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Consolidated Billing

AWS Consolidated Billing has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
