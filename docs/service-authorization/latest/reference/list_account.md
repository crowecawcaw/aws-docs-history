

# Actions, resources, and condition keys for AWS Account Management
<a name="list_account"></a>

AWS Account Management (service prefix: `account`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/accounts/latest/reference/accounts-welcome.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/accounts/latest/reference/api-reference.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/accounts/latest/reference/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/account/account.json) for this service.

**Topics**
+ [API operations defined by AWS Account Management](#list_account-operations)
+ [Actions defined by AWS Account Management](#list_account-actions-as-permissions)
+ [Permission-only actions for AWS Account Management](#list_account-permission-only-actions)
+ [Resource types defined by AWS Account Management](#list_account-resources-for-iam-policies)
+ [Condition keys for AWS Account Management](#list_account-policy-keys)

## API operations defined by AWS Account Management
<a name="list_account-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_account-actions-as-permissions).




- **   AcceptPrimaryEmailUpdate  **
  - **IAM action:**  [account:AcceptPrimaryEmailUpdate](#list_account-action-AcceptPrimaryEmailUpdate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:UpdateAccountEmailAddress](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-root-user.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteAlternateContact  **
  - **IAM action:**  [account:DeleteAlternateContact](#list_account-action-DeleteAlternateContact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisableRegion  **
  - **IAM action:**  [account:DisableRegion](#list_account-action-DisableRegion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   EnableRegion  **
  - **IAM action:**  [account:EnableRegion](#list_account-action-EnableRegion) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAccountInformation  **
  - **IAM action:**  [account:GetAccountInformation](#list_account-action-GetAccountInformation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAlternateContact  **
  - **IAM action:**  [account:GetAlternateContact](#list_account-action-GetAlternateContact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetContactInformation  **
  - **IAM action:**  [account:GetContactInformation](#list_account-action-GetContactInformation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetGovCloudAccountInformation  **
  - **IAM action:**  [account:GetGovCloudAccountInformation](#list_account-action-GetGovCloudAccountInformation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPrimaryEmail  **
  - **IAM action:**  [account:GetPrimaryEmail](#list_account-action-GetPrimaryEmail) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPrimaryEmailUpdateStatus  **
  - **IAM action:**  [account:GetPrimaryEmailUpdateStatus](#list_account-action-GetPrimaryEmailUpdateStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRegionOptStatus  **
  - **IAM action:**  [account:GetRegionOptStatus](#list_account-action-GetRegionOptStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListRegions  **
  - **IAM action:**  [account:ListRegions](#list_account-action-ListRegions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutAccountName  **
  - **IAM action:**  [account:PutAccountName](#list_account-action-PutAccountName)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:UpdateAccountName](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-root-user.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   PutAlternateContact  **
  - **IAM action:**  [account:PutAlternateContact](#list_account-action-PutAlternateContact) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutContactInformation  **
  - **IAM action:**  [account:PutContactInformation](#list_account-action-PutContactInformation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartPrimaryEmailUpdate  **
  - **IAM action:**  [account:StartPrimaryEmailUpdate](#list_account-action-StartPrimaryEmailUpdate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:UpdateAccountEmailAddress](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-root-user.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write



## Actions defined by AWS Account Management
<a name="list_account-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptPrimaryEmailUpdate](https://docs.aws.amazon.com/accounts/latest/reference/API_AcceptPrimaryEmailUpdate.html)  **
  - **Description:** Grants permission to accept the process to update the primary email address of an account
  - **Resource types (\*required):** [accountInOrganization](#list_account-resource-accountInOrganization)
  - **Condition keys:** [account:EmailTargetDomain](#list_account-account_EmailTargetDomain)
  - **Access level:** Write

- **   [DeleteAlternateContact](https://docs.aws.amazon.com/accounts/latest/reference/API_DeleteAlternateContact.html)  **
  - **Description:** Grants permission to delete the alternate contacts for an account
  - **Resource types (\*required):** [account](#list_account-resource-account) / **Condition keys:** [account:AlternateContactTypes](#list_account-account_AlternateContactTypes)
  - **Resource types (\*required):** [accountInOrganization](#list_account-resource-accountInOrganization) / **Condition keys:** [account:AlternateContactTypes](#list_account-account_AlternateContactTypes)
  - **Access level:** Write

- **   [DisableRegion](https://docs.aws.amazon.com/accounts/latest/reference/API_DisableRegion.html)  **
  - **Description:** Grants permission to disable use of a Region
  - **Resource types (\*required):** [account](#list_account-resource-account) / **Condition keys:** [account:TargetRegion](#list_account-account_TargetRegion)
  - **Resource types (\*required):** [accountInOrganization](#list_account-resource-accountInOrganization) / **Condition keys:** [account:TargetRegion](#list_account-account_TargetRegion)
  - **Access level:** Write

- **   [EnableRegion](https://docs.aws.amazon.com/accounts/latest/reference/API_EnableRegion.html)  **
  - **Description:** Grants permission to enable use of a Region
  - **Resource types (\*required):** [account](#list_account-resource-account) / **Condition keys:** [account:TargetRegion](#list_account-account_TargetRegion)
  - **Resource types (\*required):** [accountInOrganization](#list_account-resource-accountInOrganization) / **Condition keys:** [account:TargetRegion](#list_account-account_TargetRegion)
  - **Access level:** Write

- **   [GetAccountInformation](https://docs.aws.amazon.com/accounts/latest/reference/API_GetAccountInformation.html)  **
  - **Description:** Grants permission to retrieve the account information for an account
  - **Resource types (\*required):** [account](#list_account-resource-account) / **Condition keys:**  
  - **Resource types (\*required):** [accountInOrganization](#list_account-resource-accountInOrganization) / **Condition keys:**  
  - **Access level:** Read

- **   [GetAlternateContact](https://docs.aws.amazon.com/accounts/latest/reference/API_GetAlternateContact.html)  **
  - **Description:** Grants permission to retrieve the alternate contacts for an account
  - **Resource types (\*required):** [account](#list_account-resource-account) / **Condition keys:** [account:AlternateContactTypes](#list_account-account_AlternateContactTypes)
  - **Resource types (\*required):** [accountInOrganization](#list_account-resource-accountInOrganization) / **Condition keys:** [account:AlternateContactTypes](#list_account-account_AlternateContactTypes)
  - **Access level:** Read

- **   [GetContactInformation](https://docs.aws.amazon.com/accounts/latest/reference/API_GetContactInformation.html)  **
  - **Description:** Grants permission to retrieve the primary contact information for an account
  - **Resource types (\*required):** [account](#list_account-resource-account) / **Condition keys:**  
  - **Resource types (\*required):** [accountInOrganization](#list_account-resource-accountInOrganization) / **Condition keys:**  
  - **Access level:** Read

- **   [GetGovCloudAccountInformation](https://docs.aws.amazon.com/accounts/latest/reference/API_GetGovCloudAccountInformation.html)  **
  - **Description:** Grants permission to retrieve the linked GovCloud account information for an account
  - **Resource types (\*required):** [account](#list_account-resource-account) / **Condition keys:**  
  - **Resource types (\*required):** [accountInOrganization](#list_account-resource-accountInOrganization) / **Condition keys:**  
  - **Access level:** Read

- **   [GetPrimaryEmail](https://docs.aws.amazon.com/accounts/latest/reference/API_GetPrimaryEmail.html)  **
  - **Description:** Grants permission to retrieve the primary email address of an account
  - **Resource types (\*required):** [accountInOrganization](#list_account-resource-accountInOrganization)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPrimaryEmailUpdateStatus](https://docs.aws.amazon.com/accounts/latest/reference/API_GetPrimaryEmailUpdateStatus.html)  **
  - **Description:** Grants permission to retrieve information about the most recent primary email update for the account
  - **Resource types (\*required):** [accountInOrganization](#list_account-resource-accountInOrganization)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRegionOptStatus](https://docs.aws.amazon.com/accounts/latest/reference/API_GetRegionOptStatus.html)  **
  - **Description:** Grants permission to get the opt-in status of a Region
  - **Resource types (\*required):** [account](#list_account-resource-account) / **Condition keys:** [account:TargetRegion](#list_account-account_TargetRegion)
  - **Resource types (\*required):** [accountInOrganization](#list_account-resource-accountInOrganization) / **Condition keys:** [account:TargetRegion](#list_account-account_TargetRegion)
  - **Access level:** Read

- **   [ListRegions](https://docs.aws.amazon.com/accounts/latest/reference/API_ListRegions.html)  **
  - **Description:** Grants permission to list the available Regions
  - **Resource types (\*required):** [account](#list_account-resource-account) / **Condition keys:**  
  - **Resource types (\*required):** [accountInOrganization](#list_account-resource-accountInOrganization) / **Condition keys:**  
  - **Access level:** List

- **   [PutAccountName](https://docs.aws.amazon.com/accounts/latest/reference/API_PutAccountName.html)  **
  - **Description:** Grants permission to update the name for an account
  - **Resource types (\*required):** [account](#list_account-resource-account) / **Condition keys:**  
  - **Resource types (\*required):** [accountInOrganization](#list_account-resource-accountInOrganization) / **Condition keys:**  
  - **Access level:** Write

- **   [PutAlternateContact](https://docs.aws.amazon.com/accounts/latest/reference/API_PutAlternateContact.html)  **
  - **Description:** Grants permission to modify the alternate contacts for an account
  - **Resource types (\*required):** [account](#list_account-resource-account) / **Condition keys:** [account:AlternateContactTypes](#list_account-account_AlternateContactTypes)
  - **Resource types (\*required):** [accountInOrganization](#list_account-resource-accountInOrganization) / **Condition keys:** [account:AlternateContactTypes](#list_account-account_AlternateContactTypes)
  - **Access level:** Write

- **   [PutContactInformation](https://docs.aws.amazon.com/accounts/latest/reference/API_PutContactInformation.html)  **
  - **Description:** Grants permission to update the primary contact information for an account
  - **Resource types (\*required):** [account](#list_account-resource-account) / **Condition keys:**  
  - **Resource types (\*required):** [accountInOrganization](#list_account-resource-accountInOrganization) / **Condition keys:**  
  - **Access level:** Write

- **   [StartPrimaryEmailUpdate](https://docs.aws.amazon.com/accounts/latest/reference/API_StartPrimaryEmailUpdate.html)  **
  - **Description:** Grants permission to start the process to update the primary email address of an account
  - **Resource types (\*required):** [accountInOrganization](#list_account-resource-accountInOrganization)
  - **Condition keys:** [account:EmailTargetDomain](#list_account-account_EmailTargetDomain)
  - **Access level:** Write



## Permission-only actions for AWS Account Management
<a name="list_account-permission-only-actions"></a>

The following actions are defined by AWS Account Management but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [CloseAccount](https://docs.aws.amazon.com/accounts/latest/reference/security_account-permissions-ref.html)  **
  - **Description:** Grants permission to close an account
  - **Resource types (\*required):** [account](#list_account-resource-account)
  - **Condition keys:**  
  - **Access level:** Write



## Resource types defined by AWS Account Management
<a name="list_account-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [account](https://docs.aws.amazon.com/accounts/latest/reference/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources)  | arn:${Partition}:account::${Account}:account |   | 
|  [accountInOrganization](https://docs.aws.amazon.com/accounts/latest/reference/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-resources)  | arn:${Partition}:account::${ManagementAccountId}:account/o-${OrganizationId}/${MemberAccountId} |   | 

## Condition keys for AWS Account Management
<a name="list_account-policy-keys"></a>

AWS Account Management defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [account:AccountResourceOrgPaths](https://docs.aws.amazon.com/accounts/latest/reference/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by the resource path for an account in an organization | ArrayOfString | 
|   [account:AccountResourceOrgTags/${TagKey}](https://docs.aws.amazon.com/accounts/latest/reference/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by resource tags for an account in an organization | String | 
|   [account:AlternateContactTypes](https://docs.aws.amazon.com/accounts/latest/reference/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by alternate contact types | ArrayOfString | 
|   [account:EmailTargetDomain](https://docs.aws.amazon.com/accounts/latest/reference/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by email domain of the target email address | String | 
|   [account:TargetRegion](https://docs.aws.amazon.com/accounts/latest/reference/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-conditionkeys)  | Filters access by a list of Regions. Enables or disables all the Regions specified here | String | 