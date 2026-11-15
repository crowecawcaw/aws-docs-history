

# Create a Cloud Connector (AWS Management Console)
<a name="cloud-connector-gcp-create-console"></a>

We recommend that you use the AWS Management Console to create a Cloud Connector. The console wizard collects your GCP host project and target project details, and then generates a setup script that configures the GCP side for you. The generated script does the following:
+ Creates or reuses a Workload Identity Pool, an OpenID Connect (OIDC) provider, and a connector service account in your host project.
+ Creates a least-privilege custom role in each target project and grants it to the connector service account.
+ Enables VM Manager (OS Config) and sets up the OS Policy Orchestrator service agents.
+ If you record with AWS Config, creates the AWS Config service account, the Pub/Sub topic and subscription, and the audit log exports that stream resource-change events.

Because the wizard generates this script, you do not need to run the individual `gcloud` commands in [GCP prerequisites](cloud-connector-gcp-prereqs-gcp.md) yourself. Those manual steps apply only to the AWS CLI path.

Before you begin, complete the one prerequisite on the AWS side: You must enable outbound web identity federation in IAM. For instructions, see [AWS prerequisites](cloud-connector-gcp-prereqs-aws.md).

**To create a Cloud Connector for GCP in the console**

1. Open the Systems Manager console. In the navigation pane, choose **Hybrid and Multicloud nodes**. This page shows your existing Cloud connectors and Hybrid activations on separate tabs.

1. Choose **Onboard hybrid nodes**.

1. On the **GCP Cloud connector** card, choose **Configure with script**. This method uses workload identity federation.

1. On the **Create GCP Cloud connector with a script** page, under **Connector details**, provide the following:  
**Connector name**  
Enter a name for the Cloud Connector.  
**Description**  
(Optional) Enter a description for the Cloud Connector.  
**IAM role**  
Choose **Create a GCP federation role with recommended permissions**, or choose **Use an existing GCP federation role**. For more information about the roles the console creates, see [IAM roles created by the Systems Manager console](cloud-connector-gcp-console-iam-roles.md).

1. Under **GCP details**, provide the following:  
**Host project ID**  
Enter the GCP project that hosts the Workload Identity Pool and the service accounts that the script creates.  
**Scope**  
Choose **Entire organization** to manage the projects that exist when you run the script (rerun the script to add projects later), or choose **Specific projects** to target up to 75 projects.  
**Organization ID**  
Enter the numeric ID of your GCP organization. This field is required if you choose **Entire organization**. If you choose **Specific projects**, the field appears only when you record with AWS Config, and it's required if the host project belongs to an organization.  
**Target project IDs**  
If you chose **Specific projects**, enter the target project IDs, one per line or comma-separated. The form validates each entry.

1. Under **AWS Config recording**, for **Recording**, choose one of the following. You can't change this setting after you create the connector.  
**Record with AWS Config**  
(Default) AWS Config records this connector's GCP resources. The script also sets up an AWS Config service account and a Pub/Sub topic for GCP audit logs.  
**Don't record**  
AWS Config doesn't record this connector's GCP resources, and the console doesn't create an AWS Config connector. If you enable VM onboarding, new VMs get SSM Agent at the next association run.

   If you choose **Record with AWS Config**, the following fields are available. If the form detects an existing AWS Config connector for the host project, it shows an information banner.  
**Config connector ARN**  
Auto-populates if an existing AWS Config connector is detected. Leave this field blank to have the console create or reuse a AWS Config connector for the host project. If you enter an existing ARN, the Config service account and Pub/Sub topic on this page are not applied to it.  
**Pub/Sub topic**  
The script creates this topic in the host project, and AWS Config pulls GCP resource-change events from it. Defaults to `aws-config-{accountId}`.
**Changing the recording choice**  
If you change the recording choice after you copy the script or paste its output, the console doesn't create the connector until you switch back or copy and run the updated script.

1. The console generates a bash script with your values embedded. Choose **Copy** to copy the script. You run this script in the following procedure.

