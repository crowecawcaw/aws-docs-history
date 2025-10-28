# Amazon API Gateway

To build RESTful APIs, use REST APIs from Amazon API Gateway. REST APIs are intended for APIs that
require API proxy functionality and API management features in a single solution.

Amazon API Gateway Edge-optimized APIs provide a fully managed Amazon CloudFront distribution to optimize
access for geographically dispersed consumers. API requests are routed to the nearest CloudFront
Point of Presence (POP), which typically improves connection time.

![Diagram showing Edge-optimized API Gateway deployment](images/edge-optimized-api-gateway-deployment.png)

_Figure 22: Edge-optimized API Gateway deployment_

The API Gateway Regional endpoint doesn’t provide a CloudFront distribution, and enables HTTP2 by
default, which helps reduce overall latency when requests originate from the same Region.
Regional endpoints also allow you to associate your own Amazon CloudFront distribution or an existing
CDN.

![Diagram showing Regional Endpoint API Gateway deployment](images/regional-endpoint-api-gateway-deployment.png)

_Figure 23: Regional Endpoint API Gateway deployment_

This table can help you decide whether to deploy an Edge-optimized API or Regional API
Endpoint:

|                                                                                                                         | **Edge-optimized API** | **Regional API Endpoint** |
| ----------------------------------------------------------------------------------------------------------------------- | ---------------------- | ------------------------- |
| API is accessed across Regions. Includes API Gateway-managed CloudFront distribution.                                   | X                      |                           |
| API is accessed within same Region. Least request latency when API is accessed from the same Region as API is deployed. |                        | X                         |
| Ability to associate own CloudFront distribution.                                                                       |                        | X                         |
