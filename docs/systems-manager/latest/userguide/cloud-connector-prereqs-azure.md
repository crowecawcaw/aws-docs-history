# Azure prerequisites

Complete the following steps in your Azure environment. You need the following
values from the AWS prerequisites:

- **Issuer URL** — The AWS OIDC issuer URL
  from the previous section.
- **Subject** — The ARN of the Systems Manager Azure
  federation role, for example:
  `arn:aws:iam::`ACCOUNT_ID`:role/service-role/SSM-AzureRole-`connector-name``

###### To set up the Azure side of the federation

1. ###### Create an Azure Entra ID application

Create an application registration in Microsoft Entra ID (formerly Azure
Active Directory). Note the _Application (client)
ID_ from the output.

```
az ad app create --display-name "`AWSSSMAzureIntegration`" --query appId
```

2. ###### Create a service principal for the application

Create a service principal associated with the application. The command
output includes an `id` field, which is the service principal's
object ID. Note this `id` (object ID) value. It is the
`SERVICE_PRINCIPAL_ID` that you use later as
the `--assignee` in the role-assignment steps (Step 5).

```
az ad sp create --id `APPLICATION_ID`
```

3. ###### Add a federated identity credential

Add a federated identity credential to the application that trusts the
AWS OIDC issuer. This allows Azure to accept tokens issued by AWS on
behalf of the Systems Manager Azure federation role (see [Azure federation role](cloud-connector-azure-federation-role.md "cloud-connector-azure-federation-role.md")).

```
az ad app federated-credential create \
    --id `APPLICATION_ID` \
    --parameters "{
        \"name\": \"aws-ssm-federation\",
        \"issuer\": \"`AWS_OIDC_ISSUER_URL`\",
        \"subject\": \"arn:aws:iam::`ACCOUNT_ID`:role/service-role/SSM-AzureRole-`CONNECTOR_NAME`\",
        \"audiences\": [\"api://AzureADTokenExchange\"]
    }"
```

Replace:

    * `APPLICATION_ID` — The application
     (client) ID from Step 1.
    * `AWS_OIDC_ISSUER_URL` — The AWS OIDC
     issuer URL (for example,
     `https://a1667813-695b-5415-b0f7-d473d62bb123.tokens.sts.global.api.aws`).
    * `ACCOUNT_ID` — Your AWS account
     ID.
    * `CONNECTOR_NAME` — The name component
     of the Systems Manager Azure federation role. On the AWS CLI or API path, you
     create this role yourself before you create the Cloud Connector, so
     you choose its name. Use the same role ARN for this
     `subject` that you use for `--role-arn` in the
     [Step 2: Create a Systems Manager Cloud Connector](cloud-connector-create-ssm-connector.md "cloud-connector-create-ssm-connector.md") step. For
     the role's trust and permissions policies, see [Azure federation role](cloud-connector-azure-federation-role.md "cloud-connector-azure-federation-role.md").

4. ###### Create the VM Run Command custom role

Create a custom role that grants the minimum permissions
required for Systems Manager to run commands on Azure VMs. Replace
`SUBSCRIPTION_ID` with the Azure subscription
ID you want to manage.

```
az role definition create --role-definition '{
    "Name": "AWSSSMVMExtensionRole-`SUBSCRIPTION_ID`",
    "Description": "Allows AWS Systems Manager to run commands on Azure VMs",
    "Actions": [
        "Microsoft.Compute/virtualMachines/read",
        "Microsoft.Compute/virtualMachines/runCommand/action",
        "Microsoft.Compute/virtualMachines/runCommands/*"
    ],
    "AssignableScopes": [
        "/subscriptions/`SUBSCRIPTION_ID`"
    ]
}'
```

For tenant-level scope (all subscriptions in the tenant), use a
management group scope instead:

