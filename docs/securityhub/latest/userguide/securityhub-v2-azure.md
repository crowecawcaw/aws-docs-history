# Integrating Security Hub with Microsoft Azure

To monitor your Microsoft Azure resources, you can integrate Microsoft Azure with AWS Security Hub. Security Hub
then automatically enables posture management and vulnerability management for your Azure
environment and generates findings and other data about your environment. You do not need to
turn on any Azure security services—all functionality is performed by AWS. More
specifically, the service provides you with the following:

- **CIS Microsoft Azure Foundations Benchmark v4.0 and Azure
  Foundational Best Practices** – Automated compliance checks against
  the CIS Azure v4.0 standard and the Azure Foundational Best Practices standard.
  These standards cover identity, networking, storage, logging, and database
  controls.
- **Vulnerability management** – Amazon Inspector
  automatically scans your Azure VMs, Function Apps, and Azure Container Registry (ACR) container images for software
  vulnerabilities through the service-linked connector.

###### Note

VM scanning requires Amazon EC2 Systems Manager to be configured in the same Region. For
setup details, see the Amazon Inspector documentation for Azure integration.

- **Exposure correlation** – Automated detection
  of exposed Azure resources based on network reachability, public access, and
  misconfiguration combinations.
- **Microsoft Defender for Cloud threat detection
  alerts** – If you configure Azure Defender continuous export to the
  Event Hub, Security Hub ingests Defender for Cloud threat detection alerts and maps them
  to Open Cybersecurity Schema Framework (OCSF) format. These appear alongside your posture management and vulnerability
  findings in the Security Hub console.
- **Asset inventory** – A complete inventory of
  your Azure resources discovered through the integration, visible in the Security Hub
  console alongside your AWS resources.
- **OCSF format** – Security Hub generates all
  findings in the Open Cybersecurity Schema Framework (OCSF) format, providing a consistent schema
  across AWS and Azure findings.
  To create the integration, you connect your Azure environment to Security Hub through the
  following process:

1. You configure your Azure environment with an application registration, federated
   identity credentials, Azure role assignments, and Event Hub infrastructure.
2. By using the Security Hub console, you create a connector for the integration.
   You specify your Azure tenant ID, application client ID, monitoring scope, and Event
   Hub region.
3. Security Hub creates the necessary service-linked roles and resources in your
   AWS account.
4. AWS Config collects resource configuration data from your Azure environment.

AWS Config is used internally to collect resource configuration data. Unlike AWS
posture management, where you must explicitly enable AWS Config and pay for recording,
Azure posture management handles AWS Config automatically. You don't need to enable AWS Config
separately, configure a recorder, or pay separately for AWS Config usage. These costs are
included in your Security Hub pricing. 5. Security Hub begins receiving resource configuration data and Activity Log events from
your Azure environment. 6. Security Hub generates posture management and vulnerability findings about your Azure
environment.

## How AWS Config is used

AWS Config is used internally to collect resource configuration data and detect changes
in your Azure environment. The connector handles this automatically. You do not
need to enable AWS Config separately, configure a recorder, or pay for AWS Config usage. These costs
are included in your Security Hub pricing for Azure resources.

When you create the integration, Security Hub also creates corresponding service-linked
integrations in Security Hub CSPM and Amazon Inspector automatically. These service-linked integrations ensure
that the scope of your CSPM checks and your Inspector vulnerability scans match the scope
that you define in Security Hub. If you want to change the scope, you have to make the changes in
the Security Hub. You can't modify a service-linked integration directly in Security Hub CSPM or
Inspector.

You can also create an Azure integration directly in Security Hub CSPM and specify independent scope
settings. The CSPM integration then operates independently from the Security Hub integration and
can have different Azure Subscription and Azure Region scope.

For information about estimating and calculating costs for integrating Security Hub with Azure,
see [AWS Security Hub pricing](https://aws.amazon.com/security-hub/pricing/ "https://aws.amazon.com/security-hub/pricing/").

###### Topics

- [Prerequisites](securityhub-v2-azure-prereqs.md "securityhub-v2-azure-prereqs.md")
- [Configuring Azure](securityhub-v2-azure-setup-azure.md "securityhub-v2-azure-setup-azure.md")
- [Configuring
  Security Hub](securityhub-v2-azure-setup-securityhub-v2.md "securityhub-v2-azure-setup-securityhub-v2.md")
- [Deleting an Azure
  connector](securityhub-v2-azure-delete.md "securityhub-v2-azure-delete.md")
