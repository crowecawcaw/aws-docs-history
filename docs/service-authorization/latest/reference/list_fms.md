

# Actions, resources, and condition keys for AWS Firewall Manager
<a name="list_fms"></a>

AWS Firewall Manager (service prefix: `fms`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/waf/latest/developerguide/fms-auth-and-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/fms/fms.json) for this service.

**Topics**
+ [API operations defined by AWS Firewall Manager](#list_fms-operations)
+ [Actions defined by AWS Firewall Manager](#list_fms-actions-as-permissions)
+ [Resource types defined by AWS Firewall Manager](#list_fms-resources-for-iam-policies)
+ [Condition keys for AWS Firewall Manager](#list_fms-policy-keys)

## API operations defined by AWS Firewall Manager
<a name="list_fms-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_fms-actions-as-permissions).




- **   AssociateAdminAccount  **
  - **IAM action:**  [fms:AssociateAdminAccount](#list_fms-action-AssociateAdminAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociateThirdPartyFirewall  **
  - **IAM action:**  [fms:AssociateThirdPartyFirewall](#list_fms-action-AssociateThirdPartyFirewall) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchAssociateResource  **
  - **IAM action:**  [fms:BatchAssociateResource](#list_fms-action-BatchAssociateResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   BatchDisassociateResource  **
  - **IAM action:**  [fms:BatchDisassociateResource](#list_fms-action-BatchDisassociateResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteAppsList  **
  - **IAM action:**  [fms:DeleteAppsList](#list_fms-action-DeleteAppsList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteNotificationChannel  **
  - **IAM action:**  [fms:DeleteNotificationChannel](#list_fms-action-DeleteNotificationChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePolicy  **
  - **IAM action:**  [fms:DeletePolicy](#list_fms-action-DeletePolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProtocolsList  **
  - **IAM action:**  [fms:DeleteProtocolsList](#list_fms-action-DeleteProtocolsList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteResourceSet  **
  - **IAM action:**  [fms:DeleteResourceSet](#list_fms-action-DeleteResourceSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateAdminAccount  **
  - **IAM action:**  [fms:DisassociateAdminAccount](#list_fms-action-DisassociateAdminAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DisassociateThirdPartyFirewall  **
  - **IAM action:**  [fms:DisassociateThirdPartyFirewall](#list_fms-action-DisassociateThirdPartyFirewall) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetAdminAccount  **
  - **IAM action:**  [fms:GetAdminAccount](#list_fms-action-GetAdminAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAdminScope  **
  - **IAM action:**  [fms:GetAdminScope](#list_fms-action-GetAdminScope) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetAppsList  **
  - **IAM action:**  [fms:GetAppsList](#list_fms-action-GetAppsList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetComplianceDetail  **
  - **IAM action:**  [fms:GetComplianceDetail](#list_fms-action-GetComplianceDetail) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetNotificationChannel  **
  - **IAM action:**  [fms:GetNotificationChannel](#list_fms-action-GetNotificationChannel) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPolicy  **
  - **IAM action:**  [fms:GetPolicy](#list_fms-action-GetPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProtectionStatus  **
  - **IAM action:**  [fms:GetProtectionStatus](#list_fms-action-GetProtectionStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProtocolsList  **
  - **IAM action:**  [fms:GetProtocolsList](#list_fms-action-GetProtocolsList) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetResourceSet  **
  - **IAM action:**  [fms:GetResourceSet](#list_fms-action-GetResourceSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetThirdPartyFirewallAssociationStatus  **
  - **IAM action:**  [fms:GetThirdPartyFirewallAssociationStatus](#list_fms-action-GetThirdPartyFirewallAssociationStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetViolationDetails  **
  - **IAM action:**  [fms:GetViolationDetails](#list_fms-action-GetViolationDetails) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAdminAccountsForOrganization  **
  - **IAM action:**  [fms:ListAdminAccountsForOrganization](#list_fms-action-ListAdminAccountsForOrganization) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAdminsManagingAccount  **
  - **IAM action:**  [fms:ListAdminsManagingAccount](#list_fms-action-ListAdminsManagingAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAppsLists  **
  - **IAM action:**  [fms:ListAppsLists](#list_fms-action-ListAppsLists) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListComplianceStatus  **
  - **IAM action:**  [fms:ListComplianceStatus](#list_fms-action-ListComplianceStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDiscoveredResources  **
  - **IAM action:**  [fms:ListDiscoveredResources](#list_fms-action-ListDiscoveredResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListMemberAccounts  **
  - **IAM action:**  [fms:ListMemberAccounts](#list_fms-action-ListMemberAccounts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPolicies  **
  - **IAM action:**  [fms:ListPolicies](#list_fms-action-ListPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProtocolsLists  **
  - **IAM action:**  [fms:ListProtocolsLists](#list_fms-action-ListProtocolsLists) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceSetResources  **
  - **IAM action:**  [fms:ListResourceSetResources](#list_fms-action-ListResourceSetResources) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListResourceSets  **
  - **IAM action:**  [fms:ListResourceSets](#list_fms-action-ListResourceSets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [fms:ListTagsForResource](#list_fms-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListThirdPartyFirewallFirewallPolicies  **
  - **IAM action:**  [fms:ListThirdPartyFirewallFirewallPolicies](#list_fms-action-ListThirdPartyFirewallFirewallPolicies) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PutAdminAccount  **
  - **IAM action:**  [fms:PutAdminAccount](#list_fms-action-PutAdminAccount) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   PutAppsList  **
  - **IAM action:**  [fms:PutAppsList](#list_fms-action-PutAppsList)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [fms:TagResource](#list_fms-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutNotificationChannel  **
  - **IAM action:**  [fms:PutNotificationChannel](#list_fms-action-PutNotificationChannel)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** fms.amazonaws.com / **Access level:** Write

- **   PutPolicy  **
  - **IAM action:**  [fms:PutPolicy](#list_fms-action-PutPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [fms:TagResource](#list_fms-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutProtocolsList  **
  - **IAM action:**  [fms:PutProtocolsList](#list_fms-action-PutProtocolsList)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [fms:TagResource](#list_fms-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutResourceSet  **
  - **IAM action:**  [fms:PutResourceSet](#list_fms-action-PutResourceSet)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [fms:TagResource](#list_fms-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   TagResource  **
  - **IAM action:**  [fms:TagResource](#list_fms-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [fms:UntagResource](#list_fms-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write



## Actions defined by AWS Firewall Manager
<a name="list_fms-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateAdminAccount](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_AssociateAdminAccount.html)  **
  - **Description:** Grants permission to set the AWS Firewall Manager administrator account and enables the service in all organization accounts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [AssociateThirdPartyFirewall](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_AssociateThirdPartyFirewall.html)  **
  - **Description:** Grants permission to set the Firewall Manager administrator as a tenant administrator of a third-party firewall service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [BatchAssociateResource](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_BatchAssociateResource.html)  **
  - **Description:** Grants permission to associate resources to an AWS Firewall Manager resource set
  - **Resource types (\*required):** [resource-set\*](#list_fms-resource-resource-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [BatchDisassociateResource](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_BatchDisassociateResource.html)  **
  - **Description:** Grants permission to disassociate resources from an AWS Firewall Manager resource set
  - **Resource types (\*required):** [resource-set\*](#list_fms-resource-resource-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteAppsList](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_DeleteAppsList.html)  **
  - **Description:** Grants permission to permanently deletes an AWS Firewall Manager applications list
  - **Resource types (\*required):** [applications-list\*](#list_fms-resource-applications-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteNotificationChannel](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_DeleteNotificationChannel.html)  **
  - **Description:** Grants permission to delete an AWS Firewall Manager association with the IAM role and the Amazon Simple Notification Service (SNS) topic that is used to notify the FM administrator about major FM events and errors across the organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeletePolicy](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_DeletePolicy.html)  **
  - **Description:** Grants permission to permanently delete an AWS Firewall Manager policy
  - **Resource types (\*required):** [policy\*](#list_fms-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProtocolsList](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_DeleteProtocolsList.html)  **
  - **Description:** Grants permission to permanently deletes an AWS Firewall Manager protocols list
  - **Resource types (\*required):** [protocols-list\*](#list_fms-resource-protocols-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteResourceSet](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_DeleteResourceSet.html)  **
  - **Description:** Grants permission to permanently delete an AWS Firewall Manager resource set
  - **Resource types (\*required):** [resource-set\*](#list_fms-resource-resource-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DisassociateAdminAccount](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_DisassociateAdminAccount.html)  **
  - **Description:** Grants permission to disassociate the account that has been set as the AWS Firewall Manager administrator account and and disables the service in all organization accounts
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DisassociateThirdPartyFirewall](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_DisassociateThirdPartyFirewall.html)  **
  - **Description:** Grants permission to disassociate a Firewall Manager administrator from a third-party firewall tenant
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetAdminAccount](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetAdminAccount.html)  **
  - **Description:** Grants permission to return the AWS Organizations account that is associated with AWS Firewall Manager as the AWS Firewall Manager administrator
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAdminScope](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetAdminScope.html)  **
  - **Description:** Grants permission to return information about the specified account's administrative scope
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetAppsList](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetAppsList.html)  **
  - **Description:** Grants permission to return information about the specified AWS Firewall Manager applications list
  - **Resource types (\*required):** [applications-list\*](#list_fms-resource-applications-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetComplianceDetail](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetComplianceDetail.html)  **
  - **Description:** Grants permission to retrieve detailed compliance information about the specified member account. Details include resources that are in and out of compliance with the specified policy
  - **Resource types (\*required):** [policy\*](#list_fms-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetNotificationChannel](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetNotificationChannel.html)  **
  - **Description:** Grants permission to retrieve information about the Amazon Simple Notification Service (SNS) topic that is used to record AWS Firewall Manager SNS logs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetPolicy](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetPolicy.html)  **
  - **Description:** Grants permission to retrieve information about the specified AWS Firewall Manager policy
  - **Resource types (\*required):** [policy\*](#list_fms-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProtectionStatus](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetProtectionStatus.html)  **
  - **Description:** Grants permission to retrieve policy-level attack summary information in the event of a potential DDoS attack
  - **Resource types (\*required):** [policy\*](#list_fms-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProtocolsList](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetProtocolsList.html)  **
  - **Description:** Grants permission to return information about the specified AWS Firewall Manager protocols list
  - **Resource types (\*required):** [protocols-list\*](#list_fms-resource-protocols-list)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetResourceSet](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetResourceSet.html)  **
  - **Description:** Grants permission to retrieve information about the specified AWS Firewall Manager resource set
  - **Resource types (\*required):** [resource-set\*](#list_fms-resource-resource-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetThirdPartyFirewallAssociationStatus](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetThirdPartyFirewallAssociationStatus.html)  **
  - **Description:** Grants permission to retrieve the onboarding status of a Firewall Manager administrator account to third-party firewall vendor tenant
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetViolationDetails](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetViolationDetails.html)  **
  - **Description:** Grants permission to retrieve violations for a resource based on the specified AWS Firewall Manager policy and AWS account
  - **Resource types (\*required):** [policy\*](#list_fms-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAdminAccountsForOrganization](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListAdminAccountsForOrganization.html)  **
  - **Description:** Grants permission to return a AdminAccounts object that lists the Firewall Manager administrators within the organization that are onboarded to Firewall Manager by AssociateAdminAccount
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAdminsManagingAccount](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListAdminsManagingAccount.html)  **
  - **Description:** Grants permission to list the accounts that are managing the specified AWS Organizations member account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListAppsLists](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListAppsLists.html)  **
  - **Description:** Grants permission to return an array of AppsListDataSummary objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListComplianceStatus](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListComplianceStatus.html)  **
  - **Description:** Grants permission to retrieve an array of PolicyComplianceStatus objects in the response. Use PolicyComplianceStatus to get a summary of which member accounts are protected by the specified policy
  - **Resource types (\*required):** [policy\*](#list_fms-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDiscoveredResources](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListDiscoveredResources.html)  **
  - **Description:** Grants permission to retrieve an array of resources in the organization's accounts that are available to be associated with a resource set
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMemberAccounts](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListMemberAccounts.html)  **
  - **Description:** Grants permission to retrieve an array of member account ids if the caller is FMS admin account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPolicies](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListPolicies.html)  **
  - **Description:** Grants permission to retrieve an array of PolicySummary objects in the response
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProtocolsLists](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListProtocolsLists.html)  **
  - **Description:** Grants permission to return an array of ProtocolsListDataSummary objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListResourceSetResources](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListResourceSetResources.html)  **
  - **Description:** Grants permission to retrieve an array of resources that are currently associated to a resource set
  - **Resource types (\*required):** [resource-set\*](#list_fms-resource-resource-set)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListResourceSets](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListResourceSets.html)  **
  - **Description:** Grants permission to retrieve an array of ResourceSetSummary objects
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list Tags for a given resource
  - **Resource types (\*required):** [policy\*](#list_fms-resource-policy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListThirdPartyFirewallFirewallPolicies](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListThirdPartyFirewallFirewallPolicies.html)  **
  - **Description:** Grants permission to retrieve a list of all of the third-party firewall policies that are associated with the third-party firewall administrator's account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PutAdminAccount](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PutAdminAccount.html)  **
  - **Description:** Grants permission to create or update an Firewall Manager administrator account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutAppsList](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PutAppsList.html)  **
  - **Description:** Grants permission to create an AWS Firewall Manager applications list
  - **Resource types (\*required):** [applications-list\*](#list_fms-resource-applications-list)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_fms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fms-aws_TagKeys)
  - **Access level:** Write

- **   [PutNotificationChannel](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PutNotificationChannel.html)  **
  - **Description:** Grants permission to designate the IAM role and Amazon Simple Notification Service (SNS) topic that AWS Firewall Manager (FM) could use to notify the FM administrator about major FM events and errors across the organization
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutPolicy](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PutPolicy.html)  **
  - **Description:** Grants permission to create an AWS Firewall Manager policy
  - **Resource types (\*required):** [policy\*](#list_fms-resource-policy)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_fms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fms-aws_TagKeys)
  - **Access level:** Write

- **   [PutProtocolsList](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PutProtocolsList.html)  **
  - **Description:** Grants permission to creates an AWS Firewall Manager protocols list
  - **Resource types (\*required):** [protocols-list\*](#list_fms-resource-protocols-list)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_fms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fms-aws_TagKeys)
  - **Access level:** Write

- **   [PutResourceSet](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_PutResourceSet.html)  **
  - **Description:** Grants permission to create an AWS Firewall Manager resource set
  - **Resource types (\*required):** [resource-set\*](#list_fms-resource-resource-set)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_fms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fms-aws_TagKeys)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add a Tag to a given resource
  - **Resource types (\*required):** [applications-list](#list_fms-resource-applications-list) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fms-aws_TagKeys)
  - **Resource types (\*required):** [policy](#list_fms-resource-policy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fms-aws_TagKeys)
  - **Resource types (\*required):** [protocols-list](#list_fms-resource-protocols-list) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fms-aws_TagKeys)
  - **Resource types (\*required):** [resource-set](#list_fms-resource-resource-set) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_fms-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fms-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove a Tag from a given resource
  - **Resource types (\*required):** [applications-list](#list_fms-resource-applications-list) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fms-aws_TagKeys)
  - **Resource types (\*required):** [policy](#list_fms-resource-policy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fms-aws_TagKeys)
  - **Resource types (\*required):** [protocols-list](#list_fms-resource-protocols-list) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fms-aws_TagKeys)
  - **Resource types (\*required):** [resource-set](#list_fms-resource-resource-set) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_fms-aws_TagKeys)
  - **Access level:** Tagging, Write



## Resource types defined by AWS Firewall Manager
<a name="list_fms-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [applications-list](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_AppsListData.html)  | arn:${Partition}:fms:${Region}:${Account}:applications-list/${Id} | [aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_) | 
|  [policy](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_Policy.html)  | arn:${Partition}:fms:${Region}:${Account}:policy/${Id} | [aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_) | 
|  [protocols-list](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ProtocolsListData.html)  | arn:${Partition}:fms:${Region}:${Account}:protocols-list/${Id} | [aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_) | 
|  [resource-set](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ResourceSet.html)  | arn:${Partition}:fms:${Region}:${Account}:resource-set/${Id} | [aws:ResourceTag/${TagKey}](#list_fms-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Firewall Manager
<a name="list_fms-policy-keys"></a>

AWS Firewall Manager defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by the presence of tag key-value pairs in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access by the tag key-value pairs attached to the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the the presence of tag keys in the request | ArrayOfString | 