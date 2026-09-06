

# Integrating Amazon Inspector with Microsoft Azure
<a name="inspector-azure"></a>

You can create an integration to Microsoft Azure in Amazon Inspector to detect software vulnerabilities in your Azure resources. After you create the connector, Amazon Inspector continuously scans your Azure Virtual Machines (VMs), Azure Function Apps, and Azure Container Registry (ACR) images for known vulnerabilities and generates findings with remediation guidance.

## How it works
<a name="inspector-azure-how-it-works"></a>

An integration to Microsoft Azure enables Amazon Inspector to discover and scan your Azure resources for software vulnerabilities. The connector uses IAM Outbound Identity Federation to securely authenticate to your Azure environment without storing long-lived credentials.

1. You create a connector in the Amazon Inspector console or using the API. You specify your Azure tenant ID, Azure Subscriptions, and Azure Regions, and select which capabilities to enable (VM scanning, Function App scanning, ACR scanning).

1. You run the generated Azure setup script to configure the Azure app registration, Event Hub infrastructure, and permissions.

1. Amazon Inspector discovers your Azure resources and begins scanning for vulnerabilities.

## How AWS Config is used
<a name="inspector-azure-config"></a>

AWS Config is used internally to collect resource configuration data and detect changes in your Azure environment (such as new VMs being launched or new images pushed to ACR). The connector handles this automatically. You do not need to enable AWS Config separately, configure a recorder, or pay for AWS Config usage. These costs are included in your Amazon Inspector pricing for Azure resources.

## Connector types
<a name="inspector-azure-connector-types"></a>

Amazon Inspector supports two connector types for integrations to Microsoft Azure:
+ **Service-linked connector (SLC)** – Created automatically when you set up an integration to Microsoft Azure through AWS Security Hub CSPM. You cannot edit an SLC directly in Amazon Inspector. Manage it through AWS Security Hub CSPM instead. The AWS Security Hub CSPM scope (the monitored Azure Subscriptions and monitored Azure Regions) must always be greater than or equal to any existing customer-managed connector scope.
+ **Customer-managed connector (CMC)** – Created directly in the Amazon Inspector console or via API. You have full control over scope and capabilities, including the ability to create, modify, and delete the connector.

For standalone Amazon Inspector usage, create a customer-managed connector. If you already have an AWS Security Hub CSPM integration to Microsoft Azure, Amazon Inspector automatically receives a service-linked connector and you do not need to create a separate one.

## Scanning methods
<a name="inspector-azure-scanning-methods"></a>

Amazon Inspector uses the following methods to scan Azure resources:
+ **Virtual Machines** – Amazon Inspector uses the Amazon Inspector VM Scanner agent to scan VMs for operating system and application vulnerabilities. You can choose between managed deployment (recommended) or manual installation. For more information about the agent, see [Amazon Inspector VM Scanner](inspector-vm-scanner.md).
+ **Function Apps** – Amazon Inspector automatically extracts and analyzes function code dependencies for known vulnerabilities.
+ **Container Registry images** – Amazon Inspector automatically scans container images stored in Azure Container Registry (ACR) for vulnerabilities in operating system packages and application dependencies.