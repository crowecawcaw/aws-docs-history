# Monitoring usage and costs in Security Hub

The Usage page helps you understand and manage the costs of running Security Hub across your organization.
From this page, you can view your current costs, see projected monthly costs, explore usage by capability or by account, and find strategies to optimize your spending.

## Who can access the Usage page

The Usage page is available from any account that has Security Hub enabled.
To access it, open the Security Hub console and choose **Usage** under **Settings** in the navigation pane.

###### Important

If your account is a member account in an AWS Organization and a Security Hub delegated administrator has not been designated,
usage data is not available. To view usage data, your organization's management account must designate a delegated administrator.
For more information, see [Designating a delegated administrator in Security Hub](securityhub-v2-set-da.md "securityhub-v2-set-da.md").

The experience differs depending on your account type:

- **Delegated administrator or management account** –
  You see the full Usage page with an Organization Cost Summary, usage by capability, usage by account, and cost optimization strategies.
- **Member account or standalone account** –
  You see an Account Cost Summary with usage by capability for your account only. The **By account** tab is not available because you are viewing a single account.

## Organization and account cost summary

###### Note

Organization cost summary section is visible only from the delegated administrator account or the management account. Member accounts and standalone accounts see an Account cost summary instead.

When you open the Usage page from a delegated administrator or management account, the Organization Cost Summary section displays a high-level overview of your organization's Security Hub costs for the current billing cycle.
This section includes the following:

- **Data last refreshed** –
  The date when Security Hub last refreshed the usage data for your organization.
  Security Hub refreshes this data periodically. If the data is more than 24 hours old when you visit the Usage page, Security Hub automatically triggers a refresh.
  The refresh completes within a few hours, depending on the size of your organization.
  While the data is being refreshed, an alert appears with a message that the data will be available shortly.
- **Current costs** –
  The total amount your organization has incurred for using Security Hub from the start of the current billing cycle through the date the data was last refreshed.
- **Projected monthly costs (30 days)** –
  An estimated monthly cost based on the last 7 days of usage, extrapolated to a full 30-day billing cycle.
  This projection includes both paid and free trial usage to give you a realistic estimate of what your monthly costs would look like.
  Projected costs do not account for any discounts (EDPs) you have negotiated with AWS.
  If your projected costs appear to be lower than your current costs, that means that your usage has been decreasing and based on last 7 day of usage, the 30 day bill is going to be lower than your bill in the current billing cycle.

## Capability view

The Capability view shows your costs and usage across the entire organization, organized by security capability.
Capabilities are organized into three expandable groups. You can expand or collapse each group to see the individual usage types within it.
Each usage type maps directly to a corresponding usage type in AWS Cost Explorer.

**Security Hub essentials plan** –
Monitors your EC2 instances, ECR container images, Lambda functions, IAM users, and IAM roles.
Covers risk and exposure analytics, vulnerability management (powered by Amazon Inspector), security posture management (powered by Security Hub CSPM), and security response.
All of these capabilities are included in the essentials plan at a single per-resource price — you do not need to separately enable or pay for Amazon Inspector or AWS Security Hub CSPM, and you are not double-charged for the underlying service usage.

**Threat analytics** –
Includes CloudTrail management events and data events, network activity, and other logs.
These capabilities cover threat detection powered by Amazon GuardDuty.

**Additional capabilities** –
Includes Lambda functions code scan.
This is an optional enhancement powered by Amazon Inspector for analyzing Lambda function application code for security vulnerabilities.

For more information about pricing for each capability, see
[Security Hub pricing](https://aws.amazon.com/security-hub/pricing/ "https://aws.amazon.com/security-hub/pricing/").

The table in this view includes the following columns for each usage type:

- **Current usage** –
  The total usage volume for this usage type from the start of the billing cycle through the date the data was last refreshed, across all accounts and all regions.
- **Free usage** –
  The total usage volume for this usage type from accounts that are currently in the free trial.
  Free usage values appear in green.
- **Current costs** –
  The total cost for this usage type from the start of the billing cycle through the date the data was last refreshed, across all accounts and all regions.
- **Free trial value** –
  The cost you would have incurred for this usage type if the accounts currently in the free trial were not in the trial.
  This helps you understand the value of the free trial.
- **Projected monthly costs (30 days)** –
  The estimated monthly cost for this usage type, extrapolated from the last 7 days of usage across all accounts and all regions.
  This includes both paid and free trial usage to provide an estimated monthly cost.

## Account view

###### Note

The **account** view is available only from the delegated administrator account or the management account.

Choose the **account** view to view your costs organized by individual member accounts across all regions.
This view helps you identify which accounts are driving the most cost.

The table lists each account with the following columns:

- **Account** –
  The AWS account ID, displayed as a clickable link. Choosing an account opens a detailed breakdown panel.
- **Current costs** –
  The total cost for this account from the start of the billing cycle through the date the data was last refreshed, across all regions.
- **Free trial value** –
  The cost this account would have incurred if it were not in the free trial.
- **Projected monthly costs (30 days)** –
  An estimated monthly cost for this account, extrapolated from the last 7 days of usage across all regions to a full 30-day billing cycle.
  The projection includes both paid and free trial usage to provide a representative estimate of your monthly costs.
  Projected costs do not account for any discounts you have negotiated with AWS (EDPs).

If Security Hub was enabled on this account within the last 7 days, the projection is based on the number of days since enablement. After 7 days, the projection uses the full last 7 days of usage.
The Usage page does not currently detect when Security Hub has been disabled on an account. If Security Hub has recently been disabled on one or more accounts, those accounts continue to appear in the projection until their usage ages out. Allow 7 days after making these changes for the projection to reflect the updated state of your organization.

### Account detail view

When you choose an account from the list, a detail panel opens on the right side of the page.
This panel shows the same capability-level breakdown as the Capability view, but filtered to that specific account.
You can see the current usage, free usage, current costs, free trial value, and projected monthly costs for each usage type within that account, across all regions.

## Cost optimization strategies

Choose **Cost optimization strategies** on the Usage page to navigate to a dedicated page with actionable ways to manage your costs while maintaining your security coverage.

Each strategy is presented as an independent option that you can evaluate and apply based on your organization's needs.
Options without security tradeoffs are listed first.
After applying any strategy, changes typically take 24 to 48 hours to reflect in your billing.

## Related resources

- [Security Hub pricing](https://aws.amazon.com/security-hub/pricing/ "https://aws.amazon.com/security-hub/pricing/")
- [AWS Cost Explorer User Guide](../../../cost-management/latest/userguide.md "../../../cost-management/latest/userguide.md")
