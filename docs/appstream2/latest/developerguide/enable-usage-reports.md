# Enable AppStream 2.0 Usage Reports

To receive usage reports, you subscribe to them by using the AppStream 2.0 console, the
AWS Command Line Interface (AWS CLI), or the `CreateUsageReportSubscription`
API operation. You must enable usage reports separately for each AWS Region for which you want to receive usage data.

###### Note

You can start or stop your subscription to usage reports at any time. There is no charge for subscribing to usage reports, but standard Amazon S3 charges may apply to reports that are stored in your S3 bucket. For more information, see [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").

To subscribe to usage reports for AppStream 2.0 by using the AppStream 2.0 console, perform the following
steps.

1. Open the AppStream 2.0 console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. Choose the AWS Region for which you want to enable usage reports.
3. In the navigation pane, choose **Usage Reports**.
4. Choose **Enabled**, and then choose **Apply**.
   If you enabled on-instance session scripts and Amazon S3 logging for your session script
   configuration, AppStream 2.0 created an S3 bucket to store the script output. The bucket is
   unique to your account and Region. When you enable usage reporting in this case, AppStream 2.0
   uses the same bucket to store your usage reports. If you haven't already enabled on-instance session scripts,
   when you enable usage reports, AppStream 2.0 creates a new S3 bucket in the following
   location:

```
appstream-logs-`region-code`-`account-id-without-hyphens`-`random-identifier`
```

**`region-code`**

The AWS Region code for the Region in which usage reporting is
enabled.

**`account-id-without-hyphens`**

Your Amazon Web Services account identifier. The random ID ensures that there is no
conflict with other buckets in the same Region. The first part of the bucket
name, `appstream-logs`, does not change across accounts or
Regions.

For example, if you enable usage reporting in the US West (Oregon) Region (us-west-2)
on account number 123456789012, AppStream 2.0 creates an Amazon S3 bucket within your account in
that Region similar to the name shown in the following example:

```
appstream-logs-us-west-2-1234567890123-abcdefg
```

Only an administrator with sufficient permissions can delete this bucket.

###### Topics

- [AppStream 2.0 Sessions Reports](usage-report-types-sessions-reports.md "usage-report-types-sessions-reports.md")
- [AppStream 2.0 Applications Reports](usage-report-types-applications-reports.md "usage-report-types-applications-reports.md")