```
az role definition create --role-definition '{
    "Name": "AWSSSMVMExtensionRole-`TENANT_ID`",
    "Description": "Allows AWS Systems Manager to run commands on Azure VMs",
    "Actions": [
        "Microsoft.Compute/virtualMachines/read",
        "Microsoft.Compute/virtualMachines/runCommand/action",
        "Microsoft.Compute/virtualMachines/runCommands/*"
    ],
    "AssignableScopes": [
        "/providers/Microsoft.Management/managementGroups/`TENANT_ID`"
    ]
}'
```

To verify the role was created:

```
az role definition list --name "AWSSSMVMExtensionRole-`SUBSCRIPTION_ID`" --output table
```

5. ###### Assign the VM Run Command role to the service principal

Assign the custom role to the service principal you created in Step 2.
The scope determines which Azure resources Systems Manager can manage.

For subscription-level scope (repeat for each subscription):

```
az role assignment create \
    --assignee `SERVICE_PRINCIPAL_ID` \
    --role "AWSSSMVMExtensionRole-`SUBSCRIPTION_ID`" \
    --scope "/subscriptions/`SUBSCRIPTION_ID`"
```

For management group-level scope:

```
az role assignment create \
    --assignee `SERVICE_PRINCIPAL_ID` \
    --role "AWSSSMVMExtensionRole-`TENANT_ID`" \
    --scope "/providers/Microsoft.Management/managementGroups/`TENANT_ID`"
```

6. ###### Create an Azure Entra ID application for AWS Config

Create a separate application registration for AWS Config to use when
recording Azure resource state. Note the _Application (client) ID_ from the output.

```
az ad app create \
    --display-name "AWSConfigAzureIntegration-`ACCOUNT_ID`-`TENANT_ID_PREFIX`" \
    --query appId
```

Replace:

    * `ACCOUNT_ID` — Your AWS account
     ID.
    * `TENANT_ID_PREFIX` — The leading
     characters of your Azure tenant ID. This prefix exists only to make the
     application display name unique. You can use any short, recognizable
     portion of the tenant ID.

Create a service principal for the AWS Config application. The
`CONFIG_APPLICATION_ID` is the
`appId` value returned by the preceding
`az ad app create` command in this step.

```
az ad sp create --id `CONFIG_APPLICATION_ID`
```

The `az ad sp create` output includes an `id`
(object ID) field, which is the
`CONFIG_SERVICE_PRINCIPAL_ID` value that you
use in the later Reader-role and Event Hubs role-assignment steps. 7. ###### Add a federated identity credential for AWS Config

Add a federated identity credential to the AWS Config application.
The subject is the AWS Config service-linked role ARN (created
automatically when you create the Config connector in a later
step).

```
az ad app federated-credential create \
    --id `CONFIG_APPLICATION_ID` \
    --parameters "{
        \"name\": \"aws-config-federation\",
        \"issuer\": \"`AWS_OIDC_ISSUER_URL`\",
        \"subject\": \"arn:aws:iam::`ACCOUNT_ID`:role/aws-service-role/thirdparty.config.amazonaws.com/AWSServiceRoleForConfigThirdParty\",
        \"audiences\": [\"api://AzureADTokenExchange\"]
    }"
```

8. ###### Assign Reader role to the AWS Config service principal

Assign the Azure built-in Reader role to the AWS Config service
principal at the tenant (management group) level. This allows AWS Config
to discover Azure resources.

```
az role assignment create \
    --assignee `CONFIG_SERVICE_PRINCIPAL_ID` \
    --role "acdd72a7-3385-48ef-bd42-f606fba81ae7" \
    --scope "/providers/Microsoft.Management/managementGroups/`TENANT_ID`"
```

9. ###### Create an Event Hub for Azure Activity Log streaming

AWS Config uses an Azure Event Hub to receive Activity Log events
that indicate resource changes. Create an Event Hub namespace, hub,
and consumer group in one of your Azure subscriptions.

