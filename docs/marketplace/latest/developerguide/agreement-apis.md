

The AWS Marketplace API Reference was restructured. For more information about the supported API operations, see the [AWS Marketplace API Reference](https://docs.aws.amazon.com/marketplace/latest/APIReference/Welcome.html).

# Using the AWS Marketplace Agreement API
<a name="agreement-apis"></a>

AWS Marketplace is a curated digital catalog that customers can use to find, buy, deploy, and manage third-party software, data, and services to build solutions and run their businesses. The AWS Marketplace Agreement Service provides an API interface that helps AWS Marketplace buyers and sellers manage their agreements, including listing, searching, and filtering agreements.

## Key concepts
<a name="agreement-key-concepts"></a>

The following table describes key concepts used in the AWS Marketplace Agreement API.


| Concept | Description | 
| --- | --- | 
| Acceptor | The party that accepts all or a subset of the terms extended by the proposer in an agreement. For most common use cases, acceptors are the buyers of the product. | 
| Agreement | A document that binds two parties, including the proposer (commonly, the seller/ISV or channel partner) and the acceptor (commonly, the buyer) and defines the terms and conditions applicable between them. | 
| Agreement Cancellation Request | A request initiated by the seller (proposer) to cancel an active agreement. The buyer (acceptor) can accept or reject the cancellation request. If accepted, the agreement cancellation workflow executes asynchronously and the agreement status changes to cancelled. If rejected, the agreement remains active and the seller can submit a new cancellation request. | 
| Agreement Proposal | Entity referring to the set of terms/offer proposed by the seller/proposer. | 
| Agreement Request | Entity referring to resource created as a result of customer action, outlining the agreement creation/modification parameters, request lifecycle and estimated outcome upon acceptance of the request. | 
| Billable dimension | Elements related to how the product is priced. For example, Amazon Elastic Compute Cloud (Amazon EC2) instances for Amazon Machine Image (AMI) products, or premium compared to read-only users for software as a service (SaaS) products. | 
| Channel Partners (CP) | Organizations that are authorized by the product owner (ISV) to resell their products on their behalf on AWS Marketplace. | 
| Independent Software Vendors (ISVs) | Sellers that list and manage their own products in AWS Marketplace. | 
| Intent | Intent represents the motivation the buyer has while creating the Agreement. Currently supported intents are New, Amend, and Replace during agreement creation flow. | 
| Payment Request | A request initiated by the seller (proposer) for payment associated with an agreement. The buyer (acceptor) can accept or reject the payment request. | 
| Proposer | The party that extends the initial set of terms in an agreement, most commonly by using an offer. | 
| Purchase Orders | Organizations require buyers to use purchase orders to buy from approved suppliers, track what they buy, and ensure spending is forecasted, budgeted, approved, and assigned to the responsible cost center(s). | 
| Resource | A unit or resource that sellers intend to sell in AWS Marketplace, often referred to as a base product. A base product is not complete for buyer consumption until product information, deployment attributes, and billing information are added. A product describes the product information, software deployment attributes, and billing mechanism of the listing that a seller intends to sell. The product must be paired with an offer to become a transactable unit that can be sold and be used by buyers in AWS Marketplace. | 
| Term | A unit within an agreement that governs how an agreement is enforced (for example, pricing). | 

## Endpoint
<a name="agreement-endpoint"></a>

You can access the AWS Marketplace Agreement Service with the following endpoints:


| Endpoint | Region | Supported IP Protocols | 
| --- | --- | --- | 
| agreement-marketplace.us-east-1.api.aws | US East (N. Virginia) | IPv4, IPv6 | 

## Permissions
<a name="agreement-permissions"></a>

The Agreements API uses standard AWS Signature Version 4 (SigV4) authentication. You must have valid AWS credentials and the appropriate IAM permissions to call the API. For details, see [Access control for the AWS Marketplace Agreement API](agreement-api-access-control.md).

### Error codes
<a name="agreement-error-codes"></a>

The following error codes apply to [AWS Marketplace Agreement Service actions](https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Operations_AWS_Marketplace_Agreement_Service.html). A single error code may be returned for multiple use cases. Refer to the descriptions below to identify the specific scenario in which each error code occurs. This list is not exhaustive and may be updated as new features are released.

#### ValidationException
<a name="agreement-error-codes-validation"></a>


| Error code | Description | 
| --- | --- | 
| INVALID\_SOURCE\_AGREEMENT\_IDENTIFIER | Returned when the source agreement identifier does not match the expected format, or when a source agreement identifier is provided for an intent that does not require one (such as NEW). | 
| MISSING\_SOURCE\_AGREEMENT\_IDENTIFIER | Returned when the source agreement identifier is not provided for an intent that requires one (such as REPLACE or AMEND). | 
| INVALID\_REQUESTED\_TERM\_CONFIGURATION | Returned when the requested term configuration is not valid. Possible scenarios:+  A configuration is provided for a term that does not accept one. <br />+  A required configuration is missing. <br />+  The selector value does not belong to the agreement proposal. <br />+  The dimensions can only contain one dimension when multiple dimension selection is not allowed. <br />+  A dimension key is not recognized in the agreement proposal or accepted terms. <br />+  A dimension value can only be 1 when quantity configuration is not enabled for the dimension. <br />+  The configuration contains duplicate dimension keys. <br />+  The configuration does not differ from the source agreement.  | 
| INVALID\_AGREEMENT\_PROPOSAL\_IDENTIFIER | Returned when the agreement proposal identifier does not match the expected format, or when an agreement proposal identifier is provided for an intent that does not require one (such as AMEND). | 
| MISSING\_AGREEMENT\_PROPOSAL\_IDENTIFIER | Returned when the agreement proposal identifier is not provided for an intent that requires one (such as NEW or REPLACE). | 
| INVALID\_FILTER\_NAME | Returned when the provided filter name is not a recognized filter, or when duplicate filter names are included in the request. | 
| INVALID\_FILTER\_VALUES | Returned when filter values are invalid, duplicated, empty, exceed the maximum allowed count, or when a date range filter specifies a BeforeEndTime value that precedes the AfterEndTime value. | 
| INVALID\_NEXT\_TOKEN | Returned when the pagination token is malformed, expired, cannot be decrypted, or when request parameters have changed between paginated calls. | 
| DUPLICATE\_CHARGES | Returned when the request contains duplicate charge identifiers, or when different purchase order values are provided for the same charge identifier. | 
| UNSUPPORTED\_FILTERS | Returned when the provided combination of filters is not supported. Supported filter combinations vary based on party type. Check the supported combinations in the public documentation. | 
| INVALID\_PURCHASE\_ORDER\_REFERENCE | Returned when the purchase order reference does not meet format requirements, or when a required purchase order is not provided as configured by the account administrator. | 
| INVALID\_CHARGE\_AMOUNT | Returned when the charge amount is not valid. Possible scenarios:+  The charge amount exceeds the maximum total charge amount for the term. <br />+  The charge amount format does not match the currency requirements (for example, too many decimal places). <br />+  No remaining amount is available because the agreement has reached the maximum total charge amount.  | 
| UNSUPPORTED\_ACTION | Returned when the requested operation is not supported for the current state of the resource. The specific scenarios vary by API:+  `UpdatePurchaseOrders` – The charge date is in the past and auto renewal is disabled, the charge date is within 3 hours, the charge is a refund charge, the charge revision is not the latest, the purchase orders do not all belong to the same agreement, or the agreement is not active. <br />+  `CreateAgreementRequest` – Amending a future-dated agreement is not supported, the resource type and term type combination does not support the requested intent, replacing an active agreement with a future-dated agreement is not allowed, the agreement duration cannot be changed during amendment, the agreement cannot be updated at this time (for example, pending entitlements exist), the agreement proposal must refer to the same resource as the source agreement, the agreement proposal must differ from the source agreement, or the agreement type does not support this action. <br />+  `AcceptAgreementRequest` – The resource type and term type combination does not support this action, the agreement type does not support this action, an active agreement already exists on the same resource, or the agreement cannot be updated at this time. <br />+  `CancelAgreement` – The agreement has pending entitlements, the agreement type does not support cancellation, an agreement with `UsageBasedPricingTerm` cannot be cancelled while an agreement with `ConfigurableUpfrontPricingTerm` or `PaymentScheduleTerm` is still active on the same resource, or the resource type and term type combination does not support cancellation. <br />+  `GetBillingAdjustmentRequest` – The agreement is a non-purchase agreement type, or the caller is the acceptor of the agreement. <br />+  `SendAgreementCancellationRequest` – The agreement type does not support this action. <br />+  `AcceptAgreementCancellationRequest` – The agreement type does not support this action. <br />+  `RejectAgreementCancellationRequest` – The agreement type does not support this action. <br />+  `CancelAgreementCancellationRequest` – The agreement type does not support this action. <br />+  `GetAgreementCancellationRequest` – The agreement is a non-purchase agreement type.  | 

#### ResourceNotFoundException
<a name="agreement-error-codes-resource-not-found"></a>

The `ResourceNotFoundException` includes `resourceType` and `resourceId` fields that identify the resource that could not be found. The following table describes the scenarios that can cause this exception for each resource type.

**Note**  
For security reasons, the same error is returned whether a resource does not exist or the caller does not have access to it. This prevents enumeration of valid resource identifiers.


| Resource type | Possible scenarios | 
| --- | --- | 
| AgreementProposal |  +  No agreement proposal found for the given identifier. <br />+  The offer is not targeted to the acceptor. <br />+  The offer is not available in the acceptor's country.   | 
| Agreement |  +  No agreement found for the given identifier. <br />+  The caller is neither the acceptor nor the proposer of the agreement.   | 
| AgreementRequest |  +  No agreement request found for the given identifier. <br />+  The agreement request belongs to another caller. <br />+  The agreement request has expired. <br />+  The agreement request has been superseded by a subsequent accepted request on the same product or offer. <br />+  The agreement proposal became inactive between `CreateAgreementRequest` and `AcceptAgreementRequest` calls due to offer republishing or offer expiration.   | 
| Charge |  +  No charge found for the given identifier. <br />+  The charge does not belong to the specified agreement.   | 
| BillingAdjustmentRequest |  +  No billing adjustment request found for the given identifier. <br />+  The caller is neither the acceptor nor the proposer of the agreement associated with the adjustment.   | 
| AgreementCancellationRequest |  +  No agreement cancellation request found for the given identifier. <br />+  The caller is neither the acceptor nor the proposer of the agreement associated with the cancellation request.   | 
| PaymentRequest |  +  No payment request found for the given identifier. <br />+  The caller is neither the acceptor nor the proposer of the agreement associated with the payment request.   | 