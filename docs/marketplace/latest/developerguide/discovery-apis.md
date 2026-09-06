

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Using the AWS Marketplace Discovery API
<a name="discovery-apis"></a>

The AWS Marketplace Discovery API provides programmatic access to the AWS Marketplace catalog. You can use it to retrieve product and pricing information, build integrated procurement experiences, and create custom storefronts.

## Service endpoint
<a name="discovery-service-endpoint"></a>

The Discovery API uses the following endpoint format:

```
https://discovery-marketplace.{{region}}.api.aws
```

For example, to call the API in US East (N. Virginia):

```
https://discovery-marketplace.us-east-1.api.aws
```

## API version
<a name="discovery-api-version"></a>

The current API version is `2026-02-05`.

## Data model
<a name="discovery-data-model"></a>

The Discovery API organizes the AWS Marketplace catalog into the following entities:
+ **Listing** — A product or multi-product solution as it appears to buyers. A listing includes descriptions, highlights, categories, badges, pricing models, pricing units, reviews, promotional media, seller engagements, fulfillment option types, and references to associated products and offers. Use `GetListing` to retrieve a listing, or `SearchListings` to search across listings.
+ **Product** — The underlying software or service being sold. A product includes descriptions, highlights, categories, promotional media, seller engagements, and fulfillment options that describe how a buyer can deploy or access the product (such as AMI, SaaS, Container, or Helm). Use `GetProduct` to retrieve product details and `ListFulfillmentOptions` to retrieve detailed fulfillment options for a product.
+ **Offer** — A pricing arrangement for a product, including the pricing model, seller of record, availability dates, and badges. An offer contains commercial terms such as usage-based pricing, fixed upfront pricing, free trial periods, legal documents, payment schedules, and renewal terms. Use `ListPurchaseOptions` to find all available offers for a product, `GetOffer` to retrieve the details of an offer, and `GetOfferTerms` to retrieve the specific terms of the offer.
+ **Offer set** — A grouped collection of private offers for each product in a multi-product solution. An offer set lets buyers review all offers together and accept them simultaneously with a single action. Use `ListPurchaseOptions` to find all available offer sets for a product, `GetOfferSet` to retrieve the details of an offer set, `GetOffer` to retrieve the details of an offer, and `GetOfferTerms` to retrieve the specific terms of the offer.

## Authentication
<a name="discovery-authentication"></a>

The Discovery API uses standard AWS Signature Version 4 (SigV4) authentication. You must have valid AWS credentials and the appropriate IAM permissions to call the API. For details, see [Access control for the AWS Marketplace Discovery API](discovery-api-access-control.md).

## Making requests
<a name="discovery-making-requests"></a>

All Discovery API operations use the HTTP `POST` method with a JSON request body. The operation name is specified in the URL path.

## Response format
<a name="discovery-response-format"></a>

All responses are returned in JSON format. Successful responses return HTTP status code 200. Error responses include an error type and message. For details, see [Common Errors](https://docs.aws.amazon.com/marketplace/latest/APIReference/CommonErrors.html).

## Using the AWS SDK
<a name="discovery-using-sdk"></a>

The recommended way to call the Discovery API is through the AWS SDK. The SDK handles authentication, request signing, serialization, and error handling automatically.

```
# Python (Boto3) example
import boto3

client = boto3.client('marketplace-discovery', region_name='us-east-1')

response = client.get_listing(
    listingId='listing-saas-abc123'
)

print(response['listingName'])
```

```
// JavaScript (AWS SDK v3) example
import { MarketplaceDiscoveryClient, GetListingCommand } from "@aws-sdk/client-marketplace-discovery";

const client = new MarketplaceDiscoveryClient({ region: "us-east-1" });
const response = await client.send(new GetListingCommand({
    listingId: "listing-saas-abc123"
}));

console.log(response.listingName);
```

## Pagination
<a name="discovery-pagination"></a>

Operations that return lists (such as `ListPurchaseOptions` and `SearchFacets`) support pagination using `nextToken`. If the response includes a `nextToken` value, pass it in the next request to retrieve additional results.

## Throttling
<a name="discovery-throttling"></a>

The Discovery API enforces request rate limits to ensure service availability. If you exceed the rate limit, the API returns a `ThrottlingException` (HTTP 429). Implement exponential backoff and retry logic in your application.