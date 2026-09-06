

# Amazon EventBridge notifications for AWS Marketplace events
<a name="buyer-notifications-eventbridge"></a>

AWS Marketplace is integrated with Amazon EventBridge, formerly called Amazon CloudWatch Events. EventBridge is an event bus service that you use to connect your applications with data from a variety of sources. For more information, see the [*Amazon EventBridge User Guide*](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).

AWS Marketplace sends the following types of EventBridge events:
+ [Private offer events](buyer-eventbridge.md) – Buyers receive an event from AWS Marketplace every time a seller creates a private offer and makes it available to your AWS account. The event contains details such the product ID, expiration date, product details, and the seller's name. 
+ [Private marketplace events](pmp-eventbridge.md) – Private marketplace administrators and buyers receive events from AWS Marketplace every time a buyer creates a product request, and when the request is approved or declined. The events contain details like the product details and the seller's name.
+ [Agreement events](agreement-eventbridge.md) – AWS Marketplace sends notifications to Amazon EventBridge when certain events occur during the lifecycle of your agreements (i.e. offers you have purchased). The events contain details like the Agreement ID, Offer ID, and the state of your Agreement.
+ [Cancellation and billing adjustment events](cancellation-adjustment-eventbridge.md) – AWS Marketplace sends notifications to Amazon EventBridge when a seller initiates a cancellation request or billing adjustment (refund) for one of your agreements.

**Note**  
For information on creating EventBridge rules, see [Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) in the *Amazon EventBridge User Guide*.