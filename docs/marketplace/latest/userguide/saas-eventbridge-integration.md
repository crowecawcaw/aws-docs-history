# Managing SaaS subscription events with Amazon EventBridge

You can use Amazon EventBridge to integrate and manage SaaS products with AWS Marketplace. Events are sent for changes to customers' subscriptions and contract entitlements for your products. You receive notifications when customers subscribe, when their entitlements change, and when they cancel, so you know exactly when to grant or revoke access. These events serve two primary roles:

- **Manufacturer** – This is the original product manufacturer of the listing in AWS Marketplace, also known as the Independent Solution Vendor (ISV).
- **Proposer** – This is the original proposer of a purchase agreement for the product listed in AWS Marketplace. This can be either the ISV or a Channel Partner authorized to resell the product.
  Two distinct selling patterns determine whether you, as the ISV, act as a manufacturer or proposer. Your role determines which notifications you receive through EventBridge.

| Selling pattern                         | Description                                                                                     | ISV's role                     |
| --------------------------------------- | ----------------------------------------------------------------------------------------------- | ------------------------------ |
| AWS Marketplace public or private offer | You extend an offer or agreement directly to the buyer.                                         | Both manufacturer and proposer |
| Channel partner private offer           | A channel partner authorized to resell your product extends an offer or agreement to the buyer. | Manufacturer                   |

## EventBridge events for SaaS products

When a AWS Marketplace transaction occurs, EventBridge sends events to your default event bus. Your role as either a manufacturer or proposer determines which events you receive.

| Event name                                                                             | Initiated by                                                                                        | Response                                                                                                                                                                                                                                                                           | Recipient                 |
| -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| • Purchase Agreement Created - Manufacturer<br>• Purchase Agreement Created - Proposer | A new agreement is created, an existing agreement is replaced, or an existing agreement is renewed. | Purchase agreement is recorded and post-sale actions taken. `DescribeAgreement` API is used to determine if the new agreement is a free trial.                                                                                                                                     | Manufacturer and proposer |
| • Purchase Agreement Amended - Manufacturer<br>• Purchase Agreement Amended - Proposer | An existing agreement is amended.                                                                   | Purchase agreement record is amended.                                                                                                                                                                                                                                              | Manufacturer and proposer |
| • Purchase Agreement Ended - Manufacturer<br>• Purchase Agreement Ended - Proposer     | An agreement has expired, is canceled, is terminated.                                               | Purchase agreement closure is recorded and post agreement cancelation actions happen. ISV begins revoking customer entitlements. For usage-based products, the ISV reports final usage records before the license deprovisioning event is sent and the reporting window is closed. | Manufacturer and proposer |
| License Updated<br>• Manufacturer                                                      | The buyer's entitlement to a product has changed.                                                   | Customer entitlements are checked using the `GetEntitlements` API and services are provisioned accordingly.                                                                                                                                                                        | Manufacturer only         |
| License Deprovisioned<br>• Manufacturer                                                | The buyer's entitlement to a product has ended.                                                     | Customer entitlements are fully revoked.                                                                                                                                                                                                                                           | Manufacturer only         |

###### Note

Purchase agreement event types for manufacturer and proposer are nearly identical, except for the presence of a resaleAuthorization ID. To avoid redundant messages, only the proposer purchase agreement event is sent when you are both the manufacturer and proposer.

For information about how to respond to these notifications, see the following topics:

- [Integrating your SaaS subscription or Pay-As-You-Go product with AWS Marketplace](saas-integrate-subscription.md "saas-integrate-subscription.md")
- [Integrating your SaaS contract product with AWS Marketplace](saas-integrate-contract.md "saas-integrate-contract.md")
- [Integrating your SaaS contract-based product with AWS Marketplace](saas-integrate-contract-with-pay.md "saas-integrate-contract-with-pay.md")

For the full list of event types and their detailed schemas, see [Amazon EventBridge events](notifications-eventbridge.md "notifications-eventbridge.md") in the Seller Guide.

## Report final usage before license is deprovisioned

For products with a usage-based billing component, AWS Marketplace gives sellers one hour to submit final usage records for customers whose agreement has ended. After this period, the `BatchMeterUsage` API rejects reported usage and you cannot bill the customer. The following events define the start and close of that window:

- AWS Marketplace sends the purchase agreement ended event at agreement expiration and marks the start of the final reporting window. Sellers have one hour to collect any unreported usage for the customer and report it using the `BatchMeterUsage` API.
- AWS Marketplace sends the license deprovisioned event when it has fully revoked the customer's entitlements and no longer accepts usage reporting.

## Integrate EventBridge with your SaaS product

Use EventBridge to integrate your tenant provisioning operations with your SaaS listing in AWS Marketplace.

- Event rules define how to react to an event. These rules can react immediately or on a set schedule.
- Event patterns are defined in the event rules and let you filter for specific event types sent to your default event bus. Patterns templates for each event type are available in the EventBridge console. In the Event pattern configuration step, select AWS services as the event source and AWS Marketplace Agreements and Licenses as the AWS service.
  - All AWS Marketplace Agreements and Licenses event types use the following structure.

```
{
"detail-type": ["e.g. Purchase Agreement Ended - Manufacturer"],
"source": ["aws.agreement-marketplace"]
}
```

- Targets are resources that receive events when they match the event pattern defined for a rule. Many AWS services integrate with EventBridge and can serve as targets, including Lambda functions, Step Functions, and API Gateway.

For more information about setting up EventBridge rules, see [Getting started: Create an Amazon EventBridge event bus rule](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md").
