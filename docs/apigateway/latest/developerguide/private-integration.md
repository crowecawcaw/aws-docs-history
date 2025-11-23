# Private integrations for REST APIs in API Gateway

Use a private integration to expose your HTTP/HTTPS resources within an Amazon VPC for access by clients outside of
the VPC. This extends access to your private VPC resources beyond the VPC boundaries. You can control access to your
API by using any of the [authorization methods](apigateway-control-access-to-api.md "apigateway-control-access-to-api.md") that API Gateway
supports.

To create a private integration, you must first create a VPC link. API Gateway supports VPC links V2 for REST APIs.
VPC links V2 let you create private integrations that connect your REST API to Application Load Balancers without using an Network Load Balancer. Using an
Application Load Balancer allows you to connect to Amazon ECSs container-based applications and many other backends. VPC links V1 are
considered a legacy integration type. While they are supported by API Gateway, we recommend that you don't create new VPC
links V1.

## Considerations

The following considerations might impact your use of private integrations:

- All resources must be owned by the same AWS account. This includes the load balancer,
  VPC link and REST API.
- By default, private integration traffic uses the HTTP protocol. To use HTTPS, specify an [`uri`](../api/API_PutIntegration.md#apigw-PutIntegration-request-uri "../api/API_PutIntegration.md#apigw-PutIntegration-request-uri")
  that contains a secure server name, such as `https://example.com:443/test`.
- In a private integration, API Gateway includes the [stage](set-up-stages.md "set-up-stages.md") portion of the API
  endpoint in the request to your backend resources. For example, if you request the `test` stage of an
  API, API Gateway includes `test/path` in the request to your private integration. To remove the stage name from
  the request to your backend resources, use [parameter mapping](rest-api-parameter-mapping.md "rest-api-parameter-mapping.md")
  to create an override for the `$context.requestOverride.path` variable.
- Private integrations with AWS Cloud Map aren't supported.

###### Topics

- [Set up VPC links V2 in API Gateway](apigateway-vpc-links-v2.md "apigateway-vpc-links-v2.md")
- [Set up a private integration](set-up-private-integration.md "set-up-private-integration.md")
- [Private integration using VPC links V1 (legacy)](vpc-links-v1.md "vpc-links-v1.md")
