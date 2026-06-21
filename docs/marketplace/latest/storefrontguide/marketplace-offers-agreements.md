# Offers and agreements

Create private offers and manage agreements, subscriptions, and metering for your connected account.

## Creating offers

You can create private offers for specific buyers from the Storefront console. Private
offers provide custom pricing, terms, and payment schedules tailored to individual buyer
needs.

###### Note

Private offers aren't supported for discontinued products.

### Prerequisites

- A connected AWS Marketplace seller account
- At least one active product listing
- Account Admin or Offer Management role on the connected account.

### Offer types

The console provides offer generators for each pricing model:

| Generator         | Description                                                          |
| ----------------- | -------------------------------------------------------------------- |
| SaaS Contract     | Fixed-term contract with defined quantities per pricing<br>dimension |
| SaaS Subscription | Usage-based subscription with pay-as-you-go pricing                  |
| AMI               | Amazon Machine Image with hourly or annual pricing                   |

### To create a private offer

The offer creation process is a multi-step wizard with Cancel, Prev, and Next controls.

1. In your connected account, choose **Offers**.
2. Choose **Create Offer**.
3. Choose a **Select ISV** value (default Self) and a **Select Product** value.
4. Enter one or more buyer AWS account IDs in **Buyer(s) - AWS account ID(s)** (maximum 24 IDs; your account is added automatically).
5. Enable the **Flexible payment schedule** checkbox to enable fixed units and allow buyers to pay for this product in installments.
6. Choose **Next** to proceed to subsequent wizard steps for pricing, contract duration, EULA, and offer details.
7. Review the offer summary.
8. Choose **Create Offer**.

The offer is created in AWS Marketplace and the buyer receives a notification to
review and accept it.

#### Product and pricing

- **Pricing dimensions** - Configure
  quantities and prices per dimension
- **Contract duration** - Set the offer
  duration (monthly, 1-year, 2-year, 3-year)
- **Payment schedule** - Configure upfront,
  installment, or on-demand payment

#### Offer details

- **Offer name** - Internal name for
  tracking
- **Offer expiration** - Date the offer
  expires if not accepted
- **EULA** - Attach end-user license
  agreement (use standard or custom)
- **Custom fields** - Additional terms or
  metadata

### Offer statuses

| Status   | Description                          |
| -------- | ------------------------------------ |
| Pending  | Created, waiting for buyer to accept |
| Accepted | Buyer accepted the offer             |
| Expired  | Offer expired before buyer action    |
| Declined | Buyer declined the offer             |

### Related topics

