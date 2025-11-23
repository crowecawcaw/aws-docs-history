# Returning a purchased Savings Plan

When you purchase a Savings Plan, you make a commitment for one or three years.
However, in the case that you purchase a Savings Plan and quickly identify a purchase
error that you want to rectify, you'll have a limited time period to do so. Any
Savings Plan with an hourly commitment of $100 or less that has been purchased in the
last seven days and in the same calendar month can be returned, provided you haven't
reached your return limit. Once the calendar month ends (UTC time), these purchased
Savings Plans can no longer be returned. For more information about quotas, see [Quotas and
restrictions](sp-quotas.md "sp-quotas.md").

When you return a Savings Plan, you'll receive a 100% refund for any upfront charges
made towards your plan and these refunds will be reflected in your bill within 24 hours
of the return. Any usage that was covered by the plan will be charged at On-Demand rates
or get covered by a different Savings Plan, if applicable.

You can return a Savings Plan using the console or by calling the
`ReturnSavingsPlan` action through the AWS SDK/CLI.

###### To return an active Savings Plan

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, under **Savings Plans**, choose
   **Inventory**.
3. Choose a Savings Plan to open the **Savings Plan details**
   page.
4. Choose **Return Savings Plan**.

###### Note

The **Return Savings Plan** button is only visible in
the details page when a Savings Plan is eligible for return.

When you use billing transfer, the account that purchases Savings Plans must request the return, even when another account pays their bill. 5. In the **Return Savings Plan** dialog box, choose
**Confirm return**.

###### Note

This action can’t be reverted.
You can view returned Savings Plans in the **Savings Plans inventory**
page in the console or by calling the `DescribeSavingsPlans` action in the
AWS SDK/CLI. Returned Savings Plans appear with the status of **Returned**.

## Savings Plan return restrictions

If you submit a request to return a Savings Plan and it is ineligible, you'll
receive an error related to one of the following reasons:

- The limit for your consolidated billing family has been met. If you're
  using a single AWS account, the limit for that account has been
  met.

For more information about quotas, see [Quotas and restrictions](sp-quotas.md "sp-quotas.md").

- The Savings Plan is not in an "active" state. Only Savings Plans that have been
  activated can be returned. To return a “payment-pending” Savings Plan, wait
  for it to activate.
- The hourly commitment is greater than $100.
- The request has been made by a user with insufficient permissions.

###### Note

Only root users or IAM users with the
`savingsplans:returnSavingsPlan` permission can return a
Savings Plan in their account. The AWS managed policy
`AWSSavingsPlansFullAccess` includes that
permission.

- The Savings Plan was purchased in a different month or in the same month
  but more than seven days ago.
- The Savings Plan is an All Upfront or Partial Upfront Savings Plan and
  you are registered under AWS Brazil or AWS Turkey.

For more information about seller of record (SOR), see [Finding the seller of record](../../../awsaccountbilling/latest/aboutv2/finding-the-seller-of-record.md "../../../awsaccountbilling/latest/aboutv2/finding-the-seller-of-record.md").

- The management account is not the same as the management account used when
  purchasing the Savings Plan.
