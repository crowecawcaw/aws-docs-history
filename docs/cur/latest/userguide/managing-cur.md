# Viewing and managing reports

To view information about your Cost and Usage Report, use the Billing and Cost Management console. To view your report’s
files, you can use the Amazon S3 console.

Use the following procedures to find your report and report files.

###### To view your report details and files

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, under **Legacy Pages**, choose
   **Cost and Usage Reports**.
3. From your list of reports, choose the name of the report that you want to view.
4. On the **Report Details** page, you can view the report’s
   settings.
5. To view the report’s files, note the **Report path prefix** on the
   **Report Details** page.
6. Choose the bucket name listed under **Amazon S3 bucket**. The link opens
   this bucket in the Amazon S3 console.
7. From the list of objects in the bucket, choose the folder named with the first part of
   the **Report path prefix** that you noted in step 5. For example, if your
   **Report path prefix** is
   `example-report-prefix/example-report-name`, then choose the folder
   named **example-report-prefix**.
8. From the list of objects in the folder, choose the folder named with the second part of
   the **Report path prefix** that you noted in step 5. For example, if your
   **Report path prefix** is
   `example-report-prefix/example-report-name`, then choose the folder
   named **example-report-name**. This folder contains your report
   files.
