

# Amazon EventBridge notifications for AWS Marketplace events

AWS Marketplace is integrated with Amazon EventBridge, formerly called Amazon CloudWatch Events. EventBridge is an event bus service that you use to connect your applications with data from a variety of sources. For more information, see the [*Amazon EventBridge User Guide*](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).

AWS Marketplace sends the following types of EventBridge events:
+ [Private offer events](buyer-eventbridge.md) – Buyers receive an event from AWS Marketplace every time a seller creates a private offer and makes it available to your AWS account. The event contains details such the product ID, expiration date, product details, and the seller's name. 
+ [Private marketplace events](pmp-eventbridge.md) – Private marketplace administrators and buyers receive events from AWS Marketplace every time a buyer creates a product request, and when the request is approved or declined. The events contain details like the product details and the seller's name.
+ [Agreement events](agreement-eventbridge.md) – AWS Marketplace sends notifications to Amazon EventBridge when certain events occur during the lifecycle of your agreements (i.e. offers you have purchased). The events contain details like the Agreement ID, Offer ID, and the state of your Agreement.
+ [Cancellation and billing adjustment events](cancellation-adjustment-eventbridge.md) – AWS Marketplace sends notifications to Amazon EventBridge when a seller initiates a cancellation request or billing adjustment (refund) for one of your agreements.
+ [Buyer approval events](buyer-approval-eventbridge.md) – AWS Marketplace sends notifications to Amazon EventBridge when a purchase approval request needs review, and when a request is declined, expires, or is approved but the agreement can't be created.

These events are sent for all product types, including RTB Fabric module products. Agreement events are sent in the US East (N. Virginia) Region. For contract agreements with auto-renewal, the *Purchase Agreement Ending - Acceptor* event is sent 180, 120, 90, 60, and 30 days before the end date.

**Note**  
For information on creating EventBridge rules, see [Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) in the *Amazon EventBridge User Guide*.