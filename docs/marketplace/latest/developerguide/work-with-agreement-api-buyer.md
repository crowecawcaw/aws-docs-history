The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Work with the Agreement API as a buyer

An agreement is a document that binds two parties, including the proposer and the acceptor (commonly, the buyer) and defines
the terms and conditions applicable between them.

Buyer creates an AgreementRequest, which generates a quote. This quote includes all
relevant information, such as the estimated charges that will be incurred over the lifetime of the
agreement, which is critical for the buyer's purchase decision. If the buyer is
satisfied with the quote, they can accept the AgreementRequest before it expires. The
Agreement is created upon acceptance of the AgreementRequest. During
this process, the buyer admin or buyer persona can associate purchase order to charges.
Finally, based on the terms and conditions of the active agreement, the buyer is
invoiced and granted a License to use the product.

## Prerequisites: Discover products and offers

Before creating an agreement, use the AWS Marketplace Discovery API to discover the product and obtain the
`agreementProposalId`, `pricingModel`, and term details needed to construct a
`CreateAgreementRequest`.

| Step | Discovery API action                                                                                                                                       | Output                                | Used for                                   |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- | ------------------------------------------ |
| 1    | [ListPurchaseOptions](../APIReference/API_marketplace-discovery_ListPurchaseOptions.md "../APIReference/API_marketplace-discovery_ListPurchaseOptions.md") | `offerId`                             | Finding available offers for a product     |
| 2    | [GetOffer](../APIReference/API_marketplace-discovery_GetOffer.md "../APIReference/API_marketplace-discovery_GetOffer.md")                                  | `agreementProposalId`, `pricingModel` | Constructing `agreementProposalIdentifier` |
| 3    | [GetOfferTerms](../APIReference/API_marketplace-discovery_GetOfferTerms.md "../APIReference/API_marketplace-discovery_GetOfferTerms.md")                   | Term IDs and pricing details          | Constructing `requestedTerms`              |

For detailed information about discovering products and pricing, see
[Discover products and pricing](work-with-catalog-to-discover-products.md "work-with-catalog-to-discover-products.md").

An acceptor can perform the following tasks using this API:

