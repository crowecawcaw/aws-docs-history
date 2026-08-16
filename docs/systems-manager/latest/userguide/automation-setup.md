# Setting up Automation

To set up Automation, you must verify user access to the
Automation service and situationally configure roles so that the service can perform
actions on your resources. We also recommend that you opt in to the adaptive concurrency
mode in your Automation preferences. Adaptive concurrency automatically scales your
automation quota to meet your needs. For more information, see [Allowing Automation to adapt to your concurrency needs](adaptive-concurrency.md "adaptive-concurrency.md").

To make sure you have proper access to AWS Systems Manager Automation, review the following user and service
role requirements.

## Verifying user access for runbooks

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
taken in a runbook to make sure your user, group, or role is assigned the necessary
permissions to perform the actions included in the runbook.

## Configuring a service role (assume role) access for automations

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
