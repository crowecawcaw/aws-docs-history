

# Amazon EventBridge events
<a name="notifications-eventbridge"></a>

As a seller, you can use Amazon EventBridge to receive notifications for events in AWS Marketplace. For example, you can receive an *event* from AWS Marketplace when an offer is created. The *event* contains details like the ID, expiration date, and product details. EventBridge is an event bus service that you can use to connect your applications with data from a variety of sources. For more information, see the [*Amazon EventBridge User Guide*](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html). The following sections provide detailed information about events under the Marketplace Catalog service in the EventBridge console.

**Topics**
+ [Events for new offers](#events-offerreleased)
+ [Events for change sets](#events-changesets)
+ [Events for security summary report](#events-security-report)
+ [Events for disbursements](#events-for-disbursements)
+ [Events for agreements](#events-for-agreements)
+ [Events for licenses](#events-for-licenses)
+ [Events for cancellations](#events-for-cancellations)
+ [Events for billing adjustments](#events-for-billing-adjustments)

This topic 


| Action by seller | Event received | Related topic | 
| --- | --- | --- | 
| Independent software vendor (ISV) creates an offer and makes it available for purchase | Offer Released | [Events for new offers](#events-offerreleased) | 
| ISV's product is used by a channel partner to create an offer | Offer Released | [Events for new offers](#events-offerreleased) | 
| Channel partner creates an offer | Offer Released | [Events for new offers](#events-offerreleased) | 
| ISV creates a new offer set | OfferSet Released | [Events for new offers](#events-offerreleased) | 
| Channel partner creates a new offer set | OfferSet Released | [Events for new offers](#events-offerreleased) | 
| Change set succeeds | Change Set Succeeded | [Events for change sets](#events-changesets) | 
| Change set fails | Change Set Failed | [Events for change sets](#events-changesets) | 
| Change set is cancelled | Change Set Cancelled | [Events for change sets](#events-changesets) | 
| Security vulnerabilities were detected on the ISV's product | Products Security Report Created | [Events for security summary report](#events-security-report) | 
| Customer subscribes to an AWS Marketplace product | Purchase Agreement Created | [Events for agreements](#events-for-agreements) | 
| Customer's agreement is amended | Purchase Agreement Amended | [Events for agreements](#events-for-agreements) | 
| Customer cancels their agreement | Purchase Agreement Ended | [Events for agreements](#events-for-agreements) | 
| An advisory is issued that might affect a customer's agreement | Purchase Agreement Advisory Issued | [Events for agreements](#events-for-agreements) | 
| An advisory affecting a customer's agreement is resolved | Purchase Agreement Advisory Resolved | [Events for agreements](#events-for-agreements) | 
| A customer's auto-renewing agreement approaches its end date | Purchase Agreement Ending - Proposer | [Events for agreements](#events-for-agreements) | 
| A customer's renewal price uplift is finalized (percentage-range offers) | Purchase Agreement Renewal Terms Finalized - Proposer | [Events for agreements](#events-for-agreements) | 
| A customer's agreement reaches its lockout date and will auto-renew | Purchase Agreement Renewal Upcoming - Proposer | [Events for agreements](#events-for-agreements) | 
| A customer's agreement auto-renews and a new agreement is created | Purchase Agreement Created - Proposer (intent=RENEW) | [Events for agreements](#events-for-agreements) | 
| A customer's license for a product is provisioned or updated | License Updated | [Events for licenses](#events-for-licenses) | 
| A customer's license for a product is being revoked | License Deprovisioned | [Events for licenses](#events-for-licenses) | 
| Seller submits a cancellation request | Agreement Cancellation Request Pending Approval - Proposer | [Events for cancellations](#events-for-cancellations) | 
| Cancellation request is approved or auto-approved | Agreement Cancellation Request Approved - Proposer | [Events for cancellations](#events-for-cancellations) | 
| Cancellation request is denied by buyer | Agreement Cancellation Request Rejected - Proposer | [Events for cancellations](#events-for-cancellations) | 
| Seller withdraws a cancellation request | Agreement Cancellation Request Cancelled - Proposer | [Events for cancellations](#events-for-cancellations) | 
| Cancellation request fails validation | Agreement Cancellation Request Validation Failed - Proposer | [Events for cancellations](#events-for-cancellations) | 
| Billing adjustment is processed | Purchase Agreement Billing Adjustment Completed - Proposer | [Events for billing adjustments](#events-for-billing-adjustments) | 
| Billing adjustment fails validation | Purchase Agreement Billing Adjustment Failed - Proposer | [Events for billing adjustments](#events-for-billing-adjustments) | 

## Events for new offers
<a name="events-offerreleased"></a>

When sellers create an offer and make it available for purchase, they can receive an event with the following detail type: `Offer Released`. 

**Note**  
For information on creating EventBridge rules, see [Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) in the *Amazon EventBridge User Guide*.

The following is an example event body for a new offer created by an ISV.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Offer Released",
  "source": "aws.marketplacecatalog",
  "account": "123456789012",
  "time": "2023-08-26T00:00:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/Offer/offer-1234567890123"
  ],
  "detail": {
    "requestId": "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "catalog": "AWSMarketplace",
    "offer": {
      "id": "offer-1234567890123",
      "arn": "arn:aws:catalog:us-east-1:123456789012:Offer/offer-1234567890123",
      "name": "Offer Name",
      "expirationDate": "2025-08-26T00:00:00Z"
    },
    "product": {
      "id": "bbbbaaaa-abcd-1111-abcd-666666666666",
      "arn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/SaaSProduct/bbbbaaaa-abcd-1111-abcd-666666666666",
      "title": "Product Title"
    },
    "manufacturer": {
      "accountId": "123456789012",
      "name": "Manufacturer Account Name"
    },
    "sellerOfRecord": {
      "accountId": "123456789012",
      "name": "Seller Account Name"
    },
    "targetedBuyerAccountIds": [
      "999988887777",
      "111122223333"
    ]
  }
}
```

The following is an example event body for when an ISV's product is used by a channel partner to create an offer.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Offer Released",
  "source": "aws.marketplacecatalog",
  "account": "123456789012",
  "time": "2023-08-26T00:00:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace:us-east-1:987654321098:AWSMarketplace/Offer/offer-1234567890123"
  ],
  "detail": {
    "requestId": "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "catalog": "AWSMarketplace",
    "offer": {
      "id": "offer-1234567890123",
      "arn": "arn:aws:catalog:us-east-1:987654321098:Offer/offer-1234567890123",
      "name": "Offer Name",
      "expirationDate": "2025-08-26T00:00:00Z"
    },
    "product": {
      "id": "bbbbaaaa-abcd-1111-abcd-666666666666",
      "arn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/SaaSProduct/bbbbaaaa-abcd-1111-abcd-666666666666",
      "title": "Product Title"
    },
    "manufacturer": {
      "accountId": "123456789012",
      "name": "Manufacturer Account Name"
    },
    "sellerOfRecord": {
      "accountId": "987654321098",
      "name": "Seller Account Name"
    },
    "targetedBuyerAccountIds": ["999988887777", "111122223333"],
    }
  }
}
```

The following is an example event body for when a channel partner creates an offer.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Offer Released",
  "source": "aws.marketplacecatalog",
  "account": "987654321098",
  "time": "2023-08-26T00:00:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace:us-east-1:987654321098:AWSMarketplace/Offer/offer-1234567890123"
  ],
  "detail": {
    "requestId": "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "catalog": "AWSMarketplace",
    "offer": {
      "id": "offer-1234567890123",
      "arn": "arn:aws:catalog:us-east-1:987654321098:Offer/offer-1234567890123",
      "name": "Offer Name",
      "expirationDate": "2025-08-26T00:00:00Z"
    },
    "product": {
      "id": "bbbbaaaa-abcd-1111-abcd-666666666666",
      "arn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/SaaSProduct/bbbbaaaa-abcd-1111-abcd-666666666666",
      "title": "Product Title"
    },
    "manufacturer": {
      "accountId": "123456789012",
      "name": "Manufacturer Account Name"
    },
    "sellerOfRecord": {
      "accountId": "987654321098",
      "name": "Seller Account Name"
    },
    "targetedBuyerAccountIds": ["999988887777", "111122223333"],
    }
  }
}
```

The following is an example event body for a new offer set published by a partners (ISV or Channel partner).

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "OfferSet Released",
  "source": "aws.marketplacecatalog",
  "account": "123456789012",
  "time": "2023-08-26T00:00:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace:us-east-1:987654321098:AWSMarketplace/OfferSet/offerset-1234567890123"
  ],
  "detail": {
    "requestId": "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "catalog": "AWSMarketplace",
    "offerSet": {
      "id": "offerset-1234567890123",
      "arn": "arn:aws:catalog:us-east-1:987654321098:OfferSet/offerset-1234567890123",
      "name": "Offer Set Name",
    },
    "associatedOffers": [
      {
        "offer": {
          "id": "offer-1234567890123",
          "arn": "arn:aws:catalog:us-east-1:987654321098:Offer/offer-1234567890123",
          "name": "Offer Name",
        }
      },
      ...
    ]
  }
}
```

## Events for change sets
<a name="events-changesets"></a>

When a change set completes, sellers, channel partners, and private marketplace administrators can receive an event. The AWS Marketplace Catalog API sends an event when a change set completes with a status of succeeded, failed, or cancelled. The source for these events is `aws.marketplacecatalog`, and the possible detail type values are `Change Set Succeeded`, `Change Set Failed`, and `Change Set Cancelled`.

**Note**  
For information on change sets, see [Working with change sets](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html#working-with-change-sets) in the *AWS Marketplace Catalog API Reference*.

Each event contains change request details, such as the change set ID, change set name, event detail type, failure code (for failed requests), and start and end times of the request. This enables you to monitor your change sets without continuously querying the `DescribeChangeSet` action or checking the AWS Marketplace Management Portal for the status of your change requests.

**Note**  
For information on creating EventBridge rules, see [Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) in the *Amazon EventBridge User Guide*.

The following is an example event body for the `Change Set Succeeded` detail type.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Change Set Succeeded",
  "source": "aws.marketplacecatalog",
  "account": "123456789012",
  "time": "2022-11-01T13:12:22Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/76yesvf8y165pa4f98td2crtg"
  ],
  "detail": {
    "requestId" : "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "Catalog": "AWSMarketplace",
    "ChangeSetId": "76yesvf8y165pa4f98td2crtg",
    "ChangeSetName": "Create my product",
    "StartTime": "2018-02-27T13:45:22Z",
    "EndTime": "2018-02-27T14:55:22Z"
  }
}
```

The following is an example event body for the `Change Set Failed` detail type.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Change Set Failed",
  "source": "aws.marketplacecatalog",
  "account": "123456789012",
  "time": "2022-11-01T13:12:22Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/76yesvf8y165pa4f98td2crtg"
  ],
  "detail": {
    "requestId" : "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "Catalog": "AWSMarketplace",
    "ChangeSetId": "76yesvf8y165pa4f98td2crtg",
    "ChangeSetName": "Create my product",
    "StartTime": "2018-02-27T13:45:22Z",
    "EndTime": "2018-02-27T14:55:22Z",
    "FailureCode": "CLIENT_ERROR"
  }
}
```

The following is an example event body for the `Change Set Cancelled` detail type.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Change Set Cancelled",
  "source": "aws.marketplacecatalog",
  "account": "123456789012",
  "time": "2022-11-01T13:12:22Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/76yesvf8y165pa4f98td2crtg"
  ],
  "detail": {
    "requestId" : "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "Catalog": "AWSMarketplace",
    "ChangeSetId": "76yesvf8y165pa4f98td2crtg",
    "ChangeSetName": "Create my product",
    "StartTime": "2018-02-27T13:45:22Z",
    "EndTime": "2018-02-27T14:55:22Z"
  }
}
```

## Events for security summary report
<a name="events-security-report"></a>

When security vulnerabilities are detected on a seller's products, they can receive a summary report event and periodic reminders for outstanding product issues. The source for these events is `aws.marketplacecatalog`, and the detail type is `Products Security Report Created`.

Each event includes a summary of the count of products and versions with detected issues, a count of how many latest versions are affected, and the date when resolution is required to prevent a temporary restriction of these products or versions.

**Note**  
For information on creating EventBridge rules, see [Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) in the *Amazon EventBridge User Guide*.  
For details on managing security events, see the [How to improve the security of your product catalog in AWS Marketplace](https://aws.amazon.com/blogs/awsmarketplace/how-to-improve-security-your-product-catalog-aws-marketplace/) blog post on the *AWS Blog*.

The following is an example event body for the `Products Security Report Created` detail type.

```
{
  "version": "0",
   "id": "01234567-0123-0123-0123-0123456789ab",
   "detail-type": "Products Security Report Created",
   "source": "aws.marketplacecatalog",
   "account": "123456789012",
   "time": "2023-10-31T00:00:00Z",
   "region": "us-east-1",
   "resources": [],
   "detail": {
     "numberOfProductsWithIssues": 1,
     "numberOfVersionsWithIssues": 1,
     "numberOfLatestVersionsWithIssues": 1,
     "newIssuesFound": true,
     "upcomingResolutionDueDate": "2023-12-01T00:00:00Z",
     "requestId": "533fa17d-3e97-5051-bcaf-1fae45fb3f8b"
   }
  }
```

## Events for disbursements
<a name="events-for-disbursements"></a>

When a disbursement to seller bank account fails due to invalid bank account details, AWS Marketplace ISVs and channel partners may receive an event.

In the following JSON event code, the `source` value for these events is `aws.marketplace`, and the `detail-type` value is `Disbursement Paused`. The `resources` value shows the invalid bank account Amazon Resource Number (ARN).

```
{
"version": "0",
"id": "01234567-0123-0123-0123-0123456789ab", 
"detail-type": "Disbursement Paused",
"source": "aws.marketplace",
"account":"<account id of end user>",
"time": "2022-11-01T13:12:22Z",
"region": "us-east-1",
"resources": ["arn:aws:payments:us-east-1:1234567890:paymentinstrument:123"],
"detail": {
"requestId": "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
"catalog": "AWSMarketplace"
 }
}
```

To resolve the invalid bank account details issue, add your bank account details in AWS Partner Central. For instructions, see [To add bank account details](email-notifications.md#resolve-invalid-bank-account-details). 

For more information about creating Amazon EventBridge rules, see [Rules in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) in the *Amazon EventBridge User Guide*.

## Events for agreements
<a name="events-for-agreements"></a>

When agreement events occur, sellers can receive notifications for purchase agreement lifecycle changes.

For information on creating EventBridge rules, see [Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) in the *Amazon EventBridge User Guide*.

**Note**  
In the AWS Marketplace Management Portal, this date is called the renewal decision deadline – the last day you or the buyer can turn auto-renewal off (or back on) before the renewal is confirmed. In these events it is represented by the lockout fields: `renewalSummary.lockoutStartTime` is when that period ends, and `renewalSummary.lockoutReached` indicates whether the period has started.

The following is an example event body for **Purchase Agreement Created - Proposer**.

**Note**  
Resale Authorization Id in case of Channel Partner Private Offer (CPPO) will be populated, and in case of Marketplace direct offer (MPPO), this value would be null.

```
{
  "version": "0",
  "id": "12345678-1234-1234-1234-123456789012",
  "detail-type": "Purchase Agreement Created - Proposer",
  "source": "aws.agreement-marketplace",
  "account": "<ISV's or CP's account id>",
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
      "intent": "NEW",
      "status": "ACTIVE",
      "acceptanceTime": "2024-06-26T21:36:03Z",
      "startTime": "2024-08-30T21:36:03Z",
      "endTime": "2025-05-30T21:36:03Z"
    },
    "resaleAuthorization": {
      "id": "resaleauthz-yaxjqxiskysxa"
    },
    "acceptor": {
      "accountId": "845735284135"
    },
    "proposer": {
      "accountId": "123456512334"
    },
    "offer": {
      "id": "offer-1234567890123"
    }
  }
}
```

The following is an example event body for **Purchase Agreement Created - Proposer** when a renewal creates a new agreement (`intent=RENEW`).

```
{
  "version": "0",
  "id": "12345678-1234-1234-1234-123456789012",
  "detail-type": "Purchase Agreement Created - Proposer",
  "source": "aws.agreement-marketplace",
  "account": "<ISV's or CP's account id>",
  "time": "2024-08-30T21:36:03Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace::aws:agreement:agmt-newrenewalagreementid"
  ],
  "detail": {
    "requestId": "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "catalog": "AWSMarketplace",
    "agreement": {
      "id": "agmt-newrenewalagreementid",
      "intent": "RENEW",
      "status": "ACTIVE",
      "acceptanceTime": "2024-08-30T21:36:03Z",
      "startTime": "2024-08-30T21:36:03Z",
      "endTime": "2025-05-30T21:36:03Z",
      "previousAgreementId": "agmt-4mwg1nevbokzw95eca5797ixs"
    },
    "product": {
      "id": "prod-aw4fgf5tyo5w2ap6fEXAMPLE",
      "title": "Product Title"
    },
    "acceptor": {
      "accountId": "845735284135"
    },
    "proposer": {
      "name": "Seller Account Name",
      "accountId": "123456512334"
    },
    "offer": {
      "id": "offer-1234567890123"
    }
  }
}
```

The following is an example event body for **Purchase Agreement Created - Manufacturer**.

```
{
  "version": "0",
  "id": "12345678-1234-1234-1234-123456789012",
  "detail-type": "Purchase Agreement Created - Manufacturer",
  "source": "aws.agreement-marketplace",
  "account": "<ISV's account id>",
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
      "intent": "NEW",
      "status": "ACTIVE",
      "acceptanceTime": "2024-06-26T21:36:03Z",
      "startTime": "2024-08-30T21:36:03Z",
      "endTime": "2025-05-30T21:36:03Z"
    },
    "resaleAuthorization": {
      "id": "resaleauthz-yaxjqxiskysxa"
    },
    "acceptor": {
      "accountId": "845735284135"
    },
    "proposer": {
      "accountId": "123456512334"
    },
    "offer": {
      "id": "offer-1234567890123"
    }
  }
}
```

The following is an example event body for **Purchase Agreement Amended - Proposer**.

```
{
  "version": "0",
  "id": "12345678-1234-1234-1234-123456789012",
  "detail-type": "Purchase Agreement Amended - Proposer",
  "source": "aws.agreement-marketplace",
  "account": "<ISV or CP's account id>",
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
      "lockoutStartTime": "2025-04-30T21:36:03Z",
      "disabledBy": null
    },
    "product": {
      "id": "prod-aw4fgf5tyo5w2ap6fEXAMPLE",
      "title": "Product Title"
    },
    "resaleAuthorization": {
      "id": "resaleauthz-yaxjqxiskysxa"
    },
    "acceptor": {
      "accountId": "845735284135"
    },
    "proposer": {
      "accountId": "123456512334"
    },
    "offer": {
      "id": "offer-1234567890123"
    }
  }
}
```

`autoRenewalEnabled`: `true` when renewal terms are present and neither party opted out; `false` otherwise. `renewalSummary.lockoutStartTime`: `null` when the renewal term has no lockout period. `renewalSummary.disabledBy`: `ACCEPTOR` or `PROPOSER` (`PROPOSER` if both opted out); `null` when `autoRenewalEnabled` is `true` or there are no renewal terms. Seller opt-out is processed as an amendment and surfaces through this event.

The following is an example event body for **Purchase Agreement Amended - Manufacturer**.

```
{
  "version": "0",
  "id": "12345678-1234-1234-1234-123456789012",
  "detail-type": "Purchase Agreement Amended - Manufacturer",
  "source": "aws.agreement-marketplace",
  "account": "<ISV's account id>",
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
    "resaleAuthorization": {
      "id": "resaleauthz-yaxjqxiskysxa"
    },
    "acceptor": {
      "accountId": "845735284135"
    },
    "proposer": {
      "accountId": "123456512334"
    },
    "offer": {
      "id": "offer-1234567890123"
    }
  }
}
```

The following is an example event body for **Purchase Agreement Ended - Proposer**.

```
{
  "version": "0",
  "id": "12345678-1234-1234-1234-123456789012",
  "detail-type": "Purchase Agreement Ended - Proposer",
  "source": "aws.agreement-marketplace",
  "account": "<ISV's account id>",
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
      "status": "CANCELLED"
    },
    "resaleAuthorization": {
      "id": "resaleauthz-yaxjqxiskysxa"
    },
    "acceptor": {
      "accountId": "845735284135"
    },
    "proposer": {
      "accountId": "123456512334"
    },
    "offer": {
      "id": "offer-1234567890123"
    }
  }
}
```

The following is an example event body for **Purchase Agreement Ended - Manufacturer**.

```
{
  "version": "0",
  "id": "12345678-1234-1234-1234-123456789012",
  "detail-type": "Purchase Agreement Ended - Manufacturer",
  "source": "aws.agreement-marketplace",
  "account": "<ISV's account id>",
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
      "status": "CANCELLED"
    },
    "resaleAuthorization": {
      "id": "resaleauthz-yaxjqxiskysxa"
    },
    "acceptor": {
      "accountId": "845735284135"
    },
    "proposer": {
      "accountId": "123456512334"
    },
    "offer": {
      "id": "offer-1234567890123"
    }
  }
}
```

The following is an example event body for **Purchase Agreement Advisory Issued - Manufacturer**.

```
{
  "version": "0",
  "id": "a1b2c3d4-1111-2222-3333-444455556666",
  "detail-type": "Purchase Agreement Advisory Issued - Manufacturer",
  "source": "aws.agreement-marketplace",
  "account": "987654321098",
  "time": "2026-07-02T14:30:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace::aws:agreement:agmt-4mwg1nevbokzw95eca5797ixs"
  ],
  "detail": {
    "requestId": "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "catalog": "AWSMarketplace",
    "agreement": {
      "id": "agmt-4mwg1nevbokzw95eca5797ixs"
    },
    "product": {
      "id": "prod-aw4fgf5tyo5w2ap6fEXAMPLE"
    },
    "acceptor": {
      "accountId": "845735284135"
    },
    "proposer": {
      "accountId": "987654321098"
    },
    "offer": {
      "id": "offer-1234567890123"
    },
    "advisory": {
      "issuedAt": "2026-07-02T14:28:00Z"
    }
  }
}
```

The following is an example event body for **Purchase Agreement Advisory Resolved - Manufacturer**.

```
{
  "version": "0",
  "id": "k9s5f3d4-0921-2382-3333-970453552166",
  "detail-type": "Purchase Agreement Advisory Resolved - Manufacturer",
  "source": "aws.agreement-marketplace",
  "account": "987654321098",
  "time": "2026-07-02T14:30:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace::aws:agreement:agmt-4mwg1nevbokzw95eca5797ixs"
  ],
  "detail": {
    "requestId": "7s4p9f1b-b809-4f5e-9fgl-a9ae74b05cji",
    "catalog": "AWSMarketplace",
    "agreement": {
      "id": "agmt-4mwg1nevbokzw95eca5797ixs"
    },
    "product": {
      "id": "prod-aw4fgf5tyo5w2ap6fEXAMPLE"
    },
    "acceptor": {
      "accountId": "845735284135"
    },
    "proposer": {
      "accountId": "987654321098"
    },
    "offer": {
      "id": "offer-1234567890123"
    },
    "advisory": {
      "resolvedAt": "2026-08-02T11:13:05Z"
    }
  }
}
```

The following is an example event body for **Purchase Agreement Ending - Proposer**.

```
{
  "version": "0",
  "id": "12345678-1234-1234-1234-123456789012",
  "detail-type": "Purchase Agreement Ending - Proposer",
  "source": "aws.agreement-marketplace",
  "account": "<ISV's account id>",
  "time": "2026-07-04T00:00:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace::aws:agreement:agmt-4mwg1nevbokzw95eca5797ixs"
  ],
  "detail": {
    "requestId": "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "catalog": "AWSMarketplace",
    "agreement": {
      "id": "agmt-4mwg1nevbokzw95eca5797ixs",
      "startTime": "2025-06-01T00:00:00Z",
      "endTime": "2026-12-31T00:00:00Z",
      "status": "ACTIVE",
      "daysBeforeEndTime": 180,
      "autoRenewalEnabled": true
    },
    "renewalSummary": {
      "lockoutStartTime": "2026-12-01T00:00:00Z",
      "disabledBy": null
    },
    "product": {
      "id": "prod-aw4fgf5tyo5w2ap6fEXAMPLE",
      "title": "Product Title"
    },
    "acceptor": { "accountId": "845735284135" },
    "proposer": {
      "name": "Seller Account Name",
      "accountId": "123456512334"
    },
    "offer": { "id": "offer-1234567890123" }
  }
}
```

`daysBeforeEndTime` values: 180 \| 120 \| 90 \| 60 \| 30.

The following is an example event body for **Purchase Agreement Renewal Terms Finalized - Proposer**. This event fires after the seller adjustment deadline passes (percentage-range offers only).

```
{
  "version": "0",
  "id": "12345678-1234-1234-1234-123456789012",
  "detail-type": "Purchase Agreement Renewal Terms Finalized - Proposer",
  "source": "aws.agreement-marketplace",
  "account": "<ISV's account id>",
  "time": "2026-11-01T00:00:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace::aws:agreement:agmt-4mwg1nevbokzw95eca5797ixs"
  ],
  "detail": {
    "requestId": "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "catalog": "AWSMarketplace",
    "agreement": {
      "id": "agmt-4mwg1nevbokzw95eca5797ixs",
      "startTime": "2025-06-01T00:00:00Z",
      "endTime": "2026-12-31T00:00:00Z"
    },
    "renewalSummary": {
      "tcv": "105000.00",
      "currency": "USD",
      "termsFinalizedTime": "2026-11-01T00:00:00Z",
      "lockoutReached": false,
      "lockoutStartTime": "2026-12-01T00:00:00Z"
    },
    "product": {
      "id": "prod-aw4fgf5tyo5w2ap6fEXAMPLE",
      "title": "Product Title"
    },
    "acceptor": { "accountId": "845735284135" },
    "proposer": {
      "name": "Seller Account Name",
      "accountId": "123456512334"
    }
  }
}
```

`renewalSummary.lockoutReached` and `lockoutStartTime` are `null` when the accepted renewal term has no lockout period.

The following is an example event body for **Purchase Agreement Renewal Upcoming - Proposer**. This event fires at lockout period start.

```
{
  "version": "0",
  "id": "12345678-1234-1234-1234-123456789012",
  "detail-type": "Purchase Agreement Renewal Upcoming - Proposer",
  "source": "aws.agreement-marketplace",
  "account": "<ISV's account id>",
  "time": "2026-12-01T00:00:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace::aws:agreement:agmt-4mwg1nevbokzw95eca5797ixs"
  ],
  "detail": {
    "requestId": "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "catalog": "AWSMarketplace",
    "agreement": {
      "id": "agmt-4mwg1nevbokzw95eca5797ixs",
      "startTime": "2025-06-01T00:00:00Z",
      "endTime": "2026-12-31T00:00:00Z"
    },
    "renewalSummary": {
      "lockoutReached": true,
      "tcv": "105000.00",
      "currency": "USD"
    },
    "product": {
      "id": "prod-aw4fgf5tyo5w2ap6fEXAMPLE",
      "title": "Product Title"
    },
    "acceptor": { "accountId": "845735284135" },
    "proposer": {
      "name": "Seller Account Name",
      "accountId": "123456512334"
    }
  }
}
```

## Events for licenses
<a name="events-for-licenses"></a>

When license events occur, sellers can receive notifications for customer entitlement changes.

For information on creating EventBridge rules, see [Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) in the *Amazon EventBridge User Guide*.

The following is an example event body for **License Updated - Manufacturer**.

```
{
  "version": "0",
  "id": "12345678-1234-1234-1234-123456789012",
  "detail-type": "License Updated - Manufacturer",
  "source": "aws.agreement-marketplace",
  "account": "<ISV/CP account id>",
  "time": "2024-08-30T21:36:03Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace::aws:agreement:agmt-4mwg1nevbokzw95eca5797ixs"
  ],
  "detail": {
    "requestId": "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "catalog": "AWSMarketplace",
    "agreement": {
      "id": "agmt-4mwg1nevbokzw95eca5797ixs"
    },
    "product": {
      "code": "aw4fgf5tyo5w2ap6fEXAMPLE",
      "id": "prod-qtwveEXAMPLE"
    },
    "license": {
      "arn": "aws:license-manager:us-east-1:123456789012:l-e52ca6f38bf84d0fafb8802ca15ac11x"
    },
    "acceptor": {
      "accountId": "845735284135"
    },
    "proposer": {
      "accountId": "123456512334"
    },
    "offer": {
      "id": "8kkr91jo647j3qxlcjhlqce7y"
    }
  }
}
```

The following is an example event body for **License Deprovisioned - Manufacturer**.

```
{
  "version": "0",
  "id": "12345678-1234-1234-1234-123456789012",
  "detail-type": "License Deprovisioned - Manufacturer",
  "source": "aws.agreement-marketplace",
  "account": "<ISV/CP account id>",
  "time": "2024-08-30T21:36:03Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:aws-marketplace::aws:agreement:agmt-4mwg1nevbokzw95eca5797ixs"
  ],
  "detail": {
    "requestId": "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "catalog": "AWSMarketplace",
    "agreement": {
      "id": "agmt-4mwg1nevbokzw95eca5797ixs"
    },
    "product": {
      "code": "aw4fgf5tyo5w2ap6fEXAMPLE",
      "id": "prod-qtwveEXAMPLE"
    },
    "license": {
      "arn": "aws:license-manager:us-east-1:123456789012:l-e52ca6f38bf84d0fafb8802ca15ac11x"
    },
    "acceptor": {
      "accountId": "845735284135"
    },
    "proposer": {
      "accountId": "123456512334"
    },
    "offer": {
      "id": "8kkr91jo647j3qxlcjhlqce7y"
    }
  }
}
```

## Events for cancellations
<a name="events-for-cancellations"></a>

When a cancellation request status changes, sellers, buyers, and ISVs (for CPPO) receive events. Each event is sent to the relevant party with a role-specific detail type (Proposer for sellers, Acceptor for buyers, Manufacturer for ISVs). The source for these events is `aws.agreement-marketplace`.

For information on creating EventBridge rules, see [Amazon EventBridge rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) in the *Amazon EventBridge User Guide*.

The following is an example event body for **Agreement Cancellation Request Pending Approval - Proposer**. This event is sent when you submit a cancellation request and it is awaiting buyer approval.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Agreement Cancellation Request Pending Approval - Proposer",
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
      "acceptorId": "123465789012",
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

The following is an example event body for **Agreement Cancellation Request Approved - Proposer**. This event is sent when the buyer approves your cancellation request or when it is auto-approved after 7 days.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Agreement Cancellation Request Approved - Proposer",
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
      "acceptorId": "123465789012",
      "productId": "prod-exampleid",
      "offerId": "offer-exampleid"
    },
    "agreementCancellationRequest": {
      "id": "acr-abcdexampleid",
      "reasonCode": "INCORRECT_TERMS_ACCEPTED",
      "reasonMessage": "The terms accepted in agreement had wrong rate",
      "statusCode": "APPROVED",
      "statusMessage": "",
      "createdAt": "2025-01-03T16:16:22Z",
      "updatedAt": "2025-01-03T16:20:08Z"
    }
  }
}
```

