# Customizing your invoice preferences with

AWS invoice configuration

You can use **AWS invoice configuration** to configure your invoice preferences
so that certain member accounts in your AWS Organization receive invoices corresponding to their, or other member account's charges.

If you use Billing Transfers, you can use invoice configuration to support multiple tax settings and systems of record (SOR) for each organization that transfers bills to you.

**For standard invoice configuration use cases**

You can use invoice configuration so that member accounts receiving invoices accurately represent your organization's business model. As a result, invoice configuration can save you time on manual overhead of chargebacks to your
business entities. You can create groups of accounts that match your AWS
costs to your business entities, and model the billing relationship between your entities,
furthermore streamlining procurement of your AWS services. You have the flexibility to
create invoice units, and add or remove accounts from an invoice unit at any time. These
changes can be done at any time during the month, and changes reflect on the invoice that
you receive at the start of the next month. Your Out of Cycle Bills (OCBs) and subscription
purchase invoices will also be billed to the respective invoice receiver account. Accounts
that aren't a part of invoice units continue to receive AWS invoices the same way as
before, using invoice configuration.

If you've opted in to daily invoice consolidation, you will receive a consolidated daily
invoice that honors the invoice unit preferences that are active at the end of the
day.

Invoice units inherit the payer account's payment method and terms. The management account and member accounts are jointly and severally liable for all charges accrued by the member accounts while joined in AWS Organizations.

To view the invoices, payer account and invoice receiver accounts can download invoices
from the **Bills** page in the Billing and Cost Management console. Invoices are also emailed to
the billing contacts that you configure in the invoice unit. Any refunds or credit memos are
issued to the original account that the invoice is issued to.

**For Billing Transfer invoice configuration use cases**

To use invoice configuration to support multiple tax settings and seller of record (SOR) in billing transfers, create a member account in your Bill Transfer account. Then map one or more transferring organizations (including bill source accounts and all member accounts) to your member accounts under the bill transfer account.

## Key points

You can use Invoice configuration for the following specific features:

**Create invoice units**

You can create invoice units, or sets of mutually exclusive accounts, that
correspond to your business entity. Invoice units are composed of a
designated receiver account and a set of accounts where charges are grouped
under an invoice issued to the receiver. You can use invoice units to
separate your AWS costs and configure your invoice for each business
entity going forward.

**Assign invoice receivers**

You can assign receivers to each of your invoice units. You have the
option to choose either the payer account or another member account to
receive your business entity's invoice.

**Associate purchase orders to each business entity**

You can associate [purchase orders](manage-purchaseorders.md "manage-purchaseorders.md") to each
invoice unit to manage your procure-to-pay processes across business
entities.

**Visualize, analyze, and understand your costs**

You can use Cost Explorer and AWS Cost and Usage Report for each invoice unit to
further analyze your AWS costs.

### Setting up IAM permissions

An AWS Identity and Access Management (IAM) identity, such as a user or role, must have permission to use
the Invoice configuration. To grant access, see [Allow access to AWS invoice configuration in the Billing console](billing-example-policies.md#invoice-config-policy "billing-example-policies.md#invoice-config-policy").

### Quotas

There are some quotas and restrictions that apply to Invoice configuration. See [AWS invoice configuration](billing-limits.md#limits-invoicing "billing-limits.md#limits-invoicing") in the
_Quotas and restrictions_ page for details.

For more information about service quotas, see [AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md") in the _AWS General Reference_.
