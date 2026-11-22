

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Working with products integrated with AWS Services

You can use the AWS Marketplace Catalog API to create and manage RTB Fabric module products. These products use the generic `Product@1.0` entity. The delivery option that you add to the product identifies it as an RTB Fabric module product. You add the delivery option with the `AddDeliveryOption` change type.

You create these products in AWS Partner Central or with the AWS Marketplace Catalog API. When you use the Catalog API, you work in the US East (N. Virginia) Region and the `AWSMarketplace` catalog, the same as other AWS Marketplace product types.

For the seller-facing concepts, pricing model, and fulfillment steps for RTB Fabric module products, see [Products Integrated with AWS Services in AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/userguide/additional-product-types.html) in the *AWS Marketplace Seller Guide*.

The delivery option type string for an RTB Fabric module product is `rtb-module`. You can't change the type after you create the product.

**Topics**
+ [Order of operations for a first listing](#work-with-additional-product-types-order-of-operations)
+ [Delivery option](#work-with-additional-product-types-delivery)
+ [Pricing and offer change types](#work-with-additional-product-types-pricing)
+ [Checking entitlements](#work-with-additional-product-types-metering)

## Order of operations for a first listing
<a name="work-with-additional-product-types-order-of-operations"></a>

To create a first listing for an RTB Fabric module product, you submit one change set that creates the product, sets its details, adds a delivery option, and adds pricing dimensions. You then release the product, set targeting, and create and release an offer.

You submit the create steps in a single change set with the following change types, in order:

1. [CreateProduct](work-with-seller-products.md#create-product) – Creates the `Product@1.0` entity in the `Draft` state.

1. [UpdateInformation](work-with-seller-products.md#update-information) – Sets the product title, description, and other product details.

1. `AddDeliveryOption` – Adds the delivery option that identifies the product as an RTB Fabric module product. The delivery option type string is `rtb-module`.

1. [AddDimensions](work-with-seller-products.md#add-dimensions) – Adds the pricing dimensions. Use the `Entitled` dimension type for contract pricing.

The following example shows the single change set. Each change type uses the generic `Product@1.0` entity type.
+ The dimension `Types` value is `Entitled` for contract pricing.
+ `Categories` must match the AWS Marketplace category names exactly, or the change fails with `INVALID_CATEGORY_NAMES`.

```json
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet": [
    {
      "ChangeType": "CreateProduct",
      "ChangeName": "CreateProduct",
      "Entity": { "Type": "Product@1.0" },
      "DetailsDocument": {}
    },
    {
      "ChangeType": "UpdateInformation",
      "Entity": { "Type": "Product@1.0", "Identifier": "{{$CreateProduct.Entity.Identifier}}" },
      "DetailsDocument": {
        "ProductTitle": "{{Example product title}}",
        "ShortDescription": "{{A short description of the product}}",
        "LongDescription": "{{A longer description of the product}}",
        "Highlights": ["{{First highlight}}", "{{Second highlight}}"],
        "SearchKeywords": ["{{keyword1}}", "{{keyword2}}"],
        "Categories": ["{{Security}}"],
        "LogoUrl": "{{https://example-bucket.s3.amazonaws.com/logo.png}}",
        "SupportDescription": "{{How buyers reach your support team}}"
      }
    },
    {
      "ChangeType": "AddDeliveryOption",
      "Entity": { "Type": "Product@1.0", "Identifier": "{{$CreateProduct.Entity.Identifier}}" },
      "DetailsDocument": {
        "DeliveryOptions": [
          {
            "Details": {
              "DeliveryOptionDetails": {
                "Type": "rtb-module",
                "UsageInstructions": "Instructions shown to the buyer after purchase"
              }
            }
          }
        ]
      }
    },
    {
      "ChangeType": "AddDimensions",
      "Entity": { "Type": "Product@1.0", "Identifier": "{{$CreateProduct.Entity.Identifier}}" },
      "DetailsDocument": [
        {
          "Key": "module_access",
          "Name": "{{Example dimension}}",
          "Description": "{{Description of the dimension}}",
          "Unit": "Units",
          "Types": ["Entitled"]
        }
      ]
    }
  ]
}
```

After the change set completes, the product is in the `Draft` state. You then complete the listing with the following steps:

1. Associate your module in the AWS RTB Fabric console. You can't move the product to the `Public` state until RTB Fabric confirms to AWS Marketplace that the association is complete. For the delivery steps, see [Delivery option](#work-with-additional-product-types-delivery).

1. Call the [ReleaseProduct](work-with-seller-products.md#release-product) change type to validate and publish the product.

1. Call the [UpdateTargeting](work-with-seller-products.md#update-targeting) change type to set the AWS accounts that can view the product while it is in the `Limited` state.

1. Create and release a public offer. For more information, see [Pricing and offer change types](#work-with-additional-product-types-pricing).

The `start-change-set` command returns a `ChangeSetId` value. To monitor a change set, see [Monitoring a change set](work-with-ec2-image-builder-products.md#monitor-changeset).

## Delivery option
<a name="work-with-additional-product-types-delivery"></a>

You add a delivery option with the `AddDeliveryOption` change type, with the type string `rtb-module`. You associate your module with the product in the AWS RTB Fabric console in the US East (N. Virginia) Region. You can't move the product to the `Public` state until RTB Fabric confirms the association. After a buyer subscribes, the buyer deploys your module in the RTB Fabric console.

## Pricing and offer change types
<a name="work-with-additional-product-types-pricing"></a>

You set pricing on the offer, not on the product. RTB Fabric module products support contract pricing. With contract pricing, buyers choose the quantity of each dimension and a contract duration of 1, 12, 24, or 36 months. For the pricing model, see [Products Integrated with AWS Services in AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/userguide/additional-product-types.html) in the *AWS Marketplace Seller Guide*.

You create the offer with the [CreateOffer](work-with-private-offers.md#create-offer) change type, set pricing with the `UpdatePricingTerms` change type, and then publish the offer with the [ReleaseOffer](work-with-private-offers.md#release-offer) change type. The offer change types are the same as for other AWS Marketplace product types. The pricing terms that you use are:
+ `ConfigurableUpfrontPricingTerm` – Use for contract pricing, with `Entitled` dimensions.
+ `FreeTrialPricingTerm` – Use to offer a free trial.

The following offer rules apply to RTB Fabric module products:
+ A public contract offer must include a renewal term (`UpdateRenewalTerms`).
+ A product can carry one paid public offer plus a free-trial offer.
+ `UpdateSupportTerms` is available for public offers only.

You can also set the `UpdateLegalTerms` and `UpdateRenewalTerms` change types on the offer. For the full offer and pricing workflow, the request syntax, and the field descriptions for each of these change types, see [Work with offers using the AWS Marketplace APIs](work-with-offers.md).

## Checking entitlements
<a name="work-with-additional-product-types-metering"></a>

RTB Fabric module products use contract pricing only and aren't metered. AWS RTB Fabric checks the buyer's entitlement, so you don't call the AWS Marketplace Metering Service. You can optionally call the AWS Marketplace Entitlement Service `GetEntitlements` operation to retrieve the purchased quantity.

### Check entitlements with GetEntitlements
<a name="work-with-additional-product-types-getentitlements"></a>

AWS RTB Fabric verifies the buyer's entitlement before the module runs. If your systems enforce the purchased quantity, retrieve it with the AWS Marketplace Entitlement Service `GetEntitlements` operation.

The following Python example verifies that a customer has an active entitlement and returns the purchased quantity.

```python
# Import AWS Python SDK
import boto3
from botocore.exceptions import ClientError

client = boto3.client("marketplace-entitlement")

# The product code is available from describe-entity as soon as you
# release the product to the Limited state with ReleaseProduct.
try:
    response = client.get_entitlements(ProductCode="{{product-code}}")
    # TODO: Verify the dimension a customer is subscribed to and the quantity,
    # if applicable
except ClientError as error:
    # If the request is throttled (ThrottlingException), retry the call
    # with exponential backoff and jitter.
    print(error)
    raise
```

For more information about `GetEntitlements`, see [GetEntitlements](https://docs.aws.amazon.com/marketplaceentitlement/latest/APIReference/API_GetEntitlements.html) in the *AWS Marketplace Entitlement Service API Reference*.