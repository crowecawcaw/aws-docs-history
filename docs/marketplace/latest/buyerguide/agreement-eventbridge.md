# AWS Marketplace Agreement EventBridge Events

AWS Marketplace sends notifications to Amazon EventBridge when certain events occur in the lifecycle of your agreements
(i.e. offers you have purchased). You can use these events to automate workflows and track your
marketplace purchases.

The following table lists the buyer events that AWS Marketplace sends to EventBridge:

| Event                                    | Description                                                                            |
| ---------------------------------------- | -------------------------------------------------------------------------------------- |
| Purchase Agreement Created<br>• Acceptor | Sent when a new purchase agreement is created, renewed, or replaced in your account    |
| Purchase Agreement Amended<br>• Acceptor | Sent when modifications are made to an existing purchase agreement                     |
| Purchase Agreement Ended<br>• Acceptor   | Sent when a purchase agreement is cancelled, expired, terminated, renewed, or replaced |
| Purchase Agreement Ending<br>• Acceptor  | Sent 30, 60, and 90 days before a purchase agreement expires                           |

## Overview

Buyers receive EventBridge notifications for the following purchase agreement lifecycle events:

- Agreement creation
- Agreement amendments
- Agreement ends (cancellation, expiration, or termination)
- Agreement ending

All events are sent to your default EventBridge event bus in the `us-east-1` region with
the event source `aws.agreement-marketplace`.

## Event Types

### Purchase Agreement Created - Acceptor

AWS Marketplace sends this event when a new purchase agreement is created in your account.

**Triggering scenarios:**

- `NEW` - The agreement is created for the first time
- `REPLACE` - A new private offer needs to be accepted as part of an Agreement-Based Offer (ABO)
- `RENEW` - An agreement is auto-renewed at expiry (if enabled)

**Event schema:**

```
{
  "version": "0",
  "id": "abcd1234-5678-90ef-ghij-klmnopqrstuv",
  "detail-type": "Purchase Agreement Created - Acceptor",
  "source": "aws.agreement-marketplace",
  "account": "<Buyer Account ID>",
  "time": "2024-08-30T21:36:03Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace::agreement:agmt-9xyz8wmklp67rt32nb1qv45ds"
  ],
  "detail": {
    "requestId": "7f3e2d1c-a9b8-4f5e-6d7c-1234567890ab",
    "catalog": "AWSMarketplace",
    "agreement": {
      "id": "agmt-9xyz8wmklp67rt32nb1qv45ds",
      "intent": "NEW|RENEW|REPLACE",
      "status": "ACTIVE",
      "acceptanceTime": "2024-06-26T21:36:03Z",
      "startTime": "2024-08-30T21:36:03Z",
      "endTime": "2025-05-30T21:36:03Z"
    },
    "acceptor": {
      "accountId": "<Buyer Account ID>"
    },
    "proposer": {
      "accountId": "<Proposer Account ID>"
    },
    "offer": {
      "id": "offer-abcdef123456"
    }
  }
}
```

### Purchase Agreement Amended - Acceptor

AWS Marketplace sends this event when modifications are made to an existing purchase agreement, such as changes to terms, pricing, or other agreement parameters.

**Event schema:**

```
{
  "version": "0",
  "id": "12345678-1234-1234-1234-123456789012",
  "detail-type": "Purchase Agreement Amended Acceptor",
  "source": "aws.agreement-marketplace",
  "account": "<Buyer Account ID>",
  "time": "2024-08-30T21:36:03Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace::aws:agreement:agmt-4mwg1nevbokzw95eca5797ixs"
  ],
  "detail": {
    "requestId": "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "catalog": "AWSMarketplace",
    "agreement": {
      "id": "agmt-4mwg1nevbokzw95eca5797ixs",
      "intent": "AMEND",
      "status": "ACTIVE",
      "acceptanceTime": "2024-06-26T21:36:03Z",
      "startTime": "2024-08-30T21:36:03Z",
      "endTime": "2025-05-30T21:36:03Z"
    },
    "acceptor": {
      "accountId": "<Buyer Account ID>"
    },
    "proposer": {
      "accountId": "<Proposer Account ID>"
    },
    "offer": {
      "id": "offer-1234567890123"
    }
  }
}
```

