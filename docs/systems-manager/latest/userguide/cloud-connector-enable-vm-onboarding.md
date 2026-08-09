# Enable VM onboarding

After you create a Cloud Connector, you must enable VM onboarding so that Systems Manager
can discover and register the Azure VMs targeted by the connector. Enabling VM
onboarding creates a State Manager association named
`AWSSSMAzureConnector-`CONNECTOR_ID``
that uses the `AWS-InstallSSMAgentOnAzure` Automation document. The
association targets VMs through the Cloud Connector.

Systems Manager onboards Azure VMs through an event-driven process. When a new VM is
created in Azure, the AWS Config connector receives the change event through the
Azure Event Hub and forwards it to Systems Manager. The State Manager association then dispatches
an Automation execution to onboard the newly discovered VM.

The association also runs on a periodic 48-hour schedule as a safety net. This
ensures that any VMs missed due to lost events or transient failures are
eventually discovered and onboarded.

For each Azure VM to onboard, the Automation performs the following steps:

1. Creates a Systems Manager hybrid activation for the VM.
2. Installs the SSM Agent on the VM using an Azure VM extension.
3. Registers the VM as a managed instance in Systems Manager using the hybrid
   activation credentials.
4. Tags the managed instance with the `CloudConnector` tag
   (see [Tags applied to managed instances](cloud-connector-managed-instance-tags.md "cloud-connector-managed-instance-tags.md")).
5. Deletes the hybrid activation, which is no longer needed after
   registration completes.
   VM onboarding requires two IAM roles. The Automation dispatch role is assumed by
   State Manager to launch the Automation workflow. The Automation assume role is used by
   the workflow to create activations and authenticate with Azure. If you
   enable onboarding through the AWS Management Console, Systems Manager can create these roles
   automatically. For details about the required trust policies and permissions, see
   [IAM roles created by the Systems Manager console](cloud-connector-console-iam-roles.md "cloud-connector-console-iam-roles.md").
