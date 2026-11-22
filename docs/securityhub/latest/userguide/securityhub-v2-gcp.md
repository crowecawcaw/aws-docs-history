

# Integrating Security Hub with Google Cloud Platform

To monitor your Google Cloud Platform (GCP) resources, you can integrate GCP with AWS Security Hub. Security Hub then automatically enables posture management and vulnerability management for your GCP environment and generates findings and other data about your environment. You do not need to turn on any GCP security services—all functionality is performed by AWS. More specifically, the service provides you with the following:

**CIS Google Cloud Platform Foundation Benchmark v4.0.0**  
Automated compliance checks against the CIS Google Cloud Platform Foundation Benchmark v4.0.0 standard. This standard covers identity, networking, storage, logging, and database controls.

**Vulnerability management**  
Amazon Inspector automatically scans your Compute Engine VMs, Cloud Run functions, and Artifact Registry container images for software vulnerabilities through the service-linked connector.  
VM scanning requires AWS Systems Manager to be configured in the same Region. For setup details, see [Integrating Amazon Inspector with Google Cloud Platform](https://docs.aws.amazon.com/inspector/latest/user/inspector-gcp.html) in the *Amazon Inspector User Guide*.

**Exposure correlation**  
Automated detection of exposed GCP resources based on network reachability, public access, and misconfiguration combinations.

**Asset inventory**  
A complete inventory of your GCP resources discovered through the integration, visible in the Security Hub console alongside your AWS resources.

**OCSF format**  
Security Hub generates all findings in the Open Cybersecurity Schema Framework (OCSF) format, providing a consistent schema across AWS and GCP findings.

To create the integration, you connect your GCP environment to Security Hub through the following process:

1. You configure your GCP environment with a workload identity pool and provider, a service account, GCP IAM role assignments, Pub/Sub topics and subscriptions, a Cloud Audit Logs sink, and a Cloud Asset Inventory feed. The Security Hub console generates a script that does this for you.

1. In the Security Hub console, you create a connector for the integration. You specify your GCP organization ID, the scope of projects and locations to monitor, and the service account email and workload identity pool provider that the setup script created.

1. Security Hub creates the necessary service-linked roles and resources in your AWS account.

1. AWS Config collects resource configuration data from your GCP environment.

   AWS Config is used internally to collect resource configuration data. Unlike AWS posture management, where you must explicitly enable AWS Config and pay for recording, GCP posture management handles AWS Config automatically. You do not need to enable AWS Config separately, configure a recorder, or pay separately for AWS Config usage. These costs are included in your Security Hub pricing.

1. Security Hub begins receiving resource configuration data and Cloud Audit Logs events from your GCP environment.

1. Security Hub generates posture management and vulnerability findings about your GCP environment.

## How AWS Config is used
<a name="securityhub-v2-gcp-config"></a>

AWS Config is used internally to collect resource configuration data and detect changes in your GCP environment. The connector handles this automatically. You do not need to enable AWS Config separately, configure a recorder, or pay for AWS Config usage. These costs are included in your Security Hub pricing for GCP resources.

## Additional information
<a name="securityhub-v2-gcp-additional-info"></a>

When you create the integration, Security Hub also creates corresponding service-linked integrations in Security Hub CSPM and Amazon Inspector automatically. These service-linked integrations ensure that the scope of your CSPM checks and your Amazon Inspector vulnerability scans match the scope that you define in Security Hub. If you want to change the scope, you have to make the changes in the Security Hub. You cannot modify a service-linked integration directly in Security Hub CSPM or Amazon Inspector.

You can also create a GCP integration directly in Security Hub CSPM and specify independent scope settings. The CSPM integration then operates independently from the Security Hub integration and can have different GCP project and location scope.

For information about estimating and calculating costs for integrating Security Hub with GCP, see [AWS Security Hub pricing](https://aws.amazon.com/security-hub/pricing/).

**Topics**
+ [How AWS Config is used](#securityhub-v2-gcp-config)
+ [Additional information](#securityhub-v2-gcp-additional-info)
+ [Prerequisites](securityhub-v2-gcp-prereqs.md)
+ [Configuring GCP](securityhub-v2-gcp-setup-gcp.md)
+ [Configuring Security Hub](securityhub-v2-gcp-setup-securityhub-v2.md)
+ [Deleting a GCP connector](securityhub-v2-gcp-delete.md)