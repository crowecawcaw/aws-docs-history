

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Create a Cloud Connector (AWS Management Console)
<a name="cloud-connector-create-console"></a>

We recommend that you use the AWS Management Console to create a Cloud Connector. The console wizard collects your Azure tenant and subscription details, and then generates a setup script that configures the Azure side for you. The generated script creates or reuses Microsoft Entra ID application registrations and service principals. It also configures the OIDC federated credentials, assigns the least-privilege Azure roles, and creates the Event Hub resources and diagnostic settings for activity-log streaming.

Because the wizard generates this script, you do not need to run the individual `az` commands in [Azure prerequisites](cloud-connector-prereqs-azure.md) yourself. Those manual steps apply only to the AWS CLI path.

Before you begin, complete the one AWS-side prerequisite: you must enable outbound web identity federation in IAM. For instructions, see [AWS prerequisites](cloud-connector-prereqs-aws.md).

**To create a Cloud Connector for Azure in the console**

1. Open the Systems Manager console. In the navigation pane, choose **Hybrid and Multicloud nodes**. This page shows your existing Cloud connectors and Hybrid activations on separate tabs.

1. Choose **Onboard hybrid nodes**.

1. For the onboarding method, choose **Azure Cloud connector**, and then choose **Configure with script**. This method uses script-based federation with Microsoft Entra ID. We recommend it for managing Azure VMs at scale.

1. On the **Create Cloud Connector** page, provide the following details:  
**Connector name**  
Enter a name for the Cloud Connector.  
**Description**  
(Optional) Enter a description for the Cloud Connector.  
**Azure federation role**  
Choose the recommended auto-created service role, or choose an existing role that you provide. For details about the roles the console creates, see [IAM roles created by the Systems Manager console](cloud-connector-console-iam-roles.md).  
**Tenant ID**  
Enter your Microsoft Entra ID tenant UUID.  
**Tenant name**  
(Optional) Enter a friendly name for the tenant.  
**Azure subscriptions**  
Choose whether to select the entire tenant (recommended) or to select specific subscriptions. A Cloud Connector supports up to 75 Azure subscription targets.  
**Hosting subscription ID**  
Enter the Azure subscription where the Event Hub resources are created for activity-log streaming.
**Note**  
You can verify your tenant and subscription details in the Azure portal. Enter the Tenant ID and Subscription IDs from Azure in the AWS Management Console form.

1. If you chose to select specific subscriptions, enter the subscription IDs, one per line or comma-separated. The form validates the UUID format and shows an error for any invalid entry. The **Hosting subscription ID** auto-populates.

1. Review the AWS Config connector and Event Hub settings. If the form detects an existing AWS Config connector for the tenant, it shows an information banner. The following fields are optional:  
**Config connector ARN**  
Auto-populates if an existing AWS Config connector is detected. Leave this field blank to have the connector created automatically.  
**Event Hub namespace**  
Defaults to `awsconfig-{accountId}-{region}`.  
**Event Hub name**  
Defaults to `activitylog`.

1. The console generates a bash script with your values embedded. Choose **Copy** to copy the script. You run this script in the following procedure.

The generated script performs the Azure-side setup for you. Run it once, as described in the following procedure, and then return to the console to finish creating the connector.

**To run the generated setup script**

1. Open Azure Cloud Shell, or any terminal that has the Azure CLI installed, and run the script that you copied.

1. When the script runs, a browser window opens for Azure authentication. Sign in to Azure. After you sign in, the script confirms that you have logged in to Microsoft Azure and continues.

1. The script runs to completion. As it runs, it does the following in your Azure tenant:
   + Authenticates to the tenant and selects the configured subscription.
   + Creates the AWS Config Microsoft Entra ID application registration and service principal.
   + Creates the Event Hub namespace and `activitylog` Event Hub, tags the namespace for AWS Config discovery, assigns the AWS Config application the Event Hubs Data Receiver role, and configures Activity Log diagnostic settings to stream to the Event Hub.
   + Creates the Systems Manager Microsoft Entra ID application and service principal, configures the OIDC federated credential, and creates and assigns a least-privilege custom role at the subscription scope.

   When it finishes, the script outputs the SSM App ID and the Config App ID.

1. Copy the SSM App ID and Config App ID values from the script output.

1. Return to the AWS Management Console and enter the copied values in the **Azure resource IDs** section.

1. Choose **Create connector**. When you choose **Create connector**, the console creates the IAM federation role, registers the AWS Config connector, and registers the Systems Manager Cloud Connector.

After the connector is created successfully, the **Install and configure SSM Agent** page appears with a success banner. On this page, you enable node management: you select the Azure Regions to manage and configure the three IAM roles that Systems Manager creates. For instructions, see [Enable VM onboarding (AWS Management Console)](cloud-connector-onboarding-console.md). For details about the three IAM roles the console creates, see [IAM roles created by the Systems Manager console](cloud-connector-console-iam-roles.md).

The connector details page shows the following:
+ An overview of the connector (name, ID, provider, and Tenant ID).
+ Automated validation checks with pass or fail indicators for federation, permissions, and connectivity.
+ The included subscriptions with their management status.
+ Editable tags.
+ Actions such as **Edit details**, **Edit subscriptions with script**, **Delete**, and **Test connector**.

Your new connector appears on the **Cloud connectors** tab of the **Hybrid and Multicloud nodes** page. From this page, you can create more connectors, edit or delete an existing connector, or switch to the **Hybrid activations** tab.