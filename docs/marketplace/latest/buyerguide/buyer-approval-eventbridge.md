

# Buyer approval events

When your organization requires approval for purchases, AWS Marketplace sends notifications to Amazon EventBridge. You receive an event when an approval request needs a decision, and when a request ends without an agreement. You can use these events to alert your reviewers, track approval requests in your own systems, and follow up on purchases that weren't completed. For more information about buyer approvals, see [Configuring buyer approvals](buyer-approvals.md).

The following table lists the buyer approval events that AWS Marketplace sends to EventBridge.


| Event | Description | 
| --- | --- | 
| Agreement Approval Request Action Required - Approver | Sent when an approval level that an AWS account reviews becomes ready for review. Action required: review the request before it expires. | 
| Agreement Approval Request Rejected - Acceptor | Sent to your account when an approver declines your approval request | 
| Agreement Approval Request Expired - Acceptor | Sent to your account when your approval request expires before all required approvers approve it | 
| Agreement Creation Failed - Acceptor | Sent to your account when all required approvers approve your request but AWS Marketplace can't create the agreement | 

All events are sent to your default EventBridge event bus in the `us-east-1` region with the event source `aws.agreement-marketplace`. EventBridge events are delivered only to AWS accounts. Email approvers and external procurement systems don't receive them.

## Buyer approval event fields
<a name="buyer-approval-event-fields"></a>

The `detail` object of each buyer approval event contains the following fields. The table notes the fields that apply to only some events.


| Field | Description | 
| --- | --- | 
| requestId | A unique identifier for the notification. If you receive the same requestId more than once, treat it as one event. | 
| catalog | The catalog. The value is AWSMarketplace. | 
| agreementRequest.id | The ID of the agreement request that the buyer submitted. | 
| offer.id | The ID of the offer that the buyer is purchasing. | 
| agreementApproval.id | The ID of the approval request. | 
| agreementApproval.createdAt | When the approval request was created, in ISO 8601 format. | 
| agreementApproval.expiresAt | When the approval request expires, in ISO 8601 format. Included in the action required and expired events. If the private offer expires earlier, you must complete the approval before the offer expires. | 
| agreementApproval.declineReason | The reason the approver entered when declining the request. Included in the rejected event when the approver entered a reason. | 
| agreementApproval.reasonCode | Why AWS Marketplace couldn't create the agreement. Included in the agreement creation failed event. Valid values: OFFER\_EXPIRED, OFFER\_SUPERSEDED, MISSING\_PURCHASE\_ORDER\_REFERENCE, MISSING\_USAGE\_AGREEMENT, and OTHER. New values might be added. Treat a value that you don't recognize like OTHER. | 
| product.id | The ID of the product. | 
| product.title | The name of the product, when available. | 
| proposer.accountId | The AWS account ID of the seller that made the offer. | 
| proposer.name | The name of the seller, when available. | 
| acceptor.accountId | The AWS account ID of the buyer that submitted the purchase. | 
| declinedBy.emailAddress | The email address of the approver who declined the request. Included in the rejected event when it's available. This field contains personal data, so handle it accordingly in the targets and logs that receive the event. | 

## Buyer approval event types
<a name="buyer-approval-event-types"></a>

### Agreement Approval Request Action Required - Approver
<a name="buyer-approval-action-required-approver"></a>

AWS Marketplace sends this event when a level in an approval chain becomes ready for review. The event goes to the AWS accounts that review the level. For example, your management account or a delegated administrator account. Levels that are reviewed by email approvers or by an external procurement system don't produce this event.

Review the request in the AWS Marketplace console before the time in `agreementApproval.expiresAt`. If no decision is made by then, the request expires and the purchase is blocked. If the private offer expires before that time, complete the approval before the offer expires. Otherwise, AWS Marketplace can't create the agreement, and the buyer receives an Agreement Creation Failed event with the reason code `OFFER_EXPIRED`.

**Event schema:**

```
{
  "version": "0",
  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
  "detail-type": "Agreement Approval Request Action Required - Approver",
  "source": "aws.agreement-marketplace",
  "account": "123456789012",
  "time": "2025-01-01T13:12:22Z",
  "region": "us-east-1",
  "resources": [],
  "detail": {
    "requestId": "b2c3d4e5-6789-01bc-def0-EXAMPLE22221",
    "catalog": "AWSMarketplace",
    "agreementRequest": {
      "id": "ar-abcdexampleid"
    },
    "offer": {
      "id": "offer-exampleid"
    },
    "agreementApproval": {
      "id": "apr-abcdexampleid",
      "expiresAt": "2025-01-15T13:12:22Z",
      "createdAt": "2025-01-01T13:12:22Z"
    },
    "product": {
      "id": "prod-exampleid",
      "title": "Example Product"
    },
    "proposer": {
      "accountId": "111122223333",
      "name": "Example Seller"
    },
    "acceptor": {
      "accountId": "444455556666"
    }
  }
}
```

### Agreement Approval Request Rejected - Acceptor
<a name="buyer-approval-rejected-acceptor"></a>

