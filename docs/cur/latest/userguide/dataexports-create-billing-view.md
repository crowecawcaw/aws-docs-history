# Creating exports with billing views

When you sign in as a bill transfer account using billing transfer, or as a management account using AWS Billing Conductor, you can create an export based on your AWS managed billing views (billing groups and billing transfer views).

###### Important

- Custom billing views aren't supported.
- AWS Cost and Usage Report 2.0 isn't supported for billing transfer.
- You can create billing view-based reports only from the Data Exports page. The legacy Cost and Usage Reports page doesn't support creating reports based on billing views.
  You can create reports based on billing views whether billing view mode is enabled or disabled, because reports are resources of your account.

###### To create a report based on billing views

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Data Exports**.
3. Choose **Create report**.
4. Choose the billing view type (managed views only).
5. Choose the specific view for your report.
6. Complete the remaining steps to create your report.

###### Note

When creating a report based on a billing transfer showback/chargeback view or billing group view, you must disable the Split Cost Allocation Data functionality.

For more information about Data Exports for billing transfer use cases, see [billing transfer best practices](../../../awsaccountbilling/latest/aboutv2/orgs_transfer_billing-best-practices.md "../../../awsaccountbilling/latest/aboutv2/orgs_transfer_billing-best-practices.md").
