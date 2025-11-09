AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Adjusting how long the

Session Manager temporary log file is stored on disk

After you enable Session Manager logging to CloudWatch or Amazon S3, all commands executed during a
session (and the resulting output from those commands) are logged to a temporary
file on the disk of the target instance. The temporary file is named
`ipcTempFile.log`. During a session, or after it is
completed, Session Manager uploads this temporary log to either CloudWatch or S3. The temporary
log is then deleted according to the duration specified for the SSM Agent
`SessionLogsRetentionDurationHours` configuration parameter. By
default, the temporary log file is saved on the instance for 14 days in the
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
  Use the following procedure to adjust how long the Session Manager temporary log file is
  stored on disk.

###### To adjust how long the `ipcTempFile.log` file is stored on

disk

1.  Connect to your instance and locate the
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

2.  Change the value of `SessionLogsRetentionDurationHours` to the
    desired number of hours. If `SessionLogsRetentionDurationHours`
    is set to 0, the temporary log file is created during the session and
    deleted when the session is completed. This setting should ensure the log
    file doesn't persist after the session ends.
3.  Save your changes.
4.  [Restart](ssm-agent-status-and-restart.md "ssm-agent-status-and-restart.md") SSM Agent.
