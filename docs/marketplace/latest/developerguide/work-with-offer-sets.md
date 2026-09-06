

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Work with offer sets
<a name="work-with-offer-sets"></a>

AWS Marketplace offer sets enable sellers to package multiple private offers into unified multi-product transactable packages for buyers. This capability addresses growing customer demand for comprehensive, end-to-end solutions in complex enterprise environments.

Traditionally, buyers had to discover and procure individual products from multiple sellers, resulting in fragmented experiences, integration challenges, and longer procurement cycles. Offer sets simplify this by allowing AWS Marketplace partners to combine multiple offers together, streamlining the transaction process through coordinated private offers where customers can review and accept all components with one-time approval.

Offer sets work together with solutions to provide comprehensive multi-product offerings. Solutions provide rich marketing content including detailed descriptions, architecture diagrams, and use case documentation, while offer sets handle the transactable packaging and commercial terms for unified procurement.

## Offer set entity
<a name="offer-set-entity"></a>

An offer set is a container that groups 2-7 private offers into a single transactable package. Each offer within an offer set maintains its own distinct pricing, payment terms, duration, and End User License Agreement (EULA), while the offer set provides a unified discovery and acceptance experience for buyers.

**Key characteristics:**
+ Groups multiple private offers (minimum 2, maximum 7)
+ Enables unified buyer acceptance of all offers with a single action
+ Maintains flexibility with distinct terms for each offer
+ Creates separate agreements for each product, allowing independent management after purchase
+ Can be optionally associated with a solution for enhanced marketing content

The offer set entity type is `OfferSet@1.0`.

**Entity identifiers**

Offer sets use the `offerset-*` identifier format (for example, `offerset-abc123def456`).

**Entity ARN format**

Offer sets follow the standard AWS ARN format:

```
arn:aws:aws-marketplace:{region}:{account-id}:AWSMarketplace/OfferSet/{offerset-id}
```

Example:

```
arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/OfferSet/offerset-abc123def456
```

## Getting started with offer sets
<a name="getting-started-with-offer-sets"></a>

This section provides detailed information about creating and managing offer sets using AWS Marketplace Catalog API [change types](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Change.html).

