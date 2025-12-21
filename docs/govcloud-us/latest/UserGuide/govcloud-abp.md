# Amazon API Gateway in AWS GovCloud (US)

Amazon API Gateway is a fully managed service that makes it easy for developers to publish, maintain, monitor, and secure APIs at any scale. Create an API to access data, business logic, or functionality from your back-end services, such as applications running on Amazon Elastic Compute Cloud (Amazon EC2), code running on AWS Lambda, or any web application.

## How Amazon API Gateway differs for AWS GovCloud (US)

- Policy that start with `SecurityPolicy_` are not supported.
- Portals are not supported.
- Amazon API Gateway edge-optimized API and edge-optimized custom domain name are not supported.
- The Amazon Route 53 Hosted Zone ID for the regional endpoint in the AWS GovCloud (US-West) Region is Z1K6XKP9SAGWDV. The Amazon Route 53 Hosted Zone ID for the regional endpoint in the AWS GovCloud (US-East) Region is Z3SE9ATJYCRCZJ.
- HTTP API private integrations aren’t supported in AWS GovCloud (US-East).
- HTTP API private integrations with AWS Cloud Map aren’t supported in AWS GovCloud (US-West).
- All API Gateway APIs created in GovCloud Regions are FIPS-compliant by default.
- API Gateway mTLS endpoints do not currently support ECDSA server certificates.
- `TLS-CHACHA20-POLY1305-SHA256` is not supported.

The following region-specific API Gateway account IDs are automatically added to your Amazon VPC endpoint service as AllowedPrincipals for private integrations in AWS GovCloud (US):

| ​                              | Region                       | Account ID |
| ------------------------------ | ---------------------------- | ---------- |
| us-gov-west-1<br>us-gov-east-1 | 291049978687<br>044865953448 |

## Documentation for Amazon API Gateway

[Amazon API Gateway documentation](https://aws.amazon.com/documentation/apigateway/ "https://aws.amazon.com/documentation/apigateway/").

## Export-Controlled Content

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.

- API Gateway’s configuration metadata is not permitted to contain export-controlled data\*, including:
  - API Name
  - API Description
  - Authorizer Name

  However customers can send export-controlled data through the customers’ deployed APIs, with the caveat that downstream systems need to be compliant (for example, caching cannot be enabled on the API for any export-controlled data).
