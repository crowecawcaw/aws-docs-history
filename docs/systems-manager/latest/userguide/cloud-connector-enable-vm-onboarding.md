

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Enable VM onboarding
<a name="cloud-connector-enable-vm-onboarding"></a>

After you create a Cloud Connector, you must enable VM onboarding so that Systems Manager can discover and register the Azure VMs targeted by the connector. Enabling VM onboarding creates a State Manager association named `AWSSSMAzureConnector-{{CONNECTOR_ID}}` that uses the `AWS-InstallSSMAgentOnAzure` Automation document. The association targets VMs through the Cloud Connector.

Systems Manager onboards Azure VMs through an event-driven process. When a new VM is created in Azure, the AWS Config connector receives the change event through the Azure Event Hub and forwards it to Systems Manager. The State Manager association then dispatches an Automation execution to onboard the newly discovered VM.

The association also runs on a periodic 48-hour schedule as a safety net. This ensures that any VMs missed due to lost events or transient failures are eventually discovered and onboarded.

For each Azure VM to onboard, the Automation performs the following steps:

1. Creates a Systems Manager hybrid activation for the VM.

1. Installs the SSM Agent on the VM using an Azure VM extension.

1. Registers the VM as a managed instance in Systems Manager using the hybrid activation credentials.

1. Tags the managed instance with the `CloudConnector` tag (see [Tags applied to managed instances](cloud-connector-managed-instance-tags.md)).

1. Deletes the hybrid activation, which is no longer needed after registration completes.

VM onboarding requires two IAM roles. The automation dispatch role is assumed by State Manager to launch the Automation workflow. The automation assume role is used by the workflow to create activations and authenticate with Azure. If you enable onboarding through the AWS Management Console, Systems Manager can create these roles automatically. For details about the required trust policies and permissions, see [IAM roles created by the Systems Manager console](cloud-connector-console-iam-roles.md).