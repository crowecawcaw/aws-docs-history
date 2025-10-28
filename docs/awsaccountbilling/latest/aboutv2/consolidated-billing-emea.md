# Consolidated billing in AWS EMEA

The consolidated daily invoice feature combines your charges, so that you receive
fewer invoices each day. You're automatically opted into this feature if you meet the
following requirements:

- Your AWS account is invoiced through the Amazon Web Services EMEA SARL (AWS Europe)
  entity. For more information, see [Managing your payments in AWS Europe](emea-payments.md "emea-payments.md").
- You're using the pay by invoice payment method. This feature isn't available
  for credit card or direct debit payment methods.
  This feature consolidates the following:

- Daily subscriptions and out-of-cycle invoices into one invoice
- Credit memos into one invoice
  For example, if you purchase three Reserved Instances and receive two credit memos
  today, you receive a total of two invoices at the end of the day. One invoice includes
  your Reserved Instance purchases, and the other includes your credit memos.

## Consolidation period

AWS processes subscription invoices and refunds between 23:59 to 24:00 midnight
UTC. AWS then generates the consolidated invoices and credit memos during the
previous 24-hour period. Your consolidated bill is available within minutes.

## Services covered

Your daily invoice includes AWS service subscriptions, out-of-cycle purchases,
and credit memos. This feature doesn't include the following:

- AWS Marketplace purchases
- AWS monthly service and anniversary invoices
- Credit memos issued for different original invoices

For example, suppose that you receive credit memo A for original invoice
ID 123, and another credit memo B for original invoice ID 456. Both credit
memos aren't consolidated, even if they're issued on the same day. Credit
memos are consolidated only if they're issued against the same original
invoice ID.

- AWS Support purchases, such as changing Support plans
- Charges for some Amazon Route 53 offerings (for example, purchasing a domain
  name), AWS Partner Network, AWS Managed Services, and AWS conferences such as re:Invent, and
  re:Inforce

## Currency and foreign

exchange rate

Credit memos use the same currency and exchange rate as the original
invoice.

For subscription invoices, AWS applies the latest currency preference to all
one-time fees processed during the previous 24-hour period. For example, if you
purchase a Reserved Instance in the morning, and then change your preferred currency
in the afternoon, AWS converts the currency for the morning purchase into the new
preferred currency. This update appears in the consolidated invoice generated for
that day.

## Changes to your

AWS Cost and Usage Report

With consolidated billing, it can take up to 24 hours after AWS processes your
one-time charges for them to appear in your AWS Cost and Usage Report (AWS CUR), Cost Explorer, or cost budget
alerts set up using AWS Budgets.

You can continue to view your amortized one-time upfront Reserved Instance charges
in AWS CUR, Cost Explorer, or Budgets.

## Turn off consolidated

billing

By default, this feature is enabled for your account. If you don't want this
feature, use the following procedure.

###### To turn off consolidated billing

1. Sign in to the [AWS Support Center Console](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").
2. Create an **Account & billing** support case.
3. For **Service**, choose
   **Billing**,
4. For **Category**, choose **Consolidated
   Billing**.
5. Follow the prompts to create your support case.

###### Note

Repeat this procedure if you want to turn on consolidated billing
later.
