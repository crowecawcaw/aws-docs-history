

# Send platform telemetry from Microsoft Azure

Azure vended telemetry brings the telemetry that Azure services already record about your resources into Amazon CloudWatch: resource logs, traces, virtual network (VNet) flow logs, and Azure Monitor platform metrics. You do not install or run any software in Azure to collect it. After the telemetry is in CloudWatch, it appears in CloudWatch Omni.

You connect a Microsoft Entra ID tenant to an AWS account and Region once. You then choose which telemetry types to collect (resource logs, metrics, and flow logs), and from which subscriptions, regions, and resource types. A generated Bicep template sets up collection in Azure, and a telemetry pipeline reads from Azure and writes to CloudWatch. No Azure secret or key is stored: CloudWatch signs in to Microsoft Entra ID with workload identity federation.

Azure vended telemetry collects what Azure records about a resource, such as a virtual machine's CPU metrics. It does not collect telemetry from inside a virtual machine or from your application code. For that, install the CloudWatch agent; see [Send application telemetry](omni-send-application-telemetry.md).

## How Azure telemetry reaches your space
<a name="omni-send-platform-telemetry-from-microsoft-azure-how-azure-telemetry-reaches-your-space"></a>

Setup has three parts:
+ **A connection.** A connection records your Microsoft Entra tenant, the Microsoft Entra application that CloudWatch signs in as, and the IAM role (the *connection role*) that CloudWatch uses to get tokens for that application. It also stores the *telemetry scope*: the telemetry types, subscriptions, regions, and resource types to collect from. In the API, a connection is a connector.
+ **Collection resources in Azure.** A Bicep template that is generated from the telemetry scope creates an Event Hubs namespace in each region that you collect logs from, and Azure Policy assignments that add a diagnostic setting to each matching resource. For VNet flow logs, it creates a storage account in each region and a policy that adds a flow log to each matching virtual network. Platform metrics need no Azure resources.
+ **A telemetry pipeline.** The pipeline reads from the event hubs, the flow log storage accounts, and Azure Monitor, and writes to CloudWatch with a second IAM role, the *writer role*.


