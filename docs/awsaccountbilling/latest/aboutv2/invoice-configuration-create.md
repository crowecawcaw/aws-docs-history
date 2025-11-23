# Creating invoice units with

AWS invoice configuration

Invoice units are groups of mutually exclusive member accounts within a single AWS Organization that you create. You can create these invoice units so that they correspond to your business entities. Invoice units can be used to separate your AWS costs and configure which member account receives the invoice for each invoice unit going forward.

There are currently some limitations when creating invoice units:

- You can't change the invoice receivers or invoice unit name after you create
  an invoice unit. An AWS account can only be a part of one invoice unit's rule
  at a time. However, a given account can be a receiver for multiple invoice
  units.
- An account can't be a member of an invoice unit and a receiver for another
  invoice unit, unless it's the invoice receiver of both units.
- You can only create invoice units within a single payer account or
  organization.
- AWS invoice configuration doesn't automatically add new accounts to invoice units.
  Once new accounts are created, you must manually add this to an invoice unit, or
  use the [AWS Invoicing APIs](../../../aws-cost-management/latest/APIReference/API_Operations_AWSInvoicing.md "../../../aws-cost-management/latest/APIReference/API_Operations_AWSInvoicing.md").
- You can only consolidate invoices on a payer account level, and not on an
  invoice unit level.
  For more information about the number of invoice units that you can create for each
  payer account, or character limits to an invoice unit name, see [AWS invoice configuration](billing-limits.md#limits-invoicing "billing-limits.md#limits-invoicing").

###### Note

Prerequisite: To add invoice receivers, see [Adding additional billing contact
email addresses](manage-payment-method.md#manage-billing-contact-emails "manage-payment-method.md#manage-billing-contact-emails").

###### To create invoice units within your

management account (standard invoice configuration)

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Invoice
   configuration**.
3. In the **Invoice units** section, choose **Create
   invoice unit**.
4. For **Invoice unit name**, enter a unique name that's
   distinctive within your AWS account. For details on allowed characters, see
   [AWS invoice configuration](billing-limits.md#limits-invoicing "billing-limits.md#limits-invoicing").
5. (Optional) For **Invoice unit description**, enter your
   description summary.
6. In the **Invoice receiver** section, choose the account
   receives invoices related to this invoice unit. Choose either the payer or
   member account as the invoice receiver.

###### Note

The invoice receiver isn't a member of an invoice unit by default. If you
choose a payer account as the invoice unit member, the payer account must be
the invoice receiver for the invoice unit. 7. Review the invoice receiver details that automatically populate when you
choose your account. These details will appear on your invoice. 8. If the invoice issuer is `Amazon Web Services, Inc.`, you can choose to
inherit the invoice receiver's tax settings by choosing the **Apply tax
settings to all accounts in invoice unit** checkbox.

To confirm your tax settings are now inherited from the invoice unit instead
of the payer account, see the **Tax settings** page in the
console.

    * If the payer account is enabled for tax inheritance, the invoice unit
     members inherit the tax settings of the payer account.
    * If the invoice issuer isn't `Amazon Web Services, Inc.`, invoice unit
     members inherit the tax settings of the invoice receiver
     automatically.

9. In the **Accounts** section, select the accounts to add to
   the invoice unit.
10. Choose **Create invoice unit**.
    The configuration is effective immediately once you create an invoice unit.

###### To create invoice units across external management accounts (Billing Transfer)

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Invoice
   configuration**.
3. In the **Invoice units** section, choose **Create
   invoice unit**.
4. For **Invoice unit name**, enter a unique name that's
   distinctive within your AWS account. For details on allowed characters, see
   [AWS invoice configuration](billing-limits.md#limits-invoicing "billing-limits.md#limits-invoicing").
5. In the **Invoice receiver** section, choose the account
   receives invoices related to this invoice unit. Choose either the payer or
   member account as the invoice receiver.
6. Under the **Invoice units content** table choose **Add contents**.

This opens a panel where you can see both accounts and billing transfers. 7. Choose the **Billing transfers** tile, and choose the transfers to include in your invoice unit.

You can remove items individually or in bulk from the contents table. 8. Choose **Create invoice unit**.
You can find the new invoice unit on the **invoice configuration** page. Choose the unit name to view its details or choose **Edit** to make changes. The invoice configuration page includes a snapshot history that shows billing transfers within each invoice unit for specific date ranges. The **Billing Transfers** tab displays all transfers and their associated invoice units.
