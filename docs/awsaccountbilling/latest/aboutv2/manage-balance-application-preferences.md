# Managing balance application preferences

Use **Balance application preferences** to configure how your unapplied
credit memos are automatically applied to outstanding invoices. You can access these
settings from the **Payment preferences** page in the AWS Billing and Cost Management
console.

By default, credit memos are applied to the original invoice first, then to future
invoices. You can change this preference at any time to match your organization's internal
payment processes.

## Prerequisites

Balance application preferences are available to AWS accounts that meet the
following criteria:

- The account pays through **electronic funds transfer
  (EFT)**

###### Note

This feature is not available to accounts that pay by credit card or similar
payment methods. If you don't see the **Balance application
preferences** tab, your account might not be eligible due to other
account restrictions.

Before balance application preferences were available, AWS defaulted to
applying credit memos to the original invoice only. When a credit memo is
applied to an invoice, you still receive a complete credit memo and invoice for
each application.

## Understanding credit memo application preferences

When AWS issues a credit memo for your account, the credit memo can be applied to
outstanding invoices automatically based on your selected preference. The following
table describes the available options.

| Preference                                                                                       | Description                                                                                                                                                                                                                                                                                                   |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| *_Apply to original invoice first, then future<br>invoices_<br>• (Recommended – current default) | The credit memo is applied to the invoice it was issued against, if<br>the invoice is still open. Any remaining or unapplied amount is applied<br>to the next eligible future invoices as they are issued.                                                                                                    |
| **Apply to original invoice first, then oldest<br>invoices**                                     | The credit memo is applied to the invoice it was issued against, if<br>the invoice is still open. Any remaining or unapplied amount is applied<br>to your oldest outstanding invoices.                                                                                                                        |
| *_Apply to original invoice<br>only_<br>• (Previous default)                                     | The credit memo is applied to the invoice it was issued against,<br>if the invoice is still open. If the invoice is no longer open, the<br>credit memo remains unapplied. Prior to the additional preferences,<br>the default behavior was to apply the credit memo to the original<br>invoice if it is open. |
| **Apply to future<br>invoices**                                                                  | The credit memo is held and applied to the next eligible future<br>invoices as they are issued.                                                                                                                                                                                                               |
| **Apply to oldest<br>invoices**                                                                  | The credit memo is applied to your oldest outstanding<br>invoices.                                                                                                                                                                                                                                            |

###### Important

Credit memo application preferences apply to credit memos only. They do not
affect AWS promotional credits. For information about promotional credits, see
[Applying AWS credits](useconsolidatedbilling-credits.md "useconsolidatedbilling-credits.md").

Additionally, credit memos issued for AWS Marketplace purchases must be applied to the
original invoice and cannot be redirected to other invoices. Credit memos can only
be applied to invoices belonging to the same seller of record and currency as the
credit memo.

## Changing your credit memo application preference

###### To change your credit memo application preference

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Payment
   preferences**.
3. Choose the **Balance application preferences**
   tab.
4. Under **Credit memo application strategy**, select your
   preferred application method.
5. Choose **Save preferences**.

Your updated preference takes effect immediately and applies to all future credit
memo applications. Credit memos that have already been applied are not affected by
preference changes.

## Viewing credit memo application history

After a credit memo is applied, AWS sends an email notification to the account's
billing contacts (root contact, alternate billing contact, and additional billing
contacts) with details about the application, including:

- The credit memo number and total application amount
- The invoices the credit memo was applied to
- The remaining credit memo balance (if partially applied)
- A link to view your invoices and any remaining unapplied credit
  memos

To view your current unapplied credit memos, see [View remaining invoices, unapplied funds, and payment history](view-payment-info.md "view-payment-info.md").

## How credit memos are applied

When a credit memo is applied based on your preference:

- **Full application** – If the credit
  memo amount is less than or equal to the target invoice balance, the entire
  credit memo is applied.
- **Partial application** – If the credit
  memo amount exceeds a single invoice balance, the credit memo is applied to
  that invoice first. The remaining amount is applied to additional invoices
  based on your preference (future or oldest).
- **Multiple invoices** – If your
  preference involves multiple invoices (for example, oldest invoices), the
  credit memo is applied starting with the oldest invoice until the credit
  memo is fully consumed.

###### Note

If you select "Apply to original invoice only" and the original invoice is
already closed, the credit memo remains unapplied in your account. You can view
unapplied credit memos on the **Unapplied funds** tab of the
**Payments** page.
