

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Working with Benefit Allocations
<a name="working-with-benefit-allocations"></a>

A Benefit Allocation represents a benefit that has been granted to a partner. When a benefit application is approved, AWS creates one or more benefit allocations that provide partners with the actual credits, funding, access, or other benefit fulfillment.

## Understanding Benefit Allocations
<a name="understanding-benefit-allocations"></a>

Benefit allocations can represent various types of fulfillment:
+ **Financial Disbursements (CASH)** - Direct financial payments to partners with disbursement tracking
+ **AWS Credits (CREDITS)** - Credit codes applicable to AWS accounts with usage tracking
+ **Consumable Allocations** - Pre-approved funding amounts or wallets with utilization tracking
+ **Access Grants (ACCESS)** - Access to systems, tools, or resources
+ **Recognition (RECOGNITION)** - Digital badges, certifications, or status designations
+ **Resources (RESOURCE)** - Technical support, advisory services, or ProServe engagements

Each benefit allocation has a lifecycle tracked through its Status field:
+ **ACTIVE** - The allocation is available for use
+ **INACTIVE** - The allocation is temporarily unavailable
+ **FULFILLED** - The allocation has been completely used or delivered

Benefit allocations also include temporal information defining when they become effective (StartsAt) and when they expire (ExpiresAt), enabling partners to understand the timeframes for utilizing benefits.

## Listing Benefit Allocations
<a name="listing-benefit-allocations"></a>

Partners can view all their benefit allocations using the `ListBenefitAllocations` API action. This returns a paginated list of allocation summaries with comprehensive filtering capabilities.

Partners can filter allocations by:
+ **Benefit Identifier** - View allocations for a specific benefit
+ **Benefit Application Identifier** - View allocations resulting from a specific application
+ **Fulfillment Type** - Filter by allocation type (`CREDITS`, `CASH`, `ACCESS`, etc.)
+ **Status** - Filter by allocation status (`ACTIVE`, `INACTIVE`, `FULFILLED`)

The list response includes allocation summaries containing:
+ Allocation ID, ARN, and name
+ Associated benefit ID and benefit application ID (if applicable)
+ Fulfillment type
+ Current status
+ Creation timestamp
+ Start date

This list view enables partners to build allocation tracking dashboards and identify:
+ Active allocations available for immediate use
+ Allocations approaching expiration
+ Fulfilled allocations for historical tracking
+ Total allocation value by program or fulfillment type

## Viewing Detailed Allocation Information
<a name="viewing-detailed-allocation-information"></a>

Partners can retrieve complete allocation details using the `GetBenefitAllocation` API action. This provides comprehensive information about the allocation including fulfillment-specific details that vary based on the allocation type.

**Core Allocation Information:**
+ Unique identifier (ID) and Amazon Resource Name (ARN)
+ Allocation name and status
+ Status reason (explanation of current status)
+ Associated benefit ID and benefit application ID
+ Fulfillment type
+ Creation, update, start, and expiration timestamps

**Fulfillment Details (Type-Specific):**

The FulfillmentDetail field contains different information structures based on the fulfillment type:

### Cash Disbursement Details (CASH Type)
<a name="cash-disbursement-details"></a>

For direct cash payments, the fulfillment details include:
+ **Disbursed Amount** - The total amount of funding disbursed, including amount value and currency code
+ **Issuance Details (if applicable)** - Information about purchase orders or issuance events:
  + Issuance ID - Unique identifier for the disbursement
  + Issuance Amount - Amount in local currency
  + Issued At - Timestamp of disbursement

This structure supports both single disbursements and pre-approved funding scenarios where multiple issuances may occur against a single allocation.

### Credit Details (CREDITS Type)
<a name="credit-details"></a>

For AWS credits, the fulfillment details include:
+ **Allocated Amount** - Total credit amount allocated
+ **Issued Amount** - Total credit amount issued (may be less than allocated for phased issuance)
+ **Credit Codes** - Array of individual credit code details:
  + AWS Account ID - Account where credit is applied
  + Value - Monetary value of the credit code
  + AWS Credit Code - The actual credit code string
  + Status - Credit code status (`ACTIVE`, `INACTIVE`, `FULFILLED`)
  + Issued At - When the credit code was issued
  + Expires At - When the credit code expires

This detailed credit tracking allows partners to monitor credit utilization across multiple accounts and understand which credits are available, partially used, or fully consumed.

### Consumable Allocation Details (Pre-Approved Amounts/Wallets)
<a name="consumable-allocation-details"></a>

For pre-approved funding pools, the fulfillment details include:
+ **Allocated Amount** - Total amount in the allocation
+ **Remaining Amount** - Unused amount still available
+ **Utilized Amount** - Amount already consumed
+ **Issuance Details (if applicable)** - Purchase order information for the allocation

Consumable allocations enable partners to draw down funds as needed for eligible activities, with real-time tracking of remaining balance.

### Access Details (ACCESS Type)
<a name="access-details"></a>

For access grants, the fulfillment details include:
+ **Description** - Detailed explanation of the access being granted and how to utilize it

Access allocations might provide access to preview services, specialized tools, or restricted resources. The description field provides instructions on how partners can activate and use the granted access.

## Applying Allocations to New Benefit Applications
<a name="applying-allocations-to-new-benefit-applications"></a>

The ApplicableBenefitIds field in benefit allocations identifies other benefits that can leverage this allocation. This enables benefit chaining where partners can use existing allocations to apply for additional benefits.

For example, a partner might:

1. Receive a pre-approved MAP funding allocation

1. Create benefit applications for individual customer migration projects

1. Associate those applications with the pre-approved allocation

1. Draw down funds from the allocation as projects are approved

This approach streamlines the benefit application process for partners with pre-approved funding, reducing the review cycle for individual project requests.