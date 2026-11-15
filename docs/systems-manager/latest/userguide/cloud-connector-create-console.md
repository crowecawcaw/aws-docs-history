

# Create a Cloud Connector (AWS Management Console)
<a name="cloud-connector-create-console"></a>

We recommend that you use the AWS Management Console to create a Cloud Connector. The console wizard collects your Azure tenant and subscription details, and then generates a setup script that configures the Azure side for you. The generated script creates or reuses Microsoft Entra ID application registrations and service principals. It also configures the OIDC federated credentials and assigns the least-privilege Azure roles. If you record with AWS Config, the script also creates the Event Hub resources and diagnostic settings for activity-log streaming.

Because the wizard generates this script, you do not need to run the individual `az` commands in [Azure prerequisites](cloud-connector-prereqs-azure.md) yourself. Those manual steps apply only to the AWS CLI path.

Before you begin, complete the one AWS-side prerequisite: you must enable outbound web identity federation in IAM. For instructions, see [AWS prerequisites](cloud-connector-prereqs-aws.md).

**To create a Cloud Connector for Azure in the console**

1. Open the Systems Manager console. In the navigation pane, choose **Hybrid and Multicloud nodes**. This page shows your existing Cloud connectors and Hybrid activations on separate tabs.

1. Choose **Onboard hybrid nodes**.

1. On the **Azure Cloud connector** card, choose **Configure with script**. This method uses script-based federation with Microsoft Entra ID.

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
**Note**  
You can verify your tenant and subscription details in the Azure portal. Enter the Tenant ID and Subscription IDs from Azure in the AWS Management Console form.

1. If you chose to select specific subscriptions, enter the subscription IDs, one per line or comma-separated. The form validates the UUID format and shows an error for any invalid entry.

1. In the **AWS Config recording** section, choose one of the following options for **Recording**. You can't change this setting after you create the connector. For more information, see [AWS Config recording for Cloud Connectors](cloud-connector-config-recording.md).  
**Record with AWS Config**  
(Default) AWS Config records the connector's Azure resources. The script also sets up a AWS Config application and Event Hub resources for Azure activity logs. If the form detects an existing AWS Config connector for the tenant, it shows an information banner. Provide the following settings:    
**Hosting subscription ID**  
Enter the Azure subscription where the script creates the Event Hub resources for activity-log streaming. If you selected specific subscriptions, you can leave this field blank to use the first selected subscription.  
**Config connector ARN**  
(Optional) Auto-populates if an existing AWS Config connector is detected. Leave this field blank to have the connector created automatically.  
**Event Hub namespace**  
(Optional) Defaults to `awsconfig-{accountId}-{region}`.  
**Event Hub name**  
(Optional) Defaults to `activitylog`.  
**Don't record**  
AWS Config doesn't record the connector's Azure resources. The form doesn't show the AWS Config and Event Hub settings, and the script sets up only the Systems Manager application and its role assignments.

1. The console generates a bash script with your values embedded. Choose **Copy** to copy the script. You run this script in the following procedure. If you change the **Recording** setting after you copy the script, copy and run the updated script.
**Note**  
If you run the script with **Record with AWS Config** and then switch to **Don't record**, running the updated script doesn't remove the Azure resources that the first run created for AWS Config. These are the AWS Config Microsoft Entra ID application and service principal with their Reader role assignment, the Event Hub namespace and Event Hub, and the Activity Log diagnostic settings. Cloud Connectors in your AWS account that record with AWS Config can share these resources. Remove them only if none of your Cloud Connectors records with AWS Config.

The generated script performs the Azure-side setup for you. Run it once, as described in the following procedure, and then return to the console to finish creating the connector.

**To run the generated setup script**

1. Open Azure Cloud Shell, or any terminal that has the Azure CLI installed, and run the script that you copied.

1. When the script runs, a browser window opens for Azure authentication. Sign in to Azure. After you sign in, the script confirms that you have logged in to Microsoft Azure and continues.

1. The script runs to completion. As it runs, it does the following in your Azure tenant:
   + Authenticates to the tenant and selects the configured subscription.
   + If you record with AWS Config, creates the AWS Config Microsoft Entra ID application registration and service principal.
   + If you record with AWS Config, creates the Event Hub namespace and `activitylog` Event Hub, tags the namespace for AWS Config discovery, assigns the AWS Config application the Event Hubs Data Receiver role, and configures Activity Log diagnostic settings to stream to the Event Hub.
   + Creates the Systems Manager Microsoft Entra ID application and service principal, configures the OIDC federated credential, and creates and assigns a least-privilege custom role at the subscription scope.

   When it finishes, the script outputs the `Systems Manager App ID`. If you record with AWS Config, it also outputs the `Config App ID`.

1. Copy the `Systems Manager App ID` value from the script output. If you record with AWS Config, also copy the `Config App ID` value.

1. Return to the AWS Management Console and enter the copied values in the **Azure resource IDs** section.

1. Choose **Create connector**. When you choose **Create connector**, the console creates the IAM federation role, registers the AWS Config connector if you record with AWS Config, and registers the Systems Manager Cloud Connector.

After the connector is created successfully, the **Install and configure SSM Agent** page appears with a success banner. On this page, you enable node management: you select the Azure Regions to manage and configure the three IAM roles that Systems Manager creates. For instructions, see [Enable VM onboarding (AWS Management Console)](cloud-connector-onboarding-console.md). For details about the three IAM roles the console creates, see [IAM roles created by the Systems Manager console](cloud-connector-console-iam-roles.md).

The connector details page shows the following:
+ An overview of the connector (name, ID, provider, and Tenant ID). The **AWS Config recording** field shows **On** or **Off**.
+ Automated validation checks with pass or fail indicators for federation, permissions, and connectivity.
+ The included subscriptions with their management status.
+ Editable tags.
+ Actions such as **Edit details**, **Edit subscriptions with script**, **Delete**, and **Test connector**.

Your new connector appears on the **Cloud connectors** tab of the **Hybrid and Multicloud nodes** page. The **AWS Config recording** column shows whether AWS Config records each connector's Azure resources. From this page, you can create more connectors, edit or delete an existing connector, or switch to the **Hybrid activations** tab.