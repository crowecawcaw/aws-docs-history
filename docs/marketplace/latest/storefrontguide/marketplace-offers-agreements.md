

# Offers and agreements
<a name="marketplace-offers-agreements"></a>

Create private offers and manage agreements, subscriptions, and metering for your connected account.

## Creating offers
<a name="creating-offers"></a>

You can create private offers for specific buyers from the Storefront console. Private offers provide custom pricing, terms, and payment schedules tailored to individual buyer needs.

**Note**  
Private offers aren't supported for discontinued products.

### Prerequisites
<a name="creating-offers-prerequisites"></a>
+ A connected AWS Marketplace seller account
+ At least one active product listing
+ Account Admin or Offer Management role on the connected account.

### Offer types
<a name="creating-offers-types"></a>

The console provides offer generators for each pricing model:


| Generator | Description | 
| --- | --- | 
| SaaS Contract | Fixed-term contract with defined quantities per pricing dimension | 
| SaaS Subscription | Usage-based subscription with pay-as-you-go pricing | 
| AMI | Amazon Machine Image with hourly or annual pricing | 

### To create a private offer
<a name="creating-offers-create"></a>

The offer creation process is a multi-step wizard with Cancel, Prev, and Next controls.

1. In your connected account, choose **Offers**.

1. Choose **Create Offer**.

1. Choose a **Select ISV** value (default Self) and a **Select Product** value.

1. Enter one or more buyer AWS account IDs in **Buyer(s) - AWS account ID(s)** (maximum 24 IDs; your account is added automatically).

1. Enable the **Flexible payment schedule** checkbox to enable fixed units and allow buyers to pay for this product in installments.

1. Choose **Next** to proceed to subsequent wizard steps for pricing, contract duration, EULA, and offer details.

1. Review the offer summary.

1. Choose **Create Offer**.

The offer is created in AWS Marketplace and the buyer receives a notification to review and accept it.

#### Product and pricing
<a name="creating-offers-product-pricing"></a>
+ **Pricing dimensions** - Configure quantities and prices per dimension
+ **Contract duration** - Set the offer duration (monthly, 1-year, 2-year, 3-year)
+ **Payment schedule** - Configure upfront, installment, or on-demand payment

#### Offer details
<a name="creating-offers-details"></a>
+ **Offer name** - Internal name for tracking
+ **Offer expiration** - Date the offer expires if not accepted
+ **EULA** - Attach end-user license agreement (use standard or custom)
+ **Custom fields** - Additional terms or metadata

### Offer statuses
<a name="creating-offers-statuses"></a>


| Status | Description | 
| --- | --- | 
| Pending | Created, waiting for buyer to accept | 
| Accepted | Buyer accepted the offer | 
| Expired | Offer expired before buyer action | 
| Declined | Buyer declined the offer | 