| Signal | Azure source | 
| --- | --- | 
| Resource logs | A diagnostic setting on each resource sends its logs (the allLogs category group) to an event hub in the resource's region. The telemetry pipeline reads the event hub continuously. For more information, see [Diagnostic settings in Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/data-collection/diagnostic-settings) on the Microsoft Learn website. | 
| Traces | Request and dependency records arrive with the resource logs, through the same diagnostic settings and event hub. The telemetry pipeline reads them from the event hub and turns them into spans. For the resource types that send traces, see [Supported resource types](#omni-send-platform-telemetry-from-microsoft-azure-supported-resource-types). | 
| VNet flow logs | A virtual network flow log writes to a storage account in the same region. The telemetry pipeline reads new flow log files from the storage account once an hour. For more information, see [Virtual network flow logs](https://learn.microsoft.com/en-us/azure/network-watcher/vnet-flow-logs-overview) on the Microsoft Learn website. | 
| Platform metrics | The telemetry pipeline reads metrics from Azure Monitor in each region with the metrics batch API, at each metric's finest time grain, typically one minute. For the API and the metrics of each resource type, see [Metrics Batch](https://learn.microsoft.com/en-us/rest/api/monitor/metrics-batch/batch) and [Azure Monitor supported metrics by resource type](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/supported-metrics/metrics-index) on the Microsoft Learn website. | 

### Data flow
<a name="omni-send-platform-telemetry-from-microsoft-azure-data-flow"></a>

1. In each Azure region in scope, Azure Policy adds the diagnostic setting `aws-cloudwatch-ingestion-<account-id>-<aws-region>` to every resource that matches the telemetry scope. The setting sends the resource's logs to the event hub in that region.

1. For VNet flow logs, Azure Policy adds a flow log to each matching virtual network. Azure writes the flow logs to the storage account for that region.

1. The telemetry pipeline signs in to Microsoft Entra ID (see the next section). It then reads the event hubs, reads new flow log files, and queries Azure Monitor for the metrics of the resources in scope.

1. The pipeline writes logs and flow logs to your log group, sends spans to X-Ray, and sends metrics to CloudWatch, using your writer role.

1. The telemetry in CloudWatch appears in CloudWatch Omni. See [Send telemetry to CloudWatch Omni](omni-send-telemetry.md).

### How CloudWatch authenticates to Azure
<a name="omni-send-platform-telemetry-from-microsoft-azure-how-cloudwatch-authenticates-to-azure"></a>

CloudWatch signs in to Microsoft Entra ID with workload identity federation. You store no Azure secret. For more information, see [Workload identity federation](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation) on the Microsoft Learn website.

1. **Outbound web identity federation** is turned on for your AWS account. It lets IAM issue tokens for the account from an issuer URL of the form `https://<id>.tokens.sts.global.api.aws`.

1. The **AWS CloudWatch Ingestion application** in Microsoft Entra ID has a federated credential that trusts tokens from that issuer for your connection role.

1. To call Azure, CloudWatch assumes the connection role, gets a token from IAM, and exchanges it with Microsoft Entra ID for an access token as the AWS CloudWatch Ingestion application.

1. The application's Azure role assignments decide what CloudWatch can read:


| Role | Scope | Assigned by | Used for | 
| --- | --- | --- | --- | 
| Reader | Tenant root management group | cloudwatch-azure-connection-setup.sh | Listing subscriptions and resources | 
| Monitoring Reader | Tenant root management group | cloudwatch-azure-connection-setup.sh | Reading Azure Monitor metrics | 
| Azure Event Hubs Data Receiver | Each event hub that setup creates | Bicep template | Reading resource logs and traces | 
| Storage Blob Data Reader | Each flow log storage account, both the ones setup creates and the ones you name | Bicep template | Reading VNet flow logs | 

The connection role can only get tokens for Microsoft Entra ID; it has no access to your AWS data. The writer role has no access to Azure.

## Choose how to set up
<a name="omni-send-platform-telemetry-from-microsoft-azure-choose-how-to-set-up"></a>


| Approach | What happens | Where to go | 
| --- | --- | --- | 
| Omni web UI | A three-step wizard guides you through setup. It generates the setup commands for your selections, makes the AWS API calls for you, checks the deployment, and shows the pipeline status. Only a Space Admin can set up Azure telemetry in the Omni web UI; see [Control access to your space](omni-control-access-to-your-space.md). | In the Omni web UI, open Settings › Ingestion, choose Azure as the cloud provider, and then choose Platform telemetry. | 
| AWS CLI and setup scripts | You run the same [setup scripts](#omni-send-platform-telemetry-from-microsoft-azure-setup-scripts) and call the same APIs yourself. Use this path to automate setup or to see what each step changes. | [Set up with the AWS CLI and the setup scripts](#omni-send-platform-telemetry-from-microsoft-azure-set-up-with-the-aws-cli-and-the-setup-scripts) | 

## Prerequisites
<a name="omni-send-platform-telemetry-from-microsoft-azure-prerequisites"></a>

**In AWS**
+ To collect traces, Transaction Search is enabled in the account and Region. See [Transaction Search](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html).
+ An AWS CLI version that includes the `aws observabilityadmin` connector commands.

**In Microsoft Entra ID and Azure**

Setup needs two kinds of permission. Microsoft Entra roles control what you can do in the directory, such as registering applications. Azure roles control what you can do with Azure resources, subscriptions, and management groups. They are assigned separately, and having one does not give you the other. See [Azure roles, Microsoft Entra roles, and classic subscription administrator roles](https://learn.microsoft.com/en-us/azure/role-based-access-control/rbac-and-directory-admin-roles) on the Microsoft Learn website.


| Script | Microsoft Entra role | Azure role at the tenant root management group | What the roles are used for | 
| --- | --- | --- | --- | 
| [`cloudwatch-azure-connection-setup.sh`](#omni-send-platform-telemetry-from-microsoft-azure-step-1-create-the-connection) | Cloud Application Administrator, Application Administrator, or Global Administrator | Owner, User Access Administrator, or Role Based Access Control Administrator | The Microsoft Entra role registers the two applications and creates their service principals and federated credentials. The Azure role assigns Reader and Monitoring Reader to the applications. | 
| [`cloudwatch-azure-telemetry-deploy.sh`](#omni-send-platform-telemetry-from-microsoft-azure-step-4-deploy-the-azure-resources) | None | Owner, or both Contributor and User Access Administrator | The template creates two kinds of things. Contributor covers the resource groups, Event Hubs namespaces, storage accounts, the deployment, and the remediation tasks, but it cannot create anything under Microsoft.Authorization. User Access Administrator covers the policy definitions, policy assignments, custom roles, and role assignments, but it cannot create resources. Owner covers both. | 
| [`cloudwatch-azure-aws-config-setup.sh`](#omni-send-platform-telemetry-from-microsoft-azure-step-4-deploy-the-azure-resources) (topology and resource tags) | Security Administrator or Global Administrator | Owner, or both Contributor and User Access Administrator | The Microsoft Entra role exports Microsoft Entra audit logs to an event hub; see [Stream Microsoft Entra logs to an event hub](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-stream-logs-to-event-hub) on the Microsoft Learn website. The Azure roles are used as for cloudwatch-azure-telemetry-deploy.sh. | 

If a role is eligible through Privileged Identity Management, activate it before you run the script. The `cloudwatch-azure-telemetry-deploy.sh` script also needs the `Microsoft.Insights` resource provider registered in the infrastructure subscription, the subscription that holds the Event Hubs namespaces and flow log storage accounts that setup creates. You choose it in [Step 3](#omni-send-platform-telemetry-from-microsoft-azure-step-3-define-the-telemetry-scope).

**Tools**

Bash, curl, and jq. For the scripts that run in Azure, also Azure CLI 2.47.0 or later with Bicep (`az bicep install`). Azure Cloud Shell has all of these.

## Availability
<a name="omni-send-platform-telemetry-from-microsoft-azure-availability"></a>

Azure vended telemetry is available in the Azure public cloud. In AWS, it is available in all Regions where CloudWatch Omni is available. For the list, see [Supported Regions for CloudWatch Omni](omni-supported-regions.md).

## Supported resource types
<a name="omni-send-platform-telemetry-from-microsoft-azure-supported-resource-types"></a>

You can name these resource types in the telemetry scope. Each telemetry type applies only to the resource types that support it, so one entry can name resource types from several rows. The telemetry scope rejects other resource types, and resources in the `global` location, such as Azure Front Door, are not supported.


| Telemetry type | Resource types | 
| --- | --- | 
| Resource logs and metrics | Microsoft.AAD/domainServices, Microsoft.AnalysisServices/servers, Microsoft.ApiManagement/service, Microsoft.App/containerApps, Microsoft.App/managedEnvironments, Microsoft.AppConfiguration/configurationStores, Microsoft.AppPlatform/Spring, Microsoft.AVS/privateClouds, Microsoft.Batch/batchAccounts, Microsoft.Cache/redis, Microsoft.CognitiveServices/accounts, Microsoft.ContainerInstance/containerGroups, Microsoft.ContainerRegistry/registries, Microsoft.ContainerService/managedClusters, Microsoft.Dashboard/grafana, Microsoft.DataFactory/factories, Microsoft.DBforMySQL/flexibleServers, Microsoft.DBforPostgreSQL/flexibleServers, Microsoft.Devices/IotHubs, Microsoft.Devices/provisioningServices, Microsoft.DigitalTwins/digitalTwinsInstances, Microsoft.DocumentDB/databaseAccounts, Microsoft.EventGrid/domains, Microsoft.EventGrid/systemTopics, Microsoft.EventGrid/topics, Microsoft.EventHub/namespaces, Microsoft.Insights/autoscaleSettings, microsoft.insights/components, Microsoft.KeyVault/vaults, Microsoft.Kusto/clusters, Microsoft.Logic/workflows, Microsoft.MachineLearningServices/workspaces, Microsoft.Network/applicationGateways, Microsoft.Network/azureFirewalls, Microsoft.Network/bastionHosts, Microsoft.Network/expressRouteCircuits, Microsoft.Network/loadBalancers, Microsoft.Network/natGateways, Microsoft.Network/publicIPAddresses, Microsoft.Network/virtualNetworkGateways, Microsoft.Network/virtualNetworks, Microsoft.OperationalInsights/workspaces, Microsoft.PowerBIDedicated/capacities, Microsoft.Purview/accounts, Microsoft.Relay/namespaces, Microsoft.Search/searchServices, Microsoft.ServiceBus/namespaces, Microsoft.ServiceNetworking/trafficControllers, Microsoft.SignalRService/SignalR, Microsoft.SignalRService/WebPubSub, Microsoft.Sql/managedInstances, Microsoft.Sql/servers/databases, Microsoft.StreamAnalytics/streamingjobs, Microsoft.Synapse/workspaces, Microsoft.Synapse/workspaces/bigDataPools, Microsoft.Synapse/workspaces/sqlPools, Microsoft.Web/sites, Microsoft.Web/sites/slots | 
| Resource logs only | Microsoft.Chaos/experiments, Microsoft.Databricks/workspaces, Microsoft.LoadTestService/loadTests, Microsoft.Network/networkSecurityGroups, Microsoft.NotificationHubs/namespaces | 
| Metrics only | Microsoft.BotService/botServices, Microsoft.Compute/disks, Microsoft.Compute/virtualMachines, Microsoft.Compute/virtualMachineScaleSets, Microsoft.Compute/virtualMachineScaleSets/virtualMachines, Microsoft.DataLakeAnalytics/accounts, Microsoft.DBforMariaDB/servers, Microsoft.DBforMySQL/servers, Microsoft.DBforPostgreSQL/servers, Microsoft.HDInsight/clusters, Microsoft.IoTCentral/IoTApps, Microsoft.Network/networkInterfaces, Microsoft.Network/privateEndpoints, Microsoft.Network/privateLinkServices, Microsoft.Network/virtualHubs, Microsoft.Sql/servers, Microsoft.Sql/servers/elasticPools, Microsoft.Storage/storageAccounts | 
| Traces | microsoft.insights/components. Traces come with its resource logs, and only its AppRequests and AppDependencies records become spans. Its other records, such as AppTraces, become log events. | 
| VNet flow logs | Microsoft.Network/networkInterfaces, Microsoft.Network/virtualNetworks, Microsoft.Network/virtualNetworks/subnets. Flow logs from subnets and network interfaces are collected only when you name those resources by resource ID. | 

## What setup creates
<a name="omni-send-platform-telemetry-from-microsoft-azure-what-setup-creates"></a>

The setup scripts never delete anything, and you can run each one again. Each script finds what it created earlier and changes only what is missing or different.


| Created by | Where | Resources | 
| --- | --- | --- | 
| cloudwatch-azure-connection-setup.sh | AWS | Outbound web identity federation for the account. The connection role, with the inline policy CloudWatchConnectorTokenExchange. The connection. The AWS Config connector, unless you pass --telemetry-only. | 
| cloudwatch-azure-connection-setup.sh | Microsoft Entra ID | The application AWS CloudWatch Ingestion <account-id>-<aws-region>, with Reader and Monitoring Reader at the tenant root management group. The application AWS Config <account-id>-<aws-region>, with Reader, unless you pass --telemetry-only. Each application has a service principal and a federated credential, and is created for each AWS account and Region that you connect. | 
| cloudwatch-azure-telemetry-deploy.sh | Azure tenant root management group | The policy aws-cloudwatch-ingestion-diaglogs-<account-id>-<aws-region>, which adds the diagnostic setting aws-cloudwatch-ingestion-<account-id>-<aws-region> to each resource in scope. For flow logs, the policies aws-cloudwatch-ingestion-flowlogs-<account-id>-<hash>, which add the flow log aws-cloudwatch-<hash> to each virtual network in scope that does not have a flow log yet. The custom roles AWS CloudWatch Ingestion Diagnostic Deployer, AWS CloudWatch Ingestion Event Hub ListKeys, and AWS CloudWatch Flow Log Deployer, which every connection in the tenant shares. | 
| cloudwatch-azure-telemetry-deploy.sh | Azure infrastructure subscription, in each region | The resource group aws-cloudwatch-ingestion-<account-id>-<aws-region>-<azure-region>. In it, the Event Hubs namespace aws-cloudwatch-<account-id>-<hash> with the event hub telemetry-event-hub, and, for flow logs, the storage account awscw<hash>. | 
| cloudwatch-azure-telemetry-deploy.sh | Your Azure resources | The diagnostic setting on each resource that you name by resource ID. For storage accounts that you name for flow logs, two tags and a Storage Blob Data Reader role assignment. | 
| cloudwatch-azure-aws-config-setup.sh | Azure | The resource group aws-cloudwatch-config-<account-id>-<aws-region>, with an Event Hubs namespace and the event hub activitylog. An Activity Log diagnostic setting in each subscription, and a diagnostic setting that exports Microsoft Entra audit logs. | 
| cloudwatch-azure-pipeline-writer-role-setup.sh | AWS | The writer role, with the inline policy CloudWatchAzureWrite-<pipeline-name>. | 
| You, or the Omni web UI | AWS | The log group, the telemetry pipeline, and, if you turn them on, the resource tag enrichment and the topology integration. | 

After the deployment, `cloudwatch-azure-telemetry-deploy.sh` starts an Azure Policy remediation task in each subscription in scope, so that resources that already exist get their diagnostic settings and flow logs. Azure Policy adds them to resources that you create later. For more information, see [Remediate non-compliant resources](https://learn.microsoft.com/en-us/azure/governance/policy/how-to/remediate-resources) on the Microsoft Learn website.

**Important**  
Azure charges apply for Event Hubs and storage. Deleting the connection in CloudWatch does not change anything in Azure, and charges continue until you delete these resources. See [Remove the connection](#omni-send-platform-telemetry-from-microsoft-azure-remove-the-connection).

## Setup scripts
<a name="omni-send-platform-telemetry-from-microsoft-azure-setup-scripts"></a>


| Script | Run it in | What it does | 
| --- | --- | --- | 
| [cloudwatch-azure-connection-setup.sh](https://d15oz3ou10so5h.cloudfront.net/azure/v1/cloudwatch-azure-connection-setup.sh) | AWS CloudShell, Azure Cloud Shell, or one shell signed in to both | Creates the AWS trust, the Microsoft Entra applications, the connection, and the AWS Config connector. See [Step 1](#omni-send-platform-telemetry-from-microsoft-azure-step-1-create-the-connection). | 
| [cloudwatch-azure-telemetry-deploy.sh](https://d15oz3ou10so5h.cloudfront.net/azure/v1/cloudwatch-azure-telemetry-deploy.sh) | Azure Cloud Shell, or a shell signed in to the Azure tenant | Deploys the generated Bicep template and starts Azure Policy remediation. See [Step 4](#omni-send-platform-telemetry-from-microsoft-azure-step-4-deploy-the-azure-resources). | 
| [cloudwatch-azure-aws-config-setup.sh](https://d15oz3ou10so5h.cloudfront.net/azure/v1/cloudwatch-azure-aws-config-setup.sh) | Azure Cloud Shell, or a shell signed in to the Azure tenant | For topology and resource tags. Creates the Azure resources that AWS Config reads. See [Step 4](#omni-send-platform-telemetry-from-microsoft-azure-step-4-deploy-the-azure-resources). | 
| [cloudwatch-azure-pipeline-writer-role-setup.sh](https://d15oz3ou10so5h.cloudfront.net/azure/v1/cloudwatch-azure-pipeline-writer-role-setup.sh) | AWS CloudShell, or a shell with AWS credentials | Creates or updates the writer role. See [Step 5](#omni-send-platform-telemetry-from-microsoft-azure-step-5-create-the-writer-role). | 

Download each script before you run it, for example:

```bash
curl -fsS --proto '=https' -o cloudwatch-azure-connection-setup.sh \
    https://d15oz3ou10so5h.cloudfront.net/azure/v1/cloudwatch-azure-connection-setup.sh
```

Each script prints its plan and asks you to confirm before it changes anything, so run it in an interactive terminal. Use `--dry-run` to see the plan without changing anything, and `--help` for all options.

## Set up with the AWS CLI and the setup scripts
<a name="omni-send-platform-telemetry-from-microsoft-azure-set-up-with-the-aws-cli-and-the-setup-scripts"></a>

The examples use the AWS account `111122223333`, the AWS Region `us-east-1`, and the connection name `my-azure-tenant`.

### Step 1: Create the connection
<a name="omni-send-platform-telemetry-from-microsoft-azure-step-1-create-the-connection"></a>

Decide first whether you want topology and resource tags ([Step 2](#omni-send-platform-telemetry-from-microsoft-azure-step-2-turn-on-topology-and-resource-tags-optional)). Both are on by default: `cloudwatch-azure-connection-setup.sh` creates the AWS Config application and the AWS Config connector that they use. If you want neither, pass `--telemetry-only` to each `cloudwatch-azure-connection-setup.sh` command. To add them later, run `cloudwatch-azure-connection-setup.sh` again without `--telemetry-only`; it keeps what already exists and adds the AWS Config application and connector.

The `cloudwatch-azure-connection-setup.sh` script runs three steps, in order:

1. `aws-identity` (AWS): turns on outbound web identity federation if it is off, and creates or updates the connection role.

1. `azure-identity` (Azure): creates the AWS CloudWatch Ingestion application, and the AWS Config application unless you pass `--telemetry-only`, each with its service principal, federated credential, and role assignments. It uses the tenant that the Azure CLI is signed in to.

1. `connectors` (AWS): creates the connection and, unless you pass `--telemetry-only`, the AWS Config connector. It then waits up to 10 minutes for Azure to apply the role assignments, checking that CloudWatch can read your tenant.

**In one shell** that has AWS credentials for the account and is signed in to the Azure tenant:

```
bash cloudwatch-azure-connection-setup.sh \
    --aws-region us-east-1 \
    --aws-role-name CloudWatchConnector \
    --connection-name my-azure-tenant
```

**In two shells.** In AWS CloudShell, run the AWS step:

```
bash cloudwatch-azure-connection-setup.sh --steps aws-identity \
    --aws-region us-east-1 \
    --aws-role-name CloudWatchConnector
```

From its JSON output, copy `aws.outboundIdentityFederation.issuer` and `aws.connectorRole.arn`. In Azure Cloud Shell, run the Azure step:

```
bash cloudwatch-azure-connection-setup.sh --steps azure-identity \
    --aws-region us-east-1 \
    --aws-issuer-url https://<id>.tokens.sts.global.api.aws \
    --aws-role-arn arn:aws:iam::111122223333:role/CloudWatchConnector
```

It prints the tenant ID, the AWS CloudWatch Ingestion application ID (`appId`), and the AWS Config application ID (`configAppId`). Back in AWS CloudShell, create the connection:

```
bash cloudwatch-azure-connection-setup.sh --steps connectors \
    --aws-region us-east-1 \
    --aws-role-name CloudWatchConnector \
    --connection-name my-azure-tenant \
    --azure-tenant-id <tenant-id> \
    --telemetry-app-id <appId> \
    --config-app-id <configAppId>
```

On success, the script prints one JSON object with `"status": "succeeded"` and the IDs and ARNs it created or found. It also writes a log file, `cloudwatch-azure-setup-<timestamp>.log`, in the current directory. If a step fails, fix the error that it names and run the same command again. The script keeps the steps that already finished.

The `cloudwatch-azure-connection-setup.sh` script stops when it finds an application with the expected name but without its tags, or more than one tagged application. It also stops when the AWS CloudWatch Ingestion application has any role at the tenant root management group other than Reader and Monitoring Reader.

#### Create the connection without the setup script
<a name="omni-send-platform-telemetry-from-microsoft-azure-create-the-connection-without-the-setup-script"></a>

To create the same resources with your own tooling, create the following.

**Connection role trust policy.** The `cloudwatch-azure-connection-setup.sh` script creates these two statements. It recognizes them by their `Sid` values, which include the Region.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "CloudWatchAzureConnectoruseast1Prod",
      "Effect": "Allow",
      "Principal": { "Service": "observabilityadmin.amazonaws.com" },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": { "aws:SourceAccount": "111122223333" },
        "ArnLike": { "aws:SourceArn": "arn:aws:observabilityadmin:us-east-1:111122223333:connector/*" }
      }
    },
    {
      "Sid": "CloudWatchAzureConnectorPipelineuseast1Prod",
      "Effect": "Allow",
      "Principal": { "Service": "telemetry-pipelines.observabilityadmin.amazonaws.com" },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

**Connection role inline policy** `CloudWatchConnectorTokenExchange`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sts:GetWebIdentityToken",
      "Resource": "*",
      "Condition": {
        "ForAllValues:StringEquals": { "sts:IdentityTokenAudience": "api://AzureADTokenExchange" },
        "Null": { "sts:IdentityTokenAudience": "false" }
      }
    }
  ]
}
```

The `cloudwatch-azure-connection-setup.sh` script and the Omni web UI support only a connection role at the IAM root path.

**Outbound web identity federation:** run `aws iam enable-outbound-web-identity-federation`. The `IssuerIdentifier` in the response is the issuer URL.

**AWS CloudWatch Ingestion application:** a single-tenant application and its service principal, with a federated credential whose issuer is the issuer URL, whose subject is the connection role ARN, and whose audience is `api://AzureADTokenExchange`. Assign the service principal Reader and Monitoring Reader at `/providers/Microsoft.Management/managementGroups/<tenant-id>`. To let `cloudwatch-azure-connection-setup.sh` adopt the application later, tag the application and the service principal `aws-cloudwatch-ingestion-account=<account-id>` and `aws-cloudwatch-ingestion-region=<aws-region>`.

**Connection:**

```bash
aws observabilityadmin create-connector \
    --name my-azure-tenant \
    --connector-configuration '{"Azure":{"TenantIdentifier":"<tenant-id>","ClientIdentifier":"<appId>"}}' \
    --role-arn arn:aws:iam::111122223333:role/CloudWatchConnector \
    --region us-east-1
```

Creating a connection checks only the format of the role ARN. It does not use the role or call Azure, so a successful call does not mean that CloudWatch can reach your tenant. Run the check in the next section. An AWS account can have one connection for each Azure tenant in each Region. You cannot change a connection after you create it; to change its tenant, application, or role, delete it and create a new one.

#### Check that CloudWatch can read your tenant
<a name="omni-send-platform-telemetry-from-microsoft-azure-check-that-cloudwatch-can-read-your-tenant"></a>

```bash
aws observabilityadmin list-resources-by-connector \
    --connector-identifier arn:aws:observabilityadmin:us-east-1:111122223333:connector/azure/<connector-id> \
    --selector '{"Azure":{"Subscriptions":{}}}' \
    --max-results 1
```

This call signs in to Azure the same way the pipeline does. A subscription in the result means the connection works. If the call fails, its message names the step that failed and what to fix. Azure can take several minutes to apply new role assignments.

### Step 2: Turn on topology and resource tags (optional)
<a name="omni-send-platform-telemetry-from-microsoft-azure-step-2-turn-on-topology-and-resource-tags-optional"></a>

Topology adds your Azure resources to the application map. Resource tags add your Azure resource tags to the logs and metrics from this connection. Both need an AWS Config connector for your tenant. In [Step 4](#omni-send-platform-telemetry-from-microsoft-azure-step-4-deploy-the-azure-resources), you also run `cloudwatch-azure-aws-config-setup.sh`, which creates the Azure resources that AWS Config reads.

1. Create the AWS Config connector. Unless you passed `--telemetry-only`, `cloudwatch-azure-connection-setup.sh` already created it, with the AWS Config application, and printed its ARN under `connectors.awsConfig.arn`. If you passed `--telemetry-only`, run `cloudwatch-azure-connection-setup.sh` again without it. To create the connector without the script, create the AWS Config application first, then run:

```bash
aws configservice put-connector \
    --connector-configuration '{"azure":{"tenantIdentifier":"<tenant-id>","clientIdentifier":"<configAppId>"}}'
```

The response returns the ARN of the AWS Config connector.

1. To add resource tags, start an enrichment with the ARN of the AWS Config connector:

```bash
aws observabilityadmin start-third-party-telemetry-enrichment \
    --name azure-<tenant-id> \
    --telemetry-source-configuration '{"Azure":{"AwsConfigConnectorArn":"<config-connector-arn>"}}'
```

Check its status with `get-third-party-telemetry-enrichment --telemetry-enrichment-identifier azure-<tenant-id>`. The statuses are `Initializing`, `Running`, `Stopped`, and `Impaired`. Tags appear on telemetry about 10 minutes after the enrichment is running.

1. To add topology, call the CloudWatch Omni `CreateIntegration` API with the ARN of the AWS Config connector. The name must be unique in the account; the Omni web UI uses `Azure resource topology <config-connector-id>`.

```json
{
  "integrationType": "AWS_CONFIG_AZURE_SLREC",
  "name": "Azure resource topology <config-connector-id>",
  "integrationAttributes": { "connectorArn": "<config-connector-arn>" }
}
```

Call `GetIntegration` with the returned `integrationId` until the status changes from `PENDING` to `ACTIVE`. If the status is `ERROR` or `FAILED`, delete the integration with `DeleteIntegration` and create it again. Each AWS Config connector can have one topology integration. See [Using AWS Config for resource discovery](omni-using-aws-config-for-resource-discovery.md).

### Step 3: Define the telemetry scope
<a name="omni-send-platform-telemetry-from-microsoft-azure-step-3-define-the-telemetry-scope"></a>

The telemetry scope has two parts:
+ **`Source.Azure`**: a list of up to 100 entries. Each entry has `TelemetryTypes` (one or more of `ResourceLogs`, `Metrics`, and `FlowLogs`) and a `Scope`. A scope either names `Subscriptions`, `Regions`, and `ResourceTypes` together, with optional `TagFilters`, or lists `Resources` by region and resource ID. Traces do not have their own type; they come with `ResourceLogs`.
+ **`Infrastructure.Azure`**: where and how setup creates the collection resources.
  + `SubscriptionId`: the *infrastructure subscription*, which holds the Event Hubs namespaces and the flow log storage accounts that setup creates. It can differ from the subscriptions that you collect from. Required when you collect `ResourceLogs`, or `FlowLogs` with storage that setup creates.
  + `EventHubs`: one entry, `{"Tier": "Standard" | "Premium", "PartitionCount": n}`. The default is Standard with 16 partitions. Basic tier is not supported.
  + `FlowLogs`: `{"AwsManaged": {"RetentionDays": n}}` to have setup create a storage account in each region, or `{"CustomerManaged": {"StorageAccounts": [{"Region": "...", "StorageAccountIds": ["..."]}]}}` to use your own storage accounts. Required when you collect `FlowLogs`.

The following telemetry scope collects resource logs and metrics from four resource types in two regions of every subscription, and VNet flow logs from one subscription:

```json
{
  "Source": {
    "Azure": [
      {
        "TelemetryTypes": ["ResourceLogs", "Metrics"],
        "Scope": {
          "Subscriptions": { "All": {} },
          "Regions": ["eastus", "westeurope"],
          "ResourceTypes": ["Microsoft.Web/sites", "Microsoft.KeyVault/vaults", "microsoft.insights/components", "Microsoft.Compute/virtualMachines"]
        }
      },
      {
        "TelemetryTypes": ["FlowLogs"],
        "Scope": {
          "Subscriptions": { "Ids": ["<subscription-id>"] },
          "Regions": ["eastus"],
          "ResourceTypes": ["Microsoft.Network/virtualNetworks"]
        }
      }
    ]
  },
  "Infrastructure": {
    "Azure": {
      "SubscriptionId": "<infrastructure-subscription-id>",
      "EventHubs": [{ "Tier": "Standard", "PartitionCount": 16 }],
      "FlowLogs": { "AwsManaged": { "RetentionDays": 7 } }
    }
  }
}
```

Save it as `scope.json`, then store it on the connection:

```bash
aws observabilityadmin put-connector-telemetry-manifest \
    --connector-identifier <connector-arn> \
    --manifest file://scope.json
```

The response returns a `Version`. When you change the telemetry scope later, pass the version that you read with `get-connector-telemetry-manifest` as `--expected-version`, so that you do not overwrite a change that someone else made in the meantime.

### Step 4: Deploy the Azure resources
<a name="omni-send-platform-telemetry-from-microsoft-azure-step-4-deploy-the-azure-resources"></a>

1. Generate the Bicep files for the stored telemetry scope, and write them to a directory:

```bash
aws observabilityadmin get-connector-telemetry-setup \
    --connector-identifier <connector-arn> \
    --format BICEP > setup.json

jq -c '.Artifacts[]' setup.json | while read -r artifact; do
    file="azure-setup/$(jq -r '.FileName' <<<"$artifact")"
    mkdir -p "$(dirname "$file")"
    jq -r '.Content' <<<"$artifact" > "$file"
done
```

The files are `main.bicep` and the modules it uses, under `modules/`. The response also returns `ManifestVersion`, the version of the telemetry scope that the files were generated from.

1. Copy the `azure-setup` directory to Azure Cloud Shell, or to a shell signed in to the tenant, and run `cloudwatch-azure-telemetry-deploy.sh`:

```
bash cloudwatch-azure-telemetry-deploy.sh \
    --client-id <appId> \
    --tenant-id <tenant-id> \
    --connector-id <connector-id> \
    --location eastus \
    --template-file azure-setup/main.bicep
```
+ `--connector-id` is the last part of the connection ARN. Running the script again for the same connection updates the same deployment.
+ `--location` is the Azure region where Azure stores the deployment and the policy assignments. Only the first deployment for a connection uses it; later runs keep the region of the existing deployment.

The `cloudwatch-azure-telemetry-deploy.sh` script checks that the Azure CLI is signed in to the tenant, that `Microsoft.Insights` is registered in the infrastructure subscription, and that you have the permissions it needs. It then validates and deploys the template at the tenant root management group. When the deployment succeeds, it starts a policy remediation task in each subscription in scope.

1. If you turned on topology or resource tags, run `cloudwatch-azure-aws-config-setup.sh` in the same shell, with the AWS Config application ID from `cloudwatch-azure-connection-setup.sh`. It does not depend on `cloudwatch-azure-telemetry-deploy.sh`.

```
bash cloudwatch-azure-aws-config-setup.sh \
    --tenant-id <tenant-id> \
    --config-app-id <configAppId> \
    --aws-account-id 111122223333 \
    --aws-region us-east-1 \
    --location eastus \
    --hub-subscription-id <infrastructure-subscription-id>
```

AWS Config reads every enabled subscription that its application can read. `--hub-subscription-id` only chooses where the Activity Log event hub is created.

1. Check that the event hubs exist. For each region that collects resource logs:

```bash
aws observabilityadmin list-resources-by-connector \
    --connector-identifier <connector-arn> \
    --selector '{"Azure":{"EventHubs":{"Region":"eastus","Scope":{"SubscriptionIds":["<infrastructure-subscription-id>"]}}}}'
```

The result lists `telemetry-event-hub` in the namespace `aws-cloudwatch-111122223333-<hash>`. This is the check that **Verify deployment** runs in the Omni web UI. It does not check diagnostic settings or flow logs.

1. In Azure, check that the remediation tasks finished. In the Azure portal, open **Policy › Remediation**, or run `az policy remediation list --subscription <subscription-id>`. Resources that remediation has not reached yet do not send logs.

### Step 5: Create the writer role
<a name="omni-send-platform-telemetry-from-microsoft-azure-step-5-create-the-writer-role"></a>

The writer role lets the pipeline write to your log group, CloudWatch metrics, and X-Ray. Run `cloudwatch-azure-pipeline-writer-role-setup.sh` in a shell with AWS credentials:

```
bash cloudwatch-azure-pipeline-writer-role-setup.sh \
    --writer-role-arn arn:aws:iam::111122223333:role/CloudWatchAzurePipelineWriter-my-azure-tenant \
    --aws-region us-east-1 \
    --pipeline-name my-azure-tenant-telemetry \
    --log-group-name /az/my-azure-tenant-telemetry
```

The `cloudwatch-azure-pipeline-writer-role-setup.sh` script adds a trust statement for the CloudWatch telemetry pipeline service and the inline policy `CloudWatchAzureWrite-<pipeline-name>`. It keeps any statements that the role already has. To create the role yourself, use this trust policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "CloudWatchAzurePipelineuseast1Prod",
      "Effect": "Allow",
      "Principal": { "Service": "telemetry-pipelines.observabilityadmin.amazonaws.com" },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

And this permissions policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["logs:CreateLogStream", "logs:PutLogEvents"],
      "Resource": ["arn:aws:logs:us-east-1:111122223333:log-group:/az/my-azure-tenant-telemetry:*"]
    },
    {
      "Effect": "Allow",
      "Action": "cloudwatch:PutMetricData",
      "Resource": "*",
      "Condition": { "StringEquals": { "aws:RequestedRegion": "us-east-1" } }
    },
    {
      "Effect": "Allow",
      "Action": ["xray:PutTraceSegments", "xray:PutTelemetryRecords"],
      "Resource": "*",
      "Condition": { "StringEquals": { "aws:RequestedRegion": "us-east-1" } }
    }
  ]
}
```

The logs statement names the pipeline's log group. To write to another log group, run `cloudwatch-azure-pipeline-writer-role-setup.sh` again with the new `--log-group-name`. The script adds the log group to the policy and keeps the ones already there.

### Step 6: Create the telemetry pipeline
<a name="omni-send-platform-telemetry-from-microsoft-azure-step-6-create-the-telemetry-pipeline"></a>

1. Create the log group. The pipeline creates its log streams but not the log group.

```bash
aws logs create-log-group --log-group-name /az/my-azure-tenant-telemetry
```

1. Save the pipeline configuration as `pipeline.yaml`. The source names the connection, and the sink names the writer role and one destination for each signal. All three destinations are required, and processors are not supported.

```yaml
pipeline:
  source:
    cloudwatch_connector:
      connector_arn: "arn:aws:observabilityadmin:us-east-1:111122223333:connector/azure/<connector-id>"
  processor: []
  sink:
    sink_role_arn: "arn:aws:iam::111122223333:role/CloudWatchAzurePipelineWriter-my-azure-tenant"
    cloudwatch_logs:
      - log_group: "/az/my-azure-tenant-telemetry"
    cloudwatch_metrics:
      format: otlp
    cloudwatch_traces:
      - format: otlp
```

1. Create the pipeline. The name must start with a lowercase letter and have 3 to 28 lowercase letters, numbers, and hyphens.

```bash
aws observabilityadmin create-telemetry-pipeline \
    --name my-azure-tenant-telemetry \
    --configuration "$(jq -n --rawfile body pipeline.yaml '{Body: $body}')"
```

1. Wait for the pipeline status to become `ACTIVE`:

```bash
aws observabilityadmin get-telemetry-pipeline \
    --pipeline-identifier my-azure-tenant-telemetry
```

### Step 7: Verify that telemetry arrives
<a name="omni-send-platform-telemetry-from-microsoft-azure-step-7-verify-that-telemetry-arrives"></a>

1. `get-telemetry-pipeline` shows the status `ACTIVE`, and `SourceProgress.Active` equals `SourceProgress.Total`.

1. In CloudWatch metrics, the namespace `AWS/Observability Admin` shows `PipelineRecordsIn` (logs, traces, and flow logs) or `PipelineDataPointsIn` (metrics) for your pipeline. See [Monitor the pipeline](#omni-send-platform-telemetry-from-microsoft-azure-monitor-the-pipeline).

1. **Logs:** the log group has the stream `<pipeline-id>-stream`.

1. **VNet flow logs:** the stream `<pipeline-id>-vnet-flowlog-stream` appears one to two hours after Azure writes the first flow log.

1. **Metrics:** each Azure metric becomes one metric for each aggregation, named `<Azure metric name>_<aggregation>`, for example `Percentage CPU_average`. The metrics carry `cloud.provider` (`azure`), `cloud.resource_id`, `cloud.account.id` (the subscription ID), and `cloud.region`, and the Azure dimensions.

1. **Traces:** in Transaction Search, the spans carry `cloud.provider` `azure`, and `service.name` from the Application Insights role name.

1. **CloudWatch Omni:** the logs, traces, and metrics appear in your space.

1. **Topology and resource tags:** if you turned them on, `GetIntegration` shows `ACTIVE` and your Azure resources appear on the application map, and the enrichment status is `Running`.

## Change what you collect
<a name="omni-send-platform-telemetry-from-microsoft-azure-change-what-you-collect"></a>

When you update the telemetry scope with `put-connector-telemetry-manifest`, deploy it again as in [Step 4](#omni-send-platform-telemetry-from-microsoft-azure-step-4-deploy-the-azure-resources), then refresh the pipeline. The pipeline does not pick up a changed telemetry scope until you refresh it.

```bash
aws observabilityadmin start-telemetry-pipeline-refresh \
    --pipeline-identifier my-azure-tenant-telemetry
```

Removing something from the scope removes nothing in Azure. The updated policy stops adding diagnostic settings to resources outside the scope, but the settings, flow logs, event hubs, and storage accounts that exist stay until you delete them. Run the updated deployment first, then remove what is no longer needed. The Omni web UI lists these resources when you apply the change.

## Monitor the pipeline
<a name="omni-send-platform-telemetry-from-microsoft-azure-monitor-the-pipeline"></a>

The pipeline publishes metrics to your account every minute in the namespace `AWS/Observability Admin`, with the dimension `PipelineName`. Each metric is also published for each source, with a `Source` dimension. For an event hub, `Source` is the event hub's resource ID; for flow logs and metrics, it names the Azure region.


| Data | `Signal` | Metrics | 
| --- | --- | --- | 
| Reading the event hubs (logs and traces together) | none | PipelineRecordsIn and PipelineBytesIn: log records and spans read, and their bytes. PipelineRecordsUnprocessed: records that could not be parsed, had an invalid timestamp, or did not fit in the buffer. | 
| Resource logs | LOGS | PipelineRecordsOut and PipelineBytesOut: log events that CloudWatch Logs accepted. PipelineRecordsUnprocessed: log events that could not be delivered. | 
| Traces | TRACES | PipelineRecordsOut and PipelineBytesOut: spans that X-Ray accepted. PipelineRecordsUnprocessed: spans dropped because Transaction Search is disabled. | 
| VNet flow logs | FLOW\_LOGS | PipelineRecordsIn and PipelineBytesIn: records read from storage, and their bytes. PipelineRecordsOut and PipelineBytesOut: records that CloudWatch Logs accepted. PipelineRecordsUnprocessed: records that were malformed, too large, or could not be delivered. | 
| Platform metrics | METRICS | PipelineDataPointsIn: data points made from the Azure Monitor responses. PipelineDataPointsOut and PipelineBytesOut: data points that CloudWatch accepted, and their bytes. PipelineDataPointsUnprocessed: data points that the pipeline dropped. | 

`PipelineErrors` and `PipelineWarnings` count errors and warnings. `PipelineErrorsByErrorType` and `PipelineWarningsByWarningType` break them down with the dimension `ErrorType` or `WarningType`. Errors count failed requests, files, or batches, not records; to see how much data did not arrive, use the unprocessed metrics. Errors and warnings from writing resource logs carry no `Signal` dimension.


| `ErrorType` | Applies to | Cause and what to do | 
| --- | --- | --- | 
| ACCESS\_DENIED | All | A request was denied. For metrics, the AWS CloudWatch Ingestion application is missing Monitoring Reader, so that window of data is dropped, or Reader on the subscription, so resources cannot be found. For flow logs, the application is missing Storage Blob Data Reader on the storage account, or a storage firewall blocks it. For delivery, the writer role's permissions policy does not allow the write. Check the roles in [How CloudWatch authenticates to Azure](#omni-send-platform-telemetry-from-microsoft-azure-how-cloudwatch-authenticates-to-azure) and the writer role in [Step 5](#omni-send-platform-telemetry-from-microsoft-azure-step-5-create-the-writer-role). | 
| RESOURCE\_NOT\_FOUND | Metrics, logs, flow logs | For metrics, the resource was deleted or its resource provider is not registered. For logs and flow logs, the log group does not exist. For flow logs, Azure also reports it when no flow log has been written to the storage account yet, or when a file was deleted before the pipeline read it. | 
| TRANSACTION\_SEARCH\_DISABLED | Traces | Transaction Search is not enabled, so X-Ray dropped the spans. Enable Transaction Search. | 
| CARDINALITY\_LIMIT\_EXCEEDED | Metrics | An Azure Monitor response reached 1,000 series for one metric of one resource. Series beyond the first 1,000 are not collected. The error counts responses, not series. To raise the limit for a resource type, contact AWS Support. | 
| PARTIAL\_BATCH\_REJECTED | Metrics | CloudWatch rejected some data points, for example at the account limit on new metric series. They are not sent again. To raise the account limit, contact AWS Support. | 
| PAYLOAD\_SIZE\_EXCEEDED, INVALID\_REQUEST | All (INVALID\_REQUEST: logs and flow logs) | A request was too large for the destination, or was invalid. The data was dropped. | 
| ALL | All | Any other failure that lost data, such as a failed sign-in to Microsoft Entra ID, a failed request to Azure, or a batch that the destination rejected. For metrics and traces, ALL also counts the delivery errors that have their own type, so do not add error types together. Run the check in [Check that CloudWatch can read your tenant](#omni-send-platform-telemetry-from-microsoft-azure-check-that-cloudwatch-can-read-your-tenant). | 


| `WarningType` | Applies to | Meaning | 
| --- | --- | --- | 
| THROTTLED | Logs, traces, flow logs, metrics | Azure Monitor or CloudWatch throttled a request, and the pipeline retried it. The data is delayed, not lost, unless the last retry to deliver metrics or traces was throttled. Then the data is dropped and also counted in the ALL error. | 
| APPROACHING\_RESOURCE\_LIMITS | Metrics | The pipeline found more than 1,000 resources in one Azure region. Nothing is lost, but metrics might be delayed. | 

**Important**  
The pipeline publishes no error metric when it cannot read an event hub, for example when the AWS CloudWatch Ingestion application lost Azure Event Hubs Data Receiver or cannot sign in to Microsoft Entra ID. The only sign is that `PipelineRecordsIn` and `PipelineBytesIn` for that event hub stay at zero. Compare them with the **Incoming Messages** and **Outgoing Messages** metrics of the Event Hubs namespace in Azure Monitor.

## Limits
<a name="omni-send-platform-telemetry-from-microsoft-azure-limits"></a>


| Area | Limits | 
| --- | --- | 
| Account and Region | 50 connections. 30 telemetry pipelines with an external cloud source. 5 requests per second for each connector API (CreateConnector, DeleteConnector, GetConnector, ListConnectors, PutConnectorTelemetryManifest, GetConnectorTelemetryManifest, GetConnectorTelemetrySetup, and ListResourcesByConnector), and for CreateTelemetryPipeline. | 
| Connection | 1 connection for each Azure tenant in an account and Region. 1 pipeline for each connection. | 
| Pipeline | 30 sources. Each event hub, each flow log storage account, and each Azure region that you collect metrics from is one source. The pipeline name has 3 to 28 characters. | 
| Telemetry scope | 100 entries per connection. In each entry: 1 to 1,000 subscriptions, or all; 1 to 100 regions; 1 to 100 resource types, with no option for all types; 1 to 1,000 resource IDs per region; and 1 to 50 tag filters. A new Azure region is rejected until CloudWatch supports it. | 
| Tag filters | Exact match only, and values are case-sensitive. A resource matches when every key matches, and a key matches when any of its values matches. Exclude, prefix, and wildcard filters are not supported. | 
| Metrics | All dimensions that Azure publishes for a metric are collected. Up to 1,000 series per metric per resource; the rest are not collected (CARDINALITY\_LIMIT\_EXCEEDED). Above 1,000 resources in one Azure region, metrics might be delayed (APPROACHING\_RESOURCE\_LIMITS). Data arrives about 4 minutes or more after Azure records it, at 1-minute granularity at best. New resources are picked up within an hour, with no earlier history. Delivery is at least once, so a retried window can be counted twice. | 
| Resource logs and traces | Event Hubs Standard (1 to 32 partitions) or Premium (1 to 100 partitions), with one setting for all regions. After the event hubs exist, you cannot change the tier, the infrastructure subscription, or the Standard partition count, and you cannot lower the Premium partition count. Up to 20 named subscriptions across all ResourceLogs entries; to collect from more, use all subscriptions. All entries share one collection policy, so a resource ID can be listed only once for the same telemetry type. Event hubs keep events for 7 days. On its first run, the pipeline reads each event hub from its oldest event. | 
| VNet flow logs | Your own storage accounts: up to 100 regions and 100 storage accounts per region, each listed once. Storage that setup creates: one storage account per region in the infrastructure subscription, which keeps flow logs for 1 to 365 days. The pipeline reads new flow log files once an hour, starting from the most recent complete hour. | 

Azure platform metrics count toward the CloudWatch limit on new metric series for the account. Data points for new series over the limit are dropped (`PARTIAL_BATCH_REJECTED`) and are not sent again. The limit is most likely to apply when you first connect a tenant with many resources. See [OTLP endpoints](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OTLPEndpoint.html).

## Remove the connection
<a name="omni-send-platform-telemetry-from-microsoft-azure-remove-the-connection"></a>

To avoid ongoing charges, delete these resources in the following order. Until you delete them, the telemetry pipeline keeps sending logs, metrics, and traces to CloudWatch, and Azure keeps charging for the Event Hubs namespaces and the flow log storage accounts. If a step stops partway, run it again.

1. Delete the pipeline, and wait until `get-telemetry-pipeline` returns `ResourceNotFoundException`:

```bash
aws observabilityadmin delete-telemetry-pipeline --pipeline-identifier my-azure-tenant-telemetry
```

1. If you turned on resource tags, stop the enrichment with `stop-third-party-telemetry-enrichment`. This deletes its AWS Config service-linked configuration recorder.

1. If you turned on topology, delete the topology integration with `DeleteIntegration`.

1. Delete the connection. This fails with `This connector cannot be deleted because it is in use by pipelines: <ids>.` while a pipeline uses it.

```bash
aws observabilityadmin delete-connector --connector-identifier <connector-arn>
```

Deleting the connection deletes its telemetry scope. It does not delete the connection role, the writer role, the log group, outbound web identity federation, or the AWS Config connector, and it changes nothing in Azure. The Omni web UI deletes the pipeline, the enrichment, the topology integration, and the connection in the same order, and gives you a list of the Azure resources that the connection created.

Then remove the Azure resources, in this order, so that Azure Policy stops creating settings that point at deleted event hubs:

1. At the tenant root management group, delete the policy assignments `aws-cw-<hash>` for the policy definitions `aws-cloudwatch-ingestion-diaglogs-<account-id>-<aws-region>` and `aws-cloudwatch-ingestion-flowlogs-<account-id>-<hash>`, and the role assignments of their managed identities.

1. Delete the diagnostic setting `aws-cloudwatch-ingestion-<account-id>-<aws-region>` from each resource.

1. Delete the flow logs `aws-cloudwatch-<hash>` under `NetworkWatcher_<region>` in `NetworkWatcherRG` of each subscription. Flow logs that existed before setup are not affected.

1. Delete the resource groups `aws-cloudwatch-ingestion-<account-id>-<aws-region>-<azure-region>` in the infrastructure subscription. This deletes the Event Hubs namespaces, the event hubs, and the flow log storage accounts that setup created.

1. For storage accounts that you named for flow logs, remove the AWS CloudWatch Ingestion application's Storage Blob Data Reader role assignment and the two tags that setup added.

1. Delete the policy definitions.

1. Delete the AWS CloudWatch Ingestion application, or remove its federated credential and its Reader and Monitoring Reader role assignments.

Keep the custom roles `AWS CloudWatch Ingestion Diagnostic Deployer`, `AWS CloudWatch Ingestion Event Hub ListKeys`, and `AWS CloudWatch Flow Log Deployer` while another connection in the tenant uses them. Keep the AWS Config application and the resources that `cloudwatch-azure-aws-config-setup.sh` created while another AWS service uses the tenant's AWS Config connector.