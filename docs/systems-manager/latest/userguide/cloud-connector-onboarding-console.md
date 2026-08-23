# Enable VM onboarding (AWS Management Console)

To enable VM onboarding in the AWS Management Console:

1. Open the Systems Manager console and navigate to **Hybrid
   Cloud**.
2. Choose the Cloud Connector for which you want to enable VM
   onboarding.
3. Choose **Install and configure SSM Agent**.
4. Configure the following settings:

Azure Region selection

Choose whether to enable all Azure Regions (recommended)
or select specific Regions where your VMs are
located.

State Manager association role (automation dispatch role)

The IAM role that State Manager assumes to dispatch
automation executions. This role passes the Automation
execution role to Automation when launching the
onboarding workflow. For the trust policy and permissions
required by this role, see [Automation dispatch role](cloud-connector-automation-dispatch-role.md "cloud-connector-automation-dispatch-role.md").

Automation execution role (automation assume role)

The IAM role that Automation assumes to execute the
agent installation runbook. This role assumes the Azure
federation role to authenticate with Azure through OIDC,
creates hybrid activations, and manages managed instances.
For the trust policy and permissions required by this
role, see [Automation assume role](cloud-connector-automation-assume-role.md "cloud-connector-automation-assume-role.md").

Hybrid activation instance role

The IAM role assigned to Azure VMs when they register
as managed instances. This role must trust
`ssm.amazonaws.com` and have the
`AmazonSSMManagedInstanceCore` policy
attached. For more information, see [Managed instance role](cloud-connector-managed-instance-role.md "cloud-connector-managed-instance-role.md").

VM tags

Optionally add tags that will be applied to managed
instances during onboarding. The
`CloudConnector` tag is applied automatically
(see [Tags applied to managed instances](cloud-connector-managed-instance-tags.md "cloud-connector-managed-instance-tags.md")).
You can add additional tags to further organize your
managed fleet. 5. Choose **Connect**.
Systems Manager creates the association and begins onboarding Azure VMs. You can
monitor the progress on the connector details page.
