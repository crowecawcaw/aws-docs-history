# Amazon EventBridge events

As a seller, you can use Amazon EventBridge to receive notifications for events in AWS Marketplace. For
example, you can receive an _event_ from AWS Marketplace when an offer is
created. The _event_ contains details like the ID, expiration
date, and product details. EventBridge is an event bus service that you can use to connect your
applications with data from a variety of sources. For more information, see the [_Amazon EventBridge User Guide_](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md"). The following sections provide
detailed information about events under the Marketplace Catalog service in the EventBridge
console.

###### Topics

- [Events for new offers](#events-offerreleased "#events-offerreleased")
- [Events for change sets](#events-changesets "#events-changesets")
- [Events for security summary report](#events-security-report "#events-security-report")
- [Events for disbursements](#events-for-disbursements "#events-for-disbursements")
- [Events for agreements](#events-for-agreements "#events-for-agreements")
- [Events for licenses](#events-for-licenses "#events-for-licenses")
  This topic

| Action by seller                                                                          | Event received                     | Related topic                                                                           |
| ----------------------------------------------------------------------------------------- | ---------------------------------- | --------------------------------------------------------------------------------------- |
| Independent software vendor (ISV) creates an offer and makes it available for<br>purchase | `Offer Released`                   | [Events for new offers](#events-offerreleased "#events-offerreleased")                  |
| ISV's product is used by a channel partner to create an offer                             | `Offer Released`                   | [Events for new offers](#events-offerreleased "#events-offerreleased")                  |
| Channel partner creates an offer                                                          | `Offer Released`                   | [Events for new offers](#events-offerreleased "#events-offerreleased")                  |
| ISV creates a new offer set                                                               | `OfferSet Released`                | [Events for new offers](#events-offerreleased "#events-offerreleased")                  |
| Channel partner creates a new offer set                                                   | `OfferSet Released`                | [Events for new offers](#events-offerreleased "#events-offerreleased")                  |
| Change set succeeds                                                                       | `Change Set Succeeded`             | [Events for change sets](#events-changesets "#events-changesets")                       |
| Change set fails                                                                          | `Change Set Failed`                | [Events for change sets](#events-changesets "#events-changesets")                       |
| Change set is cancelled                                                                   | `Change Set Cancelled`             | [Events for change sets](#events-changesets "#events-changesets")                       |
| Security vulnerabilities were detected on the ISV's product                               | `Products Security Report Created` | [Events for security summary report](#events-security-report "#events-security-report") |
| Customer subscribes to SaaS product                                                       | `Purchase Agreement Created`       | [Events for agreements](#events-for-agreements "#events-for-agreements")                |
| Customer's SaaS agreement is amended                                                      | `Purchase Agreement Amended`       | [Events for agreements](#events-for-agreements "#events-for-agreements")                |
| Customer cancels SaaS subscription                                                        | `Purchase Agreement Ended`         | [Events for agreements](#events-for-agreements "#events-for-agreements")                |
| Customer's SaaS entitlements change                                                       | `License Updated`                  | [Events for licenses](#events-for-licenses "#events-for-licenses")                      |
| Customer's SaaS entitlements are revoked                                                  | `License Deprovisioned`            | [Events for licenses](#events-for-licenses "#events-for-licenses")                      |

## Events for new offers

When sellers create an offer and make it available for purchase, they can receive an event
with the following detail type: `Offer Released`.

###### Note

For information on creating EventBridge rules, see [Amazon EventBridge rules](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md") in the _Amazon EventBridge User Guide_.

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

The following is an example event body for when an ISV's product is used by a channel
partner to create an offer.

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

When a change set completes, sellers, channel partners, and private marketplace
administrators can receive an event. The AWS Marketplace Catalog API sends an event when a change set
completes with a status of succeeded, failed, or cancelled. The source for these events is
`aws.marketplacecatalog`, and the possible detail type values are `Change
 Set Succeeded`, `Change Set Failed`, and `Change Set
 Cancelled`.

###### Note

For information on change sets, see [Working with change sets](../../../marketplace-catalog/latest/api-reference/welcome.md#working-with-change-sets "../../../marketplace-catalog/latest/api-reference/welcome.md#working-with-change-sets") in the _AWS Marketplace Catalog API
Reference_.

Each event contains change request details, such as the change set ID, change set name,
event detail type, failure code (for failed requests), and start and end times of the request.
This enables you to monitor your change sets without continuously querying the
`DescribeChangeSet` action or checking the AWS Marketplace Management Portal for the status of your
change requests.

###### Note

For information on creating EventBridge rules, see [Amazon EventBridge rules](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md") in the _Amazon EventBridge User Guide_.

The following is an example event body for the `Change Set Succeeded` detail
type.

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

The following is an example event body for the `Change Set Failed` detail
type.

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

The following is an example event body for the `Change Set Cancelled` detail
type.

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

When security vulnerabilities are detected on a seller's products, they can receive a
summary report event and periodic reminders for outstanding product issues. The source for
these events is `aws.marketplacecatalog`, and the detail type is `Products
 Security Report Created`.

Each event includes a summary of the count of products and versions with detected issues,
a count of how many latest versions are affected, and the date when resolution is required to
prevent a temporary restriction of these products or versions.

###### Note

For information on creating EventBridge rules, see [Amazon EventBridge rules](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md") in the _Amazon EventBridge User Guide_.

For details on managing security events, see the [How to improve the security of your product catalog in AWS Marketplace](https://aws.amazon.com/blogs/awsmarketplace/how-to-improve-security-your-product-catalog-aws-marketplace/ "https://aws.amazon.com/blogs/awsmarketplace/how-to-improve-security-your-product-catalog-aws-marketplace/") blog post on the
_AWS Blog_.

The following is an example event body for the `Products Security Report
 Created` detail type.

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

To resolve the invalid bank account details issue, add your bank account details in the AWS Marketplace Management Portal. For instructions, see [To add bank account details](email-notifications.md#resolve-invalid-bank-account-details "email-notifications.md#resolve-invalid-bank-account-details").

For more information about creating Amazon EventBridge rules, see [Rules in Amazon EventBridge](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md") in the _Amazon EventBridge User Guide_.

## Events for agreements

When agreement events occur, sellers can receive notifications for purchase agreement lifecycle changes.

For information on creating EventBridge rules, see [Amazon EventBridge rules](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md") in the _Amazon EventBridge User Guide_.

The following is an example event body for **Purchase Agreement Created - Proposer**.

###### Note

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

## Events for licenses

When license events occur, sellers can receive notifications for customer entitlement changes.

For information on creating EventBridge rules, see [Amazon EventBridge rules](../../../eventbridge/latest/userguide/eb-rules.md "../../../eventbridge/latest/userguide/eb-rules.md") in the _Amazon EventBridge User Guide_.

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
