

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Work with private offers using the AWS Marketplace APIs
<a name="work-with-private-offers"></a>

You can use the AWS Marketplace Catalog API to automate tasks for working with offers. 

While the *product* describes what is being sold in AWS Marketplace, the *offer* describes the terms and rules of how a product is purchased and consumed. AWS Marketplace products can have multiple offers sold by different sellers. Each AWS Marketplace offer, however, can only be created for one product. An *offer* contains a collection of agreement terms between two parties. The accepted offer terms are translated into an agreement as proof of a transaction.

There are two types of offers:
+ **Private offers** are for sellers and buyers to negotiate pricing. Sellers sign an end-user license agreement (EULA) for software purchases in AWS Marketplace. An offer is visible only to a specified buyer. For more information, see [Private offers](https://docs.aws.amazon.com/marketplace/latest/userguide/private-offers-overview.html) in the *AWS Marketplace Seller Guide*.
+ **Public offers** are for global purchasing programs. Sellers identify customers based on available programs and geographical locations, which makes the offer accessible only to specific customers.

See the following resources:
+ For working code examples, see [Manage offers with API](https://catalog.workshops.aws/mpseller/en-US/manage-offers-with-api) in the *AWS Marketplace seller workshop*. 
+ For API request code examples, see [Python](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/python/src/catalog_api/offers) and [Java](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java/resources/changeSets/offers) examples in *AWS Samples* on GitHub.
+ For a video on creating private offers, see [Create a Private Offer Using the AWS Marketplace Catalog API](https://www.youtube.com/watch?v=Gg9JR0tB330) on YouTube.
+ For a video on updating AMI pricing, see [Update AMI Product Pricing Using the AWS Marketplace Catalog API](https://www.youtube.com/watch?v=AVIRlzHKEJw) on YouTube.

The following topics describe how to use the Catalog API to create and update offers:

**Topics**
+ [Create an offer](#create-offer)
+ [Create a replacement offer](#create-replacement-offer)
+ [Update offer information](#update-offer-information)
+ [Update targeting configuration](#update-targeting-offers)
+ [Update refund policy](#update-support-terms)
+ [Update legal resources](#update-legal-terms)
+ [Update pricing](#update-pricing-terms)
+ [Update the discoverability of the offer](#update-availability)
+ [Define the expiration date of agreements created using the offer](#update-validity-terms)
+ [Update payment schedule details](#update-payment-schedule-terms)
+ [Update net payment terms](#update-net-payment-terms)
+ [Modify renewal options](#update-renewal-terms)
+ [Publish an offer](#release-offer)
+ [Describe existing offer details](#describe-entity)

## Create an offer
<a name="create-offer"></a>

You can use the Catalog API to create a new offer in AWS Marketplace. If your request processes successfully, the AWS Marketplace Catalog API creates a `Draft`, which is an incomplete offer that's invisible to buyers. To complete an offer, use the `Update` change type. When the offer is complete, use the [`ReleaseOffer`](#release-offer) change type to create and release it. Releasing an offer validates it and makes it visible to buyers in AWS Marketplace.

To create a new offer, call the `StartChangeSet` API operation with the `CreateOffer` change type, as shown in the following example. 

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "CreateOffer",
      "Entity": {
        "Type": "Offer@1.0"
      },
      "DetailsDocument": {
        "ProductId": "prod-ad8EXAMPLE51",
        "Name": "Test Offer",
        "OfferSetId": "offerset-b3f9EXAMPLE27"
      }
    }
  ]
}
```

Provide information for the fields to add the `CreateOffer` change type:
+ **Entity** (object) (required) – Your offer.
  + **Type** (string) (required) – The `Type` is always `Offer@1.0`. 
+ **DetailsDocument** (object) (required) – The JSON value of specifics of the request.
  + **ProductId** (string) (required) – The unique identifier of the product being offered.
  + **Name** (string) (optional) – The name associated with the offer for better readability to you and your customers. It is displayed as a part of the Agreement information as well.
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

If the `Status` is `SUCCEEDED`, then a new `OfferId` is generated.

The response looks like the following.

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
      "ChangeType": "CreateOffer",
      "Entity": {
        "Type": "Offer@1.0",
        "Identifier": "offer-123456789"
      },
      "DetailsDocument": {
        "ProductId": "prod-ad8EXAMPLE51",
        "Name": "Test Offer"
      },
      "ErrorDetailList": []
    }
  ]
}
```

**Synchronous Validations**

The following schema validations are specific to `CreateOffer` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | HTTP code | 
| --- | --- | --- | 
| ProductId | Required<br />Length must be between 1 and 50 characters <br />Must not contain illegal characters (\\, <, >) | 422 | 
| ProductId | RequiredUser must be authorized to create offer for the given product | 403 | 
| ProductId | RequiredMust be an existing product in the catalog or being created in the same change set | 404 | 
| Name | Optional<br />Length must be between 1 and 150 characters <br />Must not contain illegal characters (\\, <, >) | 422 | 

**Asynchronous Errors**

The following errors are specific to `CreateOffer` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INCOMPATIBLE\_PRODUCT | Use an active product in Limited or Public state. | 
| INCOMPATIBLE\_PRODUCT | Managing offers for your chosen product type isn't currently supported in the AWS Marketplace Catalog API. | 
| INCOMPATIBLE\_PRODUCT | Managing offers for the product isn't currently supported in the AWS Marketplace Catalog API. | 
| INCOMPATIBLE\_PRODUCT | OfferSetId isn't supported in offers for the product. | 
| INCOMPATIBLE\_PRODUCT | CreateOffer change type can't be invoked to create an offer for the product. Use CreateOfferUsingResaleAuthorization change type. | 

## Create a replacement offer
<a name="create-replacement-offer"></a>

You can use the Catalog API to create a replacement offer (also known as an agreement-based offer) in AWS Marketplace. 

If your request has been processed successfully, AWS Marketplace Catalog API will have an offer in `Draft` state generated for you, which is an incomplete offer and not visible to buyers on AWS Marketplace. You will use `Update` change types to complete the offer. After the offer is completed, you will use [`ReleaseOffer`](#release-offer) change type to complete offer creation process and release the offer, which will validate the entire offer and make your offer visible to buyers on AWS Marketplace. From there, the buyer has the option to accept the replacement offer or to continue to operate under the original agreement.

To create a replacement offer, call the `StartChangeSet` API operation with the `CreateReplacementOffer` change type and provide a pre-existing agreement id, as shown in the following example. 

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "CreateReplacementOffer",
      "Entity": {
        "Type": "Offer@1.0"
      },
      "DetailsDocument": {
        "AgreementId": "agmt-12345",
        "Name": "Offer name"
      }
    }
  ]
}
```

Provide information for the fields to add the `CreateReplacementOffer` change type:
+ **Entity** (object) (required) – Your offer. 
  + **Type** (string) (required) – The `Type` is always `Offer@1.0`. 
+ **DetailsDocument** (object) (required) – The JSON value of specifics of the request.
  + **AgreementId** (string) (required) – The unique identifier for the current agreement to be replaced.
  + **Name** (string) (optional) – The name associated with the offer for better readability to you and your customers. It will be displayed as part of Agreement information as well.

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

The following schema validations are specific to `CreateReplacementOffer` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | HTTP Code | 
| --- | --- | --- | 
| AgreementId | RequiredLength must be between 1 and 64 characters | 422 | 
| AgreementId | RequiredUser must be authorized to create offer for the given agreement | 403 | 
| Name | OptionalLength must be between 1 and 150 characters<br />Must not contain invalid characters (\\, <, >) | 422 | 

**Asynchronous Errors**

The following errors are specific to `CreateReplacementOffer` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code  | Error message | 
| --- | --- | 
| INCOMPATIBLE\_PRODUCT | Replacement offers aren't supported for the product. | 
| INCOMPATIBLE\_AGREEMENT | CreateReplacementOffer change type can't be invoked to create a replacement offer for the agreement. Use CreateReplacementOfferUsingResaleAuthorization change type. | 

## Update offer information
<a name="update-offer-information"></a>

You can use the Catalog API to update the offer information in AWS Marketplace. 

To update the offer information, call the `StartChangeSet` API operation with the `UpdateInformation` change type, as shown in the following example. All other information will remain unchanged.

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
        "Type": "Offer@1.0",
        "Identifier": "offer-123456789"
      },
      "DetailsDocument": {
        "Name": "New offer name",
        "Description": "New offer description",
        "PreExistingAgreement": {
          "AcquisitionChannel": "External",
          "PricingModel": "Contract"
        }
      }
    }
  ]
}
```

Provide information for the fields to add the `UpdateInformation` change type:
+ **Entity** (object) (required) – Your offer. 
  + **Type** (string) (required) – The `Type` is always `Offer@1.0`. 
  + **Identifier** (string) (required) – Your offer ID. For more information, see [Identifier](catalog-apis.md#identifier).
+ **DetailsDocument** (object) (required) – The JSON value of specifics of the request.
  + **Name** (string) (optional) – Name associated with the offer for better readability. It is displayed as part of agreement information.
  + **Description** (string) (optional) – A free-form text that is meant to be used only by you and will never be visible to buyers.
  + **PreExistingAgreement** (object) (optional) – Determines if this offer is a renewal for an existing agreement with an existing customer for the same underlying product. The existing agreement can be within or outside AWS Marketplace. AWS may audit and verify your offer is a renewal. If AWS is unable to verify your offer, then AWS may revoke the offer and entitlements from your customer.
    + **AcquisitionChannel** (string) (required) – Indicates if the existing agreement was signed outside AWS Marketplace or within AWS Marketplace.

      Possible values: `External`, `AwsMarketplace`
    + **PricingModel** (string) (required) – Indicates which pricing model the existing agreement uses.

      Possible values: `Contract`, `Usage`, `Byol`, `Free`

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

**Synchronous Validations**

The following schema validations are specific to `UpdateInformation` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | HTTP code | 
| --- | --- | --- | 
| Properties | At least one of the following properties must be provided | 422 | 
| Name | Optional<br />Length must be between 1 and 150 characters <br />Must not contain illegal characters (\\, <, >) | 422 | 
| Description | Optional<br />Length must be between 1 and 255 characters | 422 | 
| PreExistingAgreement | OptionalCan be null to remove `PreExistingAgreement` from offer | 422 | 
| PreExistingAgreement.PricingModel | Required<br />Can be one of these values: [`Byol`, `Free`, `Usage`, `Contract`] | 422 | 
| PreExistingAgreement.AcquisitionChannel | Required<br />Can be one of these values: [`AwsMarketplace`, `External`] | 422 | 

**Asynchronous Errors**

The following errors are specific to `UpdateInformation` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code  | Error message | 
| --- | --- | 
| INCOMPATIBLE\_PRE\_EXISTING\_AGREEMENT | PreExistingAgreement can't be changed after the offer is released. | 

## Update targeting configuration
<a name="update-targeting-offers"></a>

You can use the Catalog API to update the targeting configuration of your offer in AWS Marketplace. 

All existing targeting options that aren't included in the latest request and will be removed from the offer.

**Note**  
An offer can optionally include `PositiveTargeting` or `NegativeTargeting`, but not both.  
**Positive Targeting options:**  
**Country codes only** – Creates a public offer available to buyers in the specified countries.
**Buyer accounts only** – Creates a private offer targeted to specific AWS accounts.
**Both country codes and buyer accounts** – Creates a private offer where targeted accounts can only accept the offer if they are located in one of the specified countries.
**Negative Targeting options:**  
**Country codes** – Excludes buyers from the specified countries. This creates a public offer available to all countries except those listed.

To update the targeting configuration of your offer, call the `StartChangeSet` API operation with the `UpdateTargeting` change type, as shown in the following example. 

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
            "111122223333"
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
+ **Entity** (object) (required) – Your offer.
  + **Type** (string) (required) – The `Type` is always `Offer@1.0`. 
  + **Identifier** (string) (required) – Your offer ID. For more information, see [Identifier](catalog-apis.md#identifier).
+ **DetailsDocument** (object) (required) – The JSON value of specifics of the request.
  + **PositiveTargeting** (object) (optional) – Positive targeting defines the criteria which any buyer's profile should fulfill in order to be allowed to access the offer. This field is optional, but at least one targeting option should be provided when this field is present.
    + **CountryCodes** (array of strings) (optional) – List as option for allowing targeting based on country. If the intention isn't to target the offer to a country, this field should be omitted. If it's present, the list must contain at least one country code. Each element in this list should be a valid 2-letter country code, using this format: ISO 3166-1 alpha-2.
    + **BuyerAccounts** (array of strings) (optional) – List as an option to allow targeting based on AWS accounts (also known as Private Offer). If the intention is to not target the offer to an AWS account, this field should be omitted.
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

The change request is added to a queue and processed. This includes validating information to ensure that it meets the AWS Marketplace guidelines. The validation process can take a few minutes. 

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

**Synchronous Validations**

The following schema validations are specific to `UpdateTargeting` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | HTTP code | 
| --- | --- | --- | 
| NegativeTargeting | Optional<br />Can have either one of the following: [`CountryCodes`] | 422 | 
| NegativeTargeting.CountryCodes | Optional<br />List size must be between 1 and 244<br />Country codes must be valid (ISO 3166-1 alpha-2) | 422 | 
|  PositiveTargeting | Optional<br />Can have either one of the following: [`CountryCodes`, `BuyerAccounts`] | 422 | 
| PositiveTargeting.BuyerAccounts | Optional<br />List size must be between 1 and 26<br />AWS account IDs must be in valid format (12-digit number) | 422 | 
| PositiveTargeting.CountryCodes | Optional<br />List size must be between 1 and 244<br />Country codes must be valid (ISO 3166-1 alpha-2) | 422 | 

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
| INCOMPATIBLE\_TARGETING | BuyerAccounts can't be removed after the offer is released. | 
| INCOMPATIBLE\_TARGETING | BuyerAccounts can't be added after the offer is released. | 
| MISSING\_COUNTRY\_CODES | Provide PositiveTargeting with CountryCodes: [x]. | 
| INCOMPATIBLE\_COUNTRY\_CODES | Provide CountryCodes that are compatible. | 
| INCOMPATIBLE\_BUYER\_ACCOUNTS | Provide BuyerAccounts that are compatible with the agreement. | 

## Update refund policy
<a name="update-support-terms"></a>

You can use the Catalog API to update the refund policy of your offer in AWS Marketplace. 

This change doesn't affect existing agreements. The support terms that aren't included in the latest request will be removed from the offer.

To update the refund policy, call the `StartChangeSet` API operation with the `UpdateSupportTerms` change type, as shown in the following example. 

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "UpdateSupportTerms",
      "Entity": {
        "Type": "Offer@1.0",
        "Identifier": "offer-123456789"
      },
      "DetailsDocument": {
        "Terms": [
          {
            "Type": "SupportTerm",
            "RefundPolicy": "Updated refund policy description"
          }
        ]
      }
    }
  ]
}
```

Provide information for the fields to add the `UpdateSupportTerms` change type:
+ **Entity** (object) (required) – Your offer. 
  + **Type** (string) (required) – The `Type` is always `Offer@1.0`. 
  + **Identifier** (string) (required) – Your offer ID. For more information, see [Identifier](catalog-apis.md#identifier).
+ **DetailsDocument** (object) (required) – The JSON value of specifics of the request.
  + **Terms** (array of structures) (required) – List of support terms that you would like to update. Accepted support terms are:
    + **SupportTerm** (object) (required) – Defines the customer support available for the acceptors when they purchase the software.
      + **Type** (string) (required) – Type of the term being updated. This is the object value: `"SupportTerm"`.
      + **RefundPolicy** (string) (required) – Free-text field about the refund policy description that will be shown to customers as is on the website and console.

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

**Synchronous Validations**

The following schema validations are specific to `UpdateSupportTerms` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | HTTP code | 
| --- | --- | --- | 
| Terms | Required | 422 | 
| Terms[].RefundPolicy | Required<br />Length must be between 1 and 500<br />Cannot lead or end with spaces | 422 | 
| Terms[].Type | RequiredCan only be `SupportTerm` | 422 | 

**Asynchronous Errors**

The following errors are specific to `UpdateSupportTerms` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code  | Error message | 
| --- | --- | 
| INCOMPATIBLE\_PRODUCT | SupportTerm isn't supported in private offers for the product. | 
| INCOMPATIBLE\_TERMS | SupportTerm isn't supported for free trial offers. | 
| INCOMPATIBLE\_TERMS | The requested change can't be performed after the offer is released. | 
| INCOMPATIBLE\_TERMS | The requested change can't be performed after the offer is expired. | 

## Update legal resources
<a name="update-legal-terms"></a>

You can use the Catalog API to replace the existing legal documents, such as an end user license agreement (EULA). The legal terms that aren't included in the latest request will be removed from the offer. 

To update legal resources of your offer, call the `StartChangeSet` API operation with the `UpdateLegalTerms` change type, as shown in the following example.

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
+ **Entity** (object) (required) – Your offer. 
  + **Type** (string) (required) – The `Type` is always `Offer@1.0`. 
  + **Identifier** (string) (required) – Your offer ID. For more information, see [Identifier](catalog-apis.md#identifier).
+ **DetailsDocument** (object) (required) – The JSON value of specifics of the request.
  + **LegalTerm** (object) (required) – Defines the list of text agreements to be proposed to the acceptors. One example of such an agreement is the end user license agreement (EULA).
    + **Type** (string) (required) – Type of the term being updated. This is the object value: `"LegalTerm"`.
    + **Documents** (array of structures) (required) – List of references to legal resources to be proposed to the buyers. One example of such a resource is the end user license agreement (EULA). Each reference is made up of a `Type` and a `URL`:
      + **Type** (string) (required) – Type of document. Available document types are:
        + **CustomEula** – A custom EULA provided by you as seller. Either a public S3 URL or a [presigned URL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html) is required for this document type.
        + **StandardEula** – Standard Contract For AWS Marketplace (SCMP). For more information about SCMP, see the AWS Marketplace Seller Guide. You don't provide a URL for this type because it is managed by AWS Marketplace.
      + **Url** (string) (conditionally required) – A URL to the legal document for buyers to read. Required when `Type` is one of the following [`CustomEula`].
      + **Version** (string) (conditionally required) – Version of standard contracts provided by AWS Marketplace. Required when `Type` is [`StandardEula`]. Available version:
        + **2022-07-14** – This version of the Standard Contract for AWS Marketplace is available from this Amazon S3 bucket: [https://s3.amazonaws.com/aws-mp-standard-contracts/Standard-Contact-for-AWS-Marketplace-2022-07-14.pdf](https://s3.amazonaws.com/aws-mp-standard-contracts/Standard-Contact-for-AWS-Marketplace-2022-07-14.pdf)

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

**Synchronous Validations**

The following schema validations are specific to `UpdateLegalTerms` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | HTTP code | 
| --- | --- | --- | 
| Terms | Required<br />Only `LegalTerm` is allowed in the list<br />List size must be 1 | 422 | 
| Terms[].Type | RequiredCan only be `LegalTerm` | 422 | 
| Terms[].LegalTerm.Documents | Required | 422 | 
| Terms[].LegalTerm.Documents[].Type | Required<br />Allowed values:+  `CustomEula` <br />+  `StandardEula`  | 422 | 
| Terms[].LegalTerm.Documents[].Url | Required and must be a valid URL when Type is CustomEula | 422 | 
| Terms[].LegalTerm.Documents[].Version | Required and must be a valid Version when Type is StandardEulaValid `StandardEula` versions: ["2019-04-24", "2022-07-14"] | 422 | 

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
| INVALID\_LEGAL\_DOCUMENTS | LegalTerm contains password-protected document(s). Provide accessible documents in LegalTerm. | 
| INVALID\_LEGAL\_DOCUMENTS | LegalTerm contains invalid PDF document(s). Provide accessible documents in LegalTerm. | 

## Update pricing
<a name="update-pricing-terms"></a>

You can use the Catalog API to replace the existing pricing terms completely. The pricing terms that aren't included in the latest request will be removed from the offer. 

To update pricing terms for your offer, call the `StartChangeSet` API operation with the `UpdatePricingTerms` change type, as shown in the following example.

**Note**  
The following request syntax combines multiple examples. This combination doesn't work as a valid payload. For example, a `Terms` array can't include both the term type `FixedUpfrontPricingTerm` and the term type `ConfigurableUpfrontPricingTerm`. For examples of how different term types are combined for different pricing use cases, see [Manage offers with API](https://catalog.workshops.aws/mpseller/en-US/manage-offers-with-api) in the *AWS Marketplace seller workshop*.

**Note**  
For SaaS products with Free pricing model, you must include either `UsageBasedPricingTerm` or `ConfigurableUpfrontPricingTerm` with at least one RateCard (dimension) where all prices are set to $0.00. This requirement is unique to SaaS products.

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
      "DetailsDocument": {
        "PricingModel": "Usage",
        "Terms": [
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
            "Type": "ConfigurableUpfrontPricingTerm",
            "CurrencyCode": "USD",
            "RateCards": [
              {
                "Selector": {
                  "Type": "Duration",
                  "Value": "P365D"
                },
                "RateCard": [
                  {
                    "DimensionKey": "m3.large",
                    "Price": "300"
                  },
                  {
                    "DimensionKey": "m4.xlarge",
                    "Price": "400"
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
            "Type": "ByolPricingTerm"
          },
          {
            "Type": "RecurringPaymentTerm",
            "CurrencyCode": "USD",
            "BillingPeriod": "Monthly",
            "Price": "100.0"
          },
          {
            "Type": "FixedUpfrontPricingTerm",
            "CurrencyCode": "USD",
            "Price": "200.00",
            "Grants": [
              {
                "DimensionKey": "Users",
                "MaxQuantity": 10
              }
            ]
          },
          {
            "Type": "FreeTrialPricingTerm",
            "Duration": "P30D",
            "Grants": [
              {
                "DimensionKey": "m3.xlarge",
                "MaxQuantity": 10
              },
              {
                "DimensionKey": "m4.xlarge",
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
+ **Entity** (object) (required) – Your offer. 
  + **Type** (string) (required) – The `Type` is always `Offer@1.0`. 
  + **Identifier** (string) (required) – Your offer ID. For more information, see [Identifier](catalog-apis.md#identifier).
+ **DetailsDocument** (object) (required) – The JSON value of specifics of the request.
  + **PricingModel** (string) (required) – Pricing model for your offer. Possible values for pricing model are:
    + **Usage** – Usage-based pricing model where buyers will be billed for their usage of your product.
    + **Contract** – Contract-based pricing model where buyers are either billed in advance for the use of your product, or offered a flexible payment schedule. Buyers can also pay for an additional usage above their contract.
    + **Free** – Free pricing model where buyers will not be charged for usage of product. When using this pricing model no pricing terms or payment schedule term can have non-zero rates.
    + **Byol** – Byol pricing model where buyers will bring their own license for usage of the product.
  + **Terms** (array of structures) (required) – List of pricing terms that you want to update. Supported pricing terms are:
    + **FreeTrialPricingTerm** (object) – Defines a short-term free pricing model where the buyers are not charged anything within a specified limit.
      + **Type** (string) – Type of the term being updated. This is the object value: `"FreeTrialPricingTerm"`.
      + **Duration** (string) – Duration of the free trial period.
      + **Grants** (array of structures) – Entitlements that will be granted to the acceptor of a free trial as part of an agreement execution.
        + **DimensionKey** (string) – Unique dimension key defined in the product document. Dimensions represent categories of capacity in a product and are specified when the product is listed in AWS Marketplace.
        + **MaxQuantity** (integer) (optional) – Maximum amount of capacity that the buyer can be entitled to the given dimension of the product. If `MaxQuantity` is not provided, the buyer will be able to use an unlimited amount of the given dimension.
    + **UsageBasedPricingTerm** (object) – Defines a pay-as-you-go (PAYG) pricing model where the customers are charged based on product usage.
      + **Type** (string) (required) – Category of the term being updated. This is the object value: `UsageBasedPricingTerm`.
      + **CurrencyCode** (string) – Defines the currency for prices mentioned in this term. Currently, only USD is supported.
      + **RateCards** (array of structures) – List of rate cards.
        + **RateCard** (array of structures) – A rate card defines the per-unit rates for the product dimensions.
          + **DimensionKey** (string) –Dimension that the given entitlement applies. Dimensions represent categories of capacity in a product and are specified when the product is listed in AWS Marketplace.
          + **Price** (string) – Per-unit price for the product dimension that will be used for calculating the amount to be charged to the buyer.
    + **ConfigurableUpfrontPricingTerm** (object) – Defines pre-paid payment model which allows buyers to configure the entitlements that they want to purchase and the duration of the entitlements. You can update the list of rates for each contract duration and entitlements for each dimension.
      + **Type** (string) (required) – Type of the term being updated. This is the object value: `ConfigurableUpfrontPricingTerm`.
      + **CurrencyCode** (string) (required) – Defines the currency for the prices mentioned in this term. For public offers, only USD is supported. For private offers, USD, AUD, EUR, GBP, and JPY are supported.
      + **RateCards** (array of structures) (required) – List of rate cards.
        + **Selector** (object) (required) – Selector is used to differentiate between the mutually exclusive rate cards in the same pricing term, to be selected by the buyer.
          + **Type** (string) (required) – Category of Selector. At this time, only `Duration` is supported.
          + **Value** (string) (required) – Contract duration. This field supports the ISO 8601 format.
        + **RateCard** (array of structures) (required) – A rate card defines the per-unit rates for the product dimensions.
          + **DimensionKey** (string) (required) – Unique dimension key defined in the product document. Dimensions represent categories of capacity in a product and are specified when the product is listed in AWS Marketplace.
          + **Price** (string) (required) – Per-unit price for the product dimension which will be used for calculating the amount to be charged to the buyer.
        + **Constraints** (object) (required) – Defines constraints on how the term can be configured by acceptors.
**Note**  
Currently, **MultipleDimensionSelection** and **QuantityConfiguration** values need to be same.
          + **MultipleDimensionSelection** (string) (required) – Determines if buyers are allowed to select multiple dimensions in the rate card. Possible values are `Allowed` and `Disallowed`.
          + **QuantityConfiguration** (string) (required) – Determines if acceptors are allowed to configure quantity for each dimension in rate card. Possible values are `Allowed` and `Disallowed`.
    + **ByolPricingTerm** (object) – Enables you and your customers to move your existing agreements to AWS Marketplace. The customer won't be charged for product usage in AWS Marketplace because they already paid for the product outside of AWS Marketplace.
      + **Type** (string) (required) – Type of the term being updated. This is the object value: `ByolPricingTerm`.
    + **RecurringPaymentTerm** (object) – Defines a pricing model where customers are charged a fixed recurring price at the end of each billing period.
      + **Type** (string) (required) – Type of the term being updated. This is the object value: `RecurringPaymentTerm`.
      + **BillingPeriod** (string) (required) – Defines the recurrence at which buyers are charged. Only `Monthly` is supported today.
      + **Price** (string) (required) – Amount charged to the buyer every billing period.
      + **CurrencyCode** (string) (required) – Defines the currency for the prices mentioned in this term. Currently, only `USD` is supported.
    + **FixedUpfrontPricingTerm** (object) – Defines a pre-paid pricing model where the customers are charged a fixed upfront amount.
      + **Type** (string) (required) – Type of the term being updated. This is the object value: `FixedUpfrontPricingTerm`.
      + **CurrencyCode** (string) (required) – Defines the currency for the prices mentioned in this term. For public offers, only USD is supported. For private offers, USD, AUD, EUR, GBP, and JPY are supported.
      + **Price** (string) (required) – Fixed amount to be charged to the customer when this term is accepted.
      + **Grants** (array of structures) (required) – Entitlements that will be granted to the acceptor of fixed upfront as part of agreement execution.
        + **DimensionKey** (string) (required) – Unique dimension key defined in the product document. Dimensions represent categories of capacity in a product and are specified when the product is listed in AWS Marketplace.
        + **MaxQuantity** (integer) (required) – Maximum amount of capacity that the buyer can be entitled to the given dimension of the product. If `MaxQuantity` is not provided, the buyer will be able to use an unlimited amount of the given dimension.
      + **Duration** (string) (optional) – Defines the duration that the term remains active. This ﬁeld supports the ISO 8601 format.

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

**Synchronous Validations**

The following schema validations are specific to `UpdatePricingTerms` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | HTTP | 
| --- | --- | --- | 
| PricingModel | RequiredAllowed pricing models: ["Byol", "Free", "Usage", "Contract"] | 422 | 
| Terms | RequiredAllowed Terms: ["ConfigurableUpfrontPricingTerm", "ByolPricingTerm", "FreeTrialPricingTerm", "UsageBasedPricingTerm", "RecurringPaymentTerm", "FixedUpfrontPricingTerm"] | 422 | 
| Terms[].ByolPricingTerm | Required | 422 | 
| Terms[].ByolPricingTerm.Type | RequiredCan only be "ByolPricingTerm" | 422 | 
| Terms[].ConfigurableUpfrontPricingTerm | Required | 422 | 
| Terms[].ConfigurableUpfrontPricingTerm.Type | RequiredCan only be "ConfigurableUpfrontPricingTerm" | 422 | 
| Terms[].ConfigurableUpfrontPricingTerm.CurrencyCode | RequiredSupported currencies: ["USD", "AUD", "EUR", "GBP", "JPN"] | 422 | 
| Terms[].ConfigurableUpfrontPricingTerm.RateCards | RequiredList size must be between 1 and 5 | 422 | 
| Terms[].ConfigurableUpfrontPricingTerm.RateCards[].Constraints | Required | 422 | 
| Terms[].ConfigurableUpfrontPricingTerm.RateCards[].Contraints.MultipleDimensionSelection | RequiredAllowed values: ["Allowed", "Disallowed"] | 422 | 
| Terms[].ConfigurableUpfrontPricingTerm.RateCards[].Contraints.QuantityConfiguration | RequiredAllowed values: ["Allowed", "Disallowed"] | 422 | 
| Terms[].ConfigurableUpfrontPricingTerm.RateCards[].RateCard | RequiredList size must be between 1 and 800 | 422 | 
| Terms[].ConfigurableUpfrontPricingTerm.RateCards[].RateCard[].DimensionKey | RequiredLength must be between 1 and 100 | 422 | 
| Terms[].ConfigurableUpfrontPricingTerm.RateCards[].RateCard[].Price | RequiredData type is "String"<br />Non-negative decimals with up to 3 decimal places supported | 422 | 
| Terms[].ConfigurableUpfrontPricingTerm.RateCards[].Selector | Required | 422 | 
| Terms[].ConfigurableUpfrontPricingTerm.RateCards[].Selector.Type | RequiredAllowed values: ["Duration"] | 422 | 
| Terms[].ConfigurableUpfrontPricingTerm.RateCards[].Selector.Value | RequiredExpected format per Selector type: ISO 8601 duration | 422 | 
| Terms[].FixedUpfrontPricingTerm | Required | 422 | 
| Terms[].FixedUpfrontPricingTerm.Type | RequiredCan only be "FixedUpfrontPricingTerm" | 422 | 
| Terms[].FixedUpfrontPricingTerm.CurrencyCode | RequiredSupported currencies: ["USD", "AUD", "EUR", "GBP", "JPN"] | 422 | 
| Terms[].FixedUpfrontPricingTerm.Duration | RequiredExpected format per Selector type: ISO 8601 duration | 422 | 
| Terms[].FixedUpfrontPricingTerm.Grants | RequiredList size must be between 1 and 200 | 422 | 
| Terms[].FixedUpfrontPricingTerm.Grants[].DimensionKey | RequiredLength must be between 1 and 100 | 422 | 
| Terms[].FixedUpfrontPricingTerm.Grants[].MaxQuantity | RequiredValue must be greater than 0 | 422 | 
| Terms[].FixedUpfrontPricingTerm.Price | RequiredData type is "String"<br />Non-negative decimals with up to 3 decimal places supported | 422 | 
| Terms[].FreeTrialPricingTerm | Required | 422 | 
| Terms[].FreeTrialPricingTerm.Type | RequiredCan only be "FreeTrialPricingTerm" | 422 | 
| Terms[].FreeTrialPricingTerm.Duration | RequiredExpected format: ISO 8601 duration | 422 | 
| Terms[].FreeTrialPricingTerm.Grants | RequiredList size must be between 1 and 800 | 422 | 
| Terms[].FreeTrialPricingTerm.Grants[].DimensionKey | RequiredLength must be between 1 and 100 | 422 | 
| Terms[].FreeTrialPricingTerm.Grants[].MaxQuantity | OptionalValue must be greater than 0 | 422 | 
| Terms[].RecurringPaymentTerm | Required | 422 | 
| Terms[].RecurringPaymentTerm.Type | RequiredCan only be "RecurringPaymentTerm" | 422 | 
| Terms[].RecurringPaymentTerm.BillingPeriod | RequiredAllowed values: ["Monthly"] | 422 | 
| Terms[].RecurringPaymentTerm.CurrencyCode | RequiredSupported currencies: ["USD"] | 422 | 
| Terms[].RecurringPaymentTerm.Price | RequiredData type is "String"<br />Non-negative decimals with up to 3 decimal places supported | 422 | 
| Terms[].UsageBasedPricingTerm | Required | 422 | 
| Terms[].UsageBasedPricingTerm.Type | RequiredCan only be "UsagedBasedPricingTerm" | 422 | 
| Terms[].UsageBasedPricingTerm.CurrencyCode | RequiredSupported currencies: ["USD"] | 422 | 
| Terms[].UsageBasedPricingTerm.RateCards | RequiredMust be size of 1 | 422 | 
| Terms[].UsageBasedPricingTerm.RateCards[].RateCard | RequiredList size must be between 1 and 800 | 422 | 
| Terms[].UsageBasedPricingTerm.RateCards[].RateCard[].DimensionKey | RequiredLength must be between 1 and 100 | 422 | 
| Terms[].UsageBasedPricingTerm.RateCards[].RateCard[].Price | RequiredData type is "String"<br />Non-negative decimals with up to 8 decimal places supported | 422 | 

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
| INVALID\_CURRENCY\_CODE | Provide a supported CurrencyCode. | 
| INVALID\_CURRENCY\_CODE | Provide the same CurrencyCode across all pricing and payment terms. | 
| INVALID\_DURATION | Ensure Duration in FreeTrialPricingTerm is within the allowed range. | 
| INVALID\_DURATION | Provide Duration in FixedUpfrontPricingTerm that matches the duration between AgreementStartDate and AgreementEndDate. | 
| INVALID\_DURATION | Provide duration between [x] and [y] months. | 
| INVALID\_DURATION | Ensure duration granularity is at the day level for metered dimensions. | 
| INVALID\_GRANTS | Provide the same MaxQuantity for all Grants in FreeTrialPricingTerm. | 
| INVALID\_GRANTS | Provide Grants for all available metered dimensions in FreeTrialPricingTerm. | 
| INVALID\_GRANTS | The combination of Dimensions in grants is invalid in FixedUpfrontPricingTerm for the product. | 
| INVALID\_GRANTS | The combination of Dimensions in grants is invalid in FreeTrialPricingTerm for the product. | 
| INVALID\_GRANTS | FixedUpfrontPricingTerm with MaxQuantity is not supported for this product. | 
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
| INVALID\_RATE\_CARD | The combination of Dimensions in rate card is invalid in UsageBasedPricingTerm for the product. | 
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
| INCOMPATIBLE\_RATE\_CARD\_CONSTRAINTS | Set both MultipleDimensionSelection and QuantityConfiguration to the same value (Allowed or Disallowed) in ConfigurableUpfrontPricingTerm. | 
| INCOMPATIBLE\_RATE\_CARD\_CONSTRAINTS | Provide the same constraints for all rate cards in ConfigurableUpfrontPricingTerm. | 
| INVALID\_UPDATE\_REQUEST | [x] can't be updated. To request pricing change or for more information, contact the AWS Marketplace Managed Catalog Operations Team. | 
| INCOMPATIBLE\_PRICING\_MODEL | PricingModel can't change from [x] to [y]. | 
| INVALID\_GRANTS | MaxQuantity for the FreeTrialPricingTerm is limited for the product. Provide a MaxQuantity less than or equal to [x]. For more information, contact the AWS Marketplace Managed Catalog Operations Team. | 
| INVALID\_GRANTS | Provide MaxQuantity for all Grants in FixedUpfrontPricingTerm. | 
| INVALID\_GRANTS | MaxQuantity isn't supported in FixedUpfrontPricingTerm for the product. | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | Ensure Grants in FixedUpfrontPricingTerm matches RateCards specified in the ResaleAuthorization. | 

## Update the discoverability of the offer
<a name="update-availability"></a>

You can use the Catalog API to control the discoverability of your offer in AWS Marketplace. 

You can either choose to set a specific date in the future to restrict the discoverability of your offer or in the past to expire your offer. The `UpdateAvailability` change type doesn't affect existing agreements.

**Note**  
You can use the `UpdateAvailability` change type on a private offer that has already been [published](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/offers.html#release-offer) (also known as *released*). If buyers have already accepted the private offer, those existing agreements aren't affected.
When modifying the `AvailabilityEndDate` of an existing private offer, the [constraints of the agreement duration](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/offers.html#update-validity-terms) must be adhered to. If it's not, include an additional `UpdateValidityTerms` change type in this change set to modify the agreement duration to adhere to the new expiration. The `UpdateValidityTerms` change type can be used on a private offer that is either released or not yet released.
When modifying the `AvailabilityEndDate` of an existing private offer, the [constraints of the payment schedule](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/offers.html#update-payment-schedule-terms) must be adhered to. If it's not and the private offer is *not yet released*, include an additional `UpdatePaymentScheduleTerms` change type in this change set to modify the payment schedule to adhere to the new expiration. If the private offer is *already released*, you can only make changes to the `AvailabilityEndDate` as long as the new date adheres to the constraints of the payment schedule.

To control the discoverability of your offer, call the `StartChangeSet` API operation with the `UpdateAvailability` change type, as shown in the following example. 

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
+ **Entity** (object) (required) – Your offer. 
  + **Type** (string) (required) – The `Type` is always `Offer@1.0`. 
  + **Identifier** (string) (required) – Your offer ID. For more information, see [Identifier](catalog-apis.md#identifier).
+ **DetailsDocument** (object) (required) – The JSON value of specifics of the request.
  + **AvailabilityEndDate** (string) (required) – This is the date until when the offer is discoverable and purchasable in AWS Marketplace. You can choose to set a specific date in the future to restrict the availability or in the past to expire the offer. Dates are represented in `YYYY-MM-DD` format.

A change set is created for your request. The response to this request gives you the ID and ARN for the change set and looks like the following.

**Response Syntax**

```
{
  "ChangeSetId": "example123456789012abcdef",
   "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. It includes validating information to ensure that it meets the AWS Marketplace guidelines. The validation process can take a few minutes. You can check the status of the request through the AWS Marketplace Management Portal, or in the Catalog API with the `DescribeChangeSet` action.

**Synchronous Validations**

The following schema validations are specific to `UpdateAvailability` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | HTTP code | 
| --- | --- | --- | 
| AvailabilityEndDate | Required<br />Format: "YYYY-MM-DD" | 422 | 

**Asynchronous Errors**

The following errors are specific to `UpdateAvailability` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more details about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INVALID\_AVAILABILITY\_END\_DATE | AvailabilityEndDate isn't supported for public offers. | 
| INVALID\_AVAILABILITY\_END\_DATE | Provide a future AvailabilityEndDate. | 
| INVALID\_AVAILABILITY\_END\_DATE | Provide an AvailabilityEndDate that is before AgreementEndDate. | 
| MISSING\_AVAILABILITY\_END\_DATE | Provide an AvailabilityEndDate that is before the agreement's end date. | 

## Define the expiration date of agreements created using the offer
<a name="update-validity-terms"></a>

You can use the Catalog API to define the expiration date details of agreements created using the offer in AWS Marketplace. 

This change type doesn't affect existing agreements.

**Note**  
You can use the `UpdateValidityTerms` change type on a private offer that has already been [published](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/offers.html#release-offer) (also known as *released*). If buyers have already accepted the private offer, those existing agreements aren't affected.  
For **AMI-based** and **container-based** products, if your private offer [pricing terms](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/offers.html#update-pricing-terms) include a term type that has a `Duration` (for example, the term types `FixedUpfrontPricingTerm` or `ConfigurableUpfrontPricingTerm`), your `AgreementDuration` set in this change type must be greater than the following: the number of days from today to the [expiration of the private offer](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/offers.html#update-availability) plus the number of days set in the `Duration` of those term types. This is because after a buyer accepts the private offer and the agreement is created, they can optionally purchase additional entitlements specified in those term types until the private offer expires. Furthermore, all additional entitlements must end before the agreement does. For example, if the buyer accepts the private offer on the first available day and then purchases entitlements on the last available day, those entitlements must not end after the agreement end date.

To define the expiration date details of agreements created using the offer, call the `StartChangeSet` API operation with the `UpdateValidityTerms` change type, as shown in the following example. 

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
+ **Entity** (object) (required) – Your offer. 
  + **Type** (string) (required) – The `Type` is always `Offer@1.0`. 
  + **Identifier** (string) (required) – Your offer ID. For more information, see [Identifier](catalog-apis.md#identifier).
+ **DetailsDocument** (object) (required) – The JSON value of specifics of the request.
  + **Terms** (array of structures) – List of validity terms that you want to update. Supported validity terms are:
    + **ValidityTerm** (object) – Defines the conditions that will keep an agreement, created from this offer, valid.
      + **Type** (string) – Category of the term being updated. `ValidityTerm`
      + **AgreementDuration** (string) – Defines the duration that the agreement remains active. If `AgreementStartDate` isn't provided, agreement duration is relative to the agreement signature time. The duration is represented in the ISO\_8601 format.
      + **AgreementStartDate** (string) – Defines the date when agreement starts. `AgreementStartDate` is represented in `YYYY-MM-DD` format. The agreement starts at 00:00:00.000 UTC on the date provided. If `AgreementStartDate` isn't provided, agreement start date is determined based on agreement signature time.
      + **AgreementEndDate** (string) – Defines the date when the agreement ends. The `AgreementEndDate` is represented in `YYYY-MM-DD` format. The agreement ends at 23:59:59.999 UTC on the date provided. If `AgreementEndDate` isn't provided, the agreement end date is determined by the validity of individual terms.

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

**Synchronous Validations**

The following schema validations are specific to `UpdateValidityTerms` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | HTTP code | 
| --- | --- | --- | 
| Terms | Required | 422 | 
| Terms[].Type | Required<br />Can only be `"ValidityTerm"` | 422 | 
| Terms[].AgreementDuration | Optional<br />Expected format per Selector type: ISO 8601 duration<br />Can be stand alone or paired with `AgreementStartDate` | 422 | 
| Terms[].AgreementEndDate | Optional<br />Date must be formatted like `"YYYY-MM-DD"` | 422 | 
| Terms[].AgreementStartDate | Optional<br />Date must be formatted like `"YYYY-MM-DD"`<br />Can only be paired with `AgreementEndDate` and `AgreementDuration` | 422 | 

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
| INVALID\_AGREEMENT\_END\_DATE | Provide an AgreementEndDate that is within [x] years from today. | 
| INCOMPATIBLE\_AGREEMENT\_START\_DATE | Provide the same AgreementStartDate as defined in the agreement when the agreement has a future start date. | 
| INCOMPATIBLE\_AGREEMENT | AgreementStartDate can't be future dated when the agreement isn't future dated. | 

## Update payment schedule details
<a name="update-payment-schedule-terms"></a>

You can use the Catalog API to update payment schedule details for your offer, such as flexible payment schedule, in AWS Marketplace. 

**Note**  
You cannot use the `UpdatePaymentScheduleTerms` change type on an offer that has already been [published](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/offers.html#release-offer) (also known as *released*).  
The private offer can be accepted any day between the creation of the private offer and its [expiration](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/offers.html#update-availability) (set in the `AvailabilityEndDate`). Only one `ChargeDate` value of the payment schedule can be a date on or before the last day the buyer can accept the private offer (the private offer expiration date). The remaining values of `ChargeDate` must be after the private offer expiration, but no later than the end of the agreement if the private offer was accepted immediately. The end of the agreement is based on when the private offer is accepted (creating the agreement) plus the [duration of the agreement](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/offers.html#update-validity-terms).

To update payment schedule details for your offer, call the `StartChangeSet` API operation with the `UpdatePaymentScheduleTerms` change type, as shown in the following example.

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
+ **Entity** (object) (required) – Your offer. 
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

The change request is added to a queue and processed. This includes validating information to ensure that it meets the AWS Marketplace guidelines. The validation process can take a few minutes. 

You can check the status of the request through the AWS Marketplace Management Portal, or directly through Catalog API using the `[DescribeChangeSet](https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_DescribeChangeSet.html)` API operation.

**Synchronous Validations**

The following schema validations are specific to `UpdatePaymentScheduleTerms` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input Field | Validation Rule | HTTP | 
| --- | --- | --- | 
| Terms | Required<br />Only `PaymentScheduleTerm` is allowed<br />List size must be less than 2 | 422 | 
| Terms[].Type | Required<br />Can only be `PaymentScheduleTerm` | 422 | 
| Terms[].PaymentScheduleTerm.CurrencyCode | Required<br />Supported currencies: ["USD", "AUD", "EUR", "GBP", "JPY"] | 422 | 
| Terms[].PaymentScheduleTerm.Schedule[] | Required | 422 | 
| Terms[].PaymentScheduleTerm.Schedule[].ChargeAmount | RequiredDate type is "String"<br />Non-negative decimals with up to 2 decimal places supported | 422 | 
| Terms[].PaymentScheduleTerm.Schedule[].ChargeDate | Required<br />Date must be formatted like "YYYY-MM-DD" | 422 | 

**Asynchronous Errors**

The following errors are specific to `UpdatePaymentScheduleTerms` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


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
| INVALID\_CHARGE\_DATES | Provide a last charge date that is before AgreementEndDate. | 
| INVALID\_CHARGE\_DATES | Provide a first charge date that isn't in the past. | 
| TOO\_MANY\_CHARGES | Provide up to [x] scheduled payments in PaymentScheduleTerm. | 

## Update net payment terms
<a name="update-net-payment-terms"></a>

You can use the Catalog API to set the net payment terms of your offer in AWS Marketplace. A net payment term is a term where you specify the number of days after invoice issuance by which payment is due. 

**Note**  
Net payment terms are only supported for private offers, and only apply to buyers who have a pay-by-invoice payment method with AWS. If you don't set net payment terms, your buyer's payment terms with AWS apply.

To set the net payment term of your offer, call the `StartChangeSet` API operation with the `UpdateNetPaymentTerms` change type, as shown in the following example.

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
    + **NetPaymentTerm** (object) – Defines the net payment terms that is negotiated with the buyer.
      + **Type** (string) – Type of the term being updated. This is the object value: `"NetPaymentTerm"`.
      + **PaymentDuePeriod** (string) – The number of days after the invoice issuance date that payment is due. This field supports the ISO 8601 format. Supported values are `P15D`, `P30D`, `P45D`, `P60D`, `P90D`, and `P120D`.

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

**Synchronous Validations**

The following schema validations are specific to `UpdateNetPaymentTerms` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input Field | Validation Rule | HTTP | 
| --- | --- | --- | 
| Terms | Required<br />Only `NetPaymentTerm` is allowed<br />List size must be less than 2 | 422 | 
| Terms[].Type | Required<br />Can only be `NetPaymentTerm` | 422 | 
| Terms[].NetPaymentTerm.PaymentDuePeriod | Required<br />Expected format: ISO 8601 duration<br />Allowed values: ["P15D", "P30D", "P45D", "P60D", "P90D", "P120D"] | 422 | 

**Asynchronous Errors**

The following errors are specific to `UpdateNetPaymentTerms` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INVALID\_PAYMENT\_DUE\_PERIOD | Provide a supported PaymentDuePeriod. | 
| INCOMPATIBLE\_PRODUCT | The following terms aren't supported for the product: [x,y,z]. | 
| INCOMPATIBLE\_TERMS | NetPaymentTerm isn't supported for public offers. | 
| INCOMPATIBLE\_TERMS | The requested change can't be performed after the offer is released. | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | NetPaymentTerm isn't supported because the ResaleAuthorization doesn't contain a NetPaymentTerm. | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | NetPaymentTerm can't be removed because the ResaleAuthorization contains a NetPaymentTerm. | 
| INCOMPATIBLE\_RESALE\_AUTHORIZATION | Ensure PaymentDuePeriod in NetPaymentTerm is compatible with the ResaleAuthorization. | 
| DUPLICATE\_TERM\_TYPES | Provide a unique list of term types. | 

## Modify renewal options
<a name="update-renewal-terms"></a>

You can use the Catalog API to control renewal options of the agreements that are created using this offer in AWS Marketplace. 

For offers created through Catalog API, auto-renewal remains disabled by default until you call the `UpdateRenewalTerms` change type to allow auto-renewal. This change does not affect existing agreements.

To control renewal options of the agreements that are created using this offer, call the `StartChangeSet` API operation with the `UpdateRenewalTerms` change type, as shown in the following example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "UpdateRenewalTerms",
      "Entity": {
        "Type": "Offer@1.0",
        "Identifier": "offer-123456789"
      },
      "DetailsDocument": {
        "Terms": [
          {
            "Type": "RenewalTerm",
            "LockoutPeriod": "P30D",
            "AdjustmentDeadline": "P60D",
            "MaxRenewals": 3,
            "PriceIncrease": {
              "Type": "PercentageRange",
              "Range": {
                "MinValue": "3.00",
                "MaxValue": "10.00",
                "DefaultValue": "5.00"
              }
            },
            "TermTemplates": [
              {
                "Type": "PaymentScheduleTermTemplate",
                "Schedule": [
                  { "ChargeDateOffset": "P0M", "ChargePercentage": "50.00" },
                  { "ChargeDateOffset": "P6M", "ChargePercentage": "50.00", "DayOfMonth": 15 }
                ]
              }
            ]
          }
        ]
      }
    }
  ]
}
```

Provide information for the fields to add the `UpdateRenewalTerms` change type:
+ **Entity** (object) (required) – Your offer. 
  + **Type** (string) (required) – The `Type` is always `Offer@1.0`. 
  + **Identifier** (string) (required) – Your offer ID. For more information, see [Identifier](catalog-apis.md#identifier).
+ **DetailsDocument** (object) (required) – The JSON value of specifics of the request.
  + **Terms** (array of structures) – List of renewal terms that you want to update. Supported renewal terms are:
    + **RenewalTerm** (object) – Defines that on graceful termination (expiration of the `ValidityTerm`, not buyer or AWS Marketplace cancellation) of the agreement, a new agreement will be created using the accepted terms on the existing agreement. In other words, the agreement will be renewed. Presence of `RenewalTerm` in the offer means that auto-renewal is allowed. Buyers will have the option to accept or decline auto-renewal at the offer acceptance/agreement creation.
      + **Type** (string) (required) – Type of the term being updated. Must be `RenewalTerm`.
      + **LockoutPeriod** (string) (optional) – The period before the agreement end date after which the auto-renewal decision can no longer be changed. Until then, either the buyer or the seller can opt in to or opt out of the renewal; buyers and sellers see this as the renewal decision deadline. Expressed as an ISO 8601 duration in days of at least one day, and must be shorter than the agreement duration. If you omit this field, either party can change the auto-renewal decision until the agreement end date. For example, `P30D` puts the renewal decision deadline 30 days before the agreement end date; for an agreement that ends December 31, December 1 is the last day either party can opt in or opt out.
      + **AdjustmentDeadline** (string) (optional) – The deadline, before the agreement end date, by which the seller must finalize the renewal price. Required when `PriceIncrease` is a `PercentageRange`, and supported only with that type. Expressed as an ISO 8601 duration in days of at least one day, and must be shorter than the agreement duration. When `LockoutPeriod` is also provided, this duration must be at least one day longer, so that the deadline falls before the renewal decision deadline. For example, `P60D` requires the seller to finalize the renewal price 60 days before the agreement end date; for an agreement that ends December 31, the seller must finalize by November 1.
      + **MaxRenewals** (integer) (optional) – The maximum number of times the agreement can be renewed. If you omit this field, there is no limit on the number of renewals.
      + **PriceIncrease** (object) (required for private offers) – Specifies how the price can increase at renewal. Must be one of the following two types, identified by its `Type`:
        + **FixedPercentage** – Applies a fixed percentage increase at each renewal.
          + **Type** (string) (required) – The type of price increase. Must be `FixedPercentage`.
          + **Value** (string) (required) – A percentage between `0.00` and `100.00`, with up to two decimal places. Use `0.00` to renew at the same price.
        + **PercentageRange** – A seller-adjustable range for the renewal price increase.
          + **Type** (string) (required) – Must be `PercentageRange`.
          + **Range** (object) (required) – The `MinValue`, `MaxValue`, and `DefaultValue` for the range, each a percentage between `0.00` and `100.00` with up to two decimal places. `DefaultValue` applies if the seller doesn't finalize a percentage before the `AdjustmentDeadline`.
      + **TermTemplates** (array of structures) (optional) – A list containing at most one `PaymentScheduleTermTemplate`. It defines the payment schedule applied to renewed agreements.
        + **Type** (string) – The only supported value is `PaymentScheduleTermTemplate`.
        + **Schedule** (array of structures) – A list of `1`–`86` installments. The `ChargePercentage` values must sum to exactly 100.
          + **ChargeDateOffset** (string) – An ISO 8601 duration that offsets the charge from the agreement start date. Only month and day units are supported, and every offset in a schedule must use the same unit.
          + **ChargePercentage** (string) – A percentage from `0.01` to `100.00`, inclusive, with up to two decimal places.
          + **DayOfMonth** (integer) (optional) – The day of the month (`1`–`31`) on which the charge occurs. Supported only when `ChargeDateOffset` uses months.

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

**Synchronous Validations**

The following schema validations are specific to `UpdateRenewalTerms` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | HTTP code | 
| --- | --- | --- | 
| Terms | RequiredCan contain at most one renewal term. Provide an empty list to remove all renewal terms from the offer. | 422 | 
| Terms[].Type | RequiredCan only be "RenewalTerm" | 422 | 
| Terms[].LockoutPeriod | OptionalISO 8601 duration in days of at least one day, for example "P30D" | 422 | 
| Terms[].AdjustmentDeadline | OptionalISO 8601 duration in days of at least one day, for example "P60D" | 422 | 
| Terms[].MaxRenewals | OptionalInteger greater than or equal to 1 | 422 | 
| Terms[].PriceIncrease.Type | Required when PriceIncrease is providedCan only be "FixedPercentage" or "PercentageRange" | 422 | 
| Terms[].PriceIncrease.Value | Required when PriceIncrease.Type is "FixedPercentage"A percentage between 0.00 and 100.00, with up to two decimal places | 422 | 
| Terms[].PriceIncrease.Range | Required when PriceIncrease.Type is "PercentageRange"Must provide MinValue, MaxValue, and DefaultValue, each a percentage between 0.00 and 100.00 with up to two decimal places. MinValue must be less than or equal to DefaultValue, which must be less than or equal to MaxValue. MinValue and MaxValue must not be equal. | 422 | 
| Terms[].TermTemplates | OptionalCan contain at most one PaymentScheduleTermTemplate | 422 | 
| Terms[].TermTemplates[].Type | Required when TermTemplates is providedCan only be "PaymentScheduleTermTemplate" | 422 | 
| Terms[].TermTemplates[].Schedule | Required when TermTemplates is providedBetween 1 and 86 items | 422 | 
| Terms[].TermTemplates[].Schedule[].ChargeDateOffset | RequiredISO 8601 duration in months or days, for example "P6M" or "P30D". All offsets in a schedule must use the same unit. | 422 | 
| Terms[].TermTemplates[].Schedule[].ChargePercentage | RequiredA percentage between 0.01 and 100.00, with up to two decimal places | 422 | 
| Terms[].TermTemplates[].Schedule[].DayOfMonth | OptionalInteger between 1 and 31. Only supported with a month-based ChargeDateOffset. | 422 | 

**Asynchronous Errors**

The following errors are specific to `UpdateRenewalTerms` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more details about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| DUPLICATE\_CHARGE\_DATE\_OFFSETS | Provide unique ChargeDateOffset and DayOfMonth combinations in PaymentScheduleTermTemplate. | 
| INCOMPATIBLE\_PRODUCT | RenewalTerm isn't supported for ADX products with the following fields: [LockoutPeriod, MaxRenewals, AdjustmentDeadline, PriceIncrease]. | 
| INCOMPATIBLE\_TERMS | RenewalTerm isn't supported with the PricingModel. | 
| INCOMPATIBLE\_TERMS | RenewalTerm isn't supported for public offers with the following fields: [LockoutPeriod, MaxRenewals, AdjustmentDeadline, PriceIncrease]. | 
| INCOMPATIBLE\_TERMS | PaymentScheduleTermTemplate in RenewalTerm isn't supported without a PaymentScheduleTerm in the offer. | 
| INCOMPATIBLE\_TERMS | The requested change can't be performed after the offer is released. | 
| INCOMPATIBLE\_TERMS | The requested change can't be performed after the offer is expired. | 
| INVALID\_ADJUSTMENT\_DEADLINE | AdjustmentDeadline isn't supported with the provided PriceIncrease. | 
| INVALID\_ADJUSTMENT\_DEADLINE | Provide an AdjustmentDeadline that is at least 1 days longer than LockoutPeriod in RenewalTerm. | 
| INVALID\_ADJUSTMENT\_DEADLINE | Provide an AdjustmentDeadline in RenewalTerm that is less than agreement duration. | 
| INVALID\_CHARGE\_DATE\_OFFSETS | ChargeDateOffset(s) in PaymentScheduleTermTemplate may fall beyond AgreementDuration. Provide ChargeDateOffset(s) that are within AgreementDuration. | 
| INVALID\_CHARGE\_DATE\_OFFSETS | ChargeDateOffset(s) in PaymentScheduleTermTemplate may fall beyond the duration between AgreementStartDate and AgreementEndDate. Provide ChargeDateOffset(s) that are within that duration. | 
| INVALID\_CHARGE\_PERCENTAGES | ChargePercentage values in PaymentScheduleTermTemplate in the RenewalTerm must sum to 100. | 
| INVALID\_DAY\_OF\_MONTH | Multiple charges with ChargeDateOffset P0M can't each specify DayOfMonth in PaymentScheduleTermTemplate. | 
| INVALID\_DAY\_OF\_MONTH | Charges with ChargeDateOffset in the final month of the agreement can't specify DayOfMonth in PaymentScheduleTermTemplate. | 
| INVALID\_LOCKOUT\_PERIOD | Provide a LockoutPeriod in RenewalTerm that is less than agreement duration. | 
| INVALID\_PERCENTAGE\_RANGE | Provide a valid PercentageRange for PriceIncrease in RenewalTerm. | 
| INVALID\_PERCENTAGE\_RANGE | Use FixedPercentage instead of a PercentageRange with equal MinValue and MaxValue for PriceIncrease in RenewalTerm. | 
| INVALID\_UPDATE\_REQUEST | The change type UpdateRenewalTerms isn't supported on a renewal offer. | 
| MISSING\_ADJUSTMENT\_DEADLINE | Provide an AdjustmentDeadline in RenewalTerm with the provided PriceIncrease. | 
| MISSING\_MANDATORY\_TERMS | Provide a RenewalTerm for public offers with contract pricing for the product. | 
| MISSING\_PAYMENT\_SCHEDULE\_TERM\_TEMPLATE | Provide a PaymentScheduleTermTemplate in RenewalTerm when the offer contains a PaymentScheduleTerm. | 
| MISSING\_PRICE\_INCREASE | Provide PriceIncrease in RenewalTerm. | 

## Publish an offer
<a name="release-offer"></a>

You can use the Catalog API to merge the information collected from all update change types, and then publish the offer.

Offers remain in a `Draft` state, until `ReleaseOffer` is called. After the offer is released, it's discoverable in AWS Marketplace.

To publish your offer, call the `StartChangeSet` API operation with the `ReleaseOffer` change type, as shown in the following example. 

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
+ **Entity** (object) – The named type of entity being created. The `Identifier` is your offer ID, and the `Type` is always `Offer@1.0`. For more information, see [Identifier](catalog-apis.md#identifier).
+ **DetailsDocument** (object) – The JSON value of specifics of the request. It must be empty for `ReleaseOffer`.

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

**Synchronous Validations**

The following schema validations are specific to `ReleaseOffer` actions in the AWS Marketplace Catalog API. These validations are performed when you call `StartChangeSet`. If the request doesn't meet the following requirements, it will fail with an HTTP response.


| Input field | Validation rule | 
| --- | --- | 
| DetailsDocument | Must be empty ({}) | 

**Asynchronous Errors**

The following errors are specific to `ReleaseOffer` actions in the AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet` after a change set is processing. For more information about using `DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets).


| Error code | Error message | 
| --- | --- | 
| INCOMPATIBLE\_PAYMENT\_SETTINGS | Update your payment settings to be compatible with the CurrencyCode. | 
| INCOMPATIBLE\_PRODUCT | First create a public offer for the product. | 
| INCOMPATIBLE\_SELLER\_VERIFICATION | Complete all required seller verification processes. | 
| INCOMPATIBLE\_TARGETING | PreExistingAgreement is only supported for buyer targeted offers. | 
| INCOMPATIBLE\_TARGETING | OfferSetId is only supported for buyer targeted offers. | 
| INVALID\_TAX\_INFORMATION | Your tax information is incomplete. To sell professional services on AWS Marketplace, you must complete the DAC7 tax questionnaire. Navigate to the Payment Information section, and select the DAC7 tax form. It can take up to two hours for your tax information to update. | 
| INVALID\_UPDATE\_REQUEST | The requested change can't be performed after the offer is released. | 
| MISSING\_AGREEMENT\_END\_DATE | Provide an AgreementEndDate for replacement offers. | 
| MISSING\_AVAILABILITY\_END\_DATE | Provide an AvailabilityEndDate for private offer. | 
| MISSING\_BUYER\_ACCOUNTS | Provide PositiveTargeting with BuyersAccounts for offers created using ResaleAuthorization. | 
| MISSING\_BUYER\_ACCOUNTS | All offers for the product must be private. Provide PositiveTargeting with BuyersAccounts. | 
| MISSING\_DESCRIPTION | Set Description before releasing the offer. | 
| MISSING\_MANDATORY\_TERMS | Add [x] to the offer. | 
| MISSING\_MANDATORY\_TERMS | Provide a FixedUpfrontPricingTerm when the offer contains a PaymentScheduleTerm. | 
| MISSING\_NAME | Set Name before releasing the offer. | 
| TOO\_MANY\_OFFERS | Only one public free trial offer can be created per product. | 
| TOO\_MANY\_OFFERS | Only one public offer can be created per product. | 
| MISSING\_MANDATORY\_TERMS | Provide a RenewalTerm for public offers with contract pricing for the product. | 
| MISSING\_AGREEMENT\_END\_DATE | Provide an AgreementEndDate for replacement offers. | 

## Describe existing offer details
<a name="describe-entity"></a>

You can use the Catalog API to describe existing offer details in AWS Marketplace. 

To describe existing offer details, call the `DescribeEntity` API operation with the `Offer@1.0` entity type, as shown in the following example.

**Request Syntax**

```
GET /DescribeEntity?catalog=<Catalog>&entityId=<EntityId> HTTP/1.1
```

Provide information for the fields to add the `DescribeEntity` change type:
+ **catalog** (string) – The catalog related to the request. Fixed value: `AWSMarketplace`.
+ **entityId** (string) – The unique ID of the offer to describe.

**Response Syntax**

The response to this request gives you the offer details and looks like the following.

```
{
  "EntityType": "Offer@1.0",
  "EntityIdentifier": "offer-ad8EXAMPLE51@1",
  "EntityArn": "arn:aws:aws-marketplace:us-east-1:111122223333:AWSMarketplace/Offer/offer-ad8EXAMPLE51",
  "LastModifiedDate": "2021-03-10T21:57:16Z",
  "DetailsDocument": {
    "Id": "offer-3rEXAMPLErn",
    "State": "Released",
    "Name": "Test Offer",
    "Description": "Worldwide offer for Test Product",
    "PreExistingAgreement": {
      "AcquisitionChannel": "External",
      "PricingModel": "Contract"
    },
    "ProductId": "prod-ad8EXAMPLE51",
    "OfferSetId": "offerset-b3f9EXAMPLE27",
    "Terms": [
      {
        "Type": "SupportTerm",
        "RefundPolicy": "If you need to request a refund for software sold by Amazon Web Services, LLC, please contact AWS Customer Service."
      },
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
        "Type": "FreeTrialPricingTerm",
        "Duration": "P30D",
        "Grants": [
          {
            "DimensionKey": "m3.xlarge",
            "MaxQuantity": 10
          },
          {
            "DimensionKey": "m4.xlarge",
            "MaxQuantity": 10
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
              "Value": "P365D"
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
        "Type": "FixedUpfrontPricingTerm",
        "CurrencyCode": "USD",
        "Price": "200.00",
        "Grants": [
          {
            "DimensionKey": "Users",
            "MaxQuantity": 10
          }
        ]
      },
      {
        "Type": "RecurringPaymentTerm",
        "CurrencyCode": "USD",
        "BillingPeriod": "Monthly",
        "Price": "100.0"
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
      },
      {
        "Type": "ByolPricingTerm"
      },
      {
        "Type": "RenewalTerm"
      },
      {
        "Type": "NetPaymentTerm",
        "PaymentDuePeriod": "P30D"
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
            "444455556666"
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
        "AvailabilityEndDate": "2024-08-30T01:56:03.000Z"
      }
    ]
  }
}
```

The following is information about the fields you see in the `DescribeEntity` response.
+ **EntityType** (string) – The named type of the entity, which is `Offer@1.0`.
+ **EntityIdentifier** (string) – The identifier of the entity, in the format of `EntityId@RevisionId`.
+ **EntityArn** (string) – The ARN associated to the unique identifier for the change set referenced in this request.
+ **LastModifiedDate** (string) –The last modified date of the entity, in ISO 8601 format (for example: `2018-02-27T13:45:22Z`).
+ **Details** (string) – This stringified JSON object includes the following details of the entity:
  + **Id** (string) – Unique identifier for an offer entity in AWS Marketplace and is generated during the creation of an offer.
  + **State** (string) – The status of the offer.
  + **Name** (string) – The name associated with the offer for better readability to you and your customers. It will be displayed as part of Agreement information as well.
  + **Description** (string) – Description is a free-form text which is meant to be used only by you and will never be exposed to buyers.
  + **PreExistingAgreement** (string) – Determines if this offer is a renewal for an existing agreement with an existing customer for the same underlying product. The existing agreement can be within or outside AWS Marketplace. AWS may audit and verify your offer is a renewal. If AWS is unable to verify your offer, then AWS may revoke the offer and entitlements from your customer.
    + **AcquisitionChannel** (string) – Indicates if the existing agreement was signed outside AWS Marketplace or within AWS Marketplace. Possible values: `External`, `AwsMarketplace`.

       
    + **PricingModel** (string) – Indicates which pricing model the existing agreement uses. Possible values: `Contract`, `Usage`, `Byol`, `Free`.
  + **ProductId** (string) – The unique identifier of the product being offered.
  + **OfferSetId** (string) – The unique identifier of the offer set to associate this offer with.
  + **Terms** (array of structures) – List of terms.
  + **Rules** (array of structures) – List of rules.