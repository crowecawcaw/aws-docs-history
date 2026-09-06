

# Multi-Catalog for AWS Marketplace Sellers
<a name="multi_catalog"></a>

 AWS Marketplace enables sellers to create and manage product listings across multiple separate catalogs through multi-catalog capability. Multi-Catalog allows you to list your software products in special regions and partitions beyond the standard commercial AWS Marketplace, each serving distinct customer bases with specific regulatory, data residency, or sovereignty requirements. 

 With Multi-Catalog, you maintain completely separate product catalogs in different AWS partitions while managing them from a central location. Each catalog operates independently with its own product listings and pricing, customer base and subscriptions, regulatory and compliance requirements, and geographic or jurisdictional boundaries. 

 You create and manage all catalogs through AWS Partner Central - AWS Marketplace using the catalog selection dropdown to switch between your available catalogs. 

![](http://docs.aws.amazon.com/marketplace/latest/userguide/images/multi-catalog-selection-dropdown.png)


## Available catalogs
<a name="available-catalogs"></a>

AWS Marketplace currently supports Multi-Catalog capability for the following catalogs:
+ **AWS Marketplace**: The commercial catalog refers to the standard, publicly available catalog of products and offers on AWS Marketplace that operates within the AWS Commercial Partition - the set of all regular AWS Regions.
+ **AWS Marketplace in the AWS European Sovereign Cloud (ESC)**: A new, independent cloud for Europe entirely located within the European Union (EU), designed to help customers meet their most stringent digital sovereignty requirements. Built in the EU for the EU, it is the only fully featured, independently operated sovereign cloud backed by strong technical controls, sovereign assurances and legal protections. The AWS Marketplace in the AWS ESC is the first additional catalog available through Multi-Catalog. It helps EU-based organizations to procure software with enhanced data residency and operational controls, designed by sellers to help meet stringent European regulatory requirements. See the [European Sovereign Cloud](https://aws.eu/) to learn more about European Sovereign Cloud.

## Managing multiple catalogs
<a name="managing-multiple-catalogs"></a>

 Sellers can maintain products in both Commercial and ESC catalogs simultaneously. Products in each catalog are independent, allowing separate pricing and distinct product portfolios. You may choose to support products in all catalogs or have dedicated product offerings per catalog. You manage all catalogs from the AWS Marketplace Management Portal or Partner Central. 

 At a glance, the following table summarizes the key differences between AWS Marketplace in the AWS Commercial regions ([aws.com](https://aws.amazon.com/)) and AWS Marketplace in the European Sovereign Cloud ([aws.eu](https://aws.eu/)). 


| Topic | AWS Marketplace | AWS Marketplace in the AWS ESC | 
| --- | --- | --- | 
| Customer base | All AWS customers | Global customers requiring European data sovereignty | 
| AWS partition | Standard (aws) | ESC (aws-eusc) | 
| Catalog management | Default catalog | Separate ESC catalog via the dedicated AWS Marketplace dropdown in Partner Central | 
| Product listing | Created via AWS Marketplace in Partner Central | Created in commercial via AWS Marketplace in Partner Central | 
| AWS account requirements | Commercial AWS account | Both commercial and ESC partition accounts required | 