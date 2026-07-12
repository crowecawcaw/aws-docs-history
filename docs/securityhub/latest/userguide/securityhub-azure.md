# Integrating Security Hub CSPM with Microsoft Azure

To monitor your Microsoft Azure resources, you can integrate Microsoft Azure with AWS Security Hub CSPM. Security Hub CSPM
then automatically enables posture management checks for your Azure environment and
generates findings about your environment. More specifically, the service provides you with
the following:

###### Note

You can manage Azure standards and controls using the Security Hub CSPM console, APIs, and
AWS CloudFormation. The Security Hub CSPM Central Configuration feature is not supported for Azure
standards.

- **ASFF findings** – Security Hub CSPM generates findings
  in the AWS Security Finding Format (ASFF) format for posture checks that it performs for your Azure
  resources.
- **CIS Microsoft Azure Foundations Benchmark v4.0** –
  Automated compliance checks against the CIS Azure v4.0 standard. This standard
  includes identity, networking, storage, logging, and database controls.
- **Azure Foundational Best Practices** –
  Automated detection of Azure resource misconfigurations based on AWS-curated security
  best practices covering network security, identity management, data protection, and
  logging.
- **Posture management** – Continuous evaluation
  of Azure resource configurations against security best practices and compliance
  standards, with 122 controls across both standards.
- **Per-provider security scores** – Separate
  security scores for AWS and Azure, so you can track each environment
  independently.
  To create the integration, you connect your Azure environment to Security Hub CSPM through the
  following process:

###### Note

Azure standards differ from AWS standards in the following ways:

- Azure standards do not require manual AWS Config prerequisites. Unlike AWS, where
  CSPM-only customers need a customer managed recorder, Azure standards use an
  internal service-linked recorder automatically.
- Azure standards always use internal service-linked config rules. AWS
  standards only use service-linked config rules when Security Hub is also
  enabled.

1. You configure your Azure environment with an application registration, federated
   identity credentials, Azure role assignments, and Event Hub infrastructure.
2. By using the Security Hub CSPM console, you create a connector for the integration.
   You specify your Azure tenant ID, application client ID, and monitoring scope.
3. AWS Config collects resource configuration data from your Azure environment.

AWS Config is used internally to collect resource configuration data. Unlike AWS
posture management, where you must explicitly enable AWS Config and pay for recording,
Azure posture management handles AWS Config automatically. You don't need to enable AWS Config
separately, configure a recorder, or pay separately for AWS Config usage. These costs are
included in your Security Hub CSPM pricing. 4. Security Hub CSPM begins receiving resource configuration data and Activity Log events from
your Azure environment. 5. Security Hub CSPM generates posture management findings about your Azure environment.

## How AWS Config is used

AWS Config is used internally to collect resource configuration data and detect changes
in your Azure environment. The connector handles this automatically. You do not
need to enable AWS Config separately, configure a recorder, or pay for AWS Config usage. These costs
are included in your Security Hub CSPM pricing for Azure resources.

## Service-linked connectors and customer-managed connectors

Security Hub CSPM supports two types of connectors:

Service-linked connector (SLC)

Automatically created when you set up the Azure integration in Security Hub.
The scope of a service-linked connector always matches the scope defined in
your Security Hub connector. You cannot modify the scope of a
service-linked connector directly; instead, modify the scope in Security Hub.
Security Hub manages the lifecycle of service-linked connectors on your
behalf.

Customer-managed connector (CMC)

Created directly in the Security Hub CSPM console on the Integrations page. Use a
customer-managed connector when you want to use Security Hub CSPM independently of
Security Hub, or when you need a different scope than your Security Hub connector.
When both types exist, the service-linked connector scope must always be
equal to or larger than your customer-managed connector scope.

###### Note

Unlike Security Hub, Security Hub CSPM does not offer per-capability selection for Azure
connectors. When you create a connector in Security Hub CSPM, all posture management
capabilities are enabled together.

For information about estimating and calculating costs for integrating Security Hub CSPM with Azure,
see [AWS Security Hub CSPM pricing](https://aws.amazon.com/security-hub/pricing/ "https://aws.amazon.com/security-hub/pricing/").

###### Topics

- [Prerequisites](securityhub-azure-prereqs.md "securityhub-azure-prereqs.md")
- [Configuring Azure](securityhub-azure-setup-azure.md "securityhub-azure-setup-azure.md")
- [Configuring Security Hub CSPM](securityhub-azure-setup-securityhub.md "securityhub-azure-setup-securityhub.md")
- [Deleting an Azure connector](securityhub-azure-delete.md "securityhub-azure-delete.md")
