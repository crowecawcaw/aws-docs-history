# Actions, resources, and condition keys for AWS Partner central account management

AWS Partner central account management (service prefix: `partnercentral-account-management`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../partner-central/latest/getting-started/account-linking.md "../../../partner-central/latest/getting-started/account-linking.md").
- View a list of the [API operations available for
  this service](../../../partner-central/latest/getting-started/controlling-access-in-apc-account-management.md "../../../partner-central/latest/getting-started/controlling-access-in-apc-account-management.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../partner-central/latest/getting-started/controlling-access-in-apc-account-management.md "../../../partner-central/latest/getting-started/controlling-access-in-apc-account-management.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/partnercentral-account-management/partnercentral-account-management.json "https://servicereference.us-east-1.amazonaws.com/v1/partnercentral-account-management/partnercentral-account-management.json") for this service.

###### Topics

- [Actions defined by AWS Partner central account management](#list_partnercentral-account-management-actions-as-permissions "#list_partnercentral-account-management-actions-as-permissions")
- [Permission-only actions for AWS Partner central account management](#list_partnercentral-account-management-permission-only-actions "#list_partnercentral-account-management-permission-only-actions")
- [Resource types defined by AWS Partner central account management](#list_partnercentral-account-management-resources-for-iam-policies "#list_partnercentral-account-management-resources-for-iam-policies")
- [Condition keys for AWS Partner central account management](#list_partnercentral-account-management-policy-keys "#list_partnercentral-account-management-policy-keys")

## Actions defined by AWS Partner central account management

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                                                      | Description                                                | Resource types (\*required) | Condition keys | Access level |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | --------------------------- | -------------- | ------------ |
| [AssociatePartnerUser](../../../partner-central/latest/getting-started/controlling-access-in-apc-account-management.md "../../../partner-central/latest/getting-started/controlling-access-in-apc-account-management.md")    | Grants permission to associate Partner user to IAM role    |                             |                | Write        |
| [DisassociatePartnerUser](../../../partner-central/latest/getting-started/controlling-access-in-apc-account-management.md "../../../partner-central/latest/getting-started/controlling-access-in-apc-account-management.md") | Grants permission to disassociate Partner user to IAM role |                             |                | Write        |

## Permission-only actions for AWS Partner central account management

The following actions are defined by AWS Partner central account management but are not directly
invocable through any API operation. They can only be used in IAM policy statements
to grant or deny permissions.

| Actions                                                                                                                                                                                                                         | Description                                                                              | Resource types (\*required) | Condition keys                                                                                                                                                                                                                                                        | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| [AccessLegacyPartnerCentral](../../../partner-central/latest/getting-started/controlling-access-in-apc-account-management.md "../../../partner-central/latest/getting-started/controlling-access-in-apc-account-management.md") | Grants permission to Single Sign-On from AWS Partner Central into Legacy Partner Central |                             | [partnercentral-account-management:LegacyPartnerCentralRole](#list_partnercentral-account-management-partnercentral-account-management_LegacyPartnerCentralRole "#list_partnercentral-account-management-partnercentral-account-management_LegacyPartnerCentralRole") | Write        |
| [AccessMarketingCentral](../../../partner-central/latest/getting-started/controlling-access-in-apc-account-management.md "../../../partner-central/latest/getting-started/controlling-access-in-apc-account-management.md")     | Grants permission to Single Sign-On from AWS Partner Central into Marketing Central      |                             | [partnercentral-account-management:MarketingCentralRole](#list_partnercentral-account-management-partnercentral-account-management_MarketingCentralRole "#list_partnercentral-account-management-partnercentral-account-management_MarketingCentralRole")             | Write        |
| [AccessProServeTools](../../../partner-central/latest/getting-started/controlling-access-in-apc-account-management.md "../../../partner-central/latest/getting-started/controlling-access-in-apc-account-management.md")        | Grants permission to Single Sign-On from AWS Partner Central into ProServe Tools         |                             | [partnercentral-account-management:ProServeRole](#list_partnercentral-account-management-partnercentral-account-management_ProServeRole "#list_partnercentral-account-management-partnercentral-account-management_ProServeRole")                                     | Write        |
| [AssociatePartnerAccount](../../../partner-central/latest/getting-started/controlling-access-in-apc-account-management.md "../../../partner-central/latest/getting-started/controlling-access-in-apc-account-management.md")    | Grants permission to associate Partner account to AWS account                            |                             |                                                                                                                                                                                                                                                                       | Write        |

## Resource types defined by AWS Partner central account management

AWS Partner central account management does not support specifying a resource ARN in the
`Resource` element of an IAM policy statement.

## Condition keys for AWS Partner central account management

AWS Partner central account management defines the following condition keys that can be used in the
`Condition` element of an IAM policy.

| Condition keys                                                                                                                                                                                                                                                  | Description                                       | Type          |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ------------- |
| [partnercentral-account-management:LegacyPartnerCentralRole](../../../partner-central/latest/getting-started/controlling-access-in-apc-account-management.md "../../../partner-central/latest/getting-started/controlling-access-in-apc-account-management.md") | Filters access by the Legacy Partner Central role | ArrayOfString |
| [partnercentral-account-management:MarketingCentralRole](../../../partner-central/latest/getting-started/controlling-access-in-apc-account-management.md "../../../partner-central/latest/getting-started/controlling-access-in-apc-account-management.md")     | Filters access by Marketing Central role          | ArrayOfString |
| [partnercentral-account-management:ProServeRole](../../../partner-central/latest/getting-started/controlling-access-in-apc-account-management.md "../../../partner-central/latest/getting-started/controlling-access-in-apc-account-management.md")             | Filters access by ProServe Tools role             | ArrayOfString |
