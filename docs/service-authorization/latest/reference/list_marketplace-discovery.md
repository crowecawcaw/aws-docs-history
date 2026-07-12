# Actions, resources, and condition keys for AWS Marketplace Discovery

AWS Marketplace Discovery (service prefix: `aws-marketplace`) provides the following
service-specific operations, resources, actions, and condition keys for use in IAM permission
policies.

References:

- Learn how to [configure this service](../../../marketplace/latest/buyerguide/buyer-getting-started.md "../../../marketplace/latest/buyerguide/buyer-getting-started.md").
- View a list of the [API operations available for
  this service](../../../marketplace/latest/APIReference/discovery-apis.md "../../../marketplace/latest/APIReference/discovery-apis.md").
- Learn how to secure this service and its resources by
  [using IAM](../../../marketplace/latest/APIReference/discovery-api-access-control.md "../../../marketplace/latest/APIReference/discovery-api-access-control.md") permission policies.
- View the [programmatic service authorization
  reference](https://servicereference.us-east-1.amazonaws.com/v1/aws-marketplace/aws-marketplace.json "https://servicereference.us-east-1.amazonaws.com/v1/aws-marketplace/aws-marketplace.json") for this service.

###### Topics

- [API operations defined by AWS Marketplace Discovery](#list_marketplace-discovery-operations "#list_marketplace-discovery-operations")
- [Actions defined by AWS Marketplace Discovery](#list_marketplace-discovery-actions-as-permissions "#list_marketplace-discovery-actions-as-permissions")
- [Resource types defined by AWS Marketplace Discovery](#list_marketplace-discovery-resources-for-iam-policies "#list_marketplace-discovery-resources-for-iam-policies")
- [Condition keys for AWS Marketplace Discovery](#list_marketplace-discovery-policy-keys "#list_marketplace-discovery-policy-keys")

## API operations defined by AWS Marketplace Discovery

The following table maps API operations to the IAM actions they authorize. Only condition keys that have static values for the given API and action are listed; for the full set of condition keys supported by each action, see the [Actions table](#list_marketplace-discovery-actions-as-permissions "#list_marketplace-discovery-actions-as-permissions").

| Operation                                                                                                                                              | IAM action                                                                                                                                                      | Condition key | Possible value(s) | Access level |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------- | ------------ |
| GetListing                                                                                                                                             | [aws-marketplace:GetListing](#list_marketplace-discovery-action-GetListing "#list_marketplace-discovery-action-GetListing")                                     |               |                   | Read         |
| GetOffer                                                                                                                                               | [aws-marketplace:GetOffer](#list_marketplace-discovery-action-GetOffer "#list_marketplace-discovery-action-GetOffer")                                           |               |                   | Read         |
| GetOfferSet                                                                                                                                            | [aws-marketplace:GetOfferSet](#list_marketplace-discovery-action-GetOfferSet "#list_marketplace-discovery-action-GetOfferSet")                                  |               |                   | Read         |
| GetOfferTerms                                                                                                                                          | [aws-marketplace:GetOfferTerms](#list_marketplace-discovery-action-GetOfferTerms "#list_marketplace-discovery-action-GetOfferTerms")                            |               |                   | Read         |
| GetProduct                                                                                                                                             | [aws-marketplace:GetProduct](#list_marketplace-discovery-action-GetProduct "#list_marketplace-discovery-action-GetProduct")                                     |               |                   | Read         |
| ListFulfillmentOptions                                                                                                                                 | [aws-marketplace:ListFulfillmentOptions](#list_marketplace-discovery-action-ListFulfillmentOptions "#list_marketplace-discovery-action-ListFulfillmentOptions") |               |                   | List         |
| ListPurchaseOptions                                                                                                                                    | [aws-marketplace:ListPrivateListings](#list_marketplace-discovery-action-ListPrivateListings "#list_marketplace-discovery-action-ListPrivateListings")          |               |                   | List         |
| [aws-marketplace:ListPurchaseOptions](#list_marketplace-discovery-action-ListPurchaseOptions "#list_marketplace-discovery-action-ListPurchaseOptions") |                                                                                                                                                                 |               | List              |
| SearchFacets                                                                                                                                           | [aws-marketplace:SearchFacets](#list_marketplace-discovery-action-SearchFacets "#list_marketplace-discovery-action-SearchFacets")                               |               |                   | List         |
| SearchListings                                                                                                                                         | [aws-marketplace:SearchListings](#list_marketplace-discovery-action-SearchListings "#list_marketplace-discovery-action-SearchListings")                         |               |                   | List         |

## Actions defined by AWS Marketplace Discovery

You can specify the following actions in the `Action` element of an IAM
policy statement. Use policies to grant permissions to perform an operation in AWS. When
you use an action in a policy, you usually allow or deny access to the API operation or CLI
command with the same name. However, in some cases, a single action controls access to more
than one operation. Alternatively, some operations require several different actions.

| Actions                                                                                                                                                                                                               | Description                                                       | Resource types (\*required)                                                                                                               | Condition keys | Access level |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------ |
| [GetListing](../../../marketplace/latest/APIReference/API_marketplace-discovery_GetListing.md "../../../marketplace/latest/APIReference/API_marketplace-discovery_GetListing.md")                                     | Grants permission to retrieve information about a listing         | [Listing\*](#list_marketplace-discovery-resource-Listing "#list_marketplace-discovery-resource-Listing")                                  |                | Read         |
| [GetOffer](../../../marketplace/latest/APIReference/API_marketplace-discovery_GetOffer.md "../../../marketplace/latest/APIReference/API_marketplace-discovery_GetOffer.md")                                           | Grants permission to retrieve information about an offer          | [Offer\*](#list_marketplace-discovery-resource-Offer "#list_marketplace-discovery-resource-Offer")                                        |                | Read         |
| [GetOfferSet](../../../marketplace/latest/APIReference/API_marketplace-discovery_GetOfferSet.md "../../../marketplace/latest/APIReference/API_marketplace-discovery_GetOfferSet.md")                                  | Grants permission to retrieve information about an offer set      | [OfferSet\*](#list_marketplace-discovery-resource-OfferSet "#list_marketplace-discovery-resource-OfferSet")                               |                | Read         |
| [GetOfferTerms](../../../marketplace/latest/APIReference/API_marketplace-discovery_GetOfferTerms.md "../../../marketplace/latest/APIReference/API_marketplace-discovery_GetOfferTerms.md")                            | Grants permission to retrieve terms for an offer                  | [Offer\*](#list_marketplace-discovery-resource-Offer "#list_marketplace-discovery-resource-Offer")                                        |                | Read         |
| [GetProduct](../../../marketplace/latest/APIReference/API_marketplace-discovery_GetProduct.md "../../../marketplace/latest/APIReference/API_marketplace-discovery_GetProduct.md")                                     | Grants permission to retrieve information about a product         | [Product\*](#list_marketplace-discovery-resource-Product "#list_marketplace-discovery-resource-Product")                                  |                | Read         |
| [ListFulfillmentOptions](../../../marketplace/latest/APIReference/API_marketplace-discovery_ListFulfillmentOptions.md "../../../marketplace/latest/APIReference/API_marketplace-discovery_ListFulfillmentOptions.md") | Grants permission to list fulfillment options for a product       | [Product\*](#list_marketplace-discovery-resource-Product "#list_marketplace-discovery-resource-Product")                                  |                | List         |
| [ListPrivateListings](../../../marketplace/latest/buyerguide/private-offers-page.md "../../../marketplace/latest/buyerguide/private-offers-page.md")                                                                  | Grants permission to list private offers                          |                                                                                                                                           |                | List         |
| [ListPurchaseOptions](../../../marketplace/latest/APIReference/API_marketplace-discovery_ListPurchaseOptions.md "../../../marketplace/latest/APIReference/API_marketplace-discovery_ListPurchaseOptions.md")          | Grants permission to list purchase options available to the buyer | [AllPurchaseOptions\*](#list_marketplace-discovery-resource-AllPurchaseOptions "#list_marketplace-discovery-resource-AllPurchaseOptions") |                | List         |
| [SearchFacets](../../../marketplace/latest/APIReference/API_marketplace-discovery_SearchFacets.md "../../../marketplace/latest/APIReference/API_marketplace-discovery_SearchFacets.md")                               | Grants permission to search for facet values to filter listings   | [AllListings\*](#list_marketplace-discovery-resource-AllListings "#list_marketplace-discovery-resource-AllListings")                      |                | List         |
| [SearchListings](../../../marketplace/latest/APIReference/API_marketplace-discovery_SearchListings.md "../../../marketplace/latest/APIReference/API_marketplace-discovery_SearchListings.md")                         | Grants permission to search for product listings                  | [AllListings\*](#list_marketplace-discovery-resource-AllListings "#list_marketplace-discovery-resource-AllListings")                      |                | List         |

## Resource types defined by AWS Marketplace Discovery

The following resource types are defined by this service and can be used in the
`Resource` element of IAM permission policy statements.

| Resource types                                                                                                                                                                          | ARN                                                                                          | Condition keys |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------- |
| [AllListings](../../../marketplace/latest/APIReference/discovery-apis.md#discovery-data-model "../../../marketplace/latest/APIReference/discovery-apis.md#discovery-data-model")        | arn:${Partition}:aws-marketplace:::catalog/${CatalogName}/listing/\*                         |                |
| [AllPurchaseOptions](../../../marketplace/latest/APIReference/discovery-apis.md#discovery-data-model "../../../marketplace/latest/APIReference/discovery-apis.md#discovery-data-model") | arn:${Partition}:aws-marketplace:::catalog/${CatalogName}/purchaseOption/\*                  |                |
| [Listing](../../../marketplace/latest/APIReference/discovery-apis.md#discovery-data-model "../../../marketplace/latest/APIReference/discovery-apis.md#discovery-data-model")            | arn:${Partition}:aws-marketplace:::catalog/${CatalogName}/listing/${ListingId}               |                |
| [Offer](../../../marketplace/latest/APIReference/discovery-apis.md#discovery-data-model "../../../marketplace/latest/APIReference/discovery-apis.md#discovery-data-model")              | arn:${Partition}:aws-marketplace:::catalog/${CatalogName}/offer/${OfferId}                   |                |
| [OfferSet](../../../marketplace/latest/APIReference/discovery-apis.md#discovery-data-model "../../../marketplace/latest/APIReference/discovery-apis.md#discovery-data-model")           | arn:${Partition}:aws-marketplace:::catalog/${CatalogName}/offerSet/${OfferSetId}             |                |
| [Product](../../../marketplace/latest/APIReference/discovery-apis.md#discovery-data-model "../../../marketplace/latest/APIReference/discovery-apis.md#discovery-data-model")            | arn:${Partition}:aws-marketplace:::catalog/${CatalogName}/product/${ProductId}               |                |
| [PurchaseOption](../../../marketplace/latest/APIReference/discovery-apis.md#discovery-data-model "../../../marketplace/latest/APIReference/discovery-apis.md#discovery-data-model")     | arn:${Partition}:aws-marketplace:::catalog/${CatalogName}/purchaseOption/${PurchaseOptionId} |                |

## Condition keys for AWS Marketplace Discovery

AWS Marketplace Discovery has no service-specific condition keys that can be used in the
`Condition` element of policy statements.
