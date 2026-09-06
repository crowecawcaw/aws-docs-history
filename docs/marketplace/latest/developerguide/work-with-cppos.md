

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Work with channel partner private offers using the AWS Marketplace APIs
<a name="work-with-cppos"></a>

You can use the AWS Marketplace Catalog API to automate tasks for working with channel partner private offers (CPPOs). 

When you create or update a CPPO, the draft offer will contain the terms and rules from a Resale Authorization and will be invisible to the buyer. It's possible, but not required, to involve multiple personas in your organization to create a private offer. 

For example, one persona can be responsible for updating prices while a second persona can be responsible for updating the payment schedule. Then, a third persona can be responsible for updating legal terms. You can give a persona permission to update certain parts of an offer. However, you can give only read permissions to Resale Authorizations.

As a prerequisite for calling change types, you must have received one or more Resale Authorizations and be familiar working with AWS Marketplace Catalog API.

For more information, see [ Channel partner private offers](https://docs.aws.amazon.com/marketplace/latest/userguide/channel-partner-offers.html) in the *AWS Marketplace Seller Guide*.

The following topics describe how to use the Catalog API to create and update CPPOs:

**Topics**
+ [CPPO prerequisites](#cppo-prerequisites)
+ [Create a CPPO](#create-offer-using-resale-auth)
+ [Create a channel partner private replacement offer](#create-replacement-offer-using-resale-auth)
+ [Update markup](#update-markup)
+ [Update targeting configuration](#update-targeting-cppo)
+ [Update legal resources](#update-legal-terms-cppo)
+ [Update the discoverability of the CPPO](#update-availability-cppo)
+ [Define the expiration date of agreements](#update-validity-terms-cppo)
+ [Update pricing](#update-pricing-terms-cppo)
+ [Update payment schedule details](#update-payment-schedule-terms-cppo)
+ [Update net payment terms](#update-cppo-net-payment-terms)
+ [Publish the CPPO](#release-offer-cppo)
+ [Define an existing CPPO](#describe-entity-cppo)

## CPPO prerequisites
<a name="cppo-prerequisites"></a>

Service-linked role for ResaleAuthorization (SLR) setup is a mandatory pre-requisite to use resale authorization to create a CPPO. To use Resale Authorization, both independent software vendors (ISVs) and AWS Marketplace Channel Partners must create a service-linked role that provides resource-sharing permissions to AWS. If both groups don't perform this prerequisite, AWS can't share the authorization resource from the ISV to the AWS Marketplace Channel Partner. For more information, see [Using roles for Resale Authorization for AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/userguide/using-roles-for-resale-authorization.html) in the *AWS Marketplace Seller Guide*.

## Create a CPPO
<a name="create-offer-using-resale-auth"></a>

You use a Resale Authorization targeted to you to create a channel partner private offer (CPPO) in `Draft` state in AWS Marketplace. 

If your request is processed successfully, AWS Marketplace Catalog API generates an offer in `Draft` state for you with Resale Authorization terms. You can use `DescribeEntity` to see the terms applied to the draft offer from Resale Authorization. This is an incomplete offer and not visible to buyers in AWS Marketplace. You then use change types associated with the CPPO to complete the offer.

After the offer is completed, you use the `ReleaseOffer` change type to complete the offer creation process and release the offer. This will validate the entire offer and make your offer visible to buyers in AWS Marketplace.

To create a channel partner private offer, call the `StartChangeSet` API operation with the `CreateOfferUsingResaleAuthorization` change type, as shown in the following example. 

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "CreateOfferUsingResaleAuthorization",
      "Entity": {
        "Type": "Offer@1.0"
      },
      "DetailsDocument": {
        "ResaleAuthorizationId": "resaleauthz-123456789",
        "Name": "Test Offer",
        "OfferSetId": "offerset-b3f9EXAMPLE27"
      }
    }
  ]
}
```

Provide information for the fields to add the `CreateOfferUsingResaleAuthorization` change type:
+ **Entity** (object) (required) – Your CPPO. 
  + **Type** (string) (required) – The `Type` is always `Offer@1.0`. 
+ **DetailsDocument** (object) (required) – The JSON value of specifics of the request.
  + **ResaleAuthorizationId** (string) (required) – The unique identifier that includes product, terms, and rules that are being offered. Channel partners can add additional terms and rules using update change types. ResaleAuthorization must be available and targeted to you as a partner.
  + **Name** (string) (optional) – The name associated with the offer for better readability. It is displayed as a part of the agreement information.
  + **OfferSetId** (string) (optional) – The ID of the offer set to associate this offer with. Only specify this field when creating an offer that will be part of an offer set. If OfferSetId is not provided, an individual offer will be created that can be purchased standalone. Note that specifying an OfferSetId during offer creation only indicates your intent to associate the offer with that offer set. To complete the association, you must [use the AssociateOffers change type](work-with-offer-sets.md#associate-offers) after the offer is created.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. 

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

The response to this request gives you the status of the request. If the status is `SUCCEEDED`, then a new `OfferId` is generated.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef",
  "ChangeSetName": "Submitted by 123456789012",
  "StartTime": "2021-05-27T22:21:26Z",
  "EndTime": "2021-05-27T22:32:19Z",
  "Status": "SUCCEEDED",
  "ChangeSet": [
    {
      "ChangeType": "CreateOfferUsingResaleAuthorization",
      "Entity": {
        "Type": "Offer@1.0",
        "Identifier": "offer-123456789"
      },
      "DetailsDocument": {
        "ResaleAuthorizationId": "resaleauthz-123456789",
        "Name": "Test Offer"
      },
      "ErrorDetailList": []
    }
  ]
}
```

You can use the `GET` `DescribeEntity` request to describe the draft offer rules and terms created from `ResaleAuthorization` in the AWS Marketplace Catalog API Reference. For more information, see [`DescribeChangeSet`](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html).

**Terms and rules from ResaleAuthorization**
+ **LegalTerms** – Provisions describing legal terms, such as the EULA in the ResaleAuthorization will be added to the draft offer. You can add legal terms using the `UpdateLegalTerms` change type. For more information, see [`UpdateLegalTerms`](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/cppos.html#update-legal-terms-cppo).
+ **PricingTerms** – All the pricing terms (`ConfigurableUpfrontPricingTerm`, `FixedUpfrontPricingTerm`, `UsageBasedPricingTerm`, `PaymentScheduleTerms`) described by the Manufacturer in the ResaleAuthorization will be added to the draft offer. You can choose to increase the pricing (for each dimension) for your targeted buyers using the `UpdateMarkup` change type. For more information, see [`UpdateMarkup`](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/cppos.html#update-markup) in this guide.
+ **PaymentTerms** – If the manufacturer has defined the Future Payment Schedule in the ResaleAuthorization, then you will be able to see the payment terms in the draft offer. You can choose to increase the payment schedule amount for your targeted buyers using the `UpdateMarkup` change type. If you want to set the payment schedule for your buyers, you can use `UpdatePaymentScheduleTerms`. For more information, see [`UpdatePaymentScheduleTerms`](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/cppos.html#update-payment-schedule-terms-cppo).
+ **TargetingRule** – If the ResaleAuthorization is targeted to specific buyers, then channel partners can give private offers to a subset of buyers using PositiveTargeting. By default, the rule will include all the buyers from ResaleAuthorization. You can select specific buyers and update the draft offer using the `UpdateTargeting` change type. For more information, see [`UpdateTargeting`](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/cppos.html#update-targeting-cppo).

```
{
  "EntityType": "Offer@1.0",
  "EntityIdentifier": "offer-a5EXAMPLEwzpu@1",
  "EntityArn": "arn:aws:aws-marketplace:us-east-1:444555666777:AWSMarketplace/Offer/offer-a5oEXAMPLEzpu",
  "LastModifiedDate": "2021-03-10T21:57:16Z",
  "DetailsDocument": {
    "Id": "offer-3rb23tu92rn",
    "Name": "Test Offer",
    "Description": "Worldwide private offer for Test Product",
    "ProductId": "prod-0bc848d78b51",
    "ResaleAuthorizationId": "resaleauthz-123456789",
    "Terms": [
      {
        "Type": "LegalTerm",
        "Documents": [
          {
            "Type": "CustomEula",
            "Url": "https://s3.amazonaws.com/EULA/custom-eula-1234.txt"
          }
        ]
      },
      {
        "Type": "ConfigurableUpfrontPricingTerm",
        "CurrencyCode": "USD",
        "RateCards": [
          {
            "Selector": {
              "Type": "Duration",
              "Value": "P12M"
            },
            "RateCard": [
              {
                "DimensionKey": "m3.large",
                "Price": "300.00"
              },
              {
                "DimensionKey": "m4.xlarge",
                "Price": "400.00"
              }
            ],
            "Constraints": {
              "MultipleDimensionSelection": "Allowed",
              "QuantityConfiguration": "Allowed"
            }
          }
        ]
      },
      {
        "Type": "UsageBasedPricingTerm",
        "CurrencyCode": "USD",
        "RateCards": [
          {
            "RateCard": [
              {
                "DimensionKey": "m3.large",
                "Price": "0.10"
              },
              {
                "DimensionKey": "m4.xlarge",
                "Price": "0.20"
              }
            ]
          }
        ]
      },
      {
        "Type": "PaymentScheduleTerm",
        "CurrencyCode": "USD",
        "Schedule": [
          {
            "ChargeDate": "2020-12-01T00:00:00.000Z",
            "ChargeAmount": "1000.00"
          },
          {
            "ChargeDate": "2021-06-15T00:00:00.000Z",
            "ChargeAmount": "1250.00"
          }
        ]
      }
    ],
    "Rules": [
      {
        "Type": "TargetingRule",
        "PositiveTargeting": {
          "BuyerAccounts": [
            "111222333444"
          ]
        }
      }
    ]
  }
}
```

**Synchronous Validations**

The following schema validations are specific to `CreateOfferUsingResaleAuthorization` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | HTTP code | 
| --- | --- | --- | 
| Name | Required<br />Length must be between 1 and 150 characters | 422 | 
| Description | Required<br />Length must be between 1 and 255 characters | 422 | 
| ResaleAuthorizationId | Required<br />Length must be between 1 and 50 characters | 422 | 
| ResaleAuthorizationId | ResaleAuthorization must be targeted to the channel partner. | 422 | 
| ResaleAuthorizationId | ResaleAuthorization must be active | 422 | 
| Channel Partner | Channel Partner must be paid seller in AWS Marketplace | 422 | 

**Asynchronous Errors**

The following errors are specific to `CreateOfferUsingResaleAuthorization` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code  | Error message | 
| --- | --- | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | Use a ResaleAuthorization in active state. | 
| INCOMPATIBLE\_PRODUCT | OfferSetId isn't supported in offers for the product. | 

## Create a channel partner private replacement offer
<a name="create-replacement-offer-using-resale-auth"></a>

You can use the Catalog API to create a channel partner private replacement offer in AWS Marketplace.

You use the `ResaleAuthorization` targeted to you and an Agreement of which you are the proposer to create a channel partner private replacement offer in `Draft` state in the Catalog API by calling `StartChangeSet` with the `CreateReplacementOfferUsingResaleAuthorization` change type, as shown in the following example. Replacement offers can be used to replace an agreement from a previous offer before it ends.

`CreateReplacementOfferUsingResaleAuthorization` will create a draft offer with the agreement acceptor in targeting. This targeting cannot be changed afterwards. The draft offer will also contain the source offer id of the agreement.

To create a channel partner private replacement offer, call the `StartChangeSet` API operation with the `CreateReplacementOfferUsingResaleAuthorization` change type, as shown in the following example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "CreateReplacementOfferUsingResaleAuthorization",
      "Entity": {
        "Type": "Offer@1.0"
      },
      "DetailsDocument": {
        "ResaleAuthorizationId": "2bd2c761-3b7f-3771-a9a7-e8ad36517698",
        "Name": "CAPI-saas-abo-contract-fps",
        "AgreementId": "agmt-f2ooEXAMLEamtm7mjj0j59gu"
      }
    }
  ]
}
```

Provide information for the fields to add the `CreateReplacementOfferUsingResaleAuthorization` change type:
+ **Entity** (object) (required) – Your CPPO. 
  + **Type** (string) (required) – The `Type` is always `Offer@1.0`. 
+ **DetailsDocument** (object) (required) – The JSON value of specifics of the request.
  + **ResaleAuthorizationId** (string) (required) – `ResaleAuthorizationId` is the unique identifier which includes product, terms and rules are being offered. Channel partners can add additional terms and rules using Update change types.

    `ResaleAuthorization` must be available and targeted to you as a partner.
  + **Name** (string) (optional) – `Name` associated with the offer for better readability to you and your customers. It will be displayed as part of Agreement information as well.
  + **AgreementId** (string) (required) – `AgreementId` is the unique identifier of the agreement created when the targeted buyer accepted the previous offer you are trying to replace

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. 

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

**Synchronous Validations**

The following schema validations are specific to `CreateReplacementOfferUsingResaleAuthorization` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | 
| --- | --- | 
| Name | Length must be between 1 and 150 characters | 
| AgreementId | Provided agreement must be active Provided agreement must exist<br />Provided agreement must be owned by Channel Partner | 
| ResaleAuthorizationId | Required<br />Length must be between 1 and 50 characters | 
| ResaleAuthorizationId | ResaleAuthorization must be targeted to the channel partner. | 
| ResaleAuthorizationId | ResaleAuthorization must be active | 
| Channel Partner | Channel Partner must be paid seller in AWS Marketplace | 

**Asynchronous Errors**

The following errors are specific to `CreateReplacementOfferUsingResaleAuthorization` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code  | Error message | 
| --- | --- | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | Use a ResaleAuthorization in active state. | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | The ResaleAuthorization must be for the same product that is associated with the agreement. | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | Use a ResaleAuthorization targeted to the acceptor of the agreement. | 

## Update markup
<a name="update-markup"></a>

You can use the Catalog API to update pricing terms by a percentage value in your offer in AWS Marketplace.

This will apply the given percentage markup on all pricing terms and payment terms (for future payment schedules) that are defined by the manufacturer in the ResaleAuthorization. Any existing markup will be overwritten. You can view updated pricing and payment terms using `DescribeEntity`.

To update markup, call the `StartChangeSet` API operation with the `UpdateMarkup` change type, as shown in the following example. 

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "UpdateMarkup",
      "Entity": {
        "Type": "Offer@1.0",
        "Identifier": "offer-123456789"
      },
      "DetailsDocument": {
        "Percentage": "5.0"
      }
    }
  ]
}
```

Provide information for the fields to add the `UpdateMarkup` change type:
+ **Entity** (object) (required) – Your CPPO. 
  + **Type** (string) (required) – The `Type` is always `Offer@1.0`. 
  + **Identifier** (string) (required) – Your offer ID. For more information, see [Identifier](catalog-apis.md#identifier).
+ **DetailsDocument** (object) (required) – The JSON value of specifics of the request.
  + **Percentage** (string) (required) – Percentage value will be added to the manufacturer pricing or payment terms.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating information with the AWS Marketplace Seller Operations team to ensure it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours. 

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

**Synchronous Validations**

The following schema validations are specific to `UpdateMarkup` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | 
| --- | --- | 
| Percentage | Required<br />Data type is "String" <br />Must be non-negative <br />Allow up to 9 decimals | 

**Asynchronous Errors**

The following errors are specific to `UpdateMarkup` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code  | Error message | 
| --- | --- | 
| INCOMPATIBLE\_MARKUP | The requested change can't be performed after the offer is released. | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | MarkupPercentage can't be updated when PaymentScheduleTerm or FixedUpfrontPricingTerm are present in offer and not present in ResaleAuthorization. | 
| INCOMPATIBLE\_TERMS | Use either UpdatePaymentScheduleTerms with specific payment amount or UpdateMarkup with a single markup percentage for the scheduled dates. | 
| INVALID\_MARKUP\_PERCENTAGE | UpdateMarkup can only be invoked for offers created using ResaleAuthorization. | 

## Update targeting configuration
<a name="update-targeting-cppo"></a>

You can use the Catalog API to replace the existing targeting configuration completely in AWS Marketplace.

Any existing targeting options that are not included in the latest request will be removed from the offer. Manufacturers can mention specific targeted buyers in `ResaleAuthorization`. Channel partners can give private offers to a subset of buyers using `PositiveTargeting` in the `UpdateTargeting` change type.

To update targeting configurations of your offer, call the `StartChangeSet` API operation with the `UpdateTargeting` change type, as shown in the following example. 

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "UpdateTargeting",
      "Entity": {
        "Type": "Offer@1.0",
        "Identifier": "offer-123456789"
      },
      "DetailsDocument": {
        "PositiveTargeting": {
          "CountryCodes": [
            "US",
            "CA"
          ],
          "BuyerAccounts": [
            "111222333444"
          ]
        },
        "NegativeTargeting": {
          "CountryCodes": [
            "XX"
          ]
        }
      }
    }
  ]
}
```

Provide information for the fields to add the `UpdateTargeting` change type:
+ **Entity** (object) (required) – Your CPPO. 
  + **Type** (string) (required) – The `Type` is always `Offer@1.0`. 
  + **Identifier** (string) (required) – Your offer ID. For more information, see [Identifier](catalog-apis.md#identifier).
+ **DetailsDocument** (object) (required) – The JSON value of specifics of the request.
  + **PositiveTargeting** (object) (optional) – Positive targeting defines the criteria which any buyer's profile should fulfill in order to be allowed to access the offer. This field is optional, but at least one targeting option should be provided when this field is present.
    + **CountryCodes** (array of strings) (optional) – List as option for allowing targeting based on country. If the intention isn't to target the offer to a country, this field should be omitted. If it's present, the list must contain at least one country code. Each element in this list should be a valid 2-letter country code, using this format: ISO 3166-1 alpha-2.
    + **BuyerAccounts** (array of strings) (optional) – List as an option to allow targeting based on AWS accounts (also known as, Private Offer). If the intention is to not target the offer to an AWS account, this field should be omitted.
  + **NegativeTargeting** (object) (optional) – Negative targeting defines the criteria which any customer's profile should fulfill to be restricted to access the offer. Although this field is optional, at least one targeting option should be provided when this field is present.
    + **CountryCodes** (array of strings) (required) – List as option for allowing targeting based on country. If the intention isn't to target the offer to a specific country, then this field should be omitted. If it's present, the list must contain at least one country code. Each element in this list should be a valid 2-letter country code using this format: ISO 3166-1 alpha-2.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating information to ensure that it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours. 

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

**Synchronous Validations**

The following schema validations are specific to `UpdateTargeting` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | HTTP code | 
| --- | --- | --- | 
|  Details  | Required | 422 | 
|  PositiveTargeting | Optional | 422 | 
| NegativeTargeting | Optional | 422 | 
| PositiveTargeting.CountryCodes | Optional<br />Country codes must be valid (ISO 3166-1 alpha-2) | 422 | 
| PositiveTargeting.BuyerAccounts | Optional<br />AWS account IDs must be in valid format (12-digit number)<br />Must not contain more than 25 accounts | 422 | 
| NegativeTargeting.CountryCodes | Optional<br />Country codes must be valid (ISO 3166-1 alpha-2) | 422 | 
| NegativeTargeting.BuyerAccounts | Must not be provided (negative targeting on BuyerAccounts isn't supported) | 422 | 

**Asynchronous Errors**

The following errors are specific to `UpdateTargeting` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INVALID\_BUYER\_ACCOUNTS | Provide valid buyer accounts. Invalid accounts: [x]. | 
| INVALID\_COUNTRY\_CODES | Provide supported country codes. | 
| INVALID\_TARGETING | Use either negative or positive targeting on the same attribute. | 
| INCOMPATIBLE\_PRODUCT | Country-based targeting isn't supported for the product. | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | Provide BuyerAccounts that are compatible with the ResaleAuthorization. | 
| INCOMPATIBLE\_TARGETING | The requested change can't be performed after the offer is released. | 
| INCOMPATIBLE\_TARGETING | The requested change can't be performed after the offer is expired. | 
| INCOMPATIBLE\_TARGETING | Targeting can't be updated on a replacement offer. If the buyer isn't associated with the provided AgreementId, then create a new private offer by providing an AgreementId associated with the buyer. | 
| TOO\_MANY\_BUYER\_ACCOUNTS | Provide BuyerAccounts within the allowed limits. | 

## Update legal resources
<a name="update-legal-terms-cppo"></a>

You can use the Catalog API to merge the Resale Authorization legal terms and replace the existing legal terms completely in AWS Marketplace.

This change doesn't affect existing agreements. The legal terms that aren't included in the latest request will be removed from the offer. You can view the merged legal terms by calling `DescribeEntity`.

To update legal terms of your offer, call the `StartChangeSet` API operation with the `UpdateLegalTerms` change type, as shown in the following example. 

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "UpdateLegalTerms",
      "Entity": {
        "Type": "Offer@1.0",
        "Identifier": "offer-123456789"
      },
      "DetailsDocument": {
        "Terms": [
          {
            "Type": "LegalTerm",
            "Documents": [
              {
                "Type": "CustomEula",
                "Url": "https://s3.amazonaws.com/EULA/custom-eula-1234.txt"
              }
            ]
          }
        ]
      }
    }
  ]
}
```

Provide information for the fields to add the `UpdateLegalTerms` change type:
+ **Entity** (object) (required) – Your CPPO. 
  + **Type** (string) (required) – The `Type` is always `Offer@1.0`. 
  + **Identifier** (string) (required) – Your offer ID. For more information, see [Identifier](catalog-apis.md#identifier).
+ **DetailsDocument** (object) (required) – The JSON value of specifics of the request.
  + **Terms** (array of structures) (required) – List of legal terms that you want to update. Supported legal terms are:
  + **LegalTerm** (object) (required) – Defines the list of text agreements to be proposed to the acceptors. One example of such an agreement is the end user license agreement (EULA).
    + **Type** (string) (required) – Category of term being updated.
    + **Documents** (array of structures) (required) – List of references to legal resources to be proposed to the buyers. One example of such a resource is the end user license agreement (EULA). Each reference is made up of a Type and a URL:
      + **Type** (string) (required) – Type of document. Available document types are:
        + **CustomEula** – A custom EULA provided by you as seller. A URL for a EULA stored in an accessible S3 bucket is required for this document type.
        + **StandardEula** – Standard Contract For AWS Marketplace (SCMP). For more information about SCMP, see the AWS Marketplace Seller Guide. You don't provide a URL for this type because it is managed by AWS Marketplace.
      + **Url** (string) (conditionally required) – A URL to the legal document for buyers to read. Required when `Type` is one of the following [`CustomEula`].
      + **Version** (string) (conditionally required) – A version of standard contracts provided by AWS Marketplace. This is required when `Type` is `StandardEula`. Available versions are:
        + **2022-07-14** – This version of the Standard Contract for AWS Marketplace is available from this Amazon S3 bucket: [https://s3.amazonaws.com/aws-mp-standard-contracts/Standard-Contact-for-AWS-Marketplace-2022-07-14.pdf](https://s3.amazonaws.com/aws-mp-standard-contracts/Standard-Contact-for-AWS-Marketplace-2022-07-14.pdf)

A change set is created for your request. The response to this request gives you the ID for the change set.

**Response Syntax**

```
{
"ChangeSetId": "example123456789012abcdef", "ChangeSetArn": "arn:aws:aws-marketplace:us-east-
1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating information with the AWS Marketplace Seller Operations team to ensure it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours. You can check the status of the request through the AWS Marketplace Management Portal, or in the Catalog API with the `DescribeChangeSet` action.

**Synchronous Validations**

The following schema validations are specific to `UpdateLegalTerms` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | HTTP code | 
| --- | --- | --- | 
| Terms | Required<br />Only LegalTerm is allowed in the list<br />List size must be 1 | 422 | 
| Terms[].LegalTerm.Documents | Required | 422 | 
| Terms[].LegalTerm.Documents[].Type | Required<br />Allowed values:+  CustomEula <br />+  StandardEula  | 422 | 
| Terms[].LegalTerm.Documents[].Url | Required and must be a valid URL when "Type" is one of+  CustomEula  | 422 | 

**Asynchronous Errors**

The following errors are specific to `UpdateLegalTerms` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code  | Error message | 
| --- | --- | 
| INCOMPATIBLE\_TERMS | The requested change can't be performed after the offer is released. | 
| INCOMPATIBLE\_TERMS | The requested change can't be performed after the offer is expired. | 
| INVALID\_LEGAL\_DOCUMENTS | Provide URLs for legal documents stored in accessible S3 buckets. | 
| INVALID\_LEGAL\_DOCUMENTS | Only the most recent version of StandardEula is supported for new offers. | 
| INVALID\_LEGAL\_DOCUMENTS | Provide legal documents in the supported file formats. | 
| INVALID\_LEGAL\_DOCUMENTS | Provide legal documents using the supported document types. | 
| LIMIT\_EXCEEDED\_LEGAL\_DOCUMENT\_SIZE | Provide legal documents within the allowed size limits. | 

## Update the discoverability of the CPPO
<a name="update-availability-cppo"></a>

You can use the Catalog API to manage the discoverability of your offer in AWS Marketplace. This change type doesn't affect existing agreements. 

You can either choose to set a specific date in the future to restrict the discoverability of your offer or in the past to expire your offer.

To manage the discoverability of your offer, call the `StartChangeSet` API operation with the `UpdateAvailability` change type, as shown in the following example. 

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "UpdateAvailability",
      "Entity": {
        "Type": "Offer@1.0",
        "Identifier": "offer-123456789"
      },
      "DetailsDocument": {
        "AvailabilityEndDate": "2024-05-31"
      }
    }
  ]
}
```

Provide information for the fields to add the `UpdateAvailability` change type:
+ **Entity** (object) (required) – Your CPPO. 
  + **Type** (string) (required) – The `Type` is always `Offer@1.0`. 
  + **Identifier** (string) (required) – Your offer ID. For more information, see [Identifier](catalog-apis.md#identifier).
+ **DetailsDocument** (object) (required) – The JSON value of specifics of the request.
  + **AvailabilityEndDate** (string) – Date until when the offer is discoverable and purchasable in AWS Marketplace. You can choose to set a specific date in the future to restrict the availability or in the past to expire the offer. Dates are represented in `YYYY-MM-DD` format. Offer expires at 23:59:59.999 UTC on the date provided.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating information to ensure that it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours. 

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

**Synchronous Validations**

The following schema validations are specific to `UpdateAvailability` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | HTTP code | 
| --- | --- | --- | 
| AvailabilityEndDate | Required<br />Format: "YYYY-MM-DD" | 422 | 

**Asynchronous Errors**

The following errors are specific to `UpdateAvailability` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INVALID\_AVAILABILITY\_END\_DATE | AvailabilityEndDate isn't supported for public offers. | 
| INVALID\_AVAILABILITY\_END\_DATE | Provide a future AvailabilityEndDate. | 
| INVALID\_AVAILABILITY\_END\_DATE | Provide an AvailabilityEndDate that is before AgreementEndDate. | 
| MISSING\_AVAILABILITY\_END\_DATE | Provide an AvailabilityEndDate that is before the agreement's end date. | 

## Define the expiration date of agreements
<a name="update-validity-terms-cppo"></a>

You can use the Catalog API to define the expiration date of the agreements that are created using this offer in AWS Marketplace.

This change does not affect existing agreements. The manufacturer could mention maximum agreement start date in a Resale Authorization. However, channel partners can't provide an agreement start date later than that date.

To define the expiration date of agreements, call the `StartChangeSet` API operation with the `UpdateValidityTerms` change type, as shown in the following example. 

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "UpdateValidityTerms",
      "Entity": {
        "Type": "Offer@1.0",
        "Identifier": "offer-123456789"
      },
      "DetailsDocument": {
        "Terms": [
          {
            "Type": "ValidityTerm",
            "AgreementDuration": "P12M",
            "AgreementStartDate": "2021-08-01",
            "AgreementEndDate": "2022-08-01"
          }
        ]
      }
    }
  ]
}
```

Provide information for the fields to add the `UpdateValidityTerms` change type:
+ **Entity** (object) (required) – Your CPPO. 
  + **Type** (string) (required) – The `Type` is always `Offer@1.0`. 
  + **Identifier** (string) (required) – Your offer ID. For more information, see [Identifier](catalog-apis.md#identifier).
+ **DetailsDocument** (object) (required) – The JSON value of specifics of the request.
  + **Terms** (array of structures) **–** List of validity terms that you want to update. Supported validity terms are:
    + **ValidityTerm** (object) **–** Defines the conditions that will keep an agreement, created from this offer, valid.
      + **Type** (string) **–** Category of the term being updated.
      + **AgreementDuration** (string) **–** Defines the duration that the agreement remains active. If `AgreementStartDate` isn't provided, agreement duration is relative to the agreement signature time. The duration is represented in the ISO\_8601 format.
      + **AgreementStartDate** (string) **–** Defines the date when agreement starts. `AgreementStartDate` is represented in YYYY-MM-DD format. The agreement starts at 00:00:00.000 UTC on the date provided. If `AgreementStartDate` isn't provided, agreement start date is determined based on agreement signature time.
      + **AgreementEndDate** (string) **–** Defines the date when the agreement ends. The `AgreementEndDate` is represented in YYYY-MM-DD format. The agreement ends at 23:59:59.999 UTC on the date provided. If `AgreementEndDate` isn't provided, the agreement end date is determined by the validity of individual terms.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating information to ensure that it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours. 

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

**Synchronous Validations**

The following schema validations are specific to `UpdateValidityTerms` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | HTTP code | 
| --- | --- | --- | 
| Terms | Required<br />Only "ValidityTerm" is allowed in the list <br />Must be empty or contain only 1 term | 422 | 
|  Terms[].ValidityTerm  | Supported use cases:<br />1. ValidityTerm with only AgreementDuration<br />2. ValidityTerm with only AgreementStartDate<br />3. ValidityTerm with only AgreementEndDate<br />4. ValidityTerm with both AgreementStartDate and AgreementEndDate | 422 | 
| Terms[].ValidityTerm.AgreementDuration | Optional<br />Represented in ISO\_8601 format. | 422 | 
| Terms[].ValidityTerm.AgreementStartDate | Optional<br />Format: "YYYY-MM-DD" | 422 | 
| Terms[].ValidityTerm.AgreementEndDate | Optional<br />Format: "YYYY-MM-DD" | 422 | 

**Asynchronous Errors**

The following errors are specific to `UpdateValidityTerms` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INCOMPATIBLE\_AGREEMENT | AgreementStartDate can't be in the future when the current agreement to be replaced isn't future dated. | 
| INCOMPATIBLE\_AGREEMENT\_END\_DATE | AgreementEndDate can't be updated after the offer is released. | 
| INCOMPATIBLE\_AGREEMENT\_START\_DATE | AgreementStartDate can't be updated after the offer is released. | 
| INCOMPATIBLE\_PRODUCT | AgreementStartDate in the future isn't supported. | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | Ensure the duration between AgreementStartDate and AgreementEndDate is compatible with the ResaleAuthorization. | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | Ensure AgreementStartDate is compatible with the ResaleAuthorization. | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | Ensure AgreementEndDate is compatible with the ResaleAuthorization. | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | Ensure the duration between AgreementStartDate and AgreementEndDate is compatible with the ResaleAuthorization. | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | Ensure AgreementDuration matches duration specified in the ResaleAuthorization. | 
| INCOMPATIBLE\_TERMS  | ValidityTerm isn't supported for public offers. | 
| INCOMPATIBLE\_TERMS  | The requested change can't be performed after the offer is expired. | 
| INVALID\_AGREEMENT\_DURATION | Provide AgreementDuration that is greater than or equal to [x] days. | 
| INVALID\_AGREEMENT\_END\_DATE | Provide a future AgreementEndDate. | 
| INVALID\_AGREEMENT\_END\_DATE | Provide AgreementEndDate that is after or equal to [x]. | 
| INVALID\_AGREEMENT\_START\_DATE | Provide an AgreementStartDate that is after AvailabilityEndDate. | 
| INVALID\_AGREEMENT\_START\_DATE | Provide an AgreementStartDate that is before the AgreementEndDate. | 
| INVALID\_AGREEMENT\_START\_DATE | Provide an AgreementStartDate that is within [x] years from today. | 
| INVALID\_AGREEMENT\_TIME\_INTERVAL | ValidityTerm with both AgreementDuration and AgreementEndDate isn't supported. | 
| INVALID\_AGREEMENT\_TIME\_INTERVAL | ValidityTerm with both AgreementStartDate and AgreementDuration isn't supported in an offer for the product. | 
| INVALID\_AGREEMENT\_TIME\_INTERVAL | ValidityTerm with AgreementStartDate isn't supported in an offer for the product. | 
| INVALID\_AGREEMENT\_TIME\_INTERVAL | ValidityTerm with only AgreementStartDate isn't supported. | 
| INVALID\_AGREEMENT\_TIME\_INTERVAL | AgreementEndDate isn't supported unless it's used in combination with a future AgreementStartDate or for replacement offers. | 
| INVALID\_AGREEMENT\_TIME\_INTERVAL | Provide AgreementStartDate and AgreementEndDate where the difference is less than or equal to [x] years. | 
| MISSING\_AGREEMENT\_START\_DATE | Ensure AgreementStartDate is present in ValidityTerm when used along with ConfigurableUpfrontPricingTerm. | 

## Update pricing
<a name="update-pricing-terms-cppo"></a>

You can use the Catalog API to replace the existing pricing terms completely.

The pricing terms that aren't included in the latest request will be removed from the offer. Channel partners can use this change type only to pass `FixedUpFrontPricingTerm`.

To update pricing terms for your offers, call the `StartChangeSet` API operation with the `UpdatePricingTerms` change type, as shown in the following example. 

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "UpdatePricingTerms",
      "Entity": {
        "Type": "Offer@1.0",
        "Identifier": "offer-123456789"
      },
      "Details": {
        "PricingModel": "Contract",
        "Terms": [
          {
            "Type": "FixedUpfrontPricingTerm",
            "CurrencyCode": "USD",
            "Price": "200.00",
            "Duration": "P465D",
            "Grants": [
              {
                "DimensionKey": "Users",
                "MaxQuantity": 10
              }
            ]
          }
        ]
      }
    }
  ]
}
```

Provide information for the fields to add the `UpdatePricingTerms` change type:
+ **Entity** (object) (required) – Your CPPO. 
  + **Type** (string) (required) – The `Type` is always `Offer@1.0`. 
  + **Identifier** (string) (required) – Your offer ID. For more information, see [Identifier](catalog-apis.md#identifier).
+ **Details** (string) (required) – Specifics of the request. This field is a JSON string field. It must be formatted properly for a single-line string field, including escaping characters (such as quotation marks) that can't be in a string.
  + **PricingModel** (string) (required) – Pricing model for your offer. Possible values for pricing model are:
    + **Contract** – Contract-based pricing model where buyers are either billed in advance for the use of your product, or offered a flexible payment schedule. Buyers can also pay for an additional usage above their contract.
    + **Terms** (array of structures) (required) – List of pricing terms that you want to update. Supported pricing terms are:
      + **FixedUpfrontPricingTerm** (object) – Defines a pre-paid pricing model where the customers are charged a fixed upfront amount.
        + **Type** (string) (required) – Type of the term being updated.
        + **CurrencyCode** (string) (required) – Defines the currency for the prices mentioned in this term. For public offers, only USD is supported. For private offers, USD, AUD, EUR, GBP, and JPY are supported.
        + **Price** (string) (required) – Fixed amount to be charged to the customer when this term is accepted.
        + **Grants** (array of structures) (required) – Entitlements that will be granted to the acceptor of fixed upfront as part of agreement execution.
          + **DimensionKey** (string) (required) – Unique dimension key defined in the product document. Dimensions represent categories of capacity in a product and are specified when the product is listed in AWS Marketplace.
          + **MaxQuantity** (integer) (optional) – Maximum amount of capacity that the buyer can be entitled to the given dimension of the product. If `MaxQuantity` is not provided, the buyer will be able to use an unlimited amount of the given dimension.
        + **Duration** (string) (optional) – Defines the duration that the term remains active. This ﬁeld supports the ISO 8601 format.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating information to ensure that it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours. 

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

**Synchronous Validations**

The following schema validations are specific to `UpdatePricingTerms` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | 
| --- | --- | 
| PricingModel | Required<br />Allowed pricing models: <br />Contract | 
| Terms | Required<br />Allowed terms: <br />FixedUpfrontPricingTerm | 
| Terms[].FixedUpfrontPricingTerm.CurrencyCode | Required<br />Allowed values: ["USD", "AUD", "EUR", "GBP", "JPN"]<br />Allowed pricing models:<br />Contract | 
| Terms[].FixedUpfrontPricingTerm.Price | Required<br />Data type is "String" Must be non-negative <br />Support up to 6 Decimals<br />No special character supported | 
| Terms[].FixedUpfrontPricingTerm.Duration | Required<br />Expected format: ISO 8601 duration | 
| Terms[].FixedUpfrontPricingTerm.Grants[].DimensionKey | Required<br />Length must be between 1 and 60 | 
| Terms[].FixedUpfrontPricingTerm.Grants[].MaxQuantity | Required | 

**Asynchronous Errors**

The following errors are specific to `UpdatePricingTerms` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| DUPLICATE\_DIMENSION\_KEYS | Provide Grants with a unique list of dimension keys in [x]. | 
| DUPLICATE\_DIMENSION\_KEYS | Provide RateCard with a unique list of dimension keys in [x]. | 
| DUPLICATE\_SELECTORS  | Provide a unique list of Selectors in ConfigurableUpfrontPricingTerm. | 
| DUPLICATE\_TERM\_TYPES | Provide a unique list of term types. | 
| INCOMPATIBLE\_AGREEMENT | The following terms can't be removed from the replacement offer: [x, y, z]. | 
| INCOMPATIBLE\_AGREEMENT | The following terms can't be added to the replacement offer: [x, y, z]. | 
| INCOMPATIBLE\_CURRENCY\_CODE | CurrencyCode can't be changed after the offer is released. | 
| INCOMPATIBLE\_PAYMENT\_SETTINGS | Update your payment settings to be compatible with the CurrencyCode. | 
| INCOMPATIBLE\_PRODUCT | Usage pricing model isn't supported for the product. | 
| INCOMPATIBLE\_PRODUCT | Contract pricing model isn't supported for the product. | 
| INCOMPATIBLE\_PRODUCT | Byol pricing model isn't supported for the product. | 
| INCOMPATIBLE\_PRODUCT | Free pricing model isn't supported for the product. | 
| INCOMPATIBLE\_PRODUCT | [x] isn't supported in an offer for the product. | 
| INCOMPATIBLE\_PRODUCT | Provided payment and pricing terms are incompatible. | 
| INCOMPATIBLE\_PRODUCT | Use existing, available dimensions in the product in [x]. | 
| INCOMPATIBLE\_PRODUCT | FreeTrialPricingTerm as the offer's only pricing term isn't supported for the product. | 
| INCOMPATIBLE\_PRODUCT | The following terms aren't supported for the product: [x,y,z]. | 
| INCOMPATIBLE\_PRODUCT | Replacement offers are only supported for contract pricing model. | 
| INCOMPATIBLE\_PRODUCT | Provide pricing term(s) that are compatible with the product dimensions. Incompatible pricing terms: [x,y,z]. | 
| INCOMPATIBLE\_RATE\_CARD\_CONSTRAINTS | Set MultipleDimensionSelection and QuantityConfiguration to Allowed in ConfigurableUpfrontPricingTerm for usage pricing model. | 
| INCOMPATIBLE\_RATE\_CARD\_CONSTRAINTS | Set MultipleDimensionSelection and QuantityConfiguration to Disallowed in ConfigurableUpfrontPricingTerm for usage pricing model. | 
| INCOMPATIBLE\_RATE\_CARD\_CONSTRAINTS | QuantityConfiguration in ConfigurableUpfrontPricingTerm can't be changed after the offer is released. | 
| INCOMPATIBLE\_RATE\_CARD\_CONSTRAINTS | MultipleDimensionSelection in ConfigurableUpfrontPricingTerm can't be changed after the offer is released. | 
| INCOMPATIBLE\_RATES | Set all charge amounts and prices to zero (0) when using Free pricing model. | 
| INCOMPATIBLE\_RATES | Only zero (0) prices are allowed in UsageBasedPricingTerm for a free trial offer for the product. | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | Provide the same CurrencyCode that is specified in the ResaleAuthorization. | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | Ensure Duration in FixedUpfrontPricingTerm matches duration specified in the ResaleAuthorization. | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | Provide term(s) that are compatible with the ResaleAuthorization. Incompatible terms: [x, y, z]. | 
| INCOMPATIBLE\_SELECTOR\_DURATION | Durations aren't allowed to be removed from rate cards in ConfigurableUpfrontPricingTerm after the offer released. | 
| INCOMPATIBLE\_SELLER\_VERIFICATION | Complete all required seller verification processes. | 
| INCOMPATIBLE\_TERMS  | [x] isn't supported together with the following terms: [y,z]. | 
| INCOMPATIBLE\_TERMS  | The following terms can't be added after the offer is released: [x,y,z]. | 
| INCOMPATIBLE\_TERMS  | The following terms can't be removed after the offer is released: [x,y,z]. | 
| INCOMPATIBLE\_TERMS  | [x] isn't supported for private offers. | 
| INCOMPATIBLE\_TERMS  | The following terms aren't supported with FreeTrialPricingTerm that grants unlimited usage: [x,y,z]. | 
| INCOMPATIBLE\_TERMS  | The following terms aren't supported with FreeTrialPricingTerm for the product: [x,y,z]. | 
| INCOMPATIBLE\_TERMS  | Provide zero (0) price for FixedUpfrontPricingTerm when the offer contains a PaymentScheduleTerm. | 
| INCOMPATIBLE\_TERMS  | The following terms aren't compatible with the PricingModel: [x,y,z]. | 
| INCOMPATIBLE\_TERMS  | FixedUpfrontPricingTerm isn't supported when MarkupPercentage is greater than zero (0). | 
| INCOMPATIBLE\_TERMS  | The requested change can't be performed after the offer is released. | 
| INCOMPATIBLE\_TERMS  | The requested change can't be performed after the offer is expired. | 
| INVALID\_AGREEMENT\_DURATION | Provide duration between [x] and [y] months. | 
| INVALID\_AGREEMENT\_DURATION | Ensure duration granularity is at the day level for metered dimensions. | 
| INVALID\_CURRENCY\_CODE | Provide a supported CurrencyCode. | 
| INVALID\_CURRENCY\_CODE | Provide the same CurrencyCode across all pricing and payment terms. | 
| INVALID\_DURATION | Ensure Duration in FreeTrialPricingTerm is within the allowed range. | 
| INVALID\_DURATION | Provide Duration in FixedUpfrontPricingTerm that matches the duration between AgreementStartDate and AgreementEndDate. | 
| INVALID\_DURATION | Provide duration between [x] and [y] months. | 
| INVALID\_DURATION | Ensure duration granularity is at the day level for metered dimensions. | 
| INVALID\_GRANTS | Provide the same MaxQuantity for all Grants in FreeTrialPricingTerm. | 
| INVALID\_GRANTS | Provide Grants for all available metered dimensions in FreeTrialPricingTerm. | 
| INVALID\_PRICE\_CHANGE | [x] can't be updated until [y] because you have requested a price increase in the past 120 days. To cancel your previous price increase request or for more information, contact the AWS Marketplace Managed Catalog Operations Team. | 
| INVALID\_PRICE\_CHANGE | Price increase and dimension addition in [x] isn't supported in the same request. Add dimensions first. | 
| INVALID\_PRICE\_CHANGE | Price increase and decrease in UsageBasedPricingTerm isn't supported in the same request. Decrease prices first. | 
| INVALID\_PRICE\_CHANGE | Price increase in RecurringPaymentTerm and price decrease in UsageBasedPricingTerm isn't supported in the same request. Decrease prices first. | 
| INVALID\_PRICE\_CHANGE | Price decrease in RecurringPaymentTerm and price increase in UsageBasedPricingTerm isn't supported in the same request. Decrease prices first. | 
| INVALID\_RATE\_CARD | ConfigurableUpfrontPricingTerm is missing one or more-dimension keys for duration [x]. Provide prices for the same set of dimension keys for all durations. | 
| INVALID\_RATE\_CARD | Provide a rate card for only metered dimensions in UsageBasedPricingTerm. | 
| INVALID\_RATE\_CARD | Rates can't be removed from [x]. Provide prices for all dimensions in the existing rate card. | 
| INVALID\_RATE\_CARD | Provide dimensions that have the same unit in [x]. | 
| INVALID\_RATE\_CARD | Provide either all metered or all entitled dimensions in [x]. | 
| INVALID\_RATE\_CARD | Provide only entitled dimensions in [x]. | 
| INVALID\_RATE\_CARD | Provide usage based rates for all available metered dimensions in UsageBasedPricingTerm. | 
| INVALID\_RATE\_CARD | Provide usage based rates for all free trial dimensions. | 
| INVALID\_RATE\_CARD | Provide prices with up to 8 decimal places in UsageBasedPricingTerm. | 
| INVALID\_SELECTOR\_DURATION\_VALUE | Provide duration between [x] and [y] months. | 
| INVALID\_SELECTOR\_DURATION\_VALUE | Ensure duration granularity is at the day level for metered dimensions. | 
| INVALID\_SELECTOR\_DURATION\_VALUE | Ensure Duration in ConfigurableUpfrontPricingTerm is within the allowed range. | 
| INVALID\_SELECTOR\_DURATION\_VALUE | Provide one or more supported contract durations. | 
| INVALID\_SELECTOR\_DURATION\_VALUE | Provide one or more supported contract durations or a single custom duration. | 
| INVALID\_SELECTOR\_DURATION\_VALUE | Provide Duration in ConfigurableUpfrontPricingTerm that matches the duration between AgreementStartDate and AgreementEndDate. | 
| MISSING\_DURATION | Provide Duration in FixedUpfrontPricingTerm. | 
| MISSING\_MANDATORY\_TERMS | FixedUpfrontPricingTerm is only supported when paired with ByolPricingTerm or PaymentScheduleTerm. | 
| MISSING\_MANDATORY\_TERMS | Provide at least one of [x,y,z]. | 
| MISSING\_MANDATORY\_TERMS | Provide a ByolPricingTerm when using Byol pricing model. | 
| TOO\_MANY\_GRANTS | Provide up to [x] grants in [y]. | 
| TOO\_MANY\_RATE\_CARDS | Only one rate card in ConfigurableUpfrontPricingTerm is allowed for the product. | 
| TOO\_MANY\_RATE\_CARDS | Up to [x] rate cards are allowed in ConfigurableUpfrontPricingTerm for the product. | 
| TOO\_MANY\_RATES | Provide RateCards within the allowed limits in ConfigurableUpfrontPricingTerm. | 
| TOO\_MANY\_RATES | Provide RateCards within the allowed limits in UsageBasedPricingTerm. | 

## Update payment schedule details
<a name="update-payment-schedule-terms-cppo"></a>

You can use the Catalog API to change the payment schedule details, such as flexible payment schedule, in AWS Marketplace.

If the manufacturer has provided a payment schedule in Resale Authorization, Channel Partner can either:
+ Use the `UpdateMarkup` change type to apply a uniform percentage markup to all payment schedules.
+ Use the `UpdatePaymentScheduleTerms` change type to set custom payment amounts to a value greater than or equal to what is provided in Resale Authorization. Payment dates can't be changed. Both options can't be applied simultaneously. If a markup is applied first and you need to change it to apply a payment schedule, set the markup to `0` through the `UpdateMarkup` change type. If a payment schedule is applied first you can't revert the change to apply the markup.

To update payment-associated details for your offer, call the `StartChangeSet` API operation with the `UpdatePaymentScheduleTerms` change type, as shown in the following example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "UpdatePaymentScheduleTerms",
      "Entity": {
        "Type": "Offer@1.0",
        "Identifier": "offer-123456789"
      },
      "DetailsDocument": {
        "Terms": [
          {
            "Type": "PaymentScheduleTerm",
            "Schedule": [
              {
                "ChargeDate": "2021-12-01",
                "ChargeAmount": "200.00"
              },
              {
                "ChargeDate": "2022-03-01",
                "ChargeAmount": "250.00"
              }
            ]
          }
        ]
      }
    }
  ]
}
```

Provide information for the fields to add the `UpdatePaymentScheduleTerms` change type:
+ **Entity** (object) (required) – Your CPPO. 
  + **Type** (string) (required) – The `Type` is always `Offer@1.0`. 
  + **Identifier** (string) (required) – Your offer ID. For more information, see [Identifier](catalog-apis.md#identifier).
+ **DetailsDocument** (object) (required) – The JSON value of specifics of the request.
  + **Terms** (array of structures) – List of payment terms that you want to update. Supported payment terms are:
    + **PaymentScheduleTerm** (object) – Defines an installment-based pricing model where customers are charged a fixed price on different dates during the agreement validity period.
      + **Type** (string) – Type of the term being updated. This is the object value: `"PaymentScheduleTerm"`.
      + **Schedule** (array of structures) – List of the payment schedule where each element defines one installment of payment. It contains the information necessary for calculating the price to be paid and the date on which the customer would be charged.
        + **ChargeDate** (string) – The date on which the customer would pay the price defined in this payment schedule term. `ChargeDate` is represented in YYYY-MM-DD format. Invoices are generated on the date provided.
        + **ChargeAmount ** (string) – The price that the customer would pay on scheduled date (`ChargeDate`).

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating information to ensure that it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours. 

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

**Synchronous Validations**

The following schema validations are specific to `UpdatePaymentScheduleTerms` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | HTTP | 
| --- | --- | --- | 
| Terms | Required<br />Only "PaymentScheduleTerm" is allowed<br />List size must be less than 2 | 422 | 
| Terms[].PaymentScheduleTerm.CurrencyCode | Required<br />Supported currencies: ["USD", "AUD", "EUR", "GBP", "JPN"] | 422 | 
| Terms[].PaymentScheduleTerm.Schedule[] | Required<br />List size must be between 1 and 60, inclusive | 422 | 
| Terms[].PaymentScheduleTerm.Schedule[].ChargeDate | Required<br />Format: "YYYY-MM-DD" | 422 | 
| Terms[].PaymentScheduleTerm.Schedule[].ChargeAmount | RequiredData type is "String"<br />Non-negative decimals with up to 2 decimal places supported<br />No additional properties are allowed | 422 | 

**Asynchronous Errors**

The following errors are specific to `UpdatePaymentScheduleTerms` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| DUPLICATE\_CHARGE\_DATES | Provide unique charge dates in PaymentScheduleTerm. | 
| INCOMPATIBLE\_MARKUP\_PERCENTAGE | PaymentScheduleTerm isn't supported when MarkupPercentage is greater than zero (0). | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | Provide term(s) that are compatible with the ResaleAuthorization. Incompatible terms: [PaymentScheduleTerm]. | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | Ensure the total ChargeAmounts in PaymentScheduleTerm is compatible with the ResaleAuthorization. | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | Ensure the charge dates in PaymentScheduleTerm are same as the charge dates in the ResaleAuthorization. | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | Ensure the charge amount in PaymentScheduleTerm is greater than or equal to the charge amount in the ResaleAuthorization for that date. | 
| INCOMPATIBLE\_TERMS | The requested change can't be performed after the offer is released. | 
| INCOMPATIBLE\_TERMS | The requested change can't be performed after the offer is expired. | 
| INCOMPATIBLE\_TERMS | Use either UpdatePaymentScheduleTerms with specific payment amount or UpdateMarkup with a single markup percentage for the scheduled dates. | 
| INVALID\_CHARGE\_DATES | Provide charge dates before AgreementEndDate. | 
| TOO\_MANY\_BACKDATED\_CHARGES | Provide up to 1 scheduled payment before AvailabilityEndDate. | 


| Error code | Error message | 
| --- | --- | 
| DUPLICATE\_CHARGE\_DATES | Provide unique charge dates in PaymentScheduleTerm. | 
| INCOMPATIBLE\_CURRENCY\_CODE | CurrencyCode can't be changed after the offer is released. | 
| INCOMPATIBLE\_MARKUP\_PERCENTAGE | PaymentScheduleTerm isn't supported when MarkupPercentage is greater than zero (0). | 
| INCOMPATIBLE\_PAYMENT\_SETTINGS | Update your payment settings to be compatible with the CurrencyCode. | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | Provide term(s) that are compatible with the ResaleAuthorization. Incompatible terms: [PaymentScheduleTerm]. | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | Ensure the total ChargeAmounts in PaymentScheduleTerm is compatible with the ResaleAuthorization. | 
| INCOMPATIBLE\_SELLER\_VERIFICATION | Complete all required seller verification processes. | 
| INCOMPATIBLE\_TERMS | The requested change can't be performed after the offer is released. | 
| INCOMPATIBLE\_TERMS | The requested change can't be performed after the offer is expired. | 
| INVALID\_CHARGE\_DATES | Provide charge dates before AgreementEndDate. | 
| INVALID\_CURRENCY\_CODE | Provide a supported CurrencyCode. | 
| INVALID\_CURRENCY\_CODE | Provide the same CurrencyCode across all pricing and payment terms. | 
| TOO\_MANY\_BACKDATED\_CHARGES | Provide up to 1 scheduled payment before AvailabilityEndDate. | 

## Update net payment terms
<a name="update-cppo-net-payment-terms"></a>

If the Resale Authorization that you use to create a channel partner private offer (CPPO) contains a net payment term, that term is the maximum period that you can offer to your buyer. The term from the Resale Authorization is applied to your CPPO automatically when you create it.

To offer your buyer a shorter payment period than the one that the seller authorized, call the `StartChangeSet` API operation with the `UpdateNetPaymentTerms` change type on your offer, as shown in the following example. If you want to use the same period that the seller authorized, you don't need to call `UpdateNetPaymentTerms`.

**Note**  
The term type on an offer is `NetPaymentTerm`, and the term type on a Resale Authorization is `ResaleNetPaymentTerm`. For more information about setting net payment terms on a Resale Authorization, see [Update net payment terms](work-with-resale-authorizations.md#update-resale-net-payment-terms).

If the Resale Authorization doesn't contain a net payment term, you can't add one to the CPPO, and your buyer's payment terms with AWS apply. You also can't remove the net payment term from a CPPO when the Resale Authorization contains one.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "UpdateNetPaymentTerms",
      "Entity": {
        "Type": "Offer@1.0",
        "Identifier": "offer-123456789"
      },
      "DetailsDocument": {
        "Terms": [
          {
            "Type": "NetPaymentTerm",
            "PaymentDuePeriod": "P30D"
          }
        ]
      }
    }
  ]
}
```

Provide information for the fields to add the `UpdateNetPaymentTerms` change type:
+ **Entity** (object) (required) – Your offer.
  + **Type** (string) (required) – The `Type` is always `Offer@1.0`.
  + **Identifier** (string) (required) – Your offer ID. For more information, see [Identifier](catalog-apis.md#identifier).
+ **DetailsDocument** (object) (required) – The JSON value of specifics of the request.
  + **Terms** (array of structures) (required) – List of net payment terms that you want to update. An offer can contain at most one net payment term. Supported terms are:
    + **NetPaymentTerm** (object) (required) – Defines the net payment terms that are negotiated with the buyer.
      + **Type** (string) (required) – Type of the term being updated. This is the object value: `"NetPaymentTerm"`.
      + **PaymentDuePeriod** (string) (required) – The number of days after the invoice issuance date that payment is due. This field supports the ISO 8601 format. Supported values are `P15D`, `P30D`, `P45D`, `P60D`, `P90D`, and `P120D`. This value can't exceed the `PaymentDuePeriod` in the `ResaleNetPaymentTerm` of the Resale Authorization.

**Synchronous Validations**

The following schema validations are specific to `UpdateNetPaymentTerms` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | HTTP code | 
| --- | --- | --- | 
| Terms | Required<br />Only `NetPaymentTerm` is allowed<br />List size must be less than 2 | 422 | 
| Terms[].Type | Required<br />Can only be `NetPaymentTerm` | 422 | 
| Terms[].NetPaymentTerm.PaymentDuePeriod | Required<br />Expected format: ISO 8601 duration<br />Allowed values: ["P15D", "P30D", "P45D", "P60D", "P90D", "P120D"] | 422 | 

**Asynchronous Errors**

The following errors are specific to `UpdateNetPaymentTerms` actions on a CPPO in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INVALID\_PAYMENT\_DUE\_PERIOD | Provide a supported PaymentDuePeriod. | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | NetPaymentTerm isn't supported because the ResaleAuthorization doesn't contain a NetPaymentTerm. | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | Ensure PaymentDuePeriod in NetPaymentTerm is compatible with the ResaleAuthorization. | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | NetPaymentTerm can't be removed because the ResaleAuthorization contains a NetPaymentTerm. | 

## Publish the CPPO
<a name="release-offer-cppo"></a>

You can use the Catalog API to merge the information collected from all update change types, and then publish the offer in AWS Marketplace.

Offers remain in a `Draft` state, until `ReleaseOffer` is called. After the offer is released, it's discoverable in AWS Marketplace.

To publish your offer, call the `StartChangeSet` API operation with the `ReleaseOffer` change type as shown in the following example. 

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "ReleaseOffer",
      "Entity": {
        "Type": "Offer@1.0",
        "Identifier": "offer-123456789"
      },
      "DetailsDocument": {}
    }
  ]
}
```

Provide information for the fields to add the `ReleaseOffer` change type:
+ **Entity** (object) (required) – Your CPPO. 
  + **Type** (string) (required) – The `Type` is always `Offer@1.0`. 
  + **Identifier** (string) (required) – Your offer ID. For more information, see [Identifier](catalog-apis.md#identifier).
+ **DetailsDocument** (object) (required) – The JSON value of specifics of the request. It must be empty for `ReleaseOffer`.

**Response Syntax**

A change set is created for your request. The response to this request gives you the `ChangeSetId` and `ChangeSetArn` for the change set and looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating information to ensure that it meets the AWS Marketplace guidelines. The validation process can take anywhere from a few minutes to a few hours. 

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

**Synchronous Validations**

The following schema validations are specific to `ReleaseOffer` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | 
| --- | --- | 
| Details  | Must be empty ({}) | 

**Asynchronous Errors**

The following errors are specific to `ReleaseOffer` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INCOMPATIBLE\_PAYMENT\_SETTINGS | Update your payment settings to be compatible with the CurrencyCode. | 
| INCOMPATIBLE\_PRODUCT | First create a public offer for the product. | 
| INCOMPATIBLE\_SELLER\_VERIFICATION | Complete all required seller verification processes. | 
| INVALID\_UPDATE\_REQUEST | The requested change can't be performed after the offer is released. | 
| MISSING\_AGREEMENT\_END\_DATE | Provide an AgreementEndDate for replacement offers. | 
| MISSING\_AVAILABILITY\_END\_DATE | Provide an AvailabilityEndDate for private offer. | 
| MISSING\_MANDATORY\_TERMS | Provide a FixedUpfrontPricingTerm when the offer contains a PaymentScheduleTerm. | 
| MISSING\_BUYER\_ACCOUNTS | Provide PositiveTargeting with BuyersAccounts for offers created using ResaleAuthorization. | 
| MISSING\_BUYER\_ACCOUNTS | All offers for the product must be private. Provide PositiveTargeting with BuyersAccounts. | 
| MISSING\_DESCRIPTION | Set Description before releasing the offer. | 
| MISSING\_MANDATORY\_TERMS | Add [x] to the offer. | 
| MISSING\_MANDATORY\_TERMS | Provide a FixedUpfrontPricingTerm when the offer contains a PaymentScheduleTerm. | 
| MISSING\_NAME | Set Name before releasing the offer. | 
| TOO\_MANY\_OFFERS | Only one public offer can be created per product. | 
| TOO\_MANY\_OFFERS | Only one public free trial offer can be created per product. | 

## Define an existing CPPO
<a name="describe-entity-cppo"></a>

You can use the Catalog API to define CPPO details in AWS Marketplace.

To define an existing CPPO, call the `DescribeEntity` API operation with the `Offer@1.0` entity type, as shown in the following example.

**Request Syntax**

```
GET /DescribeEntity?catalog=<Catalog>&entityId=<EntityId> HTTP/1.1
```

Provide information for the fields to add the `DescribeEntity` change type:
+ **catalog** (string) –The catalog related to the request. Fixed value: `AWSMarketplace`.
+ **entityId** (string) – The unique ID of the offer to describe.

**Response Syntax**

The response to this request gives you the offer details and looks like the following.

```
{
  "EntityType": "Offer@1.0",
  "EntityIdentifier": "offer-a5oEXAMPLEzpu@1",
  "EntityArn": "arn:aws:aws-marketplace:us-east-1:446235747164:AWSMarketplace/Offer/offer-a5oEXAMPLEzpu",
  "LastModifiedDate": "2021-03-10T21:57:16Z",
  "Details": {
    "Id": "offer-3rEXAMPLErn",
    "State": "Released",
    "Name": "Test Offer",
    "Description": "Worldwide private offer for Test Product",
    "PreExistingAgreement": {
      "AcquisitionChannel": "External",
      "PricingModel": "Contract"
    },
    "ProductId": "prod-0bEXAMPLEb51",
    "ResaleAuthorizationId": "resaleauthz-123456789",
    "MarkupPercentage": "5.0",
    "Terms": [
      {
        "Type": "LegalTerm",
        "Documents": [
          {
            "Type": "CustomEula",
            "Url": "https://s3.amazonaws.com/EULA/custom-eula-1234.txt"
          }
        ]
      },
      {
        "Type": "ConfigurableUpfrontPricingTerm",
        "CurrencyCode": "USD",
        "RateCards": [
          {
            "Selector": {
              "Type": "Duration",
              "Value": "P12M"
            },
            "RateCard": [
              {
                "DimensionKey": "m3.large",
                "Price": "300.00"
              },
              {
                "DimensionKey": "m4.xlarge",
                "Price": "400.00"
              }
            ],
            "Constraints": {
              "MultipleDimensionSelection": "Allowed",
              "QuantityConfiguration": "Allowed"
            }
          }
        ]
      },
      {
        "Type": "UsageBasedPricingTerm",
        "CurrencyCode": "USD",
        "RateCards": [
          {
            "RateCard": [
              {
                "DimensionKey": "m3.large",
                "Price": "0.10"
              },
              {
                "DimensionKey": "m4.xlarge",
                "Price": "0.20"
              }
            ]
          }
        ]
      },
      {
        "Type": "PaymentScheduleTerm",
        "CurrencyCode": "USD",
        "Schedule": [
          {
            "ChargeDate": "2020-12-01T00:00:00Z",
            "ChargeAmount": "1000.00"
          },
          {
            "ChargeDate": "2021-06-15T00:00:00Z",
            "ChargeAmount": "1250.00"
          }
        ]
      }
    ],
    "Rules": [
      {
        "Type": "TargetingRule",
        "PositiveTargeting": {
          "CountryCodes": [
            "US",
            "CA"
          ],
          "BuyerAccounts": [
            "118033953248"
          ]
        },
        "NegativeTargeting": {
          "CountryCodes": [
            "XX"
          ]
        }
      },
      {
        "Type": "AvailabilityRule",
        "AvailabilityEndDate": "2050-08-30T01:56:03Z"
      }
    ]
  }
}
```

Provide information for the input fields for the `DescribeEntity` response:
+ **EntityType** (string) – The named type of the entity, which is `Offer@1.0`.
+ **EntityIdentifier** (string) – The identifier of the entity, in the format of `EntityId@RevisionId`.
+ **EntityArn** (string) – The ARN associated to the unique identifier for the change set referenced in this request.
+ **LastModifiedDate** (string) – The last modified date of the entity, in ISO 8601 format (`2018-02-27T13:45:22Z`).
+ **DetailsDocument** (object) – The JSON object includes the details of the entity.
  + **Id** (string) – Unique identifier for an offer entity in AWS Marketplace and is generated during the creation of an offer.
  + **State** (string) – The status of the offer.
  + **Name** (string) – Name associated with the offer for better readability to you and your customers. It will be displayed as part of Agreement information as well.
  + **Description** (string) – Description is a free-form text which is meant to be used only by you and will never be exposed to buyers.
  + **PreExistingAgreement** (string) – Determines if this offer is a renewal for an existing agreement with an existing customer for the same underlying product. The existing agreement can be within or outside AWS Marketplace. AWS may audit and verify your offer is a renewal. If AWS is unable to verify your offer, then AWS may revoke the offer and entitlements from your customer.
    + **AcquisitionChannel** (string) – Indicates if the existing agreement was signed outside AWS Marketplace or within AWS Marketplace. Possible values: `External`, `AwsMarketplace`.

       
    + **PricingModel** (string) – Indicates which pricing model the existing agreement uses. Possible values: `Contract`, `Usage`, `Byol`, `Free`.
  + **ProductId** (string) – Description is a free-form text which is meant to be used only by you and will never be exposed to buyers.
  + **ResaleAuthorizationId** (string) – ResaleAuthorization is used to create the private offer.
  + **MarkupPercentage** (string) – Percentage value that the channel partner passed in the `UpdateMarkup` change type. This markup is already applied to the terms.
  + **Terms** (array of structures) – List of terms.
  + **Rules** (array of structures) – List of rules.