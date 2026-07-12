# Configuring Microsoft Azure to integrate with Security Hub CSPM

After you complete the [prerequisite tasks](securityhub-azure-prereqs.md "securityhub-azure-prereqs.md"),
you can configure your Microsoft Azure environment to support integration with AWS Security Hub CSPM. To help you
do this, the Security Hub CSPM console generates a setup script that's customized for your
configuration.

To generate the script, do the following:

1. Open the Security Hub CSPM console.
2. In the navigation pane, choose **Integrations**.
3. Choose **Create Azure connector**.
4. Complete the connector configuration (tenant ID, scope, and name), and then copy the
   generated setup script.
   To run the script, use the Azure CLI and authenticate with a Global Administrator account
   (`az login`).

When you run the script, it performs a series of tasks. The following sections describe each
task that the script performs. If your organization restricts script execution, you can perform
these tasks manually, using this topic as a guide. After you configure your Azure environment,
you can [configure Security Hub CSPM to integrate with
Azure](securityhub-azure-setup-securityhub.md "securityhub-azure-setup-securityhub.md").

###### Note

A single Azure app registration is shared across AWS security services. If you also use
Security Hub or Amazon Inspector for Azure, they use the same app registration. You do not need to create
separate registrations for each AWS service.

###### Tasks

- [Step 1: Register an
  application](#securityhub-azure-setup-azure-registration "#securityhub-azure-setup-azure-registration")
- [Step 2: Create a service
  principal](#securityhub-azure-setup-azure-sp "#securityhub-azure-setup-azure-sp")
- [Step 3: Configure
  federated credentials](#securityhub-azure-setup-azure-federation "#securityhub-azure-setup-azure-federation")
- [Step 4: Assign the Reader
  role](#securityhub-azure-setup-azure-rbac "#securityhub-azure-setup-azure-rbac")
- [Step 5: Configure Graph API
  permissions](#securityhub-azure-setup-azure-graph "#securityhub-azure-setup-azure-graph")
- [Step 6: Set up Event
  Hub](#securityhub-azure-setup-azure-eventhub "#securityhub-azure-setup-azure-eventhub")
- [Step 7: Configure log
  export](#securityhub-azure-setup-azure-export "#securityhub-azure-setup-azure-export")

## Step 1: Register an Azure application

Register a new application in Microsoft Entra ID. This application serves as the identity
that AWS uses to authenticate to your Azure environment using federated credentials. No
client secrets are required.

```
`$` `az ad app create --display-name "AWSSecurityHubIntegration"`
```

Note the **Application (client) ID** from the output (the
`appId` attribute). You will provide this value when creating the connector in the
Security Hub CSPM console.

## Step 2: Create a service principal

Create a service principal for the registered application. You use Azure role assignments
to grant permissions to the service principal. The service principal performs actions in your
Azure environment.

```
`$` `az ad sp create --id `application-client-id``
```

Where `application-client-id` is the Application (client) ID from
the previous step.

## Step 3: Configure federated identity credentials

Configure federated identity credentials on the application to enable AWS to
authenticate without client secrets. This establishes an OIDC trust between AWS and Azure.
No long-lived secrets or credentials are stored.

```
`$` `az ad app federated-credential create \
 --id `application-client-id` \
 --parameters '{
 "name": "AWSConfigFederation",
 "issuer": "`token-issuer-url`",
 "subject": "arn:aws:iam::`account-id`:role/aws-service-role/thirdparty.config.amazonaws.com/AWSServiceRoleForConfigThirdParty",
 "audiences": ["api://AzureADTokenExchange"],
 "description": "Federation for AWS Config third-party cloud resource discovery"
 }'`
```

Key values:

- **Issuer** – Your Token Issuer URL from IAM
  Outbound Identity Federation. This follows the format
  `https://`uuid`.tokens.sts.global.api.aws`.
- **Subject** – The ARN of the
  `AWSServiceRoleForConfigThirdParty` service-linked role in your
  AWS account. AWS creates this service-linked role automatically during connector
  setup.
- **Audience** –
  `api://AzureADTokenExchange` (standard value for workload identity
  federation).

## Step 4: Assign the Reader role

Assign the **Reader** role to the service principal at the
tenant root management group scope. This grants read-only access to all Azure resources across
all subscriptions in the tenant.

```
`$` `az role assignment create \
 --assignee `application-client-id` \
 --role "Reader" \
 --scope "/providers/Microsoft.Management/managementGroups/`tenant-id`"`
```

###### Note

If this step fails, verify that _Access management for Azure
resources_ is set to **Yes** in Microsoft Entra ID

> Properties. Then sign out and sign back in to refresh your token.

## Step 5: Configure Microsoft Graph API permissions

Grant the following Microsoft Graph API permissions (Application type) to the application,
and then grant admin consent:

- `Directory.Read.All`
- `AuditLog.Read.All`
- `Policy.Read.All`

```
`$` `az ad app permission admin-consent --id `application-client-id``
```

## Step 6: Set up Azure Event Hub

AWS Config uses an Azure Event Hub to receive near real-time notifications of resource
configuration changes in your Azure environment. The setup script creates the Event Hub
infrastructure and tags it for discovery.

```
`$` `az group create \
 --name "aws-securityhub-integration" \
 --location `event-hub-region`

$ az eventhubs namespace create \
 --resource-group "aws-securityhub-integration" \
 --name "aws-securityhub-`account-id`" \
 --location `event-hub-region` \
 --sku Standard

$ az eventhubs eventhub create \
 --resource-group "aws-securityhub-integration" \
 --namespace-name "aws-securityhub-`account-id`" \
 --name "activitylog" \
 --message-retention 1 \
 --partition-count 4

$ az eventhubs eventhub consumer-group create \
 --resource-group "aws-securityhub-integration" \
 --namespace-name "aws-securityhub-`account-id`" \
 --eventhub-name "activitylog" \
 --name "AWSConfig"`
```

After creating the Event Hub, tag the namespace for discovery and assign the Data Receiver
role:

```
`$` `az tag create \
 --resource-id `namespace-resource-id` \
 --tags "AWSConfig-`account-id`-`region`=activitylog"

$ az role assignment create \
 --assignee `application-client-id` \
 --role "Azure Event Hubs Data Receiver" \
 --scope `namespace-resource-id``
```

###### Note

In the tag format
`AWSConfig-`account-id`-`region``,
`account-id` is your 12-digit AWS account ID and
`region` is the AWS Region where you are creating the connector
(for example, `us-east-1`). These values identify which AWS account and Region
own this Event Hub integration.

Key configuration:

- **Namespace SKU** – Standard (required for
  consumer groups).
- **Event Hub name** –
  `activitylog`.
- **Consumer group** –
  `AWSConfig`.
- **Tag** –
  `AWSConfig-`account-id`-`region``
  with value `activitylog`. This tag enables AWS Config to discover the Event Hub
  automatically.
- **Role assignment** – Azure Event Hubs Data
  Receiver on the namespace.

## Step 7: Configure Activity Log and Entra ID Audit Log export

Configure Azure to export Activity Logs and Entra ID Audit Logs to the Event Hub.

**Activity Log export:**

Configure diagnostic settings on each subscription to export Activity Logs to the Event
Hub. The setup script configures this automatically for all monitored subscriptions. Activity
Logs capture subscription-level activity including role assignments and resource
changes.

**Entra ID Audit Log export:**

Configure diagnostic settings on Microsoft Entra ID to export audit logs to the same Event
Hub. Navigate to _Microsoft Entra ID > Monitoring > Diagnostic settings > Add
diagnostic setting_. Enable **AuditLogs** and route
them to your Event Hub.

**Microsoft Defender for Cloud continuous export (optional):**

To forward Defender for Cloud security alerts to Security Hub CSPM, configure continuous export to
your Event Hub. In the Azure portal, navigate to _Microsoft Defender for Cloud >
Environment settings > select subscription > Continuous export_. Select
**Event Hub** as the export target and choose your Event Hub
namespace. Enable **Security alerts** as the export data
type.

**Amazon Inspector data event configuration (optional):**

If you plan to use Amazon Inspector for Azure VM scanning, additional data event configuration
is required. For details about configuring Inspector-specific data events, see the
Amazon Inspector documentation for Azure integration.
