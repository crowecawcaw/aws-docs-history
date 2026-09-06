

# Actions, resources, and condition keys for AWS License Manager
<a name="list_license-manager"></a>

AWS License Manager (service prefix: `license-manager`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/license-manager/latest/userguide/license-manager.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/license-manager/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/license-manager/latest/userguide/using-service-linked-roles.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/license-manager/license-manager.json) for this service.

**Topics**
+ [API operations defined by AWS License Manager](#list_license-manager-operations)
+ [Actions defined by AWS License Manager](#list_license-manager-actions-as-permissions)
+ [Resource types defined by AWS License Manager](#list_license-manager-resources-for-iam-policies)
+ [Condition keys for AWS License Manager](#list_license-manager-policy-keys)

## API operations defined by AWS License Manager
<a name="list_license-manager-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_license-manager-actions-as-permissions).




- **   AcceptGrant  **
  - **IAM action:**  [license-manager:AcceptGrant](#list_license-manager-action-AcceptGrant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CheckInLicense  **
  - **IAM action:**  [license-manager:CheckInLicense](#list_license-manager-action-CheckInLicense) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CheckoutBorrowLicense  **
  - **IAM action:**  [license-manager:CheckoutBorrowLicense](#list_license-manager-action-CheckoutBorrowLicense) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CheckoutLicense  **
  - **IAM action:**  [license-manager:CheckoutLicense](#list_license-manager-action-CheckoutLicense) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateGrant  **
  - **IAM action:**  [license-manager:CreateGrant](#list_license-manager-action-CreateGrant)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [license-manager:TagResource](#list_license-manager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateGrantVersion  **
  - **IAM action:**  [license-manager:CreateGrantVersion](#list_license-manager-action-CreateGrantVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateLicense  **
  - **IAM action:**  [license-manager:CreateLicense](#list_license-manager-action-CreateLicense)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [license-manager:TagResource](#list_license-manager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLicenseAssetGroup  **
  - **IAM action:**  [license-manager:CreateLicenseAssetGroup](#list_license-manager-action-CreateLicenseAssetGroup)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [license-manager:TagResource](#list_license-manager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLicenseAssetRuleset  **
  - **IAM action:**  [license-manager:CreateLicenseAssetRuleset](#list_license-manager-action-CreateLicenseAssetRuleset)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [license-manager:TagResource](#list_license-manager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLicenseConfiguration  **
  - **IAM action:**  [license-manager:CreateLicenseConfiguration](#list_license-manager-action-CreateLicenseConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [license-manager:TagResource](#list_license-manager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLicenseConversionTaskForResource  **
  - **IAM action:**  [license-manager:CreateLicenseConversionTaskForResource](#list_license-manager-action-CreateLicenseConversionTaskForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateLicenseManagerReportGenerator  **
  - **IAM action:**  [license-manager:CreateLicenseManagerReportGenerator](#list_license-manager-action-CreateLicenseManagerReportGenerator)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [license-manager:TagResource](#list_license-manager-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateLicenseVersion  **
  - **IAM action:**  [license-manager:CreateLicenseVersion](#list_license-manager-action-CreateLicenseVersion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateToken  **
  - **IAM action:**  [license-manager:CreateToken](#list_license-manager-action-CreateToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteGrant  **
  - **IAM action:**  [license-manager:DeleteGrant](#list_license-manager-action-DeleteGrant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLicense  **
  - **IAM action:**  [license-manager:DeleteLicense](#list_license-manager-action-DeleteLicense) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLicenseAssetGroup  **
  - **IAM action:**  [license-manager:DeleteLicenseAssetGroup](#list_license-manager-action-DeleteLicenseAssetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLicenseAssetRuleset  **
  - **IAM action:**  [license-manager:DeleteLicenseAssetRuleset](#list_license-manager-action-DeleteLicenseAssetRuleset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLicenseConfiguration  **
  - **IAM action:**  [license-manager:DeleteLicenseConfiguration](#list_license-manager-action-DeleteLicenseConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteLicenseManagerReportGenerator  **
  - **IAM action:**  [license-manager:DeleteLicenseManagerReportGenerator](#list_license-manager-action-DeleteLicenseManagerReportGenerator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteToken  **
  - **IAM action:**  [license-manager:DeleteToken](#list_license-manager-action-DeleteToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ExtendLicenseConsumption  **
  - **IAM action:**  [license-manager:ExtendLicenseConsumption](#list_license-manager-action-ExtendLicenseConsumption) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccessToken  **
  - **IAM action:**  [license-manager:GetAccessToken](#list_license-manager-action-GetAccessToken) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGrant  **
  - **IAM action:**  [license-manager:GetGrant](#list_license-manager-action-GetGrant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLicense  **
  - **IAM action:**  [license-manager:GetLicense](#list_license-manager-action-GetLicense) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLicenseAssetGroup  **
  - **IAM action:**  [license-manager:GetLicenseAssetGroup](#list_license-manager-action-GetLicenseAssetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLicenseAssetRuleset  **
  - **IAM action:**  [license-manager:GetLicenseAssetRuleset](#list_license-manager-action-GetLicenseAssetRuleset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLicenseConfiguration  **
  - **IAM action:**  [license-manager:GetLicenseConfiguration](#list_license-manager-action-GetLicenseConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLicenseConversionTask  **
  - **IAM action:**  [license-manager:GetLicenseConversionTask](#list_license-manager-action-GetLicenseConversionTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLicenseManagerReportGenerator  **
  - **IAM action:**  [license-manager:GetLicenseManagerReportGenerator](#list_license-manager-action-GetLicenseManagerReportGenerator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetLicenseUsage  **
  - **IAM action:**  [license-manager:GetLicenseUsage](#list_license-manager-action-GetLicenseUsage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetServiceSettings  **
  - **IAM action:**  [license-manager:GetServiceSettings](#list_license-manager-action-GetServiceSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssetsForLicenseAssetGroup  **
  - **IAM action:**  [license-manager:ListAssetsForLicenseAssetGroup](#list_license-manager-action-ListAssetsForLicenseAssetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssociationsForLicenseConfiguration  **
  - **IAM action:**  [license-manager:ListAssociationsForLicenseConfiguration](#list_license-manager-action-ListAssociationsForLicenseConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDistributedGrants  **
  - **IAM action:**  [license-manager:ListDistributedGrants](#list_license-manager-action-ListDistributedGrants) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListFailuresForLicenseConfigurationOperations  **
  - **IAM action:**  [license-manager:ListFailuresForLicenseConfigurationOperations](#list_license-manager-action-ListFailuresForLicenseConfigurationOperations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLicenseAssetGroups  **
  - **IAM action:**  [license-manager:ListLicenseAssetGroups](#list_license-manager-action-ListLicenseAssetGroups) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLicenseAssetRulesets  **
  - **IAM action:**  [license-manager:ListLicenseAssetRulesets](#list_license-manager-action-ListLicenseAssetRulesets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLicenseConfigurations  **
  - **IAM action:**  [license-manager:ListLicenseConfigurations](#list_license-manager-action-ListLicenseConfigurations) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLicenseConfigurationsForOrganization  **
  - **IAM action:**  [license-manager:ListLicenseConfigurationsForOrganization](#list_license-manager-action-ListLicenseConfigurationsForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLicenseConversionTasks  **
  - **IAM action:**  [license-manager:ListLicenseConversionTasks](#list_license-manager-action-ListLicenseConversionTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLicenseManagerReportGenerators  **
  - **IAM action:**  [license-manager:ListLicenseManagerReportGenerators](#list_license-manager-action-ListLicenseManagerReportGenerators) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLicenseSpecificationsForResource  **
  - **IAM action:**  [license-manager:ListLicenseSpecificationsForResource](#list_license-manager-action-ListLicenseSpecificationsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLicenseVersions  **
  - **IAM action:**  [license-manager:ListLicenseVersions](#list_license-manager-action-ListLicenseVersions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListLicenses  **
  - **IAM action:**  [license-manager:ListLicenses](#list_license-manager-action-ListLicenses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListReceivedGrants  **
  - **IAM action:**  [license-manager:ListReceivedGrants](#list_license-manager-action-ListReceivedGrants) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReceivedGrantsForOrganization  **
  - **IAM action:**  [license-manager:ListReceivedGrantsForOrganization](#list_license-manager-action-ListReceivedGrantsForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReceivedLicenses  **
  - **IAM action:**  [license-manager:ListReceivedLicenses](#list_license-manager-action-ListReceivedLicenses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListReceivedLicensesForOrganization  **
  - **IAM action:**  [license-manager:ListReceivedLicensesForOrganization](#list_license-manager-action-ListReceivedLicensesForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceInventory  **
  - **IAM action:**  [license-manager:ListResourceInventory](#list_license-manager-action-ListResourceInventory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [license-manager:ListTagsForResource](#list_license-manager-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListTokens  **
  - **IAM action:**  [license-manager:ListTokens](#list_license-manager-action-ListTokens) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListUsageForLicenseConfiguration  **
  - **IAM action:**  [license-manager:ListUsageForLicenseConfiguration](#list_license-manager-action-ListUsageForLicenseConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   RejectGrant  **
  - **IAM action:**  [license-manager:RejectGrant](#list_license-manager-action-RejectGrant) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [license-manager:TagResource](#list_license-manager-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [license-manager:UntagResource](#list_license-manager-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateLicenseAssetGroup  **
  - **IAM action:**  [license-manager:UpdateLicenseAssetGroup](#list_license-manager-action-UpdateLicenseAssetGroup) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLicenseAssetRuleset  **
  - **IAM action:**  [license-manager:UpdateLicenseAssetRuleset](#list_license-manager-action-UpdateLicenseAssetRuleset) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLicenseConfiguration  **
  - **IAM action:**  [license-manager:UpdateLicenseConfiguration](#list_license-manager-action-UpdateLicenseConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLicenseManagerReportGenerator  **
  - **IAM action:**  [license-manager:UpdateLicenseManagerReportGenerator](#list_license-manager-action-UpdateLicenseManagerReportGenerator) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateLicenseSpecificationsForResource  **
  - **IAM action:**  [license-manager:UpdateLicenseSpecificationsForResource](#list_license-manager-action-UpdateLicenseSpecificationsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateServiceSettings  **
  - **IAM action:**  [license-manager:UpdateServiceSettings](#list_license-manager-action-UpdateServiceSettings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write



## Actions defined by AWS License Manager
<a name="list_license-manager-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptGrant](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_AcceptGrant.html)  **
  - **Description:** Grants permission to accept a grant
  - **Resource types (\*required):** [grant\*](#list_license-manager-resource-grant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CheckInLicense](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CheckInLicense.html)  **
  - **Description:** Grants permission to check in license entitlements back to pool
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CheckoutBorrowLicense](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CheckoutBorrowLicense.html)  **
  - **Description:** Grants permission to check out license entitlements for borrow use case
  - **Resource types (\*required):** [license\*](#list_license-manager-resource-license)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CheckoutLicense](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CheckoutLicense.html)  **
  - **Description:** Grants permission to check out license entitlements
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateGrant](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CreateGrant.html)  **
  - **Description:** Grants permission to create a new grant for license
  - **Resource types (\*required):** [license\*](#list_license-manager-resource-license)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_license-manager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-aws_TagKeys)
  - **Access level:** Write

- **   [CreateGrantVersion](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CreateGrantVersion.html)  **
  - **Description:** Grants permission to create new version of grant
  - **Resource types (\*required):** [grant\*](#list_license-manager-resource-grant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateLicense](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CreateLicense.html)  **
  - **Description:** Grants permission to create a new license
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_license-manager-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLicenseAssetGroup](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CreateLicenseAssetGroup.html)  **
  - **Description:** Grants permission to create a license asset group
  - **Resource types (\*required):** [license-asset-ruleset\*](#list_license-manager-resource-license-asset-ruleset)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_license-manager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLicenseAssetRuleset](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CreateLicenseAssetRuleset.html)  **
  - **Description:** Grants permission to create a license asset ruleset
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_license-manager-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLicenseConfiguration](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CreateLicenseConfiguration.html)  **
  - **Description:** Grants permission to create a new license configuration
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_license-manager-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLicenseConversionTaskForResource](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CreateLicenseConversionTaskForResource.html)  **
  - **Description:** Grants permission to create a license conversion task for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateLicenseManagerReportGenerator](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CreateLicenseManagerReportGenerator.html)  **
  - **Description:** Grants permission to create a report generator for supported license manager resources
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_license-manager-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-aws_TagKeys)
  - **Access level:** Write

- **   [CreateLicenseVersion](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CreateLicenseVersion.html)  **
  - **Description:** Grants permission to create new version of license
  - **Resource types (\*required):** [license\*](#list_license-manager-resource-license)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateToken](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CreateToken.html)  **
  - **Description:** Grants permission to create a new token for license
  - **Resource types (\*required):** [license\*](#list_license-manager-resource-license)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteGrant](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_DeleteGrant.html)  **
  - **Description:** Grants permission to delete a grant
  - **Resource types (\*required):** [grant\*](#list_license-manager-resource-grant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLicense](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_DeleteLicense.html)  **
  - **Description:** Grants permission to delete a license
  - **Resource types (\*required):** [license\*](#list_license-manager-resource-license)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLicenseAssetGroup](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_DeleteLicenseAssetGroup.html)  **
  - **Description:** Grants permission to delete a license asset group
  - **Resource types (\*required):** [license-asset-group\*](#list_license-manager-resource-license-asset-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLicenseAssetRuleset](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_DeleteLicenseAssetRuleset.html)  **
  - **Description:** Grants permission to delete a license asset ruleset
  - **Resource types (\*required):** [license-asset-ruleset\*](#list_license-manager-resource-license-asset-ruleset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLicenseConfiguration](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_DeleteLicenseConfiguration.html)  **
  - **Description:** Grants permission to permanently delete a license configuration
  - **Resource types (\*required):** [license-configuration\*](#list_license-manager-resource-license-configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[license-manager:ResourceTag/${TagKey}](#list_license-manager-license-manager_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteLicenseManagerReportGenerator](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_DeleteLicenseManagerReportGenerator.html)  **
  - **Description:** Grants permission to delete a report generator
  - **Resource types (\*required):** [report-generator\*](#list_license-manager-resource-report-generator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[license-manager:ResourceTag/${TagKey}](#list_license-manager-license-manager_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteToken](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_DeleteToken.html)  **
  - **Description:** Grants permission to delete token
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [ExtendLicenseConsumption](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ExtendLicenseConsumption.html)  **
  - **Description:** Grants permission to extend consumption period of already checkout license entitlements
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetAccessToken](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_GetAccessToken.html)  **
  - **Description:** Grants permission to get access token
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetGrant](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_GetGrant.html)  **
  - **Description:** Grants permission to get a grant
  - **Resource types (\*required):** [grant\*](#list_license-manager-resource-grant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLicense](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_GetLicense.html)  **
  - **Description:** Grants permission to get a license
  - **Resource types (\*required):** [license\*](#list_license-manager-resource-license)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLicenseAssetGroup](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_GetLicenseAssetGroup.html)  **
  - **Description:** Grants permission to get a license asset group
  - **Resource types (\*required):** [license-asset-group\*](#list_license-manager-resource-license-asset-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLicenseAssetRuleset](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_GetLicenseAssetRuleset.html)  **
  - **Description:** Grants permission to get a license asset ruleset
  - **Resource types (\*required):** [license-asset-ruleset\*](#list_license-manager-resource-license-asset-ruleset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLicenseConfiguration](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_GetLicenseConfiguration.html)  **
  - **Description:** Grants permission to get a license configuration
  - **Resource types (\*required):** [license-configuration\*](#list_license-manager-resource-license-configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[license-manager:ResourceTag/${TagKey}](#list_license-manager-license-manager_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLicenseConversionTask](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_GetLicenseConversionTask.html)  **
  - **Description:** Grants permission to retrieve a license conversion task
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetLicenseManagerReportGenerator](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_GetLicenseManagerReportGenerator.html)  **
  - **Description:** Grants permission to get a report generator
  - **Resource types (\*required):** [report-generator\*](#list_license-manager-resource-report-generator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[license-manager:ResourceTag/${TagKey}](#list_license-manager-license-manager_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetLicenseUsage](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_GetLicenseUsage.html)  **
  - **Description:** Grants permission to get a license usage
  - **Resource types (\*required):** [license\*](#list_license-manager-resource-license)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetServiceSettings](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_GetServiceSettings.html)  **
  - **Description:** Grants permission to get service settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAssetsForLicenseAssetGroup](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListAssetsForLicenseAssetGroup.html)  **
  - **Description:** Grants permission to list assets for a license asset group
  - **Resource types (\*required):** [license-asset-group\*](#list_license-manager-resource-license-asset-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAssociationsForLicenseConfiguration](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListAssociationsForLicenseConfiguration.html)  **
  - **Description:** Grants permission to list associations for a selected license configuration
  - **Resource types (\*required):** [license-configuration\*](#list_license-manager-resource-license-configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[license-manager:ResourceTag/${TagKey}](#list_license-manager-license-manager_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDistributedGrants](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListDistributedGrants.html)  **
  - **Description:** Grants permission to list distributed grants
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListFailuresForLicenseConfigurationOperations](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListFailuresForLicenseConfigurationOperations.html)  **
  - **Description:** Grants permission to list the license configuration operations that failed
  - **Resource types (\*required):** [license-configuration\*](#list_license-manager-resource-license-configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[license-manager:ResourceTag/${TagKey}](#list_license-manager-license-manager_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListLicenseAssetGroups](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListLicenseAssetGroups.html)  **
  - **Description:** Grants permission to list license asset groups
  - **Resource types (\*required):** [license-asset-group](#list_license-manager-resource-license-asset-group)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListLicenseAssetRulesets](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListLicenseAssetRulesets.html)  **
  - **Description:** Grants permission to list license asset rulesets
  - **Resource types (\*required):** [license-asset-ruleset](#list_license-manager-resource-license-asset-ruleset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListLicenseConfigurations](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListLicenseConfigurations.html)  **
  - **Description:** Grants permission to list license configurations
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLicenseConfigurationsForOrganization](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListLicenseConfigurationsForOrganization.html)  **
  - **Description:** Grants permission to list license configurations for organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLicenseConversionTasks](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListLicenseConversionTasks.html)  **
  - **Description:** Grants permission to list license conversion tasks
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLicenseManagerReportGenerators](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListLicenseManagerReportGenerators.html)  **
  - **Description:** Grants permission to list report generators
  - **Resource types (\*required):** [license-configuration](#list_license-manager-resource-license-configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[license-manager:ResourceTag/${TagKey}](#list_license-manager-license-manager_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListLicenseSpecificationsForResource](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListLicenseSpecificationsForResource.html)  **
  - **Description:** Grants permission to list license specifications associated with a selected resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListLicenseVersions](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListLicenseVersions.html)  **
  - **Description:** Grants permission to list license versions
  - **Resource types (\*required):** [license\*](#list_license-manager-resource-license)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListLicenses](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListLicenses.html)  **
  - **Description:** Grants permission to list licenses
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListReceivedGrants](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListReceivedGrants.html)  **
  - **Description:** Grants permission to list received grants
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListReceivedGrantsForOrganization](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListReceivedGrantsForOrganization.html)  **
  - **Description:** Grants permission to list received grants for organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListReceivedLicenses](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListReceivedLicenses.html)  **
  - **Description:** Grants permission to list received licenses
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListReceivedLicensesForOrganization](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListReceivedLicensesForOrganization.html)  **
  - **Description:** Grants permission to list received licenses for organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResourceInventory](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListResourceInventory.html)  **
  - **Description:** Grants permission to list resource inventory
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a selected resource
  - **Resource types (\*required):** [grant](#list_license-manager-resource-grant) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [license](#list_license-manager-resource-license) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [license-asset-group](#list_license-manager-resource-license-asset-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [license-asset-ruleset](#list_license-manager-resource-license-asset-ruleset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [license-configuration](#list_license-manager-resource-license-configuration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[license-manager:ResourceTag/${TagKey}](#list_license-manager-license-manager_ResourceTag___TagKey_)
  - **Resource types (\*required):** [report-generator](#list_license-manager-resource-report-generator) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[license-manager:ResourceTag/${TagKey}](#list_license-manager-license-manager_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListTokens](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListTokens.html)  **
  - **Description:** Grants permission to list tokens
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListUsageForLicenseConfiguration](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_ListUsageForLicenseConfiguration.html)  **
  - **Description:** Grants permission to list usage records for selected license configuration
  - **Resource types (\*required):** [license-configuration\*](#list_license-manager-resource-license-configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[license-manager:ResourceTag/${TagKey}](#list_license-manager-license-manager_ResourceTag___TagKey_)
  - **Access level:** List

- **   [RejectGrant](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_RejectGrant.html)  **
  - **Description:** Grants permission to reject a grant
  - **Resource types (\*required):** [grant\*](#list_license-manager-resource-grant)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a selected resource
  - **Resource types (\*required):** [grant](#list_license-manager-resource-grant) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_license-manager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-aws_TagKeys)
  - **Resource types (\*required):** [license](#list_license-manager-resource-license) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_license-manager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-aws_TagKeys)
  - **Resource types (\*required):** [license-asset-group](#list_license-manager-resource-license-asset-group) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_license-manager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-aws_TagKeys)
  - **Resource types (\*required):** [license-asset-ruleset](#list_license-manager-resource-license-asset-ruleset) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_license-manager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-aws_TagKeys)
  - **Resource types (\*required):** [license-configuration](#list_license-manager-resource-license-configuration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_license-manager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-aws_TagKeys)<br />[license-manager:ResourceTag/${TagKey}](#list_license-manager-license-manager_ResourceTag___TagKey_)
  - **Resource types (\*required):** [report-generator](#list_license-manager-resource-report-generator) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_license-manager-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-aws_TagKeys)<br />[license-manager:ResourceTag/${TagKey}](#list_license-manager-license-manager_ResourceTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a selected resource
  - **Resource types (\*required):** [grant](#list_license-manager-resource-grant) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-aws_TagKeys)
  - **Resource types (\*required):** [license](#list_license-manager-resource-license) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-aws_TagKeys)
  - **Resource types (\*required):** [license-asset-group](#list_license-manager-resource-license-asset-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-aws_TagKeys)
  - **Resource types (\*required):** [license-asset-ruleset](#list_license-manager-resource-license-asset-ruleset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-aws_TagKeys)
  - **Resource types (\*required):** [license-configuration](#list_license-manager-resource-license-configuration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-aws_TagKeys)<br />[license-manager:ResourceTag/${TagKey}](#list_license-manager-license-manager_ResourceTag___TagKey_)
  - **Resource types (\*required):** [report-generator](#list_license-manager-resource-report-generator) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_license-manager-aws_TagKeys)<br />[license-manager:ResourceTag/${TagKey}](#list_license-manager-license-manager_ResourceTag___TagKey_)
  - **Access level:** Tagging, Write

- **   [UpdateLicenseAssetGroup](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_UpdateLicenseAssetGroup.html)  **
  - **Description:** Grants permission to update a license asset group
  - **Resource types (\*required):** [license-asset-group\*](#list_license-manager-resource-license-asset-group) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [license-asset-ruleset\*](#list_license-manager-resource-license-asset-ruleset) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLicenseAssetRuleset](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_UpdateLicenseAssetRuleset.html)  **
  - **Description:** Grants permission to update a license asset ruleset
  - **Resource types (\*required):** [license-asset-ruleset\*](#list_license-manager-resource-license-asset-ruleset)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLicenseConfiguration](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_UpdateLicenseConfiguration.html)  **
  - **Description:** Grants permission to update an existing license configuration
  - **Resource types (\*required):** [license-configuration\*](#list_license-manager-resource-license-configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[license-manager:ResourceTag/${TagKey}](#list_license-manager-license-manager_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLicenseManagerReportGenerator](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_UpdateLicenseManagerReportGenerator.html)  **
  - **Description:** Grants permission to update a report generator for supported license manager resources
  - **Resource types (\*required):** [report-generator\*](#list_license-manager-resource-report-generator)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[license-manager:ResourceTag/${TagKey}](#list_license-manager-license-manager_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateLicenseSpecificationsForResource](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_UpdateLicenseSpecificationsForResource.html)  **
  - **Description:** Grants permission to updates license specifications for a selected resource
  - **Resource types (\*required):** [license-configuration\*](#list_license-manager-resource-license-configuration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[license-manager:ResourceTag/${TagKey}](#list_license-manager-license-manager_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateServiceSettings](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_UpdateServiceSettings.html)  **
  - **Description:** Grants permission to updates service settings
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Permissions management, Write



## Resource types defined by AWS License Manager
<a name="list_license-manager-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [grant](https://docs.aws.amazon.com/license-manager/latest/userguide/granted-licenses.html)  | arn:${Partition}:license-manager::${Account}:grant:${GrantId} | [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_) | 
|  [license](https://docs.aws.amazon.com/license-manager/latest/userguide/seller-issued-licenses.html)  | arn:${Partition}:license-manager::${Account}:license:${LicenseId} | [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_) | 
|  [license-asset-group](https://docs.aws.amazon.com/license-manager/latest/userguide/license-asset-group.html)  | arn:${Partition}:license-manager:${Region}:${Account}:license-asset-group:${LicenseAssetGroupId} | [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_) | 
|  [license-asset-ruleset](https://docs.aws.amazon.com/license-manager/latest/userguide/license-asset-ruleset.html)  | arn:${Partition}:license-manager:${Region}:${Account}:license-asset-ruleset:${LicenseAssetRulesetId} | [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_) | 
|  [license-configuration](https://docs.aws.amazon.com/license-manager/latest/userguide/license-configurations.html)  | arn:${Partition}:license-manager:${Region}:${Account}:license-configuration:${LicenseConfigurationId} | [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[license-manager:ResourceTag/${TagKey}](#list_license-manager-license-manager_ResourceTag___TagKey_) | 
|  [report-generator](https://docs.aws.amazon.com/license-manager/latest/userguide/license-reporting.html)  | arn:${Partition}:license-manager:${Region}:${Account}:report-generator:${ReportGeneratorId} | [aws:ResourceTag/${TagKey}](#list_license-manager-aws_ResourceTag___TagKey_)<br />[license-manager:ResourceTag/${TagKey}](#list_license-manager-license-manager_ResourceTag___TagKey_) | 

## Condition keys for AWS License Manager
<a name="list_license-manager-policy-keys"></a>

AWS License Manager defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/license-manager/latest/userguide/identity-access-management.html)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](identity-access-management.html)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/license-manager/latest/userguide/identity-access-management.html)  | Filters access by tag keys that are passed in the request | ArrayOfString | 
|   [license-manager:ResourceTag/${TagKey}](https://docs.aws.amazon.com/license-manager/latest/userguide/identity-access-management.html)  | Filters access by the tag key-value pairs attached to the resource | String | 