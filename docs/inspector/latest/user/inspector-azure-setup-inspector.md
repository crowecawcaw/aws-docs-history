# Configuring Amazon Inspector to integrate with Microsoft Azure

After you configure your Azure environment, create a connector in Amazon Inspector to
begin scanning your Azure resources for vulnerabilities.

###### To create an Azure connector

1. Open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. In the navigation pane, choose **Integrations**.
3. Choose **Create
   connector**.
4. Provide the following information:

   - **Name** – A
     unique name for this connector. For name and description length
     constraints, see the CreateConnector operation in the Amazon Inspector API
     Reference.
   - **Description**
     (optional) – A description of this
     connector.

###### Important

Names and descriptions are used to identify your content, and
we recommend you do not include sensitive, confidential, or
personally identifiable information (PII) in them.

    * **Azure Tenant
     ID** – Your Microsoft Entra ID
     tenant identifier. Found in the Azure portal under
     Microsoft Entra ID,
     Properties.

5. Select **capabilities** to
enable:

    * VM scanning (Amazon Inspector VM Scanner agent deployed to Azure
     VMs)
    * Function App scanning (code dependency
     analysis)
    * ACR image scanning (container image vulnerability
     detection)

You can enable any combination. Capabilities can be changed later
via `UpdateConnector`. 6. Configure your **monitoring
targets**:

    * **Azure
     subscriptions** – Choose whether to monitor all
     subscriptions in your tenant or specify individual subscription
     IDs.
    * **Azure
     regions** – Choose whether to enable all Azure
     regions or select specific regions.

7. Configure the **recording
source**:

Select an existing recording source, or create a new one. The
recording source ARN is a required field in the API
(`inspector2:CreateConnector`). 8. Copy the generated Azure setup script, run it in your Azure
environment (see [Configuring Microsoft Azure to integrate with Amazon Inspector](inspector-azure-setup-azure.md "inspector-azure-setup-azure.md")), and
then choose **Create
connector**.

###### Managed Amazon Inspector VM Scanner deployment

If you enabled VM scanning, Amazon Inspector uses Amazon EC2 Systems Manager Automation to deploy
and manage the Amazon Inspector VM Scanner agent on your Azure VMs. With managed
deployment:

- No manual installation is required.
- The agent stays up to date
  automatically.
- Amazon Inspector manages the full lifecycle (install, update, health
  monitoring).
  Amazon Inspector uses Amazon EC2 Systems Manager Automation to deploy and manage the agent.

To enable VM scanning, you must create the following IAM resources in your
account.

###### IAM OIDC identity provider

Create an IAM OIDC identity provider for Microsoft Entra ID
with the following configuration:

- **Issuer URL:**
  `https://sts.windows.net/`tenant-id`/`
- **Client ID list:**
  `api://`app-id``,
  `api://AzureADTokenExchange`
- **Thumbprint:**
  A 40-character string of all zeros (`0` repeated 40 times). AWS STS
  validates tokens via the JWKS endpoint rather than the thumbprint
  value.

###### Inspector2VmScannerRole-`tenant-id`

Used by the Amazon Inspector VM Scanner agent running on Azure VMs to send scan telemetry
to Amazon Inspector. This role uses OIDC web identity federation through the Microsoft
Entra ID identity provider.

**Trust policy:**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::`account-id`:oidc-provider/sts.windows.net/`tenant-id`/"
            },
            "Action": "sts:AssumeRoleWithWebIdentity"
        }
    ]
}
```

**Permission policy (TelemetryPolicy):**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "inspector2-telemetry:*",
            "Resource": "*"
        }
    ]
}
```

**Tags:**

- `inspector-managed` = `true`

###### Inspector2SSMFederationRole-`tenant-id`

Enables OIDC federation to Azure for secure cross-cloud authentication.
This role is assumed by the AssumeRole and DispatchRole, and by Amazon EC2 Systems Manager, to
obtain web identity tokens for Azure operations.

**Trust policy:**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::`account-id`:root"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:PrincipalTag/caller": "SSM"
                },
                "ArnLike": {
                    "aws:PrincipalArn": [
                        "arn:aws:iam::`account-id`:role/Inspector2SSMAssumeRole-`tenant-id`",
                        "arn:aws:iam::`account-id`:role/Inspector2SSMDispatchRole-`tenant-id`"
                    ]
                }
            }
        },
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ssm.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

