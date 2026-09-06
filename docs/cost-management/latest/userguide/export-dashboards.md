

# Exporting dashboards
<a name="export-dashboards"></a>

Dashboards provide flexible export options for offline analysis and sharing. You can export entire dashboards or individual widgets as PDF reports for immediate download, export individual widget data in CSV format for detailed analysis, or schedule automated email delivery of dashboard PDF reports to stakeholders.

## Export options
<a name="w2aab5c28c25b5"></a>
+ **PDF export:** Export your complete dashboard as a PDF file for offline viewing and sharing with stakeholders who don't have AWS console access. You can also export a single widget visualization into a PDF file.
+ **CSV export:** Export data from individual widgets in CSV format file for detailed analysis in spreadsheet applications.

**To export a dashboard as PDF**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Dashboards**.

1. Select the dashboard you want to export.

1. Choose **Actions**, and then choose **Export PDF** from the dropdown list.

1. Wait for PDF preview to load, verify the layout and choose **Export PDF**.

1. The PDF file will be generated and downloaded to your device.

**To export a widget as PDF**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Dashboards**.

1. Open the dashboard you want to export by choosing the dashboard name.

1. Locate the widget you want to export.

1. Open the widget menu (three dots) and select **Export** then **PDF**.

1. Wait for PDF preview to load, verify the layout and choose **Export PDF**.

1. The PDF file will be generated and downloaded to your device.

**Note**  
If a widget contains a large amount of data or uses an extended time range, widget layout may be changed or some data may be excluded from the PDF export to ensure the visual fits within the page boundaries. This is necessary to maintain readability and proper formatting in the PDF document.  
To ensure complete data export:  
Review the PDF preview before finalizing the export
If you notice data is being truncated or excluded, cancel the PDF preview
Edit the widget's time range to a shorter period (e.g., change from yearly to quarterly or monthly view)
Adjust widget filters to reduce the data volume displayed
Preview the PDF again to verify all important data is now included

**Note**  
When exporting a dashboard that contains AWS Budgets report widgets, the PDF includes the budget name, budgeted amount, actual spend, and forecasted amount columns.

**To export widget data as CSV**

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/).

1. In the navigation pane, choose **Dashboards**.

1. Open the dashboard you want to export by choosing the dashboard name.

1. Locate the widget you want to export.

1. Open the widget menu (three dots) and select **Export** then **CSV**.

1. The CSV file will be downloaded to your device.