- Cloning offers
- [Downloading offer PDFs](#downloading-offer-pdfs "#downloading-offer-pdfs")
- Offer generators

## Downloading offer PDFs

You can download a PDF version of any private offer for record-keeping, internal
approvals, or sharing with buyers outside of the AWS Marketplace console.

### To download an offer PDF

1. Choose **Download PDF** from the actions menu.
2. In the **Download PDF** dialog, Offer Details (Overview; Pricing and payment; customer contact information) is included by default and cannot be disabled.
3. Optionally choose **Metadata**, **EULA and Terms of Service**, or **Buyer Instructions**.
4. Choose **Download**.

### Use cases

- **Internal approval workflows** - Share the
  PDF with finance or legal teams before sending to the buyer.
- **Record keeping** - Archive accepted offers
  for audit purposes.
- **Buyer communication** - Send the PDF to
  buyer contacts who may not have AWS Marketplace console access.

### Notes

- PDFs reflect the offer state at the time of download.
- If the offer is modified after download, the PDF becomes outdated. Download
  a new copy after changes.
- PDF generation is available for offers in any status.

### Related topics

- [Creating offers](#creating-offers "#creating-offers")
- Cloning offers

## Viewing agreements

The Agreements section shows all active and historical agreements associated with your
connected AWS Marketplace account.

### To view agreements

1. Choose the **Agreements** tab in the account top-tab bar (alongside Offers, Offer Templates, Selling Authorizations, and Bundles).
2. The agreement list displays the following columns:

| Column               |
| -------------------- |
| Agreement ID         |
| Offer ID             |
| Status               |
| Offer Accepted On    |
| Agreement Start Date |
| Agreement End Date   |

3. Use the status tabs (**All**, **Active**, **Expired**), the **Search** field, and the **Sync**, **Refresh**, and **Export** controls to find agreements.

### Agreement detail view

Choose an agreement to open its details in a side drawer. The drawer displays the following fields:

- Agreement ID
- Offer ID
- Proposer ID
- Acceptor ID
- Offer Name
- Product Name
- Status
- Agreement type
- Duration
- Product Type
- Offer Accepted On
- Start Time
- Ends On
- Product ID
- EULA document
- Auto renewal
- Purchase Amount
- AWS listing fee (%)
- Net
- Renewal

The drawer also includes a Metadata section.

### Related topics

- [Viewing active subscriptions](#viewing-active-subscriptions "#viewing-active-subscriptions")

## Viewing active subscriptions

The Metering section shows all active subscriptions with usage data for your metered
products. Opening Metering lands you on the Active Subscriptions tab.

### To view active subscriptions

1. In your connected account, choose **Metering**.
2. The subscription list displays the following columns:

| Column       |
| ------------ |
| Agreement ID |
| Offer ID     |
| Proposer ID  |
| Acceptor ID  |
| Offer Name   |
| Product Name |

3. Use the tabs (**Active Subscriptions**, **All**, **Failed**, **Verified**, **Scheduled**) and the **Search** field to find subscriptions. Choose **+ Add New** to add a metering record.

### Subscription detail view

The detail view shows:

| Section          | Information                                      |
| ---------------- | ------------------------------------------------ |
| Overview         | Subscription ID, buyer, product, status, dates   |
| Usage            | Current period usage by dimension                |
| Metering history | Previous submissions with timestamps and amounts |
| Billing          | Invoiced amounts and payment status              |

### Notes

- Active subscriptions reflect real-time data from AWS Marketplace Metering
  Service.
- Usage data updates as metering records are submitted (either by your
  application or via scheduled metering).
- Subscriptions cancelled by the buyer remain visible with a "Cancelled"
  status for historical reference.

### Related topics

- [Managing scheduled metering](#managing-scheduled-metering "#managing-scheduled-metering")
- [Viewing agreements](#viewing-agreements "#viewing-agreements")

## Managing scheduled metering

You can schedule metering submissions for your usage-based products directly from the
Storefront console. Scheduled metering automates the process of reporting buyer usage to
AWS Marketplace.

### To view scheduled meterings

1. In your connected account, choose **Metering**.
2. Choose the **Scheduled** tab.
3. The list displays the following columns:

| Column                  |
| ----------------------- |
| Agreement Identifier    |
| Customer AWS Account ID |
| Product Title           |
| Schedule Start Time     |
| Status                  |
| Records Submitted       |

### To create a scheduled metering rule

1. In the **Scheduled** tab, choose **+ Add New**.
2. The form opens inline. Configure the following fields:

   - **Product Title**
   - **Customer AWS Account ID**
   - **Dimension API ID**
   - **Quantity**

3. Use the **Schedule** toggle to enable a one-time scheduled submission. Use the **Recurring Schedule** toggle to enable repeated submissions at a defined interval.
4. Choose **Submit**.

### To edit a scheduled metering

1. Choose the scheduled rule.
2. Choose **Edit**.
3. Modify the configuration.
4. Choose **Submit**.

### To pause or resume

1. Choose the scheduled rule.
2. Choose **Pause** to temporarily stop
   submissions, or **Resume** to restart.

Paused rules do not submit metering records until resumed.

### Error handling

If a scheduled metering submission fails:

- The status changes to **Error**.
- An error detail message indicates the reason (for example, invalid
  dimension, subscription cancelled).
- You receive a notification (if configured).
- The system retries on the next scheduled interval unless the subscription
  is no longer valid.

### Notes

- Scheduled metering submits to the AWS Marketplace Metering Service on your
  behalf using your connected account credentials.
- Metering records must be submitted within 6 hours of the usage event.
  Ensure your schedule frequency matches your reporting needs.
- For high-volume metering, consider using the API directly from your
  application.

### Related topics

- [Viewing active subscriptions](#viewing-active-subscriptions "#viewing-active-subscriptions")
- Billed revenue
