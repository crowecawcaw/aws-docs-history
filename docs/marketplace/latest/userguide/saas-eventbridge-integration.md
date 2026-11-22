

# Managing SaaS subscription events with Amazon EventBridge

You can use Amazon EventBridge to integrate and manage SaaS products with AWS Marketplace. Events are sent for changes to customers' subscriptions and contract entitlements for your products. You receive notifications when customers subscribe, when their entitlements change, and when they cancel, so you know exactly when to grant or revoke access. These events serve two primary roles:

**Note**  
These events are also sent for RTB Fabric module products.
+ **Manufacturer** – This is the original product manufacturer of the listing in AWS Marketplace, also known as the Independent Solution Vendor (ISV).
+ **Proposer** – This is the original proposer of a purchase agreement for the product listed in AWS Marketplace. This can be either the ISV or a Channel Partner authorized to resell the product.

Two distinct selling patterns determine whether you, as the ISV, act as a manufacturer or proposer. Your role determines which notifications you receive through EventBridge.


| Selling pattern | Description | ISV's role | 
| --- | --- | --- | 
| AWS Marketplace public or private offer | You extend an offer or agreement directly to the buyer. | Both manufacturer and proposer | 
| Channel partner private offer | A channel partner authorized to resell your product extends an offer or agreement to the buyer. | Manufacturer | 

## EventBridge events for SaaS products
<a name="saas-eventbridge-event-types"></a>

When a AWS Marketplace transaction occurs, EventBridge sends events to your default event bus. Your role as either a manufacturer or proposer determines which events you receive.


| Event name | Initiated by | Response | Recipient | 
| --- | --- | --- | --- | 
|  + Purchase Agreement Created - Manufacturer<br />+ Purchase Agreement Created - Proposer  | A new agreement is created, an existing agreement is replaced, or an existing agreement is renewed. | Purchase agreement is recorded and post-sale actions taken. DescribeAgreement API is used to determine if the new agreement is a free trial. | Manufacturer and proposer | 
|  + Purchase Agreement Amended - Manufacturer<br />+ Purchase Agreement Amended - Proposer  | An existing agreement is amended. | Purchase agreement record is amended. | Manufacturer and proposer | 
|  + Purchase Agreement Ended - Manufacturer<br />+ Purchase Agreement Ended - Proposer  | An agreement has expired, is canceled, is terminated. For a SaaS free trial that converts automatically, AWS Marketplace doesn't send this event when the free trial ends. It sends the event only if the buyer cancels. | Purchase agreement closure is recorded and post agreement cancelation actions happen. ISV begins revoking customer entitlements. | Manufacturer and proposer | 
| Purchase Agreement Free Trial Converted - Manufacturer | A buyer's SaaS free trial converts to a paid subscription on the conversion date. | The seller sends any remaining metering records for usage during the free trial, and updates the buyer's status. The subscription continues. | Manufacturer only | 
| Purchase Agreement Advisory Issued - Manufacturer | AWS has issued an advisory that might invalidate this agreement. Conditions that can trigger this alert include buyer account closure, compromise, abuse, or fraud. | AWS has identified an issue that affects this agreement. This issue might affect billing or service access. Contact the buyer directly and assess whether to revise their access. | Manufacturer only | 
| Purchase Agreement Advisory Resolved - Manufacturer | AWS has resolved the issues that were impacting this agreement. | AWS has resolved the issue affecting this agreement. If you made changes to the buyer's subscription or access, you can restore it at your discretion. | Manufacturer only | 
| Purchase Agreement Buyer Eligibility Updated - Manufacturer | AWS Marketplace has updated the information it has about the buyer's account. AWS Marketplace sends this event when a new agreement is created and whenever the buyer's level changes. | Informational; no action required. Review the buyer's current eligibility level and adjust access controls or service limits at your discretion. For level definitions, see [Amazon EventBridge events](notifications-eventbridge.md). | Manufacturer only | 
| License Updated - Manufacturer | The buyer's entitlement to a product has changed. | Customer entitlements are checked using the GetEntitlements API and services are provisioned accordingly. The event includes isFreeTrialTermPresent, the string "true", when the agreement has a free trial term. The field is absent when it doesn't. | Manufacturer only | 
| License Deprovisioned - Manufacturer | The buyer's entitlement to a product has ended. For a SaaS free trial that converts automatically, AWS Marketplace sends this event only if the buyer cancels. | For usage-based products, this event marks the start of a 1-hour final reporting window. Sellers should collect and report any unreported usage using the BatchMeterUsage API. After this window closes, customer entitlements are fully revoked and usage reporting is no longer accepted. This window doesn't apply to Agentic Commerce products, because AWS Marketplace meters each payment and you don't report usage. The event includes isFreeTrialTermPresent, the string "true", when the agreement has a free trial term. The field is absent when it doesn't. | Manufacturer only | 
| Spend Threshold Reached | The buyer's accumulated spend on a SaaS pay-as-you-go product reached a spend threshold, and AWS Marketplace initiated a payment verification (vet) on the buyer's card. | Informational; no action required. AWS Marketplace is verifying the buyer's ability to pay. Await the Spend Threshold Vet Succeeded or Spend Threshold Vet Failed event. | Manufacturer and proposer | 
| Spend Threshold Vet Succeeded | The payment verification on the buyer's card passed, and the spend threshold cycle reset. | Informational; no action required. AWS Marketplace validated the buyer's payment method. | Manufacturer and proposer | 
| Spend Threshold Vet Failed | The payment verification on the buyer's card failed. | AWS Marketplace could not verify the buyer's payment method. AWS Marketplace will retry verification. | Manufacturer and proposer | 

