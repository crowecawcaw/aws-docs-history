#

API endpoint types for REST APIs in API Gateway

An _[API
endpoint](api-gateway-basic-concept.md#apigateway-definition-api-endpoints "api-gateway-basic-concept.md#apigateway-definition-api-endpoints")_ type refers to the hostname of the API. The API endpoint
type can be _edge-optimized_, _Regional_, or
_private_, depending on where the majority of your API traffic
originates from.

## Edge-optimized API

endpoints

An _[edge-optimized API endpoint](api-gateway-basic-concept.md#apigateway-definition-edge-optimized-api-endpoint "api-gateway-basic-concept.md#apigateway-definition-edge-optimized-api-endpoint")_ typically routes requests to the nearest CloudFront Point of Presence
(POP), which could help in cases where your clients are geographically distributed. This is the default endpoint type for API Gateway REST APIs.

Edge-optimized APIs capitalize the names of [HTTP
headers](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers "https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers") (for example, `Cookie`).

CloudFront sorts HTTP cookies in natural order by cookie name before forwarding the
request to your origin. For more information about the way CloudFront processes cookies,
see [Caching Content Based on
Cookies](../../../AmazonCloudFront/latest/DeveloperGuide/Cookies.md "../../../AmazonCloudFront/latest/DeveloperGuide/Cookies.md").

Any custom domain name that you use for an edge-optimized API applies across all
regions.

## Regional API

endpoints

A _[Regional
API endpoint](api-gateway-basic-concept.md#apigateway-definition-regional-api-endpoint "api-gateway-basic-concept.md#apigateway-definition-regional-api-endpoint")_ is intended for clients in the same Region.
When a client running on an EC2 instance calls an API in the same Region, or when an
API is intended to serve a small number of clients with high demands, a Regional API
reduces connection overhead.

For a Regional API, any custom domain name that you use is specific to the Region
where the API is deployed. If you deploy a Regional API in multiple Regions, it can
have the same custom domain name in all Regions. You can use custom domains together
with Amazon Route 53 to perform tasks such as [latency-based
routing](../../../Route53/latest/DeveloperGuide/routing-policy.md#routing-policy-latency "../../../Route53/latest/DeveloperGuide/routing-policy.md#routing-policy-latency"). For more information, see [Set up a Regional custom
domain name in API Gateway](apigateway-regional-api-custom-domain-create.md "apigateway-regional-api-custom-domain-create.md") and [Set up an edge-optimized custom domain name in API Gateway](how-to-edge-optimized-custom-domain-name.md "how-to-edge-optimized-custom-domain-name.md").

Regional API endpoints pass all header names through as-is.

###### Note

In cases where API clients are geographically dispersed, it may still make sense to
use a Regional API endpoint, together with your own Amazon CloudFront distribution to ensure that
API Gateway does not associate the API with service-controlled CloudFront distributions. For more
information about this use case, see [How do I set up API Gateway with my own CloudFront distribution?](https://repost.aws/knowledge-center/api-gateway-cloudfront-distribution "https://repost.aws/knowledge-center/api-gateway-cloudfront-distribution").

## Private API

endpoints

A _[private API
endpoint](api-gateway-basic-concept.md#apigateway-definition-private-api-endpoint "api-gateway-basic-concept.md#apigateway-definition-private-api-endpoint")_ is an API endpoint that can only be accessed from
your Amazon Virtual Private Cloud (VPC) using an interface VPC endpoint, which is an endpoint network
interface (ENI) that you create in your VPC. For more information, see [Private REST APIs in API Gateway](apigateway-private-apis.md "apigateway-private-apis.md").

Private API endpoints pass all header names through as-is.
