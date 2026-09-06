

# Data retrieval APIs for AWS Firewall Manager
<a name="awsfirewallmanager"></a>

AWS Firewall Manager provides the following APIs for data retrieval.



| Actions | Description | Access level | 
| --- | --- | --- | 
| <a name="fms-GetAdminAccount"></a>[GetAdminAccount](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetAdminAccount.html) | Return the AWS Organizations account that is associated with AWS Firewall Manager as the AWS Firewall Manager administrator | Read | 
| <a name="fms-GetAdminScope"></a>[GetAdminScope](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetAdminScope.html) | Return information about the specified account's administrative scope | Read | 
| <a name="fms-GetAppsList"></a>[GetAppsList](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetAppsList.html) | Return information about the specified AWS Firewall Manager applications list | Read | 
| <a name="fms-GetComplianceDetail"></a>[GetComplianceDetail](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetComplianceDetail.html) | Retrieve detailed compliance information about the specified member account. Details include resources that are in and out of compliance with the specified policy | Read | 
| <a name="fms-GetNotificationChannel"></a>[GetNotificationChannel](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetNotificationChannel.html) | Retrieve information about the Amazon Simple Notification Service (SNS) topic that is used to record AWS Firewall Manager SNS logs | Read | 
| <a name="fms-GetPolicy"></a>[GetPolicy](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetPolicy.html) | Retrieve information about the specified AWS Firewall Manager policy | Read | 
| <a name="fms-GetProtectionStatus"></a>[GetProtectionStatus](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetProtectionStatus.html) | Retrieve policy-level attack summary information in the event of a potential DDoS attack | Read | 
| <a name="fms-GetProtocolsList"></a>[GetProtocolsList](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetProtocolsList.html) | Return information about the specified AWS Firewall Manager protocols list | Read | 
| <a name="fms-GetResourceSet"></a>[GetResourceSet](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetResourceSet.html) | Retrieve information about the specified AWS Firewall Manager resource set | Read | 
| <a name="fms-GetThirdPartyFirewallAssociationStatus"></a>[GetThirdPartyFirewallAssociationStatus](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetThirdPartyFirewallAssociationStatus.html) | Retrieve the onboarding status of a Firewall Manager administrator account to third-party firewall vendor tenant | Read | 
| <a name="fms-GetViolationDetails"></a>[GetViolationDetails](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_GetViolationDetails.html) | Retrieve violations for a resource based on the specified AWS Firewall Manager policy and AWS account | Read | 
| <a name="fms-ListAdminAccountsForOrganization"></a>[ListAdminAccountsForOrganization](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListAdminAccountsForOrganization.html) | Return a AdminAccounts object that lists the Firewall Manager administrators within the organization that are onboarded to Firewall Manager by AssociateAdminAccount | List | 
| <a name="fms-ListAdminsManagingAccount"></a>[ListAdminsManagingAccount](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListAdminsManagingAccount.html) | List the accounts that are managing the specified AWS Organizations member account | List | 
| <a name="fms-ListAppsLists"></a>[ListAppsLists](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListAppsLists.html) | Return an array of AppsListDataSummary objects | List | 
| <a name="fms-ListComplianceStatus"></a>[ListComplianceStatus](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListComplianceStatus.html) | Retrieve an array of PolicyComplianceStatus objects in the response. Use PolicyComplianceStatus to get a summary of which member accounts are protected by the specified policy | List | 
| <a name="fms-ListDiscoveredResources"></a>[ListDiscoveredResources](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListDiscoveredResources.html) | Retrieve an array of resources in the organization's accounts that are available to be associated with a resource set | List | 
| <a name="fms-ListMemberAccounts"></a>[ListMemberAccounts](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListMemberAccounts.html) | Retrieve an array of member account ids if the caller is FMS admin account | List | 
| <a name="fms-ListPolicies"></a>[ListPolicies](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListPolicies.html) | Retrieve an array of PolicySummary objects in the response | List | 
| <a name="fms-ListProtocolsLists"></a>[ListProtocolsLists](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListProtocolsLists.html) | Return an array of ProtocolsListDataSummary objects | List | 
| <a name="fms-ListResourceSetResources"></a>[ListResourceSetResources](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListResourceSetResources.html) | Retrieve an array of resources that are currently associated to a resource set | List | 
| <a name="fms-ListResourceSets"></a>[ListResourceSets](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListResourceSets.html) | Retrieve an array of ResourceSetSummary objects | List | 
| <a name="fms-ListTagsForResource"></a>[ListTagsForResource](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListTagsForResource.html) | List Tags for a given resource | Read | 
| <a name="fms-ListThirdPartyFirewallFirewallPolicies"></a>[ListThirdPartyFirewallFirewallPolicies](https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_ListThirdPartyFirewallFirewallPolicies.html) | Retrieve a list of all of the third-party firewall policies that are associated with the third-party firewall administrator's account | List | 