### Related topics
<a name="creating-offers-related"></a>
+ Cloning offers
+ [Downloading offer PDFs](#downloading-offer-pdfs)
+ Offer generators

## Downloading offer PDFs
<a name="downloading-offer-pdfs"></a>

You can download a PDF version of any private offer for record-keeping, internal approvals, or sharing with buyers outside of the AWS Marketplace console.

### To download an offer PDF
<a name="downloading-offer-pdfs-download"></a>

1. Choose **Download PDF** from the actions menu.

1. In the **Download PDF** dialog, Offer Details (Overview; Pricing and payment; customer contact information) is included by default and cannot be disabled.

1. Optionally choose **Metadata**, **EULA and Terms of Service**, or **Buyer Instructions**.

1. Choose **Download**.

### Use cases
<a name="downloading-offer-pdfs-use-cases"></a>
+ **Internal approval workflows** - Share the PDF with finance or legal teams before sending to the buyer.
+ **Record keeping** - Archive accepted offers for audit purposes.
+ **Buyer communication** - Send the PDF to buyer contacts who may not have AWS Marketplace console access.

### Notes
<a name="downloading-offer-pdfs-notes"></a>
+ PDFs reflect the offer state at the time of download.
+ If the offer is modified after download, the PDF becomes outdated. Download a new copy after changes.
+ PDF generation is available for offers in any status.

### Related topics
<a name="downloading-offer-pdfs-related"></a>
+ [Creating offers](#creating-offers)
+ Cloning offers

## Viewing agreements
<a name="viewing-agreements"></a>

The Agreements section shows all active and historical agreements associated with your connected AWS Marketplace account.

### To view agreements
<a name="viewing-agreements-view"></a>

1. Choose the **Agreements** tab in the account top-tab bar (alongside Offers, Offer Templates, Selling Authorizations, and Bundles).

1. The agreement list displays the following columns:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/marketplace/latest/storefrontguide/marketplace-offers-agreements.html)

1. Use the status tabs (**All**, **Active**, **Expired**), the **Search** field, and the **Sync**, **Refresh**, and **Export** controls to find agreements.

### Agreement detail view
<a name="viewing-agreements-detail"></a>

Choose an agreement to open its details in a side drawer. The drawer displays the following fields:
+ Agreement ID
+ Offer ID
+ Proposer ID
+ Acceptor ID
+ Offer Name
+ Product Name
+ Status
+ Agreement type
+ Duration
+ Product Type
+ Offer Accepted On
+ Start Time
+ Ends On
+ Product ID
+ EULA document
+ Auto renewal
+ Purchase Amount
+ AWS listing fee (%)
+ Net
+ Renewal

The drawer also includes a Metadata section.

### Related topics
<a name="viewing-agreements-related"></a>
+ [Viewing active subscriptions](#viewing-active-subscriptions)

## Viewing active subscriptions
<a name="viewing-active-subscriptions"></a>

The Metering section shows all active subscriptions with usage data for your metered products. Opening Metering lands you on the Active Subscriptions tab.

### To view active subscriptions
<a name="viewing-active-subscriptions-view"></a>

1. In your connected account, choose **Metering**.

1. The subscription list displays the following columns:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/marketplace/latest/storefrontguide/marketplace-offers-agreements.html)

1. Use the tabs (**Active Subscriptions**, **All**, **Failed**, **Verified**, **Scheduled**) and the **Search** field to find subscriptions. Choose **\+ Add New** to add a metering record.

### Subscription detail view
<a name="viewing-active-subscriptions-detail"></a>

The detail view shows:


| Section | Information | 
| --- | --- | 
| Overview | Subscription ID, buyer, product, status, dates | 
| Usage | Current period usage by dimension | 
| Metering history | Previous submissions with timestamps and amounts | 
| Billing | Invoiced amounts and payment status | 

### Notes
<a name="viewing-active-subscriptions-notes"></a>
+ Active subscriptions reflect real-time data from AWS Marketplace Metering Service.
+ Usage data updates as metering records are submitted (either by your application or via scheduled metering).
+ Subscriptions cancelled by the buyer remain visible with a "Cancelled" status for historical reference.

### Related topics
<a name="viewing-active-subscriptions-related"></a>
+ [Managing scheduled metering](#managing-scheduled-metering)
+ [Viewing agreements](#viewing-agreements)

## Managing scheduled metering
<a name="managing-scheduled-metering"></a>

You can schedule metering submissions for your usage-based products directly from the Storefront console. Scheduled metering automates the process of reporting buyer usage to AWS Marketplace.

### To view scheduled meterings
<a name="managing-scheduled-metering-view"></a>

1. In your connected account, choose **Metering**.

1. Choose the **Scheduled** tab.

1. The list displays the following columns:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/marketplace/latest/storefrontguide/marketplace-offers-agreements.html)

### To create a scheduled metering rule
<a name="managing-scheduled-metering-create"></a>

1. In the **Scheduled** tab, choose **\+ Add New**.

1. The form opens inline. Configure the following fields:
   + **Product Title**
   + **Customer AWS Account ID**
   + **Dimension API ID**
   + **Quantity**

1. Use the **Schedule** toggle to enable a one-time scheduled submission. Use the **Recurring Schedule** toggle to enable repeated submissions at a defined interval.

1. Choose **Submit**.

### To edit a scheduled metering
<a name="managing-scheduled-metering-edit"></a>

1. Choose the scheduled rule.

1. Choose **Edit**.

1. Modify the configuration.

1. Choose **Submit**.

### To pause or resume
<a name="managing-scheduled-metering-pause"></a>

1. Choose the scheduled rule.

1. Choose **Pause** to temporarily stop submissions, or **Resume** to restart.

Paused rules do not submit metering records until resumed.

### Error handling
<a name="managing-scheduled-metering-errors"></a>

If a scheduled metering submission fails:
+ The status changes to **Error**.
+ An error detail message indicates the reason (for example, invalid dimension, subscription cancelled).
+ You receive a notification (if configured).
+ The system retries on the next scheduled interval unless the subscription is no longer valid.

### Notes
<a name="managing-scheduled-metering-notes"></a>
+ Scheduled metering submits to the AWS Marketplace Metering Service on your behalf using your connected account credentials.
+ Metering records must be submitted within 6 hours of the usage event. Ensure your schedule frequency matches your reporting needs.
+ For high-volume metering, consider using the API directly from your application.

### Related topics
<a name="managing-scheduled-metering-related"></a>
+ [Viewing active subscriptions](#viewing-active-subscriptions)
+ Billed revenue