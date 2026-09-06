

# Actions, resources, and condition keys for AWS Partner central account management
<a name="list_partnercentral-account-management"></a>

AWS Partner central account management (service prefix: `partnercentral-account-management`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/partner-central/latest/getting-started/account-linking.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/partner-central/latest/getting-started/controlling-access-in-apc-account-management.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/partner-central/latest/getting-started/controlling-access-in-apc-account-management.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/partnercentral-account-management/partnercentral-account-management.json) for this service.

**Topics**
+ [Actions defined by AWS Partner central account management](#list_partnercentral-account-management-actions-as-permissions)
+ [Permission-only actions for AWS Partner central account management](#list_partnercentral-account-management-permission-only-actions)
+ [Resource types defined by AWS Partner central account management](#list_partnercentral-account-management-resources-for-iam-policies)
+ [Condition keys for AWS Partner central account management](#list_partnercentral-account-management-policy-keys)

## Actions defined by AWS Partner central account management
<a name="list_partnercentral-account-management-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [AssociatePartnerUser](https://docs.aws.amazon.com/partner-central/latest/getting-started/controlling-access-in-apc-account-management.html)  | Grants permission to associate Partner user to IAM role |  |   | Write | 
|   [DisassociatePartnerUser](https://docs.aws.amazon.com/partner-central/latest/getting-started/controlling-access-in-apc-account-management.html)  | Grants permission to disassociate Partner user to IAM role |  |   | Write | 

## Permission-only actions for AWS Partner central account management
<a name="list_partnercentral-account-management-permission-only-actions"></a>

The following actions are defined by AWS Partner central account management but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.



| Actions | Description | Resource types (\*required) | Condition keys | Access level | 
| --- | --- | --- | --- | --- | 
|   [AccessLegacyPartnerCentral](https://docs.aws.amazon.com/partner-central/latest/getting-started/controlling-access-in-apc-account-management.html)  | Grants permission to Single Sign-On from AWS Partner Central into Legacy Partner Central |  | [partnercentral-account-management:LegacyPartnerCentralRole](#list_partnercentral-account-management-partnercentral-account-management_LegacyPartnerCentralRole) | Write | 
|   [AccessMarketingCentral](https://docs.aws.amazon.com/partner-central/latest/getting-started/controlling-access-in-apc-account-management.html)  | Grants permission to Single Sign-On from AWS Partner Central into Marketing Central |  | [partnercentral-account-management:MarketingCentralRole](#list_partnercentral-account-management-partnercentral-account-management_MarketingCentralRole) | Write | 
|   [AccessProServeTools](https://docs.aws.amazon.com/partner-central/latest/getting-started/controlling-access-in-apc-account-management.html)  | Grants permission to Single Sign-On from AWS Partner Central into ProServe Tools |  | [partnercentral-account-management:ProServeRole](#list_partnercentral-account-management-partnercentral-account-management_ProServeRole) | Write | 
|   [AssociatePartnerAccount](https://docs.aws.amazon.com/partner-central/latest/getting-started/controlling-access-in-apc-account-management.html)  | Grants permission to associate Partner account to AWS account |  |   | Write | 

## Resource types defined by AWS Partner central account management
<a name="list_partnercentral-account-management-resources-for-iam-policies"></a>

AWS Partner central account management does not support specifying a resource ARN in the `Resource` element of an IAM policy statement.

## Condition keys for AWS Partner central account management
<a name="list_partnercentral-account-management-policy-keys"></a>

AWS Partner central account management defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [partnercentral-account-management:LegacyPartnerCentralRole](https://docs.aws.amazon.com/partner-central/latest/getting-started/controlling-access-in-apc-account-management.html)  | Filters access by the Legacy Partner Central role | ArrayOfString | 
|   [partnercentral-account-management:MarketingCentralRole](https://docs.aws.amazon.com/partner-central/latest/getting-started/controlling-access-in-apc-account-management.html)  | Filters access by Marketing Central role | ArrayOfString | 
|   [partnercentral-account-management:ProServeRole](https://docs.aws.amazon.com/partner-central/latest/getting-started/controlling-access-in-apc-account-management.html)  | Filters access by ProServe Tools role | ArrayOfString | 