```
# Create a resource group for the Event Hub
az group create \
    --subscription "`HOSTING_SUBSCRIPTION_ID`" \
    --name "AWSConfigAzureResources" \
    --location eastus

# Create an Event Hub namespace with a discovery tag
az eventhubs namespace create \
    --subscription "`HOSTING_SUBSCRIPTION_ID`" \
    --resource-group "AWSConfigAzureResources" \
    --name "`EVENT_HUB_NAMESPACE`" \
    --location eastus \
    --sku Standard \
    --tags "AWSConfig-`ACCOUNT_ID`-`AWS_REGION`=activitylog"

# Create the Event Hub
az eventhubs eventhub create \
    --subscription "`HOSTING_SUBSCRIPTION_ID`" \
    --resource-group "AWSConfigAzureResources" \
    --namespace-name "`EVENT_HUB_NAMESPACE`" \
    --name "activitylog" \
    --partition-count 4

# Create the consumer group for AWS Config
az eventhubs eventhub consumer-group create \
    --subscription "`HOSTING_SUBSCRIPTION_ID`" \
    --resource-group "AWSConfigAzureResources" \
    --namespace-name "`EVENT_HUB_NAMESPACE`" \
    --eventhub-name "activitylog" \
    --name "AWSConfig"
```

Replace `EVENT_HUB_NAMESPACE` with a globally
unique name (for example,
`awsconfig-`ACCOUNT_ID`-`REGION``)
and `HOSTING_SUBSCRIPTION_ID` with the Azure
subscription that will host the Event Hub resources. 10. ###### Assign Event Hubs Data Receiver role to the AWS Config service principal

Allow the AWS Config service principal to read from the Event
Hub:

```
EVENT_HUB_ID=$(az eventhubs eventhub show \
    --subscription "`HOSTING_SUBSCRIPTION_ID`" \
    --resource-group "AWSConfigAzureResources" \
    --namespace-name "`EVENT_HUB_NAMESPACE`" \
    --name "activitylog" \
    --query id \
    -o tsv)

az role assignment create \
    --assignee `CONFIG_SERVICE_PRINCIPAL_ID` \
    --role "a638d3c7-ab3a-418d-83e6-5f17a39d4fde" \
    --scope "$EVENT_HUB_ID"
```

11. ###### Configure Activity Log export to the Event Hub

For each Azure subscription you want AWS Config to monitor, create a
diagnostic setting that exports Activity Log events to the Event
Hub:

```
az provider register \
    --namespace Microsoft.Insights \
    --subscription "`SUBSCRIPTION_ID`"

az rest --method PUT \
    --url "https://management.azure.com/subscriptions/`SUBSCRIPTION_ID`/providers/Microsoft.Insights/diagnosticSettings/`EVENT_HUB_NAMESPACE`?api-version=2021-05-01-preview" \
    --body "{
        \"properties\": {
            \"eventHubAuthorizationRuleId\": \"/subscriptions/`HOSTING_SUBSCRIPTION_ID`/resourceGroups/AWSConfigAzureResources/providers/Microsoft.EventHub/namespaces/`EVENT_HUB_NAMESPACE`/authorizationRules/RootManageSharedAccessKey\",
            \"eventHubName\": \"activitylog\",
            \"logs\": [{\"category\": \"Administrative\", \"enabled\": true}]
        }
    }"
```

Repeat this step for each subscription you want to monitor.
After completing the Azure setup, note the following values. You need them when
creating the Cloud Connector:

- **Tenant ID** — Your Azure AD directory
  (tenant) ID.
- **SSM Application (Client) ID** — The
  application ID of the Systems Manager Azure AD app (Step 1).
- **Config Application (Client) ID** — The
  application ID of the AWS Config Azure AD app (Step 6).
- **Subscription IDs** — The Azure
  subscriptions you want to manage.
- **Event Hub namespace hostname** — The
  fully qualified hostname of the Event Hub namespace (for example,
  ``EVENT_HUB_NAMESPACE`.servicebus.windows.net`).
