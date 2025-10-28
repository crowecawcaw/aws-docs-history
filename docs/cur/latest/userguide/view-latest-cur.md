# Viewing the latest report version

AWS updates your Cost and Usage Report at least once a day until your charges are finalized.
When you create a report, you can choose to create new report versions or overwrite the
existing report version with every update.

If you configured your report to create new report versions with every update, then use
the **assemblyId** in the manifest file to find the latest report
files.

###### To view your latest report files when you have multiple report versions

1. Open the Billing and Cost Management console at [https://console.aws.amazon.com/costmanagement/](https://console.aws.amazon.com/costmanagement/ "https://console.aws.amazon.com/costmanagement/").
2. In the navigation pane, under **Legacy Pages**, choose
   **Cost and Usage Reports**.
3. From your list of reports, choose the name of the report that you want to view.
4. On the **Report Details** page, note the **Report path
   prefix**.
5. Choose the bucket name listed under Amazon S3 bucket. The link opens this bucket in the
   Amazon S3 console.
6. From the list of objects in the bucket, choose the folder named with the first part of
   the **Report path prefix** that you noted in step 4. For example, if your
   **Report path prefix** is
   `example-report-prefix/example-report-name`, then choose the folder
   named **example-report-prefix**.
7. From the list of objects in the folder, choose the folder named with the second part
   of the **Report path prefix** that you noted in step 4. For example, if
   your **Report path prefix** is
   `example-report-prefix/example-report-name`, then choose the folder
   named **example-report-name**.
8. Open the folder named with the latest billing period (in the YYYYMMDD-YYYYMMDD
   format).
9. Open the **`example-report-name`-Manifest.json**
   file.
10. At the top of the manifest file, note the **assemblyId**. The
    **assemblyId** value corresponds to the name of the folder with the
    latest report files.
11. Return to the Amazon S3 console page where you’re viewing the folder named with the latest
    billing period.
12. Open the folder named with the **assemblyId** value that you noted in
    step 10. For example, if the **assemblyId** value is
    `20210129T123456Z`, then open the folder named
    **20210129T123456Z/**. This folder contains your latest report
    files.
