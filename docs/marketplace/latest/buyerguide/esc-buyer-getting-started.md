

# Buying in the AWS European Sovereign Cloud Marketplace
<a name="esc-buyer-getting-started"></a>

 This guide is for buyers using AWS Marketplace in the AWS European Sovereign Cloud (ESC) partition to discover, procure, and manage software products. It describes how AWS Marketplace in the AWS ESC works, how it differs from the commercial AWS Marketplace, and what you need to get started. 

## What is AWS Marketplace in the AWS ESC?
<a name="what-is-esc-marketplace"></a>

 The AWS Marketplace in the ESC provides a modernized, fully integrated console experience for buyers in European sovereign regions. AWS Marketplace in the AWS ESC brings the latest AWS Marketplace buyer functionality while streamlining the user experience through consolidated console-based operations. This provides a more integrated and efficient procurement workflow. 

### AWS Marketplace vs. AWS Marketplace in the AWS ESC
<a name="commercial-vs-esc-marketplace"></a>

The following table summarizes the key differences between the AWS Marketplace and the AWS Marketplace in the AWS ESC from a buyer perspective.


| Aspect | Commercial Marketplace | ESC Marketplace | 
| --- | --- | --- | 
| Who it is for | Global AWS customers | EU-based customers requiring data sovereignty | 
| AWS partition | Standard ( aws ) | ESC ( aws-eusc ) | 
| Access | Marketplace website and AWS console | AWS console only (ESC partition) | 
| Product catalog | Global catalog | Separate ESC catalog — products must be explicitly listed by sellers | 
| Invoicing currency | USD (default) | EUR (default) | 
| AWS account requirement | Standard AWS account | AWS account in the ESC partition ( aws-eusc ) | 

## Accessing AWS Marketplace in the AWS ESC
<a name="accessing-esc-marketplace"></a>

 AWS Marketplace in the AWS ESC is accessible only from an AWS account in the ESC partition ( `aws-eusc` ). You cannot access the ESC catalog from a standard commercial AWS account, and commercial marketplace products are not visible from within the ESC partition unless the seller has also listed the product in the ESC catalog. 

 To access AWS Marketplace in the AWS ESC, sign in to the AWS console using your ESC partition account and navigate to AWS Marketplace. All product discovery, procurement, subscription management, and contract management take place within this single console interface. Please see [Signing up for an AWS account](https://docs.aws.eu/esc/latest/userguide/signup.html) on how to create your ESC buyer account. 

## Discovering and Purchasing Products
<a name="discovering-purchasing-products-esc"></a>

 ESC customers find products through keyword and category search, category and filter-based browsing, direct product URLs shared by sellers, and private offers extended to your account by sellers. 

### Supported product types
<a name="supported-product-types-esc"></a>

The following product types are available for purchase in AWS Marketplace in the AWS ESC:
+ **SaaS products**: All SaaS pricing models: Free, subscription, contract, and contract with consumption.
+ **AMI-based products**: Amazon Machine Images with various pricing options: Free, Paid hourly or hourly annual.

### Private offers
<a name="private-offers-esc-buyer"></a>

 Sellers can extend private offers to your ESC account with custom pricing and terms. To receive a private offer, provide the seller with your ESC partition AWS account ID. Private offers for ESC products are denominated in EUR by default, though sellers may also extend USD private offers. Your account must be in the ESC partition ( `aws-eusc` ) to accept an ESC private offer. 

### Billing and Invoicing
<a name="billing-invoicing-esc-buyer"></a>

#### Invoicing currency
<a name="invoicing-currency-esc"></a>

 All AWS Marketplace in the AWS ESC transactions are invoiced in Euros (EUR) unless you have selected an alternative preferred currency. Your invoices are generated and processed entirely within the ESC partition ( `aws-eusc` ), ensuring that all your transaction data remains within European boundaries. If you accept a USD-denominated private offer from a seller, that offer will be invoiced in USD. 

 Your invoices, subscriptions, and entitlements are managed entirely within the ESC partition. Your billing data does not leave the European Union, consistent with the data residency requirements AWS Marketplace in the AWS ESC is designed to support. 

#### Tax considerations
<a name="tax-considerations-esc-buyer"></a>

 ESC transactions follow the same tax treatment as commercial AWS Marketplace transactions. The same tax logic, rates, and obligations apply; no special or separate tax rules are introduced for ESC. For detailed guidance, refer to the [Tax Help page for Buyers](https://aws.amazon.com/tax-help/marketplace-buyers/). 