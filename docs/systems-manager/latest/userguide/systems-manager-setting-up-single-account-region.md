• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Setting up Systems Manager unified

console for a single account and Region

To set up the Systems Manager unified console experience for a single AWS account and AWS Region
you don't need to use Organizations or register a delegated administrator account. The setup process
for the Systems Manager console experience completes many prerequisite tasks for you. Depending on the
features you choose to configure, this includes enabling Default Host Management Configuration
to provide the required IAM permissions to your nodes and more. The following is a detailed
list of the resources created by Systems Manager for the unified console.

## Unified console resources

Depending on the features you choose to configure, some resources might not be
created.

IAM roles

- `RoleForOnboardingAutomation` – Allows Systems Manager to manage resources
  during the setting up process. For more information about the policy, see [AWSQuickSetupSSMManageResourcesExecutionPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSQuickSetupSSMManageResourcesExecutionPolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSQuickSetupSSMManageResourcesExecutionPolicy").
- `RoleForLifecycleManagement` – Allows Lambda to manage the
  lifecycle of resources created by the setting up process. For more information about the
  policy, see [AWSQuickSetupSSMLifecycleManagementExecutionPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSQuickSetupSSMLifecycleManagementExecutionPolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSQuickSetupSSMLifecycleManagementExecutionPolicy").
- `RoleForAutomation` – A service role for Systems Manager Automation to
  assume to execute runbooks. For more information, see [Create the service roles for Automation using
  the console](automation-setup-iam.md "automation-setup-iam.md").
- `AWSSSMDiagnosisAdminRole` – An automation execution role for the
  diagnosis runbook. For more information about the policies, see [AWS-SSM-DiagnosisAutomation-AdministrationRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-AdministrationRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-AdministrationRolePolicy"),
  [AWS-SSM-Automation-DiagnosisBucketPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-Automation-DiagnosisBucketPolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-Automation-DiagnosisBucketPolicy"), and [AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy").
- `AWSSSMRemediationAdminRole` – An automation execution role for
  the remediation runbook. For more information about the policies, see [AWS-SSM-RemediationAutomation-AdministrationRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-AdministrationRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-AdministrationRolePolicy"),
  [AWS-SSM-Automation-DiagnosisBucketPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-Automation-DiagnosisBucketPolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-Automation-DiagnosisBucketPolicy"), and [AWS-SSM-RemediationAutomation-OperationalAccountAdministrationRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-OperationalAccountAdministrationRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-OperationalAccountAdministrationRolePolicy").
- `ManagedInstanceCrossAccountManagementRole` – Allows Systems Manager to
  gather managed node information across accounts.

State Manager associations

- `EnableDHMCAssociation` – Runs daily and ensures Default Host
  Management Configuration is enabled.
- `SystemAssociationForEnablingExplorer` – Runs daily and ensures
  Explorer is enabled. Explorer is used to sync data from your managed nodes.
- `EnableAREXAssociation` – Runs daily and ensures AWS Resource Explorer is
  enabled. Resource Explorer is used to determine which Amazon EC2 instances in your organization aren't
  managed by Systems Manager.
- `SSMAgentUpdateAssociation` – Runs every 14 days and ensures the
  latest available version of SSM Agent is installed on your managed nodes.
- `SystemAssociationForInventoryCollection` – Runs every 12 hours
  and collects inventory data from your managed nodes.

S3 buckets

- `DiagnosisBucket` – Stores data collected from the diagnosis
  runbook execution.

Lambda functions

- `SSMLifecycleOperatorLambda` – Allows principals to access all
  AWS Systems Manager Quick Setup actions.
- `SSMLifecycleResource` – Custom resource to help manage the
  lifecycle of resources created by the setting up process.

Additionally, after the setup process completes you can select the **Diagnose and
remediate** node task to automatically apply fixes to nodes that aren't reporting
as managed by Systems Manager. This can include identifying issues such as network connectivity issues
to the Systems Manager endpoints, and more.

## Set up the unified

console

###### To set up Systems Manager for a single account and Region

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. Select **Enable Systems Manager**.
3. In the **Feature configurations** section, choose the options that
   you want to enable for your configuration:

 

**Enable Default Host Management Configuration (DHMC)**

Allows Systems Manager to configure DHMC. This feature allows Systems Manager to use an IAM role
to ensure that all Amazon EC2 instances in the account and Region have the permissions
necessary to be managed by Systems Manager. You can also specify the frequency of drift
remediation. Configuration drift occurs whenever a user makes any change to a
service or feature that conflicts with the selections made through your
configuration. Systems Manager checks for configuration drift and attempts to remediate it
based on the frequency you specify. You must specify a value between 1 and 31
days. If you've already configured DHMC in a Region, Systems Manager doesn't change the
IAM role you previously selected. For more information about DHMC, see [Managing EC2
instances automatically with Default Host Management Configuration](fleet-manager-default-host-management-configuration.md "fleet-manager-default-host-management-configuration.md").

DHMC makes it possible to manage Amazon EC2 instances without your having to
manually create an AWS Identity and Access Management (IAM) instance profile. We encourage you to choose
this option to ensure that your EC2 instances have the permissions necessary to be
managed by Systems Manager.

**Enable inventory metadata collection**

Enables Systems Manager to configure collection of the following types of metadata from
your nodes:

    * **AWS components** – EC2 driver,
     agents, versions, and more.
    * **Applications** – Application names,
     publishers, versions, and more.
    * **Node details** – System name,
     operating system (OS) name, OS version, last boot, DNS, domain, work group, OS
     architecture, and more.
    * **Network configuration** – IP
     address, MAC address, DNS, gateway, subnet mask, and more.
    * **Services** – Name, display name,
     status, dependent services, service type, start type, and more (Windows Server nodes
     only).
    * **Windows roles** – Name, display
     name, path, feature type, installed state, and more (Windows Server nodes
     only).
    * **Windows updates** – Hotfix ID,
     installed by, installed date, and more (Windows Server nodes only).

Specify the frequency at which inventory is collected. You must specify a
value between 1 and 744 hours. For more information about Inventory, a tool in
AWS Systems Manager, see [AWS Systems Manager Inventory](systems-manager-inventory.md "systems-manager-inventory.md").

**Enable automatic Systems Manager (SSM) Agent updates**

Enables Systems Manager to check for a new version of the agent at the frequency you
specify. The value for the frequency must be between 1 and 31 days. If there is a
new version, then Systems Manager automatically updates the agent on your managed node to
the latest released version. Systems Manager doesn't install the agent on instances where
it's not already present. For information about which AMIs have SSM Agent
preinstalled, see [Find AMIs with the SSM Agent
preinstalled](ami-preinstalled-agent.md "ami-preinstalled-agent.md").

We encourage you to choose this option to ensure that your nodes are always
running the most up-to-date version of SSM Agent. For more information about
SSM Agent, including information about how to manually install the agent, see [Working with SSM Agent](ssm-agent.md "ssm-agent.md"). 4. Choose **Submit**.
