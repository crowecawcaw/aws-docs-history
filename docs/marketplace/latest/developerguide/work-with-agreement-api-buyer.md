

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Work with the Agreement API as a buyer

An agreement is a document that binds two parties, including the proposer and the acceptor (commonly, the buyer) and defines the terms and conditions applicable between them.

Buyer creates an AgreementRequest, which generates a quote. This quote includes all relevant information, such as the estimated charges that will be incurred over the lifetime of the agreement, which is critical for the buyer's purchase decision. If the buyer is satisfied with the quote, they can accept the AgreementRequest before it expires. The Agreement is created upon acceptance of the AgreementRequest. During this process, the buyer admin or buyer persona can associate purchase order to charges. Finally, based on the terms and conditions of the active agreement, the buyer is invoiced and granted a License to use the product.

## Prerequisites: Discover products and offers
<a name="agreement-buyer-prerequisites"></a>

Before creating an agreement, use the AWS Marketplace Discovery API to discover the product and obtain the `agreementProposalId`, `pricingModel`, and term details needed to construct a `CreateAgreementRequest`.


| Step | Discovery API action | Output | Used for | 
| --- | --- | --- | --- | 
| 1 | [ListPurchaseOptions](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_ListPurchaseOptions.html) | offerId | Finding available offers for a product | 
| 2 | [GetOffer](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_GetOffer.html) | agreementProposalId, pricingModel | Constructing agreementProposalIdentifier | 
| 3 | [GetOfferTerms](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_GetOfferTerms.html) | Term IDs and pricing details | Constructing requestedTerms | 

For detailed information about discovering products and pricing, see [Discover products and pricing](work-with-catalog-to-discover-products.md).

An acceptor can perform the following tasks using this API:


