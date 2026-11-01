

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Work with subsidiary authorizations using the AWS Marketplace APIs
<a name="work-with-subsidiary-authorizations"></a>

With the AWS Marketplace Catalog API, you can automate tasks for working with subsidiary authorizations.

A seller that operates through more than one AWS Marketplace seller account can maintain a product in one account and authorize its other accounts to sell that product through direct AWS Marketplace private offers (MPPO). The account that owns the product is the *primary account*. An account that is authorized to sell it is a *subsidiary account*. Although the *product* describes what is being sold in AWS Marketplace, the *subsidiary authorization* describes which of your other seller accounts can sell that product, which countries they can sell it in, and what dimensions they can include when they create offers.

Product ownership does not transfer. The primary account continues to own and maintain the listing, and a subsidiary account can't change listing content. On each offer it creates, the subsidiary account is the seller of record. It sets its own pricing and transacts in the currencies configured in its own account. It's charged AWS Marketplace fees on its own account and receives disbursement to its own bank account.

A subsidiary authorization has one rule and up to one term:
+ **SubsidiaryTargetingRule** – Specifies the single subsidiary account that the subsidiary authorization is accessible to. AWS Marketplace sets this rule from the `SubsidiaryAccountId` you provide at creation. You can't modify it afterward.
+ **BuyerTargetingTerm** – Specifies the countries in which the subsidiary account can sell the product, and the offer types it can create.

