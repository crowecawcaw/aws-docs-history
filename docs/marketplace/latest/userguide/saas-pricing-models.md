

# SaaS product pricing in AWS Marketplace

After a buyer purchases your software as a service (SaaS) product on AWS Marketplace, AWS Marketplace provides you with their billing identiﬁer. You use the billing identifier to call the AWS Marketplace Entitlement Service and the AWS Marketplace Metering Service. Then, customers access the product in your AWS environment or through a virtual private cloud (VPC) endpoint connection that you create. This topic provides a list of SaaS pricing models for AWS Marketplace.

**Note**  
All SaaS pricing models support free trials. Free trials on SaaS subscription products can convert to paid automatically, and SaaS contract free trials expire when they end. Free trials aren't available in the AWS European Sovereign Cloud catalog. For more information, see [SaaS free trials](https://docs.aws.amazon.com/marketplace/latest/userguide/saas-free-trials.html).  
The exception is Agentic Commerce products, which support neither free trials nor free pricing. They use only usage pricing, with a reserved USD $1.00 dimension that AWS Marketplace meters for you. For more information, see [Pricing and metering](agentic-commerce-products.md#agentic-commerce-pricing).


**SaaS pricing models**  

| Pricing model | Description | 
| --- | --- | 
| SaaS subscriptions | A pay-as-you-go model where we bill buyers for their hourly usage of your SaaS product. For more information, see [Pricing for SaaS subscriptions](saas-subscriptions.md). API-based AI agent products that use Agentic Commerce also use this model, but are billed per verified request rather than hourly: AI agents pay for each request through x402, at the price in your signed quote. For each verified payment, AWS Marketplace meters the quoted amount, in dollars, against the reserved agentic\_commerce\_default dimension. You don't send metering records. For more information, see [Listing Agentic Commerce products](agentic-commerce-products.md). | 
| SaaS contracts | Buyers are either billed in advance for the use of your software, or you can offer them a flexible payment schedule. Customers can also pay for additional usage above their contract. For more information, see [Pricing for SaaS contracts](saas-contracts.md). | 
| SaaS contracts with pay-as-you-go |  Buyers are either billed in advance for the use of your software, or you can offer them a flexible payment schedule. Buyers are also billed an additional metered rate for usage on top of the contract price. For more information, see [Pricing for SaaS contracts](saas-contracts.md). | 
| SaaS free | A free pricing model where customers can use your SaaS product at no cost. You don't configure pricing or pricing dimensions. | 

**Note**  
You choose the pricing model on the **Set pricing model and dimensions** step when you create the public offer. You can't change the pricing model later. To use a different pricing model, create a new product.

To make your SaaS product available on AWS Marketplace, decide whether you want to offer the [SaaS subscriptions pricing model](saas-subscriptions.md) or the [SaaS contracts pricing model](saas-contracts.md).

**Note**  
If you add your product to the AWS Marketplace Express Checkout catalog, see [Pricing recommendations](saas-express-checkout.md#saas-express-checkout-pricing) for Express Checkout.