# Viewing and managing data exports

To view details about your exports, use the **Data Exports** page in the AWS Billing and Cost Management
console. To view your export files, use the S3 console link for your Amazon S3 bucket on the
**Data Exports** page. To view your export dashboards, use the QuickSight link on the
**Data Exports** page, or go directly to the QuickSight console and find your
dashboard.

###### To view your export details, files, and dashboards

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, choose **Data Exports**.
3. In the **Exports and dashboards** list, find the name of the export
   that you want to view.
4. To view the export details, choose the link in the **Export name**
   column to view the summary page describing the export settings.
5. To view the export files, choose the link in the **S3 bucket** column
   to be brought to the S3 console for your bucket.
6. To view the QuickSight dashboard, choose the **Cost and usage
   dashboard** link in the **Export type** column.
   The following is an overview of the columns in the **Exports and
   Dashboards** list:

- **Export name**: The name you chose when creating the export.
- **Status**: The health of your export. It can have two values:
  - **Healthy**: This status indicates that the most recent export
    delivery was successful.

  ###### Note

  Your Cost and Usage Dashboard could be missing the data for the current month
  because it can take up to 24 hours for all your data to be populated in your
  dashboard. If the export status says “Healthy”, allow 24 hours for your dashboard to
  update with the current month's data.

  When you use billing transfer as a bill transfer account, or AWS Billing Conductor as a management account, you can see all billing view-based exports with billing view mode disabled. When you enable billing view mode, you can see only exports associated with the selected billing view.
  - **Unhealthy**: This status indicates that the most recent export
    delivery failed.

- **Export type**: The type of export created. Data Exports has three types of
  exports:
  - **Standard data export**: A customized export of a table that
    delivers to Amazon S3 on a recurring basis.
  - **Cost and usage dashboard**: An export and integration to Amazon
    QuickSight that deploys a pre-built cost and usage dashboard. This becomes a link to a
    dashboard.
  - **Legacy CUR export**: An export of the Legacy Cost and Usage
    Report (CUR).

- **Data table**: The table that your export is querying.
- **Date created**: The time and date when your export was
  created.
- **Date last refreshed**: The time and date when your export was last
  refreshed.
- **S3 bucket**: The S3 bucket to which your export is being delivered
  to.
