# Create a usage report in License Manager

When you create a usage report you specify a self-managed license type for License Manager to
track, a frequency interval that defines how often to generate reports, and a report
type. All reports are generated in CSV format and published to an S3 bucket. A usage
report can produce one or more of following report types.

**Self-managed license summary report**

This report type contains information on the number of consumed licenses
and details about self-managed license. The tracked self-managed license
type is listed with details such as the license count, license rules, and
the distribution of licenses across different resource types.

**Resource usage report**

This report type gives you details about your tracked resources and their
license consumption. Each tracked resource using the specified self-managed
license type is listed with details such as the license ID, the status of
the resource, and the AWS account ID that owns the resource.

###### To create a usage report

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. From the navigation panel choose **Usage reports**.
3. Choose **Create usage report**, then from the
   **Create usage report** pane define the parameters for the
   report:
   1. Enter a **Name** and optional
      **Description** for your usage report.
   2. Select a self-managed license type from the drop down list. This is
      the type of license that the usage report will be generating data
      on.
   3. Choose the report types to generate.
   4. Choose the frequency by which License Manager will publish the reports, you can
      choose **Once every 24 hours**, **Once every 7
      days** or **Once every 30 days**.
   5. (Optional) Add **Tags** to track the usage report
      resource.

4. Select **Create usage report**.
   A new usage report will begin publishing reports within 60 minutes or less.

If you do not already have an S3 bucket associated with your account, License Manager will
create a new Amazon S3 bucket in your account when you create a usage report. If you have
previously enabled **Cross-account inventory search** reports will be
sent to the S3 bucket created by License Manager when **Cross-account inventory
search** was enabled.

Reports are stored in your bucket with the following Amazon S3 URI pattern:

```
s3://aws-license-manager-service-`*`/Reports/`usage-report-name`/`year`/`months`/`day`/`report-id`.csv
```
