

# Actions, resources, and condition keys for AWS Outposts
<a name="list_outposts"></a>

AWS Outposts (service prefix: `outposts`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/outposts/latest/userguide/get-started-outposts.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/outposts/latest/APIReference/).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/outposts/latest/userguide/identity-access-management.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/outposts/outposts.json) for this service.

**Topics**
+ [API operations defined by AWS Outposts](#list_outposts-operations)
+ [Actions defined by AWS Outposts](#list_outposts-actions-as-permissions)
+ [Resource types defined by AWS Outposts](#list_outposts-resources-for-iam-policies)
+ [Condition keys for AWS Outposts](#list_outposts-policy-keys)

## API operations defined by AWS Outposts
<a name="list_outposts-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_outposts-actions-as-permissions).




- **   CancelCapacityTask  **
  - **IAM action:**  [outposts:CancelCapacityTask](#list_outposts-action-CancelCapacityTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CancelOrder  **
  - **IAM action:**  [outposts:CancelOrder](#list_outposts-action-CancelOrder) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateOrder  **
  - **IAM action:**  [outposts:CreateOrder](#list_outposts-action-CreateOrder) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateOutpost  **
  - **IAM action:**  [outposts:CreateOutpost](#list_outposts-action-CreateOutpost)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [outposts:TagResource](#list_outposts-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePrivateConnectivityConfig  **
  - **IAM action:**  [outposts:CreatePrivateConnectivityConfig](#list_outposts-action-CreatePrivateConnectivityConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateQuote  **
  - **IAM action:**  [outposts:CreateQuote](#list_outposts-action-CreateQuote) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateRenewal  **
  - **IAM action:**  [outposts:CreateRenewal](#list_outposts-action-CreateRenewal) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateSite  **
  - **IAM action:**  [outposts:CreateSite](#list_outposts-action-CreateSite)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [outposts:TagResource](#list_outposts-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteOutpost  **
  - **IAM action:**  [outposts:DeleteOutpost](#list_outposts-action-DeleteOutpost) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteQuote  **
  - **IAM action:**  [outposts:DeleteQuote](#list_outposts-action-DeleteQuote) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteSite  **
  - **IAM action:**  [outposts:DeleteSite](#list_outposts-action-DeleteSite) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetCapacityTask  **
  - **IAM action:**  [outposts:GetCapacityTask](#list_outposts-action-GetCapacityTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetCatalogItem  **
  - **IAM action:**  [outposts:GetCatalogItem](#list_outposts-action-GetCatalogItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetConnection  **
  - **IAM action:**  [outposts:GetConnection](#list_outposts-action-GetConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOrder  **
  - **IAM action:**  [outposts:GetOrder](#list_outposts-action-GetOrder) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOutpost  **
  - **IAM action:**  [outposts:GetOutpost](#list_outposts-action-GetOutpost) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOutpostBillingInformation  **
  - **IAM action:**  [outposts:GetOutpostBillingInformation](#list_outposts-action-GetOutpostBillingInformation) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOutpostInstanceTypes  **
  - **IAM action:**  [outposts:GetOutpostInstanceTypes](#list_outposts-action-GetOutpostInstanceTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOutpostSupportedInstanceTypes  **
  - **IAM action:**  [outposts:GetOutpostSupportedInstanceTypes](#list_outposts-action-GetOutpostSupportedInstanceTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPrivateConnectivityConfig  **
  - **IAM action:**  [outposts:GetPrivateConnectivityConfig](#list_outposts-action-GetPrivateConnectivityConfig) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetQuote  **
  - **IAM action:**  [outposts:GetQuote](#list_outposts-action-GetQuote) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetRenewalPricing  **
  - **IAM action:**  [outposts:GetRenewalPricing](#list_outposts-action-GetRenewalPricing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSite  **
  - **IAM action:**  [outposts:GetSite](#list_outposts-action-GetSite) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetSiteAddress  **
  - **IAM action:**  [outposts:GetSiteAddress](#list_outposts-action-GetSiteAddress) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListAssetInstances  **
  - **IAM action:**  [outposts:ListAssetInstances](#list_outposts-action-ListAssetInstances) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListAssets  **
  - **IAM action:**  [outposts:ListAssets](#list_outposts-action-ListAssets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListBlockingInstancesForCapacityTask  **
  - **IAM action:**  [outposts:ListBlockingInstancesForCapacityTask](#list_outposts-action-ListBlockingInstancesForCapacityTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCapacityTasks  **
  - **IAM action:**  [outposts:ListCapacityTasks](#list_outposts-action-ListCapacityTasks) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListCatalogItems  **
  - **IAM action:**  [outposts:ListCatalogItems](#list_outposts-action-ListCatalogItems) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOrderableInstanceTypes  **
  - **IAM action:**  [outposts:ListOrderableInstanceTypes](#list_outposts-action-ListOrderableInstanceTypes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOrders  **
  - **IAM action:**  [outposts:ListOrders](#list_outposts-action-ListOrders) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListOutposts  **
  - **IAM action:**  [outposts:ListOutposts](#list_outposts-action-ListOutposts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListQuotes  **
  - **IAM action:**  [outposts:ListQuotes](#list_outposts-action-ListQuotes) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListSites  **
  - **IAM action:**  [outposts:ListSites](#list_outposts-action-ListSites) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [outposts:ListTagsForResource](#list_outposts-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   StartCapacityTask  **
  - **IAM action:**  [outposts:StartCapacityTask](#list_outposts-action-StartCapacityTask) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StartConnection  **
  - **IAM action:**  [outposts:StartConnection](#list_outposts-action-StartConnection) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [outposts:TagResource](#list_outposts-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [outposts:UntagResource](#list_outposts-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdateOutpost  **
  - **IAM action:**  [outposts:UpdateOutpost](#list_outposts-action-UpdateOutpost) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateQuote  **
  - **IAM action:**  [outposts:UpdateQuote](#list_outposts-action-UpdateQuote) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSite  **
  - **IAM action:**  [outposts:UpdateSite](#list_outposts-action-UpdateSite) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSiteAddress  **
  - **IAM action:**  [outposts:UpdateSiteAddress](#list_outposts-action-UpdateSiteAddress) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateSiteRackPhysicalProperties  **
  - **IAM action:**  [outposts:UpdateSiteRackPhysicalProperties](#list_outposts-action-UpdateSiteRackPhysicalProperties) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS Outposts
<a name="list_outposts-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [CancelCapacityTask](https://docs.aws.amazon.com/outposts/latest/APIReference/API_CancelCapacityTask.html)  **
  - **Description:** Grants permission to cancel a capacity task
  - **Resource types (\*required):** [outpost\*](#list_outposts-resource-outpost)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CancelOrder](https://docs.aws.amazon.com/outposts/latest/APIReference/API_CancelOrder.html)  **
  - **Description:** Grants permission to cancel an order
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateOrder](https://docs.aws.amazon.com/outposts/latest/APIReference/API_CreateOrder.html)  **
  - **Description:** Grants permission to create an order
  - **Resource types (\*required):** [outpost\*](#list_outposts-resource-outpost)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateOutpost](https://docs.aws.amazon.com/outposts/latest/APIReference/API_CreateOutpost.html)  **
  - **Description:** Grants permission to create an Outpost
  - **Resource types (\*required):** [site\*](#list_outposts-resource-site)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_outposts-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_outposts-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePrivateConnectivityConfig](https://docs.aws.amazon.com/outposts/latest/userguide/how-outposts-works.html#private-connectivity)  **
  - **Description:** Grants permission to create a private connectivity configuration
  - **Resource types (\*required):** [outpost\*](#list_outposts-resource-outpost)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateQuote](https://docs.aws.amazon.com/outposts/latest/APIReference/API_CreateQuote.html)  **
  - **Description:** Grants permission to create a quote
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [CreateRenewal](https://docs.aws.amazon.com/outposts/latest/APIReference/API_CreateRenewal.html)  **
  - **Description:** Grants permission to create a renewal for the specified Outpost
  - **Resource types (\*required):** [outpost\*](#list_outposts-resource-outpost)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateSite](https://docs.aws.amazon.com/outposts/latest/APIReference/API_CreateSite.html)  **
  - **Description:** Grants permission to create a site
  - **Resource types (\*required):** 
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_outposts-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_outposts-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteOutpost](https://docs.aws.amazon.com/outposts/latest/APIReference/API_DeleteOutpost.html)  **
  - **Description:** Grants permission to delete an Outpost
  - **Resource types (\*required):** [outpost\*](#list_outposts-resource-outpost)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteQuote](https://docs.aws.amazon.com/outposts/latest/APIReference/API_DeleteQuote.html)  **
  - **Description:** Grants permission to delete a quote
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [DeleteSite](https://docs.aws.amazon.com/outposts/latest/APIReference/API_DeleteSite.html)  **
  - **Description:** Grants permission to delete a site
  - **Resource types (\*required):** [site\*](#list_outposts-resource-site)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetCapacityTask](https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetCapacityTask.html)  **
  - **Description:** Grants permission to get information about the specified capacity task
  - **Resource types (\*required):** [outpost\*](#list_outposts-resource-outpost)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetCatalogItem](https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetCatalogItem.html)  **
  - **Description:** Grants permission to get a catalog item
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetConnection](https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetConnection.html)  **
  - **Description:** Grants permission to get information about the connection for your Outpost server
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetOrder](https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetOrder.html)  **
  - **Description:** Grants permission to get information about an order
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetOutpost](https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetOutpost.html)  **
  - **Description:** Grants permission to get information about the specified Outpost
  - **Resource types (\*required):** [outpost\*](#list_outposts-resource-outpost)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOutpostBillingInformation](https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetOutpostBillingInformation.html)  **
  - **Description:** Grants permission to get Outpost billing information for the specified Outpost
  - **Resource types (\*required):** [outpost\*](#list_outposts-resource-outpost)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOutpostInstanceTypes](https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetOutpostInstanceTypes.html)  **
  - **Description:** Grants permission to get the instance types for the specified Outpost
  - **Resource types (\*required):** [outpost\*](#list_outposts-resource-outpost)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOutpostSupportedInstanceTypes](https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetOutpostSupportedInstanceTypes.html)  **
  - **Description:** Grants permission to get the supported instance types for the specified Outpost
  - **Resource types (\*required):** [outpost\*](#list_outposts-resource-outpost)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPrivateConnectivityConfig](https://docs.aws.amazon.com/outposts/latest/userguide/how-outposts-works.html#private-connectivity)  **
  - **Description:** Grants permission to get a private connectivity configuration
  - **Resource types (\*required):** [outpost\*](#list_outposts-resource-outpost)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetQuote](https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetQuote.html)  **
  - **Description:** Grants permission to get information about a quote
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetRenewalPricing](https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetRenewalPricing.html)  **
  - **Description:** Grants permission to get renewal pricing for the specified Outpost
  - **Resource types (\*required):** [outpost\*](#list_outposts-resource-outpost)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSite](https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetSite.html)  **
  - **Description:** Grants permission to get a site
  - **Resource types (\*required):** [site\*](#list_outposts-resource-site)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetSiteAddress](https://docs.aws.amazon.com/outposts/latest/APIReference/API_GetSiteAddress.html)  **
  - **Description:** Grants permission to get a site address
  - **Resource types (\*required):** [site\*](#list_outposts-resource-site)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListAssetInstances](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListAssetInstances.html)  **
  - **Description:** Grants permission to list all running instances for the specified Outpost
  - **Resource types (\*required):** [outpost\*](#list_outposts-resource-outpost)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListAssets](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListAssets.html)  **
  - **Description:** Grants permission to list the assets for your Outpost
  - **Resource types (\*required):** [outpost\*](#list_outposts-resource-outpost)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListBlockingInstancesForCapacityTask](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListBlockingInstancesForCapacityTask.html)  **
  - **Description:** Grants permission to list all running instances that are blocking the capacity task from running for the specified Outpost
  - **Resource types (\*required):** [outpost\*](#list_outposts-resource-outpost)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListCapacityTasks](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListCapacityTasks.html)  **
  - **Description:** Grants permission to list the capacity tasks for your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListCatalogItems](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListCatalogItems.html)  **
  - **Description:** Grants permission to list all catalog items
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOrderableInstanceTypes](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListOrderableInstanceTypes.html)  **
  - **Description:** Grants permission to list the orderable instance types for your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOrders](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListOrders.html)  **
  - **Description:** Grants permission to list the orders for your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListOutposts](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListOutposts.html)  **
  - **Description:** Grants permission to list the Outposts for your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListQuotes](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListQuotes.html)  **
  - **Description:** Grants permission to list quotes for your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListSites](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListSites.html)  **
  - **Description:** Grants permission to list the sites for your AWS account
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/outposts/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list tags for a resource
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [StartCapacityTask](https://docs.aws.amazon.com/outposts/latest/APIReference/API_StartCapacityTask.html)  **
  - **Description:** Grants permission to create a capacity task
  - **Resource types (\*required):** [outpost\*](#list_outposts-resource-outpost)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StartConnection](https://docs.aws.amazon.com/outposts/latest/APIReference/API_StartConnection.html)  **
  - **Description:** Grants permission to start a connection for your Outpost server
  - **Resource types (\*required):** [outpost\*](#list_outposts-resource-outpost)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/outposts/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to tag a resource
  - **Resource types (\*required):** [outpost](#list_outposts-resource-outpost) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_outposts-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_outposts-aws_TagKeys)
  - **Resource types (\*required):** [site](#list_outposts-resource-site) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_outposts-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_outposts-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/outposts/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to untag a resource
  - **Resource types (\*required):** [outpost](#list_outposts-resource-outpost) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_outposts-aws_TagKeys)
  - **Resource types (\*required):** [site](#list_outposts-resource-site) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_outposts-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdateOutpost](https://docs.aws.amazon.com/outposts/latest/APIReference/API_UpdateOutpost.html)  **
  - **Description:** Grants permission to update an Outpost
  - **Resource types (\*required):** [outpost\*](#list_outposts-resource-outpost)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateQuote](https://docs.aws.amazon.com/outposts/latest/APIReference/API_UpdateQuote.html)  **
  - **Description:** Grants permission to update a quote
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Write

- **   [UpdateSite](https://docs.aws.amazon.com/outposts/latest/APIReference/API_UpdateSite.html)  **
  - **Description:** Grants permission to update a site
  - **Resource types (\*required):** [site\*](#list_outposts-resource-site)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSiteAddress](https://docs.aws.amazon.com/outposts/latest/APIReference/API_UpdateSiteAddress.html)  **
  - **Description:** Grants permission to update the site address
  - **Resource types (\*required):** [site\*](#list_outposts-resource-site)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateSiteRackPhysicalProperties](https://docs.aws.amazon.com/outposts/latest/APIReference/API_UpdateSiteRackPhysicalProperties.html)  **
  - **Description:** Grants permission to update the physical properties of a rack at a site
  - **Resource types (\*required):** [site\*](#list_outposts-resource-site)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS Outposts
<a name="list_outposts-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [outpost](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html)  | arn:${Partition}:outposts:${Region}:${Account}:outpost/${OutpostId} | [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_) | 
|  [site](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html)  | arn:${Partition}:outposts:${Region}:${Account}:site/${SiteId} | [aws:ResourceTag/${TagKey}](#list_outposts-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS Outposts
<a name="list_outposts-policy-keys"></a>

AWS Outposts defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/outposts/latest/userguide/identity-access-management.html)  | Filters access by the tags that are passed in the request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/outposts/latest/userguide/identity-access-management.html)  | Filters access by the tags associated with the resource | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/outposts/latest/userguide/identity-access-management.html)  | Filters access by the tag keys that are passed in the request | ArrayOfString | 