

# Prerequisites for integrating Security Hub CSPM with Microsoft Azure
<a name="securityhub-azure-prereqs"></a>

Before you integrate Microsoft Azure with AWS Security Hub CSPM, complete the following tasks in your AWS and Azure environments. This helps ensure that you and Security Hub CSPM have the resources and permissions that you need to monitor your Azure resources.

**Topics**
+ [Prerequisites for AWS](#securityhub-azure-prereqs-aws)
+ [Prerequisites for Azure](#securityhub-azure-prereqs-azure)

## Prerequisites for AWS
<a name="securityhub-azure-prereqs-aws"></a>

Verify that you have the following in your AWS account:

AWS Security Hub CSPM enabled  
Security Hub CSPM must be enabled in the AWS account and AWS Region where you want to create the connector.

Console IAM permissions  
The IAM principal creating the connector must have the following permissions:  
+ `config:GetConnector`
+ `config:ListConnectors`
+ `config:PutConnector`

IAM Outbound Identity Federation enabled  
You must enable IAM Outbound Identity Federation in your AWS account. This feature allows AWS services to authenticate to external identity providers (such as Microsoft Entra ID) using federated credentials rather than long-lived secrets.  
After enabling Outbound Identity Federation, note the **Token Issuer URL**. This URL follows the format:  

```
https://{{uuid}}.tokens.sts.global.api.aws
```
You will need this URL when configuring federated identity credentials in Azure.

## Prerequisites for Microsoft Azure
<a name="securityhub-azure-prereqs-azure"></a>

Verify that you have the following in your Azure environment:

Azure tenant  
You must have an Azure tenant in the Azure commercial cloud. Azure Government and Azure China are not supported.

Microsoft Entra ID log availability  
Resource recording requires Microsoft Graph audit logs and sign-in logs from your Microsoft Entra ID tenant. Some Microsoft Entra ID logs require Microsoft Entra ID P1 or P2 licensing.  
If the tenant lacks required logs, resource recording might report partial failures. The app registration and Azure role assignments do not supply missing log data.

Global Administrator role  
The person configuring the Azure environment must have the **Global Administrator** role in Microsoft Entra ID. This role is required to register applications, grant admin consent for Microsoft Graph API permissions, assign RBAC roles at the tenant root management group scope, and configure diagnostic settings for Entra ID Audit Logs.  
In many organizations, the Azure Global Administrator and the AWS security administrator are different people. The Azure setup can be completed independently using the generated setup script.

Azure app registration  
You must register an application in Microsoft Entra ID. This application serves as the identity that AWS uses to authenticate to your Azure environment using federated credentials. No client secrets are required.

Azure Event Hub  
You must create an Azure Event Hub namespace and Event Hub instance to receive Activity Log and Entra ID Audit Log events. The setup script automates this creation.

Microsoft Graph API permissions  
The registered application requires the following Microsoft Graph API permissions (Application type, requires admin consent):  
+ `Directory.Read.All` – Read directory data including users, groups, and service principals.
+ `AuditLog.Read.All` – Read Entra ID audit log events.
+ `Policy.Read.All` – Read organization policies and conditional access configurations.

Azure RBAC Reader role  
The service principal must be assigned the **Reader** role at the **tenant root management group** scope. This grants read-only access to all Azure resources across all subscriptions in the tenant.

After you complete these tasks, you're ready to [configure your Azure environment](securityhub-azure-setup-azure.md).