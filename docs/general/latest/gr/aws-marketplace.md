# AWS Marketplace endpoints and quotas

AWS Marketplace is a curated digital catalog that makes it easy for customers to find, buy, deploy,
and manage third-party software and services that customers need to build solutions and run their
businesses.

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

The AWS Marketplace website is available globally. The AWS Marketplace console is available in
the US East (N. Virginia) Region. The product vendor determines the Regions in which their products
are available.

### AWS Marketplace Catalog API

| Region Name           | Region    | Endpoint                                    | Protocol |
| --------------------- | --------- | ------------------------------------------- | -------- |
| US East (N. Virginia) | us-east-1 | catalog.marketplace.us-east-1.amazonaws.com | HTTPS    |

### AWS Marketplace Commerce Analytics

| Region Name           | Region    | Endpoint                                             | Protocol |
| --------------------- | --------- | ---------------------------------------------------- | -------- |
| US East (N. Virginia) | us-east-1 | marketplacecommerceanalytics.us-east-1.amazonaws.com | HTTPS    |

### AWS Marketplace Entitlement Service

| Region Name           | Region    | Endpoint                                                                                     | Protocol       |
| --------------------- | --------- | -------------------------------------------------------------------------------------------- | -------------- |
| US East (N. Virginia) | us-east-1 | entitlement.marketplace.us-east-1.amazonaws.com<br>entitlement-marketplace.us-east-1.api.aws | HTTPS<br>HTTPS |

### AWS Marketplace Metering Service

