

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Work with professional services products using the AWS Marketplace APIs
<a name="work-with-professional-services-products"></a>

You can use the AWS Marketplace Catalog API to create and manage professional services products. Professional services products use the `ProfessionalServicesProduct@1.0` entity type. The request syntax that all product types share is described in [Work with seller products](work-with-seller-products.md). The following topics describe what applies only to professional services products.

**Topics**
+ [Supported change types](#proserv-supported-change-types)
+ [Create and publish a professional services product](#proserv-create-product)
+ [Create offers for professional services products](#proserv-offers)

## Supported change types
<a name="proserv-supported-change-types"></a>

You can use the following change types with the `ProfessionalServicesProduct@1.0` entity type.


| Change type | More information | 
| --- | --- | 
| CreateProduct | [Create a product](work-with-seller-products.md#create-product) | 
| UpdateInformation | [Update product details](work-with-seller-products.md#update-information) | 
| AddDimensions | [Add pricing dimensions](work-with-seller-products.md#add-dimensions) | 
| UpdateDimensions | [Update pricing dimensions](work-with-seller-products.md#update-dimensions) | 
| UpdateTargeting | [Update targeting configuration](work-with-seller-products.md#update-targeting) | 
| ReleaseProduct | [Publish a product](work-with-seller-products.md#release-product) | 
| UpdateVisibility | [Update product visibility](work-with-seller-products.md#update-visibility) | 

To list your professional services products, call `ListEntities` with the `EntityType` **ProfessionalServicesProduct**. To get the details of one product, call `DescribeEntity` with its product ID. The `EntityTypeFilters` and `EntityTypeSort` parameters of `ListEntities` have no options for professional services products.

## Create and publish a professional services product
<a name="proserv-create-product"></a>

To create a professional services product, call `StartChangeSet` with the `CreateProduct` change type. You can add the product details and pricing dimensions in the same change set. You can publish the product in that change set or in a later one. The following example creates a product, adds its details and one pricing dimension, and publishes it into `Limited` state.

**Request Syntax**

```
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "CreateProduct",
      "ChangeName": "CreateProductChange",
      "Entity": {
        "Type": "ProfessionalServicesProduct@1.0"
      },
      "DetailsDocument": {}
    },
    {
      "ChangeType": "UpdateInformation",
      "Entity": {
        "Type": "ProfessionalServicesProduct@1.0",
        "Identifier": "$CreateProductChange.Entity.Identifier"
      },
      "DetailsDocument": {
        "ProductTitle": "{{Cloud migration assessment}}",
        "ShortDescription": "{{A two-week assessment of your workloads for migration to AWS.}}",
        "LongDescription": "{{Our team reviews your applications and infrastructure and delivers a migration plan.}}",
        "LogoUrl": "https://{{amzn-s3-demo-bucket}}.s3.amazonaws.com/{{logo.png}}",
        "SupportDescription": "{{Contact us by email during business hours.}}",
        "Highlights": ["{{Fixed-scope assessment}}"],
        "SearchKeywords": ["{{migration}}", "{{assessment}}"],
        "Categories": ["Professional Services"]
      }
    },
    {
      "ChangeType": "AddDimensions",
      "Entity": {
        "Type": "ProfessionalServicesProduct@1.0",
        "Identifier": "$CreateProductChange.Entity.Identifier"
      },
      "DetailsDocument": [
        {
          "Key": "{{MigrationAssessment}}",
          "Name": "{{Migration assessment}}",
          "Description": "{{Fixed-scope migration assessment}}",
          "Types": ["Entitled"],
          "Unit": "Units"
        }
      ]
    },
    {
      "ChangeType": "ReleaseProduct",
      "Entity": {
        "Type": "ProfessionalServicesProduct@1.0",
        "Identifier": "$CreateProductChange.Entity.Identifier"
      },
      "DetailsDocument": {}
    }
  ]
}
```

The following rules apply to professional services products:
+ **Permissions** – If your IAM policy limits change types with the `catalog:ChangeType` condition key, it must allow `UpdateInformation`, `AddDimensions`, and `ReleaseProduct` as well as `CreateProduct`. Without them, a `CreateProduct` request for a professional services product is denied, even when the change set contains only `CreateProduct`. For more information, see [Access control for the AWS Marketplace Catalog API](catalog-api-access-control.md).
+ **Product details** – `UpdateInformation` accepts the same fields as for other product types, except `VideoUrls`. Omit `VideoUrls` or set it to `null`.
+ **Pricing dimensions** – Professional services products use contract pricing. Set `Types` to `["Entitled"]` for every dimension. For the allowed units and other fields, see [Add pricing dimensions](work-with-seller-products.md#add-dimensions).
+ **Publishing** – `ReleaseProduct` requires at least one pricing dimension. You don't need a public offer to publish a professional services product. After the product is in `Limited` state, use `UpdateTargeting` to choose the AWS accounts that can view it.

## Create offers for professional services products
<a name="proserv-offers"></a>

You create offers for professional services products with the same change types as for other products. For more information, see [Work with private offers using the AWS Marketplace APIs](work-with-private-offers.md). The following rules apply to offers for professional services products:
+ Every offer must be private. Use the `UpdateTargeting` change type on the offer to set `PositiveTargeting` with the buyer's `BuyerAccounts`.
+ The pricing terms in `UpdatePricingTerms` must match one of these combinations:
  + **Upfront payment** – A `ConfigurableUpfrontPricingTerm`.
  + **Payment schedule** (called *installment plan* in the AWS Marketplace Management Portal) – A `FixedUpfrontPricingTerm` with a `PaymentScheduleTerm`. The `FixedUpfrontPricingTerm` can include only one dimension.
  + **Variable payments** – A `VariablePaymentTerm` with no other pricing term. For more information, see [Add variable payments to an offer](#proserv-variable-payment-term).
+ You can also include a `LegalTerm`, `ValidityTerm`, `NetPaymentTerm`, and `RenewalTerm`. Offers with a `PaymentScheduleTerm` or a `VariablePaymentTerm` require a `ValidityTerm`.
+ Legal documents in the `LegalTerm` must use the `CustomEula` type.

### Add variable payments to an offer
<a name="proserv-variable-payment-term"></a>

With a `VariablePaymentTerm`, you set the maximum amount that the buyer agrees to pay over the agreement. After the buyer accepts the offer, you send payment requests up to that amount with the [`SendAgreementPaymentRequest`](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_SendAgreementPaymentRequest.html) operation. For the console steps, see [Pricing professional service products](https://docs.aws.amazon.com/marketplace/latest/userguide/proserv-variable-payments.html) in the *AWS Marketplace Seller Guide*.

To add variable payments to a draft offer, call `StartChangeSet` with the `UpdatePricingTerms` change type and set `PricingModel` to `Contract`, as shown in the following example.

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
        "Identifier": "{{offer-123456789}}"
      },
      "DetailsDocument": {
        "PricingModel": "Contract",
        "Terms": [
          {
            "Type": "VariablePaymentTerm",
            "CurrencyCode": "{{USD}}",
            "MaxTotalChargeAmount": "{{50000.00}}"
          }
        ]
      }
    }
  ]
}
```

Provide information for the following fields:
+ `PricingModel` (string) (required) – Must be `Contract` when the offer includes a `VariablePaymentTerm`.
+ `Type` (string) (required) – Object value: `VariablePaymentTerm`.
+ `CurrencyCode` (string) (required) – The currency of `MaxTotalChargeAmount`. You can use any currency that AWS Marketplace supports. For the list, see [Supported currencies](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-paying-for-products.html#supported-currencies) in the *AWS Marketplace Buyer Guide*.
+ `MaxTotalChargeAmount` (string) (required) – The maximum total amount that you can request from the buyer over the agreement. Use a non-negative decimal with up to 3 decimal places.

The example sets only the pricing term. An offer with a `VariablePaymentTerm` also needs a `ValidityTerm` that sets the agreement duration. Add it with the `UpdateValidityTerms` change type, as described in [Define the expiration date of agreements created using the offer](work-with-private-offers.md#update-validity-terms).