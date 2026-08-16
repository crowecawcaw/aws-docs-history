# Configuring Security Hub to integrate with Microsoft Azure

After you complete the [prerequisite
tasks](securityhub-v2-azure-prereqs.md "securityhub-v2-azure-prereqs.md") and [configure your Microsoft Azure
environment](securityhub-v2-azure-setup-azure.md "securityhub-v2-azure-setup-azure.md"), you can configure AWS Security Hub to integrate with Azure. To configure
Security Hub to integrate with Azure, you create a connector. You can create the connector
from a Delegated Administrator account or the management account. After you create the
connector, the following events occur:

1. Security Hub validates the Azure credentials and connectivity to your Azure environment. This
   process can take several minutes.
2. Security Hub creates service-linked connectors in Security Hub CSPM and Amazon Inspector. These connectors
   ensure that posture management checks and vulnerability scanning match the scope you defined
   in Security Hub.
3. AWS Config begins discovering Azure resources using the federated identity
   credentials.
4. Security Hub automatically enables the CIS Microsoft Azure Foundations Benchmark v4.0 standard and
   the Azure Foundational Best Practices standard in CSPM for your Azure resources.
5. Initial findings begin appearing within 15–30 minutes for resources with Activity
   Log events. Full evaluation of all existing resources can take up to 24 hours.

###### Topics

