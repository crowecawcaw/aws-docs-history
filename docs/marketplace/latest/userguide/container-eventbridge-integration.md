

# Managing container agreement events with Amazon EventBridge
<a name="container-eventbridge-integration"></a>

You can use Amazon EventBridge to receive notifications about changes to customer agreements for your container products on AWS Marketplace. Events are sent for agreement lifecycle changes, so you can track when customers subscribe, amend, or cancel. These events serve two primary roles:
+ **Manufacturer** – The original product manufacturer (ISV) in a channel partner resale (CPPO) arrangement.
+ **Proposer** – The party who extends the offer directly to the buyer. This is the ISV for direct offers, or the channel partner for CPPO offers.

Two distinct selling patterns determine whether you, as the ISV, act as a manufacturer or proposer. Your role determines which notifications you receive through EventBridge.


| Selling pattern | Description | ISV's role | 
| --- | --- | --- | 
| AWS Marketplace public or private offer | You extend an offer or agreement directly to the buyer. | Both manufacturer and proposer | 
| Channel partner private offer | A channel partner authorized to resell your product extends an offer or agreement to the buyer. | Manufacturer | 

## EventBridge events for container products
<a name="container-eventbridge-event-types"></a>

When an AWS Marketplace transaction occurs, EventBridge sends events to your default event bus. Your role as either a manufacturer or proposer determines which events you receive.


| Event name | Initiated by | Response | Recipient | 
| --- | --- | --- | --- | 
| Purchase Agreement Created - Manufacturer / Purchase Agreement Created - Proposer | A new agreement is created, an existing agreement is replaced, or an existing agreement is renewed. | Purchase agreement is recorded and post-sale actions taken. Use the DescribeAgreement API to retrieve full agreement details. | Manufacturer and proposer | 
| Purchase Agreement Amended - Manufacturer / Purchase Agreement Amended - Proposer | An existing agreement is amended. | Purchase agreement record is updated. | Manufacturer and proposer | 
| Purchase Agreement Ended - Manufacturer / Purchase Agreement Ended - Proposer | An agreement has expired, is canceled, or is terminated. | Purchase agreement closure is recorded. | Manufacturer and proposer | 
| License Updated - Manufacturer | A customer's license for the product has been provisioned or updated. | Update internal records to reflect the customer's current license state. | Manufacturer only | 
| License Deprovisioned - Manufacturer | A customer's license for the product is being revoked. | Update internal records to reflect that the customer no longer has an active license. | Manufacturer only | 

**Note**  
License events are only sent for container agreements that have an associated license.  
AWS handles metering automatically for container products – you do not need to take any action in response to these events to fulfill customer entitlements. Use license events to keep your internal records current with the customer's active license state.

**Note**  
Purchase agreement event types for manufacturer and proposer are nearly identical, except for the presence of a resaleAuthorization ID. To avoid redundant messages, only the proposer purchase agreement event is sent when you are both the manufacturer and proposer.

For the full list of event types and their detailed schemas, see [Amazon EventBridge events](notifications-eventbridge.md) in the Seller Guide.

## Integrate EventBridge with your container product
<a name="container-eventbridge-using"></a>

Use EventBridge to track agreement lifecycle events for your container listing in AWS Marketplace.
+ **Event rules** define how to react to an event.
+ **Event patterns** are defined in the event rules and let you filter for specific event types sent to your default event bus. Pattern templates for each event type are available in the EventBridge console. In the Event pattern configuration step, select AWS services as the event source and AWS Marketplace Agreements and Licenses as the AWS service.
+ All AWS Marketplace Agreements and Licenses event types use the following structure:

  ```
  {
    "detail-type": ["e.g. Purchase Agreement Ended - Manufacturer"],
    "source": ["aws.agreement-marketplace"]
  }
  ```
+ **Targets** are resources that receive events when they match the event pattern defined for a rule. Many AWS services integrate with EventBridge and can serve as targets, including AWS Lambda functions, AWS Step Functions, and Amazon API Gateway.

For more information about setting up EventBridge rules, see [Getting started: Create an Amazon EventBridge event bus rule](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html).