| Task | Description | Action(s) | Intent | 
| --- | --- | --- | --- | 
| [Generate a quote](#buyer-generate-quote) | Acceptor can generate quote that includes all relevant information, such as the Charges that will be incurred over the lifetime of the agreement, which is critical for the buyer's purchase decision. | CreateAgreementRequest | NEW | 
| [Get agreement request details](#buyer-get-agreement-request) | Acceptor can view details about an agreement request, such as its status, whether it requires approval, and the expected charges. | GetAgreementRequest | N/A | 
| [Get agreement request terms](#buyer-get-agreement-request-terms) | Acceptor can obtain details about the terms in an agreement request. | GetAgreementRequestTerms | N/A | 
| [List agreement requests](#buyer-list-agreement-requests) | Acceptor can list the agreement requests that they created. The list can be filtered by status and resource. | ListAgreementRequests | N/A | 
| [Cancel an agreement request](#buyer-cancel-agreement-request) | Acceptor can cancel an agreement request. | CancelAgreementRequest | N/A | 
| [Get approval plans](#buyer-get-approval-plans) | Acceptor can get the approval plans for an agreement request that requires approval. | GetAgreementRequestApprovalPlans | N/A | 
| [Start approvals](#buyer-start-approvals) | Acceptor can start the approvals for an agreement request. | StartAgreementApprovals | N/A | 
| [List approvals](#buyer-list-approvals) | Acceptor or organization administrator can list agreement approvals. | ListAgreementApprovals | N/A | 
| [Get approval details](#buyer-get-approval) | Acceptor or organization administrator can retrieve details about an agreement approval, including its status and each approver's outcome. | GetAgreementApproval | N/A | 
| [Approve an agreement approval](#approve-agreement-approval) | Organization administrator can approve an agreement approval, as the organization administrator approver or on behalf of another approver. | AcceptAgreementApproval | N/A | 
| [Reject an agreement approval](#reject-agreement-approval) | Organization administrator can reject an agreement approval, as the organization administrator approver or on behalf of another approver. | RejectAgreementApproval | N/A | 
| [Accept an offer](#buyer-accept-offer) | The Acceptor can accept terms proposed by the proposer that creates a new agreement. This acceptance can involve passing parameters for certain terms, such as selecting the quantity or duration, adding purchase order etc. Acceptor can also create a new agreement where the product usage begins at a future date. The agreement sign date will be when the offer is accepted and when the agreement is created. The Agreement start date is future date when the product usage begins. This is the date when license/entitlement gets activated. To retrieve the latest status of your usage entitlement, refer to the [GetAgreementEntitlements](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_GetAgreementEntitlements.html) API. | CreateAgreementRequest, AcceptAgreementRequest | NEW | 
| [Replace an existing agreement](#buyer-replace-agreement) | The Acceptor can perform a mid-term upgrade on their agreement to either switch to more favorable terms or switch seller for their agreements. This action terminates the existing Agreement passed as input and creates net new Agreement. This action is logically equivalent to a CANCEL followed by a NEW agreement, but ensures entitlement continuity for the Acceptor and at no point is the Acceptor left without entitlements. | CreateAgreementRequest, AcceptAgreementRequest | REPLACE | 
| [Amend an existing agreement](#buyer-amend-agreement) | The acceptor is only permitted to modify the configuration for the accepted terms. For example, they can enable or disable auto-renewal, or modify the purchased quantity, as long as the price change post-modification does not result in refunds. We will only support amending charge if agreement has not started. Note: Proposer is allowed to modify prices for pay-as-you-go pricing term. Any increase in pay as you go prices takes 90 days to go into effect after the buyer is notified about the price increase. Any decrease in pay as you go prices takes effect immediately. | CreateAgreementRequest, AcceptAgreementRequest | AMEND | 
| [Enable or disable auto-renewal](#buyer-auto-renew) | The Acceptor can turn ON/Off the auto renew flag on their agreement if the seller has enabled renewal offer terms, and can change the flag until the renewal decision deadline. In case its enabled, the renew agreement will be created by the Agreement service on the date of expiry of the original agreement using the offer that renewalSummary.offerId identifies. The start date of this Agreement created will be same as the end date of the original agreement. Turning ON the flag does not guarantee that the agreement will renew. | CreateAgreementRequest, AcceptAgreementRequest | AMEND | 
| [Cancel an agreement](#buyer-cancel-agreement) | Acceptor can cancel usage agreement. For everything else, buyer must reach out to seller to initiate cancellation. When you cancel your agreement, your license and entitlement gets deactivated. | CancelAgreement | N/A | 
| [Search agreements](#buyer-search-agreements) | Acceptor can perform search across all agreements that they participated in as acceptor in AWS Marketplace. The search returns a list of agreements with basic agreement information. | SearchAgreements | N/A | 
| [Describe an agreement](#buyer-describe-agreement) | Acceptor can view details about an agreement, such as the proposer, acceptor, start date, and end date. | DescribeAgreement | N/A | 
| [Get agreement terms](#buyer-get-terms) | Acceptor can obtain details about the terms in an agreement that they participated in as acceptor. | GetAgreementTerms | N/A | 
| [Get agreement contacts](#buyer-get-contacts) | Acceptor can retrieve the contact information captured on an agreement that they participated in as acceptor. | GetAgreementContacts | N/A | 
| [Get agreement entitlements](#buyer-get-entitlements) | Acceptor can obtain agreement level view of status and details of entitlements tied to their agreement - for example, whether it's in the process of being granted or if it has been rejected (and if so, for what reasons), what's the entitlements being granted to customers. | GetAgreementEntitlements | N/A | 
| [Get a registration token](#buyer-get-registration-token) | Registration token is a short-lived token required by acceptors to setup account with proposers. This token is used for both externally metered and entitled dimension types. The token is only valid for 30 minutes after creation and currently only applicable for SaaS purchase agreements. | GetAgreementEntitlements | N/A | 
| [List agreement charges](#buyer-list-charges) | Acceptor can view charges and Purchase Order details associated with them for their Agreement. | ListAgreementCharges | N/A | 
| [Update purchase orders](#buyer-update-purchase-orders) | Acceptor can add a purchase order number after subscribing to a product. Once a purchase order is associated with a charge, the invoice generated for that charge will include the purchase order number. | UpdatePurchaseOrders | N/A | 
| [List cancellation requests](#buyer-list-cancellations) | Acceptor can list all cancellation requests for agreements they participate in. The list can be filtered by agreement, status, and other criteria. | ListAgreementCancellationRequests | N/A | 
| [Get cancellation request details](#buyer-get-cancellation) | Acceptor can retrieve detailed information about a specific cancellation request initiated by the seller (proposer), including status, timestamps, and reason codes. | GetAgreementCancellationRequest | N/A | 
| [Accept a cancellation request](#buyer-accept-cancellation) | Acceptor can approve a cancellation request initiated by the seller (proposer) for an active agreement. After approval, the agreement cancellation workflow executes asynchronously and the agreement status changes to cancelled. Note: Users also need CancelAgreement permission because approving the cancellation request leads to agreement cancellation. | AcceptAgreementCancellationRequest, CancelAgreement | N/A | 
| [Reject a cancellation request](#buyer-reject-cancellation) | Acceptor can reject a cancellation request initiated by the seller (proposer). After rejection, the agreement remains active and the cancellation request enters a terminal state. The seller can create a new cancellation request if needed. | RejectAgreementCancellationRequest | N/A | 
| [List payment requests](#buyer-list-payments) | Acceptor can list all payment requests for agreements they participate in. The list can be filtered by agreement, status, and other criteria. | ListAgreementPaymentRequests | N/A | 
| [Get payment request details](#buyer-get-payment) | Acceptor can retrieve detailed information about a specific payment request initiated by the seller (proposer), including status, timestamps, and associated charges. | GetAgreementPaymentRequest | N/A | 
| [Accept a payment request](#buyer-accept-payment) | Acceptor can approve a payment request initiated by the seller (proposer) for an active agreement. | AcceptAgreementPaymentRequest | N/A | 
| [Reject a payment request](#buyer-reject-payment) | Acceptor can reject a payment request initiated by the seller (proposer). After rejection, the payment request enters a terminal state. The seller can create a new payment request if needed. | RejectAgreementPaymentRequest | N/A | 

## Generate a quote
<a name="buyer-generate-quote"></a>

Use `CreateAgreementRequest` to generate a quote. You must provide:
+ `agreementProposalIdentifier` — the `agreementProposalId` from the [GetOffer](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_GetOffer.html) response.
+ `requestedTerms` — constructed from the terms in the [GetOfferTerms](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_GetOfferTerms.html) response. Each term requires its `id`, and some require additional `configuration`. See [Constructing requestedTerms](#car-requested-term-overview).

You can optionally provide `acceptorContact` with your contact information.

```python
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
<a name="car-requested-term-overview"></a>

To construct `requestedTerms`, you need to determine two things:

1. **Which terms to include** — determined by the pricing model of the offer. See [Required terms by pricing model](#car-required-terms-by-pricing-model).

1. **Which terms need configuration** — most terms only need the `id`, but three term types require additional buyer-supplied configuration. See [Term configurations](#car-term-configurations).

### Required terms by pricing model
<a name="car-required-terms-by-pricing-model"></a>

The `pricingModel.[PricingModel](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_PricingModel.html)` field in the [GetOffer](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_GetOffer.html) response determines which terms must be included in your `CreateAgreementRequest`.

The following terms must be included in **every** agreement when present in the offer: `LegalTerm`, `SupportTerm`, `ValidityTerm`, and `RenewalTerm`.

**Note**  
`FreeTrialPricingTerm` can only be accepted **once** per product — `CreateAgreementRequest` will return an error if the buyer has already used a free trial.

**CONTRACT**

All terms returned by [GetOfferTerms](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_GetOfferTerms.html) are required in a **single** `CreateAgreementRequest`.

**USAGE**

Agreement creation depends on the terms present in the offer:

1. **First agreement** — Accept `UsageBasedPricingTerm` and/or `RecurringPaymentTerm` (depending on what the offer includes) along with the mandatory terms. This grants product usage entitlements.

1. **Subsequent agreement(s)** (optional) — If the offer includes `ConfigurableUpfrontPricingTerm`, `FixedUpfrontPricingTerm`, or `PaymentScheduleTerm`, you can optionally create a separate agreement to purchase annual to get discounted pricing.

**Note**  
If you create both agreements and later want to cancel, cancel the subsequent agreement (with `ConfigurableUpfrontPricingTerm`) first, then cancel the first agreement (with `UsageBasedPricingTerm` and/or `RecurringPaymentTerm`).

**BYOL**

Accept `ByolPricingTerm` along with the mandatory terms.

### Term configurations
<a name="car-term-configurations"></a>

Most terms require only the `id` from [GetOfferTerms](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-discovery_GetOfferTerms.html). The following term types require a buyer-supplied `configuration` in addition to the `id`:


| Term type | Configuration | What the buyer provides | 
| --- | --- | --- | 
| ConfigurableUpfrontPricingTerm | [ConfigurableUpfrontPricingTermConfiguration](#car-configurable-upfront-pricing-term) | Agreement duration and number of units per dimension | 
| RenewalTerm | [RenewalTermConfiguration](#car-renewal-term) | Whether to auto-renew when the agreement expires | 
| VariablePaymentTerm | [VariablePaymentTermConfiguration](#car-variable-payment-term) | How payment requests from the seller are approved | 

#### ConfigurableUpfrontPricingTermConfiguration
<a name="car-configurable-upfront-pricing-term"></a>

Use the example below to locate the values needed for `ConfigurableUpfrontPricingTermConfiguration`.

Example `GetOfferTerms` response:

```json
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


| Field | Value / source | 
| --- | --- | 
| ConfigurableUpfrontPricingTermConfiguration.selectorValue | offerTerms[].configurableUpfrontPricingTerm.rateCards[].selector.value | 
| Dimension.dimensionKey | offerTerms[].configurableUpfrontPricingTerm.rateCards[].rateCard[].dimensionKey | 
| Dimension.dimensionValue | Buyer-supplied integer (number of units to purchase for that dimension) | 

**Note**  
The `constraints` field in the rate card governs how you may craft the `ConfigurableUpfrontPricingTermConfiguration` — for example, whether you may select multiple dimensions or only one. See the [Constraints](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_Constraints.html) data type for details.

Example `RequestedTerm` payload for `ConfigurableUpfrontPricingTerm`:

```json
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
<a name="car-renewal-term"></a>


| Field | Value / source | 
| --- | --- | 
| enableAutoRenew | Buyer-supplied boolean (true or false) — required | 

Example `RequestedTerm` payload for `RenewalTerm`:

```json
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
<a name="car-variable-payment-term"></a>


| Field | Value / source | 
| --- | --- | 
| RequestedTerm.configuration.variablePaymentTermConfiguration.paymentRequestApprovalStrategy | Buyer-supplied: AUTO\_APPROVE\_ON\_EXPIRATION or WAIT\_FOR\_APPROVAL — required | 
| RequestedTerm.configuration.variablePaymentTermConfiguration.expirationDuration | Buyer-supplied duration (for example, P10D); required only when strategy is AUTO\_APPROVE\_ON\_EXPIRATION | 

Example `RequestedTerm` payload for `VariablePaymentTerm`:

```json
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

## Get agreement request details
<a name="buyer-get-agreement-request"></a>

Use `GetAgreementRequest` to view details about an agreement request, such as its status, intent, approval requirement, and expected charges.

```python
response = client.get_agreement_request(
    agreementRequestId='ar-abc123'
)

print(f"Status: {response['status']}")
print(f"Approval requirement: {response['approvalRequirement']}")
```

## Get agreement request terms
<a name="buyer-get-agreement-request-terms"></a>

Use `GetAgreementRequestTerms` to obtain details about the terms in an agreement request.

```python
response = client.get_agreement_request_terms(
    agreementRequestId='ar-abc123'
)

for term in response['terms']:
    print(f"  Term: {term}")
```

## List agreement requests
<a name="buyer-list-agreement-requests"></a>

Use `ListAgreementRequests` to list the agreement requests that you created as an acceptor. You can filter by status and resource.

```python
response = client.list_agreement_requests(
    status='PENDING_APPROVAL'
)

for req in response['items']:
    print(f"  {req['agreementRequestId']}: {req['status']}")
```

## Cancel an agreement request
<a name="buyer-cancel-agreement-request"></a>

Use `CancelAgreementRequest` to cancel an agreement request that is pending approval, or approved but not yet accepted. Cancelling an agreement request also cancels its open approvals.

```python
client.cancel_agreement_request(
    agreementRequestId='ar-abc123'
)
```

## Get approval for an agreement request
<a name="buyer-agreement-approvals"></a>

Your organization can require approval before an agreement request is accepted. After you generate a quote as described in [Generate a quote](#buyer-generate-quote), check `approvalRequirement` in the `CreateAgreementRequest` response, or call `GetAgreementRequest`. If the value is `REQUIRED`, get the approval plans and start the approvals.

When every approval is approved, the agreement request is accepted and its status changes to `ACCEPTED`. If the status is `APPROVED` instead, the approvals are complete but the agreement request wasn't accepted, so call `AcceptAgreementRequest` to accept it. This happens when AWS Marketplace can't accept the agreement request automatically after the approvals complete, for example because the offer changed during the review. If the call fails, its error explains why. If an approval is rejected, the status changes to `REJECTED`.

### Get approval plans
<a name="buyer-get-approval-plans"></a>

Use `GetAgreementRequestApprovalPlans` to get the approval plans for an agreement request that requires approval.

```python
response = client.get_agreement_request_approval_plans(
    agreementRequestId='ar-abc123'
)

for plan in response['items']:
    print(f"  Plan: {plan['buyerAgreementApprovalPlan']['planReference']}")
```

### Start approvals
<a name="buyer-start-approvals"></a>

Use `StartAgreementApprovals` to start the approvals for an agreement request, using the plan references from `GetAgreementRequestApprovalPlans`. You can also add a note for the approvers and associate purchase order numbers with charges. You also need `AcceptAgreementRequest` permission because the agreement request is accepted when its approvals are complete.

```python
response = client.start_agreement_approvals(
    agreementRequestId='ar-abc123',
    planInputs=[
        {
            'buyerAgreementApprovalPlanInput': {
                'planReference': 'aplan-abc123',
                'requesterNote': 'Annual subscription for the analytics team'
            }
        }
    ]
)

for approval in response['approvalSummaries']:
    print(f"  {approval['agreementApprovalId']}: {approval['status']}")
```

### List approvals
<a name="buyer-list-approvals"></a>

Use `ListAgreementApprovals` to list agreement approvals. Set `partyType` to `REQUESTER` to list agreement approvals for agreement requests that you created, or to `AWS_ORGANIZATION_ADMIN` to list agreement approvals as an AWS Organizations administrator. You can filter by agreement request, approval type, and status.

```python
response = client.list_agreement_approvals(
    partyType='REQUESTER',
    agreementRequestId='ar-abc123'
)

for approval in response['items']:
    print(f"  {approval['agreementApprovalId']}: {approval['status']}")
```

### Get approval details
<a name="buyer-get-approval"></a>

Use `GetAgreementApproval` to retrieve detailed information about an agreement approval, including its status and the outcome recorded for each approver.

```python
response = client.get_agreement_approval(
    agreementApprovalId='apr-abc123'
)

print(f"Status: {response['buyerAgreementApproval']['status']}")
```

### Approve an agreement approval
<a name="approve-agreement-approval"></a>

If your account is the management account or a delegated administrator of your AWS organization, use `AcceptAgreementApproval` to approve an agreement approval as the organization administrator approver. To approve on behalf of another approver, set `approverOutcomeIdToOverride`. After every level of the agreement approval is approved, its status changes to `APPROVED`.

```python
client.accept_agreement_approval(
    buyerAgreementApprovalApproverInput={
        'agreementApprovalId': 'apr-abc123',
        'note': 'Approved for the analytics team budget'
    }
)
```

### Reject an agreement approval
<a name="reject-agreement-approval"></a>

If your account is the management account or a delegated administrator of your AWS organization, use `RejectAgreementApproval` to reject an agreement approval as the organization administrator approver. To reject on behalf of another approver, set `approverOutcomeIdToOverride`. A note that explains the rejection is required. After rejection, the agreement approval and the agreement request change to `REJECTED` status.

```python
client.reject_agreement_approval(
    buyerAgreementApprovalRejectionInput={
        'agreementApprovalId': 'apr-abc123',
        'note': 'Use the existing enterprise agreement instead'
    }
)
```

## Accept an offer
<a name="buyer-accept-offer"></a>

First, generate a quote as described in [Generate a quote](#buyer-generate-quote). Then, use `AcceptAgreementRequest` to accept the quote and create the agreement. You must call `AcceptAgreementRequest` before the agreement request expires. You can optionally associate a purchase order number during acceptance.

```python
# Use chargeId from CreateAgreementRequest response
response = client.accept_agreement_request(
    agreementRequestId='ar-abc123',
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
<a name="buyer-replace-agreement"></a>

Construct a `CreateAgreementRequest` as described in [Generate a quote](#buyer-generate-quote), but set `intent` to `REPLACE` and provide `sourceAgreementIdentifier` with the agreement to replace. Then call `AcceptAgreementRequest` to complete the replacement.

```python
response = client.create_agreement_request(
    agreementProposalIdentifier='at-edhtjnbilupjv3xqbphtom77y',
    intent='REPLACE',
    sourceAgreementIdentifier='agmt-existing123'
)

print(f"Agreement Request ID: {response['agreementRequestId']}")
```

## Amend an existing agreement
<a name="buyer-amend-agreement"></a>

To modify term configuration on an existing agreement, set `intent` to `AMEND` and provide `sourceAgreementIdentifier`. Unlike a new agreement, no `agreementProposalIdentifier` is needed. Only include the terms whose configuration you want to change. Then call `AcceptAgreementRequest` to apply the amendment.

```python
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
<a name="buyer-auto-renew"></a>

Use `CreateAgreementRequest` with the `AMEND` intent to toggle auto-renewal.

```python
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

**Note**  
Turning auto-renewal on records your renewal preference. It does not guarantee that the agreement renews, because the seller can opt out of the renewal independently of you, and a seller opt-out is final. Call `DescribeAgreement` and read `endTimeBehavior` to find out what happens at the agreement end date.

You can change your preference until the renewal decision deadline, or until the agreement end date if the offer sets no deadline. After that, this `AMEND` request is rejected. The deadline and the other renewal values the seller authorized are reported in the [RenewalTerm](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_RenewalTerm.html).

## Cancel an agreement
<a name="buyer-cancel-agreement"></a>

Use `CancelAgreement` to cancel a usage agreement. For other agreement types, the buyer must reach out to the seller to initiate cancellation.

```python
client.cancel_agreement(
    agreementId='agmt-abc123'
)
```

## Search agreements
<a name="buyer-search-agreements"></a>

Use `SearchAgreements` to search across all agreements that you participate in as an acceptor. The search returns a list of agreements with basic agreement information.

```python
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
<a name="buyer-describe-agreement"></a>

Use `DescribeAgreement` to view details about an agreement, such as the proposer, acceptor, start date, and end date.

```python
response = client.describe_agreement(
    agreementId='agmt-abc123'
)

print(f"Status: {response['status']}")
print(f"Start: {response['startTime']}")
print(f"End: {response['endTime']}")
```

## Get agreement terms
<a name="buyer-get-terms"></a>

Use `GetAgreementTerms` to obtain details about the terms in an agreement that you participate in as an acceptor.

```python
response = client.get_agreement_terms(
    agreementId='agmt-abc123'
)

for term in response['acceptedTerms']:
    print(f"  Term: {term}")
```

## Get agreement contacts
<a name="buyer-get-contacts"></a>

Use `GetAgreementContacts` to retrieve the contact information captured on an agreement that you participate in as an acceptor.

```python
response = client.get_agreement_contacts(
    agreementId='agmt-abc123'
)

contact = response.get('acceptorContact')
if contact:
    print(f"Name: {contact['firstName']} {contact['lastName']}")
    print(f"Email: {contact['emailAddress']}")
    print(f"Company: {contact['companyName']}")
    print(f"Country: {contact['countryCode']}")
```

## Get agreement entitlements
<a name="buyer-get-entitlements"></a>

Use `GetAgreementEntitlements` to obtain an agreement-level view of the status and details of entitlements tied to your agreement.

```python
response = client.get_agreement_entitlements(
    agreementId='agmt-abc123'
)

for ent in response['agreementEntitlements']:
    print(f"  {ent['resource']}: {ent['status']}")
```

## Get a registration token
<a name="buyer-get-registration-token"></a>

Use `GetAgreementEntitlements` to obtain a registration token. This short-lived token (valid for 30 minutes) is required by acceptors to set up an account with proposers. Currently only applicable for SaaS purchase agreements.

```python
response = client.get_agreement_entitlements(
    agreementId='agmt-abc123'
)

for ent in response['agreementEntitlements']:
    if 'registrationToken' in ent:
        print(f"Registration Token: {ent['registrationToken']}")
        # Token is valid for 30 minutes
```

## List agreement charges
<a name="buyer-list-charges"></a>

Use `ListAgreementCharges` to view charges and purchase order details associated with your agreement.

```python
response = client.list_agreement_charges(
    agreementId='agmt-abc123'
)

for charge in response['items']:
    print(f"  {charge['id']} (rev {charge['revision']}): ${charge['amount']}")
    print(f"  PO: {charge.get('purchaseOrderReference', 'N/A')}")
```

## Update purchase orders
<a name="buyer-update-purchase-orders"></a>

Use `UpdatePurchaseOrders` to add a purchase order number after subscribing to a product. Use the `chargeId` and `chargeRevision` from the [List agreement charges](#buyer-list-charges) response. Once a purchase order is associated with a charge, the invoice generated for that charge includes the purchase order number.

```python
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

For how purchase orders carry over when an agreement renews, see [Purchase orders for renewals](https://docs.aws.amazon.com/marketplace/latest/buyerguide/purchase-orders-for-renewals.html).

## List cancellation requests
<a name="buyer-list-cancellations"></a>

Use `ListAgreementCancellationRequests` to list all cancellation requests for agreements you participate in. You can filter by agreement, status, and other criteria.

```python
response = client.list_agreement_cancellation_requests(
    partyType='Acceptor',
    agreementId='agmt-abc123'
)

for req in response['agreementCancellationRequests']:
    print(f"  {req['agreementCancellationRequestId']}: {req['status']}")
```

## Get cancellation request details
<a name="buyer-get-cancellation"></a>

Use `GetAgreementCancellationRequest` to retrieve detailed information about a specific cancellation request, including status, timestamps, and reason codes.

```python
response = client.get_agreement_cancellation_request(
    agreementId='agmt-abc123',
    agreementCancellationRequestId='acr-abc123'
)

print(f"Status: {response['status']}")
print(f"Reason: {response['reasonCode']}")
```

## Accept a cancellation request
<a name="buyer-accept-cancellation"></a>

Use `AcceptAgreementCancellationRequest` to approve a cancellation request initiated by the seller. After approval, the agreement cancellation workflow executes asynchronously. You also need `CancelAgreement` permission because approving the cancellation request leads to agreement cancellation.

```python
client.accept_agreement_cancellation_request(
    agreementId='agmt-abc123',
    agreementCancellationRequestId='acr-abc123'
)
```

## Reject a cancellation request
<a name="buyer-reject-cancellation"></a>

Use `RejectAgreementCancellationRequest` to reject a cancellation request initiated by the seller. After rejection, the agreement remains active and the seller can create a new cancellation request if needed.

```python
client.reject_agreement_cancellation_request(
    agreementId='agmt-abc123',
    agreementCancellationRequestId='acr-abc123'
)
```

## List payment requests
<a name="buyer-list-payments"></a>

Use `ListAgreementPaymentRequests` to list all payment requests for agreements you participate in. You can filter by agreement, status, and other criteria.

```python
response = client.list_agreement_payment_requests(
    partyType='Acceptor',
    agreementId='agmt-abc123'
)

for req in response['agreementPaymentRequests']:
    print(f"  {req['agreementPaymentRequestId']}: {req['status']}")
```

## Get payment request details
<a name="buyer-get-payment"></a>

Use `GetAgreementPaymentRequest` to retrieve detailed information about a specific payment request, including status, timestamps, and associated charges.

```python
response = client.get_agreement_payment_request(
    paymentRequestId='pr-abc123',
    agreementId='agmt-abc123'
)

print(f"Status: {response['status']}")
print(f"Amount: ${response['amount']}")
```

## Accept a payment request
<a name="buyer-accept-payment"></a>

Use `AcceptAgreementPaymentRequest` to approve a payment request initiated by the seller for an active agreement.

```python
client.accept_agreement_payment_request(
    paymentRequestId='pr-abc123',
    agreementId='agmt-abc123'
)
```

## Reject a payment request
<a name="buyer-reject-payment"></a>

Use `RejectAgreementPaymentRequest` to reject a payment request initiated by the seller. After rejection, the seller can create a new payment request if needed.

```python
client.reject_agreement_payment_request(
    paymentRequestId='pr-abc123',
    agreementId='agmt-abc123'
)
```