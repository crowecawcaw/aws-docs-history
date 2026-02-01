• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Setting up Automation

To set up Automation, a tool in AWS Systems Manager, you must verify user access to the
Automation service and situationally configure roles so that the service can perform
actions on your resources. We also recommend that you opt in to the adaptive concurrency
mode in your Automation preferences. Adaptive concurrency automatically scales your
automation quota to meet your needs. For more information, see [Allowing Automation to adapt to your
concurrency needs](adaptive-concurrency.md "adaptive-concurrency.md").

To ensure proper access to AWS Systems Manager Automation, review the following user and service
role requirements.

## Verifying user access for

runbooks

Verify that you have permission to use runbooks. If your user, group, or role is
assigned administrator permissions, then you have access to Systems Manager Automation. If you
don't have administrator permissions, then an administrator must give you permission
by assigning the `AmazonSSMFullAccess` managed policy, or a policy that
provides comparable permissions, to your user, group, or role.

###### Important

The IAM policy `AmazonSSMFullAccess` grants permissions to Systems Manager
actions. However, some runbooks require permissions to other services, such as
the runbook `AWS-ReleaseElasticIP`, which requires IAM permissions
for `ec2:ReleaseAddress`. Therefore, you must review the actions
taken in a runbook to ensure your user, group, or role is assigned the necessary
permissions to perform the actions included in the runbook.

## Configuring a service role (assume

role) access for automations

Automations can be initiated under the context of a service role (or
_assume role_). This allows the service to perform actions on
your behalf. If you don't specify an assume role, Automation uses the context of the
user who invoked the automation.

However, the following situations require that you specify a service role for
Automation:

- When you want to restrict a user's permissions on a resource, but you want
  the user to run an automation that requires elevated permissions. In this
  scenario, you can create a service role with elevated permissions and allow
  the user to run the automation.
- When you create a Systems Manager State Manager association that runs a runbook.
- When you have operations that you expect to run longer than 12
  hours.
- When you're running a runbook not owned by Amazon that uses the
  `aws:executeScript` action to call an AWS API operation or
  to act on an AWS resource. For information, see [Permissions for using runbooks](automation-document-script-considerations.md#script-permissions "automation-document-script-considerations.md#script-permissions").

If you need to create a service role for Automation, you can use one of the
following methods.

###### Topics

- [Create service roles for
  Automation by using CloudFormation](automation-setup-cloudformation.md "automation-setup-cloudformation.md")
- [Create the service roles for Automation using
  the console](automation-setup-iam.md "automation-setup-iam.md")
- [Setting up identity based policies examples](automation-setup-identity-based-policies.md "automation-setup-identity-based-policies.md")
- [Allowing Automation to adapt to your
  concurrency needs](adaptive-concurrency.md "adaptive-concurrency.md")
- [Configuring automatic retry for
  throttled operations](automation-throttling-retry.md "automation-throttling-retry.md")
- [Implement change controls
  for Automation](automation-change-calendar-integration.md "automation-change-calendar-integration.md")
