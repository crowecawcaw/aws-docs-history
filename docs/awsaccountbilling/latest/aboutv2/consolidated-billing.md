# Consolidating billing for AWS Organizations

You can use the consolidated billing feature in AWS Organizations to consolidate billing and
payment for multiple AWS accounts. Every
organization in AWS Organizations has a _management account_ that pays the charges
of all the _member accounts_. For more information about organizations,
see the [AWS Organizations User Guide](../../../organizations/latest/userguide.md "../../../organizations/latest/userguide.md").

Consolidated billing has the following benefits:

- **One bill** – You get one bill for multiple
  accounts in the same SOR. If an organization has accounts from multiple SORs, you
  receive one bill per SOR.
- **Easy tracking** – You can track the charges
  across multiple accounts and download the combined cost and usage data.
- **Combined usage** – You can combine the usage
  across all accounts in the organization to share the volume pricing discounts,
  Reserved Instance discounts, and Savings Plans. This can result in a lower charge for your
  project, department, or company than with individual standalone accounts. For more
  information, see [Volume discounts](useconsolidatedbilling-effective.md#useconsolidatedbilling-discounts "useconsolidatedbilling-effective.md#useconsolidatedbilling-discounts").
- **No extra fee** – Consolidated billing is
  offered at no additional cost.

###### Note

The member account bills are for informational purpose only. The management account
might reallocate the additional volume discounts, Reserved Instance, or Savings Plans discounts
that your account receives.

If you have access to the management account, you can see a combined view of the AWS
charges that the member accounts incur. You also can get a cost report for each member
account.

###### Important

When a member account leaves an organization, the member account can no longer access
Cost Explorer data that was generated when the account was in the organization. The
data isn't deleted, and the management account in the organization can still access the
data. If the member account rejoins the organization, the member account can access the
data again.

###### Topics

- [Consolidated billing process](useconsolidatedbilling-procedure.md "useconsolidatedbilling-procedure.md")
- [Consolidated billing in AWS EMEA](consolidated-billing-emea.md "consolidated-billing-emea.md")
- [Consolidated billing in India](useconsolidatedbilling-India.md "useconsolidatedbilling-India.md")
- [Effective billing date, account
  activity, and volume discounts](useconsolidatedbilling-effective.md "useconsolidatedbilling-effective.md")
- [Reserved Instances](ri-behavior.md "ri-behavior.md")
- [Understanding Consolidated Bills](con-bill-blended-rates.md "con-bill-blended-rates.md")
- [Requesting shorter PDF
  invoices](consolidated-invoice-summary-options.md "consolidated-invoice-summary-options.md")
- [Support charges for accounts in an
  AWS Organizations](consolidatedbilling-support.md "consolidatedbilling-support.md")
