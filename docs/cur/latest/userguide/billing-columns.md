# Billing details

Columns under the **bill** header in AWS Cost and Usage Reports are
static fields that appear in all Cost and Usage Reports. You can use the billing line items in the
report to find details about the specific bill covered by the report, such as the charge
type and the beginning and end of the billing period. This includes the following
columns:

A | [B](#b-B "#b-B") | C | D | E | F | G | H | [I](#b-I "#b-I") | J | K | L | M | N | O | [P](#b-P "#b-P") | Q | R | S | T | U | VWXYZ

## B

### bill/BillingEntity

Helps you identify whether your invoices or transactions are for AWS Marketplace or for
purchases of other AWS services. Possible values include:

- **AWS** – Identifies a transaction for AWS
  services other than in AWS Marketplace.
- **AWS Marketplace** – Identifies a purchase in
  AWS Marketplace.

### bill/BillingPeriodEndDate

The end date of the billing period that is covered by this report, in UTC. The
format is `YYYY-MM-DDTHH:mm:ssZ`.

### bill/BillingPeriodStartDate

The start date of the billing period that is covered by this report, in UTC.
The format is `YYYY-MM-DDTHH:mm:ssZ`.

### bill/BillType

The type of bill that this report covers. There are three bill types:

- **Anniversary** – Line items for services that
  you used during the month
- **Purchase** – Line items for upfront service
  fees
- **Refund** – Line items for refunds

## I

### bill/InvoiceId

The ID associated with a specific line item. Until the report is final, the
**InvoiceId** is blank.

### bill/InvoicingEntity

The AWS entity that issues the invoice. Possible values include:

- **Amazon Web Services, Inc.** – The entity
  that issues invoices to customer globally, where applicable.
- **Amazon Web Services India Private Limited**
  – The entity that issues invoices to customers based in
  India.
- **Amazon Web Services South Africa Proprietary
  Limited** – The entity that issues invoices to
  customers in South Africa.

## P

### bill/PayerAccountId

The account ID of the paying account. For an organization in AWS Organizations, this is
the account ID of the management account.
