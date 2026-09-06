

# Amazon API Gateway in AWS GovCloud (US)
<a name="govcloud-abp"></a>

Amazon API Gateway is a fully managed service that makes it easy for developers to publish, maintain, monitor, and secure APIs at any scale. Create an API to access data, business logic, or functionality from your back-end services, such as applications running on Amazon Elastic Compute Cloud (Amazon EC2), code running on AWS Lambda, or any web application.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Amazon API Gateway differs
<a name="govcloud-apigw-diffs"></a>

The following differences apply to Amazon API Gateway:
+ The `TLS_1_0` security policy for Regional APIs is not available.
+ Portals are not available.
+  Amazon API Gateway edge-optimized API and edge-optimized custom domain name are not available.
+ The Amazon Route 53 Hosted Zone ID for the regional endpoint in the AWS GovCloud (US-West) Region is Z1K6XKP9SAGWDV. The Amazon Route 53 Hosted Zone ID for the regional endpoint in the AWS GovCloud (US-East) Region is Z3SE9ATJYCRCZJ.
+ HTTP API private integrations are not available in AWS GovCloud (US-East).
+ HTTP API private integrations with AWS Cloud Map are not available in AWS GovCloud (US-West).
+ All API Gateway APIs created in GovCloud Regions are FIPS-compliant by default.
+  API Gateway mTLS endpoints do not currently support ECDSA server certificates.
+  `TLS-CHACHA20-POLY1305-SHA256` is not available.

The following region-specific API Gateway account IDs are automatically added to your Amazon VPC endpoint service as AllowedPrincipals for private integrations in AWS GovCloud (US):


**​**  

| Region | Account ID | 
| --- | --- | 
| us-gov-west-1<br />us-gov-east-1 | 291049978687<br />044865953448 | 

## Documentation
<a name="govcloud-apigw-docs"></a>
+  [Amazon API Gateway documentation](https://docs.aws.amazon.com/documentation/apigateway/) 

## Export-Controlled Content
<a name="api-gateway"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ API Gateway’s configuration metadata is not permitted to contain export-controlled data\*, including:
  + API Name
  + API Description
  + Authorizer Name

    However customers can send export-controlled data through the customers’ deployed APIs, with the caveat that downstream systems need to be compliant (for example, caching cannot be enabled on the API for any export-controlled data).