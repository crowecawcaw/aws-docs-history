# Running commands on managed nodes

This section includes information about how to send commands from the AWS Systems Manager
console to managed nodes. This section also includes information about how to cancel a
command.

Note that if your node is configured with the `noexec` mount option for the
var directory, Run Command is unable to successfuly run commands.

###### Important

When you send a command using Run Command, don't include sensitive information formatted
as plaintext, such as passwords, configuration data, or other secrets. All Systems Manager API
activity in your account is logged in an S3 bucket for AWS CloudTrail logs. This means that any
user with access to S3 bucket can view the plaintext values of those secrets. For this
reason, we recommend creating and using `SecureString` parameters to encrypt
sensitive data you use in your Systems Manager operations.

For more information, see [Restricting access to Parameter Store parameters
using IAM policies](sysman-paramstore-access.md "sysman-paramstore-access.md").

###### Execution history retention

The history of each command is available for up to 30 days. In addition, you can
store a copy of all log files in Amazon Simple Storage Service or have an audit trail of all API calls in
AWS CloudTrail.

###### Related information

For information about sending commands using other tools, see the following
topics:

- [Walkthrough: Use the AWS Tools for Windows PowerShell with
  Run Command](walkthrough-powershell.md "walkthrough-powershell.md") or the examples in the [AWS Systems Manager section of the AWS Tools for PowerShell Cmdlet Reference](../../../powershell/latest/reference/items/AWS_Systems_Manager_cmdlets.md "../../../powershell/latest/reference/items/AWS_Systems_Manager_cmdlets.md").
- [Walkthrough: Use the AWS CLI with Run Command](walkthrough-cli.md "walkthrough-cli.md") or the
  examples in the [SSM CLI Reference](../../../cli/latest/reference/ssm.md "../../../cli/latest/reference/ssm.md")

###### Contents

- [Running commands from the console](running-commands-console.md "running-commands-console.md")
- [Running commands using a specific document
  version](run-command-version.md "run-command-version.md")
- [Run commands at scale](send-commands-multiple.md "send-commands-multiple.md")
- [Canceling a command](cancel-run-command.md "cancel-run-command.md")
