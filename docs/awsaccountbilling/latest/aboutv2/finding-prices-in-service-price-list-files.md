

# Finding prices in the service price list file
<a name="finding-prices-in-service-price-list-files"></a>


|  | 
| --- |
| To provide feedback about AWS Price List, complete this [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_cO0deTMyKyFeezA). Your responses will be anonymous. **Note:** This survey is in English only. | 

The AWS Price List Bulk API provides prices for all AWS products for informational purposes, including On-Demand and Reserved Instances pricing.

To find the prices and terms for a specific product, you can use the offer files. For example, you can find a list of Amazon Elastic Compute Cloud (Amazon EC2) instance prices.

**Note**  
The AWS Price List Bulk API is not a comprehensive source for limited period offers, such as AWS Free Tier pricing. For information about Free Tier prices, see [AWS Free Tier](https://aws.amazon.com/free/).

To find prices for the products you're interested in.

**Contents**
+ [Finding On-Demand prices for services](#finding-one-demand-prices-services)
+ [Finding tiered prices for services](#finding-tiered-prices-services)
+ [Finding tiered prices for services with Free Tier](#finding-tiered-prices-services-free-tier)
  + [Example](#finding-tiered-prices-services-free-tier-example)
+ [Finding prices for services with Reserved Instances](#finding-prices-services-reserved-instances)

## Finding On-Demand prices for services
<a name="finding-one-demand-prices-services"></a>

The following procedure shows how to find On-Demand prices for AWS services, such as Amazon EC2.

**To find an On-Demand price by using the CSV file**

1. Download the CSV file for the service.

1. Open the CSV file with your preferred application.

1. Under the **TermType** column, filter to show **OnDemand**.

1. Find the usage type and operation that you want.

1. In the **PricePerUnit** column, see the corresponding price.

**To find an On-Demand price by using the JSON file**

1. Download the JSON file for the service.

1. Open the JSON file with your preferred application.

1. Under **terms** and **On-Demand**, find the SKU that you want.

   If you don't know the SKU, search under **products** for the **usage type** and **operation**.

1. See the **pricePerUnit** to find the corresponding On-Demand price for the SKU.

## Finding tiered prices for services
<a name="finding-tiered-prices-services"></a>

The following procedure shows how to find tiered prices for services, such as Amazon Simple Storage Service (Amazon S3).

**To find tiered prices for services by using the CSV file**

1. Download the CSV file for the service.

1. Open the CSV file with your preferred application

1. Under the **TermType** column, filter to show **OnDemand**.

1. Find the usage type and operation that you want.

1. In the **PricePerUnit** column, see the corresponding price for each **StartingRange** and **EndingRange**.

**To find tiered prices for services by using the JSON file**

1. Download the JSON file.

1. Open the JSON file with your preferred application.

1. Under **terms** and **On-Demand** find the SKU that you want.

   If you don't know the SKU, search under **products** for the **usage type** and **operation**.

1. Under each **beginRange** and **endRange**, see the **pricePerUnit** to find the corresponding tiered prices.

## Finding tiered prices for services with Free Tier
<a name="finding-tiered-prices-services-free-tier"></a>

The following procedure shows how to find AWS services that publish Free Tier prices in the AWS Price List Bulk API, such as AWS Lambda.

All Free Tier prices are subject to the terms documented in [AWS Free Tier](https://aws.amazon.com/free).

**To find prices for services with Free Tier by using the CSV file**

1. Download the CSV file for the service.

1. Open the CSV file with your preferred application.

1. Under the **TermType** column, filter to show **OnDemand**.

1. Under the **Location** column, filter to show **Any**.

   **Any** doesn't represent all AWS Regions in this scenario. It's a subset of Regions defined by other line items in the CSV file, with a **RelatedTo** column matching the SKU for the location **Any** entry.

1. To find a list of all eligible locations and products for a specific Free Tier SKU, find the Free Tier SKU under the **RelatedTo** column.

1. To find the covered usage by Free Tier across all eligible locations, see the **StartingRange** and **EndingRange** for the location **Any**.

### Example
<a name="finding-tiered-prices-services-free-tier-example"></a>

This example assumes there are no more entries in the price file where **RelatedTo** equals to the SKU `ABCD`.

As shown in the following table, the Free Tier offer with SKU `ABCD` is valid in the `Asia Pacific (Singapore)` and `US East (Ohio)` Regions, but not in `AWS GovCloud (US)`. The covered usage by Free Tier is 400,000 seconds total, used across both eligible Regions.



| SKU | StartingRage | EndingRange | Unit | RelatedTo | Location | 
| --- | --- | --- | --- | --- | --- | 
| ABCD | 0 | 400000 | seconds |  | Any | 
| QWER | 0 | Inf | seconds | ABCD | Asia Pacific (Singapore) | 
| WERT | 0 | Inf | seconds | ABCD | US East (Ohio) | 
| ERTY | 0 | Inf | seconds |  | AWS GovCloud (US) | 

**To find tiered prices for services with Free Tier by using the JSON file**

1. Download the JSON file for the service.

1. Open the JSON file with your preferred application.

1. Under **products**, find the **usagetype** with the Region prefix **Global**.

1. Take note of the SKU, and look for the same SKU under **terms** and **OnDemand**.

1. For the amount of Free Tier usage, see the **BeginRange** and **EndRange** .

   For a list of products and Regions covered by Free Tier, see **appliesTo**.

## Finding prices for services with Reserved Instances
<a name="finding-prices-services-reserved-instances"></a>

The following procedure shows how to find prices for services with Reserved Instances, such as Amazon Relational Database Service (Amazon RDS).

**To find prices for a Reserved Instance by using the CSV file**

1. Download the Amazon EC2 CSV file.

1. Open the CSV file with your preferred application.

1. Under the **TermType** column, filter to show **reserved**.

1. Find the usage type and operation that you want.

1. For each **LeaseContractLength**, **PurchaseOption**, and **OfferingClass**, see the **PricePerUnit** column for the corresponding price.

**To find prices for Reserved Instances by using the JSON file**

1. Download the JSON file for the service.

1. Open the JSON file with your preferred application.

1. Under **terms** and **Reserved**, find the SKU that you want.

   If you don't know the SKU, search under **products** for the **usage type** and **operation**.

You can find prices for **LeaseContractLength**, **PurchaseOption**, and **OfferingClass** for the same product.