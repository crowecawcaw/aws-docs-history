

# Enable VM onboarding
<a name="cloud-connector-gcp-enable-vm-onboarding"></a>

After you create a Cloud Connector, you must enable VM onboarding so that Systems Manager can discover and register the GCP VMs targeted by the connector. Enabling VM onboarding creates a State Manager association named `AWSSSMGcpConnector-{{CONNECTOR_ID}}` that uses the `AWS-InstallSSMAgentOnGCP` Automation document. The association runs the `AWS-InstallSSMAgentOnGCP` runbook against the Cloud Connector.

The association runs when you create it and then every 48 hours. Each run onboards the GCP VMs in the connector's scope that aren't yet managed nodes, so VMs that you create later are onboarded on the next scheduled run.

The `AWS-InstallSSMAgentOnGCP` runbook runs the following child runbooks in sequence:

1. `AWS-InstallSSMAgentOnGCP-SetupAndActivation` – Runs once per VM. It authenticates to GCP through workload identity federation, creates a Systems Manager hybrid activation, and writes the activation to the VM's metadata.

1. `AWS-InstallSSMAgentOnGCP-ApplyOSPolicy` – Runs once. It creates GCP VM Manager OS policy orchestrators that install SSM Agent and register Linux and Windows VMs across the projects and Regions in scope.

1. `AWS-InstallSSMAgentOnGCP-VerifyVMStatus` – Runs once per VM. It waits for the VM to come online as a managed node, checks OS policy compliance, and removes the activation metadata from the VM.

Systems Manager tags each managed instance with the `CloudConnector` tag (see [Tags applied to managed instances](cloud-connector-gcp-managed-instance-tags.md)).

VM onboarding requires two IAM roles. The automation dispatch role is assumed by State Manager to launch the Automation workflow. The automation assume role is used by the workflow to create activations and authenticate with GCP. If you enable onboarding through the AWS Management Console, Systems Manager can create these roles automatically. For more information about the required trust policies and permissions, see [IAM roles created by the Systems Manager console](cloud-connector-gcp-console-iam-roles.md).