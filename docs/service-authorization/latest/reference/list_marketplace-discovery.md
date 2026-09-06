

# Actions, resources, and condition keys for AWS Marketplace Discovery
<a name="list_marketplace-discovery"></a>

AWS Marketplace Discovery (service prefix: `aws-marketplace`) provides the following service-specific operations, resources, actions, and condition keys for use in IAM permission policies.

References:
+ Learn how to [configure this service](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-getting-started.html).
+ View a list of the [API operations available for this service](https://docs.aws.amazon.com/marketplace/latest/APIReference/discovery-apis.html).
+ Learn how to secure this service and its resources by [using IAM](https://docs.aws.amazon.com/marketplace/latest/APIReference/discovery-api-access-control.html) permission policies.
+ View the [programmatic service authorization reference](https://servicereference.us-east-1.amazonaws.com/v1/aws-marketplace/aws-marketplace.json) for this service.

**Topics**
+ [API operations defined by AWS Marketplace Discovery](#list_marketplace-discovery-operations)
+ [Actions defined by AWS Marketplace Discovery](#list_marketplace-discovery-actions-as-permissions)
+ [Resource types defined by AWS Marketplace Discovery](#list_marketplace-discovery-resources-for-iam-policies)
+ [Condition keys for AWS Marketplace Discovery](#list_marketplace-discovery-policy-keys)

## API operations defined by AWS Marketplace Discovery
<a name="list_marketplace-discovery-operations"></a>

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_marketplace-discovery-actions-as-permissions).




- **   GetListing  **
  - **IAM action:**  [aws-marketplace:GetListing](#list_marketplace-discovery-action-GetListing) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOffer  **
  - **IAM action:**  [aws-marketplace:GetOffer](#list_marketplace-discovery-action-GetOffer) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOfferSet  **
  - **IAM action:**  [aws-marketplace:GetOfferSet](#list_marketplace-discovery-action-GetOfferSet) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetOfferTerms  **
  - **IAM action:**  [aws-marketplace:GetOfferTerms](#list_marketplace-discovery-action-GetOfferTerms) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   GetProduct  **
  - **IAM action:**  [aws-marketplace:GetProduct](#list_marketplace-discovery-action-GetProduct) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** Read

- **   ListFulfillmentOptions  **
  - **IAM action:**  [aws-marketplace:ListFulfillmentOptions](#list_marketplace-discovery-action-ListFulfillmentOptions) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   ListPurchaseOptions  **
  - **IAM action:**  [aws-marketplace:ListPrivateListings](#list_marketplace-discovery-action-ListPrivateListings)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List
  - **IAM action:**  [aws-marketplace:ListPurchaseOptions](#list_marketplace-discovery-action-ListPurchaseOptions)  / **Condition key:**  / **Possible value(s):**  / **Access level:** List

- **   SearchFacets  **
  - **IAM action:**  [aws-marketplace:SearchFacets](#list_marketplace-discovery-action-SearchFacets) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List

- **   SearchListings  **
  - **IAM action:**  [aws-marketplace:SearchListings](#list_marketplace-discovery-action-SearchListings) 
  - **Condition key:** 
  - **Possible value(s):** 
  - **Access level:** List



## Actions defined by AWS Marketplace Discovery
<a name="list_marketplace-discovery-actions-as-permissions"></a>

You can specify the following actions in the `Action` element of an IAM policy statement. Use policies to grant permissions to perform an operation in AWS. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.




- **   [GetListing](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_GetListing.html)  **
  - **Description:** Grants permission to retrieve information about a listing
  - **Resource types (\*required):** [Listing\*](#list_marketplace-discovery-resource-Listing)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetOffer](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_GetOffer.html)  **
  - **Description:** Grants permission to retrieve information about an offer
  - **Resource types (\*required):** [Offer\*](#list_marketplace-discovery-resource-Offer)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetOfferSet](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_GetOfferSet.html)  **
  - **Description:** Grants permission to retrieve information about an offer set
  - **Resource types (\*required):** [OfferSet\*](#list_marketplace-discovery-resource-OfferSet)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetOfferTerms](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_GetOfferTerms.html)  **
  - **Description:** Grants permission to retrieve terms for an offer
  - **Resource types (\*required):** [Offer\*](#list_marketplace-discovery-resource-Offer)
  - **Condition keys:**  
  - **Access level:** Read

- **   [GetProduct](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_GetProduct.html)  **
  - **Description:** Grants permission to retrieve information about a product
  - **Resource types (\*required):** [Product\*](#list_marketplace-discovery-resource-Product)
  - **Condition keys:**  
  - **Access level:** Read

- **   [ListFulfillmentOptions](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_ListFulfillmentOptions.html)  **
  - **Description:** Grants permission to list fulfillment options for a product
  - **Resource types (\*required):** [Product\*](#list_marketplace-discovery-resource-Product)
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPrivateListings](https://docs.aws.amazon.com/marketplace/latest/buyerguide/private-offers-page.html)  **
  - **Description:** Grants permission to list private offers
  - **Resource types (\*required):** 
  - **Condition keys:**  
  - **Access level:** List

- **   [ListPurchaseOptions](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_ListPurchaseOptions.html)  **
  - **Description:** Grants permission to list purchase options available to the buyer
  - **Resource types (\*required):** [AllPurchaseOptions\*](#list_marketplace-discovery-resource-AllPurchaseOptions)
  - **Condition keys:**  
  - **Access level:** List

- **   [SearchFacets](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_SearchFacets.html)  **
  - **Description:** Grants permission to search for facet values to filter listings
  - **Resource types (\*required):** [AllListings\*](#list_marketplace-discovery-resource-AllListings)
  - **Condition keys:**  
  - **Access level:** List

- **   [SearchListings](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_SearchListings.html)  **
  - **Description:** Grants permission to search for product listings
  - **Resource types (\*required):** [AllListings\*](#list_marketplace-discovery-resource-AllListings)
  - **Condition keys:**  
  - **Access level:** List



## Resource types defined by AWS Marketplace Discovery
<a name="list_marketplace-discovery-resources-for-iam-policies"></a>

The following resource types are defined by this service and can be used in the `Resource` element of IAM permission policy statements.



| Resource types | ARN | Condition keys | 
| --- | --- | --- | 
|  [AllListings](https://docs.aws.amazon.com/marketplace/latest/APIReference/discovery-apis.html#discovery-data-model)  | arn:${Partition}:aws-marketplace:::catalog/${CatalogName}/listing/\* |   | 
|  [AllPurchaseOptions](https://docs.aws.amazon.com/marketplace/latest/APIReference/discovery-apis.html#discovery-data-model)  | arn:${Partition}:aws-marketplace:::catalog/${CatalogName}/purchaseOption/\* |   | 
|  [Listing](https://docs.aws.amazon.com/marketplace/latest/APIReference/discovery-apis.html#discovery-data-model)  | arn:${Partition}:aws-marketplace:::catalog/${CatalogName}/listing/${ListingId} |   | 
|  [Offer](https://docs.aws.amazon.com/marketplace/latest/APIReference/discovery-apis.html#discovery-data-model)  | arn:${Partition}:aws-marketplace:::catalog/${CatalogName}/offer/${OfferId} |   | 
|  [OfferSet](https://docs.aws.amazon.com/marketplace/latest/APIReference/discovery-apis.html#discovery-data-model)  | arn:${Partition}:aws-marketplace:::catalog/${CatalogName}/offerSet/${OfferSetId} |   | 
|  [Product](https://docs.aws.amazon.com/marketplace/latest/APIReference/discovery-apis.html#discovery-data-model)  | arn:${Partition}:aws-marketplace:::catalog/${CatalogName}/product/${ProductId} |   | 
|  [PurchaseOption](https://docs.aws.amazon.com/marketplace/latest/APIReference/discovery-apis.html#discovery-data-model)  | arn:${Partition}:aws-marketplace:::catalog/${CatalogName}/purchaseOption/${PurchaseOptionId} |   | 

## Condition keys for AWS Marketplace Discovery
<a name="list_marketplace-discovery-policy-keys"></a>

AWS Marketplace Discovery has no service-specific condition keys that can be used in the `Condition` element of policy statements.