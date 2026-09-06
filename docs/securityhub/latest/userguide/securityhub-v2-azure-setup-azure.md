

# Configuring Microsoft Azure to integrate with Security Hub
<a name="securityhub-v2-azure-setup-azure"></a>

After you complete the [prerequisite tasks](securityhub-v2-azure-prereqs.md), you can configure your Microsoft Azure environment to support integration with AWS Security Hub. To help you do this, the Security Hub console generates a setup script that is customized for your configuration.

**To generate the setup script**

1. Open the AWS Security Hub console at [https://console.aws.amazon.com/securityhub/advanced/home?region=us-east-1.](https://console.aws.amazon.com/securityhub/advanced/home?region=us-east-1.).

1. In the navigation pane, choose **Integrations**.

1. Choose **Create Azure connector**.

1. Complete the connector configuration (tenant ID, scope, and name), and then copy the generated setup script.

To run the script, use the Azure CLI and authenticate with a Global Administrator account (`az login`).

When you run the script, it performs a series of tasks. The following sections describe each task that the script performs. If your organization restricts script execution, you can perform these tasks manually, using this topic as a guide. After you configure your Azure environment, you can [configure Security Hub to integrate with Azure](securityhub-v2-azure-setup-securityhub-v2.md).

Steps 1–7 configure the shared foundation that all Security Hub capabilities use: the application registration, federated credentials, Azure role assignments, Microsoft Graph permissions, Event Hub, and log export. Steps 8–10 configure the additional Azure resources for specific capabilities:
+ **Vulnerability management (Amazon Inspector)** – Configures Azure Container Registry (ACR) repository-event export and a system-assigned managed identity on your Azure VMs.
+ **Threat detection (Microsoft Defender for Cloud)** – Configures Microsoft Defender for Cloud to continuously export security alerts to the Event Hub.

**Note**  
A single Azure app registration is shared across AWS security services. If you also use Security Hub CSPM or Amazon Inspector for Azure, they use the same app registration. You do not need to create separate registrations for each AWS service.

**Topics**
+ [Step 1: Register an application](#securityhub-v2-azure-setup-azure-registration)
+ [Step 2: Create a service principal](#securityhub-v2-azure-setup-azure-sp)
+ [Step 3: Configure federated credentials](#securityhub-v2-azure-setup-azure-federation)
+ [Step 4: Assign RBAC roles](#securityhub-v2-azure-setup-azure-rbac)
+ [Step 5: Configure Graph API permissions](#securityhub-v2-azure-setup-azure-graph)
+ [Step 6: Set up Event Hub](#securityhub-v2-azure-setup-azure-eventhub)
+ [Step 7: Configure log export](#securityhub-v2-azure-setup-azure-export)
+ [Step 8: Configure ACR export](#securityhub-v2-azure-setup-azure-acr)
+ [Step 9: Enable VM managed identity](#securityhub-v2-azure-setup-azure-vm-identity)
+ [Step 10: Export Defender alerts](#securityhub-v2-azure-setup-azure-defender)

## Step 1: Register an Azure application
<a name="securityhub-v2-azure-setup-azure-registration"></a>

Register a new application in Microsoft Entra ID. This application serves as the identity that AWS uses to authenticate to your Azure environment using federated credentials. No client secrets are required.

```
$ az ad app create --display-name "AWSSecurityHubIntegration"
```

Note the **Application (client) ID** from the output (the `appId` attribute). You will provide this value when creating the connector in the Security Hub console.

## Step 2: Create a service principal
<a name="securityhub-v2-azure-setup-azure-sp"></a>

Create a service principal for the registered application. You use Azure role assignments to grant permissions to the service principal. The service principal performs actions in your Azure environment.

```
$ az ad sp create --id {{application-client-id}}
```

Where {{application-client-id}} is the Application (client) ID from the previous step.

Set the Application ID URI on the registration to `api://{{application-client-id}}`. AWS requires this identifier to exchange federated tokens with the application. Without this URI, AWS cannot produce a valid federated-token audience, and every capability fails to authenticate to Azure.

```
$ az ad app update \
  --id {{application-client-id}} \
  --identifier-uris "api://{{application-client-id}}"
```

## Step 3: Configure federated identity credentials
<a name="securityhub-v2-azure-setup-azure-federation"></a>

Configure federated identity credentials on the application to enable AWS to authenticate without client secrets. This establishes an OIDC trust between AWS and Azure. No long-lived secrets or credentials are stored.

The Security Hub Azure integration authenticates using one AWS IAM role per capability: resource configuration discovery, vulnerability management, and threat detection. Add a federated identity credential for each role so that every capability can authenticate to Azure. AWS creates the service-linked roles automatically when you create the connector. The `Inspector2SSMFederationRole` used for VM scanning is not a service-linked role; you create it as part of Amazon Inspector VM scanning setup, described in [Step 9](#securityhub-v2-azure-setup-azure-vm-identity).


| Capability | Subject (IAM role ARN) | 
| --- | --- | 
| Resource configuration discovery (AWS Config) | arn:aws:iam::{{account-id}}:role/aws-service-role/thirdparty.config.amazonaws.com/AWSServiceRoleForConfigThirdParty | 
| Vulnerability management (Inspector) | arn:aws:iam::{{account-id}}:role/aws-service-role/thirdparty.inspector2.amazonaws.com/AWSServiceRoleForAmazonInspector2ThirdParty | 
| Vulnerability management – VM scanning (Amazon EC2 Systems Manager) | arn:aws:iam::{{account-id}}:role/Inspector2SSMFederationRole-{{tenant-id}} | 
| Threat detection (Security Hub) | arn:aws:iam::{{account-id}}:role/aws-service-role/securityhubv2.amazonaws.com/AWSServiceRoleForSecurityHubV2 | 

Run the following command once for each subject in the preceding table, changing the `name` and `subject` values each time. The `issuer` and `audiences` values are the same for every credential.

```
$ az ad app federated-credential create \
  --id {{application-client-id}} \
  --parameters '{
    "name": "{{credential-name}}",
    "issuer": "{{token-issuer-url}}",
    "subject": "{{service-linked-role-arn}}",
    "audiences": ["api://AzureADTokenExchange"],
    "description": "AWS federation for Security Hub Azure integration"
  }'
```

Key values:
+ **Issuer** – Your Token Issuer URL from IAM Outbound Identity Federation. This follows the format `https://{{uuid}}.tokens.sts.global.api.aws`.
+ **Subject** – An IAM role ARN from the preceding table. The {{tenant-id}} in the Amazon EC2 Systems Manager role is your Azure tenant ID.
+ **Audience** – `api://AzureADTokenExchange` (standard value for workload identity federation).
+ **Name** – Any name that is unique within the application.

## Step 4: Assign RBAC roles
<a name="securityhub-v2-azure-setup-azure-rbac"></a>

Assign the following built-in roles to the service principal at the tenant root management group scope. Assigning them at this scope propagates the permissions to every subscription in the tenant.
+ **Reader** – Grants read-only access to all Azure resources, so Security Hub can discover and evaluate your resource configurations.
+ **Contributor** – Grants the write access that Amazon Inspector requires to scan your Azure virtual machines, Function Apps, and container images for vulnerabilities.
+ **Azure Event Hubs Data Receiver** – Allows AWS to read events from the Event Hub.

**Important**  
The **Contributor** role at the tenant root management group scope grants highly privileged, tenant-wide write access to your Azure resources. Security Hub requires this access so that Amazon Inspector can scan your compute resources for vulnerabilities. For example, Inspector uses the virtual machine run-command permissions that Contributor provides. Through Amazon EC2 Systems Manager Automation, Inspector runs commands on your Azure VMs to install and operate the VM Scanner agent.

```
$ az role assignment create \
  --assignee {{application-client-id}} \
  --role "Reader" \
  --scope "/providers/Microsoft.Management/managementGroups/{{tenant-id}}"

$ az role assignment create \
  --assignee {{application-client-id}} \
  --role "Contributor" \
  --scope "/providers/Microsoft.Management/managementGroups/{{tenant-id}}"

$ az role assignment create \
  --assignee {{application-client-id}} \
  --role "Azure Event Hubs Data Receiver" \
  --scope "/providers/Microsoft.Management/managementGroups/{{tenant-id}}"
```

**Note**  
If this step fails, verify that *Access management for Azure resources* is set to **Yes** in Microsoft Entra ID > Properties. Then sign out and sign back in to refresh your token.

## Step 5: Configure Microsoft Graph API permissions
<a name="securityhub-v2-azure-setup-azure-graph"></a>

Grant the following Microsoft Graph API permissions (Application type) to the application, and then grant admin consent:
+ `Directory.Read.All`
+ `AuditLog.Read.All`
+ `Policy.Read.All`

```
$ az ad app permission admin-consent --id {{application-client-id}}
```

## Step 6: Set up Azure Event Hub
<a name="securityhub-v2-azure-setup-azure-eventhub"></a>

AWS Config uses an Azure Event Hub to receive near real-time notifications of resource configuration changes in your Azure environment. The setup script creates the Event Hub infrastructure and tags it for discovery. Event Hub discovery uses tag-based resolution: Security Hub looks for a tag on the Event Hub namespace with the format `AWSConfig-{{account-id}}-{{region}}` to identify the correct Event Hub instance for your integration.

```
$ az group create \
  --name "aws-securityhub-integration" \
  --location {{event-hub-region}}

$ az eventhubs namespace create \
  --resource-group "aws-securityhub-integration" \
  --name "aws-securityhub-{{account-id}}" \
  --location {{event-hub-region}} \
  --sku Standard

$ az eventhubs eventhub create \
  --resource-group "aws-securityhub-integration" \
  --namespace-name "aws-securityhub-{{account-id}}" \
  --name "activitylog" \
  --message-retention 3 \
  --partition-count 4

$ az eventhubs eventhub consumer-group create \
  --resource-group "aws-securityhub-integration" \
  --namespace-name "aws-securityhub-{{account-id}}" \
  --eventhub-name "activitylog" \
  --name "AWSConfig"
```

After creating the Event Hub, tag the namespace for discovery and assign the Data Receiver role. Use `az tag update` with `--operation merge` so that you preserve any other tags on the namespace (such as the threat detection discovery tag from [Step 10](#securityhub-v2-azure-setup-azure-defender)):

```
$ az tag update \
  --resource-id {{namespace-resource-id}} \
  --operation merge \
  --tags "AWSConfig-{{account-id}}-{{region}}=activitylog"

$ az role assignment create \
  --assignee {{application-client-id}} \
  --role "Azure Event Hubs Data Receiver" \
  --scope {{namespace-resource-id}}
```

**Note**  
In the tag format `AWSConfig-{{account-id}}-{{region}}`, {{account-id}} is your 12-digit AWS account ID and {{region}} is the AWS Region where you are creating the connector (for example, `us-east-1`). These values identify which AWS account and Region own this Event Hub integration.

Key configuration:
+ **Namespace SKU** – Standard (required for consumer groups).
+ **Event Hub name** – `activitylog`.
+ **Consumer group** – `AWSConfig`.
+ **Tag** – `AWSConfig-{{account-id}}-{{region}}` with value `activitylog`. This tag enables AWS Config to discover the Event Hub automatically.
+ **Role assignment** – Azure Event Hubs Data Receiver on the namespace.

For threat detection, the setup also creates a separate `defender-alerts` Event Hub with an `AWSSecurityHub` consumer group, and adds a second discovery tag in the format `AWSSecurityHub-{{account-id}}-{{region}}` that identifies the hubs Security Hub reads directly. For more information, see [Step 10](#securityhub-v2-azure-setup-azure-defender).

## Step 7: Configure Activity Log and Entra ID Audit Log export
<a name="securityhub-v2-azure-setup-azure-export"></a>

Configure Azure to export Activity Logs and Microsoft Entra ID logs to the Event Hub.

**Activity Log export:**

Configure diagnostic settings on each subscription to export Activity Logs to the Event Hub. The setup script configures this automatically for all monitored subscriptions. Activity Logs capture subscription-level activity including role assignments and resource changes.

**Microsoft Entra ID log export:**

Configure diagnostic settings on Microsoft Entra ID to export logs to the same Event Hub. Navigate to *Microsoft Entra ID > Monitoring > Diagnostic settings > Add diagnostic setting*. Enable **AuditLogs**, **SignInLogs**, and **NonInteractiveUserSignInLogs**, and route them to your Event Hub.

## Step 8: Configure Azure Container Registry export
<a name="securityhub-v2-azure-setup-azure-acr"></a>

Security Hub scans your Azure Container Registry (ACR) container images for vulnerabilities through Amazon Inspector. To do this, Inspector needs ACR repository events exported to an Event Hub in the same Azure region as the registry. For the ACR export setup, see [Configuring Amazon Inspector to integrate with Microsoft Azure](https://docs.aws.amazon.com/inspector/latest/user/inspector-azure.html) in the *Amazon Inspector User Guide*.

## Step 9: Enable a managed identity on Azure VMs
<a name="securityhub-v2-azure-setup-azure-vm-identity"></a>

Security Hub scans your Azure virtual machines through Inspector. Each target Azure VM must have a system-assigned managed identity enabled. To add this identity to your VMs automatically, assign two Azure Policies that use the `modify` effect at the tenant root management group scope:
+ For a VM that has no identity, the policy adds a system-assigned managed identity.
+ For a VM that has only a user-assigned identity, the policy adds a system-assigned managed identity while preserving the existing user-assigned identities.

A VM that already has a system-assigned managed identity is left unchanged. Because the policies use the `modify` effect, they adjust the identity in place without redeploying the VM.

Inspector uses Amazon EC2 Systems Manager Automation to deploy and manage the Inspector VM Scanner agent on your Azure VMs. This requires additional AWS-side setup, including an IAM OIDC identity provider for Microsoft Entra ID and several IAM roles. For the complete VM scanning setup, see [Configuring Amazon Inspector to integrate with Microsoft Azure](https://docs.aws.amazon.com/inspector/latest/user/inspector-azure-setup-inspector.html) in the *Amazon Inspector User Guide*.

## Step 10: Export Microsoft Defender for Cloud alerts
<a name="securityhub-v2-azure-setup-azure-defender"></a>

Security Hub ingests Microsoft Defender for Cloud threat detection alerts and maps them to the Open Cybersecurity Schema Framework (OCSF) format. To deliver these alerts, create a dedicated `defender-alerts` Event Hub and configure Microsoft Defender for Cloud to continuously export security alerts to it.

In the Event Hub namespace from [Step 6](#securityhub-v2-azure-setup-azure-eventhub), create the `defender-alerts` Event Hub, an `AWSSecurityHub` consumer group for Security Hub to read from, and a hub-scoped shared access signature (SAS) authorization rule with **Send** permission that Microsoft Defender for Cloud uses to send alerts:

```
$ az eventhubs eventhub create \
  --resource-group "aws-securityhub-integration" \
  --namespace-name "aws-securityhub-{{account-id}}" \
  --name "defender-alerts" \
  --message-retention 3 \
  --partition-count 4

$ az eventhubs eventhub consumer-group create \
  --resource-group "aws-securityhub-integration" \
  --namespace-name "aws-securityhub-{{account-id}}" \
  --eventhub-name "defender-alerts" \
  --name "AWSSecurityHub"

$ az eventhubs eventhub authorization-rule create \
  --resource-group "aws-securityhub-integration" \
  --namespace-name "aws-securityhub-{{account-id}}" \
  --eventhub-name "defender-alerts" \
  --name "DefenderExportSend" \
  --rights Send
```

Then, merge a second discovery tag onto the namespace so that Security Hub discovers the `defender-alerts` hub. Use `az tag update` with `--operation merge` so that you preserve the `AWSConfig` discovery tag from [Step 6](#securityhub-v2-azure-setup-azure-eventhub):

```
$ az tag update \
  --resource-id {{namespace-resource-id}} \
  --operation merge \
  --tags "AWSSecurityHub-{{account-id}}-{{region}}=defender-alerts"
```

Finally, configure Microsoft Defender for Cloud continuous export of the **Security alerts** data type to the `defender-alerts` Event Hub. In the Azure portal, go to *Microsoft Defender for Cloud > Environment settings*, select the subscription, choose *Continuous export > Event Hub*, select **Security alerts**, and choose the `defender-alerts` Event Hub and the `DefenderExportSend` SAS rule.

**Note**  
If you configure continuous export programmatically (through the Azure Resource Manager API, an ARM template, or Azure Policy) rather than in the portal, authenticate the export to the Event Hub with the `DefenderExportSend` SAS connection string. Retrieve it with `az eventhubs eventhub authorization-rule keys list` for the `DefenderExportSend` rule, and set it as the export action's connection string. For more information, see [Set up continuous export](https://learn.microsoft.com/en-us/azure/defender-for-cloud/continuous-export) in the Microsoft Azure documentation.

**Note**  
After you complete these tasks, wait approximately 15–30 minutes for the configuration to take effect. Then, verify that your Event Hub is receiving messages (the *IncomingMessages* metric) before you create the connector in Security Hub.