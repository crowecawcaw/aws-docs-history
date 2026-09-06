

# AWS Marketplace Agreement EventBridge Events
<a name="agreement-eventbridge"></a>

AWS Marketplace sends notifications to Amazon EventBridge when certain events occur in the lifecycle of your agreements (i.e. offers you have purchased). You can use these events to automate workflows and track your marketplace purchases.

**Note**  
In the AWS Marketplace console, this date is called the renewal decision deadline – the last day you can turn auto-renewal off (or back on) before the renewal is confirmed. In these events it is represented by the lockout fields: `renewalSummary.lockoutStartTime` is when that period ends, and `renewalSummary.lockoutReached` indicates whether the period has started.

The following table lists the buyer events that AWS Marketplace sends to EventBridge:


| Event | Description | 
| --- | --- | 
| Purchase Agreement Created - Acceptor | Sent when a new purchase agreement is created, renewed, or replaced in your account | 
| Purchase Agreement Amended - Acceptor | Sent when modifications are made to an existing purchase agreement | 
| Purchase Agreement Ended - Acceptor | Sent when a purchase agreement is cancelled, expired, terminated, renewed, or replaced | 
| Purchase Agreement Ending - Acceptor | Sent 180, 120, 90, 60, and 30 days before a purchase agreement expires | 
| Purchase Agreement Renewal Terms Finalized - Acceptor | Sent after the seller's adjustment deadline passes, for percentage-range renewals, once the renewal price uplift is finalized (or the default uplift is applied) | 
| Purchase Agreement Renewal Upcoming - Acceptor | Sent when the renewal decision deadline is reached and the renewal is confirmed to proceed | 

## Overview
<a name="agreement-events-overview"></a>

Buyers receive EventBridge notifications for the following purchase agreement lifecycle events:
+ Agreement creation
+ Agreement amendments
+ Agreement ends (cancellation, expiration, or termination)
+ Agreement ending

All events are sent to your default EventBridge event bus in the `us-east-1` region with the event source `aws.agreement-marketplace`.

## Event Types
<a name="agreement-event-types"></a>

### Purchase Agreement Created - Acceptor
<a name="agreement-created-event"></a>

AWS Marketplace sends this event when a new purchase agreement is created in your account.

**Triggering scenarios:**
+ `NEW` - The agreement is created for the first time
+ `REPLACE` - A new private offer needs to be accepted as part of an Agreement-Based Offer (ABO)
+ `RENEW` - An agreement is auto-renewed at expiry (if enabled)

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

For an auto-renewal, AWS Marketplace sends this event with `intent` set to `RENEW`. The event includes `agreement.previousAgreementId`, a `product` block, `proposer.name`, and `offer.name`.

```
{
  "version": "0",
  "id": "abcd1234-5678-90ef-ghij-klmnopqrstuv",
  "detail-type": "Purchase Agreement Created - Acceptor",
  "source": "aws.agreement-marketplace",
  "account": "<Buyer Account ID>",
  "time": "2025-05-30T21:36:03Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace::aws:agreement:agmt-newrenewalagreementid"
  ],
  "detail": {
    "requestId": "7f3e2d1c-a9b8-4f5e-6d7c-1234567890ab",
    "catalog": "AWSMarketplace",
    "agreement": {
      "id": "agmt-newrenewalagreementid",
      "intent": "RENEW",
      "status": "ACTIVE",
      "startTime": "2025-05-30T21:36:03Z",
      "endTime": "2026-05-30T21:36:03Z",
      "previousAgreementId": "agmt-9xyz8wmklp67rt32nb1qv45ds"
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

### Purchase Agreement Amended - Acceptor
<a name="agreement-amended-event"></a>

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
      "endTime": "2025-05-30T21:36:03Z",
      "autoRenewalEnabled": true
    },
    "renewalSummary": {
      "lockoutStartTime": "2025-05-20T21:36:03Z",
      "disabledBy": "ACCEPTOR"
    },
    "product": {
      "id": "prod-abc123xyz456",
      "title": "Example Product Title"
    },
    "acceptor": {
      "accountId": "<Buyer Account ID>"
    },
    "proposer": {
      "accountId": "<Proposer Account ID>"
    },
    "offer": {
      "id": "offer-1234567890123",
      "name": "Example Offer Name"
    }
  }
}
```

Buyer opt-in and opt-out, and seller opt-out, are processed as agreement amendments and surface through this event. `renewalSummary.disabledBy` is `ACCEPTOR` or `PROPOSER` (`PROPOSER` if both opted out), or `null` when `autoRenewalEnabled` is `true` or there are no renewal terms. `renewalSummary.lockoutStartTime` is `null` when the renewal term has no lockout period.

