

# Actions, resources, and condition keys for Amazon OpenSearch Service
<a name="list_es"></a>

Amazon OpenSearch Service (service prefix: `es`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/es/es.json) for this service.

**Topics**
+ [API operations defined by Amazon OpenSearch Service](#list_es-operations)
+ [Actions defined by Amazon OpenSearch Service](#list_es-actions-as-permissions)
+ [Resource types defined by Amazon OpenSearch Service](#list_es-resources-for-iam-policies)
+ [Condition keys for Amazon OpenSearch Service](#list_es-policy-keys)

## API operations defined by Amazon OpenSearch Service
<a name="list_es-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_es-actions-as-permissions).




- **   AcceptInboundCrossClusterSearchConnection  **
  - **IAM action:**  [es:AcceptInboundConnection](#list_es-action-AcceptInboundConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [es:AcceptInboundCrossClusterSearchConnection](#list_es-action-AcceptInboundCrossClusterSearchConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   AddTags  **
  - **IAM action:**  [es:AddTags](#list_es-action-AddTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   AssociatePackage  **
  - **IAM action:**  [es:AssociatePackage](#list_es-action-AssociatePackage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** es.amazonaws.com / **Access level:** Write

- **   AuthorizeVpcEndpointAccess  **
  - **IAM action:**  [es:AuthorizeVpcEndpointAccess](#list_es-action-AuthorizeVpcEndpointAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelDomainConfigChange  **
  - **IAM action:**  [es:CancelDomainConfigChange](#list_es-action-CancelDomainConfigChange) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelElasticsearchServiceSoftwareUpdate  **
  - **IAM action:**  [es:CancelElasticsearchServiceSoftwareUpdate](#list_es-action-CancelElasticsearchServiceSoftwareUpdate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [es:CancelServiceSoftwareUpdate](#list_es-action-CancelServiceSoftwareUpdate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreateElasticsearchDomain  **
  - **IAM action:**  [es:AddTags](#list_es-action-AddTags)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write
  - **IAM action:**  [es:CreateDomain](#list_es-action-CreateDomain)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [es:CreateElasticsearchDomain](#list_es-action-CreateElasticsearchDomain)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** es.amazonaws.com / **Access level:** Write

- **   CreateOutboundCrossClusterSearchConnection  **
  - **IAM action:**  [es:CreateOutboundConnection](#list_es-action-CreateOutboundConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [es:CreateOutboundCrossClusterSearchConnection](#list_es-action-CreateOutboundCrossClusterSearchConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   CreatePackage  **
  - **IAM action:**  [es:CreatePackage](#list_es-action-CreatePackage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateVpcEndpoint  **
  - **IAM action:**  [es:CreateVpcEndpoint](#list_es-action-CreateVpcEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteElasticsearchDomain  **
  - **IAM action:**  [es:DeleteDomain](#list_es-action-DeleteDomain)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [es:DeleteElasticsearchDomain](#list_es-action-DeleteElasticsearchDomain)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeleteElasticsearchServiceRole  **
  - **IAM action:**  [es:DeleteElasticsearchServiceRole](#list_es-action-DeleteElasticsearchServiceRole) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteInboundCrossClusterSearchConnection  **
  - **IAM action:**  [es:DeleteInboundCrossClusterSearchConnection](#list_es-action-DeleteInboundCrossClusterSearchConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOutboundCrossClusterSearchConnection  **
  - **IAM action:**  [es:DeleteOutboundConnection](#list_es-action-DeleteOutboundConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [es:DeleteOutboundCrossClusterSearchConnection](#list_es-action-DeleteOutboundCrossClusterSearchConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   DeletePackage  **
  - **IAM action:**  [es:DeletePackage](#list_es-action-DeletePackage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteVpcEndpoint  **
  - **IAM action:**  [es:DeleteVpcEndpoint](#list_es-action-DeleteVpcEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DescribeDomainAutoTunes  **
  - **IAM action:**  [es:DescribeDomainAutoTunes](#list_es-action-DescribeDomainAutoTunes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeDomainChangeProgress  **
  - **IAM action:**  [es:DescribeDomainChangeProgress](#list_es-action-DescribeDomainChangeProgress) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeElasticsearchDomain  **
  - **IAM action:**  [es:DescribeDomain](#list_es-action-DescribeDomain)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [es:DescribeElasticsearchDomain](#list_es-action-DescribeElasticsearchDomain)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeElasticsearchDomainConfig  **
  - **IAM action:**  [es:DescribeDomainConfig](#list_es-action-DescribeDomainConfig)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [es:DescribeElasticsearchDomainConfig](#list_es-action-DescribeElasticsearchDomainConfig)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read

- **   DescribeElasticsearchDomains  **
  - **IAM action:**  [es:DescribeDomains](#list_es-action-DescribeDomains)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [es:DescribeElasticsearchDomains](#list_es-action-DescribeElasticsearchDomains)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribeElasticsearchInstanceTypeLimits  **
  - **IAM action:**  [es:DescribeElasticsearchInstanceTypeLimits](#list_es-action-DescribeElasticsearchInstanceTypeLimits)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [es:DescribeInstanceTypeLimits](#list_es-action-DescribeInstanceTypeLimits)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribeInboundCrossClusterSearchConnections  **
  - **IAM action:**  [es:DescribeInboundConnections](#list_es-action-DescribeInboundConnections)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [es:DescribeInboundCrossClusterSearchConnections](#list_es-action-DescribeInboundCrossClusterSearchConnections)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribeOutboundCrossClusterSearchConnections  **
  - **IAM action:**  [es:DescribeOutboundConnections](#list_es-action-DescribeOutboundConnections)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [es:DescribeOutboundCrossClusterSearchConnections](#list_es-action-DescribeOutboundCrossClusterSearchConnections)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribePackages  **
  - **IAM action:**  [es:DescribePackages](#list_es-action-DescribePackages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   DescribeReservedElasticsearchInstanceOfferings  **
  - **IAM action:**  [es:DescribeReservedElasticsearchInstanceOfferings](#list_es-action-DescribeReservedElasticsearchInstanceOfferings)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [es:DescribeReservedInstanceOfferings](#list_es-action-DescribeReservedInstanceOfferings)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribeReservedElasticsearchInstances  **
  - **IAM action:**  [es:DescribeReservedElasticsearchInstances](#list_es-action-DescribeReservedElasticsearchInstances)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [es:DescribeReservedInstances](#list_es-action-DescribeReservedInstances)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   DescribeVpcEndpoints  **
  - **IAM action:**  [es:DescribeVpcEndpoints](#list_es-action-DescribeVpcEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   DissociatePackage  **
  - **IAM action:**  [es:DissociatePackage](#list_es-action-DissociatePackage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetCompatibleElasticsearchVersions  **
  - **IAM action:**  [es:GetCompatibleElasticsearchVersions](#list_es-action-GetCompatibleElasticsearchVersions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [es:GetCompatibleVersions](#list_es-action-GetCompatibleVersions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   GetPackageVersionHistory  **
  - **IAM action:**  [es:GetPackageVersionHistory](#list_es-action-GetPackageVersionHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUpgradeHistory  **
  - **IAM action:**  [es:GetUpgradeHistory](#list_es-action-GetUpgradeHistory) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetUpgradeStatus  **
  - **IAM action:**  [es:GetUpgradeStatus](#list_es-action-GetUpgradeStatus) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListDomainNames  **
  - **IAM action:**  [es:ListDomainNames](#list_es-action-ListDomainNames) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDomainsForPackage  **
  - **IAM action:**  [es:ListDomainsForPackage](#list_es-action-ListDomainsForPackage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListElasticsearchInstanceTypes  **
  - **IAM action:**  [es:ListElasticsearchInstanceTypes](#list_es-action-ListElasticsearchInstanceTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListElasticsearchVersions  **
  - **IAM action:**  [es:ListElasticsearchVersions](#list_es-action-ListElasticsearchVersions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [es:ListVersions](#list_es-action-ListVersions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   ListPackagesForDomain  **
  - **IAM action:**  [es:ListPackagesForDomain](#list_es-action-ListPackagesForDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTags  **
  - **IAM action:**  [es:ListTags](#list_es-action-ListTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListVpcEndpointAccess  **
  - **IAM action:**  [es:ListVpcEndpointAccess](#list_es-action-ListVpcEndpointAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVpcEndpoints  **
  - **IAM action:**  [es:ListVpcEndpoints](#list_es-action-ListVpcEndpoints) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListVpcEndpointsForDomain  **
  - **IAM action:**  [es:ListVpcEndpointsForDomain](#list_es-action-ListVpcEndpointsForDomain) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   PurchaseReservedElasticsearchInstanceOffering  **
  - **IAM action:**  [es:PurchaseReservedElasticsearchInstanceOffering](#list_es-action-PurchaseReservedElasticsearchInstanceOffering)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [es:PurchaseReservedInstanceOffering](#list_es-action-PurchaseReservedInstanceOffering)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   RejectInboundCrossClusterSearchConnection  **
  - **IAM action:**  [es:RejectInboundConnection](#list_es-action-RejectInboundConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [es:RejectInboundCrossClusterSearchConnection](#list_es-action-RejectInboundCrossClusterSearchConnection)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   RemoveTags  **
  - **IAM action:**  [es:RemoveTags](#list_es-action-RemoveTags) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   RevokeVpcEndpointAccess  **
  - **IAM action:**  [es:RevokeVpcEndpointAccess](#list_es-action-RevokeVpcEndpointAccess) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartElasticsearchServiceSoftwareUpdate  **
  - **IAM action:**  [es:StartElasticsearchServiceSoftwareUpdate](#list_es-action-StartElasticsearchServiceSoftwareUpdate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [es:StartServiceSoftwareUpdate](#list_es-action-StartServiceSoftwareUpdate)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateElasticsearchDomainConfig  **
  - **IAM action:**  [es:UpdateDomainConfig](#list_es-action-UpdateDomainConfig)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [es:UpdateElasticsearchDomainConfig](#list_es-action-UpdateElasticsearchDomainConfig)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [iam:PassRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html)  / **Condition key:** iam:PassedToService / **Possible value(s):** es.amazonaws.com / **Access level:** Write

- **   UpdatePackage  **
  - **IAM action:**  [es:UpdatePackage](#list_es-action-UpdatePackage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateVpcEndpoint  **
  - **IAM action:**  [es:UpdateVpcEndpoint](#list_es-action-UpdateVpcEndpoint) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpgradeElasticsearchDomain  **
  - **IAM action:**  [es:UpgradeDomain](#list_es-action-UpgradeDomain)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [es:UpgradeElasticsearchDomain](#list_es-action-UpgradeElasticsearchDomain)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write



## Actions defined by Amazon OpenSearch Service
<a name="list_es-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AcceptInboundConnection](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AcceptInboundConnection.html)  **
  - **Description:** Grants permission to the destination domain owner to accept an inbound cross-cluster search connection request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [AcceptInboundCrossClusterSearchConnection](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AcceptInboundConnection.html)  **
  - **Description:** Grants permission to the destination domain owner to accept an inbound cross-cluster search connection request. This permission is deprecated. Use AcceptInboundConnection instead
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [AddDataSource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AddDataSource.html)  **
  - **Description:** Grants permission to add the data source for the OpenSearch Service domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AddDirectQueryDataSource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AddDirectQueryDataSource.html)  **
  - **Description:** Grants permission to add the data source for the provided OpenSearch arns
  - **Resource types (\*required):** [datasource\*](#list_es-resource-datasource)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_es-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_es-aws_TagKeys)
  - **Access level:** Write

- **   [AddTags](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AddTags.html)  **
  - **Description:** Grants permission to attach resource tags to an OpenSearch Service domain, data source, or application
  - **Resource types (\*required):** [application\*](#list_es-resource-application) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_es-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_es-aws_TagKeys)
  - **Resource types (\*required):** [datasource\*](#list_es-resource-datasource) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_es-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_es-aws_TagKeys)
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_es-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_es-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [AssociatePackage](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AssociatePackage.html)  **
  - **Description:** Grants permission to associate a package with an OpenSearch Service domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AssociatePackages](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AssociatePackages.html)  **
  - **Description:** Grants permission to associate multiple packages with an OpenSearch Service domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AttachDataSource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AttachDataSource.html)  **
  - **Description:** Grants permission to attach a data source to an OpenSearch Application
  - **Resource types (\*required):** [application\*](#list_es-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [AuthorizeVpcEndpointAccess](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AuthorizeVpcEndpointAccess.html)  **
  - **Description:** Grants permission to provide access to an Amazon OpenSearch Service domain through the use of an interface VPC endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CancelDomainConfigChange](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CancelDomainConfigChange.html)  **
  - **Description:** Grants permission to cancel a change on an OpenSearch Service domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelElasticsearchServiceSoftwareUpdate](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CancelServiceSoftwareUpdate.html)  **
  - **Description:** Grants permission to cancel a service software update of a domain. This permission is deprecated. Use CancelServiceSoftwareUpdate instead
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelServiceSoftwareUpdate](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CancelServiceSoftwareUpdate.html)  **
  - **Description:** Grants permission to cancel a service software update of a domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateApplication](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreateApplication.html)  **
  - **Description:** Grants permission to create an OpenSearch Application
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_es-aws_RequestTag___TagKey_)<br />[aws:TagKeys](#list_es-aws_TagKeys)
  - **Access level:** Write

- **   [CreateDomain](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreateDomain.html)  **
  - **Description:** Grants permission to create an Amazon OpenSearch Service domain
  - **Resource types (\*required):** [domain](#list_es-resource-domain)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_es-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_es-aws_TagKeys)
  - **Access level:** Write

- **   [CreateElasticsearchDomain](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreateDomain.html)  **
  - **Description:** Grants permission to create an OpenSearch Service domain. This permission is deprecated. Use CreateDomain instead
  - **Resource types (\*required):** [domain](#list_es-resource-domain)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_es-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_es-aws_TagKeys)
  - **Access level:** Write

- **   [CreateElasticsearchServiceRole](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to create the service-linked role required for OpenSearch Service domains that use VPC access. This permission is deprecated. OpenSearch Service creates the service-linked role for you
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateIndex](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreateIndex.html)  **
  - **Description:** Grants permission to create index for the OpenSearch Service domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateOutboundConnection](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreateOutboundConnection.html)  **
  - **Description:** Grants permission to create a new cross-cluster search connection from a source domain to a destination domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateOutboundCrossClusterSearchConnection](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreateOutboundConnection.html)  **
  - **Description:** Grants permission to create a new cross-cluster search connection from a source domain to a destination domain. This permission is deprecated. Use CreateOutboundConnection instead
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreatePackage](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreatePackage.html)  **
  - **Description:** Grants permission to add a package for use with OpenSearch Service domains
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateServiceRole](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to create the service-linked role required for Amazon OpenSearch Service domains that use VPC access
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateVpcEndpoint](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CreateVpcEndpoint.html)  **
  - **Description:** Grants permission to create an Amazon OpenSearch Service-managed VPC endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteApplication](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteApplication.html)  **
  - **Description:** Grants permission to delete an OpenSearch Application
  - **Resource types (\*required):** [application\*](#list_es-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDataSource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteDataSource.html)  **
  - **Description:** Grants permission to delete the data source for the OpenSearch Service domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDirectQueryDataSource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteDirectQueryDataSource.html)  **
  - **Description:** Grants permission to delete the data source for the provided OpenSearch arns
  - **Resource types (\*required):** [datasource\*](#list_es-resource-datasource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteDomain](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteDomain.html)  **
  - **Description:** Grants permission to delete an Amazon OpenSearch Service domain and all of its data
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteElasticsearchDomain](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteDomain.html)  **
  - **Description:** Grants permission to delete an OpenSearch Service domain and all of its data. This permission is deprecated. Use DeleteDomain instead
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteElasticsearchServiceRole](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_Welcome.html)  **
  - **Description:** Grants permission to delete the service-linked role required for OpenSearch Service domains that use VPC access. This permission is deprecated. Use the IAM API to delete service-linked roles
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteInboundConnection](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteInboundConnection.html)  **
  - **Description:** Grants permission to the destination domain owner to delete an existing inbound cross-cluster search connection
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteInboundCrossClusterSearchConnection](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteInboundConnection.html)  **
  - **Description:** Grants permission to the destination domain owner to delete an existing inbound cross-cluster search connection. This permission is deprecated. Use DeleteInboundConnection instead
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteIndex](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteIndex.html)  **
  - **Description:** Grants permission to delete Index for the OpenSearch Service domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteOutboundConnection](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteOutboundConnection.html)  **
  - **Description:** Grants permission to the source domain owner to delete an existing outbound cross-cluster search connection
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteOutboundCrossClusterSearchConnection](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteOutboundConnection.html)  **
  - **Description:** Grants permission to the source domain owner to delete an existing outbound cross-cluster search connection. This permission is deprecated. Use DeleteOutboundConnection instead
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeletePackage](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeletePackage.html)  **
  - **Description:** Grants permission to delete a package from OpenSearch Service. The package cannot be associated with any domains
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteVpcEndpoint](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeleteVpcEndpoint.html)  **
  - **Description:** Grants permission to delete an Amazon OpenSearch Service-managed interface VPC endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeregisterCapability](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DeregisterCapability.html)  **
  - **Description:** Grants permission to deregister a capability from an OpenSearch Application
  - **Resource types (\*required):** [application\*](#list_es-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DescribeDataSourceAttachment](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDataSourceAttachment.html)  **
  - **Description:** Grants permission to describe the status of a data source attachment for an OpenSearch Application
  - **Resource types (\*required):** [application\*](#list_es-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDomain](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomain.html)  **
  - **Description:** Grants permission to view a description of the domain configuration for the specified OpenSearch Service domain, including the domain ID, service endpoint, and ARN
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDomainAutoTunes](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomainAutoTunes.html)  **
  - **Description:** Grants permission to view the Auto-Tune configuration of the domain for the specified OpenSearch Service domain, including the Auto-Tune state and maintenance schedules
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDomainChangeProgress](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomainChangeProgress.html)  **
  - **Description:** Grants permission to view detail stage progress of an OpenSearch Service domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDomainConfig](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomainConfig.html)  **
  - **Description:** Grants permission to view a description of the configuration options and status of an OpenSearch Service domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDomainHealth](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomainHealth.html)  **
  - **Description:** Grants permission to view information about domain and node health, the standby Availability Zone, number of nodes per Availability Zone, and shard count per node
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDomainNodes](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomainNodes.html)  **
  - **Description:** Grants permission to view information about nodes configured for the domain and their configurations- the node id, type of node, status of node, Availability Zone, instance type and storage
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeDomains](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomains.html)  **
  - **Description:** Grants permission to view a description of the domain configuration for up to five specified OpenSearch Service domains
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeDryRunProgress](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDryRunProgress.html)  **
  - **Description:** Grants permission to describe the status of a pre-update validation check on an OpenSearch Service domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeElasticsearchDomain](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomain.html)  **
  - **Description:** Grants permission to view a description of the domain configuration for the specified OpenSearch Service domain, including the domain ID, service endpoint, and ARN. This permission is deprecated. Use DescribeDomain instead
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeElasticsearchDomainConfig](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomainConfig.html)  **
  - **Description:** Grants permission to view a description of the configuration and status of an OpenSearch Service domain. This permission is deprecated. Use DescribeDomainConfig instead
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeElasticsearchDomains](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomains.html)  **
  - **Description:** Grants permission to view a description of the domain configuration for up to five specified Amazon OpenSearch domains. This permission is deprecated. Use DescribeDomains instead
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [DescribeElasticsearchInstanceTypeLimits](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeInstanceTypeLimits.html)  **
  - **Description:** Grants permission to view the instance count, storage, and master node limits for a given OpenSearch version and instance type. This permission is deprecated. Use DescribeInstanceTypeLimits instead
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeInboundConnections](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeInboundConnections.html)  **
  - **Description:** Grants permission to list all the inbound cross-cluster search connections for a destination domain
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeInboundCrossClusterSearchConnections](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeInboundConnections.html)  **
  - **Description:** Grants permission to list all the inbound cross-cluster search connections for a destination domain. This permission is deprecated. Use DescribeInboundConnections instead
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeInsightDetails](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeInsightDetails.html)  **
  - **Description:** Grants permission to view detailed information about insights for an OpenSearch Service domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [DescribeInstanceTypeLimits](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeInstanceTypeLimits.html)  **
  - **Description:** Grants permission to view the instance count, storage, and master node limits for a given engine version and instance type
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeOutboundConnections](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeOutboundConnections.html)  **
  - **Description:** Grants permission to list all the outbound cross-cluster search connections for a source domain
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeOutboundCrossClusterSearchConnections](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeOutboundConnections.html)  **
  - **Description:** Grants permission to list all the outbound cross-cluster search connections for a source domain. This permission is deprecated. Use DescribeOutboundConnections instead
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribePackages](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribePackages.html)  **
  - **Description:** Grants permission to describe all packages available to OpenSearch Service domains
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [DescribeReservedElasticsearchInstanceOfferings](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeReservedInstanceOfferings.html)  **
  - **Description:** Grants permission to fetch Reserved Instance offerings for Amazon OpenSearch Service. This permission is deprecated. Use DescribeReservedInstanceOfferings instead
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeReservedElasticsearchInstances](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeReservedInstances.html)  **
  - **Description:** Grants permission to fetch OpenSearch Service Reserved Instances that have already been purchased. This permission is deprecated. Use DescribeReservedInstances instead
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeReservedInstanceOfferings](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeReservedInstanceOfferings.html)  **
  - **Description:** Grants permission to fetch Reserved Instance offerings for OpenSearch Service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeReservedInstances](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeReservedInstances.html)  **
  - **Description:** Grants permission to fetch OpenSearch Service Reserved Instances that have already been purchased
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DescribeVpcEndpoints](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeVpcEndpoints.html)  **
  - **Description:** Grants permission to describe one or more Amazon OpenSearch Service-managed VPC endpoints
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [DetachDataSource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DetachDataSource.html)  **
  - **Description:** Grants permission to detach a data source from an OpenSearch Application
  - **Resource types (\*required):** [application\*](#list_es-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DissociatePackage](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DissociatePackage.html)  **
  - **Description:** Grants permission to disassociate a package from the specified OpenSearch Service domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DissociatePackages](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DissociatePackages.html)  **
  - **Description:** Grants permission to disassociate multiple packages from the specified OpenSearch Service domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ESCrossClusterGet](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to send cross-cluster requests to a destination domain
  - **Resource types (\*required):** [domain](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ESHttpDelete](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to send HTTP DELETE requests to the OpenSearch APIs
  - **Resource types (\*required):** [domain](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ESHttpGet](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to send HTTP GET requests to the OpenSearch APIs
  - **Resource types (\*required):** [domain](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ESHttpHead](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to send HTTP HEAD requests to the OpenSearch APIs
  - **Resource types (\*required):** [domain](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ESHttpPatch](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to send HTTP PATCH requests to the OpenSearch APIs
  - **Resource types (\*required):** [domain](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ESHttpPost](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to send HTTP POST requests to the OpenSearch APIs
  - **Resource types (\*required):** [domain](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ESHttpPut](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/Welcome.html)  **
  - **Description:** Grants permission to send HTTP PUT requests to the OpenSearch APIs
  - **Resource types (\*required):** [domain](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetApplication](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetApplication.html)  **
  - **Description:** Grants permission to get information about an OpenSearch Application
  - **Resource types (\*required):** [application\*](#list_es-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCapability](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetCapability.html)  **
  - **Description:** Grants permission to get a registered capability for an OpenSearch Application
  - **Resource types (\*required):** [application\*](#list_es-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCompatibleElasticsearchVersions](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetCompatibleVersions.html)  **
  - **Description:** Grants permission to fetch a list of compatible OpenSearch and Elasticsearch versions to which an OpenSearch Service domain can be upgraded. This permission is deprecated. Use GetCompatibleVersions instead
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetCompatibleVersions](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetCompatibleVersions.html)  **
  - **Description:** Grants permission to fetch list of compatible engine versions to which an OpenSearch Service domain can be upgraded
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [GetDataSource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetDataSource.html)  **
  - **Description:** Grants permission to get the data source for the OpenSearch Service domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDefaultApplicationSetting](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetDefaultApplicationSetting.html)  **
  - **Description:** Grants permission to get the default application setting for OpenSearch Service
  - **Resource types (\*required):** [application\*](#list_es-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDirectQueryDataSource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetDirectQueryDataSource.html)  **
  - **Description:** Grants permission to get the data source for the provided OpenSearch arns
  - **Resource types (\*required):** [datasource\*](#list_es-resource-datasource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetDomainMaintenanceStatus](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetDomainMaintenanceStatus.html)  **
  - **Description:** Grants permission to retrieve the status of maintenance action for the node
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetIndex](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetIndex.html)  **
  - **Description:** Grants permission to get index for the OpenSearch Service domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetMigration](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetMigration.html)  **
  - **Description:** Grants permission to get the status and progress of a migration job for an OpenSearch Application
  - **Resource types (\*required):** [application\*](#list_es-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPackageVersionHistory](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetPackageVersionHistory.html)  **
  - **Description:** Grants permission to fetch the version history for a package
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetUpgradeHistory](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetUpgradeHistory.html)  **
  - **Description:** Grants permission to fetch the upgrade history of a given OpenSearch Service domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetUpgradeStatus](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetUpgradeStatus.html)  **
  - **Description:** Grants permission to fetch the upgrade status of a given OpenSearch Service domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [InsightFeedback](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_InsightFeedback.html)  **
  - **Description:** Grants permission to submit feedback for OpenSearch domain insight
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [ListApplications](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListApplications.html)  **
  - **Description:** Grants permission to list OpenSearch Applications
  - **Resource types (\*required):** [application\*](#list_es-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDataSourceAttachments](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListDataSourceAttachments.html)  **
  - **Description:** Grants permission to list data source attachments for an OpenSearch Application
  - **Resource types (\*required):** [application\*](#list_es-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDataSources](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListDataSources.html)  **
  - **Description:** Grants permission to retrieve a list of data source for the OpenSearch Service domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDirectQueryDataSources](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListDirectQueryDataSources.html)  **
  - **Description:** Grants permission to retrieve a list of data source for the provided OpenSearch arns
  - **Resource types (\*required):** [datasource\*](#list_es-resource-datasource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDomainMaintenances](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListDomainMaintenances.html)  **
  - **Description:** Grants permission to retrieve a list of maintenance actions for the OpenSearch Service domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListDomainNames](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListDomainNames.html)  **
  - **Description:** Grants permission to display the names of all OpenSearch Service domains that the current user owns
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDomainsForPackage](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListDomainsForPackage.html)  **
  - **Description:** Grants permission to list all OpenSearch Service domains that a package is associated with
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListElasticsearchInstanceTypeDetails](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListInstanceTypeDetails.html)  **
  - **Description:** Grants permission to list all instance types and available features for a given OpenSearch version. This permission is deprecated. Use ListInstanceTypeDetails instead
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListElasticsearchInstanceTypes](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListInstanceTypeDetails.html)  **
  - **Description:** Grants permission to list all EC2 instance types that are supported for a given OpenSearch version
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListElasticsearchVersions](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListVersions.html)  **
  - **Description:** Grants permission to list all supported OpenSearch versions on Amazon OpenSearch Service. This permission is deprecated. Use ListVersions instead
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListInsights](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListInsights.html)  **
  - **Description:** Grants permission to list insights for OpenSearch Service domains in the account
  - **Resource types (\*required):** [domain](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListInstanceTypeDetails](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListInstanceTypeDetails.html)  **
  - **Description:** Grants permission to list all instance types and available features for a given OpenSearch or Elasticsearch version
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListMigrations](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListMigrations.html)  **
  - **Description:** Grants permission to list migration jobs for an OpenSearch Application
  - **Resource types (\*required):** [application\*](#list_es-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListPackagesForDomain](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListPackagesForDomain.html)  **
  - **Description:** Grants permission to list all packages associated with the OpenSearch Service domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListScheduledActions](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListScheduledActions.html)  **
  - **Description:** Grants permission to retrieve a list of configuration changes that are scheduled for a OpenSearch Service domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListTags](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListTags.html)  **
  - **Description:** Grants permission to display all resource tags for an OpenSearch Service domain, data source, or application
  - **Resource types (\*required):** [application\*](#list_es-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [datasource\*](#list_es-resource-datasource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListVersions](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListVersions.html)  **
  - **Description:** Grants permission to list all supported OpenSearch and Elasticsearch versions in Amazon OpenSearch Service
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListVpcEndpointAccess](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListVpcEndpointAccess.html)  **
  - **Description:** Grants permission to retrieve information about each AWS principal that is allowed to access a given Amazon OpenSearch Service domain through the use of an interface VPC endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListVpcEndpoints](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListVpcEndpoints.html)  **
  - **Description:** Grants permission to retrieve all Amazon OpenSearch Service-managed VPC endpoints in the current AWS account and Region
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListVpcEndpointsForDomain](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_ListVpcEndpointsForDomain.html)  **
  - **Description:** Grants permission to retrieve all Amazon OpenSearch Service-managed VPC endpoints associated with a particular domain
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [PurchaseReservedElasticsearchInstanceOffering](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_PurchaseReservedInstanceOffering.html)  **
  - **Description:** Grants permission to purchase OpenSearch Service Reserved Instances. This permission is deprecated. Use PurchaseReservedInstanceOffering instead
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PurchaseReservedInstanceOffering](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_PurchaseReservedInstanceOffering.html)  **
  - **Description:** Grants permission to purchase OpenSearch reserved instances
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [PutDefaultApplicationSetting](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_PutDefaultApplicationSetting.html)  **
  - **Description:** Grants permission to set or remove the default application setting for OpenSearch Service
  - **Resource types (\*required):** [application\*](#list_es-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RegisterCapability](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_RegisterCapability.html)  **
  - **Description:** Grants permission to register a capability for an OpenSearch Application
  - **Resource types (\*required):** [application\*](#list_es-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RejectInboundConnection](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_RejectInboundConnection.html)  **
  - **Description:** Grants permission to the destination domain owner to reject an inbound cross-cluster search connection request
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RejectInboundCrossClusterSearchConnection](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_RejectInboundConnection.html)  **
  - **Description:** Grants permission to the destination domain owner to reject an inbound cross-cluster search connection request. This permission is deprecated. Use RejectInboundConnection instead
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RemoveTags](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_RemoveTags.html)  **
  - **Description:** Grants permission to remove resource tags from an OpenSearch Service domain, data source, or application
  - **Resource types (\*required):** [application\*](#list_es-resource-application) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_es-aws_TagKeys)
  - **Resource types (\*required):** [datasource\*](#list_es-resource-datasource) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_es-aws_TagKeys)
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_es-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [RevokeVpcEndpointAccess](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_RevokeVpcEndpointAccess.html)  **
  - **Description:** Grants permission to revoke access to an Amazon OpenSearch Service domain that was provided through an interface VPC endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [RollbackElasticsearchServiceSoftwareUpdate](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_RollbackServiceSoftwareUpdate.html)  **
  - **Description:** Grants permission to rollback a service software update of an elasticsearch domain to its previous version
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [RollbackServiceSoftwareUpdate](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_RollbackServiceSoftwareUpdate.html)  **
  - **Description:** Grants permission to rollback a service software update of an opensearch domain to its previous version
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartDomainMaintenance](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_StartDomainMaintenance.html)  **
  - **Description:** Grants permission to initiate the maintenance on the node
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartElasticsearchServiceSoftwareUpdate](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_StartServiceSoftwareUpdate.html)  **
  - **Description:** Grants permission to start a service software update of a domain. This permission is deprecated. Use StartServiceSoftwareUpdate instead
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartMigration](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_StartMigration.html)  **
  - **Description:** Grants permission to initiate a migration of saved objects to an OpenSearch Application
  - **Resource types (\*required):** [application\*](#list_es-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartServiceSoftwareUpdate](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_StartServiceSoftwareUpdate.html)  **
  - **Description:** Grants permission to start a service software update of a domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateApplication](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdateApplication.html)  **
  - **Description:** Grants permission to update an OpenSearch Application
  - **Resource types (\*required):** [application\*](#list_es-resource-application)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDataSource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdateDataSource.html)  **
  - **Description:** Grants permission to update the data source for the OpenSearch Service domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDirectQueryDataSource](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdateDirectQueryDataSource.html)  **
  - **Description:** Grants permission to update the data source for the provided OpenSearch arns
  - **Resource types (\*required):** [datasource\*](#list_es-resource-datasource)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateDomainConfig](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdateDomainConfig.html)  **
  - **Description:** Grants permission to modify the configuration of an OpenSearch Service domain, such as the instance type or number of instances
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateElasticsearchDomainConfig](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdateDomainConfig.html)  **
  - **Description:** Grants permission to modify the configuration of an OpenSearch Service domain, such as the instance type or number of instances. This permission is deprecated. Use UpdateDomainConfig instead
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateIndex](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdateIndex.html)  **
  - **Description:** Grants permission to update index for the OpenSearch Service domain
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePackage](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdatePackage.html)  **
  - **Description:** Grants permission to update a package for use with OpenSearch Service domains
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdatePackageScope](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdatePackageScope.html)  **
  - **Description:** Grants permission to update scope a package
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateScheduledAction](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdateScheduledAction.html)  **
  - **Description:** Grants permission to reschedule a planned OpenSearch Service domain configuration change for a later time
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateVpcEndpoint](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdateVpcEndpoint.html)  **
  - **Description:** Grants permission to modify an Amazon OpenSearch Service-managed interface VPC endpoint
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpgradeDomain](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpgradeDomain.html)  **
  - **Description:** Grants permission to initiate upgrade of an OpenSearch Service domain to a given version
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpgradeElasticsearchDomain](https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpgradeDomain.html)  **
  - **Description:** Grants permission to initiate upgrade of an OpenSearch Service domain to a specified version. This permission is deprecated. Use UpgradeDomain instead
  - **Resource types (\*required):** [domain\*](#list_es-resource-domain)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by Amazon OpenSearch Service
<a name="list_es-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [application](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html)  | arn:${Partition}:opensearch:${Region}:${Account}:application/${AppId} | [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_) | 
|  [datasource](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/datasource.html)  | arn:${Partition}:opensearch:${Region}:${Account}:datasource/${DataSourceName} | [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_) | 
|  [domain](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/ac.html)  | arn:${Partition}:es:${Region}:${Account}:domain/${DomainName} | [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_) | 
|  [es\_role](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/slr.html)  | arn:${Partition}:iam::${Account}:role/aws-service-role/es.amazonaws.com/AWSServiceRoleForAmazonOpenSearchService | [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_) | 
|  [opensearchservice\_role](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/slr.html)  | arn:${Partition}:iam::${Account}:role/aws-service-role/opensearchservice.amazonaws.com/AWSServiceRoleForAmazonOpenSearchService | [aws:ResourceTag/${TagKey}](#list_es-aws_ResourceTag___TagKey_) | 

## Condition keys for Amazon OpenSearch Service
<a name="list_es-policy-keys"></a>

Amazon OpenSearch Service defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access based on the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters access based on the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access based on the tag keys that are passed in the request | ArrayOfString | 