Before you begin, make sure you have:
+ Valid AWS Marketplace seller registration and a public profile. For more information, see [Register and create your seller profile](https://docs.aws.amazon.com/marketplace/latest/userguide/create-public-profile.html).
+ Access to the API and completed seller prerequisites. For more information, see [Access control for the AWS Marketplace Catalog API](https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-api-access-control.html).
+ Learned the basics of using the AWS Marketplace Catalog API, see [Using the AWS Marketplace Catalog API](https://docs.aws.amazon.com/marketplace/latest/APIReference/catalog-apis.html).

## List offer sets
<a name="list-offer-sets"></a>

To list all offer sets in your account, call the `ListEntities` API operation with `EntityType` set to `OfferSet`.

**Request**

```
POST /ListEntities HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "EntityType": "OfferSet"
}
```

**Response**

```
{
  "EntitySummaryList": [
    {
      "EntityType": "OfferSet",
      "EntityId": "offerset-xyz123",
      "EntityArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/OfferSet/offerset-xyz123",
      "LastModifiedDate": "2025-06-25T23:46:25Z",
      "OfferSetSummary": {
        "Name": "Enterprise Security Solution Offer Set",
        "State": "Released",
        "ReleaseDate": "2025-06-25T23:46:20Z",
        "SolutionId": "soln-abc987",
        "AssociatedOfferIds": [
          "offer-abc123",
          "offer-def456",
          "offer-ghi789"
        ]
      }
    }
  ],
  "NextToken": null
}
```

### Filter offer sets by state
<a name="filter-offer-sets-by-state"></a>

You can filter offer sets by state using the `EntityTypeFilters` parameter.

**Request**

```
POST /ListEntities HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "EntityType": "OfferSet",
  "EntityTypeFilters": {
    "OfferSetFilters": {
      "State": {
        "ValueList": [
          "Released"
        ]
      }
    }
  }
}
```

### Filter offer sets by solution ID
<a name="filter-offer-sets-by-solution-id"></a>

You can filter offer sets by solution ID using the `EntityTypeFilters` parameter.

**Request**

```
POST /ListEntities HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "EntityType": "OfferSet",
  "EntityTypeFilters": {
    "OfferSetFilters": {
      "SolutionId": {
        "ValueList": [
          "soln-abc987"
        ]
      }
    }
  }
}
```

### Filter offer sets by release date
<a name="filter-offer-sets-by-release-date"></a>

You can filter offer sets by release date and sort the results using the `EntityTypeFilters` and `EntityTypeSort` parameters.

**Request**

```
POST /ListEntities HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "EntityType": "OfferSet",
  "EntityTypeFilters": {
    "OfferSetFilters": {
      "ReleaseDate": {
        "AfterValue": "2025-11-01"
      }
    }
  },
  "EntityTypeSort": {
    "OfferSetSort": {
      "SortBy": "ReleaseDate",
      "SortOrder": "DESCENDING"
    }
  }
}
```

## Describe an offer set
<a name="describe-offer-set"></a>

To get detailed information about a specific offer set, call the `DescribeEntity` API operation.

**Request**

```
GET /DescribeEntity?catalog=AWSMarketplace&entityId=offerset-xyz123 HTTP/1.1
```

**Response**

```
{
  "EntityType": "OfferSet@1.0",
  "EntityId": "offerset-xyz123",
  "EntityArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/OfferSet/offerset-xyz123",
  "LastModifiedDate": "2025-06-25T23:46:25Z",
  "DetailsDocument": {
    "Id": "offerset-xyz123",
    "Name": "Enterprise Security Solution Offer Set",
    "BuyerNotes": "Complete security solution including endpoint protection and network monitoring",
    "State": "Released",
    "SolutionId": "soln-abc987",
    "ReleaseDate": "2025-06-25T23:46:20Z",
    "AssociatedOffers": [
      {
        "OfferId": "offer-abc123"
      },
      {
        "OfferId": "offer-def456"
      },
      {
        "OfferId": "offer-ghi789"
      }      
    ]
  }
}
```

## Create an offer set
<a name="create-offer-set"></a>

Use the `CreateOfferSet` change type to create a new offer set entity in Draft state. This is the first step in the offer set lifecycle, establishing the foundational entity that will later be configured with offer associations and metadata before releasing to buyers.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "CreateOfferSet",
      "Entity": {
        "Type": "OfferSet@1.0"
      },
      "ChangeName": "CreateOfferSetChange",
      "DetailsDocument": {
        "Name": "Enterprise Security Solution Offer Set"
      }
    }
  ]
}
```

Provide information for the fields to add the `CreateOfferSet` change type:
+ `Entity` (object) (required) – The entity type being created.
  + `Type` (string) (required) – Must be `OfferSet@1.0`.
+ `DetailsDocument` (object) (required) – The details of the request.
  + `Name` (string) (required) – The name associated with the offer set for better readability to you and your customers. Minimum length: 1 character. Maximum length: 150 characters.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating information to ensure that it meets the AWS Marketplace guidelines. The validation process can take a few minutes.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

After successful processing, AWS Marketplace generates an offer set in Draft state with a unique identifier prefixed with `offerset-`.

## Update offer set information
<a name="update-offer-set-information"></a>

Use the `UpdateInformation` change type to modify the details of an existing offer set, including its name and buyer notes.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "UpdateInformation",
      "Entity": {
        "Type": "OfferSet@1.0",
        "Identifier": "offerset-abc123"
      },
      "DetailsDocument": {
        "Name": "Updated Enterprise Security Offer Set",
        "BuyerNotes": "Complete security solution including endpoint protection, network monitoring, and professional services implementation"
      }
    }
  ]
}
```

Provide information for the fields to add the `UpdateInformation` change type:
+ `Entity` (object) (required) – The entity being updated.
  + `Identifier` (string) (required) – Your offer set ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – Must be `OfferSet@1.0`.
