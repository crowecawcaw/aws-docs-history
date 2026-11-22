

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Configuring purchase order number requirement settings

With purchase order number requirement settings, you can require buyers to enter a purchase order number before they subscribe to products in AWS Marketplace, for specific offer types and pricing types. You can also display a custom message that explains your organization's procurement requirements to buyers on the procurement page. Before you configure these settings, complete [Prerequisites for buying policies](work-with-buying-policies.md#buying-policies-api-prerequisites).

## Configuring mandatory purchase orders
<a name="buying-policies-api-mandatory-po"></a>

Mandatory purchase orders are configured as a `ProcurementPolicy` entity with the `PolicyType` of `PURCHASE_ORDER_POLICY`. When mandatory purchase orders are enabled, users can't complete a subscription that matches the configured offer types and pricing types without entering a purchase order number.

**Create the mandatory purchase order policy**  
Call `StartChangeSet` with the `CreateProcurementPolicy` change type and the `PolicyType` of `PURCHASE_ORDER_POLICY`. Specify the experience that the policy applies to as the `Entity`.

```json
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "CreateProcurementPolicy",
      "DetailsDocument":
      {
        "Name": "ExamplePurchaseOrderPolicy",
        "PolicyType": "PURCHASE_ORDER_POLICY"
      },
      "Entity":
      {
        "Type": "Experience@1.0",
        "Identifier": "exp-1234example"
      }
    }
  ]
}
```

Use `DescribeChangeSet` with the returned `ChangeSetId` to track the request and get the identifier of the new `ProcurementPolicy` entity.

**Choose the offer types and pricing types**  
Call `StartChangeSet` with the `UpdateProcurementPolicy` change type on the `ProcurementPolicy` entity. In `MandatoryPurchaseOrderConfig`, list the `AgreementTerms` that require a purchase order separately for public offers (`PublicOffer`) and private offers (`PrivateOffer`). The following table maps each agreement term type to the pricing type shown to buyers.


| Agreement term type | Pricing type shown to buyers | Public offer | Private offer | 
| --- | --- | --- | --- | 
| `ConfigurableUpfrontPricingTerm` | Contract pricing with upfront payment | Yes | Yes | 
| `FixedUpfrontPricingTerm` | Contract pricing with upfront payment | Yes | Yes | 
| `UsageBasedPricingTerm` | Usage-based pricing (pay-as-you-go) | Yes | Yes | 
| `RecurringPaymentTerm` | Recurring pricing (fixed monthly charges) | Yes | Yes | 
| `VariablePaymentTerm` | Variable pricing (charges on completion or milestones) | No | Yes | 
| `PaymentScheduleTerm` | Contract pricing with flexible payment schedule | No | Yes | 

The following example makes a purchase order mandatory for all public and private offers with the listed term types.

```json
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "UpdateProcurementPolicy",
      "DetailsDocument":
      {
        "MandatoryPurchaseOrderConfig":
        {
          "PublicOffer":
          {
            "AgreementTerms":
            [
              "FixedUpfrontPricingTerm",
              "UsageBasedPricingTerm",
              "RecurringPaymentTerm"
            ]
          },
          "PrivateOffer":
          {
            "AgreementTerms":
            [
              "ConfigurableUpfrontPricingTerm",
              "FixedUpfrontPricingTerm",
              "UsageBasedPricingTerm",
              "RecurringPaymentTerm",
              "VariablePaymentTerm",
              "PaymentScheduleTerm"
            ]
          }
        }
      },
      "Entity":
      {
        "Type": "ProcurementPolicy@2.0",
        "Identifier": "procpolicy-1234example"
      }
    }
  ]
}
```

**Note**  
If you require purchase orders for pay-as-you-go public offers, buyers can't subscribe through service consoles such as Amazon EC2, because those consoles don't support purchase orders. Mandatory purchase order settings don't apply to Amazon Bedrock serverless purchases made through the Amazon Bedrock console.

Configuration changes take a few hours to apply to all users in your organization.

## Configuring custom procurement messaging
<a name="buying-policies-api-procurement-message"></a>

The procurement administrator message is displayed to buyers on the procurement page in AWS Marketplace. Use it to explain your purchase order number format, link to your procurement policy, or tell buyers whom to contact. In the API, the message is the `ProcurementMessage` field (up to 1,000 characters) in the `Configuration` of the experience's `BrandingSettings`. Buyers see a notice that the message comes from your organization and not from AWS.

To add or change the message, call `StartChangeSet` with the `UpdateBrandingSettings` change type.

```json
POST /StartChangeSet HTTP/1.1
Content-type: application/json

{
  "Catalog": "AWSMarketplace",
  "ChangeSet":
  [
    {
      "ChangeType": "UpdateBrandingSettings",
      "DetailsDocument":
      {
        "Name": "ExampleBrandingSettingsName",
        "Configuration":
        {
          "ProcurementMessage": "Contact procurement@example.com for a purchase order."
        }
      },
      "Entity":
      {
        "Type": "Experience@1.0",
        "Identifier": "exp-1234example"
      }
    }
  ]
}
```

## Errors for purchase order number requirement settings
<a name="purchase-order-requirement-error-codes"></a>

The following errors can occur when you configure mandatory purchase orders or the custom procurement message. They're returned in `ErrorDetailList` when you call `DescribeChangeSet` on a failed change set. For errors that apply to all private marketplace change types, see [Errors in the private marketplace API](work-with-private-marketplace.md#private-marketplace-error-codes).


| Change type | Error code | Error message | Description | 
| --- | --- | --- | --- | 
| CreateProcurementPolicy | ENTITY\_ALREADY\_EXISTS | *[Entity]* exists for *[Experience]* | The experience already has a `PURCHASE_ORDER_POLICY`. An experience can have one policy of each type. Update the existing policy instead. | 
| CreateProcurementPolicy, UpdateProcurementPolicy, UpdateBrandingSettings | ENTITY\_NOT\_FOUND | *[Entity]* missing from Experience | The experience or policy that you specified doesn't exist. Use `ListEntities` to find the identifier. | 
| CreateProcurementPolicy, UpdateProcurementPolicy | INVALID\_OPERATION | Only *[PolicyType]* policy type is supported for this change | The change doesn't match the policy type. For example, `MandatoryPurchaseOrderConfig` is valid only on a `PURCHASE_ORDER_POLICY`. | 