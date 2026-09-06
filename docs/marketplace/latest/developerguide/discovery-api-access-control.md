

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Access control for the AWS Marketplace Discovery API
<a name="discovery-api-access-control"></a>

The Discovery API uses AWS Identity and Access Management (IAM) for authentication and authorization. Any AWS customer can call the Discovery API by configuring the appropriate IAM permissions.

Users must have the following permissions to call Discovery API operations:
+ `GetListing` – Grants permission to retrieve information about a listing.
+ `GetProduct` – Grants permission to retrieve information about a product.
+ `GetOffer` – Grants permission to retrieve information about an offer.
+ `GetOfferTerms` – Grants permission to retrieve terms for an offer.
+ `GetOfferSet` – Grants permission to retrieve information about an offer set.
+ `ListPurchaseOptions` – Grants permission to list purchase options available to the buyer.
+ `ListFulfillmentOptions` – Grants permission to list fulfillment options for a product.
+ `SearchListings` – Grants permission to search for product listings.
+ `SearchFacets` – Grants permission to retrieve facet values for filtering listings.

## IAM permissions
<a name="discovery-iam-permissions"></a>

To call Discovery API operations, the IAM principal (user or role) must have the appropriate `aws-marketplace` permissions. The Discovery API supports resource-level permissions, so you can scope access to specific resource types in your IAM policies.

The following IAM policy grants access to all Discovery API operations with resource-level scoping:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "aws-marketplace:GetListing",
                "aws-marketplace:GetProduct",
                "aws-marketplace:GetOffer",
                "aws-marketplace:GetOfferTerms",
                "aws-marketplace:GetOfferSet",
                "aws-marketplace:ListPurchaseOptions",
                "aws-marketplace:ListFulfillmentOptions",
                "aws-marketplace:SearchFacets",
                "aws-marketplace:SearchListings"
            ],
            "Resource": [
                "arn:aws:aws-marketplace:::catalog/<catalog-name>/product/*",
                "arn:aws:aws-marketplace:::catalog/<catalog-name>/listing/*",
                "arn:aws:aws-marketplace:::catalog/<catalog-name>/offer/*",
                "arn:aws:aws-marketplace:::catalog/<catalog-name>/offerSet/*",
                "arn:aws:aws-marketplace:::catalog/<catalog-name>/purchaseOption/*"
            ]
        }
    ]
}
```

Replace `<catalog-name>` with the appropriate catalog identifier (for example, `AWSMarketplace`).

### Resource ARN formats
<a name="discovery-resource-arn-formats"></a>

The following table shows the resource types and their ARN formats used by Discovery API operations:


| Resource type | ARN format | Used by | 
| --- | --- | --- | 
| Product | arn:aws:aws-marketplace:::catalog/{{catalog-name}}/product/{{product-id}} | GetProduct, ListFulfillmentOptions | 
| Listing | arn:aws:aws-marketplace:::catalog/{{catalog-name}}/listing/{{listing-id}} | GetListing, SearchListings, SearchFacets | 
| Offer | arn:aws:aws-marketplace:::catalog/{{catalog-name}}/offer/{{offer-id}} | GetOffer, GetOfferTerms | 
| Offer Set | arn:aws:aws-marketplace:::catalog/{{catalog-name}}/offerSet/{{offerSet-id}} | GetOfferSet | 
| Purchase Option | arn:aws:aws-marketplace:::catalog/{{catalog-name}}/purchaseOption/{{purchaseOption-id}} | ListPurchaseOptions | 

### Scoping operations to specific resources
<a name="discovery-scoping-get-operations"></a>

For Get operations (GetListing, GetProduct, GetOffer, GetOfferTerms, GetOfferSet) and the ListFulfillmentOptions operation, you can scope access down to specific resource IDs instead of using a wildcard. For example, to restrict access to a single listing:

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "aws-marketplace:GetListing",
            "Resource": "arn:aws:aws-marketplace:::catalog/AWSMarketplace/listing/{{listing-id}}"
        }
    ]
}
```

This pattern works for any Get operation and ListFulfillmentOptions. Replace the resource type and ID accordingly:
+ `arn:aws:aws-marketplace:::catalog/{{catalog-name}}/product/{{product-id}}`
+ `arn:aws:aws-marketplace:::catalog/{{catalog-name}}/listing/{{listing-id}}`
+ `arn:aws:aws-marketplace:::catalog/{{catalog-name}}/offer/{{offer-id}}`
+ `arn:aws:aws-marketplace:::catalog/{{catalog-name}}/offerSet/{{offerSet-id}}`

The SearchListings, SearchFacets, and ListPurchaseOptions operations do not support scoping to a single resource because they operate across multiple items. Use the following wildcard ARN patterns for these operations:
+ For SearchListings and SearchFacets: `arn:aws:aws-marketplace:::catalog/{{catalog-name}}/listing/*`
+ For ListPurchaseOptions: `arn:aws:aws-marketplace:::catalog/{{catalog-name}}/purchaseOption/*`

## Service-linked roles
<a name="discovery-service-linked-roles"></a>

The Discovery API does not use service-linked roles. All access is controlled through standard IAM policies.

## Cross-account access
<a name="discovery-cross-account-access"></a>

You can grant cross-account access to the Discovery API using IAM roles. Create a role in the target account with the appropriate Discovery API permissions, then assume the role from the source account.