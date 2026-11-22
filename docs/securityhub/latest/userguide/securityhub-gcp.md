

# Integrating Security Hub CSPM with Google Cloud Platform

To monitor your Google Cloud Platform (GCP) resources, you can integrate GCP with AWS Security Hub CSPM. Security Hub CSPM then automatically enables posture management checks for your GCP environment and generates findings about your environment. More specifically, the service provides you with the following:

**Note**  
You can manage GCP standards and controls using the Security Hub CSPM console, APIs, and AWS CloudFormation. The Security Hub CSPM Central Configuration feature is not supported for GCP standards.
+ **ASFF findings** – Security Hub CSPM generates findings in the AWS Security Finding Format (ASFF) format for posture checks that it performs for your GCP resources.
+ **CIS Google Cloud Platform Foundation Benchmark v4.0.0** – Automated compliance checks against the CIS Google Cloud Platform Foundation Benchmark v4.0.0 standard. This standard includes identity, networking, storage, logging, and database controls.
+ **Posture management** – Continuous evaluation of GCP resource configurations against the CIS Google Cloud Platform Foundation Benchmark v4.0.0 standard, with 69 controls.
+ **Per-provider security scores** – Separate security scores for AWS and GCP, so you can track each environment independently.

To create the integration, you connect your GCP environment to Security Hub CSPM through the following process:

**Note**  
GCP standards differ from AWS standards in the following ways:  
GCP standards do not require manual AWS Config prerequisites. Unlike AWS, where CSPM-only customers need a customer managed recorder, GCP standards use an internal service-linked recorder automatically.
GCP standards always use internal service-linked config rules. AWS standards only use service-linked config rules when Security Hub is also enabled.

1. You configure your GCP environment with a workload identity pool and provider, a service account, GCP IAM role assignments, Pub/Sub topics and subscriptions, a Cloud Audit Logs sink, and a Cloud Asset Inventory feed. The Security Hub CSPM console generates a script that does this for you.

1. By using the Security Hub CSPM console, you create a connector for the integration. You specify your GCP organization ID, the scope of projects and locations to monitor, and the service account email and workload identity pool provider that the setup script created.

1. AWS Config collects resource configuration data from your GCP environment.

   AWS Config is used internally to collect resource configuration data. Unlike AWS posture management, where you must explicitly enable AWS Config and pay for recording, GCP posture management handles AWS Config automatically. You don't need to enable AWS Config separately, configure a recorder, or pay separately for AWS Config usage. These costs are included in your Security Hub CSPM pricing.

1. Security Hub CSPM begins receiving resource configuration data and Cloud Audit Logs events from your GCP environment.

1. Security Hub CSPM generates posture management findings about your GCP environment.

## How AWS Config is used
<a name="securityhub-gcp-config"></a>

AWS Config is used internally to collect resource configuration data and detect changes in your GCP environment. The connector handles this automatically. You do not need to enable AWS Config separately, configure a recorder, or pay for AWS Config usage. These costs are included in your Security Hub CSPM pricing for GCP resources.

## Service-linked connectors and customer-managed connectors
<a name="securityhub-gcp-slc-cmc"></a>

Security Hub CSPM supports two types of connectors:

Service-linked connector (SLC)  
Automatically created when you set up the GCP integration in Security Hub. The scope of a service-linked connector always matches the scope defined in your Security Hub connector. You cannot modify the scope of a service-linked connector directly; instead, modify the scope in Security Hub. Security Hub manages the lifecycle of service-linked connectors on your behalf.

Customer-managed connector (CMC)  
Created directly in the Security Hub CSPM console on the Integrations page. Use a customer-managed connector when you want to use Security Hub CSPM independently of Security Hub, or when you need a different scope than your Security Hub connector. When both types exist, the service-linked connector scope must always be equal to or larger than your customer-managed connector scope.

**Note**  
Unlike Security Hub, Security Hub CSPM does not offer per-capability selection for GCP connectors. When you create a connector in Security Hub CSPM, all posture management capabilities are enabled together.

For information about estimating and calculating costs for integrating Security Hub CSPM with GCP, see [AWS Security Hub CSPM pricing](https://aws.amazon.com/security-hub/pricing/).

**Topics**
+ [How AWS Config is used](#securityhub-gcp-config)
+ [Connector types](#securityhub-gcp-slc-cmc)
+ [Prerequisites](securityhub-gcp-prereqs.md)
+ [Configuring GCP](securityhub-gcp-setup-gcp.md)
+ [Configuring Security Hub CSPM](securityhub-gcp-setup-securityhub.md)
+ [Deleting a GCP connector](securityhub-gcp-delete.md)