

# Cancellation and billing adjustment events
<a name="cancellation-adjustment-eventbridge"></a>

AWS Marketplace sends notifications to Amazon EventBridge when a seller initiates a cancellation request or billing adjustment for one of your agreements. You can use these events to automate workflows and track cancellation and refund activity.

The following table lists the buyer events that AWS Marketplace sends to EventBridge for cancellations and billing adjustments:


| Event | Description | 
| --- | --- | 
| Agreement Cancellation Request Pending Approval - Acceptor | Sent when a seller submits a cancellation request for your agreement. Action required: you have 7 days to approve or deny. | 
| Agreement Cancellation Request Approved - Acceptor | Sent when a cancellation request is approved by you or auto-approved after 7 days | 
| Agreement Cancellation Request Rejected - Acceptor | Sent when you deny a cancellation request | 
| Agreement Cancellation Request Cancelled - Acceptor | Sent when the seller withdraws a cancellation request | 
| Purchase Agreement Billing Adjustment Completed - Acceptor | Sent when a billing adjustment (refund) for your agreement is processed | 

All events are sent to your default EventBridge event bus in the `us-east-1` region with the event source `aws.agreement-marketplace`.

## Cancellation request event types
<a name="cancellation-event-types"></a>

### Agreement Cancellation Request Pending Approval - Acceptor
<a name="cancellation-pending-approval-acceptor"></a>

AWS Marketplace sends this event when a seller submits a cancellation request for one of your agreements. You have 7 days to approve or deny the request. If you don't respond, the cancellation is automatically approved.

**Event schema:**

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Agreement Cancellation Request Pending Approval - Acceptor",
  "source": "aws.agreement-marketplace",
  "account": "123456789012",
  "time": "2025-01-01T13:12:22Z",
  "region": "us-east-1",
  "resources": [],
  "detail": {
    "requestId": "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "catalog": "AWSMarketplace",
    "agreement": {
      "id": "agmt-abcdexampleid",
      "proposerId": "123456789012",
      "productId": "prod-exampleid",
      "offerId": "offer-exampleid"
    },
    "agreementCancellationRequest": {
      "id": "acr-abcdexampleid",
      "reasonCode": "INCORRECT_TERMS_ACCEPTED",
      "reasonMessage": "",
      "statusCode": "PENDING_APPROVAL",
      "statusMessage": "",
      "createdAt": "2025-01-01T13:12:22Z",
      "updatedAt": "2025-01-01T13:12:22Z"
    }
  }
}
```

### Agreement Cancellation Request Approved - Acceptor
<a name="cancellation-approved-acceptor"></a>

AWS Marketplace sends this event when a cancellation request for one of your agreements is approved. This can happen when you approve the request or when it is auto-approved after 7 days without a response.

**Event schema:**

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Agreement Cancellation Request Approved - Acceptor",
  "source": "aws.agreement-marketplace",
  "account": "123456789012",
  "time": "2025-01-01T13:16:07Z",
  "region": "us-east-1",
  "resources": [],
  "detail": {
    "requestId": "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "catalog": "AWSMarketplace",
    "agreement": {
      "id": "agmt-abcdexampleid",
      "proposerId": "123456789012",
      "productId": "prod-exampleid",
      "offerId": "offer-exampleid"
    },
    "agreementCancellationRequest": {
      "id": "acr-abcdexampleid",
      "reasonCode": "INCORRECT_TERMS_ACCEPTED",
      "reasonMessage": "The terms accepted in agreement had wrong rate",
      "statusCode": "APPROVED",
      "statusMessage": "",
      "createdAt": "2025-01-01T13:12:22Z",
      "updatedAt": "2025-01-01T13:16:07Z"
    }
  }
}
```

### Agreement Cancellation Request Rejected - Acceptor
<a name="cancellation-rejected-acceptor"></a>

AWS Marketplace sends this event when you deny a cancellation request for one of your agreements.

**Event schema:**

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Agreement Cancellation Request Rejected - Acceptor",
  "source": "aws.agreement-marketplace",
  "account": "123456789012",
  "time": "2025-01-02T10:30:00Z",
  "region": "us-east-1",
  "resources": [],
  "detail": {
    "requestId": "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "catalog": "AWSMarketplace",
    "agreement": {
      "id": "agmt-abcdexampleid",
      "proposerId": "123456789012",
      "productId": "prod-exampleid",
      "offerId": "offer-exampleid"
    },
    "agreementCancellationRequest": {
      "id": "acr-abcdexampleid",
      "reasonCode": "INCORRECT_TERMS_ACCEPTED",
      "reasonMessage": "",
      "statusCode": "REJECTED",
      "statusMessage": "We still need this product",
      "createdAt": "2025-01-01T13:12:22Z",
      "updatedAt": "2025-01-02T10:30:00Z"
    }
  }
}
```

### Agreement Cancellation Request Cancelled - Acceptor
<a name="cancellation-cancelled-acceptor"></a>

AWS Marketplace sends this event when the seller withdraws a cancellation request before you respond.

**Event schema:**

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Agreement Cancellation Request Cancelled - Acceptor",
  "source": "aws.agreement-marketplace",
  "account": "123456789012",
  "time": "2025-01-02T08:00:00Z",
  "region": "us-east-1",
  "resources": [],
  "detail": {
    "requestId": "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "catalog": "AWSMarketplace",
    "agreement": {
      "id": "agmt-abcdexampleid",
      "proposerId": "123456789012",
      "productId": "prod-exampleid",
      "offerId": "offer-exampleid"
    },
    "agreementCancellationRequest": {
      "id": "acr-abcdexampleid",
      "reasonCode": "INCORRECT_TERMS_ACCEPTED",
      "reasonMessage": "",
      "statusCode": "CANCELLED",
      "statusMessage": "Seller withdrew the request",
      "createdAt": "2025-01-01T13:12:22Z",
      "updatedAt": "2025-01-02T08:00:00Z"
    }
  }
}
```

## Billing adjustment event types
<a name="billing-adjustment-event-types"></a>

### Purchase Agreement Billing Adjustment Completed - Acceptor
<a name="billing-adjustment-successful-acceptor"></a>

AWS Marketplace sends this event when a billing adjustment (refund) for one of your agreements is processed.

**Event schema:**

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Purchase Agreement Billing Adjustment Completed - Acceptor",
  "source": "aws.agreement-marketplace",
  "account": "123456789012",
  "time": "2025-01-01T14:00:00Z",
  "region": "us-east-1",
  "resources": [],
  "detail": {
    "requestId": "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "catalog": "AWSMarketplace",
    "agreement": {
      "id": "agmt-abcdexampleid"
    },
    "billingAdjustmentRequest": {
      "id": "ba-abcdexampleid",
      "adjustmentAmount": "-1000.00",
      "currencyCode": "USD",
      "adjustmentReasonCode": "INCORRECT_TERMS_ACCEPTED"
    },
    "invoice": {
      "originalInvoiceId": "2028746221"
    }
  }
}
```

For more information about responding to cancellation requests and tracking billing adjustments, see [Refunds and cancellations in AWS Marketplace](buyer-refunds.md).