- [Create a
  connector](#securityhub-v2-azure-setup-securityhub-v2-proc "#securityhub-v2-azure-setup-securityhub-v2-proc")
- [Adjust the
  scope of a connector](#securityhub-v2-azure-setup-securityhub-v2-manage "#securityhub-v2-azure-setup-securityhub-v2-manage")
- [Verify the
  health of a connector](#securityhub-v2-azure-setup-securityhub-v2-verify "#securityhub-v2-azure-setup-securityhub-v2-verify")
- [Troubleshoot a
  connector](#securityhub-v2-azure-setup-securityhub-v2-tshoot "#securityhub-v2-azure-setup-securityhub-v2-tshoot")
- [Resource
  and finding identifiers](#securityhub-v2-azure-setup-securityhub-v2-identifiers "#securityhub-v2-azure-setup-securityhub-v2-identifiers")

## Create an Azure connector

To create an Microsoft Azure connector for your environment, complete the following steps by
using the AWS Security Hub console or the API.

1. Open the AWS Security Hub console at [https://console.aws.amazon.com/securityhub/advanced/home?region=us-east-1.](https://console.aws.amazon.com/securityhub/advanced/home?region=us-east-1. "https://console.aws.amazon.com/securityhub/advanced/home?region=us-east-1.").
2. In the navigation pane, choose **Integrations**.
3. Choose **Create Azure connector**.
4. In the **Security capabilities** section, choose whether you want
   the **Network scanning** feature enabled. This feature is
   enabled by default for the account where you are enabling the Azure integration, and
   can be unchecked before completing your connector setup. If an organization policy is
   blocking this feature for your account, it does not appear as an option. For more
   information, see
   [Network scanning in Security Hub](securityhub-network-scanning.md "securityhub-network-scanning.md").
5. For **Azure Tenant ID**, enter your Microsoft Entra ID tenant
   identifier. You can find this in the Azure portal under _Microsoft Entra ID >
   Properties > Tenant ID_.
6. For **Application (client) ID**, enter the application ID for the
   Azure application that you registered during the Azure environment setup.
7. Configure additional settings and the scope of the connector by doing the
   following:

   - For **Name**, enter a unique name for the connector. The name can
     contain up to 50 alphanumeric characters and it can include hyphens.

   ###### Note

   The connector name cannot be changed after creation.
   - For **Description**, optionally enter a brief description of the
     connector. The description can contain up to 200 characters.

###### Important

Names and descriptions are used to identify your content. Do not
include sensitive, confidential, or personally identifiable information (PII) in
them.

    * For **Subscriptions**, choose **All
     subscriptions** to monitor all current and future subscriptions in the
     tenant, or **Specific subscriptions** to monitor only the
     subscriptions that you specify. If you choose to monitor only specific subscriptions,
     enter the ID for each one.
    * For **Regions**, choose **All regions** to
     monitor resources in all Azure regions, or **Specific regions** to
     monitor only the Regions that you specify.


    ###### Note

    If you already created a connector in Security Hub CSPM or Amazon Inspector for the same Azure
     tenant, the scope of the connector in Security Hub must include the same subscriptions
     and Regions as the connector in Security Hub CSPM or Amazon Inspector.


    ###### Note

    Controls that evaluate Microsoft Entra ID and Microsoft Graph resources require
     the global Region scope to be included in your integration configuration. If you
     select specific Azure Regions only, these controls do not generate findings.

8. Review the connector configuration.

###### Note

If you plan to use Amazon Inspector for Azure VM scanning, you must create the required
IAM roles. For details, see [IAM roles for Azure VM scanning through Amazon Inspector](#securityhub-v2-azure-setup-securityhub-v2-iam "#securityhub-v2-azure-setup-securityhub-v2-iam"). 9. When you finish entering and reviewing the settings, choose **Create
connector**.

### IAM roles for Azure VM scanning through Amazon Inspector

To enable vulnerability scanning through Amazon Inspector, you must create the following IAM
resources in your AWS account.

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
    "Version":"2012-10-17",
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

**Tags:**

- `inspector-managed` = `true`

**Permission policy (TelemetryPolicy):**

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "inspector2-telemetry:*",
            "Resource": "*"
        }
    ]
}
```

###### Inspector2SSMFederationRole-`tenant-id`

Enables OIDC federation to Azure for secure cross-cloud authentication.
This role is assumed by the AssumeRole and DispatchRole, and by Amazon EC2 Systems Manager, to
obtain web identity tokens for Azure operations.

**Trust policy:**

```
{
    "Version":"2012-10-17",
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
    "Version":"2012-10-17",
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
    "Version":"2012-10-17",
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
    "Version":"2012-10-17",
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
    "Version":"2012-10-17",
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
    "Version":"2012-10-17",
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

###### Prerequisites for VM scanning

The Azure app registration must have its Application ID URI set to
`api://`app-id``.

Each Azure VM that you want to scan
must have a system-assigned managed identity enabled. To automatically assign managed
identity to new VMs, use a DeployIfNotExists policy in your Azure environment.

After you create the connector, Security Hub begins monitoring your Azure environment. You can
check the status of the connector on the **Integrations** page.

## Adjust the scope of an Azure connector

After you create an Microsoft Azure connector, you can adjust the scope of the connector by
changing the Azure Subscriptions or Azure Regions that it monitors. Scope changes typically take effect
within 15–30 minutes for resources with Activity Log events. Full evaluation of newly
added Azure Subscriptions can take up to 24 hours.

Before you adjust the scope of a connector, note the following:

- When you change the scope of a connector in Security Hub, the associated
  service-linked connectors in Security Hub CSPM and Amazon Inspector are automatically updated to
  match.
- The scope of a Security Hub connector can never be less than any existing customer-managed
  connector in Security Hub CSPM or Amazon Inspector for the same Azure tenant.
- If you add a Region to the connector scope, you must re-run the setup script to
  provision Event Hub infrastructure in the new Region. Your existing Event Hub
  configuration is not affected.

## Verify the health of an Azure connector

You can check the health of an Microsoft Azure connector at any time to confirm that Security Hub is
receiving data from your Azure environment.

###### To verify the health of a connector

1. Open the AWS Security Hub console at [https://console.aws.amazon.com/securityhub/advanced/home?region=us-east-1.](https://console.aws.amazon.com/securityhub/advanced/home?region=us-east-1. "https://console.aws.amazon.com/securityhub/advanced/home?region=us-east-1.").
2. In the navigation pane, choose **Integrations** and select your Azure
   connector.
3. Verify that the connector status shows **Active**. If the
   connector shows Active, verification is complete. If it shows a different status, see
   [Troubleshoot an Azure connector](#securityhub-v2-azure-setup-securityhub-v2-tshoot "#securityhub-v2-azure-setup-securityhub-v2-tshoot").
4. Navigate to **Findings** and filter by
   `ResourceCloudProviders = Azure` to confirm findings are being
   generated for your Azure resources.
5. Check the **Security standards** page to confirm the CIS Azure v4.0
   standard shows controls in PASSED or FAILED status (not all NO\_DATA).

###### Note

Connector health status is eventually consistent. When a permission or
configuration issue occurs, the connector status changes to **Degraded** quickly with an actionable message. However, after
you fix the issue, the status can take up to 24 hours to return to **Connected**.

- A **Degraded** status after a recent fix
  does not necessarily indicate an ongoing problem.
- For real-time visibility into recording failures, check the CloudWatch
  metrics in the namespace.

## Troubleshoot an Azure connector

If you experience issues with your connector, review the following common issues and
resolutions.

Connector status is Unhealthy

This issue typically occurs if federated credentials are not configured correctly in
Azure.

To address this issue, verify that the Token Issuer URL and subject ARN in your
Azure federated credentials match your AWS account.

No findings after 30 minutes

This issue can occur if the Event Hub is not receiving Activity Logs.

To address this issue, check that diagnostic settings are configured on your Azure
subscriptions and that the Event Hub namespace is tagged correctly with
`AWSConfig-`account-id`-`region``.

All controls show NO\_DATA

This issue can occur if the connector is disabled or if AWS Config cannot reach your
Azure environment.

To address this issue, verify that the connector is enabled and that the service
principal has the Reader role at the tenant root management group scope.

Unable to record some Azure resources

The error can occur for any of the following reasons:

- The Azure environment does not meet the prerequisites for resource recording.
- The app registration does not have admin consent for Microsoft Graph API permissions.
- The Reader role assignment does not cover all required scopes.
- The Microsoft Entra ID tenant does not have required log data.

To address the error, do the following:

1. To confirm that your environment meets all requirements, review [Prerequisites for Microsoft Azure](securityhub-v2-azure-prereqs.md#securityhub-v2-azure-prereqs-azure "securityhub-v2-azure-prereqs.md#securityhub-v2-azure-prereqs-azure").
2. Confirm that the app registration has the required Microsoft Graph API
   permissions with admin consent.
3. Verify that the service principal has the Reader role at the tenant root
   management group scope.

Findings appear for some subscriptions only

This issue can occur if Activity Log export is not configured for all target
subscriptions.

To address this issue, confirm that the diagnostic settings cover all subscriptions
included in the connector scope.

## How Security Hub handles resource and finding identifiers

By enabling your Azure integration for AWS Security Hub, resource and security finding
identifiers from other cloud providers are stored in AWS Config, Security Hub, and other AWS
services (as needed) as metadata related to the management of the corresponding resource
configuration and security finding data collected from the other cloud providers. Such
identifiers do not constitute Your Content. Do not include sensitive,
confidential, or personally identifiable information in them.

The following identifiers from your connected cloud environment are stored and used by
AWS to provide multicloud security capabilities:

- **Resource identifiers:** Azure Tenant ID,
  Subscription ID, Location (region), Resource ID (Resource Group IDs or Names, Resource
  Provider, Resource Type)
- **Security Finding identifiers:** the unique
  identifiers assigned to each security finding generated by the detecting
  service.

Relationships among these identifiers - including how resources relate to one another and
how findings relate to resources - are also stored as service metadata. AWS uses these
identifiers for resource correlation, associating findings to resources, service operational
logging, and de-duplication.