The generated script performs the GCP-side setup for you. Run it once, as described in the following procedure, and then return to the console to finish creating the connector.

**To run the generated setup script**

1. Open Google Cloud Shell, or any terminal that has `gcloud` and `jq` installed, and run the script that you copied. The running identity must be able to manage IAM, service accounts, and services in the host project and each target project. For the organization scope, it must also be able to grant roles at the organization level.

1. Wait for the script to finish. As it runs, it does the following:
   + Enables the required APIs in the host project.
   + For the organization scope, discovers the active projects.
   + Checks the `iam.disableCrossProjectServiceAccountUsage` organization policy constraint on the host project. If the constraint is enforced and you target other projects, the script stops and provides guidance.
   + Creates or reuses the Workload Identity Pool, the OIDC provider (which trusts your IAM federation role), and the connector service account.
   + If you record with AWS Config, creates the AWS Config service account, the Pub/Sub topic and subscription, and grants AWS Config its discovery and read roles.
   + In each target project, enables VM Manager, onboards the OS Policy Orchestrator agents, creates the custom role and grants it to the connector service account, and grants use of the VMs' service accounts. If you record with AWS Config, it also sets up an audit log export to the topic.
   + For the organization scope, grants the organization-level roles.

   When it finishes, the script prints the Workload Identity Pool provider and the service account email. If you record with AWS Config, it also prints the Config service account email and the Pub/Sub topic. The script is safe to rerun.

1. Copy the values from the script output.

1. Return to the AWS Management Console, and under **Resource IDs**, enter the following values. Enter the Config service account email only if you record with AWS Config and you are not using an existing AWS Config connector.  
**Workload identity pool provider**  
Enter the Workload Identity Pool provider resource name from the script output.  
**Service account email**  
Enter the connector service account email from the script output.  
**Config service account email**  
Enter the AWS Config service account email from the script output.

1. Under **Node management**, choose **Enable node management now** to continue to the node onboarding page, or choose **Create connector only** to enable node management later from the connector details page.

1. (Optional) Add tags.

1. Review the **Summary**, and then choose **Create connector**. The console creates the IAM federation role (if you chose the recommended role), registers the AWS Config connector, and registers the Systems Manager Cloud Connector.

If you chose **Enable node management now**, the **Install and configure SSM Agent** page appears. On this page, you select the GCP Regions to manage and configure the three IAM roles that Systems Manager creates. For instructions, see [Enable VM onboarding (AWS Management Console)](cloud-connector-gcp-onboarding-console.md). For more information about the three IAM roles the console creates, see [IAM roles created by the Systems Manager console](cloud-connector-gcp-console-iam-roles.md).

On the connector details page, you can view the following:
+ An overview of the connector (name, ID, provider, organization ID, Workload identity pool provider, and service account email).
+ Whether AWS Config records the connector's resources (**AWS Config recording**: On or Off). The **Cloud connectors** tab shows the same setting in a column.
+ Automated validation checks with pass or fail indicators for federation, permissions, and connectivity.
+ The included projects with their management status.
+ Editable tags.
+ Actions such as **Edit**, **Edit projects**, **Delete**, and **Test connector**.

For a connector that doesn't record with AWS Config, **Edit projects** doesn't show the Pub/Sub topic field, and its script leaves out the AWS Config parts.

Your new connector appears on the **Cloud connectors** tab of the **Hybrid and Multicloud nodes** page. From this page, you can create more connectors, edit or delete an existing connector, or switch to the **Hybrid activations** tab.

**Note**  
If you change the recording choice to **Don't record** after you run the setup script, the AWS Config resources that the script created stay in your GCP host project: the AWS Config service account and its role grants, the Pub/Sub topic and subscription, and the audit log exports. Every Cloud Connector for the same AWS account and host project shares these resources in all AWS Regions, except the Pub/Sub subscription, which is created per AWS Region. Remove them only if none of those Cloud Connectors records with AWS Config.