The Spend Threshold Reached, Spend Threshold Vet Succeeded, and Spend Threshold Vet Failed events apply only to SaaS products with usage-based (pay-as-you-go) pricing. AWS Marketplace does not send these events for SaaS products with contract-only or subscription pricing.

**Note**  
Purchase agreement event types for manufacturer and proposer are nearly identical, except for the presence of a resaleAuthorization ID. To avoid redundant messages, only the proposer purchase agreement event is sent when you are both the manufacturer and proposer. This doesn't apply to the `Purchase Agreement Free Trial Converted - Manufacturer` event, which AWS Marketplace sends only to the manufacturer.

For the full list of event types and their detailed schemas, see [Amazon EventBridge events](notifications-eventbridge.md) in the Seller Guide.

## Final usage reporting window for usage-based products
<a name="saas-eventbridge-final-usage"></a>

For products with a usage-based billing component, AWS Marketplace gives sellers one hour to submit final usage records for customers whose entitlements have ended. After this period, the `BatchMeterUsage` API rejects reported usage and you cannot bill the customer.

AWS Marketplace sends the License Deprovisioned - Manufacturer event to signal the start of the final reporting window. Sellers have one hour after receiving this event to collect any unreported usage for the customer and report it using the `BatchMeterUsage` API.

After the one-hour window closes, AWS Marketplace fully revokes the customer's entitlements and no longer accepts usage reporting.

**Note**  
The final reporting window doesn't apply to Agentic Commerce products. AWS Marketplace meters each verified payment, so you have no usage to report. For more information, see [Pricing and metering](agentic-commerce-products.md#agentic-commerce-pricing).

## Buyer Eligibility Level notifications
<a name="saas-eventbridge-buyer-eligibility"></a>

Sellers can use an Eligibility Level to inform access decisions within their SaaS product, based on how much information AWS has about the buyer's account.

When a buyer creates an agreement for your SaaS product, AWS Marketplace sends a `Purchase Agreement Buyer Eligibility Updated - Manufacturer` event that includes the buyer's current Eligibility Level. AWS Marketplace also sends this event whenever the level changes while the agreement is active.

This event is only available through EventBridge. It does not appear in the AWS Marketplace Notification Center or trigger email notifications.

For the full Eligibility Level reference, field definitions, and the event JSON schema, see [Amazon EventBridge events](notifications-eventbridge.md).

## Integrate EventBridge with your SaaS product
<a name="saas-eventbridge-using"></a>

Use EventBridge to integrate your tenant provisioning operations with your SaaS listing in AWS Marketplace.
+ Event rules define how to react to an event. These rules can react immediately or on a set schedule.
+ Event patterns are defined in the event rules and let you filter for specific event types sent to your default event bus. Patterns templates for each event type are available in the EventBridge console. In the Event pattern configuration step, select AWS services as the event source and AWS Marketplace Agreements and Licenses as the AWS service.
  + All AWS Marketplace Agreements and Licenses event types use the following structure.

  ```
  {
  "detail-type": ["e.g. Purchase Agreement Ended - Manufacturer"],
  "source": ["aws.agreement-marketplace"]
  }
  ```
+ Targets are resources that receive events when they match the event pattern defined for a rule. Many AWS services integrate with EventBridge and can serve as targets, including Lambda functions, Step Functions, and API Gateway.

For more information about setting up EventBridge rules, see [Getting started: Create an Amazon EventBridge event bus rule](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html).