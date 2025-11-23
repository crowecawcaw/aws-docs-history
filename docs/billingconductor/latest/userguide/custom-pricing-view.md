# Viewing your pro forma costs on the Bills page

After you create and assign your billing groups and pricing plans, you can view your custom
billing dimensions with usage type granularity for each billing group under management.

Use the following steps to view your billing details in the pro forma domain.

###### To view your pro forma billing details

1. Open the AWS Billing and Cost Management console at
   [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Bills**.
3. In the navigation pane, enable **billing view** mode.
4. From the dropdown list, choose **billing transfer** view.

The dropdown shows your 10 most recently accessed views. To see all views, choose **See all views** at the bottom of the dropdown menu. 5. From the **Billing view** modal, choose either `billing group view` or `billing transfer views`. 6. Use the search bar to filter results across all columns in the table.

Search for views using these parameters:

- View name (partial match, starts with)

- Account ID (exact match)

- Type (exact match for `BILLING_TRANSFER` or `BILLING_TRANSFER_SHOWBACK`)

- Billing period (choose month)

7. Select the desired billing view and select **Choose view**.
   When using Billing Conductor as a standalone service, you can analyze billing group usage and costs by service and AWS Region through billing group views. The costs reflect the rates defined in your pricing configuration.

You can analyze pro forma usage for AWS Organizations transferring their bills by using billing transfer views of type **Showback/Chargeback**. All Cost Explorer filters are available for analyzing your billing transfer views.

You can find the custom line items under the service **AWS Billing Conductor**
on the **Billing details** page.
