# Downloading the cost data CSV file

When you want to review comprehensive detail, you can download a comma-separated
values (CSV) file of the cost data that Cost Explorer uses to generate the chart. This
is the same data that appears in the data table under the chart. The data table
sometimes doesn't display the complete dataset that is used for the
chart. For more information, see [Reading the Cost Explorer data table](ce-table.md "ce-table.md").

###### To download a CSV file

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/cost-management/](https://console.aws.amazon.com/cost-management/ "https://console.aws.amazon.com/cost-management/").
2. Configure Cost Explorer to use the options that you want to see in the CSV
   file.
3. Choose **Download CSV**.
   Note the following about the format of the CSV download:

- If you view the CSV file in a table format, the file’s columns represent costs
  and the rows represent time. When compared to the Cost Explorer data table in
  the console, the columns and rows are transposed.
- The file shows data with up to 15 decimal places of precision.
- The file shows dates in the YYYY-MM-DD format.