+ `DetailsDocument` (object) (required) – At least one field must be provided.
  + `Name` (string) (optional) – Display name visible to buyers. Minimum length: 1 character. Maximum length: 150 characters.
  + `BuyerNotes` (string) (optional) – Detailed information about the offer set that helps buyers understand its purpose and contents. Minimum length: 1 character. Maximum length: 1,000 characters.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating information to ensure that it meets the AWS Marketplace guidelines. The validation process can take a few minutes.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

## Associate offers with an offer set
<a name="associate-offers"></a>

Use the `AssociateOffers` change type to associate multiple AWS Marketplace offers with an offer set. This creates the relationship between offers and the offer set, making the offers part of the offer set's transactable configuration.

The operation is idempotent and allows associating offers regardless of their current state, enabling complete configuration before individual offers are released. Each offer can only belong to one offer set.

**Important**  
The `OfferSetId` on individual offers is immutable and can only be set during offer creation. Before associating offers with an offer set using `AssociateOffers`, you must first create the individual offers and specify the `OfferSetId` during offer creation. If you need to include an existing offer that doesn't have the correct `OfferSetId`, you must create a new offer with the correct `OfferSetId` specified.

For information about required IAM permissions, see [IAM permissions for offer sets](#iam-permissions-offer-sets).

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "AssociateOffers",
      "Entity": {
        "Type": "OfferSet@1.0",
        "Identifier": "offerset-abc123"
      },
      "DetailsDocument": {
        "Offers": [
          {
            "OfferId": "offer-xyz789"
          },
          {
            "OfferId": "offer-def456"
          },
          {
            "OfferId": "offer-ghi123"
          }
        ]
      }
    }
  ]
}
```

Provide information for the fields to add the `AssociateOffers` change type:
+ `Entity` (object) (required) – The entity being updated.
  + `Identifier` (string) (required) – Your offer set ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – Must be `OfferSet@1.0`.
+ `DetailsDocument` (object) (required) – The details of the request.
  + `Offers` (array) (required) – List of AWS Marketplace offers to associate. Minimum: 1 item. Maximum: 7 items.
    + `OfferId` (string) (required) – The identifier of the AWS Marketplace offer. Minimum length: 1 character. Maximum length: 36 characters.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating information to ensure that it meets the AWS Marketplace guidelines. The validation process can take a few minutes.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

### Asynchronous Errors
<a name="associate-offers-asynchronous-errors"></a>

The following errors are specific to `AssociateOffers` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| TOO\_MANY\_OFFERS | Associate up to 7 offers to the offer set. | 
| INCOMPATIBLE\_OFFER\_SET\_REFERENCE | Ensure all offers were created specifically for this offer set. | 
| INVALID\_UPDATE\_REQUEST | The requested change can't be performed after the offer set released. | 

## Disassociate offers from an offer set
<a name="disassociate-offers"></a>

Use the `DisassociateOffers` change type to remove multiple AWS Marketplace offers from an offer set. This idempotent operation removes the association relationship while preserving the offer's `OfferSetId` attribute. Disassociated offers become hidden from buyer discovery until re-associated with the same offer set. They cannot be associated with a different offer set.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "DisassociateOffers",
      "Entity": {
        "Type": "OfferSet@1.0",
        "Identifier": "offerset-abc123"
      },
      "DetailsDocument": {
        "Offers": [
          {
            "OfferId": "offer-xyz789"
          }
        ]
      }
    }
  ]
}
```

Provide information for the fields to add the `DisassociateOffers` change type:
+ `Entity` (object) (required) – The entity being updated.
  + `Identifier` (string) (required) – Your offer set ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – Must be `OfferSet@1.0`.
+ `DetailsDocument` (object) (required) – The details of the request.
  + `Offers` (array) (required) – List of offers to disassociate. Minimum: 1 item. Maximum: 7 items.
    + `OfferId` (string) (required) – The identifier of the AWS Marketplace offer. Minimum length: 1 character. Maximum length: 36 characters.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating information to ensure that it meets the AWS Marketplace guidelines. The validation process can take a few minutes.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

### Asynchronous Errors
<a name="disassociate-offers-asynchronous-errors"></a>