**Important**  
A subsidiary account can create direct private offers only. Public offers and resale authorizations created from an authorized product are not supported, and the Catalog API rejects them. For more information, see [Subsidiary authorization considerations](#subsidiary-authorization-limitations).

See the following resources:
+ For instructions on the buyer-facing and seller console experience, see [Creating private offers as an AWS Marketplace subsidiary seller](https://docs.aws.amazon.com/marketplace/latest/userguide/subsidiary-offers.html) in the *AWS Marketplace Seller Guide*.
+ For information about creating offers from a subsidiary authorization, see [Create an offer using a subsidiary authorization](work-with-private-offers.md#create-offer-using-subsidiary-authorization).

The following topics describe how to use the Catalog API to create and manage subsidiary authorizations.

**Topics**
+ [Subsidiary authorization prerequisites](#subsidiary-authorization-prerequisites)
+ [Subsidiary authorization considerations](#subsidiary-authorization-limitations)
+ [Creating a new subsidiary authorization](#create-subsidiary-authorization)
+ [Update subsidiary authorization details](#update-subsidiary-authorization-information)
+ [Release a subsidiary authorization](#release-subsidiary-authorization)
+ [Revoke a subsidiary authorization](#revoke-subsidiary-authorization)
+ [List your subsidiary authorizations](#list-subsidiary-authorizations)
+ [Describe an existing subsidiary authorization](#describe-subsidiary-authorization)
+ [Status reference](#subsidiary-authorization-status-reference)
+ [Error reference](#subsidiary-authorization-error-reference)

## Subsidiary authorization prerequisites
<a name="subsidiary-authorization-prerequisites"></a>

Before you create a subsidiary authorization, the following must be true.
+ **Both accounts are registered AWS Marketplace sellers, and the primary account is also registered as a partner.** The primary account and the subsidiary account must each be registered as a paid seller in AWS Marketplace, and each account must complete its own tax and banking information. One account can't complete seller registration, the tax interview, or Know Your Customer (KYC) verification on behalf of another.
+ **An accepted subsidiary connection exists between the two accounts.** From AWS Partner Central, the primary account sends a subsidiary connection request to the other account, and an administrator in that account signs in and accepts it. The Catalog API returns `INCOMPATIBLE_SUBSIDIARY_ACCOUNT_CONNECTION` if no active subsidiary connection exists.
+ **The primary account owns the product.** The entity named by `Resource.Arn` must be owned by the account sending the connection request. The Catalog API returns `INCOMPATIBLE_PRODUCT` otherwise.
+ **The subsidiary authorization service role exists in both the primary and subsidiary accounts.** Create the `AWSMarketplaceSubsidiaryAuthorizationServiceRole` service role in both accounts. AWS uses this role to share the authorization resource from the primary account to the subsidiary account. Without it, the subsidiary account can't use the authorization to create offers. If the role is missing or not assumable, the Catalog API returns `INCOMPATIBLE_ACCOUNT_STATE` for the primary account and `INCOMPATIBLE_SUBSIDIARY_ACCOUNT_STATE` for the subsidiary account.

  To create the role, in each account, in AWS Partner Central, choose **Settings**. On the **Service roles** tab, choose **Create Partner Central service role**, select **AWSMarketplaceSubsidiaryAuthorizationServiceRole**, and then choose **Save role**. For more information, see [Using roles for subsidiary authorization for AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/userguide/using-roles-for-subsidiary-authorization.html) in the *AWS Marketplace Seller Guide*.

**Important**  
The subsidiary account's own payment and tax setup determines where it can transact. A subsidiary account that has not completed AWS Marketplace payment setup can't create an offer, even if an active subsidiary authorization exists.

## Subsidiary authorization considerations
<a name="subsidiary-authorization-limitations"></a>

Consider the following before you use subsidiary authorizations.


| Area | Behavior | 
| --- | --- | 
| Offer types | A subsidiary account can create direct private offers from an authorized product. Public offers are not supported. | 
| Resale authorizations | A subsidiary account can't create a resale authorization (CPPO) from a product authorized to it by its primary account. It can still create resale authorizations for products it owns, using the normal flow described in [Work with resale authorizations using the AWS Marketplace APIs](work-with-resale-authorizations.md). | 
| Product changes | An authorization covers one product, and Resource.Arn is fixed after creation. To authorize a different product, create a second authorization for that product. If you change a product that is already authorized, for example by adding a pricing dimension, use UpdateInformation to update the authorization so that the subsidiary account can sell the latest version. | 
| Overlapping authorizations | Two authorizations for the same product and subsidiary account can't cover overlapping countries and dimension keys. A conflicting request fails with DUPLICATE\_SUBSIDIARY\_AUTHORIZATION. | 
| Geographic granularity | You specify authorized countries at the country level. Sub-country and state-level scoping is not supported. | 
| Pricing | A subsidiary authorization carries no pricing terms. The subsidiary account sets its own prices on the offers it creates. | 
| Fees and disbursement | AWS Marketplace listing and transaction fees are charged to the transacting subsidiary account, and disbursement is paid to that account's bank account. Fees and proceeds are not pooled, netted, or rebilled across accounts. | 

## Creating a new subsidiary authorization
<a name="create-subsidiary-authorization"></a>

You can use the Catalog API to create a new subsidiary authorization in AWS Marketplace.

If your request is processed successfully, the AWS Marketplace Catalog API generates a subsidiary authorization in `Draft` state. A draft is not visible to the subsidiary account and can't be used to create offers.

You can supply the `BuyerTargetingTerm` in the create request to configure the authorization in a single call. Alternatively, omit `Terms` and add them later with the `UpdateInformation` change type. Either way, the authorization must have a `BuyerTargetingTerm` before you can release it. After the authorization is complete, use the `UpdateAvailability` change type to set its status to `Active`, which validates the authorization and makes it visible to the subsidiary account.

To create a subsidiary authorization in `Draft` state, call the `StartChangeSet` API operation with the `CreateSubsidiaryAuthorization` change type, as shown in the following example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "CreateSubsidiaryAuthorization",
      "ChangeName": "CreateAuthorization",
      "Entity": {
        "Type": "SubsidiaryAuthorization@1.0"
      },
      "DetailsDocument": {
        "Name": "AnyCompany LATAM - Brazil",
        "Description": "Authorization for the Brazil seller account to sell Example Security Suite in BR and AR",
        "Resource": {
          "Arn": "arn:aws:aws-marketplace:us-east-1:111122223333:AWSMarketplace/SaaSProduct/prod-abcEXAMPLE23",
          "ResourceTypeDetails": {
            "ProductDetails": {
              "Dimensions": [
                { "Key": "users_id" },
                { "Key": "api_requests_id" }
              ]
            }
          }
        },
        "SubsidiaryAccountId": "444455556666",
        "Terms": [
          {
            "Type": "BuyerTargetingTerm",
            "PositiveTargeting": {
              "CountryCodes": ["BR", "AR"],
              "OfferTargeting": ["PrivateOffer"]
            }
          }
        ]
      }
    }
  ]
}
```

Provide information for the fields to add the `CreateSubsidiaryAuthorization` change type:
+ **Entity** (object) (required) – Your subsidiary authorization.
  + **Type** (string) (required) – The `Type` is always `SubsidiaryAuthorization@1.0`.
+ **DetailsDocument** (object) (required) – Specifics of the request.
  + **Name** (string) (required) – Name associated with the subsidiary authorization for better readability to you and to the subsidiary account. 1 to 100 characters.
  + **Description** (string) (optional) – A free-form text field available to add details about the subsidiary authorization. Up to 255 characters.
  + **Resource** (object) (required) – The AWS Marketplace entity being authorized.
    + **Arn** (string) (required) – The full ARN of the product to authorize. The product must be owned by the calling account.
    + **ResourceTypeDetails** (object) (required) – Metadata specific to the resource type.
      + **ProductDetails** (object) (required) – Product metadata.
        + **Dimensions** (list) (required) – The product dimensions that this authorization covers. Must be non-empty. Each entry contains a `Key` (string) (required), and optionally `Types` (list of strings), with valid values `Entitled` and `ExternallyMetered`. AWS Marketplace populates the dimension `Name`, `Description`, and `Unit` from the product.
  + **SubsidiaryAccountId** (string) (required) – The 12-digit AWS account ID of the subsidiary account that can describe and use this subsidiary authorization to create a private offer. It can't be the calling account.
  + **Terms** (list) (optional) – The terms of the authorization. If you omit `Terms`, the authorization is created with no terms and you must add them with `UpdateInformation` before you release it.
    + **BuyerTargetingTerm** (object) – Controls where the subsidiary account can sell and which offer types it can create.
      + **PositiveTargeting.CountryCodes** (list of strings) (optional) – ISO 3166-1 alpha-2 country codes in which the subsidiary account can sell the product. No duplicates. If you omit this field, it defaults to an empty list, and an empty list means all countries. Buyer eligibility is evaluated against the buyer's tax address.
      + **PositiveTargeting.OfferTargeting** (list of strings) (optional) – The offer types the subsidiary account can create. Defaults to `["PrivateOffer"]`. `PublicOffer` is not supported.

You don't supply `Status`, `CreatedDate`, `Issuer`, `Rules`, or the `Resource` fields `Name` and `Description`. AWS Marketplace populates these. Supplying them fails the request.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example111122223333abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:111122223333:AWSMarketplace/ChangeSet/example111122223333abcdef"
}
```

The change request is added to a queue and processed.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through the Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

When the request is complete (if the `Status` is `SUCCEEDED`), a new `SubsidiaryAuthorization` is generated. Although the `SUCCEEDED` status indicates that the `CreateSubsidiaryAuthorization` change type call is completed, the subsidiary authorization is still in `Draft` state.

The following shows the response from the `DescribeChangeSet` API operation.

```
{
  "ChangeSetId": "example111122223333abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:111122223333:AWSMarketplace/ChangeSet/example111122223333abcdef",
  "ChangeSetName": "Submitted by 111122223333",
  "StartTime": "2026-10-26T22:21:26Z",
  "EndTime": "2026-10-26T22:32:19Z",
  "Status": "SUCCEEDED",
  "ChangeSet": [
    {
      "ChangeType": "CreateSubsidiaryAuthorization",
      "Entity": {
        "Type": "SubsidiaryAuthorization@1.0",
        "Identifier": "subauthz-1a2bEXAMPLE34"
      },
      "DetailsDocument": {
        "Name": "AnyCompany LATAM - Brazil",
        "Description": "Authorization for the Brazil seller account to sell Example Security Suite in BR and AR",
        "Resource": {
          "Arn": "arn:aws:aws-marketplace:us-east-1:111122223333:AWSMarketplace/SaaSProduct/prod-abcEXAMPLE23",
          "ResourceTypeDetails": {
            "ProductDetails": {
              "Dimensions": [
                { "Key": "users_id" },
                { "Key": "api_requests_id" }
              ]
            }
          }
        },
        "SubsidiaryAccountId": "444455556666"
      },
      "ErrorDetailList": []
    }
  ]
}
```

**Synchronous Validations**

The following schema validations are specific to `CreateSubsidiaryAuthorization` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it fails with an HTTP response.


| Input field | Validation rule | HTTP code | 
| --- | --- | --- | 
| Name | Required<br />1 to 100 characters | 422 | 
| Description | Optional<br />0 to 255 characters | 422 | 
| Resource.Arn | Required<br />Must be a valid ARN whose service is `aws-marketplace` | 422 | 
| Resource.Name, Resource.Description | Not accepted<br />AWS Marketplace populates these from the product. Rejected as an additional property if supplied. | 422 | 
| Resource.ResourceTypeDetails.ProductDetails.Dimensions | Required<br />Non-empty list. Each element contains `Key`, and optionally `Types`. | 422 | 
| SubsidiaryAccountId | Required<br />A 12-digit AWS account ID. Can't equal the calling account. | 422 | 
| Terms | Optional<br />If supplied, must contain a `BuyerTargetingTerm`. | 422 | 
| BuyerTargetingTerm.PositiveTargeting.CountryCodes | Optional<br />Defaults to an empty list, which means all countries. If non-empty, must be valid ISO 3166-1 alpha-2 codes with no duplicates. | 422 | 
| BuyerTargetingTerm.PositiveTargeting.OfferTargeting | Optional<br />Defaults to `["PrivateOffer"]`. If present, a non-empty list of distinct values. | 422 | 
| Unknown properties | Rejected. No additional properties are allowed. | 422 | 

For errors returned asynchronously, see [Error reference](#subsidiary-authorization-error-reference).

## Update subsidiary authorization details
<a name="update-subsidiary-authorization-information"></a>

You can use the Catalog API to update the name, description, authorized dimensions, and terms of a subsidiary authorization. You can update an authorization in `Draft` or `Active` state. Updating an `Active` authorization takes effect immediately for new offers. It does not change offers the subsidiary account has already created or agreements already in place.

**Important**  
`UpdateInformation` replaces the fields it manages. Supply the complete intended state of `Name`, `Description`, `Resource`, and `Terms` on every call. Any value you omit is removed.

**Keep the authorization current with the product.** If you change a product that is already authorized, for example by adding a pricing dimension, the subsidiary account continues to sell only what the authorization covers. Call `UpdateInformation` with the new `Dimensions` list so that the subsidiary account can sell the latest version of the product.

You can't change `Resource.Arn`. An authorization covers one product. To authorize a different product, create a second authorization for that product with the `CreateSubsidiaryAuthorization` change type. You don't need to revoke this one, and a subsidiary account can hold authorizations for as many of your products as you choose to authorize.

To update a subsidiary authorization, call the `StartChangeSet` API operation with the `UpdateInformation` change type, as shown in the following example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "UpdateInformation",
      "ChangeName": "UpdateAuthorizationDetails",
      "Entity": {
        "Type": "SubsidiaryAuthorization@1.0",
        "Identifier": "subauthz-1a2bEXAMPLE34"
      },
      "DetailsDocument": {
        "Name": "AnyCompany LATAM - Brazil",
        "Description": "Authorization for the Brazil seller account to sell Example Security Suite in BR, AR, and MX",
        "Resource": {
          "Arn": "arn:aws:aws-marketplace:us-east-1:111122223333:AWSMarketplace/SaaSProduct/prod-abcEXAMPLE23",
          "ResourceTypeDetails": {
            "ProductDetails": {
              "Dimensions": [
                { "Key": "users_id" },
                { "Key": "api_requests_id" },
                { "Key": "storage_gb_id" }
              ]
            }
          }
        },
        "Terms": [
          {
            "Type": "BuyerTargetingTerm",
            "PositiveTargeting": {
              "CountryCodes": ["BR", "AR", "MX"],
              "OfferTargeting": ["PrivateOffer"]
            }
          }
        ]
      }
    }
  ]
}
```

Provide information for the fields to add the `UpdateInformation` change type:
+ **Entity** (object) (required) – Your subsidiary authorization.
  + **Type** (string) (required) – The `Type` is always `SubsidiaryAuthorization@1.0`.
  + **Identifier** (string) (required) – The unique ID of the subsidiary authorization to update.
+ **DetailsDocument** (object) (required) – The complete intended state of the fields you want the authorization to have.
  + **Name** (string) (required) – 1 to 100 characters.
  + **Description** (string) (required) – 0 to 255 characters.
  + **Resource** (object) (required) – Must contain the same `Arn` already stored on the authorization. Supply the complete `Dimensions` list you want the authorization to cover.
  + **Terms** (list) (required) – Must contain a `BuyerTargetingTerm`. Fields are the same as in [Creating a new subsidiary authorization](#create-subsidiary-authorization).

**Response Syntax**

```
{
  "ChangeSetId": "example111122223333abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:111122223333:AWSMarketplace/ChangeSet/example111122223333abcdef"
}
```

**Synchronous Validations**


| Input field | Validation rule | HTTP code | 
| --- | --- | --- | 
| Identifier | Required<br />1 to 50 characters | 422 | 
| Name | Required<br />1 to 100 characters | 422 | 
| Description | Required<br />0 to 255 characters | 422 | 
| Resource.Arn | Required<br />Must match the ARN stored on the authorization | 422 | 
| Resource.ResourceTypeDetails.ProductDetails.Dimensions | Required<br />Non-empty list | 422 | 
| Terms | Required<br />Must contain a `BuyerTargetingTerm` | 422 | 
| SubsidiaryAccountId | Not accepted on update | 422 | 

## Release a subsidiary authorization
<a name="release-subsidiary-authorization"></a>

Releasing a subsidiary authorization validates it and makes it visible to the subsidiary account, which can then use it to create private offers. You release an authorization by transitioning its status from `Draft` to `Active` with the `UpdateAvailability` change type.

To release a subsidiary authorization, call the `StartChangeSet` API operation as shown in the following example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "UpdateAvailability",
      "ChangeName": "ReleaseAuthorization",
      "Entity": {
        "Type": "SubsidiaryAuthorization@1.0",
        "Identifier": "subauthz-1a2bEXAMPLE34"
      },
      "DetailsDocument": {
        "Status": "Active"
      }
    }
  ]
}
```

Provide information for the fields to add the `UpdateAvailability` change type:
+ **Entity** (object) (required) – Your subsidiary authorization.
  + **Type** (string) (required) – The `Type` is always `SubsidiaryAuthorization@1.0`.
  + **Identifier** (string) (required) – The unique ID of the subsidiary authorization.
+ **DetailsDocument** (object) (required) – Specifics of the request.
  + **Status** (string) (required) – The status you want the authorization to have. Valid values are `Active` and `Restricted`.

**Response Syntax**

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:111122223333:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

**Note**  
A release fails with `MISSING_TERMS` if the authorization has no `BuyerTargetingTerm`. Add the term with `UpdateInformation`, then release again. For more information, see [Update subsidiary authorization details](#update-subsidiary-authorization-information).

## Revoke a subsidiary authorization
<a name="revoke-subsidiary-authorization"></a>

Revoking a subsidiary authorization stops the subsidiary account from creating any new offers from the authorized product. You revoke an authorization by transitioning its status to `Restricted` with the `UpdateAvailability` change type. You can revoke from either `Draft` or `Active`. Revoking a `Draft` authorization discards it.

**Important**  
Revoking a subsidiary authorization does not cancel offers the subsidiary account has already published, and does not terminate or change agreements already in place with buyers. An offer the subsidiary account published before you revoked the authorization can still be accepted by the buyer, and existing agreements continue according to their agreed terms. Revocation is permanent. To authorize the product again, create a new subsidiary authorization.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "UpdateAvailability",
      "ChangeName": "RevokeAuthorization",
      "Entity": {
        "Type": "SubsidiaryAuthorization@1.0",
        "Identifier": "subauthz-1a2bEXAMPLE34"
      },
      "DetailsDocument": {
        "Status": "Restricted"
      }
    }
  ]
}
```

**Response Syntax**

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:111122223333:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

AWS Marketplace notifies the subsidiary account and the primary account by email when an authorization is revoked from the `Active` state. Revoking an authorization that is still in `Draft` notifies only the primary account, because a draft is never visible to the subsidiary account.

## List your subsidiary authorizations
<a name="list-subsidiary-authorizations"></a>

The `[ListEntities](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_ListEntities.html)` API operation supports the `SubsidiaryAuthorization` entity type. A primary account sees the authorizations it issued. A subsidiary account sees the active authorizations shared with it.

**Request Syntax**

```
POST /ListEntities HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "EntityType": "SubsidiaryAuthorization",
  "EntityTypeFilters": {
    "SubsidiaryAuthorizationFilters": {
      "Status": { "ValueList": ["Active"] },
      "SubsidiaryAccountId": { "ValueList": ["444455556666"] }
    }
  },
  "EntityTypeSort": {
    "SubsidiaryAuthorizationSort": {
      "SortBy": "CreatedDate",
      "SortOrder": "DESCENDING"
    }
  },
  "MaxResults": 20
}
```

**Filters**

`EntityTypeFilters` supports a `SubsidiaryAuthorizationFilters` structure with the following filters.


| Filter | Description | Example | 
| --- | --- | --- | 
| EntityId | Filter by subsidiary authorization ID. Accepts 1 to 10 values. | { "ValueList": ["subauthz-1a2bEXAMPLE34"] } | 
| Status | Filter by status. Valid values are Draft, Active, and Restricted. Accepts 1 to 10 values. | { "ValueList": ["Active"] } | 
| ResourceId | Filter by the authorized product's ID. Accepts 1 to 10 values. | { "ValueList": ["prod-abcEXAMPLE23"] } | 
| ResourceName | Filter by the authorized product's name. Use ValueList for an exact match on 1 to 10 values, or WildCardValue for a substring match of at least 3 characters. | { "WildCardValue": "Security" } | 
| Name | Filter by the authorization name. Use ValueList for an exact match on 1 to 10 values, or WildCardValue for a substring match of at least 3 characters. | { "ValueList": ["AnyCompany LATAM - Brazil"] } | 
| SubsidiaryAccountId | Filter by the target subsidiary account ID. Accepts 1 to 10 values. | { "ValueList": ["444455556666"] } | 
| CreatedDate | Filter by creation date range, in ISO 8601 format. | { "DateRange": { "AfterValue": "2026-01-01", "BeforeValue": "2026-12-31" } } | 
| LastModifiedDate | Filter by last modified date range, in ISO 8601 format. | { "DateRange": { "AfterValue": "2026-01-01", "BeforeValue": "2026-12-31" } } | 

**Sorting**

`EntityTypeSort` supports a `SubsidiaryAuthorizationSort` structure. Valid `SortBy` values are `EntityId`, `Status`, `ResourceId`, `SubsidiaryAccountId`, `CreatedDate`, and `LastModifiedDate`. Valid `SortOrder` values are `ASCENDING` and `DESCENDING`. Sorting by `EntityId` and `LastModifiedDate` is also supported by the common `SortBy` attribute.

**Response Syntax**

```
{
  "EntitySummaryList": [
    {
      "Name": "AnyCompany LATAM - Brazil",
      "EntityType": "SubsidiaryAuthorization",
      "EntityId": "subauthz-1a2bEXAMPLE34",
      "EntityArn": "arn:aws:aws-marketplace:us-east-1:111122223333:AWSMarketplace/SubsidiaryAuthorization/subauthz-1a2bEXAMPLE34",
      "LastModifiedDate": "2026-10-26T14:00:00Z",
      "SubsidiaryAuthorizationSummary": {
        "Status": "Active",
        "ResourceId": "prod-abcEXAMPLE23",
        "ResourceName": "Example Security Suite",
        "SubsidiaryAccountId": "444455556666",
        "CreatedDate": "2026-10-26T22:32:19Z"
      }
    }
  ],
  "NextToken": null
}
```

Each entry includes the authorization's `Name` as a top-level attribute, alongside the common `EntityId`, `EntityArn`, `EntityType`, and `LastModifiedDate` attributes, and a `SubsidiaryAuthorizationSummary` structure with the following attributes.


| Attribute | Type | Description | 
| --- | --- | --- | 
| CreatedDate | String | The date the authorization was created, in ISO 8601 format. | 
| ResourceId | String | The authorized product's ID. | 
| ResourceName | String | The authorized product's name. | 
| SubsidiaryAccountId | String | The subsidiary account ID. | 
| Status | String | Draft, Active, or Restricted. | 

## Describe an existing subsidiary authorization
<a name="describe-subsidiary-authorization"></a>

You can use the `[DescribeEntity](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeEntity.html)` API operation to retrieve the full details of a subsidiary authorization.

**Request Syntax**

```
GET /DescribeEntity?catalog=AWSMarketplace&entityId=subauthz-1a2bEXAMPLE34 HTTP/1.1
```
+ **catalog** (string) (required) – The catalog related to the request. Fixed value: `AWSMarketplace`.
+ **entityId** (string) (required) – The unique ID of the `SubsidiaryAuthorization` to describe.

**Response Syntax**

```
{
  "EntityType": "SubsidiaryAuthorization@1.0",
  "EntityIdentifier": "subauthz-1a2bEXAMPLE34",
  "EntityArn": "arn:aws:aws-marketplace:us-east-1:111122223333:AWSMarketplace/SubsidiaryAuthorization/subauthz-1a2bEXAMPLE34",
  "LastModifiedDate": "2026-10-26T14:00:00Z",
  "DetailsDocument": {
    "Name": "AnyCompany LATAM - Brazil",
    "Description": "Authorization for the Brazil seller account to sell Example Security Suite in BR and AR",
    "Status": "Active",
    "CreatedDate": "2026-10-26T22:32:19Z",
    "Issuer": {
      "AccountId": "111122223333",
      "LegalName": "AnyCompany Inc."
    },
    "Resource": {
      "Arn": "arn:aws:aws-marketplace:us-east-1:111122223333:AWSMarketplace/SaaSProduct/prod-abcEXAMPLE23",
      "Name": "Example Security Suite",
      "Description": "Enterprise endpoint security suite",
      "ResourceTypeDetails": {
        "ProductDetails": {
          "Dimensions": [
            {
              "Name": "Users - Contract Pricing",
              "Description": "Licensed users",
              "Key": "users_id",
              "Unit": "Units",
              "Types": ["Entitled"]
            },
            {
              "Name": "API Requests - Contract Only",
              "Description": "API requests",
              "Key": "api_requests_id",
              "Unit": "Requests",
              "Types": ["Entitled"]
            }
          ]
        }
      }
    },
    "Terms": [
      {
        "Type": "BuyerTargetingTerm",
        "PositiveTargeting": {
          "CountryCodes": ["BR", "AR"],
          "OfferTargeting": ["PrivateOffer"]
        }
      }
    ],
    "Rules": [
      {
        "Type": "SubsidiaryTargetingRule",
        "AccountId": "444455556666",
        "LegalName": "AnyCompany Brazil Ltda"
      }
    ]
  }
}
```

The response contains the following:
+ **EntityType** (string) – The named type of the entity, which is `SubsidiaryAuthorization@1.0`.
+ **EntityIdentifier** (string) – The identifier of the entity.
+ **EntityArn** (string) – The ARN associated with the unique identifier for the entity.
+ **LastModifiedDate** (string) – The last modified date of the entity, in ISO 8601 format (for example: `2026-10-26T13:45:22Z`).
+ **DetailsDocument** (object) – This JSON object includes the following details of the entity:
  + **Status** (string) – `Draft`, `Active`, or `Restricted`.
  + **CreatedDate** (string) – The date the authorization was created, in ISO 8601 format.
  + **Issuer** (object) – The `AccountId` and `LegalName` of the primary account that created the authorization.
  + **Resource** (object) – The authorized product, including the dimensions covered by the authorization. AWS Marketplace populates `Name`, `Description`, and each dimension's `Name`, `Description`, and `Unit` from the product.
  + **Terms** (list) – The authorization's terms.
  + **Rules** (list) – Contains the `SubsidiaryTargetingRule` with the `AccountId` and `LegalName` of the subsidiary account that the authorization targets.

## Status reference
<a name="subsidiary-authorization-status-reference"></a>


| Status | Meaning | Valid transitions | 
| --- | --- | --- | 
| Draft | Created but not released. Not visible to the subsidiary account and can't be used to create offers. | To Active (release), to Restricted (discard) | 
| Active | Visible to the subsidiary account, which can use it to create private offers within the authorization's terms. | To Restricted (revoke) | 
| Restricted | Revoked. The subsidiary account can't create new offers from it. Offers already published and agreements already in place are unaffected. You can't update or re-release a restricted authorization. | None | 

## Error reference
<a name="subsidiary-authorization-error-reference"></a>

The system returns the following errors asynchronously. Retrieve them with the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation when a change set fails. The error code is returned in `ErrorCode` and the error message in `ErrorMessage`, in the `ErrorDetailList` of the failed change.

For errors returned immediately when you call `StartChangeSet`, see the **Synchronous Validations** table in each change type's section.

**Errors common to all change types**


| Error code | Error message | 
| --- | --- | 
| INCOMPATIBLE\_SUBSIDIARY\_ACCOUNT\_CONNECTION | Establish a subsidiary account connection with the subsidiary account before activating this subsidiary authorization. | 
| INCOMPATIBLE\_ACCOUNT\_STATE | The AWSMarketplaceSubsidiaryAuthorizationServiceRole in your account is missing or not assumable. Please ensure the role exists and has the correct trust policy before creating a subsidiary authorization. | 
| INCOMPATIBLE\_SUBSIDIARY\_ACCOUNT\_STATE | This subsidiary account hasn't completed their prerequisites for using subsidiary authorization. | 

**`CreateSubsidiaryAuthorization` errors**

The following table lists the errors specific to `CreateSubsidiaryAuthorization`. The errors common to all change types can also be returned and aren't repeated here.


| Error code | Error message | 
| --- | --- | 
| INCOMPATIBLE\_PRODUCT | Provide a product in your account. | 
| INCOMPATIBLE\_SUBSIDIARY\_ACCOUNT | This subsidiary account hasn't completed their prerequisites for using subsidiary authorization. | 
| INCOMPATIBLE\_PRODUCT\_DIMENSIONS | Returned with one of the following messages, depending on the problem with the `Dimensions` list:+  Use existing, available dimensions in the product. – A requested dimension key doesn't exist in the product. <br />+  Every product dimension tagged Metered or ExternallyMetered must be included in the request. – A metered dimension is left out. <br />+  The Dimensions list must include at least one product dimension tagged Entitled when the product has one or more Entitled dimensions available. – The product has `Entitled` dimensions and the request includes none.  | 

**`UpdateInformation` errors**

The following table lists the errors specific to `UpdateInformation`. The errors listed for `CreateSubsidiaryAuthorization` and `UpdateAvailability` can also be returned and aren't repeated here.


| Error code | Error message | 
| --- | --- | 
| INCOMPATIBLE\_STATUS | UpdateInformation request can't be performed after the subsidiary authorization is restricted. | 
| INCOMPATIBLE\_PRODUCT | The authorized product can't be changed. To authorize a different product, restrict this authorization and create a new one. | 

**`UpdateAvailability` errors**

The following table lists the errors specific to `UpdateAvailability`. The connection and service role errors listed in errors common to all change types aren't repeated here.


| Error code | Error message | 
| --- | --- | 
| INCOMPATIBLE\_STATUS | UpdateAvailability request can't be performed after the subsidiary authorization is restricted. | 
| MISSING\_TERMS | Provide a BuyerTargetingTerm. | 
| INVALID\_COUNTRY\_CODES | Provide supported country codes. | 
| DUPLICATE\_COUNTRY\_CODES | Provide unique list of country codes. | 
| DUPLICATE\_SUBSIDIARY\_AUTHORIZATION | Duplicate subsidiary authorization detected. An existing authorization already covers overlapping countries and dimension keys for the same subsidiary account and resource. Remove the overlapping countries or dimension keys before proceeding. | 