The following is an example event body for **Agreement Cancellation Request Rejected - Proposer**. This event is sent when the buyer denies your cancellation request.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Agreement Cancellation Request Rejected - Proposer",
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
      "acceptorId": "123465789012",
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

The following is an example event body for **Agreement Cancellation Request Cancelled - Proposer**. This event is sent when you withdraw a cancellation request.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Agreement Cancellation Request Cancelled - Proposer",
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
      "acceptorId": "123465789012",
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

The following is an example event body for **Agreement Cancellation Request Validation Failed - Proposer**. This event is sent only to the seller when an async validation fails after submission.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Agreement Cancellation Request Validation Failed - Proposer",
  "source": "aws.agreement-marketplace",
  "account": "123456789012",
  "time": "2025-01-01T13:15:00Z",
  "region": "us-east-1",
  "resources": [],
  "detail": {
    "requestId": "3d4c9f9b-b809-4f5e-9fac-a9ae98b05cbb",
    "catalog": "AWSMarketplace",
    "agreement": {
      "id": "agmt-abcdexampleid",
      "acceptorId": "123465789012",
      "productId": "prod-exampleid",
      "offerId": "offer-exampleid"
    },
    "agreementCancellationRequest": {
      "id": "acr-abcdexampleid",
      "reasonCode": "INCORRECT_TERMS_ACCEPTED",
      "reasonMessage": "The terms accepted in agreement had wrong rate",
      "statusCode": "VALIDATION_FAILED",
      "statusMessage": "Agreement has a renewal agreement that must be canceled first",
      "createdAt": "2025-01-01T13:12:22Z",
      "updatedAt": "2025-01-01T13:15:00Z"
    }
  }
}
```

## Events for billing adjustments
<a name="events-for-billing-adjustments"></a>

When a billing adjustment status changes, sellers, buyers, and ISVs (for CPPO) receive events. Each event is sent to the relevant party with a role-specific detail type (Proposer for sellers, Acceptor for buyers, Manufacturer for ISVs). The source for these events is `aws.agreement-marketplace`.

The following is an example event body for **Purchase Agreement Billing Adjustment Completed - Proposer**.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Purchase Agreement Billing Adjustment Completed - Proposer",
  "source": "aws.agreement-marketplace",
  "account": "123456789012",
  "time": "2025-01-01T13:12:22Z",
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
      "adjustmentAmount": "-100.00",
      "currencyCode": "USD",
      "adjustmentReasonCode": "INCORRECT_TERMS_ACCEPTED"
    },
    "invoice": {
      "originalInvoiceId": "2028746221"
    }
  }
}
```

The following is an example event body for **Purchase Agreement Billing Adjustment Failed - Proposer**. This event is sent only to the seller when a billing adjustment fails async validation.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Purchase Agreement Billing Adjustment Failed - Proposer",
  "source": "aws.agreement-marketplace",
  "account": "123456789012",
  "time": "2025-01-01T13:15:00Z",
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