### Purchase Agreement Ended - Acceptor

AWS Marketplace sends this event when a purchase agreement ends.

**Triggering scenarios:**

- `CANCELLED` - You ended the agreement before the defined end date
- `EXPIRED` - The agreement reached its defined end date
- `TERMINATED` - AWS terminated the agreement (for example, due to a payment failure)
- `RENEWED` - The agreement was renewed into a new agreement
- `REPLACED` - The agreement was replaced using an agreement replacement offer

**Event schema:**

```
{
  "version": "0",
  "id": "abcd1234-5678-90ef-ghij-klmnopqrstuv",
  "detail-type": "Purchase Agreement Ended - Acceptor",
  "source": "aws.agreement-marketplace",
  "account": "987654321098",
  "time": "2024-08-30T21:36:03Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace:aws:agreement:agmt-9xyz8wmklp67rt32nb1qv45ds"
  ],
  "detail": {
    "requestId": "7f3e2d1c-a9b8-4f5e-6d7c-1234567890ab",
    "catalog": "AWSMarketplace",
    "agreement": {
      "id": "agmt-9xyz8wmklp67rt32nb1qv45ds",
      "status": "CANCELLED|EXPIRED|RENEWED|REPLACED|TERMINATED"
    },
    "acceptor": {
      "accountId": "<Buyer Account ID>"
    },
    "proposer": {
      "accountId": "<Proposer Account ID>"
    },
    "offer": {
      "id": "offer-abcdef123456"
    }
  }
}
```

### Purchase Agreement Ending - Acceptor

AWS Marketplace sends this event 30, 60, and 90 days before a purchase agreement expires.

This event includes additional fields not present in other buyer events:

- `agreement.autoRenewalEnabled` - Indicates whether auto-renewal is enabled for the agreement
- `product.id` and `product.title` - Product information for the agreement
- `proposer.name` and `offer.name` - Human-readable names for the seller and offer

**Event schema:**

```
{
  "version": "0",
  "id": "abcd1234-5678-90ef-ghij-klmnopqrstuv",
  "detail-type": "Purchase Agreement Ending - Acceptor",
  "source": "aws.agreement-marketplace",
  "account": "<Buyer Account ID>",
  "time": "2025-03-31T21:36:03Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace::aws:agreement:agmt-9xyz8wmklp67rt32nb1qv45ds"
  ],
  "detail": {
    "requestId": "7f3e2d1c-a9b8-4f5e-6d7c-1234567890ab",
    "catalog": "AWSMarketplace",
    "agreement": {
      "id": "agmt-9xyz8wmklp67rt32nb1qv45ds",
      "startTime": "2024-08-30T21:36:03Z",
      "endTime": "2025-05-30T21:36:03Z",
      "autoRenewalEnabled": true,
      "status": "ACTIVE"
    },
    "product": {
      "id": "prod-abc123xyz456",
      "title": "Example Product Title"
    },
    "acceptor": {
      "accountId": "<Buyer Account ID>"
    },
    "proposer": {
      "name": "Example Seller Name",
      "accountId": "<Proposer Account ID>"
    },
    "offer": {
      "id": "offer-abcdef123456",
      "name": "Example Offer Name"
    }
  }
}
```

## Common Event Fields

All buyer events include these common fields:

| Field                | Description                                              |
| -------------------- | -------------------------------------------------------- |
| `requestId`          | UUID used to deduplicate duplicate events                |
| `catalog`            | The AWS Marketplace catalog (typically "AWSMarketplace") |
| `agreementId`        | Unique identifier for the agreement                      |
| `acceptor.accountId` | Your AWS account ID                                      |
| `proposer.accountId` | The seller's AWS account ID                              |
| `offer.id`           | The offer identifier                                     |

## Setting Up EventBridge Rules

To receive these notifications, create EventBridge rules that match the event patterns for buyer events.
For more information about creating rules, see [Creating Amazon EventBridge rules](../../../eventbridge/latest/userguide/eb-create-rule.md "../../../eventbridge/latest/userguide/eb-create-rule.md") in the _Amazon EventBridge User Guide_.
