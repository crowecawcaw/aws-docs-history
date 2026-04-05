# Implementation

Partner Revenue Measurement integrates with AWS Marketplace Metering to measure service usage and
attribute the consumption to your product, without requiring any additional inputs such as tagging
resources or implementing user agents. This is a zero-touch experience that leverages existing product
metadata for revenue attribution.

To avail attribution via this method, you need to list your AMI or ML product on
AWS Marketplace and ensure customers purchase and use it via AWS Marketplace.

## Amazon Machine Image (AMI) products

Revenue attribution for AMI products works as follows:

1. When you list an AMI product on AWS Marketplace, a unique product code is assigned to it.
2. This product code is automatically attached as instance metadata to every Amazon EC2 instance launched from your AMI.
3. When a buyer purchases and starts using your AMI product, Partner Revenue Measurement uses the product code to measure Amazon EC2 usage and attribute the consumption to your product.

Refer to [Understanding AMI-based products and AMI product codes](../../../marketplace/latest/userguide/ami-getting-started.md#ami-product-codes "../../../marketplace/latest/userguide/ami-getting-started.md#ami-product-codes")
for more details.

## Machine Learning (ML) products

When a buyer purchases, deploys, and starts consuming an ML product, AWS Marketplace can measure
the usage of the product to bill the customer. Partner Revenue Measurement integrates with
AWS Marketplace Metering to measure the customers' usage of Amazon SageMaker AI resources created
by your product and automatically attributes the consumption to your product.
