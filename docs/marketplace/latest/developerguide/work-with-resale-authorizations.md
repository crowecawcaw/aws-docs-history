The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Work with resale authorizations using the AWS Marketplace APIs

You can use the AWS Marketplace Catalog API to automate tasks for working with Resale Authorizations.

While the _product_ describes what is being sold in
AWS Marketplace, the _Resale Authorization_ (also known as an
opportunity) describes the terms and rules regarding how this product is authorized to
be resold in AWS Marketplace. The _CPPO_ is the target of the
Resale Authorization.

A Resale Authorization has a collection of terms and rules to be accepted for a
reseller agreement between manufacturers and channel partners. Accepting the terms of
the Resale Authorization allows the reseller to create offers for the product per the
conditions expressed in the terms.

There are two types of rules in a Resale Authorization:

- **AvailabilityRule** – Controls the
  lifecycle of the Resale Authorization in AWS Marketplace.
- **PartnerTargetingRule** – Specifies
  whether the Resale Authorization should be accessible to a specific set of
  channel partners.
  See the following resources:

- For end-to-end labs with working code examples, see [Lab: Authorize a reseller](https://catalog.workshops.aws/mpseller/en-US/manage-offers-with-api/authorize-a-reseller "https://catalog.workshops.aws/mpseller/en-US/manage-offers-with-api/authorize-a-reseller") in the _AWS Marketplace
  seller workshop_.
- For code examples of API requests, see [Python](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/python/src/catalog_api/resale_authorization "https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/python/src/catalog_api/resale_authorization") and [Java](https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java/resources/changeSets/channel_partner_offers "https://github.com/aws-samples/aws-marketplace-reference-code/tree/main/java/resources/changeSets/channel_partner_offers") examples in _AWS Samples_
  on GitHub.
- For a video on creating resale authorizations, see [Create Resale
  Authorizations Using the AWS Marketplace Catalog API](https://www.youtube.com/watch?v=vLIbvFYI974 "https://www.youtube.com/watch?v=vLIbvFYI974") on YouTube.
  The following topics describe how to use the Catalog API to create and update Resale
  Authorizations:

###### Topics

- [Resale Authorization prerequisites](#prerequisites "#prerequisites")
- [Create a new Resale Authorization](#create-resale-authorization "#create-resale-authorization")
- [Update buyer targeting](#update-buyer-targeting "#update-buyer-targeting")
- [Update availability](#update-availability-resale-auth "#update-availability-resale-auth")
- [Update the validity of a future dated agreement](#update-validity-fda "#update-validity-fda")
- [Update legal resources](#update-existing-legal-terms "#update-existing-legal-terms")
- [Update pricing](#update-existing-pricing-terms "#update-existing-pricing-terms")
- [Update payment schedule](#update-payment-schedule-details "#update-payment-schedule-details")
- [Update net payment terms](#update-resale-net-payment-terms "#update-resale-net-payment-terms")
- [Update Resale Authorization details](#update-resale-auth-information "#update-resale-auth-information")
- [Restrict a Resale Authorization](#restricte-resale-auth "#restricte-resale-auth")
- [Release a Resale Authorization and make it visible to a Channel Partner](#release-resale-auth "#release-resale-auth")
- [Describe an existing Resale Authorization](#describe-entity-resale-auth "#describe-entity-resale-auth")

## Resale Authorization prerequisites

To use Resale Authorization, both independent software vendors (ISVs) and AWS Marketplace
Channel Partners must create a service-linked role that provides resource-sharing
permissions to AWS. If both groups don't perform this prerequisite, AWS can't
share the authorization resource from the ISV to the AWS Marketplace Channel Partner. For more
information, see [Using roles for Resale Authorization for AWS Marketplace](../userguide/using-roles-for-resale-authorization.md "../userguide/using-roles-for-resale-authorization.md") in the _AWS Marketplace
Seller Guide_.

## Create a new Resale Authorization

You can use the Catalog API to create a new Resale Authorization in AWS Marketplace.

If your request is processed successfully, AWS Marketplace Catalog API generates a Resale
Authorization in `Draft` state for you. It's an incomplete Resale
Authorization and not visible to channel partners in AWS Marketplace.

Use the `Update` change types to complete the Resale Authorization.
After the Resale Authorization is completed, use the
`ReleaseResaleAuthorization` change type to complete the Resale
Authorization creation process and release the Resale Authorization, which will
validate the entire Resale Authorization and make your it visible to channel
partners in AWS Marketplace.

To create a Resale Authorization in `Draft` state, call the
`StartChangeSet` API operation with the
`CreateResaleAuthorization` change type, as shown in the following
example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "CreateResaleAuthorization",
      "ChangeName": "xyz",
      "Entity":
      {
        "Type": "ResaleAuthorization@1.0"
      },
      "DetailsDocument":
      {
        "ProductId": "prod-ad8EXAMPLE51",
        "Name": "Test ResaleAuthorization",
        "Description": "Worldwide ResaleAuthorization for Test Product",
        "ResellerAccountId": "777788889999"
      }
    }
  ]
}

```

Provide information for the input fields to add the
`CreateResaleAuthorization` change type:

- **Entity** (object) (required) – Your
  Resale Authorization.

  - **Type** (string) (required) –
    The `Type` is always
    `ResaleAuthorization@1.0`.

- **DetailsDocument** (object) (required)
  – Specifics of the request.

  - **ProductId** (string) (required)
    – Product ID for which to create the resale
    authorization.
  - **Name** (string) (required) –
    Name associated with the ResaleAuthorization for better readability
    to you and your channel partners.
  - **Description** (string) (optional)
    – A free-form text field available to add details about the
    ResaleAuthorization.
  - **ResellerAccountId** (string)
    (required) – Add targeted channel partner's AWS account who
    can describe and use this `ResaleAuthorization` to create
    a private offer.

**Response Syntax**

A change set is created for your request. The response to this request gives you
the `ChangeSetId` and `ChangeSetArn` for the change set and
looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through
Catalog API using the `DescribeChangeSet` API operation.

When the request is complete (if the `Status` is
`SUCCEEDED`), a new `ResaleAuthorization` is generated.
Although the `SUCCEEDED` status indicates that the
`CreateResaleAuthorization` change type call is completed, the
`ResaleAuthorization` status is still in `Draft`
state.

The following shows the response from the [DescribeChangeSet](../../../marketplace-catalog/latest/api-reference/API_DescribeChangeSet.md "../../../marketplace-catalog/latest/api-reference/API_DescribeChangeSet.md") API operation.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef",
  "ChangeSetName": "Submitted by 123456789012",
  "StartTime": "2021-05-27T22:21:26Z",
  "EndTime": "2021-05-27T22:32:19Z",
  "Status": "SUCCEEDED",
  "ChangeSet":
  [
    {
      "ChangeType": "CreateResaleAuthorization",
      "Entity":
      {
        "Type": "ResaleAuthorization@1.0",
        "Identifier": "resaleauthz-123456789"
      },
      "DetailsDocument":
      {
        "ProductId": "prod-ad8EXAMPLE51",
        "Name": "Test ResaleAuthorization",
        "Description": "Worldwide ResaleAuthorization for Test Product",
        "ResellerAccountId": "777788889999",
        "BulkRequestId": "84977023-5093-4a66-8b24-ef2c5a2f8b1f"
      },
      "ErrorDetailList":
      []
    }
  ]
}
```

**Synchronous Validations**

The schema validations are specific to `CreateResaleAuthorization`
actions in the AWS Marketplace Catalog API. The validations are performed when you call
`StartChangeSet`. If the request doesn't meet the following
requirements, it will fail with an HTTP response.

| Input field         | Validation rule                                                                                                       | HTTP code |
| ------------------- | --------------------------------------------------------------------------------------------------------------------- | --------- |
| ProductId           | Required<br>Must not be null or empty<br>Length must be between 1 and 50 characters                                   | 422       |
| ProductId           | User must be authorized to create ResaleAuthorization for the<br>given product                                        | 403       |
| ProductId           | Must be an existing product in the catalog and not in<br>`Draft` state Product should be supported to<br>resell       | 404       |
| Name                | Required<br>Must not be null or empty<br>Length must be between 1 and 100 characters<br>No special characters allowed | 422       |
| Description         | Optional<br>Length must be between 1 and 255 characters<br>No special characters allowed                              | 422       |
| ResellerAccountId   | Required<br>Must not be empty<br>AWS account IDs must be in valid format (12-digit<br>number)                         | 422       |
| BulkRequestId       | Optional<br>Length must be between 1 and 50 characters<br>Must be in UUID format                                      | 422       |
| An unknown property | No additional properties are allowed                                                                                  | 422       |

**Asynchronous Errors**

The following errors are specific to `CreateResaleAuthorization`
actions in the AWS Marketplace Catalog API. These errors are returned when you call
`DescribeChangeSet` after a change set is processing. For more
information about using `DescribeChangeSet` to get the status of a change
request, see [Working with change sets](catalog-apis.md#working-with-change-sets "catalog-apis.md#working-with-change-sets").

| Error code                 | Error message                           |
| -------------------------- | --------------------------------------- |
| INVALID\_RESELLER\_ACCOUNT | **`Provide a valid reseller account.`** |

## Update buyer targeting

You can use the Catalog API to update buyers targeting your Resale Authorization
in AWS Marketplace.

Any existing targeting options that aren't included in the latest request are
removed from the Resale Authorization. This change type is optional for release of
the Resale Authorization.

To update buyers targeting your Resale Authorization, call the
`StartChangeSet` API operation with the
`UpdateBuyerTargetingTerms` change type, as shown in the following
example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
   "Catalog": "AWSMarketplace",
   "ChangeSet": [
      {
         "ChangeType":"UpdateBuyerTargetingTerms",
         "Entity":{
            "Type": "ResaleAuthorization@1.0",
            "Identifier": "resaleauthz-123456789"
         },
         "DetailsDocument":
         {
           "Terms":
           [
             {
               "Type": "BuyerTargetingTerm",
               "PositiveTargeting":
               {
                 "BuyerAccounts":
                 [
                  "123456789012"
                 ]
               }
             }
           ]
         }
      }
   ]
}
```

Provide information for the fields to add the
`UpdateBuyerTargetingTerms` change type:

- **Entity** (object) (required) – Your
  Resale Authorization.

  - **Type** (string) (required) –
    The `Type` is always
    `ResaleAuthorization@1.0`.
  - **Identifier** (string) (required)
    – Your Resale Authorization ID. For more information, see
    [Identifier](catalog-apis.md#identifier "catalog-apis.md#identifier").

- **DetailsDocument** (object) (required)
  – Specifics of the request.

  - **Terms** (array of structures)
    (optional) – List of buyers targeting terms that you want to
    update. If the intentions aren't to target the
    `ResaleAuthorization` to any specific buyer, then
    terms field can be skipped. By default,
    `ResaleAuthorization` is targeted to all buyers.
    Supported terms are:

    - **BuyerTargetingTerms**
      (object) (optional) – Define buyer-specific targeting
      to your ResaleAuthorization.

      - **Type** (string)
        (required) – Category of the term being
        updated.
      - **PositiveTargeting**
        (object) (required) – Defines the criteria
        that any buyer's profile should fulfill to be
        allowed access to the
        `ResaleAuthorization`.

        - **BuyerAccounts** (array of strings)
          (optional) – List as optional. You can add
          the targeted buyer's AWS accounts. If the
          intention isn't to target
          `ResaleAuthorization` to specific
          buyers, then this field should be omitted. By
          default, all buyers are targeted. Targeted channel
          partners can choose to create a private offer and
          target a subset of buyers, if specified.

**Response Syntax**

A change set is created for your request. The response to this request gives you
the `ChangeSetId` and `ChangeSetArn` for the change set and
looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating
information with the AWS Marketplace Seller Operations team to ensure it meets the AWS Marketplace
guidelines. The validation process can take anywhere from a few minutes to a few
hours.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through
Catalog API using the `DescribeChangeSet` API operation.

**Synchronous Validations**

The schema validations are specific to `UpdateBuyerTargetingTerms`
actions in the AWS Marketplace Catalog API. These validations are performed when you call
`StartChangeSet`. If the request doesn't meet the following
requirements, it will fail with an HTTP response.

| Input field                                        | Validation rule                                                                                                                                                                     |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Terms                                              | Optional<br>Must not be null or empty<br>Only "BuyerTargetingTerm" is allowed in the list<br>List size must be 1 (there is no use case today that requires<br>multiple buyer terms) |
| BuyerTargetingTerm.PositiveTargeting               | Required<br>Must not be empty                                                                                                                                                       |
| BuyerTargetingTerm.PositiveTargeting.BuyerAccounts | Optional<br>AWS account IDs must be in valid format (12-digit<br>number)<br>Must not contain more than 25 accounts                                                                  |
| An unknown property                                | No additional properties are allowed                                                                                                                                                |

**Asynchronous Errors**

The following errors are specific to `UpdateBuyerTargetingTerms`
actions in the AWS Marketplace Catalog API. These errors are returned when you call
`DescribeChangeSet` after a change set is processing. For more
information about using `DescribeChangeSet` to get the status of a change
request, see [Working with change sets](catalog-apis.md#working-with-change-sets "catalog-apis.md#working-with-change-sets").

| Error code                     | Error message                                                                                                  |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| INCOMPATIBLE\_BUYER\_TARGETING | **`At least one Buyer account must be present for<br>ResaleAuthorization with<br>PreExistingBuyerAgreement.`** |

## Update availability

You can use the Catalog API to limit the availability of how many private offers
are created or until what specific time a private offer can be created.

By default, the value is unlimited usage of this Resale Authorization, although
you can check the availability under the rule list.

To control the availability and usability of your Resale Authorization, call the
`StartChangeSet` API operation with the
`UpdateAvailability` change type, as shown in the following example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "UpdateAvailability",
      "Entity":
      {
        "Type": "ResaleAuthorization@1.0",
        "Identifier": "resaleauthz-123456789"
      },
      "DetailsDocument":
      {
        "AvailabilityEndDate": "2022-05-31",
        "OffersMaxQuantity": 1
      }
    }
  ]
}
```

Provide information for the fields to add the `UpdateAvailability`
change type:

- **Entity** (object) (required) – Your
  Resale Authorization.

  - **Type** (string) (required) –
    The `Type` is always
    `ResaleAuthorization@1.0`.
  - **Identifier** (string) (required)
    – Your Resale Authorization ID. For more information, see
    [Identifier](catalog-apis.md#identifier "catalog-apis.md#identifier").

- **DetailsDocument** (object) (required)
  – Specifics of the request.

  - **AvailabilityEndDate** (string)
    (optional) – Define the end date until Channel Partners can
    leverage the `ResaleAuthorization` to create an offer.
    Channel Partners can use this `ResaleAuthorization`
    multiple times until the specified end date. Dates are represented
    in ISO\_8601 format.
  - **OffersMaxQuantity** (integer)
    (optional) – Define the maximum number of private offers that
    can be created using the ResaleAuthorization. This doesn't define
    the number of subscriptions.

**Response Syntax**

A change set is created for your request. The response to this request gives you
the `ChangeSetId` and `ChangeSetArn` for the change set and
looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating
information with the AWS Marketplace Seller Operations team to ensure it meets the AWS Marketplace
guidelines. The validation process can take anywhere from a few minutes to a few
hours.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through
Catalog API using the `DescribeChangeSet` API operation.

**Synchronous Validations**

The schema validations are specific to `UpdateAvailability` actions in
the AWS Marketplace Catalog API. The validations are performed when you call
`StartChangeSet`. If the request doesn't meet the following
requirements, it will fail with an HTTP response

| Input field         | Validation rule                                                                                                            |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| OffersMaxQuantity   | Optional<br>Must be non-negative integer<br>Allowed value only "1" (Currently no use case to support<br>multiple quantity) |
| AvailabilityEndDate | Optional<br>Must be ISO\_8601 formatted<br>Must be date in the future                                                      |
| Availability        | Provide either OffersMaxQuantity or AvailabilityEndDate.                                                                   |
| An unknown property | No additional properties are allowed                                                                                       |

**Asynchronous Errors**

The following errors are specific to `UpdateAvailability` actions in
the AWS Marketplace Catalog API. These errors are returned when you call
`DescribeChangeSet` after a change set is processing. For more
information about using `DescribeChangeSet` to get the status of a change
request, see [Working with change sets](catalog-apis.md#working-with-change-sets "catalog-apis.md#working-with-change-sets").

| Error code                       | Error message                                                                                            |
| -------------------------------- | -------------------------------------------------------------------------------------------------------- |
| INVALID\_AVAILABILITY\_END\_DATE | **`Provide an AvailabilityEndDate that is before all the<br>ChargeDate in ResalePaymentScheduleTerms.`** |
| INVALID\_AVAILABILITY\_END\_DATE | **`Provide a future<br>AvailabilityEndDate.`**                                                           |

## Update the validity of a future dated agreement

You can use the Catalog API to modify and control a future dated service start
date in AWS Marketplace.

This change set is not mandatory to release a Resale Authorization.

To modify and control the product agreement duration of your Resale Authorization,
call the `StartChangeSet` API operation with the
`UpdateBuyerValidityTerms` change type, as shown in the following
example.

###### Note

Future-dated agreements are only supported for SaaS product types.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "UpdateBuyerValidityTerms",
      "Entity":
      {
        "Type": "ResaleAuthorization@1.0",
        "Identifier": "resaleauthz-123456789"
      },
      "DetailsDocument":
      {
        "Terms":
        [
          {
            "Type": "BuyerValidityTerm",
            "MaximumAgreementStartDate": "2024-05-31"
          }
        ]
      }
    }
  ]
}
```

Provide information for the input fields to add the
`UpdateBuyerValidityTerms` change type:

- **Entity** (object) (required) – Your
  Resale Authorization.

  - **Type** (string) (required) –
    The `Type` is always
    `ResaleAuthorization@1.0`.
  - **Identifier** (string) (required)
    – Your Resale Authorization ID. For more information, see
    [Identifier](catalog-apis.md#identifier "catalog-apis.md#identifier").

- **DetailsDocument** (object) (required)
  – Specifics of the request.

  - **Terms** (array of structures)
    – List of agreement validity terms that you want to update.
    Supported terms are:

    - **BuyerValidityTerm**
      (object) – Defines the availabilities of a service
      for a product in your ResaleAuthorization.

      - **Type** (string)
        – Category of term being updated.
      - **MaximumAgreementStartDate** (string)
        (required) – Define the agreement start date
        for the product offered. Future dated offers can't
        exceed this service start date. Dates are
        represented in ISO\_8601 format.

**Response Syntax**

A change set is created for your request. The response to this request gives you
the `ChangeSetId` and `ChangeSetArn` for the change set and
looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating
information with the AWS Marketplace Seller Operations team to ensure it meets the AWS Marketplace
guidelines. The validation process can take anywhere from a few minutes to a few
hours.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through
Catalog API using the `DescribeChangeSet` API operation.

**Synchronous Validations**

The schema validations are specific to `UpdateBuyerValidityTerms`
actions in the AWS Marketplace Catalog API. The validations are performed when you call
`StartChangeSet`. If the request doesn't meet the following
requirements, it will fail with an HTTP response.

| Input field               | Validation rule                                                                                                                                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Terms                     | Required<br>Must not be null or empty<br>Only "BuyerValidityTerm" is allowed in the list<br>List size must be 1 (there's no use case today that requires<br>multiple service availability terms) |
| MaximumAgreementStartDate | Required<br>Must not be null or empty<br>Must be future date and shouldn't exceed more than 3 years<br>from now<br>Must be ISO\_8601 formatted                                                   |
| An unknown property       | No additional properties are allowed                                                                                                                                                             |

**Asynchronous Errors**

The following errors are specific to `UpdateBuyerValidityTerms`
actions in the AWS Marketplace Catalog API. These errors are returned when you call
`DescribeChangeSet` after a change set is processing. For more
information about using `DescribeChangeSet` to get the status of a change
request, see [Working with change sets](catalog-apis.md#working-with-change-sets "catalog-apis.md#working-with-change-sets").

| Error code                               | Error message                                                              |
| ---------------------------------------- | -------------------------------------------------------------------------- |
| INCOMPATIBLE\_PRODUCT                    | **`BuyerValidityTerm isn't supported for the<br>product.`**                |
| INVALID\_MAXIMUM\_AGREEMENT\_START\_DATE | **`Provide a future MaximumAgreementStartDate with in<br>allowed limit.`** |

## Update legal resources

You can use the Catalog API to replace the existing legal terms completely in
AWS Marketplace.

The legal terms that aren't included in the latest request will be removed from
the Resale Authorization. `BuyerLegalTerm` contains the EULA which will
be included on the final buyer agreement and `LegalTerm` includes the
Reseller Contract which will be included in the reseller agreement between the
channel partner and the ISV.

To update legal terms of your `ResaleAuthorization`, call the
`StartChangeSet` API operation with the `UpdateLegalTerms`
change type, as shown in the following example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "UpdateLegalTerms",
      "Entity":
      {
        "Type": "ResaleAuthorization@1.0",
        "Identifier": "resaleauthz-123456789"
      },
      "DetailsDocument":
      {
        "Terms":
        [
          {
            "Type": "BuyerLegalTerm",
            "Documents":
            [
              {
                "Type": "CustomEula",
                "Url": "https://my-public-bucket.s3.amazonaws.com/eula-example12345.txt"
              }
            ]
          },
          {
            "Type": "ResaleLegalTerm",
            "Documents":
            [
              {
                "Type": "CustomResellerContract",
                "Url": "https://my-public-bucket.s3.amazonaws.com/reseller-example12345.txt"
              }
            ]
          }
        ]
      }
    }
  ]
}

```

Provide information for the fields to add the `UpdateLegalTerms` change
type:

- **Entity** (object) (required) – Your
  Resale Authorization.

  - **Type** (string) (required) –
    The `Type` is always
    `ResaleAuthorization@1.0`.
  - **Identifier** (string) (required)
    – Your Resale Authorization ID. For more information, see
    [Identifier](catalog-apis.md#identifier "catalog-apis.md#identifier").

- **DetailsDocument** (object) (required)
  – Specifics of the request.

  - **Terms** (array of structures)
    (required) – List of legal terms. Supported legal terms
    are:

    - **BuyerLegalTerm** (object)
      (required) – Defines the list of text agreements to
      be proposed to acceptors. For example, the end user license
      agreement (EULA).
    - **Type** (string) (required)
      – Category of the term being updated.
    - **Documents** (array of
      structures) (required) – List of references to legal
      resources to be proposed to the buyers. For example, the
      EULA. Each reference is made up of a `Type` and a
      `URL`:

      - **Type** (string)
        (required) – Type of document. Available
        document types are:

        - **StandardEula** – Standard
          Contract for AWS Marketplace. For more information, see
          [SCMP](../userguide/standardized-license-terms.md#standard-contracts "../userguide/standardized-license-terms.md#standard-contracts") in the _AWS Marketplace
          Seller Guide_. You don't need to provide
          a URL for this type because it's managed by
          AWS Marketplace.
        - **EnterpriseEula** – Enterprise
          Contract for AWS Marketplace. For more information, see DSA
          in the AWS Marketplace Seller Guide. You don't need to
          provide a URL for this type because it's managed
          by AWS Marketplace.
        - **CustomEula**
          – Custom EULA provided by you as a
          manufacturer. A URL for the EULA stored in an
          accessible S3 bucket is required for this document
          type.

      - **Url** (string)
        (conditionally required) – A URL to the legal
        document for buyers to read. This is required when
        category Type is `CustomEula`.

    - **ResaleLegalTerm** (object)
      (optional) – Defines the list of text agreements to
      propose only to channel partners. This term won't be
      available to buyers.

      - **Type** (string)
        (required) – Category of term being
        updated.
      - **Documents** (array
        of structures) (required) – List of
        references to the reseller legal resources to be
        proposed to the channel partners.

        - **Type**
          (string) (required) – Category of the
          document. Available document types are:

          - **StandardResellerContract** –
            Standard Reseller Contract for AWS Marketplace.
          - **CustomResellerContract** – A
            custom reseller contract by you as a manufacturer.
            A URL for the reseller contract is stored in an
            accessible S3 bucket and is required for this
            document type.

        - **Url**
          (string) (conditionally required) – URL to
          the reseller contract document for channel
          partners to read. It's required when the Type is
          CustomResellerContract.

**Response Syntax**

A change set is created for your request. The response to this request gives you
the `ChangeSetId` and `ChangeSetArn` for the change set and
looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating
information to ensure that it meets the AWS Marketplace guidelines. The validation process can
take anywhere from a few minutes to a few hours.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through
Catalog API using the `DescribeChangeSet` API operation.

**Synchronous Validations**

The schema validations are specific to `UpdateLegalTerms` actions in
the AWS Marketplace Catalog API. The validations are performed when you call
`StartChangeSet`. If the request doesn't meet the following
requirements, it will fail with an HTTP response.

| Input field                              | Validation rule                                                                                                                                   | HTTP code |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| Terms                                    | Required<br>Must not be null or empty                                                                                                             | 422       |
| Terms[].BuyerLegalTerm                   | Required<br>Must not be null or empty                                                                                                             | 422       |
| Terms[].ResaleLegalTerm                  | Optional<br>Must not be null or empty if present                                                                                                  | 422       |
| Terms[].BuyerLegalTerm.Documents         | Required<br>Must not be null or empty                                                                                                             | 422       |
| Terms[].BuyerLegalTerm.Documents[].Type  | Required<br>Must not be null or empty<br>Allowed values:<br>• StandardEula<br>• EnterpriseEula<br>• CustomEula                                    | 422       |
| Terms[].BuyerLegalTerm.Documents[].Url   | Required and must be a valid URL when "Type" is "CustomEula"<br>Must not be provided when "Type" is one of<br>["StandardEula", "EnterpriseEula"]  | 422       |
| Terms[].ResaleLegalTerm.Documents        | Required<br>Must not be null or empty                                                                                                             | 422       |
| Terms[].ResaleLegalTerm.Documents[].Type | Required<br>Must not be null or empty Allowed values:<br>• StandardEula<br>• CustomResellerContract                                               | 422       |
| Terms[].ResaleLegalTerm.Documents[].Url  | Required and must be a valid URL when "Type" is<br>"CustomResellerContract"<br>Must not be provided when "Type" is one of<br>["StandardContract"] | 422       |
| An unknown property                      | No additional properties are allowed                                                                                                              | 422       |

**Asynchronous Errors**

The following errors are specific to `UpdateLegalTerms` actions in the
AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet`,
after a change set is processing. For more information about using
`DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets "catalog-apis.md#working-with-change-sets").

| Error code                        | Error message                                                                     |
| --------------------------------- | --------------------------------------------------------------------------------- |
| INVALID\_BUYER\_LEGAL\_DOCUMENTS  | **`Provide URLs for buyer legal documents stored in<br>accessible S3 buckets.`**  |
| INVALID\_RESALE\_LEGAL\_DOCUMENTS | **`Provide URLs for resale legal documents stored in<br>accessible S3 buckets.`** |
| MISSING\_MANDATORY\_TERMS         | **`Provide a BuyerLegalTerm.`**                                                   |

## Update pricing

You can use the Catalog API to replace the existing pricing terms completely in
AWS Marketplace.

Pricing terms that aren't included in the latest request will be removed from the
Resale Authorization. You can update the discounted pricing for your product through
this API.

To update pricing details for your Resale Authorizations, call the
`StartChangeSet` API operation with the
`UpdatePricingTerms` change type, as shown in the following example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "UpdatePricingTerms",
      "Entity":
      {
        "Type": "ResaleAuthorization@1.0",
        "Identifier": "resaleauthz-123456789"
      },
      "DetailsDocument":
      {
        "PricingModel": "Contract",
        "Terms":
        [
          {
            "Type": "ResaleUsageBasedPricingTerm",
            "CurrencyCode": "USD",
            "RateCards":
            [
              {
                "RateCard":
                [
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
            "Type": "ResaleConfigurableUpfrontPricingTerm",
            "CurrencyCode": "USD",
            "RateCards":
            [
              {
                "Selector":
                {
                  "Type": "Duration",
                  "Value": "P12M"
                },
                "RateCard":
                [
                  {
                    "DimensionKey": "m3.large",
                    "Price": "300"
                  },
                  {
                    "DimensionKey": "m4.xlarge",
                    "Price": "400"
                  }
                ],
                "Constraints":
                {
                  "MultipleDimensionSelection": "Allowed",
                  "QuantityConfiguration": "Allowed"
                }
              }
            ]
          },
          {
            "Type": "ResaleFixedUpfrontPricingTerm",
            "CurrencyCode": "USD",
            "Duration": "P2M",
            "Price": "200.0",
            "Grants":
            [
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

Provide information for the fields to add the `UpdatePricingTerms`
change type:

- **Entity** (object) (required) – Your
  Resale Authorization.

  - **Type** (string) (required) –
    The `Type` is always
    `ResaleAuthorization@1.0`.
  - **Identifier** (string) (required)
    – Your Resale Authorization ID. For more information, see
    [Identifier](catalog-apis.md#identifier "catalog-apis.md#identifier").

- **DetailsDocument** (object) (required)
  – Specifics of the request.

  - **PricingModel** (string) (required)
    – Pricing model for your offer. Possible values for pricing
    model are:

    - **Usage** –
      Usage-based pricing model where buyers will be billed for
      their usage of your product.
    - **Contract** – In the
      contract-based pricing model, buyers are either billed in
      advance for the use of your product or offered a flexible
      payment schedule. Buyers can also pay for additional usage
      above their contract. Channel partners can add their markup
      to this payment schedule and pricing for each
      dimension.

  - **Terms** (array of structures)
    (required) – List of pricing terms that you want to update.
    Supported pricing terms are:

    - **ResaleUsageBasedPricingTerm** (object)
      – Defines a pay-as-you-go (PAYG) pricing model where
      the customers are charged based on product usage.

      - **Type** (string)
        (required) – Category of the term.
      - **CurrencyCode**
        (string) – Defines the currency for prices
        mentioned in this term. Currently, only USD is
        supported.
      - **RateCards** (array
        of structures) – List of rate cards.

        - **RateCard**
          (array of structures) – A rate card defines
          the per-unit rates for the product
          dimensions.

          - **DimensionKey** (string) –
            Dimension for which the given entitlement applies.
            Dimensions represent categories of capacity in a
            product and are specified when the product is
            listed in AWS Marketplace.
          - **Price**
            (string) – Per unit price for the product
            dimension which is used for calculating the amount
            to be charged.

        - **Constraints**
          (object) (optional) – Defines limits on how
          the term can be configured by acceptors.

          - **MultipleDimensionSelection** (string)
            (optional) – Determines if buyers are
            allowed to select multiple dimensions in the rate
            card. Possible values are `Allowed` and
            `Disallowed`. Default value is
            `Allowed`.
          - **QuantityConfiguration** (string)
            (optional) – Determines if acceptors are
            allowed to configure quantity for each dimension
            in rate card. Possible values are
            `Allowed` and `Disallowed`.
            Default value is `Allowed`.

    - **ResaleFixedUpfrontPricingTerm** (object)
      – Defines a pre-paid pricing model where the
      customers are charged a fixed upfront amount.

      - **Type** (string)
        (required) – Category of the term being
        updated.
      - **CurrencyCode**
        (string) – Defines the currency for prices
        mentioned in this term. Defines the currency for the
        prices mentioned in this term. USD, AUD, EUR, GBP,
        and JPY are supported.
      - **Price** (string)
        (required) – Fixed amount to be charged to
        the customer when this term is accepted.
      - **Duration** (string)
        (required) – Contract duration of the
        ResaleAuthorization. This field supports the ISO
        8601 format.
      - **Grants** (array of
        structures) (required) – Entitlements that
        will be granted to the acceptor of fixed upfront
        pricing as part of agreement execution.

        - **DimensionKey** (string) (required)
          – Unique dimension key defined in the
          product document. Dimensions represent categories
          of capacity in a product and are specified when
          the product is listed in AWS Marketplace.
        - **MaxQuantity**
          (integer) (required) – Maximum amount of
          capacity that the buyer can be entitled to the
          given dimension of the product. If MaxQuantity is
          not provided, the buyer will be able to use an
          unlimited amount of the given dimension.

**Response Syntax**

A change set is created for your request. The response to this request gives you
the `ChangeSetId` and `ChangeSetArn` for the change set and
looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating
information to ensure that it meets the AWS Marketplace guidelines. The validation process can
take anywhere from a few minutes to a few hours.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through
Catalog API using the `DescribeChangeSet` API operation.

**Synchronous Validations**

The following schema validations are specific to `UpdatePricingTerms`
actions in the AWS Marketplace Catalog API. The validations are performed when you
call `StartChangeSet`. If the request doesn't meet the following
requirements, it will fail with an HTTP response.

| Input field                                                                    | Validation rule                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Terms                                                                          | Required<br>Must not be null or empty<br>Each term must present only single time Allowed terms:<br>• \* ResaleUsageBasedPricingTerm<br>• \* ResaleConfigurableUpfrontPricingTerm<br>• \* ResaleFixedupfrontPricingTerm |
| Terms[].ResaleUsageBasedPricingTerm.CurrencyCode                               | Required<br>Allowed values: USD                                                                                                                                                                                        |
| Terms[].ResaleUsageBasedPricingTerm.Validity                                   | Required<br>Must not be null or empty<br>Expected format: ISO 8601 duration                                                                                                                                            |
| Terms[].ResaleUsageBasedPricingTerm.RateCards                                  | Required<br>Must not be null or empty                                                                                                                                                                                  |
| Terms[].ResaleUsageBasedPricingTerm.RateCards[].DimensionKey                   | Required<br>Must not be null or empty<br>Length must be between 1 and 60                                                                                                                                               |
| Terms[].ResaleUsageBasedPricingTerm.RateCards[].Price                          | Required<br>Must not be null or empty<br>Data type is "String"<br>Must be non-negative<br>Support up to 8 Decimal<br>No special characters supported                                                                   |
| Terms[].ResaleConfigurableUpfrontPricingTerm.CurrencyCode                      | Required<br>Allowed values: ["USD", "AUD", "EUR", "GBP", "JPN"]                                                                                                                                                        |
| Terms[].ResaleConfigurableUpfrontPricingTerm.RateCards[].Selector.Type         | Required<br>Must not be null or empty<br>Allowed values: Duration                                                                                                                                                      |
| Terms[].ResaleConfigurableUpfrontPricingTerm.RateCards[].Selector.Value        | Required<br>Must not be null or empty<br>Expected format: ISO 8601 duration                                                                                                                                            |
| Terms[].ResaleConfigurableUpfrontPricingTerm.RateCards[].RateCard.DimensionKey | Required<br>Must not be null or empty<br>Length must be between 1 and 60                                                                                                                                               |
| Terms[].ResaleConfigurableUpfrontPricingTerm.RateCards[].RateCard.Price        | Required<br>Must not be null or empty<br>Data type is "String"<br>Must be non-negative<br>Support up to 6 Decimal<br>No special characters supported                                                                   |
| Terms[].ResaleConfigurableUpfrontPricingTerm.RateCards[].Constraints           | Optional                                                                                                                                                                                                               |
| Terms[].ResaleFixedUpfrontPricingTerm.CurrencyCode                             | Required Allowed values: ["USD", "AUD", "EUR", "GBP",<br>"JPN"]                                                                                                                                                        |
| Terms[].ResaleFixedUpfrontPricingTerm.Price                                    | Required<br>Must not be null or empty<br>Data type is "String"<br>Must be non-negative<br>Support up to 6 Decimal<br>No special characters supported<br>Allowed values: 0.0                                            |
| Terms[].ResaleFixedUpfrontPricingTerm.Duration                                 | Required<br>Must not be null or empty<br>Expected format: ISO 8601 duration                                                                                                                                            |
| Terms[].ResaleFixedUpfrontPricingTerm.Grants[].DimensionKey                    | Required<br>Must not be null or empty<br>Length must be between 1 and 60                                                                                                                                               |
| Terms[].ResaleFixedUpfrontPricingTerm.Grants[].MaxQuantty                      | Required<br>Must not be null or empty                                                                                                                                                                                  |
| An unknown property                                                            | No additional properties are allowed                                                                                                                                                                                   |

**Asynchronous Errors**

The following errors are specific to `UpdatePricingTerms` actions in
the AWS Marketplace Catalog API. These errors are returned when you call
`DescribeChangeSet` after a change set is processing. For more
information about using `DescribeChangeSet` to get the status of a change
request, see [Working with change sets](catalog-apis.md#working-with-change-sets "catalog-apis.md#working-with-change-sets").

| Error code                            | Error message                                                                                                                                                           |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| INVALID\_CURRENCY\_CODE               | **`Provide the same CurrencyCode across all pricing and<br>payment terms.`**                                                                                            |
| INCOMPATIBLE\_PRODUCT                 | **`Use existing, available dimensions in the product in<br>[x].`**                                                                                                      |
| DUPLICATE\_DIMENSION\_KEYS            | **`Provide rate card with a unique list of dimension keys<br>in [x]`**                                                                                                  |
| INVALID\_RATE\_CARD                   | **`Provide dimensions that have the same unit in<br>[x]`**                                                                                                              |
| INVALID\_RATE\_CARD                   | **`Provide a rate card for only metered dimensions in<br>ResaleUsageBasedPricingTerm.`**                                                                                |
| INVALID\_RATE\_CARD                   | **`Provide usage based rates for all available metered<br>dimensions in ResaleUsageBasedPricingTerm.`**                                                                 |
| TOO\_MANY\_RATES                      | **`Provide RateCards within the allowed limits in<br>ResaleUsageBasedPricingTerm.`**                                                                                    |
| DUPLICATE\_SELECTORS                  | **`Provide a unique list of Selectors in<br>ResaleConfigurableUpfrontPricingTerm.`**                                                                                    |
| INVALID\_RATE\_CARD                   | **`ConfigurableUpfrontPricingTerm is missing one or more<br>dimension keys for duration [x]. Provide prices for the same set<br>of dimension keys for all durations.`** |
| INVALID\_RATE\_CARD                   | **`Provide either all metered or all entitled dimensions<br>in [x].`**                                                                                                  |
| INCOMPATIBLE\_RATE\_CARD\_CONSTRAINTS | **`Set MultipleDimensionSelection and<br>QuantityConfiguration to Disallowed in<br>ResaleConfigurableUpfrontPricingTerm for the<br>PricingModel.`**                     |
| TOO\_MANY\_RATE\_CARDS                | **`Only one rate card in ConfigurableUpfrontPricingTerm<br>is allowed for the product.`**                                                                               |
| INCOMPATIBLE\_TERMS                   | **`The following terms aren't compatible with the<br>PricingModel: [x,y,z].`**                                                                                          |
| TOO\_MANY\_RATES                      | **`Provide RateCards within the allowed limits in [x<br>term].`**                                                                                                       |
| TOO\_MANY\_GRANTS                     | **`Provide up to [N] grants in [x<br>term].`**                                                                                                                          |
| INVALID\_SELECTOR\_DURATION\_VALUE    | **`Provide duration between [x] and [y] months in<br>ResaleConfigurableUpfront`**                                                                                       |
| TOO\_MANY\_GRANTS                     | **`Provide duration between [x] and [y]<br>months.`**                                                                                                                   |
| INVALID\_SELECTOR\_DURATION\_VALUE    | **`Ensure duration granularity is at the day level for<br>metered dimensions in<br>ResaleConfigurableUpfront`**                                                         |
| INVALID\_DURATION                     | **`Ensure duration granularity is at the day level for<br>metered dimensions in FixedUpfront.`**                                                                        |
| INVALID\_RATE\_CARD                   | **`Provide only entitled dimensions in<br>[x].`**                                                                                                                       |
| MISSING\_DURATION                     | **`Provide a Duration in [x].`**                                                                                                                                        |
| DUPLICATE\_DIMENSION\_KEYS            | **`Provide Grants with a unique list of dimension keys in<br>[x].`**                                                                                                    |
| INCOMPATIBLE\_PAYMENT\_SETTINGS       | **`Update your payment settings to be compatible with the<br>CurrencyCode.`**                                                                                           |
| INCOMPATIBLE\_SELLER\_VERIFICATION    | **`Complete all required seller verification<br>processes.`**                                                                                                           |
| INVALID\_CURRENCY\_CODE               | **`Provide a supported CurrencyCode.`**                                                                                                                                 |
| INVALID\_CURRENCY\_CODE               | **`Provide the same CurrencyCode across all pricing and<br>payment terms.`**                                                                                            |
| INCOMPATIBLE\_CURRENCY\_CODE          | **`CurrencyCode can't be changed after the offer is<br>released.`**                                                                                                     |

## Update payment schedule

You can use the Catalog API to change payment-associated details, such as a
flexible payment schedule, in AWS Marketplace.

To update payment-associated details for your Resale Authorization, call the
`StartChangeSet` API operation with the
`UpdatePaymentScheduleTerms` change type, as shown in the following
example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "UpdatePaymentScheduleTerms",
      "Entity":
      {
        "Type": "ResaleAuthorization@1.0",
        "Identifier": "resaleauthz-123456789"
      },
      "DetailsDocument":
      {
        "Terms":
        [
          {
            "Type": "ResalePaymentScheduleTerm",
            "CurrencyCode": "USD",
            "Schedule":
            [
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

Provide information for the fields to add the
`UpdatePaymentScheduleTerms` change type:

- **Entity** (object) (required) – Your
  Resale Authorization.

  - **Type** (string) (required) –
    The `Type` is always
    `ResaleAuthorization@1.0`.
  - **Identifier** (string) (required)
    – Your Resale Authorization ID. For more information, see
    [Identifier](catalog-apis.md#identifier "catalog-apis.md#identifier").

- **DetailsDocument** (object) (required)
  – Specifics of the request.

  - **Terms** (array of structures)
    – List of payment terms that you want to update. Supported
    payment terms are:

    - **ResalePaymentScheduleTerm**
      (object) – Defines an installment-based pricing model
      where the customers are charged a fixed price on different
      dates during the agreement validity period.

      - **Type** (string)
        – Category of the term being updated.
      - **CurrencyCode**
        (string) (required) – Defines the currency
        for the payment mentioned in the schedule. USD, AUD,
        EUR, GBP, and JPY are supported.
      - **Schedule** (array
        of structures) – List of the payment schedule
        where each element defines one installment of
        payment. It contains the information necessary for
        calculating the price to be paid and the date on
        which the customer would be charged.

        - **ChargeDate**
          (string) (required) – The date the customer
          would pay the price defined in this payment
          schedule term. This field supports the ISO 8601
          format.
        - **ChargeAmount** (string) (required)
          – The price the customer would pay on a
          scheduled date (ChargeDate).

**Response Syntax**

A change set is created for your request. The response to this request gives you
the `ChangeSetId` and `ChangeSetArn` for the change set and
looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating
information to ensure that it meets the AWS Marketplace guidelines. The validation process can
take anywhere from a few minutes to a few hours.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through
Catalog API using the `DescribeChangeSet` API operation.

**Synchronous Validations**

The schema validations are specific to `UpdatePaymentScheduleTerms`
actions in the AWS Marketplace Catalog API. The validations are performed when you call
`StartChangeSet`. If the request doesn't meet the following
requirements, it will fail with an HTTP response.

| Input field                                            | Validation rule                                                                       | HTTP |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------- | ---- |
| Terms.Type                                             | Required<br>Not supported for [x] product<br>Allowed terms: ResalePaymentScheduleTerm | 422  |
| Terms[].CurrencyCode                                   | Required<br>Allowed values: USD                                                       | 422  |
| Terms[].ResalePaymentScheduleTerm.Schedule             | Required<br>Length must be between 1 and 60                                           | 422  |
| Terms[].ResalePaymentScheduleTerm.Shedule.ChargeDate   | Required<br>Must be in ISO 8601 format<br>Date must be in the future                  | 422  |
| Terms[].ResalePaymentScheduleTerm.Shedule.ChargeAmount | Required<br>Must be non-negative                                                      | 422  |
| An unknown property                                    | No additional properties are allowed                                                  | 422  |

**Asynchronous Errors**

The following errors are specific to `UpdatePaymentScheduleTerms`
actions in the AWS Marketplace Catalog API. These errors are returned when you call
`DescribeChangeSet` after a change set is processing. or more
information about using `DescribeChangeSet` to get the status of a change
request, see [Working with change sets](catalog-apis.md#working-with-change-sets "catalog-apis.md#working-with-change-sets").

| Error code                         | Error message                                                                                      |
| ---------------------------------- | -------------------------------------------------------------------------------------------------- |
| INCOMPATIBLE\_TERMS                | **`OffersMaxQuantity and AvailabilityEndDate must be<br>present with ResalePaymentScheduleTerm.`** |
| TOO\_MANY\_SCHEDULED\_PAYMENTS     | **`Provide up to 60 scheduled payments in<br>ResalePaymentScheduleTerm.`**                         |
| DUPLICATE\_CHARGE\_DATES           | **`Provide unique charge dates in<br>ResalePaymentScheduleTerm.`**                                 |
| INVALID\_CHARGE\_DATES             | **`Provide a future ChargeDate.`**                                                                 |
| INVALID\_CHARGE\_DATES             | **`Provide a last charge date that is before<br>[x].`**                                            |
| MISSING\_MANDATORY\_TERMS          | **`Provide a ResaleFixedUpfrontPricingTerm and<br>ResalePaymentScheduleTerm together.`**           |
| INVALID\_CURRENCY\_CODE            | **`Provide the same CurrencyCode across all pricing and<br>payment terms.`**                       |
| INCOMPATIBLE\_PAYMENT\_SETTINGS    | **`Update your payment settings to be compatible with the<br>CurrencyCode.`**                      |
| INCOMPATIBLE\_SELLER\_VERIFICATION | **`Complete all required seller verification<br>processes.`**                                      |
| INVALID\_CURRENCY\_CODE            | **`Provide a supported CurrencyCode.`**                                                            |
| INVALID\_CURRENCY\_CODE            | **`Provide the same CurrencyCode across all pricing and<br>payment terms.`**                       |
| INCOMPATIBLE\_CURRENCY\_CODE       | **`CurrencyCode can't be changed after the offer is<br>released.`**                                |

## Update net payment terms

You can use the Catalog API to set the net payment terms of your Resale
Authorization in AWS Marketplace. A net payment term is a term where you specify the number of
days after invoice issuance by which payment is due.

The net payment term that you set on a Resale Authorization is the maximum term
that the channel partner can offer to a buyer in a channel partner private offer
(CPPO). The channel partner can offer the same period or a shorter one, but not a
longer one. For more information, see [Create a CPPO](work-with-cppos.md#create-offer-using-resale-auth "work-with-cppos.md#create-offer-using-resale-auth").

###### Note

Net payment terms only apply to buyers who have a pay-by-invoice payment method
with AWS. If you don't set net payment terms on your Resale Authorization, the
channel partner can't set net payment terms on the CPPO, and the buyer's payment
terms with AWS apply.

To set the net payment term of your Resale Authorization, call the
`StartChangeSet` API operation with the
`UpdateNetPaymentTerms` change type, as shown in the following
example.

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
        "Type": "ResaleAuthorization@1.0",
        "Identifier": "resaleauthz-123456789"
      },
      "DetailsDocument": {
        "Terms": [
          {
            "Type": "ResaleNetPaymentTerm",
            "PaymentDuePeriod": "P60D"
          }
        ]
      }
    }
  ]
}
```

Provide information for the fields to add the
`UpdateNetPaymentTerms` change type:

- **Entity** (object) (required) – Your
  Resale Authorization.

  - **Type** (string) (required) –
    The `Type` is always
    `ResaleAuthorization@1.0`.
  - **Identifier** (string) (required)
    – Your Resale Authorization ID. For more information, see
    [Identifier](catalog-apis.md#identifier "catalog-apis.md#identifier").

- **DetailsDocument** (object) (required)
  – The JSON value of specifics of the request.

  - **Terms** (array of structures)
    (required) – List of net payment terms that you want to
    update. A Resale Authorization can contain at most one net payment
    term. To remove the net payment term, provide an empty list.
    Supported terms are:

    - **ResaleNetPaymentTerm**
      (object) – Defines the maximum net payment term that
      the channel partner can offer to a buyer.

      - **Type** (string)
        – Type of the term being updated. This is the
        object value:
        `"ResaleNetPaymentTerm"`.
      - **PaymentDuePeriod**
        (string) – The number of days after the
        invoice issuance date that payment is due. This
        field supports the ISO 8601 format. Supported values
        are `P15D`, `P30D`,
        `P45D`, `P60D`,
        `P90D`, and
        `P120D`.

**Response Syntax**

A change set is created for your request. The response to this request gives you
the `ChangeSetId` and `ChangeSetArn` for the change set and
looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating
information to ensure that it meets the AWS Marketplace guidelines. The validation process can
take a few minutes.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through
Catalog API using the `DescribeChangeSet` API operation.

**Synchronous Validations**

The following schema validations are specific to
`UpdateNetPaymentTerms` actions in the AWS Marketplace Catalog API. These validations
are performed when you call `StartChangeSet`. If the request doesn't meet
the following requirements, it will fail with an HTTP response.

| Input field                                   | Validation rule                                                                                                        | HTTP code |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------- |
| Terms                                         | Required<br>Only `ResaleNetPaymentTerm` is allowed<br>List size must be less than 2                                    | 422       |
| Terms[].Type                                  | Required<br>Can only be `ResaleNetPaymentTerm`                                                                         | 422       |
| Terms[].ResaleNetPaymentTerm.PaymentDuePeriod | Required<br>Expected format: ISO 8601 duration<br>Allowed values: ["P15D", "P30D", "P45D", "P60D", "P90D",<br>"P120D"] | 422       |

**Asynchronous Errors**

The following errors are specific to `UpdateNetPaymentTerms` actions in
the AWS Marketplace Catalog API. These errors are returned when you call
`DescribeChangeSet` after a change set is processing. For more
information about using `DescribeChangeSet` to get the status of a change
request, see [Working with change sets](catalog-apis.md#working-with-change-sets "catalog-apis.md#working-with-change-sets").

| Error code           | Error message                                                                                         |
| -------------------- | ----------------------------------------------------------------------------------------------------- |
| INCOMPATIBLE\_STATUS | **`UpdateNetPaymentTerms request can't be performed after<br>the resale authorization is released.`** |
| INCOMPATIBLE\_TERMS  | **`ResaleNetPaymentTerm is not supported for the seller<br>account [x].`**                            |

## Update Resale Authorization details

You can use the Catalog API to update Resale Authorization details in
AWS Marketplace.

To update Resale Authorization details, call the `StartChangeSet` API
operation with the `UpdateInformation` change type, as shown in the
following example.

###### Note

The `UpdateInformation` change type only updates the sections
provided in the request; all other information remains unchanged.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "UpdateInformation",
      "Entity":
      {
        "Type": "ResaleAuthorization@1.0",
        "Identifier": "resaleauthz-123456789"
      },
      "DetailsDocument":
      {
        "Name": "TestResaleAuthorization",
        "Description": "Worldwide ResaleAuthorization for Test Product",
        "PreExistingBuyerAgreement":
        {
          "AcquisitionChannel": "AwsMarketplace",
          "PricingModel": "Contract"
        }
      }
    }
  ]
}
```

Provide information for the fields to add the `UpdateInformation`
change type:

- **Entity** (object) (required) – Your
  Resale Authorization.

  - **Type** (string) (required) –
    The `Type` is always
    `ResaleAuthorization@1.0`.
  - **Identifier** (string) (required)
    – Your Resale Authorization ID. For more information, see
    [Identifier](catalog-apis.md#identifier "catalog-apis.md#identifier").

- **DetailsDocument** (object) (required)
  – Details of the request, including the information you want to
  update information for the Resale Authorization.

  - **Name** (string) (optional) –
    The name associated with the ResaleAuthorization for better
    readability to you and your channel partners.
  - **Description** (string) (optional)
    – The description is free-form text where you can add details
    about the ResaleAuthorization.
  - **PreExistingBuyerAgreement**
    (object) (optional) – Determines if this offer is a renewal
    for an existing agreement with an existing customer for the same
    underlying product. The existing agreement can be within or outside
    AWS Marketplace. AWS may audit and verify your offer is a renewal. If AWS
    is unable to verify your offer, then AWS may revoke the offer and
    entitlements from your customer.

    - **AcquisitionChannel**
      (string) (required) – Indicates if the existing buyer
      agreement was signed outside AWS Marketplace or in AWS Marketplace.

    Possible values: `External`,
    `AwsMarketplace`
    - **PricingModel** (string)
      (required) **–** Indicates
      which pricing model the exiting agreement uses.

    Possible values: `Contract`,
    `Usage`, `BYOL`,
    `Free`

**Response Syntax**

A change set is created for your request. The response to this request gives you
the `ChangeSetId` and `ChangeSetArn` for the change set and
looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating
information to ensure that it meets the AWS Marketplace guidelines. The validation process can
take anywhere from a few minutes to a few hours.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through
Catalog API using the `DescribeChangeSet` API operation.

**Synchronous Validations**

The following schema validations are specific to `UpdateInformation`
actions in the AWS Marketplace Catalog API. These validations are performed when you call
`StartChangeSet`, and the request will fail with an HTTP error if the
input does not meet the following requirements.

| Input field         | Validation rule                                                                                                                                                | HTTP code |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| Name                | Optional<br>Must not be null or empty<br>Length must be between 1 and 100 characters<br>Pattern ^[A-Za-z0-9]\*$<br>No special character or white space allowed | 422       |
| Description         | Optional<br>Length must be between 1 and 255 characters<br>Pattern ^[A-Za-z0-9\\s]\*$<br>No special characters allowed                                         | 422       |
| An unknown property | No additional properties are allowed                                                                                                                           | 422       |

**Asynchronous Errors**

The following errors are specific to `UpdateInformation` actions in the
AWS Marketplace Catalog API. These errors are returned when you call `DescribeChangeSet`
after a change set is processing. or more information about using
`DescribeChangeSet` to get the status of a change request, see [Working with change sets](catalog-apis.md#working-with-change-sets "catalog-apis.md#working-with-change-sets").

| Error code                     | Error message                                                                                                  |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| INCOMPATIBLE\_BUYER\_TARGETING | **`At least one Buyer account must be present for<br>ResaleAuthorization with<br>PreExistingBuyerAgreement.`** |

## Restrict a Resale Authorization

You can use the Catalog API to set restrict rules to a Resale Authorization in
AWS Marketplace.

A restricted Resale Authorization can no longer be used by a channel partner to
create a private offer. An existing private offer won't be impacted.

To restrict your Resale Authorization, call the `StartChangeSet` API
operation with the `RestrictResaleAuthorization` change type, as shown in
the following example.

###### Important

This is a non-reversible operation. After the Resale Authorization is marked
as `Restricted`, it can't be in an `Active` state
again.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "RestrictResaleAuthorization",
      "Entity": {
        "Type": "ResaleAuthorization@1.0",
        "Identifier": "resaleauthz-123456789"
      },
      "DetailsDocument": {}
    }
  ]
}
```

Provide information for the fields to add the
`RestrictResaleAuthorization` change type:

- **Entity** (object) (required) – Your
  Resale Authorization.

  - **Type** (string) (required) –
    The `Type` is always
    `ResaleAuthorization@1.0`.
  - **Identifier** (string) (required)
    – Your Resale Authorization ID. For more information, see
    [Identifier](catalog-apis.md#identifier "catalog-apis.md#identifier").

- **DetailsDocument** (object) (required)
  – Specifics of the request. It must be an empty object for
  `RestrictResaleAuthorization`.

**Response Syntax**

A change set is created for your request. The response to this request gives you
the `ChangeSetId` and `ChangeSetArn` for the change set and
looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating
information to ensure that it meets the AWS Marketplace guidelines. The validation process can
take anywhere from a few minutes to a few hours.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through
Catalog API using the `DescribeChangeSet` API operation.

**Synchronous Validations**

The schema validations are specific to `RestrictResaleAuthorization`
actions in the AWS Marketplace Catalog API. These validations are performed when you
call `StartChangeSet`. If the request doesn't meet the following
requirements, it will fail with an HTTP response.

| Input field                   | Validation rule                                                | HTTP code |
| ----------------------------- | -------------------------------------------------------------- | --------- |
| DetailsDocument               | Must be empty                                                  | 422       |
| `RestrictResaleAuthorization` | Expired ResaleAuthorization can't be marked as<br>`Restricted` | 422       |
| An unknown property           | No additional properties are allowed                           | 422       |

**Asynchronous Errors**

The following errors are specific to `RestrictResaleAuthorization`
actions in the AWS Marketplace Catalog API. These errors are returned when you call
`DescribeChangeSet` after a change set is processing. or more
information about using `DescribeChangeSet` to get the status of a change
request, see [Working with change sets](catalog-apis.md#working-with-change-sets "catalog-apis.md#working-with-change-sets").

| Error code           | Error message                                                       |
| -------------------- | ------------------------------------------------------------------- |
| INCOMPATIBLE\_STATUS | **`Expired ResaleAuthorization can't be marked as<br>restricted.`** |

## Release a Resale Authorization and make it visible to a Channel Partner

You can use the Catalog API to initiate your `ResaleAuthorization` to
an `Active` state.

`ReleaseResaleAuthorization` makes your Resale Authorization active so
that a Channel Partner can use your Resale Authorization to create private
offers.

To release your Resale Authorization, call the `StartChangeSet` API
operation with the `ReleaseResaleAuthorization` change type, as shown in
the following example.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "ReleaseResaleAuthorization",
      "Entity":
      {
        "Type": "ResaleAuthorization@1.0",
        "Identifier": "resaleauthz-123456789"
      },
      "DetailsDocument": {}
    }
  ]
}
```

Provide information for the fields to add the
`ReleaseResaleAuthorization` change type:

- **Entity** (object) (required) – Your
  Resale Authorization.

  - **Type** (string) (required) –
    The `Type` is always
    `ResaleAuthorization@1.0`.
  - **Identifier** (string) (required)
    – Your Resale Authorization ID. For more information, see
    [Identifier](catalog-apis.md#identifier "catalog-apis.md#identifier").

- **DetailsDocument** (object) (required)
  – Specifics of the request. It must be empty for
  `ReleaseResaleAuthorization`.

**Response Syntax**

A change set is created for your request. The response to this request gives you
the `ChangeSetId` and `ChangeSetArn` for the change set and
looks like the following.

```
{
  "ChangeSetId": "example123456789012abcdef",
  "ChangeSetArn": "arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/ChangeSet/example123456789012abcdef"
}
```

The change request is added to a queue and processed. This includes validating
information to ensure that it meets the AWS Marketplace guidelines. The validation process can
take anywhere from a few minutes to a few hours.

You can check the status of the request through the AWS Marketplace Management Portal, or directly through
Catalog API using the `DescribeChangeSet` API operation.

**Synchronous Validations**

The schema validations are specific to `ReleaseResaleAuthorization`
actions in the AWS Marketplace Catalog API. The validations are performed when you call
`StartChangeSet`. If the request doesn't meet the following
requirements, it will fail with an HTTP response.

| Input field         | Validation rule                      | HTTP code |
| ------------------- | ------------------------------------ | --------- |
| An unknown property | No additional properties are allowed | 422       |

**Asynchronous Errors**

The following errors are specific to `ReleaseResaleAuthorization`
actions in the AWS Marketplace Catalog API. These errors are returned when you call
`DescribeChangeSet` after a change set is processing. For more
details about using `DescribeChangeSet` to get the status of a change
request, see [Working with change sets](catalog-apis.md#working-with-change-sets "catalog-apis.md#working-with-change-sets").

| Error code                     | Error message                                                                                                  |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------- |
| MISSING\_MANDATORY\_TERMS      | **`Provide a BuyerLegalTerm.`**                                                                                |
| MISSING\_MANDATORY\_TERMS      | **`Provide a PricingTerm.`**                                                                                   |
| INCOMPATIBLE\_PRODUCT          | **`Use an active product in limited or public<br>state.`**                                                     |
| INCOMPATIBLE\_PRICING\_TERM    | **`PaymentScheduleTerm and FixedUpfrontPricingTerm must<br>be present together.`**                             |
| INCOMPATIBLE\_BUYER\_TARGETING | **`At least one Buyer account must be present for<br>ResaleAuthorization with<br>PreExistingBuyerAgreement.`** |
| MISSING\_MANDATORY\_TERMS      | **`Provide at least one of [x,y,z].`**                                                                         |
| INCOMPATIBLE\_STATUS           | **`[x] request can't be performed after the resale<br>authorization is released.`**                            |

## Describe an existing Resale Authorization

To describe Resale Authorization details, call the `DescribeEntity` API
operation with the `ResaleAuthorization@1.0` entity type, as shown in the
following example.

**Request Syntax**

```
GET /DescribeEntity?catalog=<Catalog>&entityId=<EntityId> HTTP/1.1
```

Provide information for the fields to add the `DescribeEntity` change
type:

- **catalog** (string) – The catalog
  related to the request. Fixed value: `AWSMarketplace`.
- **entityId** (string) – The unique ID
  of the `ResaleAuthorization` to describe.

**Response Syntax**

The response to this request gives you the offer details and looks like the
following.

```
{
  "EntityType": "ResaleAuthorization@1.0",
  "EntityIdentifier": "resaleauthz-123456789",
  "EntityArn": "arn:aws:aws-marketplace:us-east-1:111122223333:AWSMarketplace/ResaleAuthorization/resaleauthz-123456789",
  "LastModifiedDate": "2021-03-10T21:57:16Z",
  "DetailsDocument": {
    "Name": "TestResaleAuthorization",
    "Description": "ResaleAuthorization for Test Product",
    "ProductId": "prod-ad8EXAMPLE51",
    "ProductName": "TestProduct",
    "Status": "Active", /*Draft, Active, Restricted*/
    "PreExistingBuyerAgreement": {
      "AcquisitionChannel": "Unknown",
      "PricingModel": "Unknown"
    },
    "CreatedDate": "2023-07-18T16:39:31.335Z",
    "ManufacturerLegalName": "ChannelCAPI.Inc",
    "ManufacturerAccountId": "123456789012",
    "Dimensions": [
      {
        "Name": "Protected Resources",
        "Description": "Additional 100 protected resources",
        "Key": "hundredresources",
        "Unit": "Units",
        "Types": [
          "Entitled"
        ]
      }
    ],
    "OfferDetails": {
      "OfferExtendedStatus": "Not Started", /* Not Started, Completed-Used, Completed-Usable*/
      "OfferCreatedCount": 0
    },
    "Terms": [
      {
        "Type": "ResaleNetPaymentTerm",
        "Id": "term_id_placeholder",
        "PaymentDuePeriod": "P60D"
      },
      {
        "Type": "ResaleUsageBasedPricingTerm",
        "Id": "term_id_placeholder",
        "CurrencyCode": "USD",
        "RateCards": [
          {
            "RateCard": [
              {
                "DimensionKey": "resource_number",
                "Price": "0.05"
              },
              {
                "DimensionKey": "scanned_data",
                "Price": "0.05"
              }
            ]
          }
        ]
      },
      {
        "Type": "ResaleConfigurableUpfrontPricingTerm",
        "Id": "term_id_placeholder",
        "CurrencyCode": "USD",
        "RateCards": [
          {
            "Selector": {
              "Type": "Duration",
              "Value": "P24M"
            },
            "RateCard": [
              {
                "DimensionKey": "hundredresources",
                "Price": "0.04"
              },
              {
                "DimensionKey": "tenTBData",
                "Price": "0.03"
              },
              {
                "DimensionKey": "channel_custom",
                "Price": "0.02"
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
        "Type": "ResaleFixedUpfrontPricingTerm",
        "Id": "term-sdh27fb2",
        "CurrencyCode": "USD",
        "Duration": "P180D",
        "Price": "0.0",
        "Grants": [
          {
            "DimensionKey": "sdf73rbns93nl120d10xm1",
            "MaxQuantity": 1
          }
        ]
      },
      {
        "Type": "ResalePaymentScheduleTerm",
        "Id": "term-sdh27fb2",
        "CurrencyCode": "USD",
        "Schedule": [
          {
            "ChargeDate": "2018-07-01T00:00:00.000Z",
            "ChargeAmount": "200.00"
          },
          {
            "ChargeDate": "2019-05-01T00:00:00.000Z",
            "ChargeAmount": "200.00"
          }
        ]
      },
      {
        "Type": "BuyerLegalTerm",
        "Id": "term_id_placeholder",
        "Documents": [
          {
            "Type": "StandardEula",
            "Url": "https://resale-auth-legal-terms-iad-beta.s3.us-east-1.amazonaws.com/09ae57d6-c75a-3a4c-aadf-9b866bae64ab/a85cace8-6d9d-40ca-a053-78fc265479bf?isSigned=yes"
          }
        ]
      },
      {
        "Type": "ResaleLegalTerm",
        "Id": "term_id_placeholder",
        "Documents": [
          {
            "Type": "StandardResellerContract",
            "Url": "https://resale-auth-legal-terms-iad-beta.s3.us-east-1.amazonaws.com/09ae57d6-c75a-3a4c-aadf-9b866bae64ab/bed55b56-7ab4-4c4c-b633-3bf4f6efcb98?isSigned=yes"
          }
        ]
      },
      {
        "Type": "BuyerValidityTerm",
        "Id": "term_id_placeholder",
        "MaximumAgreementStartDate": "2023-09-25T23:59:59.000Z"
      },
      {
        "Type": "BuyerTargetingTerm",
        "Id": "term_id_placeholder",
        "PositiveTargeting": {
          "BuyerAccounts": [
            {
              "AwsAccountId": "444455556666"
            }
          ]
        }
      }
    ],
    "Rules": [
      {
        "Type": "AvailabilityRule",
        "Id": "availability_rule_id_placeholder",
        /* If the AvailabilityEndDate and OffersMaxQuantity not present Usage will be Unlimited*/
        "Usage": "Limited",
        "AvailabilityEndDate": "2022-05-31T23:59:59Z",
        "OffersMaxQuantity": 1
      },
      {
        "Type": "PartnerTargetingRule",
        "Id": "partner_targeting_rule_id_placeholder",
        "ResellerAccountId": "777777777777",
        "ResellerLegalName": "ChannelCAPICP.Inc"
      }
    ]
  }
}
```

The following is information about the fields you see in the
`DescribeEntity` response.

- **EntityType** (string) – The named
  type of the entity, which is ResaleAuthorization@1.0.
- **EntityIdentifier** (string) – The
  identifier of the entity, in the format of EntityId@RevisionId.
- **EntityArn** (string) – The ARN
  associated to the unique identifier for the change set referenced in this
  request.
- **LastModifiedDate** (string) – The
  last modified date of the entity, in ISO 8601 format
  (2018-02-27T13:45:22Z).
- **DetailsDocument** (object) (required)
  – This JSON string includes the details of the entity.

  - **Name** (string) – Name
    associated with the ResaleAuthorization for better readability to
    you and your Channel Partners. It's displayed as part of the
    Agreement information.
  - **Description** (string) –
    Description is a free-form text which is meant to be used only by
    you and will never be exposed to buyers.
  - **ProductId** (string) –
    Description is a free-form text which is meant to be used only by
    you and will never be exposed to buyers.
  - **AgreementToken** (string) –
    Generated from content in ResaleAuthorization. It contains
    information about terms, rules, and proposer while creating an
    agreement. It's used for authorization checks and validations during
    procurement.
  - **Terms** (array of structures)
    – List of terms presented for acceptance.
  - **Rules** (array of structures)
    – List of rules or set of instructions.
