

# Actions, resources, and condition keys for AWS API Portal

AWS API Portal (service prefix: `apiportal`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/apigateway/latest/developerguide/apiportal.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/apiportal/latest/APIReference/Welcome.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/apiportal/latest/userguide/security-iam.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/apiportal/apiportal.json) for this service.

**Topics**
+ [API operations defined by AWS API Portal](#list_apiportal-operations)
+ [Actions defined by AWS API Portal](#list_apiportal-actions-as-permissions)
+ [Resource types defined by AWS API Portal](#list_apiportal-resources-for-iam-policies)
+ [Condition keys for AWS API Portal](#list_apiportal-policy-keys)

## API operations defined by AWS API Portal
<a name="list_apiportal-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_apiportal-actions-as-permissions).




- **   AssociateManagedApis  **
  - **IAM action:**  [apiportal:AssociateManagedApis](#list_apiportal-action-AssociateManagedApis) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateManagedApi  **
  - **IAM action:**  [apiportal:CreateManagedApi](#list_apiportal-action-CreateManagedApi)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apiportal:TagResource](#list_apiportal-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePortal  **
  - **IAM action:**  [apiportal:CreatePortal](#list_apiportal-action-CreatePortal)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apiportal:GetProduct](#list_apiportal-action-GetProduct)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [apiportal:TagResource](#list_apiportal-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreatePortalPreview  **
  - **IAM action:**  [apiportal:CreatePortalPreview](#list_apiportal-action-CreatePortalPreview) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   CreateProduct  **
  - **IAM action:**  [apiportal:CreateProduct](#list_apiportal-action-CreateProduct)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apiportal:TagResource](#list_apiportal-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateProductApiPage  **
  - **IAM action:**  [apiportal:CreateProductApiPage](#list_apiportal-action-CreateProductApiPage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apiportal:TagResource](#list_apiportal-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   CreateProductPage  **
  - **IAM action:**  [apiportal:CreateProductPage](#list_apiportal-action-CreateProductPage)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apiportal:TagResource](#list_apiportal-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   DeleteDiscoveryConfiguration  **
  - **IAM action:**  [apiportal:DeleteDiscoveryConfiguration](#list_apiportal-action-DeleteDiscoveryConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteManagedApi  **
  - **IAM action:**  [apiportal:DeleteManagedApi](#list_apiportal-action-DeleteManagedApi) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteOrganizationDiscoveryConfiguration  **
  - **IAM action:**  [apiportal:DeleteOrganizationDiscoveryConfiguration](#list_apiportal-action-DeleteOrganizationDiscoveryConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeletePortal  **
  - **IAM action:**  [apiportal:DeletePortal](#list_apiportal-action-DeletePortal) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProduct  **
  - **IAM action:**  [apiportal:DeleteProduct](#list_apiportal-action-DeleteProduct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProductApiPage  **
  - **IAM action:**  [apiportal:DeleteProductApiPage](#list_apiportal-action-DeleteProductApiPage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProductPage  **
  - **IAM action:**  [apiportal:DeleteProductPage](#list_apiportal-action-DeleteProductPage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   DeleteProductSharingPolicy  **
  - **IAM action:**  [apiportal:DeleteProductSharingPolicy](#list_apiportal-action-DeleteProductSharingPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Permissions management, Write

- **   DisassociateManagedApis  **
  - **IAM action:**  [apiportal:DisassociateManagedApis](#list_apiportal-action-DisassociateManagedApis) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   GetApiInventoryItem  **
  - **IAM action:**  [apiportal:GetApiInventoryItem](#list_apiportal-action-GetApiInventoryItem) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetDiscoveryConfiguration  **
  - **IAM action:**  [apiportal:GetDiscoveryConfiguration](#list_apiportal-action-GetDiscoveryConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetManagedApi  **
  - **IAM action:**  [apiportal:GetManagedApi](#list_apiportal-action-GetManagedApi) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOrganizationDiscoveryConfiguration  **
  - **IAM action:**  [apiportal:GetOrganizationDiscoveryConfiguration](#list_apiportal-action-GetOrganizationDiscoveryConfiguration) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetPortal  **
  - **IAM action:**  [apiportal:GetPortal](#list_apiportal-action-GetPortal) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProduct  **
  - **IAM action:**  [apiportal:GetProduct](#list_apiportal-action-GetProduct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProductApiPage  **
  - **IAM action:**  [apiportal:GetProductApiPage](#list_apiportal-action-GetProductApiPage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProductPage  **
  - **IAM action:**  [apiportal:GetProductPage](#list_apiportal-action-GetProductPage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProductSharingPolicy  **
  - **IAM action:**  [apiportal:GetProductSharingPolicy](#list_apiportal-action-GetProductSharingPolicy) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListApiInventoryItems  **
  - **IAM action:**  [apiportal:ListApiInventoryItems](#list_apiportal-action-ListApiInventoryItems) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListDiscoveryStatuses  **
  - **IAM action:**  [apiportal:ListDiscoveryStatuses](#list_apiportal-action-ListDiscoveryStatuses) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListManagedApiEvents  **
  - **IAM action:**  [apiportal:ListManagedApiEvents](#list_apiportal-action-ListManagedApiEvents) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListManagedApis  **
  - **IAM action:**  [apiportal:ListManagedApis](#list_apiportal-action-ListManagedApis) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPortals  **
  - **IAM action:**  [apiportal:ListPortals](#list_apiportal-action-ListPortals) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProductApiPages  **
  - **IAM action:**  [apiportal:ListProductApiPages](#list_apiportal-action-ListProductApiPages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProductPages  **
  - **IAM action:**  [apiportal:ListProductPages](#list_apiportal-action-ListProductPages) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListProducts  **
  - **IAM action:**  [apiportal:ListProducts](#list_apiportal-action-ListProducts) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListTagsForResource  **
  - **IAM action:**  [apiportal:ListTagsForResource](#list_apiportal-action-ListTagsForResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   PutDiscoveryConfiguration  **
  - **IAM action:**  [apiportal:PutDiscoveryConfiguration](#list_apiportal-action-PutDiscoveryConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apiportal:TagResource](#list_apiportal-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutOrganizationDiscoveryConfiguration  **
  - **IAM action:**  [apiportal:PutOrganizationDiscoveryConfiguration](#list_apiportal-action-PutOrganizationDiscoveryConfiguration)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write
  - **IAM action:**  [apiportal:TagResource](#list_apiportal-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   PutProductSharingPolicy  **
  - **IAM action:**  [apiportal:PutProductSharingPolicy](#list_apiportal-action-PutProductSharingPolicy)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Permissions management, Write
  - **IAM action:**  [apiportal:TagResource](#list_apiportal-action-TagResource)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Tagging, Write

- **   StartDiscovery  **
  - **IAM action:**  [apiportal:StartDiscovery](#list_apiportal-action-StartDiscovery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   StopDiscovery  **
  - **IAM action:**  [apiportal:StopDiscovery](#list_apiportal-action-StopDiscovery) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   TagResource  **
  - **IAM action:**  [apiportal:TagResource](#list_apiportal-action-TagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UntagResource  **
  - **IAM action:**  [apiportal:UntagResource](#list_apiportal-action-UntagResource) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Tagging, Write

- **   UpdatePortal  **
  - **IAM action:**  [apiportal:GetProduct](#list_apiportal-action-GetProduct)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [apiportal:UpdatePortal](#list_apiportal-action-UpdatePortal)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdatePortalPublishStatus  **
  - **IAM action:**  [apiportal:GetProduct](#list_apiportal-action-GetProduct)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Read
  - **IAM action:**  [apiportal:UpdatePortalPublishStatus](#list_apiportal-action-UpdatePortalPublishStatus)  / **Condition key:**  / **Possible value(s):**  / **Access level:** Write

- **   UpdateProduct  **
  - **IAM action:**  [apiportal:UpdateProduct](#list_apiportal-action-UpdateProduct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProductApiPage  **
  - **IAM action:**  [apiportal:UpdateProductApiPage](#list_apiportal-action-UpdateProductApiPage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write

- **   UpdateProductPage  **
  - **IAM action:**  [apiportal:UpdateProductPage](#list_apiportal-action-UpdateProductPage) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Write



## Actions defined by AWS API Portal
<a name="list_apiportal-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. For each action, the table lists the resource types and condition keys supported by that action. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [AssociateManagedApis](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_AssociateManagedApis.html)  **
  - **Description:** Grants permission to associate managed APIs with a product
  - **Resource types (\*required):** [Product\*](#list_apiportal-resource-Product)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateManagedApi](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_CreateManagedApi.html)  **
  - **Description:** Grants permission to create a managed API from a discovered API
  - **Resource types (\*required):** [ManagedApi\*](#list_apiportal-resource-ManagedApi)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_apiportal-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apiportal-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePortal](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_CreatePortal.html)  **
  - **Description:** Grants permission to create a portal
  - **Resource types (\*required):** [Portal\*](#list_apiportal-resource-Portal)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_apiportal-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apiportal-aws_TagKeys)
  - **Access level:** Write

- **   [CreatePortalPreview](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_CreatePortalPreview.html)  **
  - **Description:** Grants permission to create a preview of a portal
  - **Resource types (\*required):** [Portal\*](#list_apiportal-resource-Portal)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [CreateProduct](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_CreateProduct.html)  **
  - **Description:** Grants permission to create a product
  - **Resource types (\*required):** [Product\*](#list_apiportal-resource-Product)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_apiportal-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apiportal-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProductApiPage](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_CreateProductApiPage.html)  **
  - **Description:** Grants permission to create an API reference page in a product
  - **Resource types (\*required):** [ProductApiPage\*](#list_apiportal-resource-ProductApiPage)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_apiportal-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apiportal-aws_TagKeys)
  - **Access level:** Write

- **   [CreateProductPage](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_CreateProductPage.html)  **
  - **Description:** Grants permission to create a documentation page in a product
  - **Resource types (\*required):** [ProductPage\*](#list_apiportal-resource-ProductPage)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_apiportal-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apiportal-aws_TagKeys)
  - **Access level:** Write

- **   [DeleteDiscoveryConfiguration](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_DeleteDiscoveryConfiguration.html)  **
  - **Description:** Grants permission to delete the API discovery configuration for an account
  - **Resource types (\*required):** [DiscoveryConfiguration\*](#list_apiportal-resource-DiscoveryConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteManagedApi](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_DeleteManagedApi.html)  **
  - **Description:** Grants permission to delete a managed API
  - **Resource types (\*required):** [ManagedApi\*](#list_apiportal-resource-ManagedApi)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteOrganizationDiscoveryConfiguration](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_DeleteOrganizationDiscoveryConfiguration.html)  **
  - **Description:** Grants permission to delete the API discovery configuration for an organization
  - **Resource types (\*required):** [OrganizationDiscoveryConfiguration\*](#list_apiportal-resource-OrganizationDiscoveryConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeletePortal](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_DeletePortal.html)  **
  - **Description:** Grants permission to delete a portal
  - **Resource types (\*required):** [Portal\*](#list_apiportal-resource-Portal)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProduct](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_DeleteProduct.html)  **
  - **Description:** Grants permission to delete a product
  - **Resource types (\*required):** [Product\*](#list_apiportal-resource-Product)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProductApiPage](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_DeleteProductApiPage.html)  **
  - **Description:** Grants permission to delete an API reference page from a product
  - **Resource types (\*required):** [ProductApiPage\*](#list_apiportal-resource-ProductApiPage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProductPage](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_DeleteProductPage.html)  **
  - **Description:** Grants permission to delete a documentation page from a product
  - **Resource types (\*required):** [ProductPage\*](#list_apiportal-resource-ProductPage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [DeleteProductSharingPolicy](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_DeleteProductSharingPolicy.html)  **
  - **Description:** Grants permission to delete the sharing policy of a product
  - **Resource types (\*required):** [ProductSharingPolicy\*](#list_apiportal-resource-ProductSharingPolicy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Permissions management, Write

- **   [DisassociateManagedApis](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_DisassociateManagedApis.html)  **
  - **Description:** Grants permission to disassociate managed APIs from a product
  - **Resource types (\*required):** [Product\*](#list_apiportal-resource-Product)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [GetApiInventoryItem](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_GetApiInventoryItem.html)  **
  - **Description:** Grants permission to retrieve details of a discovered API in the API inventory
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetDiscoveryConfiguration](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_GetDiscoveryConfiguration.html)  **
  - **Description:** Grants permission to retrieve the API discovery configuration for an account
  - **Resource types (\*required):** [DiscoveryConfiguration\*](#list_apiportal-resource-DiscoveryConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetManagedApi](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_GetManagedApi.html)  **
  - **Description:** Grants permission to retrieve a managed API
  - **Resource types (\*required):** [ManagedApi\*](#list_apiportal-resource-ManagedApi)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetOrganizationDiscoveryConfiguration](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_GetOrganizationDiscoveryConfiguration.html)  **
  - **Description:** Grants permission to retrieve the API discovery configuration for an organization
  - **Resource types (\*required):** [OrganizationDiscoveryConfiguration\*](#list_apiportal-resource-OrganizationDiscoveryConfiguration)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetPortal](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_GetPortal.html)  **
  - **Description:** Grants permission to retrieve a portal
  - **Resource types (\*required):** [Portal\*](#list_apiportal-resource-Portal)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProduct](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_GetProduct.html)  **
  - **Description:** Grants permission to retrieve a product
  - **Resource types (\*required):** [Product\*](#list_apiportal-resource-Product)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProductApiPage](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_GetProductApiPage.html)  **
  - **Description:** Grants permission to retrieve an API reference page in a product
  - **Resource types (\*required):** [ProductApiPage\*](#list_apiportal-resource-ProductApiPage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProductPage](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_GetProductPage.html)  **
  - **Description:** Grants permission to retrieve a documentation page in a product
  - **Resource types (\*required):** [ProductPage\*](#list_apiportal-resource-ProductPage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [GetProductSharingPolicy](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_GetProductSharingPolicy.html)  **
  - **Description:** Grants permission to retrieve the sharing policy of a product
  - **Resource types (\*required):** [ProductSharingPolicy\*](#list_apiportal-resource-ProductSharingPolicy)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [ListApiInventoryItems](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_ListApiInventoryItems.html)  **
  - **Description:** Grants permission to list discovered APIs in the API inventory
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListDiscoveryStatuses](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_ListDiscoveryStatuses.html)  **
  - **Description:** Grants permission to list API discovery statuses
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListManagedApiEvents](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_ListManagedApiEvents.html)  **
  - **Description:** Grants permission to list API security events for a managed API
  - **Resource types (\*required):** [ManagedApi\*](#list_apiportal-resource-ManagedApi)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListManagedApis](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_ListManagedApis.html)  **
  - **Description:** Grants permission to list managed APIs
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPortals](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_ListPortals.html)  **
  - **Description:** Grants permission to list portals
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListProductApiPages](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_ListProductApiPages.html)  **
  - **Description:** Grants permission to list the API reference pages in a product
  - **Resource types (\*required):** [Product\*](#list_apiportal-resource-Product)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProductPages](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_ListProductPages.html)  **
  - **Description:** Grants permission to list the documentation pages in a product
  - **Resource types (\*required):** [Product\*](#list_apiportal-resource-Product)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** List

- **   [ListProducts](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_ListProducts.html)  **
  - **Description:** Grants permission to list products
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListTagsForResource](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_ListTagsForResource.html)  **
  - **Description:** Grants permission to list the tags for an API Portal resource
  - **Resource types (\*required):** [DiscoveryConfiguration](#list_apiportal-resource-DiscoveryConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ManagedApi](#list_apiportal-resource-ManagedApi) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [OrganizationDiscoveryConfiguration](#list_apiportal-resource-OrganizationDiscoveryConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Portal](#list_apiportal-resource-Portal) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [Product](#list_apiportal-resource-Product) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ProductApiPage](#list_apiportal-resource-ProductApiPage) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ProductPage](#list_apiportal-resource-ProductPage) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [ProductSharingPolicy](#list_apiportal-resource-ProductSharingPolicy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Read

- **   [PutDiscoveryConfiguration](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_PutDiscoveryConfiguration.html)  **
  - **Description:** Grants permission to create or update the API discovery configuration for an account
  - **Resource types (\*required):** [DiscoveryConfiguration\*](#list_apiportal-resource-DiscoveryConfiguration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_apiportal-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apiportal-aws_TagKeys)
  - **Access level:** Write

- **   [PutOrganizationDiscoveryConfiguration](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_PutOrganizationDiscoveryConfiguration.html)  **
  - **Description:** Grants permission to create or update the API discovery configuration for an organization
  - **Resource types (\*required):** [OrganizationDiscoveryConfiguration\*](#list_apiportal-resource-OrganizationDiscoveryConfiguration)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_apiportal-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apiportal-aws_TagKeys)
  - **Access level:** Write

- **   [PutProductSharingPolicy](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_PutProductSharingPolicy.html)  **
  - **Description:** Grants permission to create or update the sharing policy of a product
  - **Resource types (\*required):** [ProductSharingPolicy\*](#list_apiportal-resource-ProductSharingPolicy)
  - **Condition keys:** [aws:RequestTag/${TagKey}](#list_apiportal-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apiportal-aws_TagKeys)
  - **Access level:** Permissions management, Write

- **   [StartDiscovery](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_StartDiscovery.html)  **
  - **Description:** Grants permission to start API discovery for a discovery configuration
  - **Resource types (\*required):** [DiscoveryConfiguration\*](#list_apiportal-resource-DiscoveryConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [OrganizationDiscoveryConfiguration\*](#list_apiportal-resource-OrganizationDiscoveryConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [StopDiscovery](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_StopDiscovery.html)  **
  - **Description:** Grants permission to stop API discovery for a discovery configuration
  - **Resource types (\*required):** [DiscoveryConfiguration\*](#list_apiportal-resource-DiscoveryConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Resource types (\*required):** [OrganizationDiscoveryConfiguration\*](#list_apiportal-resource-OrganizationDiscoveryConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [TagResource](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_TagResource.html)  **
  - **Description:** Grants permission to add tags to an API Portal resource
  - **Resource types (\*required):** [DiscoveryConfiguration](#list_apiportal-resource-DiscoveryConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apiportal-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apiportal-aws_TagKeys)
  - **Resource types (\*required):** [ManagedApi](#list_apiportal-resource-ManagedApi) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apiportal-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apiportal-aws_TagKeys)
  - **Resource types (\*required):** [OrganizationDiscoveryConfiguration](#list_apiportal-resource-OrganizationDiscoveryConfiguration) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apiportal-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apiportal-aws_TagKeys)
  - **Resource types (\*required):** [Portal](#list_apiportal-resource-Portal) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apiportal-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apiportal-aws_TagKeys)
  - **Resource types (\*required):** [Product](#list_apiportal-resource-Product) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apiportal-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apiportal-aws_TagKeys)
  - **Resource types (\*required):** [ProductApiPage](#list_apiportal-resource-ProductApiPage) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apiportal-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apiportal-aws_TagKeys)
  - **Resource types (\*required):** [ProductPage](#list_apiportal-resource-ProductPage) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apiportal-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apiportal-aws_TagKeys)
  - **Resource types (\*required):** [ProductSharingPolicy](#list_apiportal-resource-ProductSharingPolicy) / **Condition keys:** [aws:RequestTag/${TagKey}](#list_apiportal-aws_RequestTag___TagKey_)<br />[aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apiportal-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UntagResource](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_UntagResource.html)  **
  - **Description:** Grants permission to remove tags from an API Portal resource
  - **Resource types (\*required):** [DiscoveryConfiguration](#list_apiportal-resource-DiscoveryConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apiportal-aws_TagKeys)
  - **Resource types (\*required):** [ManagedApi](#list_apiportal-resource-ManagedApi) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apiportal-aws_TagKeys)
  - **Resource types (\*required):** [OrganizationDiscoveryConfiguration](#list_apiportal-resource-OrganizationDiscoveryConfiguration) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apiportal-aws_TagKeys)
  - **Resource types (\*required):** [Portal](#list_apiportal-resource-Portal) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apiportal-aws_TagKeys)
  - **Resource types (\*required):** [Product](#list_apiportal-resource-Product) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apiportal-aws_TagKeys)
  - **Resource types (\*required):** [ProductApiPage](#list_apiportal-resource-ProductApiPage) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apiportal-aws_TagKeys)
  - **Resource types (\*required):** [ProductPage](#list_apiportal-resource-ProductPage) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apiportal-aws_TagKeys)
  - **Resource types (\*required):** [ProductSharingPolicy](#list_apiportal-resource-ProductSharingPolicy) / **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)<br />[aws:TagKeys](#list_apiportal-aws_TagKeys)
  - **Access level:** Tagging, Write

- **   [UpdatePortal](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_UpdatePortal.html)  **
  - **Description:** Grants permission to update a portal
  - **Resource types (\*required):** [Portal\*](#list_apiportal-resource-Portal)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdatePortalPublishStatus](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_UpdatePortalPublishStatus.html)  **
  - **Description:** Grants permission to publish or unpublish a portal
  - **Resource types (\*required):** [Portal\*](#list_apiportal-resource-Portal)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProduct](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_UpdateProduct.html)  **
  - **Description:** Grants permission to update a product
  - **Resource types (\*required):** [Product\*](#list_apiportal-resource-Product)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProductApiPage](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_UpdateProductApiPage.html)  **
  - **Description:** Grants permission to update an API reference page in a product
  - **Resource types (\*required):** [ProductApiPage\*](#list_apiportal-resource-ProductApiPage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Write

- **   [UpdateProductPage](https://docs.aws.amazon.com/apiportal/latest/APIReference/API_UpdateProductPage.html)  **
  - **Description:** Grants permission to update a documentation page in a product
  - **Resource types (\*required):** [ProductPage\*](#list_apiportal-resource-ProductPage)
  - **Condition keys:** [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_)
  - **Access level:** Write



## Resource types defined by AWS API Portal
<a name="list_apiportal-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [DiscoveryConfiguration](https://docs.aws.amazon.com/apiportal/latest/userguide/security-iam.html#security-iam-resources-DiscoveryConfiguration)  | arn:${Partition}:apiportal:${Region}:${Account}:discoveryconfiguration | [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_) | 
|  [ManagedApi](https://docs.aws.amazon.com/apiportal/latest/userguide/security-iam.html#security-iam-resources-ManagedApi)  | arn:${Partition}:apiportal:${Region}:${Account}:managedapis/${ManagedApiId} | [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_) | 
|  [OrganizationDiscoveryConfiguration](https://docs.aws.amazon.com/apiportal/latest/userguide/security-iam.html#security-iam-resources-OrganizationDiscoveryConfiguration)  | arn:${Partition}:apiportal:${Region}:${Account}:orgdiscoveryconfiguration | [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_) | 
|  [Portal](https://docs.aws.amazon.com/apiportal/latest/userguide/security-iam.html#security-iam-resources-Portal)  | arn:${Partition}:apiportal:${Region}:${Account}:portals/${PortalId} | [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_) | 
|  [Product](https://docs.aws.amazon.com/apiportal/latest/userguide/security-iam.html#security-iam-resources-Product)  | arn:${Partition}:apiportal:${Region}:${Account}:products/${ProductId} | [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_) | 
|  [ProductApiPage](https://docs.aws.amazon.com/apiportal/latest/userguide/security-iam.html#security-iam-resources-ProductApiPage)  | arn:${Partition}:apiportal:${Region}:${Account}:products/${ProductId}/apipages/${ProductApiPageId} | [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_) | 
|  [ProductPage](https://docs.aws.amazon.com/apiportal/latest/userguide/security-iam.html#security-iam-resources-ProductPage)  | arn:${Partition}:apiportal:${Region}:${Account}:products/${ProductId}/productpages/${ProductPageId} | [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_) | 
|  [ProductSharingPolicy](https://docs.aws.amazon.com/apiportal/latest/userguide/security-iam.html#security-iam-resources-ProductSharingPolicy)  | arn:${Partition}:apiportal:${Region}:${Account}:products/${ProductId}/sharingpolicy | [aws:ResourceTag/${TagKey}](#list_apiportal-aws_ResourceTag___TagKey_) | 

## Condition keys for AWS API Portal
<a name="list_apiportal-policy-keys"></a>

AWS API Portal defines the following condition keys that can be used in the `Condition` element of an IAM policy.



| Condition keys | Description | Type | 
| --- | --- | --- | 
|   [aws:RequestTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-requesttag)  | Filters access by a tag's key and value in a request | String | 
|   [aws:ResourceTag/${TagKey}](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourcetag)  | Filters actions based on the presence of tag key-value pairs in the request | String | 
|   [aws:TagKeys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-tagkeys)  | Filters access by the tag keys in a request | ArrayOfString | 