

# Prerequisites for integrating Security Hub with Microsoft Azure
<a name="securityhub-v2-azure-prereqs"></a>

Before you integrate Microsoft Azure with AWS Security Hub, complete the following tasks in your AWS and Azure environments. This helps ensure that you and Security Hub have the resources and permissions that you need to monitor your Azure resources.

**Topics**
+ [Prerequisites for AWS](#securityhub-v2-azure-prereqs-aws)
+ [Prerequisites for Azure](#securityhub-v2-azure-prereqs-azure)

## Prerequisites for AWS
<a name="securityhub-v2-azure-prereqs-aws"></a>

Verify that you have the following in your AWS account:

**AWS Security Hub enabled**  
Security Hub must be enabled in the AWS account and AWS Region where you want to create the connector. You must enable Security Hub before creating an Azure connector.

**AWS Security Hub CSPM enabled**  
Security Hub CSPM must be enabled in the same AWS account and AWS Region. The Azure integration relies on Security Hub CSPM for resource configuration evaluation.

**Console IAM permissions**  
The IAM principal creating the connector must have the following permissions:  
+ `config:GetConnector`
+ `config:ListConnectors`
+ `config:PutConnector`

**IAM Outbound Identity Federation enabled**  
You must enable IAM Outbound Identity Federation in your AWS account. This feature allows AWS services to authenticate to external identity providers (such as Microsoft Entra ID) using federated credentials rather than long-lived secrets.  
After enabling Outbound Identity Federation, note the **Token Issuer URL**. This URL follows the format:  

```
https://{{uuid}}.tokens.sts.global.api.aws
```
You will need this URL when configuring federated identity credentials in Azure.

## Prerequisites for Microsoft Azure
<a name="securityhub-v2-azure-prereqs-azure"></a>

Verify that you have the following in your Azure environment:

**Azure tenant**  
You must have an Azure tenant in the Azure commercial cloud. Azure Government and Azure China are not supported.

**Microsoft Entra ID log availability**  
Resource recording requires Microsoft Graph audit logs and sign-in logs from your Microsoft Entra ID tenant. Some Microsoft Entra ID logs require Microsoft Entra ID P1 or P2 licensing.  
If the tenant lacks required logs, resource recording might report partial failures. The app registration and Azure role assignments do not supply missing log data.

**Global Administrator role**  
You must have the **Global Administrator** role in Microsoft Entra ID to configure the Azure environment. This role is required to register applications, grant admin consent for Microsoft Graph API permissions, assign RBAC roles at the tenant root management group scope, and configure diagnostic settings for Entra ID Audit Logs.  
In addition to Global Administrator, you need the following Azure RBAC roles to create the resources that the integration requires:  
+ **User Access Administrator** (or Owner) at the root scope (`/`) – to assign RBAC roles at the tenant root management group scope.
+ **Resource Policy Contributor** (or Owner) at the tenant root management group scope – to create the Azure Policy definitions and assignments that automate diagnostic settings and remediation.
+ **Contributor** (or Owner) at the subscription scope that hosts the Event Hub – to create the Event Hub namespace and related resources.
In many organizations, the Azure Global Administrator and the AWS security administrator are different people. The Azure setup can be completed independently using the generated setup script.

After you complete these tasks, you are ready to [configure your Azure environment](securityhub-v2-azure-setup-azure.md).