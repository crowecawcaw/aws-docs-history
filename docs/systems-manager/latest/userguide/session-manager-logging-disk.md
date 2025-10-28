# Configuring session logging to

disk

After you enable Session Manager logging to CloudWatch or Amazon S3, all commands executed during a
session (and the resulting output from those commands) are logged to a temporary
file on the disk of the target instance. The temporary file is named
`ipcTempFile.log`.

The `ipcTempFile.log` is controlled by the
`SessionLogsDestination` parameter in the SSM Agent configuration
file. This parameter accepts the following values:

- **disk**: If you specify this parameter and
  session logging to CloudWatch or Amazon S3 are _enabled_, SSM Agent
  creates the `ipcTempFile.log` temporary log file and logs
  session commands and output to disk. Session Manager uploads this log to either
  CloudWatch or S3 during or after the session, depending on the logging
  configuration. The log is then deleted according to the duration specified
  for the SSM Agent `SessionLogsRetentionDurationHours`
  configuration parameter.

If you specify this parameter and session logging to CloudWatch and Amazon S3 are
_disabled_, SSM Agent still logs command history and
output in the `ipcTempFile.log` file. The file will be
deleted according to the duration specified for the SSM Agent
`SessionLogsRetentionDurationHours` configuration
parameter.

- **none**: If you specify this parameter and
  session logging to CloudWatch or Amazon S3 are _enabled_, logging to
  disk works exactly as it does as if you'd specified the `disk`
  parameter. SSM Agent requires the temporary file when session logging to CloudWatch
  or Amazon S3 are enabled.

If you specify this parameter and session logging to CloudWatch or Amazon S3 are
_disabled_, SSM Agent doesn't create the
`ipcTempFile.log` file.
Use the following procedure to enable or disable creating the
`ipcTempFile.log` temporary log file to disk when a session
is stared.

###### To enable or disable creating the Session Manager temporary log file to disk

1.  Either install SSM Agent on your instance or upgrade to version 3.2.2086 or
    higher. For information about how to check the agent version number, see
    [Checking the SSM Agent version number](ssm-agent-get-version.md "ssm-agent-get-version.md"). For information about how to
    manually install the agent, locate the procedure for your operating system
    in the following sections:
    - [Manually installing and
      uninstalling SSM Agent on EC2 instances for Linux](manually-install-ssm-agent-linux.md "manually-install-ssm-agent-linux.md")
    - [Manually installing and
      uninstalling SSM Agent on EC2 instances for macOS](manually-install-ssm-agent-macos.md "manually-install-ssm-agent-macos.md")
    - [Manually installing and
      uninstalling SSM Agent on EC2 instances for Windows Server](manually-install-ssm-agent-windows.md "manually-install-ssm-agent-windows.md")

2.  Connect to your instance and locate the
    `amazon-ssm-agent.json` file in the following
    location.

        * **Linux**: /etc/amazon/ssm/
        * **macOS**: /opt/aws/ssm/
        * **Windows Server**: C:\Program
         Files\Amazon\SSM

    If the file `amazon-ssm-agent.json` doesn't exist, copy
    the contents of the `amazon-ssm-agent.json.template` to a
    new file in the same directory. Name the new file
    `amazon-ssm-agent.json`.

3.  Specify either `none` or `disk` for the
    `SessionLogsDestination` parameter. Save your changes.
4.  [Restart](ssm-agent-status-and-restart.md "ssm-agent-status-and-restart.md") SSM Agent.
    If you specified `disk` for the `SessionLogsDestination`
    parameter, you can verify that SSM Agent creates the temporary log file by starting a
    new session and then locating the `ipcTempFile.log` in the
    following location:

- **Linux**:
  /var/lib/amazon/ssm/`target
ID`/session/orchestration/`session
ID`/Standard_Stream/ipcTempFile.log
- **macOS**:
  /opt/aws/ssm/data/`target
ID`/session/orchestration/`session
ID`/Standard_Stream/ipcTempFile.log
- **Windows Server**:
  C:\ProgramData\Amazon\SSM\InstanceData\`target
  ID`\session\orchestration\`session
  ID`\Standard_Stream\ipcTempFile.log

###### Note

By default, the temporary log file is saved on the instance for 14
days.

If you want to update the `SessionLogsDestination` parameter across
multiple instances, we recommend you create an SSM Document that specifies the new
configuration. You can then use Systems Manager Run Command to implement the change on your
instances. For more information, see [Writing your own AWS Systems Manager documents (blog)](https://aws.amazon.com/blogs/mt/writing-your-own-aws-systems-manager-documents/ "https://aws.amazon.com/blogs/mt/writing-your-own-aws-systems-manager-documents/") and [Running commands on managed nodes](running-commands.md "running-commands.md").
