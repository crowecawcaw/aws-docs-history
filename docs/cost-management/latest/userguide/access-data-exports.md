# Viewing and creating exports using billing views

AWS Cost Management Data Export supports primary, billing group, and billing transfer views that help you generate detailed cost and usage reports. You can filter data across multiple accounts in your organization. When you create a data export, you can choose a billing view to define which cost and usage data to include. This enables you to focus on specific departments or projects without requiring access to the management account.

You can customize your exports by choosing specific data dimensions, time periods, and accounts. AWS Cost Management saves all configurations for future use. The service automatically delivers exported data to your specified Amazon Simple Storage Service bucket on a schedule, enabling integration with external analysis tools.

###### To view or create an export using a billing view

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, enable **Billing Views**. The default
   selection is the **Primary view**, which represents cost management data
   for the account you're currently logged in to.
3. From the dropdown list, choose the billing view you want to use:
   - **Primary view**: Shows cost management data for your current
     account.
   - **Billing Group views**: Shows cost management data for accounts included in billing groups via .
   - **Billing Transfer views**: Shows cost management data for accounts that have transferred their AWS billing responsibility to you.

4. In the navigation pane, choose **Data Exports**.
5. For existing exports, the exports list displays only the exports created using the
   selected billing view.
6. For a new export, choose **Create export**, and then
   follow the export creation workflow. The selected billing view is automatically applied to
   the new export.

###### Note

Custom billing views are not currently supported for Data Exports. All other billing view types are supported.
