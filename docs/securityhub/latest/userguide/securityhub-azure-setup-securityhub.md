

# Configuring Security Hub CSPM to integrate with Microsoft Azure
<a name="securityhub-azure-setup-securityhub"></a>

After you complete the [prerequisite tasks](securityhub-azure-prereqs.md) and [configure your Microsoft Azure environment](securityhub-azure-setup-azure.md), you can configure AWS Security Hub CSPM to integrate with Azure. To configure Security Hub CSPM to integrate with Azure, you create a connector. After you create the connector, the following events occur:

1. Security Hub CSPM validates the Azure credentials and connectivity to your Azure environment. This process can take several minutes.

1. AWS Config begins discovering and recording configuration data for your Azure resources.

1. Security Hub CSPM begins generating posture management findings for your Azure resources after resource data collection completes.

**Note**  
If you already created a connector in Security Hub, a service-linked connector was automatically created in Security Hub CSPM. You do not need to create a separate customer-managed connector unless you require a different scope.

**Topics**
+ [Create a connector](#securityhub-azure-setup-securityhub-proc)
+ [Enable standards and controls](#securityhub-azure-setup-securityhub-standards)
+ [Adjust the scope of a connector](#securityhub-azure-setup-securityhub-manage)
+ [Verify the health of a connector](#securityhub-azure-setup-securityhub-verify)
+ [Troubleshoot a connector](#securityhub-azure-setup-securityhub-tshoot)
+ [Resource identifiers](#securityhub-azure-setup-securityhub-identifiers)
+ [Available controls](#securityhub-azure-controls)

## Create an Azure connector
<a name="securityhub-azure-setup-securityhub-proc"></a>

To create an Microsoft Azure connector for your environment, complete the following steps by using the AWS Security Hub CSPM console or the API.

1. Open the Security Hub CSPM console.

1. In the navigation pane, choose **Integrations**.

1. Choose **Create Azure connector**.

1. For **Azure Tenant ID**, enter your Azure Active Directory tenant identifier.

1. For **Application (client ID)**, enter the application ID for the Azure app registration that you created.

1. Configure additional settings and the scope of the connector by doing the following:
   + For **Name**, enter a unique name for the connector. The name can contain up to 50 alphanumeric characters and it can include hyphens (‐).
**Important**  
Names and descriptions are used to identify your content, and we recommend you do not include sensitive, confidential, or personally identifiable information (PII) in them.
   + For **Description**, optionally enter a brief description of the connector. The description can contain up to 200 characters.
   + For **Subscriptions**, choose **All subscriptions** to monitor all current and future subscriptions in the tenant, or **Specific subscriptions** to monitor only the subscriptions that you specify. If you choose to monitor only specific subscriptions, enter the ID for each one.
   + For **Regions**, choose the Azure regions where your resources are deployed.
**Note**  
Controls that evaluate Microsoft Entra ID and Microsoft Graph resources require the global region scope to be included in your integration configuration. If you select specific Azure Regions only, these controls will not generate findings.

1. Review your configuration and choose **Create connector**.

After you create the connector, Security Hub CSPM validates your Azure credentials and begins resource discovery. The connector should show a status of Active within 2-5 minutes.

## Enabling standards and controls
<a name="securityhub-azure-setup-securityhub-standards"></a>

After creating the connector, you must enable Azure security standards to begin generating findings. For general information about enabling standards and managing controls, see [Enabling standards](https://docs.aws.amazon.com/securityhub/latest/userguide/enable-standards.html) and [Enabling and disabling controls](https://docs.aws.amazon.com/securityhub/latest/userguide/enable-controls-overview.html).
+ **CIS Microsoft Azure Foundations Benchmark v4.0** - A widely adopted security benchmark that defines best practices for securing Azure environments. Each control evaluates a specific aspect of your Azure configuration (for example, storage account encryption, network security group rules, identity and access settings).
+ **Azure Foundational Best Practices** - Evaluates Azure resources for exposure risks by correlating network reachability, public access, and sensitive data indicators. Generates exposure-type findings that highlight resources at elevated risk.

Azure standards have their own set of controls, separate from AWS controls. There are no cross-cloud controls that evaluate both AWS and Azure resources in a single check.

You can enable Azure standards through the Security Hub CSPM console or through the API/CLI. Navigate to **Standards** in the Security Hub CSPM console and enable the desired standard. Alternatively, use the CLI:

```
$ aws securityhub batch-enable-standards \
  --standards-subscription-requests '[{"StandardsArn": "{{Standard-ARN}}"}]' \
  --region {{your-aws-region}}
```

**Note**  
You can enable Azure standards before or after creating the connector - they are not coupled. However, findings will only be generated once both the connector and the standard are active and resource data has been collected.

Once a standard is enabled (typically within seconds), you can view and manage individual controls:
+ **View controls:** Use the Security Hub CSPM console (Standards > select standard > Controls) or the `list-standards-control-associations` API.
+ **Disable a control:** If a specific control is not applicable to your environment, you can disable it.
+ **Configure custom parameters:** Some controls accept custom input parameters (for example, password length thresholds). These can be configured through the `update-security-control` API.
+ Azure standards apply uniformly across your entire connector scope. You cannot enable different standards or controls for different Azure subscriptions within the same connector.
+ **Controls depend on resource data availability.** Each control evaluates a specific Azure resource type. If AWS Config has not yet collected configuration data for a particular resource type, the control will generate a default PASS finding for those resources. These default PASS findings will automatically update to accurate evaluations as resource data arrives. Do not treat initial compliance scores as accurate until resource data collection is complete.
+ Custom input parameters for security controls can be configured even before creating a connector - they persist independently.
+ Controls evaluating subscription-level settings (for example, Microsoft Defender plans, activity log alerts) produce one finding per Azure subscription rather than per individual resource.
+ Multicloud standards cannot be included in Central Configuration policies. You must manage Azure standard enablement independently in each AWS account and AWS Region.

## Adjust the scope of an Azure connector
<a name="securityhub-azure-setup-securityhub-manage"></a>

After you create a Microsoft Azure connector, you can adjust the scope of the connector by changing the Azure Subscriptions or Azure Regions that it monitors. If you adjust the scope, most types of changes take effect within approximately 15 minutes.

Before you adjust the scope, note the following:
+ The scope of a customer-managed connector cannot exceed the scope of any existing service-linked connector in the same account and Region.
+ When you expand the scope, Security Hub CSPM begins generating findings for new resources after AWS Config collects their configuration data.
+ When you reduce the scope, existing findings for removed resources transition to an archived state.

## Verify the health of an Azure connector
<a name="securityhub-azure-setup-securityhub-verify"></a>

You can check the health of an Microsoft Azure connector at any time. Navigate to **Integrations** in the Security Hub CSPM console and confirm your connector shows Active status.

Initial findings typically appear within 15-30 minutes of resource data collection completing.

**Note**  
Connector health status is eventually consistent. When a permission or configuration issue occurs, the connector status changes to **Degraded** quickly with an actionable message. However, after you fix the issue, the status can take up to 24 hours to return to **Connected**.  
A **Degraded** status after a recent fix does not necessarily indicate an ongoing problem.
For real-time visibility into recording failures, check the CloudWatch metrics in the namespace.

## Troubleshoot an Azure connector
<a name="securityhub-azure-setup-securityhub-tshoot"></a>

If you encounter issues with your connector, use the following information to diagnose and resolve common problems.

**Connector status is Unhealthy**  
This issue typically occurs if federated credentials aren't configured correctly in Azure.  
To address this issue, verify that the token issuer URL and subject ARN in your Azure federated credentials match your AWS account.

**No findings after 30 minutes**  
This issue can occur if Event Hub isn't receiving Activity Logs or if no standard is enabled.  
To address this issue, verify that the Event Hub namespace is tagged correctly (`AWSConfig-{{account-id}}-{{region}}=activitylog`), the `AWSConfig` consumer group exists, the Data Receiver role is assigned, and at least one Azure standard is enabled.

**Unable to record some Azure resources**  
The error can occur for any of the following reasons:  
+ The Azure environment does not meet the prerequisites for resource recording.
+ The app registration does not have admin consent for Microsoft Graph API permissions.
+ The Reader role assignment does not cover all required scopes.
+ The Microsoft Entra ID tenant does not have required log data.
To address the error, do the following:  

1. To confirm that your environment meets all requirements, review [Prerequisites for Microsoft Azure](securityhub-azure-prereqs.md#securityhub-azure-prereqs-azure).

1. Confirm that the app registration has the required Microsoft Graph API permissions with admin consent.

1. Verify that the service principal has the Reader role at the tenant root management group scope.

**Connector stays in Pending status**  
This issue can occur if the Azure app registration is misconfigured.  
To address this issue, verify that the federated identity credential issuer URL and subject identifier match your AWS account. Also verify that admin consent has been granted for all required Microsoft Graph API permissions.

## How Security Hub CSPM handles resource identifiers
<a name="securityhub-azure-setup-securityhub-identifiers"></a>

By enabling your Azure integration for AWS Security Hub CSPM, resource identifiers from other cloud providers will be stored in AWS Config, AWS Security Hub CSPM, and other AWS services (as needed) as metadata related to the management of the corresponding resource configuration data collected from the other cloud providers. Such resource identifiers do not constitute Your Content, and we recommend you do not include sensitive, confidential, or personally identifiable information in them.

The following identifiers from your connected cloud environment are stored and used by AWS to provide multicloud security capabilities:
+ **Resource identifiers:** Azure Tenant ID, Subscription ID, Location (region), Resource ID (Resource Group IDs or Names, Resource Provider, Resource Type)

Relationships among these identifiers - including how resources relate to one another and how findings relate to resources - are also stored as service metadata. AWS uses these identifiers for resource correlation, associating findings to resources, service operational logging, and de-duplication.

## Available controls for Azure
<a name="securityhub-azure-controls"></a>

After you enable Azure standards, the following 122 controls evaluate your Azure resources. Controls are distributed across two standards:
+ **CIS Microsoft Azure Foundations Benchmark v4.0** – 96 controls mapped to specific CIS sections
+ **Azure Foundational Best Practices** – 26 controls covering additional security best practices

**Note**  
Controls that evaluate Microsoft Entra ID and Microsoft Graph resources require the global region scope to be included in your integration configuration.


**Available Azure controls**  

| Control title | Resource type | Standard | 
| --- | --- | --- | 
| Azure Container Apps with managed identity enabled should follow least privilege | microsoft.app/containerapps | Azure Foundational Best Practices | 
| Azure Container Apps should not pass Azure SDK credentials as environment variables | microsoft.app/containerapps | Azure Foundational Best Practices | 
| Azure Container Apps should not have external ingress enabled | microsoft.app/containerapps | Azure Foundational Best Practices | 
| Azure Container App environments should not have unrestricted NSG access | microsoft.app/containerapps | Azure Foundational Best Practices | 
| Azure Container App managed environments should not have public IP enabled | microsoft.app/managedenvironments | Azure Foundational Best Practices | 
| Azure role assignments should not grant broad admin access at subscription scope | microsoft.authorization/roleassignments | Azure Foundational Best Practices | 
| Azure role assignments should not grant the User Access Administrator role | microsoft.authorization/roleassignments | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure custom role definitions should not have wildcard administrative permissions | microsoft.authorization/roledefinitions | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Microsoft Cloud Security Benchmark policy assignments should have enforcement mode enabled | microsoft.authorization/policyassignments | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Kubernetes Service (AKS) clusters should not have publicly accessible API servers without IP restrictions | microsoft.containerservice/managedclusters | Azure Foundational Best Practices | 
| Azure Kubernetes Service (AKS) clusters should encrypt Kubernetes secrets at rest | microsoft.containerservice/managedclusters | Azure Foundational Best Practices | 
| Azure Kubernetes Service (AKS) clusters should run a supported Kubernetes version | microsoft.containerservice/managedclusters | Azure Foundational Best Practices | 
| Azure Cosmos DB accounts should have continuous backup enabled | microsoft.documentdb/databaseaccounts | Azure Foundational Best Practices | 
| Azure Database for MySQL flexible servers should have public network access disabled | microsoft.dbformysql/flexibleservers | Azure Foundational Best Practices | 
| Azure Databricks workspaces should be deployed in a customer-managed virtual network | microsoft.databricks/workspaces | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Databricks workspaces should have diagnostic log delivery configured | microsoft.databricks/workspaces | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Databricks workspaces should use customer-managed keys for managed disk encryption | microsoft.databricks/workspaces | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Microsoft Entra ID authorization policies should prohibit default users from registering applications | microsoft.graph/policies/authorizationpolicy | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Entra ID should have security defaults enabled | microsoft.graph/policies/identitysecuritydefaultsenforcementpolicy | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Microsoft Entra tenants should have a Conditional Access policy that blocks access from disallowed geographic locations | microsoft.graph/organization | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Microsoft Entra tenants should have a Conditional Access policy that blocks the device code authentication flow | microsoft.graph/organization | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure conditional access policies should require MFA for all users | microsoft.graph/organization | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Microsoft Entra tenants should require multifactor authentication for risky sign-ins through a Conditional Access policy | microsoft.graph/organization | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure tenants should require MFA via Conditional Access for the Azure Service Management API | microsoft.graph/organization | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| At least one Conditional Access policy should require MFA for Microsoft Admin Portals | microsoft.graph/organization | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Microsoft Entra authorization policies should restrict non-admin users from creating tenants | microsoft.graph/policies/authorizationpolicy | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Microsoft Entra ID authentication methods policies should set the reconfirmation period to a non-zero value | microsoft.graph/policies/authenticationmethodspolicy | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Microsoft Entra authorization policies should restrict user consent for applications | microsoft.graph/policies/authorizationpolicy | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure authorization policies should restrict user consent to verified publisher apps | microsoft.graph/policies/authorizationpolicy | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Microsoft Entra authorization policies should restrict guest user access to their own directory objects | microsoft.graph/policies/authorizationpolicy | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure authorization policies should restrict guest invitations to admin roles only | microsoft.graph/policies/authorizationpolicy | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure authorization policies should restrict security group creation to administrators | microsoft.graph/policies/authorizationpolicy | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Microsoft Entra tenants should require multi-factor authentication to register or join devices | microsoft.graph/organization | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Microsoft Entra ID directory roles should have between 2 and 4 Global Administrators | microsoft.graph/directoryrole | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Entra ID group settings should restrict group creation to administrators | microsoft.graph/organization | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have a diagnostic setting configured for activity logs | microsoft.insights/diagnosticsettings | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have an activity log alert for create policy assignment | microsoft.insights/activitylogalerts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have an activity log alert for policy assignment deletion | microsoft.insights/activitylogalerts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have an activity log alert for create or update Network Security Group operations | microsoft.insights/activitylogalerts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have an activity log alert for Network Security Group deletion | microsoft.insights/activitylogalerts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have an activity log alert for create or update Security Solution | microsoft.insights/activitylogalerts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have an activity log alert for Security Solution deletion | microsoft.insights/activitylogalerts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have an activity log alert for create or update of SQL server firewall rules | microsoft.insights/activitylogalerts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have an activity log alert for deleting SQL server firewall rules | microsoft.insights/activitylogalerts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have an activity log alert configured for Create or Update Public IP Address operations | microsoft.insights/activitylogalerts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have an activity log alert for Public IP address deletion | microsoft.insights/activitylogalerts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have an activity log alert for Service Health incidents | microsoft.insights/activitylogalerts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have at least one Application Insights component configured | microsoft.insights/components | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Key Vaults should have soft delete and purge protection enabled | microsoft.keyvault/vaults | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Key Vaults should have role-based access control enabled | microsoft.keyvault/vaults | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Key Vaults should have public network access disabled when using private endpoints | microsoft.keyvault/vaults | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Key Vaults should use private endpoints | microsoft.keyvault/vaults | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Key Vaults should have purge protection enabled | microsoft.keyvault/vaults | Azure Foundational Best Practices | 
| Azure Key Vaults should restrict network access | microsoft.keyvault/vaults | Azure Foundational Best Practices | 
| Azure Key Vaults should have AuditEvent logging enabled | microsoft.keyvault/vaults | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Key Vault keys in RBAC vaults should have an expiration date set | microsoft.keyvault/vaults/keys | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Key Vault keys in non-RBAC vaults should have an expiration date set | microsoft.keyvault/vaults/keys | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Key Vault secrets in RBAC-enabled vaults should have an expiration date set | microsoft.keyvault/vaults/secrets | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Key Vault secrets in non-RBAC vaults should have an expiration date set | microsoft.keyvault/vaults/secrets | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Key Vault keys should have automatic rotation enabled | microsoft.keyvault/vaults/keys | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure network security groups should restrict inbound RDP access from the internet | microsoft.network/networksecuritygroups | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure network security groups should restrict inbound UDP access from the internet | microsoft.network/networksecuritygroups | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure network security groups should restrict inbound HTTP access from the internet | microsoft.network/networksecuritygroups | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Application Gateway subnets should not have unrestricted NSG access | microsoft.network/networksecuritygroups | Azure Foundational Best Practices | 
| Azure network security groups should have an explicit deny-all rule | microsoft.network/networksecuritygroups | Azure Foundational Best Practices | 
| Azure network security groups should not allow unrestricted inbound access to restricted ports | microsoft.network/networksecuritygroups | Azure Foundational Best Practices | 
| Azure Network Watcher flow logs should have virtual network flow logging enabled with traffic analytics sent to Log Analytics | microsoft.network/networkwatchers/flowlogs | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure network security groups should restrict SSH access from the internet | microsoft.network/networksecuritygroups | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have at least one Azure Bastion host | microsoft.network/bastionhosts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have Microsoft Defender for Servers enabled | microsoft.security/pricings | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Machines should have a healthy vulnerability assessment solution deployed in Microsoft Defender for Cloud | microsoft.security/assessments | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have endpoint protection integration with Microsoft Defender for Cloud enabled | microsoft.security/settings | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have agentless scanning for machines enabled in Microsoft Defender for Servers | microsoft.security/pricings | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have File Integrity Monitoring enabled in Defender for Servers | microsoft.security/pricings | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscription should have Microsoft Defender for Containers enabled | microsoft.security/pricings | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have Microsoft Defender for Storage enabled | microsoft.security/pricings | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have Microsoft Defender for App Service enabled | microsoft.security/pricings | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have Microsoft Defender for Azure Cosmos DB enabled | microsoft.security/pricings | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have Microsoft Defender for open-source relational databases enabled | microsoft.security/pricings | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have Microsoft Defender for Azure SQL Databases enabled | microsoft.security/pricings | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have Microsoft Defender for SQL Servers on Machines enabled | microsoft.security/pricings | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have Microsoft Defender for Key Vault enabled | microsoft.security/pricings | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have Microsoft Defender for Resource Manager enabled | microsoft.security/pricings | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Virtual machines should have system update assessments reported as healthy by Microsoft Defender for Cloud | microsoft.security/assessments | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Microsoft Defender for Cloud security contacts should notify the Owner role of alerts | microsoft.security/securitycontacts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Microsoft Defender for Cloud security contacts should have an additional email address configured | microsoft.security/securitycontacts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure security contacts should have alert email notifications enabled with a sufficiently inclusive minimum severity | microsoft.security/securitycontacts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure security contacts should have attack path email notifications enabled with a risk level configured | microsoft.security/securitycontacts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure subscriptions should have Microsoft Defender for IoT enabled | microsoft.security/iotsecuritysolutions | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure SQL servers should have public network access disabled | microsoft.sql/servers | Azure Foundational Best Practices | 
| SQL servers should have an Azure Active Directory administrator configured | microsoft.sql/servers | Azure Foundational Best Practices | 
| Azure SQL databases should have geo-redundant backup enabled | microsoft.sql/servers/databases | Azure Foundational Best Practices | 
| Azure SQL servers should not use default administrator account names | microsoft.sql/servers | Azure Foundational Best Practices | 
| Azure SQL Managed Instances should have automatic minor version upgrade enabled | microsoft.sql/managedinstances | Azure Foundational Best Practices | 
| Azure Storage accounts should use customer-managed keys for encryption | microsoft.storage/storageaccounts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Storage account file services should have soft delete enabled for file shares | microsoft.storage/storageaccounts/fileservices | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Storage account file shares should restrict SMB protocol versions to SMB 3.1.1 | microsoft.storage/storageaccounts/fileservices | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Storage accounts should use a secure SMB channel encryption algorithm for file shares | microsoft.storage/storageaccounts/fileservices | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Storage accounts should have a key rotation reminder configured | microsoft.storage/storageaccounts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Storage accounts should have shared key access disabled | microsoft.storage/storageaccounts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Storage accounts should use private endpoints for access | microsoft.storage/storageaccounts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Storage accounts should have public network access disabled | microsoft.storage/storageaccounts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Storage accounts should have default network access set to deny | microsoft.storage/storageaccounts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Storage accounts should default to Microsoft Entra authorization in the Azure portal | microsoft.storage/storageaccounts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Storage accounts should require secure transfer | microsoft.storage/storageaccounts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Storage accounts should allow trusted Azure services to bypass network rules | microsoft.storage/storageaccounts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Storage accounts should be configured with the required minimum TLS version | microsoft.storage/storageaccounts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Storage accounts should have cross-tenant replication disabled | microsoft.storage/storageaccounts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Storage accounts should have anonymous blob access disabled | microsoft.storage/storageaccounts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Storage accounts should restrict permanent blob deletion | microsoft.storage/storageaccounts/blobservices | Azure Foundational Best Practices | 
| Azure storage accounts containing activity logs should be encrypted with a customer-managed key | microsoft.storage/storageaccounts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Storage account blob services should have blob soft delete enabled | microsoft.storage/storageaccounts/blobservices | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Storage account blob services should have versioning enabled | microsoft.storage/storageaccounts/blobservices | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Storage account blob services should have blob and container soft delete enabled | microsoft.storage/storageaccounts/blobservices | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Storage accounts should have an Azure Resource Manager delete lock applied | microsoft.storage/storageaccounts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Storage accounts should have a ReadOnly resource manager lock | microsoft.storage/storageaccounts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Storage accounts should use geo-redundant storage | microsoft.storage/storageaccounts | CIS Microsoft Azure Foundations Benchmark v4.0 | 
| Azure Function apps should restrict administrative access | microsoft.web/sites/config | Azure Foundational Best Practices | 
| Azure Functions should not allow anonymous HTTP trigger invocation | microsoft.web/sites/functions | Azure Foundational Best Practices | 
| Azure App Service web apps and function apps should not use unsupported runtime versions | microsoft.web/sites | Azure Foundational Best Practices | 
| Azure Function apps on Premium or Dedicated plans should be integrated with a virtual network | microsoft.web/sites | Azure Foundational Best Practices | 
| Azure App Service web apps should have HTTP logs enabled in diagnostic settings | microsoft.web/sites | CIS Microsoft Azure Foundations Benchmark v4.0 | 