The following errors are specific to `DisassociateOffers` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INVALID\_UPDATE\_REQUEST | The requested change can't be performed after the offer set released. | 

## Associate a solution with an offer set
<a name="associate-solution-with-offer-set"></a>

Use the `AssociateSolution` change type to associate a single AWS Marketplace solution with an offer set. This creates a relationship that allows buyers to discover the offer set's connection to the solution and access the solution's rich marketing content such as detailed descriptions, architecture diagrams, and use case documentation.

**Note**  
This is a loosely coupled association. AWS Marketplace doesn't enforce consistency between the solution and offer set. Solutions can contain no AWS Marketplace products, different products than those in the offer set, or overlapping products. You have complete flexibility to associate any solution you own for marketing and discovery purposes.

For information about required IAM permissions, see [IAM permissions for offer sets](#iam-permissions-offer-sets).

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "AssociateSolution",
      "Entity": {
        "Type": "OfferSet@1.0",
        "Identifier": "offerset-abc123"
      },
      "DetailsDocument": {
        "SolutionId": "soln-xyz789"
      }
    }
  ]
}
```

Provide information for the fields to add the `AssociateSolution` change type:
+ `Entity` (object) (required) – The entity being updated.
  + `Identifier` (string) (required) – Your offer set ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – Must be `OfferSet@1.0`.
+ `DetailsDocument` (object) (required) – The details of the request.
  + `SolutionId` (string) (required) – The identifier of the AWS Marketplace solution to associate. Minimum length: 1 character. Maximum length: 50 characters. Must match pattern `^soln-[A-Za-z0-9]+$`.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating information to ensure that it meets the AWS Marketplace guidelines. The validation process can take a few minutes.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

### Asynchronous Errors
<a name="associate-solution-asynchronous-errors"></a>

The following errors are specific to `AssociateSolution` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INCOMPATIBLE\_SOLUTION\_ASSOCIATION | Disassociate the existing solution before associating a new solution. | 
| INVALID\_UPDATE\_REQUEST | The requested change can't be performed after the offer set released. | 

## Disassociate a solution from an offer set
<a name="disassociate-solution-from-offer-set"></a>

Use the `DisassociateSolution` change type to remove the association between a solution and an offer set. This removes the solution's marketing content from the offer set while maintaining the offer set's transactable functionality.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "DisassociateSolution",
      "Entity": {
        "Type": "OfferSet@1.0",
        "Identifier": "offerset-abc123"
      },
      "DetailsDocument": {
        "SolutionId": "soln-xyz789"
      }
    }
  ]
}
```

Provide information for the fields to add the `DisassociateSolution` change type:
+ `Entity` (object) (required) – The entity being updated.
  + `Identifier` (string) (required) – Your offer set ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – Must be `OfferSet@1.0`.
+ `DetailsDocument` (object) (required) – The details of the request.
  + `SolutionId` (string) (required) – The identifier of the solution to disassociate. Minimum length: 1 character. Maximum length: 50 characters.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating information to ensure that it meets the AWS Marketplace guidelines. The validation process can take a few minutes.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

### Asynchronous Errors
<a name="disassociate-solution-asynchronous-errors"></a>

The following errors are specific to `DisassociateSolution` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INVALID\_UPDATE\_REQUEST | The requested change can't be performed after the offer set released. | 

## Release an offer set
<a name="release-offer-set"></a>

Use the `ReleaseOfferSet` change type to make an offer set available to buyers. Once released, the offer set transitions from Draft to Released state, becomes discoverable through AWS Marketplace, and associated offers can only be found as part of the unified package.

