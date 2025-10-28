# Trusted Remediator FAQs

The following are frequently asked questions about Trusted Remediator:

When a non-compliance is identified by Trusted Advisor or a recommendation is issued by Compute Optimizer, Trusted Remediator responds according to your specified preferences, either
by applying remediation,
seeking approval through manual remediations, or reporting the remediations during your upcoming Monthly Business Review (MBR). The remediation happen at
your preferred remediation time or schedule. Trusted Remediator provides you with the ability to self-service and act on Trusted Advisor checks with the flexibility to
configure and remediate checks individually or in bulk. With a library of tested remediation documents, AMS constantly bar raises your accounts by applying
safety checks and following AWS best practices. You are only notified if you specify to do so in your configuration. AMS users can opt-in to Trusted Remediator
at no additional charge.

You have access to Trusted Advisor checks and Compute Optimizer recommendations as part of your existing Enterprise Support plan. Trusted Remediator integrates with Trusted Advisor
and Compute Optimizer to leverage existing AMS
automation capabilities. Specifically, AMS uses AWS Systems Manager automation documents (runbooks) for automated remediations. AWS AppConfig is used to configure
the remediation workflows. You can view all the current and past remediations through the Systems Manager OpsCenter. The remediation logs are stored in an Amazon S3 bucket.
You can use the logs to import and build custom reporting dashboards in Quick Suite.

You own the configurations in your account. Managing your configurations is your responsibility. You can reach out to your CA or CDSM for
help managing your configurations. You can also reach out to AMS through a service request for configuration support, manual remediations, and troubleshooting
remediation failures.

SSM automation documents are automatically shared to onboarded AMS accounts.

AMS owned resources aren't flagged by Trusted Remediator. Trusted Remediator focuses only on your resources.

Trusted Remediator is available for AMS Accelerate customers. For a current list of support Regions, see
[AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/").

Since SSM automation documents directly update resources through the AWS API, resource drift might occur. You can use tags to segregate resources
created through your existing
CI/CD packages. You can configure Trusted Remediator to ignore the tagged resources while still remediating your other resources.

You can turn off Trusted Remediator through the AWS AppConfig application. To pause or stop Trusted Remediator, complete the following steps:

1. Open the AWS AppConfig console at [https://console.aws.amazon.com/systems-manager/appconfig](https://console.aws.amazon.com/systems-manager/appconfig "https://console.aws.amazon.com/systems-manager/appconfig").
2. Select Trusted Remediator.
3. Choose **Settings** on the configuration profile.
4. Select the **Suspend Trusted Remediator** flag.
5. Set the valueof the `suspended` attribute to `true`.

###### Note

Be cautious when using this procedure as this stops Trusted Remediator for all accounts linked to the delegated administrator account.

You can continue to reach out to AMS through Operations On Demand (OOD) for unsupported checks. AMS assists you with remediating these checks.
For more information, see
[Operations On Demand](ops-on-demand.md "ops-on-demand.md").

AWS Config Remediation is another solution that helps you optimize cloud resources and maintain compliance with best practices. The following are some of the
operational differences between the two solutions:

- Trusted Remediator uses Trusted Advisor and Compute Optimizer as the detection mechanisms. AWS Config Remediation uses AWS Config rules as the detection mechanism.
- For Trusted Remediator, remediation happens at your predefined remediation schedule. In AWS Config, remediation happens in real time.
- The parameters for each remediation in Trusted Remediator is easily customizable based on your use case and remediation can be automated or made manual
  by adding tags on resources.
- Trusted Remediator provides reporting functionality.
- Trusted Remediator sends an email notification to you with the list of remediation and the remediation status.
  Some Trusted Advisor checks and Compute Optimizer recommendations might have the same rule in AWS Config. It's a best practice to enable only one remediation if there is a matching AWS Config rule and Trusted Advisor check.
  For information on AWS Config rules for each Trusted Advisor check, see
  [Trusted Advisor checks supported by Trusted Remediator](tr-supported-checks.md "tr-supported-checks.md").

Trusted Remediator deploys the following resources in the Trusted Remediator delegated administrator account:

- An Amazon S3 bucket named `ams-trusted-remediator-{your-account-id}-logs`. Trusted Remediator creates the `Remediation item log` in
  JSON format when a remediation OpsItem is created, and uploads the log files to this bucket.
- An AWS AppConfig application to hold the remediation configurations for supported Trusted Advisor checks and Compute Optimizer recommendations.
  Trusted Remediator doesn't deploy resources in the Trusted Remediator member account.
