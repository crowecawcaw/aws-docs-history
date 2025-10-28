# Accessing cost management data using custom

billing views

If your account has access to a custom billing view, you can access the cost management data
defined in that custom billing view. This is in addition to the cost management data owned by
your account, which is contained in your primary billing view. The primary billing view supports
all AWS Billing and Cost Management tools. To access the data in a custom billing view, you
can use either Cost Explorer or the AWS Billing and Cost Management home page. Cost Explorer
offers additional functionality with custom billing views, allowing you to create forecasts and
access Cost Explorer Saved Reports based on the data.

###### To choose a custom billing view

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, select the **Choose billing view** menu. The
   default selection is the **Primary view**, which represents cost management
   data for the account you're currently logged in to.
3. From the **Custom views** section of the dropdown list, choose the
   custom billing view you want to use for accessing cost management data.
4. If the custom billing view you want to access is not listed, choose **See all
   views** to open the **Billing views** dialog box.
5. Use the **Find view name** search field to filter the custom billing
   views in the **Billing views** table.
6. Once you find the custom billing view you want to access, select it and choose
   **Choose**.
   Once you choose a custom billing view, the contents of the AWS Billing and Cost Management
   console are refreshed to reflect the cost management data defined in the chosen custom billing
   view. The console navigation pane refreshes to display only those tools supported by the chosen
   custom billing view. Navigating to a different AWS Billing and Cost Management tool will
   maintain the currently chosen custom billing view.

###### Note

- Not all widgets on the AWS Billing and Cost Management home page support custom
  billing views. Cost management data included in the selected custom billing view is shown
  in the “Cost summary”, “Cost breakdown”, and “Cost allocation coverage” widgets. The
  “Recommended actions”, “Savings opportunities”, and “Cost monitor” widgets don't display
  recommended actions, savings opportunities, or cost monitors when accessing a custom
  billing view.
- The **Choose billing view** dropdown menu only displays custom
  billing views and the primary billing view. It doesn’t display billing group billing
  views. To access cost management data contained in a billing group billing view, see
  [Viewing your billing group details](../../../billingconductor/latest/userguide/viewing-abc.md "../../../billingconductor/latest/userguide/viewing-abc.md") in the _AWS Billing
  Conductor User Guide_. You can also access all available billing views using
  the [ListBillingViews](../../../aws-cost-management/latest/APIReference/API_billing_ListBillingViews.md "../../../aws-cost-management/latest/APIReference/API_billing_ListBillingViews.md") API.