Released offer sets generate notifications at two levels: individual offers and the offer set itself. All individual offer notifications include the OfferSetId in existing notification channels ([email notifications](https://docs.aws.amazon.com/marketplace/latest/userguide/email-notifications.html) and [Amazon EventBridge events](https://docs.aws.amazon.com/marketplace/latest/userguide/notifications-eventbridge.html)). Offer set-level notifications are sent for key events such as when the offer set is released.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "ReleaseOfferSet",
      "Entity": {
        "Type": "OfferSet@1.0",
        "Identifier": "offerset-abc123"
      },
      "DetailsDocument": {}
    }
  ]
}
```

Provide information for the fields to add the `ReleaseOfferSet` change type:
+ `Entity` (object) (required) – The entity being updated.
  + `Identifier` (string) (required) – Your offer set ID. For more information, see [Identifier](catalog-apis.md#identifier).
  + `Type` (string) (required) – Must be `OfferSet@1.0`.
+ `DetailsDocument` (object) (required) – Empty object for this operation.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating information to ensure that it meets the AWS Marketplace guidelines. The validation process can take a few minutes.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

### Asynchronous Errors
<a name="release-offer-set-asynchronous-errors"></a>

The following errors are specific to `ReleaseOfferSet` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| MISSING\_BUYER\_NOTES | Provide BuyerNotes before releasing the offer set. | 
| MISSING\_OFFERS | Associate at least two offers to the offer set before releasing it. | 
| TOO\_MANY\_OFFERS\_PER\_PRODUCT | Associate only one offer per product to the offer set. | 
| INCONSISTENT\_OFFER\_CURRENCY\_CODE | Ensure all associated offers have matching CurrencyCode. | 
| INCONSISTENT\_OFFER\_AVAILABILITY\_END\_DATE | Ensure all associated offers have matching AvailabilityEndDate. | 
| INCONSISTENT\_OFFER\_TARGETING\_RULE | Ensure all associated offers have matching TargetingRule. | 
| INCOMPATIBLE\_OFFER\_TARGETING\_RULE | Only buyer-targeted offers can be associated to an offer set. | 
| EXPIRED\_OFFERS | Disassociate expired offers from the offer set or extend their AvailabilityEndDates. | 
| DRAFT\_OFFERS | Release all associated offers before releasing the offer set. | 
| INCOMPATIBLE\_SOLUTION\_STATE | Provide a solution in limited or public state. | 
| INVALID\_UPDATE\_REQUEST | The requested change can't be performed after the offer set released. | 

## Offer set lifecycle
<a name="offer-set-lifecycle"></a>

The offer set lifecycle consists of the following stages:

### Creation phase
<a name="creation-phase"></a>

Create the offer set entity in Draft state using the `CreateOfferSet` change type. The offer set receives a unique identifier and begins in Draft state.

### Configuration phase
<a name="configuration-phase"></a>

During configuration, you:
+ Add or update metadata using `UpdateInformation` (name, buyer notes)
+ Create individual private offers, specifying the `OfferSetId` during offer creation
+ Associate offers with the offer set using `AssociateOffers`
+ Optionally associate a solution using `AssociateSolution` for enhanced marketing content

**Important**  
The `OfferSetId` on individual offers is immutable and can only be set during offer creation. Before associating offers with an offer set using `AssociateOffers`, you must first create the individual offers and specify the `OfferSetId` during offer creation. If you need to include an existing offer that doesn't have the correct `OfferSetId`, you must create a new offer with the correct `OfferSetId` specified.

### Validation phase
<a name="validation-phase"></a>

Before releasing an offer set, ensure:
+ The offer set contains between 2 and 7 offers
+ All associated offers must be: 
  + In Released state
  + Active
  + Using the same currency
  + Targeting the same buyer AWS account ID(s)
  + Having identical expiration dates

### Release phase
<a name="release-phase"></a>

When ready, use the `ReleaseOfferSet` change type to transition the offer set from Draft to Released state. This makes the offer set discoverable to buyers through AWS Marketplace.

### Post-release management
<a name="post-release-management"></a>

**Expiration management:**
+ The effective expiration of an offer set is calculated as the earliest expiration date among all associated offers
+ You can modify individual offer expiration dates using existing offer management capabilities (`UpdateAvailability` change type)

**Offer set modifications:**

When buyers request changes to a released offer set, use the recreation workflow:

1. Create a new offer set entity

1. For offers that don't require changes, clone existing offers through the AWS Marketplace Management Portal

1. For offers requiring modifications, create new offers with the requested changes, specifying the new `OfferSetId`

1. Associate all offers (cloned and new) with the new offer set using `AssociateOffers`

1. Release the new offer set using `ReleaseOfferSet`

1. Expire the original offer set by setting the availability end date of associated offers

## IAM permissions for offer sets
<a name="iam-permissions-offer-sets"></a>

To work with offer sets using the AWS Marketplace Catalog API, you need specific IAM permissions. This section describes the required permissions for offer set operations and cross-entity authorization requirements.

### Required IAM actions
<a name="required-iam-actions"></a>

The following IAM actions are required for offer set operations:
+ `aws-marketplace:StartChangeSet` – Required for all offer set change types including create, update, associate, and release operations
+ `aws-marketplace:DescribeChangeSet` – Required to check the status and results of change set executions
+ `aws-marketplace:ListEntities` – Required to list offer sets in your account
+ `aws-marketplace:DescribeEntity` – Required to retrieve detailed information about an offer set

### Resource permissions
<a name="resource-permissions"></a>

Use the following ARN patterns to grant permissions on specific resources:
+ **Offer sets** – `arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/OfferSet/*`
+ **Individual offers** – `arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/Offer/*`
+ **Solutions** – `arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/Solution/*`

For more restrictive permissions, replace the wildcard (\*) with specific entity identifiers.

### Cross-entity authorization
<a name="cross-entity-authorization"></a>

Some offer set operations require permissions on both the offer set and the entities being associated:

**AssociateOffers**
+ `aws-marketplace:StartChangeSet` permission on the offer set entity
+ `aws-marketplace:StartChangeSet` permission with `AssociateWithOfferSet` change type on each individual offer entity being associated

**AssociateSolution**
+ `aws-marketplace:StartChangeSet` permission on the offer set entity
+ `aws-marketplace:StartChangeSet` permission with `AssociateWithOfferSet` change type on the solution entity being associated

**Note**  
Having only `DescribeEntity` (read-only) permission on offers or solutions is not sufficient for association operations. You must have `StartChangeSet` permission with the `AssociateWithOfferSet` change type on the entities being associated with the offer set.

### Example IAM policies
<a name="example-iam-policies"></a>

**Basic offer set management**

This policy provides permissions for basic offer set operations without cross-entity associations:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "aws-marketplace:StartChangeSet",
        "aws-marketplace:DescribeChangeSet",
        "aws-marketplace:ListEntities",
        "aws-marketplace:DescribeEntity"
      ],
      "Resource": [
        "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/OfferSet/*"
      ]
    }
  ]
}
```

**Cross-entity permissions for AssociateOffers**

This policy demonstrates the specific permissions and conditions required for AssociateOffers:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "aws-marketplace:StartChangeSet",
      "Resource": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/OfferSet/*",
      "Condition": {
        "StringEquals": {
          "catalog:ChangeType": ["AssociateOffers"]
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": "aws-marketplace:DescribeEntity",
      "Resource": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/Offer/*"
    },
    {
      "Effect": "Allow",
      "Action": "aws-marketplace:StartChangeSet",
      "Resource": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/Offer/*",
      "Condition": {
        "StringEquals": {
          "catalog:ChangeType": ["AssociateWithOfferSet"]
        }
      }
    }
  ]
}
```

For more restrictive permissions, replace the wildcard (\*) with specific entity identifiers.

**Cross-entity permissions for AssociateSolution**

This policy demonstrates the specific permissions and conditions required for AssociateSolution:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "aws-marketplace:StartChangeSet",
      "Resource": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/OfferSet/*",
      "Condition": {
        "StringEquals": {
          "catalog:ChangeType": ["AssociateSolution"]
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": "aws-marketplace:DescribeEntity",
      "Resource": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/Solution/*"
    },
    {
      "Effect": "Allow",
      "Action": "aws-marketplace:StartChangeSet",
      "Resource": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/Solution/*",
      "Condition": {
        "StringEquals": {
          "catalog:ChangeType": ["AssociateWithOfferSet"]
        }
      }
    }
  ]
}
```

For more restrictive permissions, replace the wildcard (\*) with specific entity identifiers.