

# Configuring Microsoft Azure to integrate with Amazon Inspector
<a name="inspector-azure-setup-azure"></a>

The Azure setup process configures your Azure environment to allow Amazon Inspector to authenticate and receive resource change notifications. Amazon Inspector generates a customized setup script during connector creation. The script performs the following steps.

**Note**  
If you have already completed Azure environment setup for AWS Security Hub CSPM or AWS Security Hub CSPM CSPM, the same app registration is shared. The script detects the existing registration and adds the required federated identity credential for Amazon Inspector without modifying existing configuration.

The setup script performs a series of tasks. The following sections describe each task that the script performs. If your organization restricts script execution, you can perform these tasks manually, using this topic as a guide.

Register a new application in Microsoft Entra ID. This application serves as the identity that AWS uses to authenticate to your Azure environment using federated credentials. No client secrets are required.

```
$ az ad app create --display-name "AWSSecurityHubIntegration"
```

Note the **Application (client) ID** from the output (the `appId` attribute). You will provide this value when creating the connector in the Amazon Inspector console.

Create a service principal for the registered application. You use Azure role assignments to grant permissions to the service principal. The service principal performs actions in your Azure environment.

```
$ az ad sp create --id {{application-client-id}}
```

Where {{application-client-id}} is the Application (client) ID from the previous step.

Configure federated identity credentials on the application to enable AWS to authenticate without client secrets. This establishes an OIDC trust between AWS and Azure. No long-lived secrets or credentials are stored.

```
$ az ad app federated-credential create \
  --id {{application-client-id}} \
  --parameters '{
    "name": "AWSConfigFederation",
    "issuer": "{{token-issuer-url}}",
    "subject": "arn:aws:iam::{{account-id}}:role/aws-service-role/thirdparty.config.amazonaws.com/AWSServiceRoleForConfigThirdParty",
    "audiences": ["api://AzureADTokenExchange"],
    "description": "Federation for AWS Config third-party cloud resource discovery"
  }'
```

Key values:
+ **Issuer** – Your Token Issuer URL from IAM Outbound Identity Federation. This follows the format `https://{{uuid}}.tokens.sts.global.api.aws`.
+ **Subject** – The ARN of the `AWSServiceRoleForConfigThirdParty` service-linked role in your AWS account. AWS creates this service-linked role automatically when you create the connector.
+ **Audience** – `api://AzureADTokenExchange` (standard value for workload identity federation).

Assign the **Reader** role to the service principal at the tenant root management group scope. This grants read-only access to all Azure resources across all subscriptions in the tenant.

```
$ az role assignment create \
  --assignee {{application-client-id}} \
  --role "Reader" \
  --scope "/providers/Microsoft.Management/managementGroups/{{tenant-id}}"
```

**Note**  
If this step fails, verify that *Access management for Azure resources* is set to **Yes** in Microsoft Entra ID > Properties. Then sign out and sign back in to refresh your token.

Grant the required Microsoft Graph API permissions (Application type) to the application: `Directory.Read.All`, `AuditLog.Read.All`, and `Policy.Read.All`. Then grant admin consent.

AWS Config uses an Azure Event Hub to receive near real-time notifications of resource configuration changes in your Azure environment. The setup script creates the Event Hub infrastructure and tags it for discovery.

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
  --message-retention 1 \
  --partition-count 4

$ az eventhubs eventhub consumer-group create \
  --resource-group "aws-securityhub-integration" \
  --namespace-name "aws-securityhub-{{account-id}}" \
  --eventhub-name "activitylog" \
  --name "AWSConfig"
```

After creating the Event Hub, tag the namespace for discovery and assign the Data Receiver role:

```
$ az tag create \
  --resource-id {{namespace-resource-id}} \
  --tags "AWSConfig-{{account-id}}-{{region}}=activitylog"

$ az role assignment create \
  --assignee {{application-client-id}} \
  --role "Azure Event Hubs Data Receiver" \
  --scope {{namespace-resource-id}}
```

Key configuration:
+ **Namespace SKU** – Standard (required for consumer groups).
+ **Event Hub name** – `activitylog`.
+ **Consumer group** – `AWSConfig`.
+ **Tag** – `AWSConfig-{{account-id}}-{{region}}` with value `activitylog`. This tag enables AWS Config to discover the Event Hub automatically.
+ **Role assignment** – Azure Event Hubs Data Receiver on the namespace.

**Note**  
The tag format is `AWSConfig-{{account-id}}-{{region}}` where {{account-id}} is your 12-digit AWS account identifier and {{region}} is the AWS Region where you created the connector (for example, `us-east-1`).

Configure Azure to export Activity Logs and Entra ID Audit Logs to the Event Hub.

**Activity Log export:**

Configure diagnostic settings on each subscription to export Activity Logs to the Event Hub. The setup script configures this automatically for all monitored subscriptions. Activity Logs capture subscription-level activity including role assignments and resource changes.

**Entra ID Audit Log export:**

Configure diagnostic settings on Microsoft Entra ID to export audit logs to the same Event Hub. Navigate to *Microsoft Entra ID > Monitoring > Diagnostic settings > Add diagnostic setting*. Enable **AuditLogs** and route them to your Event Hub.

To run the Azure setup script:

1. Open a terminal with the Azure CLI authenticated to your Azure tenant (`az login`). You must have Contributor and Owner permissions on the target subscriptions.

1. Copy the setup script from the Amazon Inspector console (generated during connector creation).

1. Run the setup script. The script completes the Azure environment setup described above.

1. After the script completes successfully, return to the Amazon Inspector console to finish creating the connector.

**Important**  
If you later change the connector scope (for example, add a new Azure region), the console regenerates the setup script to provision Event Hub infrastructure in the new region. You must re-run the updated script.