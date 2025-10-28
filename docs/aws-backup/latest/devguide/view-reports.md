# Viewing audit reports

You can open, view, and analyze AWS Backup Audit Manager reports using the programs that you
ordinarily use to work with CSV or JSON files. Note that reports for multiple regions or
multiple accounts are only available in CSV format.

Large files are broken up into multiple reports if the total file size exceeds 50 MB. If
the resulting files are over 50 MB, AWS Backup Audit Manager will create additional CSV files
with the remainder of the report.

###### To view a report

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup "https://console.aws.amazon.com/backup").
2. In the left navigation pane, choose **Reports**.
3. Under **Report plan name**, select a report plan by choosing its
   name.
4. Under **Report jobs**, click on the report link to view the
   report.
5. If your report's **Report status** has a dotted underline, choose
   it for information about your report.
6. Choose which report to view by its **Completion time**.
7. Choose the **S3 link**. This opens your destination S3
   bucket.
8. Under **Name**, choose the name of the report that you want to
   view.
9. To save the report to your computer, choose **Download**.
