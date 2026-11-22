

# Integrating Amazon Inspector with Google Cloud Platform

You can create an integration to Google Cloud Platform (GCP) in Amazon Inspector to detect software vulnerabilities in your GCP resources. After you create the connector, Amazon Inspector continuously scans your Compute Engine VM instances, Cloud Run functions, and Artifact Registry images for known vulnerabilities and generates findings with remediation guidance.

## How it works
<a name="inspector-gcp-how-it-works"></a>

An integration to GCP enables Amazon Inspector to discover and scan your GCP resources for software vulnerabilities. The connector uses IAM Outbound Identity Federation and GCP workload identity federation to securely authenticate to your GCP environment without storing long-lived credentials.

1. You create a connector in the Amazon Inspector console or using the API. You specify your GCP organization ID, GCP projects, and GCP locations, and select which capabilities to enable (VM scanning, Cloud Run function scanning, Artifact Registry image scanning).

1. You run the generated GCP setup script to configure workload identity federation, the GCP service account, Pub/Sub and log sink infrastructure, and permissions.

1. Amazon Inspector discovers your GCP resources and begins scanning for vulnerabilities. Findings, coverage, and usage for your GCP resources appear in the AWS account and AWS Region where you create the connector.

## How AWS Config is used
<a name="inspector-gcp-config"></a>

AWS Config is used internally to collect resource configuration data and detect changes in your GCP environment (such as new VM instances being launched or new images pushed to Artifact Registry). The connector handles this automatically. You do not pay for AWS Config usage separately. These costs are included in your Amazon Inspector pricing for GCP resources.

## Connector types
<a name="inspector-gcp-connector-types"></a>

Amazon Inspector supports two connector types for integrations to GCP:
+ **Service-linked connector (SLC)** – Created automatically when you set up an integration to GCP through AWS Security Hub. You cannot edit an SLC directly in Amazon Inspector. Manage it through AWS Security Hub instead. The AWS Security Hub scope (the monitored GCP projects and monitored GCP locations) must always be greater than or equal to any existing customer-managed connector scope.
+ **Customer-managed connector (CMC)** – Created directly in the Amazon Inspector console or via API. You have full control over scope and capabilities, including the ability to create, modify, and delete the connector.

For standalone Amazon Inspector usage, create a customer-managed connector. If you already have an AWS Security Hub integration to GCP, Amazon Inspector automatically receives a service-linked connector and you do not need to create a separate one.

## Scanning methods
<a name="inspector-gcp-scanning-methods"></a>

Amazon Inspector uses the following methods to scan GCP resources:
+ **Compute Engine VM instances** – Amazon Inspector uses the Amazon Inspector VM Scanner agent to scan VMs for operating system and application vulnerabilities. You can choose between managed deployment (recommended) or manual installation. For more information about the agent, see [Amazon Inspector VM Scanner](inspector-vm-scanner.md).
+ **Cloud Run functions** – Amazon Inspector automatically extracts and analyzes function code dependencies of 1st gen and 2nd gen Cloud Run functions for known vulnerabilities. Amazon Inspector does not scan function code for code vulnerabilities, and does not scan Cloud Run services or jobs as functions. Artifact Registry image scanning covers their container images when the repository is in scope.
+ **Artifact Registry images** – Amazon Inspector automatically scans container images stored in standard Docker-format repositories in Artifact Registry for vulnerabilities in operating system packages and application dependencies. Amazon Inspector does not scan remote or virtual repositories, or repositories in other formats, such as Maven, npm, or Python.