AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Using scripts in

runbooks

Automation runbooks support running scripts as part of the automation. Automation
is a tool in AWS Systems Manager. By using runbooks, you can run scripts directly in AWS
without creating a separate compute environment to run your scripts. Because
runbooks can run script steps along with other automation step types, such as
approvals, you can manually intervene in critical or ambiguous situations. You can
send the output from `aws:executeScript` actions in your runbooks to
Amazon CloudWatch Logs. For more information, see [Logging Automation action output with
CloudWatch Logs](automation-action-logging.md "automation-action-logging.md").

## Permissions for using runbooks

To use a runbook, Systems Manager must use the permissions of an AWS Identity and Access Management (IAM) role.
The method that Automation uses to determine which role's permissions to use
depends on a few factors, and whether a step uses the
`aws:executeScript` action.

For runbooks that don't use `aws:executeScript`, Automation uses
one of two sources of permissions:

- The permissions of an IAM service role, or Assume role, that is
  specified in the runbook or passed in as a parameter.
- If no IAM service role is specified, the permissions of the user who
  started the automation.

When a step in a runbook includes the `aws:executeScript` action,
however, an IAM service role (Assume role) is always required if the Python or
PowerShell script specified for the action is calling any AWS API operations.
Automation checks for this role in the following order:

- The permissions of an IAM service role, or Assume role, that is
  specified in the runbook or passed in as a parameter.
- If no role is found, Automation attempts to run the Python or
  PowerShell script specified for `aws:executeScript` without
  any permissions. If the script is calling an AWS API operation (for
  example the Amazon EC2 `CreateImage` operation), or attempting to
  act on an AWS resource (such as an EC2 instance), the step containing
  the script fails, and Systems Manager returns an error message reporting the
  failure.

## Adding scripts to runbooks

You can add scripts to your runbooks by including the script inline as part of
a step in the runbook. You can also attach scripts to the runbook by uploading
the scripts from your local machine or by specifying an Amazon Simple Storage Service (Amazon S3) bucket
where the scripts are located. After a step that runs a script is complete, the
output of the script is available as a JSON object, which you can then use as
input for subsequent steps in your runbook. For more information about the
`aws:executeScript` action and how to use attachments for
scripts, see [aws:executeScript
– Run a script](automation-action-executeScript.md "automation-action-executeScript.md").

## Script constraints for runbooks

Runbooks enforce a limit of five file attachments. Scripts can either be in
the form of a Python script (.py), a PowerShell Core script (.ps1), or attached
as contents within a .zip file.
