• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Setting up Systems Manager unified console

for an organization

The setup process for the Systems Manager unified console experience is completed from the AWS Management Console
with just a few clicks. To set up Systems Manager for an AWS Organizations organization, you must have access to
the management account for your organization and another account in your organization to use as
a delegated administrator. Access to the management account is only required to enable or
disable Systems Manager. To manage your nodes, you'll use the delegated administrator account.

## Prerequisites

When managing nodes across an organization, Systems Manager uses various dependent services to set
up and enhance the functionality of the unified console. As a result, Systems Manager must enable
trusted access and register a delegated administrator account for the following
services:

- AWS CloudFormation - Deploys resources required for Systems Manager to your accounts.
- AWS Resource Explorer - Searching and filtering EC2 instances in your accounts.
- AWS Systems Manager Explorer - Monitoring and troubleshooting the health of resources
  deployed for Systems Manager in your accounts.
- AWS Systems Manager Quick Setup - Deploys Quick Setup configurations required for Systems Manager to your
  accounts.

Before you begin, make sure you're not already over the quota for delegated
administrators for any of these dependent services. Otherwise, you won't be able to register
the delegated administrator accounts necessary to enable Systems Manager. When you enable Systems Manager for an
organization, every account in your organization is included. At this time, there is no
provision for excluding accounts from the setting up process. When you enable Systems Manager, you can
choose the AWS Regions you want to include. Only Regions that currently support the Systems Manager
unified console can be selected. To learn more about the Regions where the console
experience is available, see [Supported
AWS Regions](what-is-systems-manager.md#regions "what-is-systems-manager.md#regions").

## Unified console resources

The setup process for the Systems Manager unified console completes many prerequisite tasks for
you. Depending on the features you choose to configure, this includes enabling Default Host
Management Configuration to provide the required IAM permissions to your nodes and more.
The following is a detailed list of the resources created by Systems Manager for the unified console.
Depending on the features you choose to configure, some resources might not be
created.

AWS Resource Explorer managed views

- `AWSManagedViewForSSM` – Allows Systems Manager to access resource
  information indexed by Resource Explorer for your organization. These managed views can only be
  updated or deleted by Systems Manager. This means that if you want to delete the managed views, or
  turn off Resource Explorer, you must disable the unified console. For more information about
  disabling the unified console, see [Disabling the Systems Manager unified
  console](systems-manager-disable-integrated-console.md "systems-manager-disable-integrated-console.md"). For more information
  about managed views, see [AWS Managed
  Views](../../../resource-explorer/latest/userguide/aws-managed-views.md "../../../resource-explorer/latest/userguide/aws-managed-views.md") in the _Resource Explorer User Guide_.

###### Note

If you've created an aggregator index for Resource Explorer in a Region different than your
home Region, Systems Manager demotes the current index. Then, Systems Manager promotes the local index in
your home Region as the new aggregator index. During this time, only nodes for your
home Region are displayed. This process can take up to 24 hours to complete.

IAM roles

- `RoleForOnboardingAutomation` – Allows Systems Manager to manage resources
  during the setting up process. For more information about the policy, see [AWSQuickSetupSSMManageResourcesExecutionPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSQuickSetupSSMManageResourcesExecutionPolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSQuickSetupSSMManageResourcesExecutionPolicy").
- `RoleForLifecycleManagement` – Allows Lambda to manage the
  lifecycle of resources created by the setting up process. For more information about the
  policy, see [AWSQuickSetupSSMLifecycleManagementExecutionPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSQuickSetupSSMLifecycleManagementExecutionPolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSQuickSetupSSMLifecycleManagementExecutionPolicy").
- `RoleForAutomation` – A service role for Systems Manager Automation to
  assume to execute runbooks. For more information, see [Create the service roles for Automation using
  the console](automation-setup-iam.md "automation-setup-iam.md").
- `AWSSSMDiagnosisAdminRole` – An adminsitrative role used to start
  automations that use diagnosis runbooks. For more information about the policies, see
  [AWS-SSM-DiagnosisAutomation-AdministrationRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-AdministrationRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-AdministrationRolePolicy"),
  [AWS-SSM-Automation-DiagnosisBucketPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-Automation-DiagnosisBucketPolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-Automation-DiagnosisBucketPolicy"), and [AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-OperationalAccountAdministrationRolePolicy").
- `AWSSSMDiagnosisExecutionRole` – An automation execution role for
  the diagnosis runbook. For more information about the policies, see [AWS-SSM-DiagnosisAutomation-ExecutionRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-ExecutionRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-DiagnosisAutomation-ExecutionRolePolicy") and
  [AWS-SSM-Automation-DiagnosisBucketPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-Automation-DiagnosisBucketPolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-Automation-DiagnosisBucketPolicy").
- `AWSSSMRemediationAdminRole` – An adminsitrative role used to
  start automations that use remediation runbooks. For more information about the
  policies, see [AWS-SSM-RemediationAutomation-AdministrationRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-AdministrationRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-AdministrationRolePolicy"),
  [AWS-SSM-Automation-DiagnosisBucketPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-Automation-DiagnosisBucketPolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-Automation-DiagnosisBucketPolicy"), and [AWS-SSM-RemediationAutomation-OperationalAccountAdministrationRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-OperationalAccountAdministrationRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-OperationalAccountAdministrationRolePolicy").
- `AWSSSMRemediationExecutionRole` – An automation execution role
  for the remediation runbook. For more information about the policies, see [AWS-SSM-RemediationAutomation-ExecutionRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-ExecutionRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-RemediationAutomation-ExecutionRolePolicy") and
  [AWS-SSM-Automation-DiagnosisBucketPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-Automation-DiagnosisBucketPolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-AWS-SSM-Automation-DiagnosisBucketPolicy").
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
to the Systems Manager endpoints, and more. For more information, see [Diagnosing and remediating](diagnose-and-remediate.md "diagnose-and-remediate.md").

## Set up the unified

console

###### To set up Systems Manager for an organization

1. Log in to the management account for your organization.
2. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
3. Enter the ID of the account you want to register as a delegated
   administrator.
4. After the delegated administrator account is successfully registered, log in to the
   delegated administrator account you just registered and return to the Systems Manager console to
   finish setting up Systems Manager.
5. Select **Enable Systems Manager**.
6. In the **Home Region** section, you determine a Region where you
   want Systems Manager to aggregate your node data. By default, Systems Manager selects the Region you're
   currently using. To choose a different home Region, change the console to the Region you
   want to use before you set up Systems Manager. Node data is replicated across accounts and Regions
   for your organization and stored in the home Region. The Region you choose can't be
   changed after Systems Manager is set up. To use a different Region as the home Region for your
   organization, you must disable the unified console and complete the setup process again.
   If your organization uses IAM Identity Center, you must select the same Region where you set up IAM Identity Center
   as your home Region.
7. In the **Regions** section, select the Regions where you want to
   enable Systems Manager.
8. In the **Feature configurations** section, choose the options that
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
SSM Agent, including information about how to manually install the agent, see [Working with SSM Agent](ssm-agent.md "ssm-agent.md"). 9. Choose **Submit**.

Depending on the size of your organization, it can take an extended amount of time to
set up the Systems Manager unified console experience.
