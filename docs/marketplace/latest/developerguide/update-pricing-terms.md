The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Update pricing terms

You can use the Catalog API to update the pricing of your machine learning products in AWS Marketplace.

###### Note

You must price all supported instance types of your machine learning products.
When creating your first version, the `UpdatePricingTerms` and
`AddDeliveryOptions` change types with prices for
all supported instances types in order to publish your product.
When adding a new version to an existing product with new instance types that
were not supported before, you must include those instance types in the `UpdatePricingTerms` and
`AddDeliveryOptions` change types.

To update pricing terms, call the `StartChangeSet` operation
with the `UpdatePricingTerms` change type.

## Request syntax

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
                "Identifier": "$CreateOfferChange.Entity.Identifier"
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
                                      "DimensionKey": "ml.m4.4xlarge.m.i.b",
                                      "Price": 0.1
                                    },
                                    {
                                      "DimensionKey": "ml.m5.4xlarge.m.i.b",
                                      "Price": 0.1
                                    },
                                    {
                                      "DimensionKey": "ml.m4.16xlarge.m.i.b",
                                      "Price": 0.1
                                    },
                                    {
                                      "DimensionKey": "m.i.c",
                                      "Price": 0.1
                                    },
                                    {
                                      "DimensionKey": "ml.m4.4xlarge.a.t",
                                      "Price": 0.1
                                    },
                                    {
                                      "DimensionKey": "ml.m5.4xlarge.a.t",
                                      "Price": 0.1
                                    },
                                    {
                                      "DimensionKey": "ml.m4.16xlarge.a.t",
                                      "Price": 0.1
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "Type": "FreeTrialPricingTerm",
                        "Duration": "P30D",
                        "Grants": [
                            {
                                "DimensionKey": "ml.m4.4xlarge.m.i.b"
                            },
                              {
                                "DimensionKey": "ml.m5.4xlarge.m.i.b"
                              },
                              {
                                "DimensionKey": "ml.m4.16xlarge.m.i.b"
                              },
                              {
                                "DimensionKey": "m.i.c"
                              },
                              {
                                "DimensionKey": "ml.m4.4xlarge.a.t"
                              },
                              {
                                "DimensionKey": "ml.m5.4xlarge.a.t"
                              },
                              {
                                "DimensionKey": "ml.m4.16xlarge.a.t"
                              }
                        ]
                    }
                ]
            }
        },
    ]
}
```

## Required fields

- `Entity` (object) (required) - Contains information about the offer of your ML product.

  - `Identifier` (string) (required) – The offer id for which you would like to update pricing terms. For more information, see [Identifier](../APIReference/catalog-apis.md#identifier "../APIReference/catalog-apis.md#identifier").
  - `Type` (string) (required) – The `Type` must be `Offer@1.0` for updating pricing.

- `DetailsDocument` (object) (required) – Details about the pricing terms of your machine learning product.

  - `PricingModel` (string) (required) - The pricing model for your product - you can choose between Usage, Free, and Contract (for private offers). For more information, see [Machine Learning Product Pricing](../userguide/machine-learning-pricing.md "../userguide/machine-learning-pricing.md").
  - `Terms` (array of objects) - An array of pricing terms that collectively define the overall pricing of your product.

    - `Type` (string) (required) - The type of pricing term. Valid options are `UsageBasedPricingTerm` or `FreeTrialPricingTerm` or `FixedUpfrontPricingTerm` (for private offers).
    - `CurrencyCode` (string) (required for `UsageBasedPricingTerm` or `FixedUpfrontPricingTerm` - the currency of the pricing term. Valid values are `USD`.
    - `RateCards` (array of objects) (required for `UsageBasedPricingTerm`) - The rate cards that define the pricing for your machine learning product. You must include one `RateCard` only within this array.

      - `RateCard` (array of objects) - The array of dimensions and rates for your machine learning product. All supported instance types must be priced in order to publish your product.

        - `DimensionKey` - The dimension you are pricing. Valid dimension keys are:

          - Instance type followed by the operation for hourly rates:

            - Instance type will start with `ml` followed by the instance name and size.
              For exampole, `ml.m4.xlarge`
            - Operation will be `m.i.b` for batch transform, `m.i.r`
              for hourly real-time inference, and `a.t` for algorithm training.
            - Examples: `ml.m4.4xlarge.m.i.b` for batch transform, `ml.m4.xlarge.m.i.r`
              for real-time inference, or `ml.m4.16xlarge.a.t` for algorithm training

          - `m.i.c` for real-time per inference pricing.

        - `Price` - The rate of the dimension. The rate is either hourly or per-inference,
          depending on the dimensionKey.

    - `Duration` (string) (required for `FreeTrialPricingTerm` or `FixedUpfrontPricingTerm` -
      The duration of your free trial or contract. For free trial valid values are between X and Y. For contract,
      valid values are between X and Y.
    - Grants (array of objects) - Details about which dimensionKeys are eligible for free trial.
      All supported dimensionKeys must be provided.

      - DimensionKey - The dimension to include as part of the free trial offer.

        - Instance type followed by the operation for hourly rates:

          - Instance type starts with `ml` followed by the instance name and size e.g. `ml.m4.xlarge`
          - Operation is `m.i.b` for batch transform, `m.i.r` for hourly real-time inference,
            or `a.t` for algorithm training.
          - Examples: `ml.m4.4xlarge.m.i.b` for batch transform,
            `ml.m4.xlarge.m.i.r` for real-time inference, or
            `ml.m4.16xlarge.a.t` for algorithm training

        - `m.i.c` for real-time per inference pricing.

## Response syntax

A successful request returns:

```
{
    "ChangeSetId": "`example123456789012abcdef`",
    "ChangeSetArn": "arn:aws:aws-marketplace:`us-east-1`:`123456789012`:AWSMarketplace/ChangeSet/`example123456789012abcdef`"
}
```

## Change set processing

The change request enters a processing queue, where it undergoes several steps:

1. Validation: The system checks to ensure all information meets AWS Marketplace guidelines.

   - Processing time: Few minutes to several hours
   - For validation errors, see [Change set status and errors](../APIReference/work-with-seller-products.md#seller-product-change-set-errors "../APIReference/work-with-seller-products.md#seller-product-change-set-errors").

2. Status monitoring: You can check the status of the request two ways.

   - Via AWS Marketplace Management Portal
   - Using the `DescribeChangeSet` operation

3. Completion: When approved, the pricing terms are updated.

## Errors

###### Asynchronous errors

Specific errors for `UpdatePricingTerms`
actions can be retrieved using the `DescribeChangeSet`
operation after the change set begins processing. For error details and
troubleshooting, see
[Change set status and errors](../APIReference/catalog-apis.md#working-with-change-sets "../APIReference/catalog-apis.md#working-with-change-sets").

| Error code                  | Error message                              |
| --------------------------- | ------------------------------------------ |
| INCOMPATIBLE_PRODUCT_STATUS | Use an existing limited or public product. |
