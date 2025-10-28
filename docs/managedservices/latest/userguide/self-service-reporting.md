# Self-service reports

AWS Managed Services (AMS) self-service reports (SSR) is a feature that collects data from various native
AWS services and provides access to reports on major AMS offerings. SSR provides information that you can use to support operations,
configuration management, asset management, security management, and compliance.

Use SSR to access the reports from the AMS console and report datasets through Amazon S3
buckets (one bucket per account). You can plug the data into your favorite business
intelligence (BI) tool to customize the reports based on your unique needs.
AMS creates this S3 bucket (S3 bucket name: (ams-reporting-data-a<Account_ID>) in your primary AWS Region,
and the data is shared from the AMS control plane hosted in the us-east-1 Region.

###### Important

To access this feature, you must have one of the following roles:

- Multi-Account Landing Zone: **AWSManagedServicesReadOnlyRole**
- Single-Account Landing Zone: **Customer_ReadOnly_Role**

###### Important

**Using custom keys with AWS Glue**

To encrypt your AWS Glue metadata with a customer-managed KMS key, you must perform the following additional steps to allow AMS to aggregate data from the account:

1. Open the AWS Key Management Service console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms "https://console.aws.amazon.com/kms"), and then choose **Customer Managed Keys**.
2. Select the key ID that you plan to use to
   encrypt the AWS Glue metadata.
3. Choose the **Aliases** tab, and then choose **Create alias**.
4. In the text box, enter **AmsReportingFlywheelCustomKey**, and then choose **Create alias**.

###### Topics

- [Internal API operations](internal-apis.md "internal-apis.md")
- [Patch report (daily)](daily-patch-report.md "daily-patch-report.md")
- [Backup report (daily)](daily-backup-report.md "daily-backup-report.md")
- [Incident report (weekly)](weekly-incident-report.md "weekly-incident-report.md")
- [Billing report (monthly)](monthly-billing.md "monthly-billing.md")
- [Aggregated reports](aggregated-reports.md "aggregated-reports.md")
- [AMS self-service reports dashboards](ssr-dashboards.md "ssr-dashboards.md")
- [Data retention policy](data-retention-policy.md "data-retention-policy.md")
- [Offboard from SSR](offboarding-ssr.md "offboarding-ssr.md")
