

# Actions, resources, and condition keys for Amazon OpenSearch
<a name="list_opensearch"></a>

Amazon OpenSearch (service prefix: `opensearch`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/opensearch/opensearch.json) for this service.

**Topics**
+ [API operations defined by Amazon OpenSearch](#list_opensearch-operations)
+ [Actions defined by Amazon OpenSearch](#list_opensearch-actions-as-permissions)
+ [Permission-only actions for Amazon OpenSearch](#list_opensearch-permission-only-actions)
+ [Resource types defined by Amazon OpenSearch](#list_opensearch-resources-for-iam-policies)
+ [Condition keys for Amazon OpenSearch](#list_opensearch-policy-keys)

## API operations defined by Amazon OpenSearch
<a name="list_opensearch-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_opensearch-actions-as-permissions).




- **   AcceptInboundConnection  **
  - **IAM action:**  [es:AcceptInboundConnection](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AcceptInboundConnection.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [es:AcceptInboundCrossClusterSearchConnection](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AcceptInboundConnection.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   AddDataSource  **
  - **IAM action:**  [es:AddDataSource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AddDataSource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** directquery.opensearchservice.amazonaws.com / **Access level:** Write

- **   AddDirectQueryDataSource  **
  - **IAM action:**  [es:AddDirectQueryDataSource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AddDirectQueryDataSource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [es:AddTags](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AddTags.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** directquery.opensearchservice.amazonaws.com / **Access level:** Write

- **   AddTags  **
  - **IAM action:**  [es:AddTags](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AddTags.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   AssociatePackage  **
  - **IAM action:**  [es:AssociatePackage](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AssociatePackage.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AssociatePackages  **
  - **IAM action:**  [es:AssociatePackages](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AssociatePackages.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AttachDataSource  **
  - **IAM action:**  [es:AttachDataSource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AttachDataSource.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   AuthorizeVpcEndpointAccess  **
  - **IAM action:**  [es:AuthorizeVpcEndpointAccess](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AuthorizeVpcEndpointAccess.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelDomainConfigChange  **
  - **IAM action:**  [es:CancelDomainConfigChange](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CancelDomainConfigChange.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelServiceSoftwareUpdate  **
  - **IAM action:**  [es:CancelElasticsearchServiceSoftwareUpdate](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CancelServiceSoftwareUpdate.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [es:CancelServiceSoftwareUpdate](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CancelServiceSoftwareUpdate.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateApplication  **
  - **IAM action:**  [es:AddTags](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AddTags.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [es:CreateApplication](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreateApplication.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateDomain  **
  - **IAM action:**  [es:AddTags](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AddTags.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [es:CreateDomain](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreateDomain.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [es:CreateElasticsearchDomain](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreateDomain.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** es.amazonaws.com / **Access level:** Write

- **   CreateIndex  **
  - **IAM action:**  [es:CreateIndex](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreateIndex.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateOutboundConnection  **
  - **IAM action:**  [es:CreateOutboundConnection](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreateOutboundConnection.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [es:CreateOutboundCrossClusterSearchConnection](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreateOutboundConnection.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreatePackage  **
  - **IAM action:**  [es:CreatePackage](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreatePackage.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateVpcEndpoint  **
  - **IAM action:**  [es:CreateVpcEndpoint](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreateVpcEndpoint.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteApplication  **
  - **IAM action:**  [es:DeleteApplication](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteApplication.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDataSource  **
  - **IAM action:**  [es:DeleteDataSource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteDataSource.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDirectQueryDataSource  **
  - **IAM action:**  [es:DeleteDirectQueryDataSource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteDirectQueryDataSource.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteDomain  **
  - **IAM action:**  [es:DeleteDomain](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteDomain.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [es:DeleteElasticsearchDomain](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteDomain.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteInboundConnection  **
  - **IAM action:**  [es:DeleteInboundConnection](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteInboundConnection.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteIndex  **
  - **IAM action:**  [es:DeleteIndex](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteIndex.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOutboundConnection  **
  - **IAM action:**  [es:DeleteOutboundConnection](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteOutboundConnection.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [es:DeleteOutboundCrossClusterSearchConnection](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteOutboundConnection.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeletePackage  **
  - **IAM action:**  [es:DeletePackage](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeletePackage.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVpcEndpoint  **
  - **IAM action:**  [es:DeleteVpcEndpoint](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteVpcEndpoint.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeregisterCapability  **
  - **IAM action:**  [es:DeregisterCapability](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeregisterCapability.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeDataSourceAttachment  **
  - **IAM action:**  [es:DescribeDataSourceAttachment](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDataSourceAttachment.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDomain  **
  - **IAM action:**  [es:DescribeDomain](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomain.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [es:DescribeElasticsearchDomain](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomain.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeDomainAutoTunes  **
  - **IAM action:**  [es:DescribeDomainAutoTunes](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomainAutoTunes.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDomainChangeProgress  **
  - **IAM action:**  [es:DescribeDomainChangeProgress](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomainChangeProgress.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDomainConfig  **
  - **IAM action:**  [es:DescribeDomainConfig](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomainConfig.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [es:DescribeElasticsearchDomainConfig](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomainConfig.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeDomainHealth  **
  - **IAM action:**  [es:DescribeDomainHealth](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomainHealth.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDomainNodes  **
  - **IAM action:**  [es:DescribeDomainNodes](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomainNodes.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDomains  **
  - **IAM action:**  [es:DescribeDomains](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomains.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [es:DescribeElasticsearchDomains](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomains.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribeDryRunProgress  **
  - **IAM action:**  [es:DescribeDryRunProgress](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDryRunProgress.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInboundConnections  **
  - **IAM action:**  [es:DescribeInboundConnections](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeInboundConnections.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [es:DescribeInboundCrossClusterSearchConnections](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeInboundConnections.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribeInsightDetails  **
  - **IAM action:**  [es:DescribeInsightDetails](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeInsightDetails.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeInstanceTypeLimits  **
  - **IAM action:**  [es:DescribeElasticsearchInstanceTypeLimits](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeInstanceTypeLimits.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [es:DescribeInstanceTypeLimits](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeInstanceTypeLimits.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribeOutboundConnections  **
  - **IAM action:**  [es:DescribeOutboundConnections](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeOutboundConnections.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [es:DescribeOutboundCrossClusterSearchConnections](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeOutboundConnections.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribePackages  **
  - **IAM action:**  [es:DescribePackages](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribePackages.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReservedInstanceOfferings  **
  - **IAM action:**  [es:DescribeReservedElasticsearchInstanceOfferings](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeReservedInstanceOfferings.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [es:DescribeReservedInstanceOfferings](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeReservedInstanceOfferings.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribeReservedInstances  **
  - **IAM action:**  [es:DescribeReservedElasticsearchInstances](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeReservedInstances.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [es:DescribeReservedInstances](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeReservedInstances.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribeVpcEndpoints  **
  - **IAM action:**  [es:DescribeVpcEndpoints](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeVpcEndpoints.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DetachDataSource  **
  - **IAM action:**  [es:DetachDataSource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DetachDataSource.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DissociatePackage  **
  - **IAM action:**  [es:DissociatePackage](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DissociatePackage.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DissociatePackages  **
  - **IAM action:**  [es:DissociatePackages](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DissociatePackages.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetApplication  **
  - **IAM action:**  [es:GetApplication](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetApplication.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCapability  **
  - **IAM action:**  [es:GetCapability](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetCapability.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCompatibleVersions  **
  - **IAM action:**  [es:GetCompatibleElasticsearchVersions](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetCompatibleVersions.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [es:GetCompatibleVersions](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetCompatibleVersions.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   GetDataSource  **
  - **IAM action:**  [es:GetDataSource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetDataSource.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDefaultApplicationSetting  **
  - **IAM action:**  [es:GetDefaultApplicationSetting](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetDefaultApplicationSetting.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDirectQueryDataSource  **
  - **IAM action:**  [es:GetDirectQueryDataSource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetDirectQueryDataSource.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDomainMaintenanceStatus  **
  - **IAM action:**  [es:GetDomainMaintenanceStatus](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetDomainMaintenanceStatus.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetIndex  **
  - **IAM action:**  [es:GetIndex](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetIndex.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetMigration  **
  - **IAM action:**  [es:GetMigration](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetMigration.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPackageVersionHistory  **
  - **IAM action:**  [es:GetPackageVersionHistory](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetPackageVersionHistory.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUpgradeHistory  **
  - **IAM action:**  [es:GetUpgradeHistory](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetUpgradeHistory.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUpgradeStatus  **
  - **IAM action:**  [es:GetUpgradeStatus](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetUpgradeStatus.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   InsightFeedback  **
  - **IAM action:**  [es:InsightFeedback](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_InsightFeedback.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   ListApplications  **
  - **IAM action:**  [es:ListApplications](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListApplications.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataSourceAttachments  **
  - **IAM action:**  [es:ListDataSourceAttachments](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListDataSourceAttachments.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDataSources  **
  - **IAM action:**  [es:ListDataSources](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListDataSources.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDirectQueryDataSources  **
  - **IAM action:**  [es:ListDirectQueryDataSources](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListDirectQueryDataSources.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDomainMaintenances  **
  - **IAM action:**  [es:ListDomainMaintenances](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListDomainMaintenances.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDomainNames  **
  - **IAM action:**  [es:ListDomainNames](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListDomainNames.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDomainsForPackage  **
  - **IAM action:**  [es:ListDomainsForPackage](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListDomainsForPackage.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInsights  **
  - **IAM action:**  [es:ListInsights](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListInsights.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListInstanceTypeDetails  **
  - **IAM action:**  [es:ListElasticsearchInstanceTypeDetails](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListInstanceTypeDetails.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [es:ListInstanceTypeDetails](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListInstanceTypeDetails.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListMigrations  **
  - **IAM action:**  [es:ListMigrations](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListMigrations.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPackagesForDomain  **
  - **IAM action:**  [es:ListPackagesForDomain](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListPackagesForDomain.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListScheduledActions  **
  - **IAM action:**  [es:ListScheduledActions](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListScheduledActions.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTags  **
  - **IAM action:**  [es:ListTags](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListTags.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListVersions  **
  - **IAM action:**  [es:ListElasticsearchVersions](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListVersions.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [es:ListVersions](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListVersions.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListVpcEndpointAccess  **
  - **IAM action:**  [es:ListVpcEndpointAccess](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListVpcEndpointAccess.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVpcEndpoints  **
  - **IAM action:**  [es:ListVpcEndpoints](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListVpcEndpoints.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVpcEndpointsForDomain  **
  - **IAM action:**  [es:ListVpcEndpointsForDomain](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListVpcEndpointsForDomain.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PurchaseReservedInstanceOffering  **
  - **IAM action:**  [es:PurchaseReservedElasticsearchInstanceOffering](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_PurchaseReservedInstanceOffering.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [es:PurchaseReservedInstanceOffering](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_PurchaseReservedInstanceOffering.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   PutDefaultApplicationSetting  **
  - **IAM action:**  [es:PutDefaultApplicationSetting](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_PutDefaultApplicationSetting.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RegisterCapability  **
  - **IAM action:**  [es:RegisterCapability](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_RegisterCapability.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RejectInboundConnection  **
  - **IAM action:**  [es:RejectInboundConnection](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_RejectInboundConnection.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [es:RejectInboundCrossClusterSearchConnection](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_RejectInboundConnection.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   RemoveTags  **
  - **IAM action:**  [es:RemoveTags](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_RemoveTags.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   RevokeVpcEndpointAccess  **
  - **IAM action:**  [es:RevokeVpcEndpointAccess](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_RevokeVpcEndpointAccess.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   RollbackServiceSoftwareUpdate  **
  - **IAM action:**  [es:RollbackElasticsearchServiceSoftwareUpdate](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_RollbackServiceSoftwareUpdate.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [es:RollbackServiceSoftwareUpdate](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_RollbackServiceSoftwareUpdate.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   StartDomainMaintenance  **
  - **IAM action:**  [es:StartDomainMaintenance](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_StartDomainMaintenance.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartMigration  **
  - **IAM action:**  [es:StartMigration](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_StartMigration.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartServiceSoftwareUpdate  **
  - **IAM action:**  [es:StartElasticsearchServiceSoftwareUpdate](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_StartServiceSoftwareUpdate.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [es:StartServiceSoftwareUpdate](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_StartServiceSoftwareUpdate.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateApplication  **
  - **IAM action:**  [es:UpdateApplication](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdateApplication.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateDataSource  **
  - **IAM action:**  [es:UpdateDataSource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdateDataSource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** directquery.opensearchservice.amazonaws.com / **Access level:** Write

- **   UpdateDirectQueryDataSource  **
  - **IAM action:**  [es:UpdateDirectQueryDataSource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdateDirectQueryDataSource.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** directquery.opensearchservice.amazonaws.com / **Access level:** Write

- **   UpdateDomainConfig  **
  - **IAM action:**  [es:UpdateDomainConfig](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdateDomainConfig.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [es:UpdateElasticsearchDomainConfig](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdateDomainConfig.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** es.amazonaws.com / **Access level:** Write

- **   UpdateIndex  **
  - **IAM action:**  [es:UpdateIndex](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdateIndex.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePackage  **
  - **IAM action:**  [es:UpdatePackage](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdatePackage.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdatePackageScope  **
  - **IAM action:**  [es:UpdatePackageScope](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdatePackageScope.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateScheduledAction  **
  - **IAM action:**  [es:UpdateScheduledAction](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdateScheduledAction.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateVpcEndpoint  **
  - **IAM action:**  [es:UpdateVpcEndpoint](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdateVpcEndpoint.html) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpgradeDomain  **
  - **IAM action:**  [es:UpgradeDomain](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpgradeDomain.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [es:UpgradeElasticsearchDomain](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpgradeDomain.html)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write



## Actions defined by Amazon OpenSearch
<a name="list_opensearch-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelAutoOptimizeJob](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-auto-optimize.html)  **
  - **Description:** Grants permission to cancel submitted Auto Optimize Job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelDirectQuery](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CancelDirectQuery.html)  **
  - **Description:** Grants permission to cancel the query that is submitted on the OpenSearch DataSource resource
  - **Resource types (\*required):** [datasource\*](#list_opensearch-resource-datasource)
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteAutoOptimizeJob](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-auto-optimize.html)  **
  - **Description:** Grants permission to delete Auto Optimize Job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [GetAutoOptimizeJob](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-auto-optimize.html)  **
  - **Description:** Grants permission to get the Auto Optimize Job details
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDirectQuery](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetDirectQuery.html)  **
  - **Description:** Grants permission to get the query status that are performed on the OpenSearch DataSource resource
  - **Resource types (\*required):** [datasource\*](#list_opensearch-resource-datasource)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDirectQueryResult](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetDirectQueryResult.html)  **
  - **Description:** Grants permission to get the results of a query that is performed on the OpenSearch DataSource resource
  - **Resource types (\*required):** [datasource\*](#list_opensearch-resource-datasource)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListAutoOptimizeJobs](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-auto-optimize.html)  **
  - **Description:** Grants permission to retrieve a list of Auto Optimize Jobs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [StartDirectQuery](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_StartDirectQuery.html)  **
  - **Description:** Grants permission to start a direct query on the provided OpenSearch DataSource arns
  - **Resource types (\*required):** [datasource\*](#list_opensearch-resource-datasource)
  - **Condition keys:**  
  - **Access level:** Write

- **   [SubmitAutoOptimizeJob](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-auto-optimize.html)  **
  - **Description:** Grants permission to create new Auto Optimize Job
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write



## Permission-only actions for Amazon OpenSearch
<a name="list_opensearch-permission-only-actions"></a>

The following actions are defined by Amazon OpenSearch but are not directly invocable through any API operation. They can only be used in IAM policy statements to grant or deny permissions.




- **   [ApplicationAccessAll](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/)  **
  - **Description:** Grants permission to access OpenSearch Application
  - **Resource types (\*required):** [application\*](#list_opensearch-resource-application)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write

- **   [ViewLoginPage](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/)  **
  - **Description:** Grants permission to view the login page of an OpenSearch Application
  - **Resource types (\*required):** [application\*](#list_opensearch-resource-application)
  - **Condition keys:**  
  - **Access level:** Permissions management, Write



## Resource types defined by Amazon OpenSearch
<a name="list_opensearch-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [application](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html)  | arn:${Partition}:opensearch:${Region}:${Account}:application/${AppId} |   | 
|  [datasource](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/datasource.html)  | arn:${Partition}:opensearch:${Region}:${Account}:datasource/${DataSourceName} |   | 

## Condition keys for Amazon OpenSearch
<a name="list_opensearch-policy-keys"></a>

Amazon OpenSearch has no service-specific condition keys that can be used in the `Condition` element of policy statements.