AWS Marketplace sends this event to the buyer when an approver declines the approval request. The request's status shows as **Declined**, and AWS Marketplace doesn't create an agreement. If the approver entered a reason, it's in `agreementApproval.declineReason`. For questions, contact your AWS Marketplace administrator.

**Event schema:**

```
{
  "version": "0",
  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11112",
  "detail-type": "Agreement Approval Request Rejected - Acceptor",
  "source": "aws.agreement-marketplace",
  "account": "123456789012",
  "time": "2025-01-03T09:30:00Z",
  "region": "us-east-1",
  "resources": [],
  "detail": {
    "requestId": "b2c3d4e5-6789-01bc-def0-EXAMPLE22222",
    "catalog": "AWSMarketplace",
    "agreementRequest": {
      "id": "ar-abcdexampleid"
    },
    "offer": {
      "id": "offer-exampleid"
    },
    "agreementApproval": {
      "id": "apr-abcdexampleid",
      "declineReason": "Budget not approved for this quarter",
      "createdAt": "2025-01-01T13:12:22Z"
    },
    "product": {
      "id": "prod-exampleid",
      "title": "Example Product"
    },
    "proposer": {
      "accountId": "111122223333",
      "name": "Example Seller"
    },
    "acceptor": {
      "accountId": "123456789012"
    },
    "declinedBy": {
      "emailAddress": "mary_major@example.com"
    }
  }
}
```

### Agreement Approval Request Expired - Acceptor
<a name="buyer-approval-expired-acceptor"></a>

AWS Marketplace sends this event to the buyer when the approval request expires before all required approvers approve it. AWS Marketplace doesn't create an agreement. You can submit another request, or contact your AWS Marketplace administrator for next steps.

**Event schema:**

```
{
  "version": "0",
  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11113",
  "detail-type": "Agreement Approval Request Expired - Acceptor",
  "source": "aws.agreement-marketplace",
  "account": "123456789012",
  "time": "2025-01-15T13:12:22Z",
  "region": "us-east-1",
  "resources": [],
  "detail": {
    "requestId": "b2c3d4e5-6789-01bc-def0-EXAMPLE22223",
    "catalog": "AWSMarketplace",
    "agreementRequest": {
      "id": "ar-abcdexampleid"
    },
    "offer": {
      "id": "offer-exampleid"
    },
    "agreementApproval": {
      "id": "apr-abcdexampleid",
      "expiresAt": "2025-01-15T13:12:22Z",
      "createdAt": "2025-01-01T13:12:22Z"
    },
    "product": {
      "id": "prod-exampleid",
      "title": "Example Product"
    },
    "proposer": {
      "accountId": "111122223333",
      "name": "Example Seller"
    },
    "acceptor": {
      "accountId": "123456789012"
    }
  }
}
```

### Agreement Creation Failed - Acceptor
<a name="buyer-approval-creation-failed-acceptor"></a>

AWS Marketplace sends this event to the buyer when all required approvers approve the request, but AWS Marketplace can't create the agreement. The `agreementApproval.reasonCode` field says why:
+ `OFFER_EXPIRED` – The private offer expired before the approval process was complete. Ask the seller to extend the private offer expiration date, and then accept the offer.
+ `OFFER_SUPERSEDED` – The seller updated the offer, or the offer is no longer available. Cancel the request, and then create a new request from the seller's current offer. The new request needs approval again. If there is no current offer, contact the seller.
+ `MISSING_PURCHASE_ORDER_REFERENCE` – The purchase needs a purchase order, and the request didn't include one. Accept the offer, and then provide a purchase order for each charge that requires one.
+ `MISSING_USAGE_AGREEMENT` – The annual subscription needs an active usage agreement on the same offer, and you don't have one. Subscribe to the usage-based pricing on the same offer, and then accept the annual terms.
+ `OTHER` – AWS Marketplace couldn't create the agreement for another reason. Review the request, and then accept the offer. If you can't accept it, contact AWS Support.

**Event schema:**

```
{
  "version": "0",
  "id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11114",
  "detail-type": "Agreement Creation Failed - Acceptor",
  "source": "aws.agreement-marketplace",
  "account": "123456789012",
  "time": "2025-01-05T10:00:00Z",
  "region": "us-east-1",
  "resources": [],
  "detail": {
    "requestId": "b2c3d4e5-6789-01bc-def0-EXAMPLE22224",
    "catalog": "AWSMarketplace",
    "agreementRequest": {
      "id": "ar-abcdexampleid"
    },
    "offer": {
      "id": "offer-exampleid"
    },
    "agreementApproval": {
      "id": "apr-abcdexampleid",
      "reasonCode": "OFFER_EXPIRED",
      "createdAt": "2025-01-01T13:12:22Z"
    },
    "product": {
      "id": "prod-exampleid",
      "title": "Example Product"
    },
    "proposer": {
      "accountId": "111122223333",
      "name": "Example Seller"
    },
    "acceptor": {
      "accountId": "123456789012"
    }
  }
}
```