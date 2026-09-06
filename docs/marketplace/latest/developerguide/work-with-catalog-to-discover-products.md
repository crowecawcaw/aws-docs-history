

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Discover products and pricing
<a name="work-with-catalog-to-discover-products"></a>

You can use the AWS Marketplace Discovery API to programmatically search the catalog, retrieve detailed product information, and access pricing details including public and private offers. This section describes common workflows for discovering products and evaluating pricing.

## Browse the catalog
<a name="discovery-browse-catalog"></a>

Use `SearchFacets` to retrieve available filter values and build a browsing experience. Facets include categories, pricing models, fulfillment types, publishers, and deployment status. Each facet value includes a count of matching listings.

```
response = client.search_facets(
    facetTypes=['CATEGORY', 'PRICING_MODEL', 'FULFILLMENT_OPTION_TYPE']
)

for facet_type, values in response['listingFacets'].items():
    print(f"\n{facet_type}:")
    for facet in values:
        print(f"  {facet['displayName']} ({facet['count']} listings)")
```

## Search for listings
<a name="discovery-search-listings"></a>

Use `SearchListings` to find listings by keyword and filters. You can combine text search with facet-based filters, and sort results by relevance or customer rating.

```
results = client.search_listings(
    searchText='computer vision',
    filters=[
        {'filterType': 'CATEGORY', 'filterValues': ['machine-learning']},
        {'filterType': 'FULFILLMENT_OPTION_TYPE', 'filterValues': ['SAAS']}
    ],
    sortBy='RELEVANCE',
    maxResults=25
)

print(f"Found {results['totalResults']} listings")
for listing in results['listingSummaries']:
    print(f"  {listing['listingName']} -- {listing['publisher']['displayName']}")
```

## Get listing details
<a name="discovery-get-listing-details"></a>

Use `GetListing` to retrieve a listing's full details, including descriptions, categories, badges, pricing model summaries, reviews, and associated products and offers.

```
listing = client.get_listing(listingId='listing-saas-abc123')

print(f"Name: {listing['listingName']}")
print(f"Publisher: {listing['publisher']['displayName']}")
print(f"Pricing: {[p['displayName'] for p in listing['pricingModels']]}")
print(f"Rating: {listing['reviewSummary']['reviewSourceSummaries'][0]['averageRating']}")
```

## Get product details and fulfillment options
<a name="discovery-get-product-details"></a>

Use `GetProduct` to get detailed product information including descriptions, highlights, categories, and seller engagements. Use `ListFulfillmentOptions` to see how the product can be deployed (AMI, SaaS, Container, Helm, etc.).

```
product = client.get_product(productId='prod-gitpod-enterprise')

print(f"Description: {product['shortDescription']}")
print(f"Deployed on AWS: {product['deployedOnAws']}")

fulfillment = client.list_fulfillment_options(productId='prod-gitpod-enterprise')
for option in fulfillment['fulfillmentOptions']:
    # Each option is a union -- check which variant is present
    for variant_name, variant_data in option.items():
        print(f"  Deploy as: {variant_data['fulfillmentOptionType']}")
```

## Find available offers for a product
<a name="discovery-find-offers"></a>

Use `ListPurchaseOptions` to find all available purchase options (offers and offer sets) for a product. You can filter by product ID, seller, purchase option type, visibility scope, and availability status.

```
options = client.list_purchase_options(
    filters=[{
        'filterType': 'PRODUCT_ID',
        'filterValues': ['prod-gitpod-enterprise']
    }]
)

for option in options['purchaseOptions']:
    print(f"  {option['purchaseOptionType']}: {option.get('purchaseOptionName', 'Public offer')}")
    print(f"  Seller: {option['sellerOfRecord']['displayName']}")
```

## Get detailed pricing terms
<a name="discovery-get-pricing-terms"></a>

Use `GetOfferTerms` to retrieve the full commercial structure of an offer. Each offer contains one or more terms — pricing terms (usage-based, fixed upfront, configurable upfront, BYOL, free trial), legal terms, payment schedules, validity terms, support terms, and renewal terms.

```
terms = client.get_offer_terms(offerId='offer-abc123')

for term in terms['offerTerms']:
    # Each term is a union -- check which type is present
    for term_type, term_data in term.items():
        print(f"  Term: {term_data['type']}")
        if 'rateCards' in term_data:
            for card in term_data['rateCards']:
                for rate in card.get('rateCard', []):
                    print(f"    {rate['displayName']}: ${rate['price']}/{rate['unit']}")
```

## Get offer set details
<a name="discovery-get-offer-set"></a>

When a purchase option returned by `ListPurchaseOptions` has a `purchaseOptionType` of `OFFERSET`, it represents a grouped collection of private offers for a multi-product solution. Use `GetOfferSet` to retrieve the details of the offer set, including the associated products and offers, seller of record, availability dates, and buyer notes. You can then call `GetOffer` and `GetOfferTerms` for each individual offer within the set.

```
# Find offer sets for a product
options = client.list_purchase_options(
    filters=[
        {'filterType': 'PRODUCT_ID', 'filterValues': ['prod-abc123']},
        {'filterType': 'PURCHASE_OPTION_TYPE', 'filterValues': ['OFFERSET']}
    ]
)

for option in options.get('purchaseOptions', []):
    offer_set_id = option['purchaseOptionId']
    offer_set = client.get_offer_set(offerSetId=offer_set_id)

    print(f"Offer set: {offer_set.get('offerSetName', offer_set_id)}")
    print(f"Seller: {offer_set['sellerOfRecord']['displayName']}")

    # Review each product and offer in the set
    for entity in offer_set['associatedEntities']:
        print(f"  Product: {entity['product']['productName']}")
        print(f"  Offer: {entity['offer']['offerId']}")

        # Get terms for each offer in the set
        terms = client.get_offer_terms(offerId=entity['offer']['offerId'])
        for term in terms['offerTerms']:
            for term_type, term_data in term.items():
                print(f"    Term: {term_data['type']}")
```

## Access private offer pricing
<a name="discovery-private-offers"></a>

To access private offer pricing, the calling IAM principal must have the appropriate permissions. Private offers include negotiated pricing, custom terms, and organization-specific offers. Use the `VISIBILITY_SCOPE` filter with value `PRIVATE` in `ListPurchaseOptions` to find private offers available to your account.

```
private_options = client.list_purchase_options(
    filters=[
        {'filterType': 'PRODUCT_ID', 'filterValues': ['prod-gitpod-enterprise']},
        {'filterType': 'VISIBILITY_SCOPE', 'filterValues': ['PRIVATE']}
    ]
)
```

## Integrate with procurement tools
<a name="discovery-procurement-integration"></a>

The Discovery API is designed to integrate with enterprise procurement platforms. Common integration patterns include:
+ Integrating the AWS Marketplace catalog into your procurement tool's product catalog
+ Displaying product details and pricing within purchase request workflows
+ Enabling comparison shopping across AWS Marketplace offers

**Note**  
The Discovery API provides the product and pricing data you need to build integrated procurement experiences. Combine it with your existing procurement workflows to streamline purchasing decisions.