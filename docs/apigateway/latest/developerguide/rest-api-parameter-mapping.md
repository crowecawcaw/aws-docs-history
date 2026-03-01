# Parameter mapping for REST APIs in API Gateway

###### Note

If you are using an HTTP API, see [Transform API requests and responses for HTTP APIs in API Gateway](http-api-parameter-mapping.md "http-api-parameter-mapping.md").

In parameter mapping, you map request or response parameters. You can map parameters using parameter mapping
expressions or static values. For a list of mapping expressions, see [Parameter mapping source reference for REST APIs in API Gateway](rest-api-parameter-mapping-sources.md "rest-api-parameter-mapping-sources.md"). You can use parameter mapping in your integration request for
proxy and non-proxy integrations, but to use parameter mapping for an integration response, you need a non-proxy
integration.

For example, you can map the method request header parameter `puppies` to the integration request
header parameter `DogsAge0`. Then, if a client sends the header `puppies:true` to your API,
the integration request sends the request header `DogsAge0:true` to the integration endpoint. The following diagram shows the request lifecycle of this example.

![Diagram of API Gateway parameter mapping example for a request](images/parameter-mapping-example1.png)
To create this example using API Gateway, see [Example 1: Map a method request parameter to an integration request parameter](request-response-data-mappings.md#request-response-data-mappings-example-1 "request-response-data-mappings.md#request-response-data-mappings-example-1").

As another
example, you can also map the integration response header parameter `kittens` to the method response
header parameter `CatsAge0`. Then, if the integration endpoint returns `kittens:false`, the
client receives the header `CatsAge0:false`. The following diagram shows the request lifecycle of this example.

![Diagram of API Gateway parameter mapping example for a response](images/parameter-mapping-example2.png)

###### Topics

- [Parameter mapping examples for REST APIs in API Gateway](request-response-data-mappings.md "request-response-data-mappings.md")
- [Parameter mapping source reference for REST APIs in API Gateway](rest-api-parameter-mapping-sources.md "rest-api-parameter-mapping-sources.md")
