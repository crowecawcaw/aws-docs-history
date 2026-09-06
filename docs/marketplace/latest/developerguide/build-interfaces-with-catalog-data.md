

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Build interfaces with catalog data
<a name="build-interfaces-with-catalog-data"></a>

You can use the AWS Marketplace Discovery API to programmatically access the catalog and display product and pricing information on your own platforms. This section describes how to build custom interfaces such as storefronts, partner portals, and integrated sales experiences for your customers to navigate, using the Discovery API.

## Architecture overview
<a name="discovery-seller-architecture"></a>

A typical integration follows this pattern:

1. **Browse experience** — Call `SearchListings` to retrieve listing summaries based on search text and filters, and `SearchFacets` to populate category navigation and filter options with counts.

1. **Product detail pages** — Call `GetListing` or `GetProduct` to display full product details, media, and reviews.

1. **Pricing display** — Call `ListPurchaseOptions`, `GetOffer`, and `GetOfferTerms` to show pricing options.

## Build a browse experience
<a name="discovery-seller-browse"></a>

Use `SearchListings` to retrieve listing summaries based on search text and filters, and `SearchFacets` to build dynamic filter navigation. Facets include categories, fulfillment types, pricing models, pricing units, publishers, and deployment status. Each facet value includes a count of matching listings, which you can display alongside filter options.

```
import boto3

client = boto3.client('marketplace-discovery', region_name='us-east-1')

# Get facet values for building filter navigation
facets = client.search_facets(
    facetTypes=['CATEGORY', 'FULFILLMENT_OPTION_TYPE', 'PRICING_MODEL']
)

for facet_type, values in facets['listingFacets'].items():
    print(f"\n{facet_type}:")
    for facet in values:
        print(f"  {facet['displayName']} ({facet['count']})")

# Search listings with filters applied from user selections
response = client.search_listings(
    searchText='machine learning',
    filters=[
        {
            'filterType': 'CATEGORY',
            'filterValues': ['Machine Learning']
        },
        {
            'filterType': 'PRICING_MODEL',
            'filterValues': ['USAGE']
        }
    ],
    sortBy='RELEVANCE',
    maxResults=25
)

for listing in response['listingSummaries']:
    print(f"{listing['listingName']} - {listing['shortDescription']}")
```

## Build product detail pages
<a name="discovery-seller-product-pages"></a>

Use `GetListing` or `GetProduct` to display full product details, media, and reviews. Use `GetListing` when you need the listing overview including badges, categories, and pricing summaries. Use `GetProduct` when you need detailed product information such as descriptions, highlights, and media. Call `ListFulfillmentOptions` to retrieve deployment options for a specific product.

```
def get_product_page_data(listing_id, product_id):
    """Retrieve data for a product detail page."""

    # Use GetListing for listing-level overview
    listing = client.get_listing(listingId=listing_id)

    # Or use GetProduct for detailed product information
    product = client.get_product(productId=product_id)

    # Get deployment options for the product
    fulfillment = client.list_fulfillment_options(productId=product_id)

    return {
        'listing': listing,
        'product': product,
        'fulfillmentOptions': fulfillment
    }
```

## Display pricing information
<a name="discovery-seller-pricing"></a>

Use `ListPurchaseOptions` to find available offers for a product, then `GetOffer` and `GetOfferTerms` to retrieve detailed pricing. Display pricing models, rate cards, and term details to help your customers evaluate options.

```
def get_pricing_for_product(product_id):
    """Retrieve pricing options for display."""
    options = client.list_purchase_options(
        filters=[{
            'filterType': 'PRODUCT_ID',
            'filterValues': [product_id]
        }]
    )

    pricing = []
    for option in options.get('purchaseOptions', []):
        for entity in option['associatedEntities']:
            offer = client.get_offer(
                offerId=entity['offer']['offerId']
            )
            terms = client.get_offer_terms(
                offerId=entity['offer']['offerId']
            )
            pricing.append({
                'option': option,
                'offer': offer,
                'terms': terms
            })

    return pricing
```

## Best practices
<a name="discovery-seller-best-practices"></a>
+ **Cache responses** — Product and pricing data changes infrequently. Cache API responses for 15–60 minutes to reduce API calls and improve page load times.
+ **Handle pagination** — Use `nextToken` to retrieve all results from paginated operations. Pagination tokens expire after 24 hours.
+ **Implement retry logic** — Use exponential backoff for `ThrottlingException` (HTTP 429) responses.
+ **Display attribution** — When displaying AWS Marketplace data on your platform, follow the [AWS Trademark Guidelines](https://aws.amazon.com/trademark-guidelines/).
+ **Minimize API calls** — Use `SearchListings` for summary data and only call detail APIs (`GetProduct`, `GetOffer`, `GetOfferTerms`) when a user navigates to a specific product.

**Note**  
The Discovery API supports all product types on AWS Marketplace, including SaaS, AI agents and tools, AMI, containers, and machine learning models. Your interface can display the full breadth of the catalog.