### Purchase Agreement Ended - Acceptor
<a name="agreement-ended-event"></a>

AWS Marketplace sends this event when a purchase agreement ends.

**Triggering scenarios:**
+ `CANCELLED` - You ended the agreement before the defined end date
+ `EXPIRED` - The agreement reached its defined end date
+ `TERMINATED` - AWS terminated the agreement (for example, due to a payment failure)
+ `RENEWED` - The agreement was renewed into a new agreement
+ `REPLACED` - The agreement was replaced using an agreement replacement offer

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
<a name="agreement-ending-event"></a>

AWS Marketplace sends this event 180, 120, 90, 60, and 30 days before a purchase agreement expires.

This event includes additional fields not present in other buyer events:
+ `agreement.daysBeforeEndTime` - The number of days before the end date that the notification is sent: 180, 120, 90, 60, or 30
+ `agreement.autoRenewalEnabled` - Indicates whether auto-renewal is enabled for the agreement
+ `renewalSummary` - Renewal lockout details. `renewalSummary.lockoutStartTime` is `null` when the renewal term has no lockout period; `renewalSummary.disabledBy` is `ACCEPTOR` or `PROPOSER` (`PROPOSER` if both opted out), or `null` when auto-renewal is enabled or there are no renewal terms
+ `product.id` and `product.title` - Product information for the agreement
+ `proposer.name` and `offer.name` - Human-readable names for the seller and offer

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
      "daysBeforeEndTime": 180,
      "autoRenewalEnabled": true,
      "status": "ACTIVE"
    },
    "renewalSummary": {
      "lockoutStartTime": "2025-05-20T21:36:03Z",
      "disabledBy": "ACCEPTOR"
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

### Purchase Agreement Renewal Terms Finalized - Acceptor
<a name="agreement-renewal-terms-finalized-event"></a>

AWS Marketplace sends this event after the seller's adjustment deadline passes, for percentage-range offers only, once the renewal price uplift is finalized (or the default uplift is applied).

**Event schema:**

```
{
  "version": "0",
  "id": "abcd1234-5678-90ef-ghij-klmnopqrstuv",
  "detail-type": "Purchase Agreement Renewal Terms Finalized - Acceptor",
  "source": "aws.agreement-marketplace",
  "account": "<Buyer Account ID>",
  "time": "2025-05-15T21:36:03Z",
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
      "endTime": "2025-05-30T21:36:03Z"
    },
    "renewalSummary": {
      "tcv": "105000.00",
      "currency": "USD",
      "termsFinalizedTime": "2025-05-15T21:36:03Z",
      "lockoutReached": false,
      "lockoutStartTime": "2025-05-20T21:36:03Z"
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
    }
  }
}
```

`renewalSummary.lockoutReached` and `lockoutStartTime` are `null` when the accepted renewal term has no lockout period.

### Purchase Agreement Renewal Upcoming - Acceptor
<a name="agreement-renewal-upcoming-event"></a>

AWS Marketplace sends this event at the start of the renewal decision lockout period, when the renewal decision deadline is reached and the renewal is confirmed to proceed.

**Event schema:**

```
{
  "version": "0",
  "id": "abcd1234-5678-90ef-ghij-klmnopqrstuv",
  "detail-type": "Purchase Agreement Renewal Upcoming - Acceptor",
  "source": "aws.agreement-marketplace",
  "account": "<Buyer Account ID>",
  "time": "2025-05-20T21:36:03Z",
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
      "endTime": "2025-05-30T21:36:03Z"
    },
    "renewalSummary": {
      "lockoutReached": true,
      "tcv": "105000.00",
      "currency": "USD"
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
    }
  }
}
```

## Common Event Fields
<a name="agreement-common-fields"></a>

All buyer events include these common fields:


| Field | Description | 
| --- | --- | 
| requestId | UUID used to deduplicate duplicate events | 
| catalog | The AWS Marketplace catalog (typically "AWSMarketplace") | 
| agreementId | Unique identifier for the agreement | 
| acceptor.accountId | Your AWS account ID | 
| proposer.accountId | The seller's AWS account ID | 
| offer.id | The offer identifier | 

## Setting Up EventBridge Rules
<a name="agreement-eventbridge-setup"></a>

To receive these notifications, create EventBridge rules that match the event patterns for buyer events. For more information about creating rules, see [Creating Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html) in the *Amazon EventBridge User Guide*.