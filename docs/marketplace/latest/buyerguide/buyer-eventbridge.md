# AWS Marketplace private offer Amazon EventBridge events

As a buyer, you receive an _event_ from AWS Marketplace every time
a seller creates a private offer and makes it available to your AWS account. The event contains details such
as the seller ID, expiration date, product details, and the seller's name.

This topic provides detailed information about the event listed in the following table.

| Action by seller                                                   | Event received by buyer   | More information                                                                              |
| ------------------------------------------------------------------ | ------------------------- | --------------------------------------------------------------------------------------------- |
| Creates a private offer and makes it available to your AWS account | `Private Offer Available` | [Event for new private offers](#events-privateofferavailable "#events-privateofferavailable") |

## Event for new private offers

When a seller creates a private offer and makes it available to your AWS account, the buyer receives
an event with the `Private Offer Available` detail type.

The following example shows the event body for a `Private Offer Available`
event.

```
{
    "version": "0",
    "id": "`01234567-0123-0123-0123-0123456789ab`",
    "detail-type": "Private Offer Available",
    "source": "aws.discovery-marketplace",
    "account": "`123456789012`",
    "time": "`2023-08-26T00:00:00Z`",
    "region": "us-east-1",
    "resources": [],
    "detail": {
        "requestId": "`3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb`",
        "catalog": "AWSMarketplace",
        "offer": {
            "id": "offer-`1234567890123`",
            "name": "`Offer Name`",
            "publishDate": "`2023-08-26T00:00:00Z`",
            "expirationDate": "`2025-08-26T00:00:00Z`"
        },
        "product": {
            "id": "`bbbbaaaa-abcd-1111-abcd-666666666666`",
            "title": "`Product Title`"
        },
        "sellerOfRecord": {
            "name": "`Seller Name`"
        }
    }
}
```

## Setting Up EventBridge Rules

To receive these notifications, create EventBridge rules that match the event patterns for buyer events.
For more information about creating rules, see [Creating Amazon EventBridge rules](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md") in the _Amazon EventBridge User Guide_.

To find this event when building an event pattern in the Amazon EventBridge console:

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/") and choose **Create rule**.
2. On the **Build event pattern** page, for **Event source**, choose **AWS services**.
3. For **AWS service**, choose **AWS Marketplace Discovery**.
4. For **Event type**, choose **Private Offer Available**.
