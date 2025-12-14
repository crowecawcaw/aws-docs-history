# Calling AWS services and prices using the AWS Price List

|                                                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| To provide feedback about AWS Price List, complete this [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_cO0deTMyKyFeezA "https://amazonmr.au1.qualtrics.com/jfe/form/SV_cO0deTMyKyFeezA"). Your responses will be anonymous. \*_Note:_<br>• This survey is in English only. |

AWS Price List provides a catalog of the products and prices for AWS services that you can
purchase on AWS.

This catalog includes perpetual free offers from AWS Free Tier. This includes usage-based free tier offers that refresh periodically, available permanently. This catalog doesn't include time-limited Free Tier offers that expire based on how long the account's been active. For more information about
Free Tier offers, see [Trying services using AWS Free Tier (before July 15, 2025)](billing-free-tier.md "billing-free-tier.md"). Also, this catalog doesn't include Amazon Elastic Compute Cloud (Amazon EC2) Spot
Instances. For more information about Amazon EC2 Spot Instances, see [Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot/ "https://aws.amazon.com/ec2/spot/").

For more information, see the following topics:

- [AWS Billing and Cost Management API Reference](../../../aws-cost-management/latest/APIReference/Welcome.md#Welcome_AWS_Price_List_Service "../../../aws-cost-management/latest/APIReference/Welcome.md#Welcome_AWS_Price_List_Service")
- [Language-specific AWS SDKs](../../../aws-cost-management/latest/APIReference/API_pricing_DescribeServices.md#API_pricing_DescribeServices_SeeAlso "../../../aws-cost-management/latest/APIReference/API_pricing_DescribeServices.md#API_pricing_DescribeServices_SeeAlso")
- [Tools for Amazon Web Services](https://aws.amazon.com/tools "https://aws.amazon.com/tools")

## Overview

To help you use the AWS Price List, the following are its key concepts:

**Service**

An AWS service, such as `Amazon EC2` or Savings Plans, for example: a Savings Plan for
Amazon EC2 is `AWSComputeSavingsPlan` or a service representing limited AWS Marketplace offerings,
for example: `AmazonBedrockFoundationModels`.

**Product**

An entity sold by an AWS service. In the price list file, products are indexed by a
unique stock keeping unit (SKU).

**Attribute**

The property associated with a product. This property consists of
`AttributeName` and `AttributeValue`. Products can
have multiple attributes. Each attribute has one `AttributeName` and
a list of applicable `AttributeValues`.

You can use the following AWS Price List APIs:

**[AWS Price List Query API](using-price-list-query-api.md "using-price-list-query-api.md")**

This API provides a centralized and convenient way to programmatically query
AWS for services, products, and pricing information.

The Price List Query API uses product attributes and provides prices at the SKU
level. Use this API to build cost control and scenario planning tools, reconcile
billing data, forecast future spend for budgeting purposes, and provide cost
benefit analyses that compare your internal workloads with AWS.

###### Note

The Price List Query API doesn't support Savings Plan prices.

**[AWS Price List Bulk API](using-the-aws-price-list-bulk-api.md "using-the-aws-price-list-bulk-api.md")**

This API provides a way to programmatically fetch up-to-date pricing
information on current AWS services and products in bulk by using the price list files.
The price list files are available in JSON and CSV formats. The price list files are organized by
AWS service and AWS Region.

###### Note

The Price List Query API and Price List Bulk API provide pricing details for informational
purposes only. If there's a difference between the price list file and a service pricing page,
AWS charges the prices on the _service pricing page_.

For more information about AWS service pricing, see [AWS Pricing](https://aws.amazon.com/pricing/services/ "https://aws.amazon.com/pricing/services/").

To call the AWS Price List APIs, we recommend that you use an AWS SDK that supports your
preferred programming language. AWS SDKs save you time and simplify the process of signing
requests. You can also integrate the AWS SDKs with your development environment and access
the related commands.

## Getting started with AWS Price List

### IAM permissions

An AWS Identity and Access Management (IAM) identity, such as a user or role, must have permission to use the
Price List Query API or Price List Bulk API. To grant access, see [Find products and prices](billing-example-policies.md#example-policy-pe-api "billing-example-policies.md#example-policy-pe-api").

### Endpoints

The Price List Query API and Price List Bulk API provides the following endpoints:

- https://api.pricing.us-east-1.amazonaws.com
- https://api.pricing.eu-central-1.amazonaws.com
- https://api.pricing.ap-south-1.amazonaws.com

The AWS Region is the API endpoint for the Price List Query API. The endpoints
aren't related to product or service attributes.

To call the Price List Query API or Price List Bulk API, see the following examples.

Java
In the following example, specify the
`region_name` and use it to create the
`PricingClient`.

```
public class Main {
    public static void main(String[] args) {

        // Create pricing client
        PricingClient client = PricingClient.builder()
                .region(Region.US\_EAST\_1)// or Region.AP\_SOUTH\_1
                .credentialsProvider(DefaultCredentialsProvider.builder().build())
                .build();
        );
    }
}
```

AWS Command Line Interface
Specify the Region with the following command.

```
aws pricing describe-services --region us-east-1
```

### Quotas

See [AWS Price List](billing-limits.md#price-list-api-quotas "billing-limits.md#price-list-api-quotas") in the _Quotas and restrictions_ page.

For more information about service quotas, see [AWS service
quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md") in the _AWS General Reference_.
