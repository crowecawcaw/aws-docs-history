

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Trusted Remediator FAQs
<a name="tr-faq"></a>

The following are frequently asked questions about Trusted Remediator:

## What is Trusted Remediator and how does it benefit me?
<a name="tr-faq-benefits"></a>

When a non-compliance is identified by Trusted Advisor or a recommendation is issued by Compute Optimizer, or Security Hub CSPM, Trusted Remediator responds according to your specified preferences, either by applying remediation, seeking approval through manual remediations, or reporting the remediations during your upcoming Monthly Business Review (MBR). The remediation happen at your preferred remediation time or schedule. Trusted Remediator provides you with the ability to self-service and act on Trusted Advisor checks with the flexibility to configure and remediate checks individually or in bulk. With a library of tested remediation documents, AMS constantly bar raises your accounts by applying safety checks and following AWS best practices. You are only notified if you specify to do so in your configuration. AMS users can opt-in to Trusted Remediator at no additional charge.

## How does Trusted Remediator relate to and work with other AWS services?
<a name="tr-faq-relates"></a>

You have access to Trusted Advisor checks, Compute Optimizer recommendations, and Security Hub CSPM controls as part of your existing Enterprise Support plan. Trusted Remediator integrates with Trusted Advisor, Compute Optimizer, and Security Hub CSPM to leverage existing AMS automation capabilities. Specifically, AMS uses AWS Systems Manager automation documents (runbooks) for automated remediations. AWS AppConfig is used to configure the remediation workflows. You can view all the current and past remediations through the Systems Manager OpsCenter. The remediation logs are stored in an Amazon S3 bucket. You can use the logs to import and build custom reporting dashboards in Quick.

## Who configures the remediations?
<a name="tr-faq-configure"></a>

You own the configurations in your account. Managing your configurations is your responsibility. You can also reach out to AMS for configuration changes, support, and manual remediations, and troubleshooting remediation failures.

## How do I install SSM automation documents?
<a name="tr-faq-ssm"></a>

SSM automation documents are automatically shared to onboarded AMS accounts.

## Will AMS owned resources be remediated too?
<a name="tr-faq-ams-owned"></a>

AMS owned resources aren't flagged by Trusted Remediator. Trusted Remediator focuses only on your resources.

## What AWS Regions is Trusted Remediator available in and who can use it?
<a name="tr-faq-regions"></a>

Trusted Remediator is available for AMS Advanced customers. For a current list of support Regions, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).

## Will Trusted Remediator cause resource drift?
<a name="tr-faq-drift"></a>

Since SSM automation documents directly update resources through the AWS API, resource drift might occur. You can use tags to segregate resources created through your existing CI/CD packages. You can configure Trusted Remediator to ignore the tagged resources while still remediating your other resources.

## How do I pause or stop Trusted Remediator?
<a name="tr-faq-stop-adv"></a>

Use the [ Management \| Trusted Remediator \| State \| Enable or disable](https://docs.aws.amazon.com/managedservices/latest/ctref/management-trusted-state-enable-or-disable.html) change type to stop the Trusted Remediator service. Use the same change type to re-enable Trusted Remediator.

## How can I remediate checks that aren't supported by Trusted Remediator?
<a name="tr-faq-remediate-checks"></a>

You can continue to reach out to AMS through Operations On Demand (OOD) for unsupported checks. AMS assists you with remediating these checks. For more information, see [Operations On Demand](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/ops-on-demand.html).

## What resources does Trusted Remediator deploy to your accounts?
<a name="tr-faq-deployed-resources"></a>

Trusted Remediator deploys the following resources in the Trusted Remediator delegated administrator account:
+ An Amazon S3 bucket named `ams-trusted-remediator-{your-account-id}-logs`. Trusted Remediator creates the `Remediation item log` in JSON format when a remediation OpsItem is created, and uploads the log files to this bucket.
+ An AWS AppConfig application to hold the remediation configurations for supported Trusted Advisor checks, Compute Optimizer and Security Hub CSPM recommendations.

Trusted Remediator doesn't deploy resources in the Trusted Remediator member account.