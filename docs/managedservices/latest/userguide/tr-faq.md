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

You own the configurations in your account. Managing your configurations is your responsibility. You can also reach out to AMS for
configuration changes, support, and manual remediations, and troubleshooting remediation failures.

SSM automation documents are automatically shared to onboarded AMS accounts.

AMS owned resources aren't flagged by Trusted Remediator. Trusted Remediator focuses only on your resources.

Trusted Remediator is available for AMS Advanced customers. For a current list of support Regions, see
[AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/").

Since SSM automation documents directly update resources through the AWS API, resource drift might occur. You can use tags to segregate resources
created through your existing
CI/CD packages. You can configure Trusted Remediator to ignore the tagged resources while still remediating your other resources.

Use the
[Management | Trusted Remediator | State | Enable or disable](../ctref/management-trusted-state-enable-or-disable.md "../ctref/management-trusted-state-enable-or-disable.md") change type to stop the Trusted Remediator service.
Use the same change type to re-enable Trusted Remediator.

You can continue to reach out to AMS through Operations On Demand (OOD) for unsupported checks. AMS assists you with remediating these checks.
For more information, see
[Operations On Demand](../accelerate-guide/ops-on-demand.md "../accelerate-guide/ops-on-demand.md").

Trusted Remediator deploys the following resources in the Trusted Remediator delegated administrator account:

- An Amazon S3 bucket named `ams-trusted-remediator-{your-account-id}-logs`. Trusted Remediator creates the `Remediation item log` in
  JSON format when a remediation OpsItem is created, and uploads the log files to this bucket.
- An AWS AppConfig application to hold the remediation configurations for supported Trusted Advisor checks and Compute Optimizer recommendations.
  Trusted Remediator doesn't deploy resources in the Trusted Remediator member account.
