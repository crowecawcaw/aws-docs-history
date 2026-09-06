

# Self-service reports
<a name="self-service-reporting"></a>

AWS Managed Services (AMS) self-service reports (SSR) is a feature that collects data from various native AWS services and provides access to reports on major AMS offerings. SSR provides information that you can use to support operations, configuration management, asset management, security management, and compliance.

Use SSR to access the reports from the AMS console and report datasets through Amazon S3 buckets (one bucket per account). You can plug the data into your favorite business intelligence (BI) tool to customize the reports based on your unique needs. AMS creates this S3 bucket (S3 bucket name: (ams-reporting-data-a<Account\_ID>) in your primary AWS Region, and the data is shared from the AMS control plane hosted in the us-east-1 Region.

To allow your users to view AMS Accelerate reports in the AMS console, you must grant explicit permissions in AWS Identity and Access Management (IAM) to perform those actions. For example IAM policies, see [Permissions to use AMS features](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-access-customer.html).

**Important**  
**Using custom keys with AWS Glue**  
To encrypt your AWS Glue metadata with a customer-managed KMS key, you must perform the following additional steps to allow AMS to aggregate data from the account:  
Open the AWS Key Management Service console at [https://console.aws.amazon.com/kms](https://console.aws.amazon.com/kms), and then choose **Customer Managed Keys**.
Select the key ID that you plan to use to encrypt the AWS Glue metadata.
Choose the **Aliases** tab, and then choose **Create alias**.
In the text box, enter **AmsReportingFlywheelCustomKey**, and then choose **Create alias**.

**Topics**
+ [Internal API operations](internal-apis.md)
+ [Patch report (daily)](daily-patch-report.md)
+ [Backup report (daily)](daily-backup-report.md)
+ [Incident report (weekly)](weekly-incident-report.md)
+ [Billing report (monthly)](monthly-billing.md)
+ [Aggregated reports](aggregated-reports.md)
+ [AMS self-service reports dashboards](ssr-dashboards.md)
+ [Data retention policy](data-retention-policy.md)
+ [Offboard from SSR](offboarding-ssr.md)