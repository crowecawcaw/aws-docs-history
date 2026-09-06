

# Using AWS managed views
<a name="access-data-managed-views"></a>

**To choose an AWS managed billing view**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, enable **billing view** mode.

1. From the dropdown list, choose** billing transfer **view.

   The dropdown shows your 10 most recently accessed views. To see all views, choose **See all views** at the bottom of the dropdown menu.

1. From the **Billing vieBilling view** modal, choose either `billing group view` or `billing transfer views`.

1. Use the search bar to filter results across all columns in the table.

   Search for views using these parameters:

   - View name (partial match, starts with)

   - Account ID (exact match)

   - Type (exact match for` BILLING_TRANSFER` or `BILLING_TRANSFER_SHOWBACK`)

   - Billing period (choose month)

1. Select the desired billing view and select **Choose**.

You can analyze billing transfer showback/chargeback views and billing group views in AWS Cost and Usage Report (during beta, only legacy AWS Cost and Usage Report is supported), Cost Explorer, and the **Bills** page.