# Billing Transfer FAQ for AWS Marketplace Buyers

Billing transfer allows a management account to designate an external management account to manage and pay for its consolidated bill. This centralizes billing while maintaining security management autonomy. To set up billing transfer, an external account (bill transfer account) sends a billing transfer invitation to a management account (bill source account). If the invitation is accepted, the external account becomes the bill transfer account. The bill transfer account then manages and pays for the bill source account's consolidated bill, starting on the date specified in the invitation.

This FAQ addresses common questions for buyers who have a bill transfer account and purchase products from sellers on AWS Marketplace.

###### Topics

- [I'm in a billing transfer relationship with an AWS Solution Provider or Distributor. How does this affect my AWS Marketplace purchases?](#billing-transfer-marketplace-purchases "#billing-transfer-marketplace-purchases")
- [Who is responsible for paying my AWS Marketplace invoices when using billing transfer?](#billing-transfer-payment-responsibility "#billing-transfer-payment-responsibility")
- [When is billing transfer effective for marketplace purchases?](#billing-transfer-effective-date "#billing-transfer-effective-date")
- [What happens to my Purchase Order (PO) numbers when I make marketplace purchases when using billing transfer?](#billing-transfer-purchase-orders "#billing-transfer-purchase-orders")
- [Can my AWS Solution Provider or Distributor prevent my PO from appearing on their invoice when using billing transfer?](#billing-transfer-po-prevention "#billing-transfer-po-prevention")
- [Should I coordinate with my Channel Partner before making marketplace purchases when using billing transfer?](#billing-transfer-coordination "#billing-transfer-coordination")
- [Can I still see the costs of my AWS Marketplace purchases when using billing transfer?](#billing-transfer-cost-visibility "#billing-transfer-cost-visibility")
- [Will I have access to the Procurement Insights dashboard when using billing transfer?](#billing-transfer-procurement-insights "#billing-transfer-procurement-insights")
- [How can I track my marketplace spending when using billing transfer?](#billing-transfer-spending-tracking "#billing-transfer-spending-tracking")
- [Whose tax profile is used for my marketplace purchases when using billing transfer?](#billing-transfer-tax-profile "#billing-transfer-tax-profile")
- [How does using billing transfer affect tax exemptions for my purchases?](#billing-transfer-tax-exemptions "#billing-transfer-tax-exemptions")
- [Are there any tax-related considerations I should be aware of when using billing transfer?](#billing-transfer-tax-considerations "#billing-transfer-tax-considerations")
- [Who receives purchase confirmations and notifications when using billing transfer?](#billing-transfer-notifications "#billing-transfer-notifications")
- [Who do I contact if I have issues with my marketplace purchases when using billing transfer?](#billing-transfer-support "#billing-transfer-support")
- [What if I need to dispute a marketplace charge when using billing transfer?](#billing-transfer-disputes "#billing-transfer-disputes")
- [How should I handle subscription renewals or cancellations when using billing transfer?](#billing-transfer-subscription-management "#billing-transfer-subscription-management")
- [Do I maintain control over my AWS accounts?](#billing-transfer-account-control "#billing-transfer-account-control")
- [What's the best way to manage marketplace purchases with billing transfer?](#billing-transfer-best-practices "#billing-transfer-best-practices")

## I'm in a billing transfer relationship with an AWS Solution Provider or Distributor. How does this affect my AWS Marketplace purchases?

When you purchase products from AWS Marketplace, your invoices are transferred to your channel partner's Bill-Transfer account. Your channel partner becomes responsible for paying for all your marketplace purchases.

## Who is responsible for paying my AWS Marketplace invoices when using billing transfer?

The Bill-Transfer account owner is responsible for paying all your AWS Marketplace purchase invoices when using billing transfer.

## When is billing transfer effective for marketplace purchases?

When you accept a billing transfer request, the request will include an effective date. This effective date can be found in AWS Billing and Cost Management console. After the effective day, you will no longer receive AWS Marketplace purchase invoices directly in your AWS organization.

## What happens to my Purchase Order (PO) numbers when I make marketplace purchases when using billing transfer?

Any PO numbers you enter during marketplace checkout will appear on the final invoice sent to the Bill-Transfer account.

## Can my AWS Solution Provider or Distributor prevent my PO from appearing on their invoice when using billing transfer?

Yes. Channel partners may choose to prevent your PO from appearing on their invoice by implementing Service Control Policies (SCPs).

## Should I coordinate with my Channel Partner before making marketplace purchases when using billing transfer?

Yes. It's best practice to coordinate with your channel partner about Purchase Order requirements before making marketplace purchases.

## Can I still see the costs of my AWS Marketplace purchases when using billing transfer?

Yes, you can continue to use the Procurement insights dashboard to view the agreements and cost information for AWS Marketplace purchases in your organization.

## Will I have access to the Procurement Insights dashboard when using billing transfer?

You will retain access to the Agreements dashboard showing your subscriptions. Your cost analysis capabilities in the Procurement Insights dashboard will use your Bill-Source account identifier rather than the Bill-Transfer account and you will only see spend data for your own AWS organization.

## How can I track my marketplace spending when using billing transfer?

Use the Procurement insights dashboard for each of your AWS organizations independently to manage costs.

## Whose tax profile is used for my marketplace purchases when using billing transfer?

For marketplace purchases, your channel partner's tax profile is used for tax calculations as the invoice is delivered to the Bill-Transfer account.

## How does using billing transfer affect tax exemptions for my purchases?

If tax exemptions are needed, they must be applied to your channel partner's tax profile, as they are the entity being taxed for your marketplace purchases. Coordinate with your channel partner to ensure proper tax exemptions are in place.

## Are there any tax-related considerations I should be aware of when using billing transfer?

Tax calculations for your purchases are based on your channel partner's tax profile. This could potentially affect the tax rates applied to your purchases compared to direct purchases. Discuss any tax implications with your channel partner.

## Who receives purchase confirmations and notifications when using billing transfer?

Purchase confirmations and other notifications related to your marketplace transactions are sent to the Bill-Transfer account controlled by the channel partner.

## Who do I contact if I have issues with my marketplace purchases when using billing transfer?

The support process depends on the type of issue:

- For billing-related questions, contact your channel partner first
- For technical issues with the marketplace product itself, contact the seller
- For platform issues, AWS Support can help resolve billing transfer and AWS Marketplace integration problems

## What if I need to dispute a marketplace charge when using billing transfer?

Since your channel partner receives the invoice, you should work with them to address any billing disputes. They will coordinate with AWS as needed to resolve the issue.

## How should I handle subscription renewals or cancellations when using billing transfer?

You should establish a clear process with your channel partner for handling subscription renewals and cancellations. While you may have administrative control to make these changes, the billing changes impact your channel partner.

## Do I maintain control over my AWS accounts?

Yes. Billing transfer only affects billing relationships. You maintain full control over account access and permissions, resource management, security configurations, and all administrative functions.

## What's the best way to manage marketplace purchases with billing transfer?

Best practices include:

- Coordinating with your Channel Partner about PO requirements
- Establishing clear processes for requesting and approving new software purchases
- Reviewing your agreement terms to understand billing cycles
- Maintaining regular communication about planned purchases to avoid surprise charges
