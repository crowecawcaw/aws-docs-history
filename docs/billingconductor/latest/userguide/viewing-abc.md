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

###### Note

The auto-associate functionality applies only when using Billing Conductor as a standalone service.

## Viewing your pro forma configurations by linked account

This feature is available only when using Billing Conductor as a standalone service, not with billing transfer. You can review your billing group configurations by linked account, using the account inventory tool in the AWS Billing Conductor console.

###### To view your billing group configurations by linked account

1. Sign in to the AWS Management Console and open AWS Billing Conductor at
   [https://console.aws.amazon.com/billingconductor/](https://console.aws.amazon.com/billingconductor/ "https://console.aws.amazon.com/billingconductor/").
2. In the navigation pane, choose **Account inventory**.
3. In the **Account inventory** table, find your account ID or use the filter to search for the account ID.
4. Choose the account to view the account and billing group configurations.

## Viewing your billing details by custom pricing dimensions

After you create and assign your billing groups and pricing plans, you can view your custom
billing dimensions with usage type granularity for each billing group.

Use the following steps to view your billing details in the pro forma domain.

###### To view your pro forma billing details

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, enable **billing view** mode.
3. From the dropdown list, choose **billing transfer** view.

The dropdown shows your 10 most recently accessed views. To see all views, choose **See all views** at the bottom of the dropdown menu. 4. From the **Billing view** modal, choose either `billing group view` or `billing transfer views`. 5. Use the search bar to filter results across all columns in the table.

Search for views using these parameters:

- View name (partial match, starts with)

- Account ID (exact match)

- Type (exact match for `BILLING_TRANSFER` or `BILLING_TRANSFER_SHOWBACK`)

- Billing period (choose month)

6. Select the desired billing view and select **Choose view**.

When using Billing Conductor as a standalone service, you can analyze billing group usage and costs by service and AWS Region through billing group views. The costs reflect the rates defined in your pricing configuration.

You can analyze pro forma usage for AWS Organizations transferring their bills by using billing transfer views of type `Showback/Chargeback`. You can use all available Cost Explorer filters to analyze your billing transfer views.

You can find the custom line items under the service **AWS Billing Conductor**
on the **Billing details** page.