**Permission policy (FederationPolicy):**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "sts:IdentityTokenAudience": [
                        "api://AzureADTokenExchange"
                    ]
                }
            },
            "Action": [
                "sts:GetWebIdentityToken",
                "sts:TagGetWebIdentityToken"
            ],
            "Resource": "*",
            "Effect": "Allow"
        }
    ]
}
```

**Tags:**

- `caller` = `SSM`
- `inspector-managed` = `true`

###### Inspector2SSMAssumeRole-`tenant-id`

Executes Amazon EC2 Systems Manager Automation to onboard Azure VMs as managed instances.
This role creates and manages hybrid activations, passes roles to Amazon EC2 Systems Manager,
and retrieves automation documents.

**Trust policy:**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ssm.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "`account-id`"
                }
            }
        }
    ]
}
```

**Permission policy (AssumeRolePolicy):**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": "arn:aws:iam::`account-id`:role/Inspector2SSMFederationRole-`tenant-id`"
        },
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::`account-id`:role/AmazonEC2RunCommandRoleForManagedInstances",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "ssm.amazonaws.com"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:CreateActivation",
                "ssm:DeleteActivation",
                "ssm:DescribeActivations",
                "ssm:DescribeInstanceInformation",
                "ssm:PutConfigurePackageResult",
                "iam:ListRoleTags"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "ssm:AddTagsToResource",
            "Resource": [
                "arn:aws:ssm:*:`account-id`:activation/*",
                "arn:aws:ssm:*:`account-id`:managed-instance/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": "ssm:GetDocument",
            "Resource": [
                "arn:aws:ssm:*:*:document/AWS-InstallDistributorPackageOnAzure",
                "arn:aws:ssm:*:*:document/AWS-InstallSsmAgentOnAzure",
                "arn:aws:ssm:*::document/AmazonInspector2-InspectorVmScanner"
            ]
        },
        {
            "Effect": "Allow",
            "Action": "ssm:GetCloudConnector",
            "Resource": "*"
        }
    ]
}
```

**Tags:**

- `caller` = `SSM`
- `AzureTenantId` = `tenant-id`
- `AzureApplicationId` = `app-id`
- `inspector-managed` = `true`

###### Inspector2SSMDispatchRole-`tenant-id`

Resolves Azure VM targets and dispatches Amazon Inspector VM Scanner agent installation via
Amazon EC2 Systems Manager Automation. This role starts automation executions and passes the
AssumeRole to Amazon EC2 Systems Manager.

**Trust policy:**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "ssm.amazonaws.com"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "aws:SourceAccount": "`account-id`"
                }
            }
        }
    ]
}
```

**Permission policy (DispatchPolicy):**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::`account-id`:role/Inspector2SSMAssumeRole-`tenant-id`",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "ssm.amazonaws.com"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": "ssm:StartAutomationExecution",
            "Resource": [
                "arn:aws:ssm:*:*:document/AWS-InstallDistributorPackageOnAzure",
                "arn:aws:ssm:*:`account-id`:automation-execution/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": "arn:aws:iam::`account-id`:role/Inspector2SSMFederationRole-`tenant-id`"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssm:DescribeInstanceInformation",
                "ssm:ListCloudConnectors",
                "ssm:GetCloudConnector",
                "iam:ListRoleTags"
            ],
            "Resource": "*"
        }
    ]
}
```

**Tags:**

- `caller` = `SSM`
- `inspector-managed` = `true`
  The Azure app registration must have its Application ID URI set to
  `api://`app-id``.

Each target Azure VM must have a system-assigned managed identity enabled.
To automatically assign managed identity to new VMs, use a DeployIfNotExists
policy in your Azure environment.

For more information about the Amazon Inspector VM Scanner agent, see [Amazon Inspector VM Scanner](inspector-vm-scanner.md "inspector-vm-scanner.md").

Alternatively, you can manually install the Amazon Inspector VM Scanner agent. For manual
installation at scale across many Azure VMs, use an Azure VM custom
extension. For instructions, see [Amazon Inspector VM Scanner](inspector-vm-scanner.md "inspector-vm-scanner.md").

To exclude specific Azure VMs from scanning, apply the following tag to
the VM:

