# Amazon EventBridge notifications for AWS Marketplace events

AWS Marketplace is integrated with Amazon EventBridge, formerly called Amazon CloudWatch Events. EventBridge is an event bus service
that you use to connect your applications with data from a variety of sources. For more
information, see the [_Amazon EventBridge User
Guide_](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md").

AWS Marketplace sends the following types of EventBridge events:

- [Discovery API events](buyer-eventbridge.md "buyer-eventbridge.md") – Buyers receive an event
  from AWS Marketplace every time a seller creates an offer and makes it available for purchase. The
  event contains details such the product ID, expiration date, product details, and the
  seller's name.
- [Private marketplace events](pmp-eventbridge.md "pmp-eventbridge.md") – Private
  marketplace administrators and buyers receive events from AWS Marketplace every time a buyer creates a
  product request, and when the request is approved or declined. The events contain details
  like the product details and the seller's name.
- [Agreement events](agreement-eventbridge.md "agreement-eventbridge.md") – AWS Marketplace sends notifications
  to Amazon EventBridge when certain events occur during the lifecycle of your agreements (i.e. offers you have purchased).
  The events contain details like the Agreement ID, Offer ID, and the state of your Agreement.

###### Note

For information on creating EventBridge rules, see [Amazon EventBridge rules](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md") in the
_Amazon EventBridge User Guide_.
