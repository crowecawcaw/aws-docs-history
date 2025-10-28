# Downloading an AWS Usage Report

###### Important

On September 15, 2023, the AWS Usage Report will no longer provide access to
usage data older than March 1, 2019. To access such usage data, download historical
usage and save it locally before September 15, 2023. The AWS Usage Report feature
will be unavailable at a later date. We recommend that you use AWS Cost and Usage Reports
instead.

You can download a usage report in XML or CSV format. Your report covers a single
service, based on usage type, operation, and time period. You can also choose how the
data is aggregated.

###### To download a usage report

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, under **Legacy Pages**,
   choose **Cost and Usage Reports**.
3. Under the **AWS Usage Report** section, choose
   **Create a Usage Report**.
4. On the **Download usage report** page, under
   **Services**, choose the service that you want to view
   usage for.
5. Choose the **Usage type**.
6. Choose the **Operation**.
7. Choose the **Time period** for the report. If you choose
   **Custom date range**, you need to specify the
   **Date range** for the report manually.
8. Under **Report granularity**, choose
   **Hourly**, **Daily**, or
   **Monthly**.
9. Choose **Download**, and then choose **XML
   Report** or **CSV Report**.

###### Note

If you download a large report, the content of the report might be truncated.
Check the last row of the downloaded file for warnings or error messages. If the
report is truncated, download smaller reports by choosing a shorter time period.
Another option is to decrease the report granularity from hourly to daily or
monthly.
