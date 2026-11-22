

# DaaS product pricing in AWS Marketplace

When you create a Data as a Service (DaaS) product, you choose the pricing model that AWS Marketplace uses to bill buyers on your behalf. The pricing model decides which AWS Marketplace APIs your product integrates with. All pricing models rely on entitlements, and usage-based pricing also relies on the usage that you report.

DaaS products support the following pricing models:


**DaaS pricing models**  

| Pricing model | How buyers are billed | What your product integrates with | 
| --- | --- | --- | 
| Contract | Buyers pay for a quantity of your product for a contract duration that you define. You can bill them in advance or offer a flexible payment schedule. | Check what each buyer purchased with the AWS Marketplace Entitlement Service, and grant access to that level. Check entitlements again when you receive an event that the buyer's entitlement changed. | 
| Pay as you go | AWS Marketplace bills buyers for their usage of your product, based on the usage that you report. | Check what each buyer is entitled to with the AWS Marketplace Entitlement Service. Report usage to the AWS Marketplace Metering Service. Send metering records on a regular schedule, ideally every hour. | 
| Contract with consumption | Buyers pay for a contract, and they're also billed for usage beyond the quantity that the contract includes. | Check entitlements to learn what the contract includes. Report only the usage that goes beyond those entitlements to the AWS Marketplace Metering Service. | 
| Free | Buyers use your product at no cost. All pricing dimensions must be set to USD $0.00. | Integrate with the fulfillment URL and subscription events, and check entitlements with the AWS Marketplace Entitlement Service. | 

You can also offer a free trial, so that buyers can evaluate your product before they pay. For more information, see [Creating a DaaS free trial offer in AWS Marketplace](daas-free-trials.md).

**You can't change the pricing model after you create a public offer**  
After you create a public offer, you can't change its pricing model. For more information about statuses, see [DaaS product lifecycle in AWS Marketplace](daas-product-lifecycle.md).

## How your pricing model affects your integration
<a name="daas-pricing-integration"></a>
+ For contract pricing, you need the fulfillment URL integration, subscription events, and entitlement checks. You don't report usage. For the fulfillment URL, see [Onboarding customers to your DaaS product through AWS Marketplace](daas-product-customer-setup.md).
+ For pay as you go pricing, you need the fulfillment URL integration, subscription events, entitlement checks, and metering.
+ For contract with consumption pricing, you need all of them: the fulfillment URL integration, subscription events, entitlement checks, and metering for usage beyond the contract.
+ For free pricing, you need the fulfillment URL integration, subscription events, and entitlement checks.

For usage-based pricing, report usage for each buyer with the [BatchMeterUsage](https://docs.aws.amazon.com/marketplacemetering/latest/APIReference/API_BatchMeterUsage.html) API. In each usage record, include the buyer's `CustomerAWSAccountId` and `LicenseArn` from the `ResolveCustomer` response. Don't include `ProductCode` in the request. After you report usage for an hour, you can't amend the record.

## Pricing dimensions
<a name="daas-pricing-dimensions"></a>

A pricing dimension is a unit that you charge for, such as API calls, records delivered, or users. Each dimension has its own price, and buyers see each one on your listing. Choose dimensions that match how buyers use your data and that they can understand and predict. For example, you might charge per API call, or charge a fixed amount for a 12-month contract with unlimited access.

## Offer availability by country
<a name="daas-pricing-availability"></a>

When you create an offer, you choose where it's available. You can make the offer available in all countries, or include or exclude specific countries to meet data licensing, regulatory, or export requirements.