# Viewing your billing group details

You can use this section to see the different ways you can review your billing group and
pricing plan configurations, as well as your output post-creation.

## Viewing the billing group table

After you create a billing group, you can view the details of the billing group in a
filterable table. You can filter using the following dimensions:

- Billing group name
- Primary account name
- Primary account ID
- Number of accounts
- Pricing plan name

To view the details for each billing group, choose the billing group name in the table. The
billing group that you enabled for the automatic account association feature will have an
**Auto-associate** icon next to the billing group name.

## Viewing your pro forma configurations by billing group

You can use your billing group details to
monitor, analyze, and edit your billing group in AWS Billing Conductor. The billing group details provide a
month-to-date margin analysis, a history of custom line items applied, and the ability to edit and
delete the billing group as needed.

###### To view your billing group details page

1. Sign in to the AWS Management Console and open AWS Billing Conductor at
   [https://console.aws.amazon.com/billingconductor/](https://console.aws.amazon.com/billingconductor/ "https://console.aws.amazon.com/billingconductor/").
2. In the navigation pane, choose **Billing groups**.
3. In the **Billing groups** table, choose the billing group name.

## Viewing your pro forma configurations by linked account

You can review your billing group configurations by linked account, using the account inventory tool in the AWS Billing Conductor console.

###### To view your billing group configurations by linked account

1. Sign in to the AWS Management Console and open AWS Billing Conductor at
   [https://console.aws.amazon.com/billingconductor/](https://console.aws.amazon.com/billingconductor/ "https://console.aws.amazon.com/billingconductor/").
2. In the navigation pane, choose **Account inventory**.
3. In the **Account inventory** table, find your account ID or use the filter to search for the account ID.
4. Choose the account to view the account and billing group configurations.

## Viewing your billing details by custom pricing dimensions

After you create and assign your billing groups and pricing plans, you can view your custom
billing dimensions with usage type granularity for each billing group under management.

Use the following steps to view your billing details in the pro forma domain.

###### To view your pro forma billing details

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Bills**.
3. Choose **Settings** in the top-right corner of **billing
   details**.
4. Enable the **Pro forma data view**.
5. For **Billing group**, choose the billing to analyze.

You can analyze the billing group usage by service and AWS Region to see the cost of that
usage, consistent with the rates defined in AWS Billing Conductor.

You can find the custom line items under the service **AWS Billing Conductor**
on the **Billing details** page.
