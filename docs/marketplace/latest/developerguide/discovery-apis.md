

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

For the list of Regions where the Discovery API is available, see [Supported AWS Regions for the AWS Marketplace Discovery API](discovery-regions.md).

## Global endpoint
<a name="discovery-global-endpoint"></a>

The Discovery API also provides a global endpoint. The global endpoint routes each request to the nearest available AWS Region where the Discovery API is deployed, based on latency and availability health checks.

```
https://discovery-marketplace.global.api.aws
```

Use the global endpoint when your application doesn't depend on which Region serves a request.

### Sign requests to the global endpoint with SigV4a
<a name="discovery-global-endpoint-sigv4a"></a>

Requests to the global endpoint must be signed with SigV4a. A SigV4 signature is valid in only one Region, but the global endpoint can serve your request from any Region. If you sign a request to the global endpoint with SigV4, the request succeeds only when it's routed to the Region in your signature. Otherwise, the request fails with an authentication error (HTTP 403).

To use the global endpoint, configure your AWS SDK client as follows:

1. Set the client endpoint to `https://discovery-marketplace.global.api.aws`.

1. Set the authentication scheme preference to `sigv4a`. You can set this in the shared AWS `config` file (`auth_scheme_preference`), with the `AWS_AUTH_SCHEME_PREFERENCE` environment variable, or in the client configuration.

1. Set the SigV4a signing Region set to `*` so that the signature is valid in every Region. You can set this in the shared AWS `config` file (`sigv4a_signing_region_set`), with the `AWS_SIGV4A_SIGNING_REGION_SET` environment variable, or in the client configuration.

SigV4a signing requires the AWS Common Runtime (CRT). For example, install `botocore[crt]` for Python, or add the `auth-crt` module for Java. For the settings that each SDK supports, see [Authentication scheme](https://docs.aws.amazon.com/sdkref/latest/guide/feature-auth-scheme.html) in the *AWS SDKs and Tools Reference Guide*.

The following example configures a Python (Boto3) client for the global endpoint.

```
# Python (Boto3) example
import boto3
from botocore.config import Config

client = boto3.client(
    'marketplace-discovery',
    region_name='us-east-1',  # Required by the SDK, but doesn't affect routing.
    endpoint_url='https://discovery-marketplace.global.api.aws',
    config=Config(
        auth_scheme_preference='sigv4a',
        sigv4a_signing_region_set='*',
    ),
)

response = client.get_listing(
    listingId='listing-saas-abc123'
)

print(response['listingName'])
```

**Session token version requirement**  
If you use temporary security credentials, they must include a version 2 session token. Regional AWS STS endpoints return version 2 tokens by default. The global AWS STS endpoint (`sts.amazonaws.com`) returns version 1 tokens unless you change the account setting. For more information, see [Managing global endpoint session tokens](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_enable-regions.html#sts-regions-manage-tokens) in the *IAM User Guide*.

### Pagination constraint for the global endpoint
<a name="discovery-global-endpoint-pagination"></a>

A `nextToken` value is valid only in the Region that issued it. The global endpoint rejects a `nextToken` received from one Region if it routes the next request to another Region. This can happen when the nearest available Region changes or when the Region that issued the token becomes unhealthy. In that case, the API returns a `ValidationException` with the reason `INVALID_PAGINATION_TOKEN`.

If you paginate through the global endpoint, handle `INVALID_PAGINATION_TOKEN` by restarting from the first page.

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

The Discovery API supports SigV4 and SigV4a authentication for Regional endpoints. Requests to the global endpoint must be signed with SigV4a. For more information about signing requests to the global endpoint, see [Sign requests to the global endpoint with SigV4a](#discovery-global-endpoint-sigv4a). You must have valid AWS credentials and the appropriate IAM permissions to call the API. For details, see [Access control for the AWS Marketplace Discovery API](discovery-api-access-control.md).

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