| Region Name               | Region         | Endpoint                                                                                         | Protocol       |
| ------------------------- | -------------- | ------------------------------------------------------------------------------------------------ | -------------- |
| US East (Ohio)            | us-east-2      | metering.marketplace.us-east-2.amazonaws.com<br>metering-marketplace.us-east-2.api.aws           | HTTPS<br>HTTPS |
| US East (N. Virginia)     | us-east-1      | metering.marketplace.us-east-1.amazonaws.com<br>metering-marketplace.us-east-1.api.aws           | HTTPS<br>HTTPS |
| US West (N. California)   | us-west-1      | metering.marketplace.us-west-1.amazonaws.com<br>metering-marketplace.us-west-1.api.aws           | HTTPS<br>HTTPS |
| US West (Oregon)          | us-west-2      | metering.marketplace.us-west-2.amazonaws.com<br>metering-marketplace.us-west-2.api.aws           | HTTPS<br>HTTPS |
| Africa (Cape Town)        | af-south-1     | metering.marketplace.af-south-1.amazonaws.com<br>metering-marketplace.af-south-1.api.aws         | HTTPS<br>HTTPS |
| Asia Pacific (Hong Kong)  | ap-east-1      | metering.marketplace.ap-east-1.amazonaws.com<br>metering-marketplace.ap-east-1.api.aws           | HTTPS<br>HTTPS |
| Asia Pacific (Hyderabad)  | ap-south-2     | metering.marketplace.ap-south-2.amazonaws.com<br>metering-marketplace.ap-south-2.api.aws         | HTTPS<br>HTTPS |
| Asia Pacific (Jakarta)    | ap-southeast-3 | metering.marketplace.ap-southeast-3.amazonaws.com<br>metering-marketplace.ap-southeast-3.api.aws | HTTPS<br>HTTPS |
| Asia Pacific (Melbourne)  | ap-southeast-4 | metering.marketplace.ap-southeast-4.amazonaws.com<br>metering-marketplace.ap-southeast-4.api.aws | HTTPS<br>HTTPS |
| Asia Pacific (Mumbai)     | ap-south-1     | metering.marketplace.ap-south-1.amazonaws.com<br>metering-marketplace.ap-south-1.api.aws         | HTTPS<br>HTTPS |
| Asia Pacific (Osaka)      | ap-northeast-3 | metering.marketplace.ap-northeast-3.amazonaws.com<br>metering-marketplace.ap-northeast-3.api.aws | HTTPS<br>HTTPS |
| Asia Pacific (Seoul)      | ap-northeast-2 | metering.marketplace.ap-northeast-2.amazonaws.com<br>metering-marketplace.ap-northeast-2.api.aws | HTTPS<br>HTTPS |
| Asia Pacific (Singapore)  | ap-southeast-1 | metering.marketplace.ap-southeast-1.amazonaws.com<br>metering-marketplace.ap-southeast-1.api.aws | HTTPS<br>HTTPS |
| Asia Pacific (Sydney)     | ap-southeast-2 | metering.marketplace.ap-southeast-2.amazonaws.com<br>metering-marketplace.ap-southeast-2.api.aws | HTTPS<br>HTTPS |
| Asia Pacific (Tokyo)      | ap-northeast-1 | metering.marketplace.ap-northeast-1.amazonaws.com<br>metering-marketplace.ap-northeast-1.api.aws | HTTPS<br>HTTPS |
| Canada (Central)          | ca-central-1   | metering.marketplace.ca-central-1.amazonaws.com<br>metering-marketplace.ca-central-1.api.aws     | HTTPS<br>HTTPS |
| Europe (Frankfurt)        | eu-central-1   | metering.marketplace.eu-central-1.amazonaws.com<br>metering-marketplace.eu-central-1.api.aws     | HTTPS<br>HTTPS |
| Europe (Ireland)          | eu-west-1      | metering.marketplace.eu-west-1.amazonaws.com<br>metering-marketplace.eu-west-1.api.aws           | HTTPS<br>HTTPS |
| Europe (London)           | eu-west-2      | metering.marketplace.eu-west-2.amazonaws.com<br>metering-marketplace.eu-west-2.api.aws           | HTTPS<br>HTTPS |
| Europe (Milan)            | eu-south-1     | metering.marketplace.eu-south-1.amazonaws.com<br>metering-marketplace.eu-south-1.api.aws         | HTTPS<br>HTTPS |
| Europe (Paris)            | eu-west-3      | metering.marketplace.eu-west-3.amazonaws.com<br>metering-marketplace.eu-west-3.api.aws           | HTTPS<br>HTTPS |
| Europe (Spain)            | eu-south-2     | metering.marketplace.eu-south-2.amazonaws.com<br>metering-marketplace.eu-south-2.api.aws         | HTTPS<br>HTTPS |
| Europe (Stockholm)        | eu-north-1     | metering.marketplace.eu-north-1.amazonaws.com<br>metering-marketplace.eu-north-1.api.aws         | HTTPS<br>HTTPS |
| Europe (Zurich)           | eu-central-2   | metering.marketplace.eu-central-2.amazonaws.com<br>metering-marketplace.eu-central-2.api.aws     | HTTPS<br>HTTPS |
| Israel (Tel Aviv)         | il-central-1   | metering.marketplace.il-central-1.amazonaws.com<br>metering-marketplace.il-central-1.api.aws     | HTTPS<br>HTTPS |
| Middle East (Bahrain)     | me-south-1     | metering.marketplace.me-south-1.amazonaws.com<br>metering-marketplace.me-south-1.api.aws         | HTTPS<br>HTTPS |
| Middle East (UAE)         | me-central-1   | metering.marketplace.me-central-1.amazonaws.com<br>metering-marketplace.me-central-1.api.aws     | HTTPS<br>HTTPS |
| South America (São Paulo) | sa-east-1      | metering.marketplace.sa-east-1.amazonaws.com<br>metering-marketplace.sa-east-1.api.aws           | HTTPS<br>HTTPS |
| AWS GovCloud (US-East)    | us-gov-east-1  | metering.marketplace.us-gov-east-1.amazonaws.com<br>metering-marketplace.us-gov-east-1.api.aws   | HTTPS<br>HTTPS |
| AWS GovCloud (US-West)    | us-gov-west-1  | metering.marketplace.us-gov-west-1.amazonaws.com<br>metering-marketplace.us-gov-west-1.api.aws   | HTTPS<br>HTTPS |

## Service quotas

For more information, see [Quotas for the AWS Marketplace
API](../../../marketplace/latest/APIReference/service-quotas.md "../../../marketplace/latest/APIReference/service-quotas.md").
