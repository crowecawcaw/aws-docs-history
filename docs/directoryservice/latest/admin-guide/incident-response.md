# Logging and monitoring in AWS Directory Service

As a best practice, monitor your organization to ensure that changes are logged. This
helps you to ensure that any unexpected change can be investigated and unwanted changes can
be rolled back. AWS Directory Service currently supports the following two AWS services, so you
can monitor your organization and the activity that happens within it.

- Amazon CloudWatch - You can use CloudWatch Events with the AWS Managed Microsoft AD directory type. For more
  information, see [Enabling Amazon CloudWatch Logs log forwarding for
  AWS Managed Microsoft AD](ms_ad_enable_log_forwarding.md "ms_ad_enable_log_forwarding.md"). Additionally, you can use CloudWatch
  Metrics to monitor domain controller performance. For more information, see [Determining when to add domain controllers with CloudWatch metrics](ms_ad_monitor_dc_performance.md#scaledcs "ms_ad_monitor_dc_performance.md#scaledcs").
- AWS CloudTrail
  - You can use CloudTrail
    with all AWS Directory Service directory types.
    For more information,
    see [Logging AWS Directory Service API calls using AWS CloudTrail](logging-using-cloudtrail-ads.md "logging-using-cloudtrail-ads.md").
  - You can use CloudTrail
    with AWS Managed Microsoft AD
    in the Directory Service Data API.
    For more
    information,
    see [Logging AWS Directory Service Data API calls using
    AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").
