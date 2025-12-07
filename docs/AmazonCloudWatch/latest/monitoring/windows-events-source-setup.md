# Source configuration for Microsoft Windows Events

## Integrating with Windows Event

Microsoft Windows Event Logs provide a comprehensive logging system that records system, security, and application events on Windows operating systems. CloudWatch Pipeline uses the Log Analytics API to retrieve information about system operations, security events, user activities, and application behaviors from Windows servers and workstations. The Log Analytics API enables access to event data through KQL (Kusto Query Language) queries, allowing retrieval of Windows Event logs from Log Analytics workspaces.

## Authenticating with Windows Event

To read Windows Event audit Logs, the pipeline needs to authenticate with your account. The plugin supports OAuth2 Authentication. Follow these instructions to get started with Microsoft Windows Event: Log Analytics APIs.

- Register an application in Azure with Supported account types, Accounts in this organizational directory only (Single tenant). After registration is complete, note down the Application (client) ID and Directory (tenant) ID.
- Generate a new client secret for your application. The client secret is used when exchanging an authorization code for an access token. Copy the secret value immediately as it won't be shown again.
- In the AWS Secrets Manager, create a secret and store the Application (client) ID under the key `client_id` and the client secret under the key `client_secret`.
- Specify the API permissions your application requires to access the Log Analytics API. The permission you need is: Data.Read: Required to execute KQL queries and read log data from Log Analytics workspaces, including Windows Event logs.
- Create and configure a Log Analytics Workspace: Create a workspace in Azure portal (Monitor → Log Analytics workspaces). Create a Data Collection Rule (DCR) to specify which Windows Event Logs to collect (System, Application, Security). Connect your Windows servers/VMs to the workspace through the DCR. Note down your Workspace ID from the workspace Overview page (required for API queries)
- Grant workspace access to your application: Navigate to your Log Analytics workspace → Access control (IAM). Assign the Log Analytics Reader role to your registered application. This RBAC role works together with the API permission to provide secure access: OAuth confirms API usage rights, while IAM confirms workspace data access rights.

## Configuring the CloudWatch Pipeline

When configuring the pipeline to read logs, choose Microsoft Windows Events as the data source. Fill in the required information like Tenant Id using Directory (tenant) ID and Workspace Id (workspace_id). Once you create the pipeline, data will be available in the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes

This integration supports OCSF schema version v1.5.0 and Windows audit events that map to Account Change (3001), Authentication (3002), Entity Management (3004), Event Log Activity (1008), File System Activity (1001), Group Management (3006), and Kernel Activity (1003).

**Account Change** contains the following events:

- 4740

**Authentication** contains the following events:

- 4624
- 4625
- 4634
- 4647
- 4648
- 4649
- 4672

**Entity Management** contains the following events:

- 4616
- 4907
- 4719
- 4902

**Event Log Activity** contains the following events:

- 1100
- 1102
- 1104
- 1105

**File System Activity** contains the following events:

- 4608
- 4660
- 4688
- 4696
- 4826
- 5024
- 5033
- 5058
- 5059
- 5061
- 5382
- 5379

**Group Management** contains the following events:

- 4732
- 4798
- 4799
- 4733
- 4731
- 4734
- 4735

**Kernel Activity** contains the following events:

- 4674