- **Key:**
  `InspectorExclusion`
- **Value:**
  `true`

###### Adjusting the scope of a connector

After you create a connector, you can adjust its scope by changing the
Azure Subscriptions or Azure Regions that it monitors. If you adjust the scope, most changes
take effect within approximately 15 minutes.

Before you adjust the scope, note the following:

- If you add a region to the scope, the console generates an updated
  setup script that creates the necessary Event Hub infrastructure in the new
  region.
- If a service-linked connector exists (created via AWS Security Hub CSPM), you
  cannot reduce its scope in Amazon Inspector directly. Modify the scope in AWS Security Hub CSPM
  instead.
- The scope of a AWS Security Hub CSPM connector can never be less than any
  existing customer-managed connector in Amazon Inspector for the same Azure
  tenant.

###### Verifying the connector

After you create the connector, Amazon Inspector begins discovering and scanning
your Azure resources. It can take up to 24 hours for the initial set of
findings to appear. To verify that the connector is working:

1. In the Amazon Inspector console, navigate to **Summary** to confirm Azure resource counts are
   populating.
2. Navigate to **Coverage** to
   verify Azure resources appear with scan status.
3. Navigate to **Integrations**, select your integration to
   Microsoft Azure, and verify the connector health shows
   `Active`.
4. For VM scanning, verify that Azure VMs appear with Amazon Inspector VM Scanner
   agent status in the Coverage view.
5. Navigate to **Findings** and
   filter by resource type to view Azure resource
   findings.

###### Note

Connector health status is eventually consistent. When a permission or
configuration issue occurs, the connector status changes to **Degraded** quickly with an actionable message.
However, after you fix the issue, the status can take up to 24 hours to
return to **Connected**.

- A **Degraded** status after a
  recent fix does not necessarily indicate an ongoing
  problem.
- For real-time visibility into recording failures, check the
  CloudWatch metrics in the namespace.

###### Troubleshooting

If the connector status shows Error or resources are not appearing after
24 hours, review the following:

Connector shows Error status
Verify that the Azure app registration has the correct
federated identity credential and that the IAM Token Issuer URL is
configured in your AWS account.

Unable to record some Azure resources

The error can occur for any of the following reasons:

- The Azure environment does not meet the prerequisites for resource recording.
- The app registration does not have admin consent for Microsoft Graph API permissions.
- The Reader role assignment does not cover all required scopes.
- The Microsoft Entra ID tenant does not have required log data.

To address the error, do the following:

1. To confirm that your environment meets all requirements, review [Prerequisites for integrating Amazon Inspector with Microsoft Azure](inspector-azure-prereqs.md "inspector-azure-prereqs.md").
2. Confirm that the app registration has the required Microsoft Graph
   API permissions with admin consent.
3. Verify that the service principal has the Reader role at the
   tenant root management group scope.

Resources not appearing
Confirm that the Event Hub is receiving events. Check
Event Hub metrics in the Azure portal and verify the
`AWSConfig` consumer group exists.

VMs not scanning
Verify that VMs have network connectivity to Amazon EC2 Systems Manager
endpoints and are running a supported operating
system.

ACR images not appearing
Verify that diagnostic settings are enabled on your
container registries.

Scope change not taking effect
When you change the connector scope to add a new Azure
region, the console regenerates the setup script. You must re-run the
updated script to provision Event Hub infrastructure in the new
region.

###### How Amazon Inspector handles resource identifiers

By enabling your Azure integration for Amazon Inspector, resource identifiers from other
cloud providers will be stored in AWS Config, Amazon Inspector, and other AWS services (as
needed) as metadata related to the management of the corresponding resource
configuration data collected from the other cloud providers. Such resource identifiers
do not constitute Your Content, and we recommend you do not include sensitive,
confidential, or personally identifiable information in them.

The following identifiers from your connected cloud environment are stored and used by
AWS to provide multicloud security capabilities:

- **Resource identifiers:** Azure Tenant ID,
  Subscription ID, Location (region), Resource ID (Resource Group IDs or Names,
  Resource Provider, Resource Type)
  Relationships among these identifiers - including how resources relate to one another
  and how findings relate to resources - are also stored as service metadata. AWS uses
  these identifiers for resource correlation, associating findings to resources, service
  operational logging, and de-duplication.