| Task                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Action(s)                                                  | Intent  |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ------- |
| [Generate a quote](#buyer-generate-quote "#buyer-generate-quote")                         | Acceptor can generate quote that includes all relevant information,<br>such as the Charges that will be incurred over the lifetime of the<br>agreement, which is critical for the buyer's purchase<br>decision.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `CreateAgreementRequest`                                   | NEW     |
| [Accept an offer](#buyer-accept-offer "#buyer-accept-offer")                              | The Acceptor can accept terms proposed by the proposer that creates a<br>new agreement. This acceptance can involve passing parameters for<br>certain terms, such as selecting the quantity or duration, adding<br>purchase order etc. Acceptor can also create a new agreement where the<br>product usage begins at a future date. The agreement sign date will be<br>when the offer is accepted and when the agreement is created. The<br>Agreement start date is future date when the product usage begins. This<br>is the date when license/entitlement gets activated. To retrieve the latest status of your usage entitlement, refer to the<br>[GetAgreementEntitlements](../APIReference/API_marketplace-agreements_GetAgreementEntitlements.md "../APIReference/API_marketplace-agreements_GetAgreementEntitlements.md") API. | `CreateAgreementRequest`,<br>`AcceptAgreementRequest`      | NEW     |
| [Replace an existing agreement](#buyer-replace-agreement "#buyer-replace-agreement")      | The Acceptor can perform a mid-term upgrade on their agreement to<br>either switch to more favorable terms or switch seller for their<br>agreements. This action terminates the existing Agreement passed as<br>input and creates net new Agreement. This action is logically equivalent<br>to a CANCEL followed by a NEW agreement, but ensures entitlement<br>continuity for the Acceptor and at no point is the Acceptor left without<br>entitlements.                                                                                                                                                                                                                                                                                                                                                                             | `CreateAgreementRequest`,<br>`AcceptAgreementRequest`      | REPLACE |
| [Amend an existing agreement](#buyer-amend-agreement "#buyer-amend-agreement")            | The acceptor is only permitted to modify the configuration for the<br>accepted terms. For example, they can enable or disable auto-renewal, or<br>modify the purchased quantity, as long as the price change<br>post-modification does not result in refunds. We will only support<br>amending charge if agreement has not started. **Note:*<br>• Proposer is allowed to modify prices for<br>pay-as-you-go pricing term. Any increase in pay as you go prices takes<br>90 days to go into effect after the buyer is notified about the price<br>increase. Any decrease in pay as you go prices takes effect<br>immediately.                                                                                                                                                                                                          | `CreateAgreementRequest`,<br>`AcceptAgreementRequest`      | AMEND   |
| [Enable or disable auto-renewal](#buyer-auto-renew "#buyer-auto-renew")                   | The Acceptor can turn ON/Off the auto renew flag on their agreement<br>if the seller has enabled renewal offer terms, and can change the flag<br>until the renewal decision deadline. In case its enabled, the<br>renew agreement will be created by the Agreement service on the date of<br>expiry of the original agreement using the offer that<br>`renewalSummary.offerId` identifies. The start<br>date of this Agreement created will be same as the end date of the<br>original agreement. Turning ON the flag does not guarantee that the<br>agreement will renew.                                                                                                                                                                                                                                                            | `CreateAgreementRequest`,<br>`AcceptAgreementRequest`      | AMEND   |
| [Cancel an agreement](#buyer-cancel-agreement "#buyer-cancel-agreement")                  | Acceptor can cancel usage agreement. For everything else,<br>buyer must reach out to seller to initiate cancellation. When you cancel your agreement, your license and<br>entitlement gets deactivated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `CancelAgreement`                                          | N/A     |
| [Search agreements](#buyer-search-agreements "#buyer-search-agreements")                  | Acceptor can perform search across all agreements that they<br>participated in as acceptor in AWS Marketplace. The search returns a list of<br>agreements with basic agreement information.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `SearchAgreements`                                         | N/A     |
| [Describe an agreement](#buyer-describe-agreement "#buyer-describe-agreement")            | Acceptor can view details about an agreement, such as the proposer,<br>acceptor, start date, and end date.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `DescribeAgreement`                                        | N/A     |
| [Get agreement terms](#buyer-get-terms "#buyer-get-terms")                                | Acceptor can obtain details about the terms in an agreement that they<br>participated in as acceptor.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `GetAgreementTerms`                                        | N/A     |
| [Get agreement entitlements](#buyer-get-entitlements "#buyer-get-entitlements")           | Acceptor can obtain agreement level view of status and details of<br>entitlements tied to their agreement<br>• for example, whether it's in the<br>process of being granted or if it has been rejected (and if so, for what<br>reasons), what's the entitlements being granted to customers.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | `GetAgreementEntitlements`                                 | N/A     |
| [Get a registration token](#buyer-get-registration-token "#buyer-get-registration-token") | Registration token is a short-lived token required by acceptors to setup<br>account with proposers. This token is used for both externally metered<br>and entitled dimension types. The token is only valid for 30 minutes<br>after creation and currently only applicable for SaaS purchase<br>agreements.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | `GetAgreementEntitlements`                                 | N/A     |
| [List agreement charges](#buyer-list-charges "#buyer-list-charges")                       | Acceptor can view charges and Purchase Order details associated with<br>them for their Agreement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | `ListAgreementCharges`                                     | N/A     |
| [Update purchase orders](#buyer-update-purchase-orders "#buyer-update-purchase-orders")   | Acceptor can add a purchase order number after subscribing to a<br>product. Once a purchase order is associated with a charge, the invoice<br>generated for that charge will include the purchase order<br>number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | `UpdatePurchaseOrders`                                     | N/A     |
| [List cancellation requests](#buyer-list-cancellations "#buyer-list-cancellations")       | Acceptor can list all cancellation requests for agreements they<br>participate in. The list can be filtered by agreement, status, and<br>other criteria.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `ListAgreementCancellationRequests`                        | N/A     |
| [Get cancellation request details](#buyer-get-cancellation "#buyer-get-cancellation")     | Acceptor can retrieve detailed information about a specific<br>cancellation request initiated by the seller<br>(proposer), including status, timestamps, and reason<br>codes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | `GetAgreementCancellationRequest`                          | N/A     |
| [Accept a cancellation request](#buyer-accept-cancellation "#buyer-accept-cancellation")  | Acceptor can approve a cancellation request initiated by the seller<br>(proposer) for an active agreement. After approval, the agreement<br>cancellation workflow executes asynchronously and the agreement status<br>changes to cancelled. Note: Users also need<br>`CancelAgreement` permission because approving the<br>cancellation request leads to agreement cancellation.                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `AcceptAgreementCancellationRequest`,<br>`CancelAgreement` | N/A     |
| [Reject a cancellation request](#buyer-reject-cancellation "#buyer-reject-cancellation")  | Acceptor can reject a cancellation request initiated by the seller<br>(proposer). After rejection, the agreement remains active and the<br>cancellation request enters a terminal state. The seller can create a<br>new cancellation request if needed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `RejectAgreementCancellationRequest`                       | N/A     |
| [List payment requests](#buyer-list-payments "#buyer-list-payments")                      | Acceptor can list all payment requests for agreements they<br>participate in. The list can be filtered by agreement, status, and<br>other criteria.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `ListAgreementPaymentRequests`                             | N/A     |
| [Get payment request details](#buyer-get-payment "#buyer-get-payment")                    | Acceptor can retrieve detailed information about a specific<br>payment request initiated by the seller<br>(proposer), including status, timestamps, and associated<br>charges.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | `GetAgreementPaymentRequest`                               | N/A     |
| [Accept a payment request](#buyer-accept-payment "#buyer-accept-payment")                 | Acceptor can approve a payment request initiated by the seller<br>(proposer) for an active agreement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `AcceptAgreementPaymentRequest`                            | N/A     |
| [Reject a payment request](#buyer-reject-payment "#buyer-reject-payment")                 | Acceptor can reject a payment request initiated by the seller<br>(proposer). After rejection, the payment request enters a terminal<br>state. The seller can create a new payment request if<br>needed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `RejectAgreementPaymentRequest`                            | N/A     |

## Generate a quote

Use `CreateAgreementRequest` to generate a quote. You must provide:

- `agreementProposalIdentifier` — the `agreementProposalId` from the
  [GetOffer](../APIReference/API_marketplace-discovery_GetOffer.md "../APIReference/API_marketplace-discovery_GetOffer.md") response.
- `requestedTerms` — constructed from the terms in the
  [GetOfferTerms](../APIReference/API_marketplace-discovery_GetOfferTerms.md "../APIReference/API_marketplace-discovery_GetOfferTerms.md") response.
  Each term requires its `id`, and some require additional `configuration`.
  See [Constructing requestedTerms](#car-requested-term-overview "#car-requested-term-overview").

```
response = client.create_agreement_request(
    agreementProposalIdentifier='at-edhtjnbilupjv3xqbphtom77y',
    intent='NEW',
    requestedTerms=[
        {'id': 'term-legal-abc123'},
        {'id': 'term-validity-def456'},
        {
            'id': 'term-configurable-pricing-789',
            'configuration': {
                'configurableUpfrontPricingTermConfiguration': {
                    'selectorValue': 'P12M',
                    'dimensions': [
                        {'dimensionKey': 'Users', 'dimensionValue': 50}
                    ]
                }
            }
        },
        {
            'id': 'term-renewal-012',
            'configuration': {
                'renewalTermConfiguration': {'enableAutoRenew': True}
            }
        }
    ]
)

print(f"Agreement Request ID: {response['agreementRequestId']}")
for charge in response['chargeSummary']['expectedCharges']:
    print(f"  Charge ID: {charge['id']}, Amount: ${charge['amount']}")
```

### Constructing requestedTerms

To construct `requestedTerms`, you need to determine two things:

1. **Which terms to include** — determined by the pricing model of the offer. See [Required terms by pricing model](#car-required-terms-by-pricing-model "#car-required-terms-by-pricing-model").
2. **Which terms need configuration** — most terms only need the `id`, but three term types require additional buyer-supplied configuration. See [Term configurations](#car-term-configurations "#car-term-configurations").

### Required terms by pricing model

The `pricingModel.PricingModel` field in the
[GetOffer](../APIReference/API_marketplace-discovery_GetOffer.md "../APIReference/API_marketplace-discovery_GetOffer.md")
response determines which terms must be included in your `CreateAgreementRequest`.

The following terms must be included in **every** agreement when present in the offer:
`LegalTerm`, `SupportTerm`, `ValidityTerm`, and `RenewalTerm`.

###### Note

`FreeTrialPricingTerm` can only be accepted **once** per product — `CreateAgreementRequest` will return an error if the buyer has already used a free trial.

**CONTRACT**

All terms returned by
[GetOfferTerms](../APIReference/API_marketplace-discovery_GetOfferTerms.md "../APIReference/API_marketplace-discovery_GetOfferTerms.md")
are required in a **single** `CreateAgreementRequest`.

**USAGE**

Agreement creation depends on the terms present in the offer:

1. **First agreement** — Accept `UsageBasedPricingTerm` and/or `RecurringPaymentTerm` (depending on what the offer includes) along with the mandatory terms. This grants product usage entitlements.
2. **Subsequent agreement(s)** (optional) — If the offer includes `ConfigurableUpfrontPricingTerm`, `FixedUpfrontPricingTerm`, or `PaymentScheduleTerm`, you can optionally create a separate agreement to purchase annual to get discounted pricing.

###### Note

If you create both agreements and later want to cancel, cancel the subsequent agreement (with `ConfigurableUpfrontPricingTerm`) first, then cancel the first agreement (with `UsageBasedPricingTerm` and/or `RecurringPaymentTerm`).

**BYOL**

Accept `ByolPricingTerm` along with the mandatory terms.

### Term configurations

Most terms require only the `id` from
[GetOfferTerms](../APIReference/API_marketplace-discovery_GetOfferTerms.md "../APIReference/API_marketplace-discovery_GetOfferTerms.md").
The following term types require a buyer-supplied `configuration` in addition to the `id`:

| Term type                        | Configuration                                                                                                                  | What the buyer provides                              |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| `ConfigurableUpfrontPricingTerm` | [ConfigurableUpfrontPricingTermConfiguration](#car-configurable-upfront-pricing-term "#car-configurable-upfront-pricing-term") | Agreement duration and number of units per dimension |
| `RenewalTerm`                    | [RenewalTermConfiguration](#car-renewal-term "#car-renewal-term")                                                              | Whether to auto-renew when the agreement expires     |
| `VariablePaymentTerm`            | [VariablePaymentTermConfiguration](#car-variable-payment-term "#car-variable-payment-term")                                    | How payment requests from the seller are approved    |

#### ConfigurableUpfrontPricingTermConfiguration

Use the example below to locate the values needed for `ConfigurableUpfrontPricingTermConfiguration`.

Example `GetOfferTerms` response:

```
{
  "offerTerms": [
    {
      "configurableUpfrontPricingTerm": {
        "id": "term-34dfb665ebd38eb2d0269a4af454c4f33cd90292ecc7b0f71058175594f67394",
        "currencyCode": "USD",
        "rateCards": [
          {
            "constraints": {
              "multipleDimensionSelection": "Allowed",
              "quantityConfiguration": "Allowed"
            },
            "selector": {
              "type": "Duration",
              "value": "P1M"
            },
            "rateCard": [
              {
                "dimensionKey": "BasicService",
                "displayName": "Basic Service",
                "price": "0",
                "unit": "Units"
              },
              {
                "dimensionKey": "PremiumService",
                "displayName": "Premium Service",
                "price": "0",
                "unit": "Units"
              }
            ]
          }
        ],
        "type": "ConfigurableUpfrontPricingTerm"
      }
    }
  ]
}
```

| Field                                                       | Value / source                                                                    |
| ----------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `ConfigurableUpfrontPricingTermConfiguration.selectorValue` | `offerTerms[].configurableUpfrontPricingTerm.rateCards[].selector.value`          |
| `Dimension.dimensionKey`                                    | `offerTerms[].configurableUpfrontPricingTerm.rateCards[].rateCard[].dimensionKey` |
| `Dimension.dimensionValue`                                  | Buyer-supplied integer (number of units to purchase for that dimension)           |

###### Note

The `constraints` field in the rate card governs how you may craft the
`ConfigurableUpfrontPricingTermConfiguration` — for example, whether you may select multiple dimensions or only one.
See the [Constraints](../APIReference/API_marketplace-agreements_Constraints.md "../APIReference/API_marketplace-agreements_Constraints.md") data type for details.

Example `RequestedTerm` payload for `ConfigurableUpfrontPricingTerm`:

```
{
  "id": "term-43ab7a2445f89dfcb7e1a6a81c92fe08c124125ffad126bea5e5b7915c065166",
  "configuration": {
    "configurableUpfrontPricingTermConfiguration": {
      "selectorValue": "P12M",
      "dimensions": [
        {
          "dimensionKey": "AdminUsers",
          "dimensionValue": 5
        },
        {
          "dimensionKey": "ReadOnlyUsers",
          "dimensionValue": 10
        }
      ]
    }
  }
}
```

#### RenewalTermConfiguration

| Field             | Value / source                                            |
| ----------------- | --------------------------------------------------------- |
| `enableAutoRenew` | Buyer-supplied boolean (`true` or `false`) — **required** |

Example `RequestedTerm` payload for `RenewalTerm`:

```
{
  "id": "term-ffcc0100ce0c5468426dc07d0b05cff09ab8447640108d9c95ce1591f0949738",
  "configuration": {
    "renewalTermConfiguration": {
      "enableAutoRenew": false
    }
  }
}
```

#### VariablePaymentTermConfiguration

| Field                                                                                         | Value / source                                                                                                     |
| --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| `RequestedTerm.configuration.variablePaymentTermConfiguration.paymentRequestApprovalStrategy` | Buyer-supplied: `AUTO_APPROVE_ON_EXPIRATION` or `WAIT_FOR_APPROVAL` — **required**                                 |
| `RequestedTerm.configuration.variablePaymentTermConfiguration.expirationDuration`             | Buyer-supplied duration (for example, `P10D`); *_required_<br>• only when strategy is `AUTO_APPROVE_ON_EXPIRATION` |

Example `RequestedTerm` payload for `VariablePaymentTerm`:

```
{
  "id": "term-9ab34376c51cd5b4dc995aa0f410b657d58bd577b3f09b34d38afb6964aaaf12",
  "configuration": {
    "variablePaymentTermConfiguration": {
      "paymentRequestApprovalStrategy": "AUTO_APPROVE_ON_EXPIRATION",
      "expirationDuration": "P10D"
    }
  }
}
```

## Accept an offer

First, generate a quote as described in [Generate a quote](#buyer-generate-quote "#buyer-generate-quote").
Then, use `AcceptAgreementRequest` to accept the quote and create the agreement.
You must call `AcceptAgreementRequest` before the agreement request expires.
You can optionally associate a purchase order number during acceptance.

```
# Use chargeId from CreateAgreementRequest response
response = client.accept_agreement_request(
    agreementRequestId='agrq-abc123',
    purchaseOrders=[
        {
            'chargeId': 'charge-xyz',  # From chargeSummary.expectedCharges[].id
            'purchaseOrderReference': 'PO-2024-001'
        }
    ]
)

print(f"Agreement ID: {response['agreementId']}")
```

## Replace an existing agreement

Construct a `CreateAgreementRequest` as described in
[Generate a quote](#buyer-generate-quote "#buyer-generate-quote"), but set
`intent` to `REPLACE` and provide `sourceAgreementIdentifier`
with the agreement to replace. Then call `AcceptAgreementRequest` to complete the replacement.

```
response = client.create_agreement_request(
    agreementProposalIdentifier='at-edhtjnbilupjv3xqbphtom77y',
    intent='REPLACE',
    sourceAgreementIdentifier='agmt-existing123'
)

print(f"Agreement Request ID: {response['agreementRequestId']}")
```

## Amend an existing agreement

To modify term configuration on an existing agreement, set `intent` to `AMEND`
and provide `sourceAgreementIdentifier`. Unlike a new agreement, no
`agreementProposalIdentifier` is needed. Only include the terms whose configuration
you want to change. Then call `AcceptAgreementRequest` to apply the amendment.

```
response = client.create_agreement_request(
    intent='AMEND',
    sourceAgreementIdentifier='agmt-existing123',
    requestedTerms=[
        {
            'id': 'term-configurable-pricing-789',
            'configuration': {
                'configurableUpfrontPricingTermConfiguration': {
                    'selectorValue': 'P12M',
                    'dimensions': [
                        {'dimensionKey': 'Users', 'dimensionValue': 100}
                    ]
                }
            }
        }
    ]
)

print(f"Agreement Request ID: {response['agreementRequestId']}")
```

## Enable or disable auto-renewal

Use `CreateAgreementRequest` with the `AMEND` intent to toggle auto-renewal.

```
response = client.create_agreement_request(
    intent='AMEND',
    sourceAgreementIdentifier='agmt-existing123',
    requestedTerms=[
        {
            'id': 'term-renewal-456',
            'configuration': {
                'renewalTermConfiguration': {'enableAutoRenew': True}
            }
        }
    ]
)

print(f"Agreement Request ID: {response['agreementRequestId']}")
```

Set `enableAutoRenew` to `false` to turn auto-renewal off.

###### Note

Turning auto-renewal on records your renewal preference. It does not guarantee
that the agreement renews, because the seller can opt out of the renewal
independently of you, and a seller opt-out is final. Call
`DescribeAgreement` and read `endTimeBehavior` to find
out what happens at the agreement end date.

You can change your preference until the renewal decision deadline, or until the
agreement end date if the offer sets no deadline. After that, this
`AMEND` request is rejected. The deadline and the other renewal values
the seller authorized are reported in the [RenewalTerm](../APIReference/API_marketplace-agreements_RenewalTerm.md "../APIReference/API_marketplace-agreements_RenewalTerm.md").

## Cancel an agreement

Use `CancelAgreement` to cancel a usage agreement. For other agreement types,
the buyer must reach out to the seller to initiate cancellation.

```
client.cancel_agreement(
    agreementId='agmt-abc123'
)
```

## Search agreements

Use `SearchAgreements` to search across all agreements that you participate in as an acceptor.
The search returns a list of agreements with basic agreement information.

```
response = client.search_agreements(
    catalog='AWSMarketplace',
    filters=[
        {'name': 'PartyType', 'values': ['Acceptor']},
        {'name': 'AgreementType', 'values': ['PurchaseAgreement']},
        {'name': 'Status', 'values': ['ACTIVE']}
    ]
)

for agmt in response['agreementViewSummaries']:
    print(f"  {agmt['agreementId']}: {agmt['status']}")
```

## Describe an agreement

Use `DescribeAgreement` to view details about an agreement, such as the proposer,
acceptor, start date, and end date.

```
response = client.describe_agreement(
    agreementId='agmt-abc123'
)

print(f"Status: {response['status']}")
print(f"Start: {response['startTime']}")
print(f"End: {response['endTime']}")
```

## Get agreement terms

Use `GetAgreementTerms` to obtain details about the terms in an agreement
that you participate in as an acceptor.

```
response = client.get_agreement_terms(
    agreementId='agmt-abc123'
)

for term in response['acceptedTerms']:
    print(f"  Term: {term}")
```

## Get agreement entitlements

Use `GetAgreementEntitlements` to obtain an agreement-level view of the status and details
of entitlements tied to your agreement.

```
response = client.get_agreement_entitlements(
    agreementId='agmt-abc123'
)

for ent in response['agreementEntitlements']:
    print(f"  {ent['resource']}: {ent['status']}")
```

## Get a registration token

Use `GetAgreementEntitlements` to obtain a registration token. This short-lived token
(valid for 30 minutes) is required by acceptors to set up an account with proposers.
Currently only applicable for SaaS purchase agreements.

```
response = client.get_agreement_entitlements(
    agreementId='agmt-abc123'
)

for ent in response['agreementEntitlements']:
    if 'registrationToken' in ent:
        print(f"Registration Token: {ent['registrationToken']}")
        # Token is valid for 30 minutes
```

## List agreement charges

Use `ListAgreementCharges` to view charges and purchase order details
associated with your agreement.

```
response = client.list_agreement_charges(
    agreementId='agmt-abc123'
)

for charge in response['items']:
    print(f"  {charge['id']} (rev {charge['revision']}): ${charge['amount']}")
    print(f"  PO: {charge.get('purchaseOrderReference', 'N/A')}")
```

## Update purchase orders

Use `UpdatePurchaseOrders` to add a purchase order number after subscribing to a product.
Use the `chargeId` and `chargeRevision` from the
[List agreement charges](#buyer-list-charges "#buyer-list-charges") response.
Once a purchase order is associated with a charge, the invoice generated for that charge includes
the purchase order number.

```
client.update_purchase_orders(
    agreementId='agmt-abc123',
    purchaseOrders=[
        {
            'chargeId': 'charge-xyz',
            'chargeRevision': 1,
            'purchaseOrderReference': 'PO-2024-001'
        }
    ]
)
```

For how purchase orders carry over when an agreement renews, see [Purchase orders for renewals](../buyerguide/purchase-orders-for-renewals.md "../buyerguide/purchase-orders-for-renewals.md").

## List cancellation requests

Use `ListAgreementCancellationRequests` to list all cancellation requests for
agreements you participate in. You can filter by agreement, status, and other criteria.

```
response = client.list_agreement_cancellation_requests(
    partyType='Acceptor',
    agreementId='agmt-abc123'
)

for req in response['agreementCancellationRequests']:
    print(f"  {req['agreementCancellationRequestId']}: {req['status']}")
```

## Get cancellation request details

Use `GetAgreementCancellationRequest` to retrieve detailed information about a
specific cancellation request, including status, timestamps, and reason codes.

```
response = client.get_agreement_cancellation_request(
    agreementId='agmt-abc123',
    agreementCancellationRequestId='acr-abc123'
)

print(f"Status: {response['status']}")
print(f"Reason: {response['reasonCode']}")
```

## Accept a cancellation request

Use `AcceptAgreementCancellationRequest` to approve a cancellation request initiated
by the seller. After approval, the agreement cancellation workflow executes asynchronously.
You also need `CancelAgreement` permission because approving the cancellation request
leads to agreement cancellation.

```
client.accept_agreement_cancellation_request(
    agreementId='agmt-abc123',
    agreementCancellationRequestId='acr-abc123'
)
```

## Reject a cancellation request

Use `RejectAgreementCancellationRequest` to reject a cancellation request initiated
by the seller. After rejection, the agreement remains active and the seller can create a new
cancellation request if needed.

```
client.reject_agreement_cancellation_request(
    agreementId='agmt-abc123',
    agreementCancellationRequestId='acr-abc123'
)
```

## List payment requests

Use `ListAgreementPaymentRequests` to list all payment requests for
agreements you participate in. You can filter by agreement, status, and other criteria.

```
response = client.list_agreement_payment_requests(
    partyType='Acceptor',
    agreementId='agmt-abc123'
)

for req in response['agreementPaymentRequests']:
    print(f"  {req['agreementPaymentRequestId']}: {req['status']}")
```

## Get payment request details

Use `GetAgreementPaymentRequest` to retrieve detailed information about a
specific payment request, including status, timestamps, and associated charges.

```
response = client.get_agreement_payment_request(
    paymentRequestId='apr-abc123',
    agreementId='agmt-abc123'
)

print(f"Status: {response['status']}")
print(f"Amount: ${response['amount']}")
```

## Accept a payment request

Use `AcceptAgreementPaymentRequest` to approve a payment request initiated
by the seller for an active agreement.

```
client.accept_agreement_payment_request(
    paymentRequestId='apr-abc123',
    agreementId='agmt-abc123'
)
```

## Reject a payment request

Use `RejectAgreementPaymentRequest` to reject a payment request initiated
by the seller. After rejection, the seller can create a new payment request if needed.

```
client.reject_agreement_payment_request(
    paymentRequestId='apr-abc123',
    agreementId='agmt-abc123'
)
```
