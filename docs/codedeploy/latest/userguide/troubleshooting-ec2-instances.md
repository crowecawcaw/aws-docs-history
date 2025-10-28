# Troubleshoot instance issues

###### Topics

- [Tags must be set correctly](#troubleshooting-EC2-tags "#troubleshooting-EC2-tags")
- [AWS CodeDeploy agent must be installed and running on
  instances](#troubleshooting-sds-agent "#troubleshooting-sds-agent")
- [Deployments do not fail for up to an hour
  when an instance is terminated during a deployment](#troubleshooting-one-hour-timeout "#troubleshooting-one-hour-timeout")
- [Analyzing log files to investigate
  deployment failures on instances](#troubleshooting-deploy-failures "#troubleshooting-deploy-failures")
- [Create a new CodeDeploy log file if it was
  accidentally deleted](#troubleshooting-create-new-log-file "#troubleshooting-create-new-log-file")
- [Troubleshooting
  “InvalidSignatureException – Signature expired: [time] is now earlier than [time]”
  deployment errors](#troubleshooting-instance-time-failures "#troubleshooting-instance-time-failures")

## Tags must be set correctly

Use the [list-deployment-instances](../../../cli/latest/reference/deploy/list-deployment-instances.md "../../../cli/latest/reference/deploy/list-deployment-instances.md") command to confirm the instances used
for a deployment are tagged correctly. If an EC2 instance is missing in the output,
use the EC2 console to confirm the tags have been set on the instance. For more
information, see [Working with
tags in the console](../../../AWSEC2/latest/UserGuide/Using_Tags.md#Using_Tags_Console "../../../AWSEC2/latest/UserGuide/Using_Tags.md#Using_Tags_Console") in the _Amazon EC2 User Guide_.

###### Note

If you tag an instance and immediately use CodeDeploy to deploy an application to it, the
instance might not be included in the deployment. This is because it can take several
minutes before CodeDeploy can read the tags. We recommend that you wait at least five minutes
between the time you tag an instance and attempt to deploy to it.

## AWS CodeDeploy agent must be installed and running on

instances

To verify the CodeDeploy agent is installed and running on an instance, see [Verify the CodeDeploy agent is running](codedeploy-agent-operations-verify.md "codedeploy-agent-operations-verify.md").

To install, uninstall, or reinstall the CodeDeploy agent, see [Install the CodeDeploy agent](codedeploy-agent-operations-install.md "codedeploy-agent-operations-install.md").

## Deployments do not fail for up to an hour

when an instance is terminated during a deployment

CodeDeploy provides a one-hour window for each deployment lifecycle event to run to
completion. This provides ample time for long-running scripts.

If the scripts don't run to completion while a lifecycle event is in progress (for
example, if an instance is terminated or the CodeDeploy agent is shut down), it might take up to
an hour for the status of the deployment to be displayed as Failed. This is true even if the
timeout period specified in the script is shorter than an hour. This is because when the
instance is terminated, the CodeDeploy agent shuts down and cannot process more scripts.

If an instance is terminated between lifecycle events or before the first lifecycle
event step starts, the timeout occurs after just five minutes.

## Analyzing log files to investigate

deployment failures on instances

If the status of an instance in the deployment is anything other than
`Succeeded`, you can review the deployment log file data to help identify the
problem. For information about accessing deployment log data, see [View log data for CodeDeploy EC2/On-Premises
deployments](deployments-view-logs.md "deployments-view-logs.md").

## Create a new CodeDeploy log file if it was

accidentally deleted

If you accidentally delete the deployment log file on an instance, CodeDeploy does not create
a replacement log file. To create a new log file, sign in to the instance, and then run
these commands:

**For an Amazon Linux, Ubuntu Server, or RHEL instance**, run these
commands in this order, one at a time:

```
systemctl stop codedeploy-agent
```

```
systemctl start codedeploy-agent
```

**For a Windows Server instance**:

```
powershell.exe -Command Restart-Service -Name codedeployagent
```

## Troubleshooting

“InvalidSignatureException – Signature expired: [time] is now earlier than [time]”
deployment errors

CodeDeploy requires accurate time references to perform its operations. If the date and time
on your instance are not set correctly, they might not match the signature date of your
deployment request, which CodeDeploy rejects.

To avoid deployment failures related to incorrect time settings, see the following
topics:

- [Setting the Time for Your Linux
  Instance](../../../AWSEC2/latest/UserGuide/set-time.md "../../../AWSEC2/latest/UserGuide/set-time.md")
- [Setting the Time for a Windows
  Instance](../../../AWSEC2/latest/WindowsGuide/windows-set-time.md "../../../AWSEC2/latest/WindowsGuide/windows-set-time.md")
