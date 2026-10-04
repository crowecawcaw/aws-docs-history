

# Remove an Azure DevOps integration
<a name="remove-azure-devops"></a>

This procedure removes the connection between AWS Security Agent and an Azure DevOps organization. Use it when you no longer need AWS Security Agent to access that organization’s repositories.

## Prerequisites for removal
<a name="_prerequisites_for_removal"></a>

Before removing an Azure DevOps integration:
+ Check which Agent Spaces have repositories connected from this integration.
+ Note that removing the integration breaks code review, penetration testing context, threat modeling, and automated remediation for all connected repositories.

## Step 1: Removing the integration from AWS Security Agent
<a name="remove-azure-devops-step-1"></a>

First, remove the integration in the AWS Security Agent Management Console.

1. In the AWS Security Agent Management Console, choose **Integrations**.

1. Locate the Azure DevOps integration you want to remove.

1. Select the integration.

1. Choose **Remove**.

1. Review the confirmation dialog.

1. Choose **Confirm removal**.

When you remove the integration, AWS Security Agent deletes the pull request service hook subscriptions that it created in your Azure DevOps projects.

**Important**  
Remove the integration before you remove the **AWS Continuum for Azure DevOps** service principal from your organization. AWS Security Agent uses the service principal’s Service Hooks permissions to delete its subscriptions. If you remove the service principal first, the removal might fail.

## Step 2: Removing the service principal from your organization
<a name="remove-azure-devops-step-2"></a>

After you remove the integration, you can remove the **AWS Continuum for Azure DevOps** service principal from your Azure DevOps organization.

1. In Azure DevOps, choose **Organization settings**.

1. Choose **Users**.

1. Locate **AWS Continuum for Azure DevOps**.

1. Open the actions menu for the service principal.

1. Choose **Remove from organization**.

**Note**  
If you plan to register the same Azure DevOps organization again, you can keep the service principal in the organization. Registering again then doesn’t require you to add the service principal or repeat the Service Hooks grant.

## (Optional) Step 3: Removing the application from Microsoft Entra ID
<a name="remove-azure-devops-step-3"></a>

To also revoke the admin consent that you granted when you registered the integration, delete the **AWS Continuum for Azure DevOps** enterprise application from your Microsoft Entra tenant.

1. In the Azure portal, choose **Microsoft Entra ID**.

1. Choose **Enterprise applications**.

1. Search for **AWS Continuum for Azure DevOps**.

1. Select **AWS Continuum for Azure DevOps**.

1. Choose **Properties**.

1. Choose **Delete**.

**Important**  
The **AWS Continuum for Azure DevOps** enterprise application is shared by every Azure DevOps integration that uses your Microsoft Entra tenant. Delete it only if no other Azure DevOps organization in the tenant is connected to AWS Security Agent.