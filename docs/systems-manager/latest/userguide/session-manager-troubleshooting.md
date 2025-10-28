# Troubleshooting Session Manager

Use the following information to help you troubleshoot problems with AWS Systems Manager
Session Manager.

###### Topics

- [AccessDeniedException when calling the TerminateSession operation](#session-manager-troubleshooting-access-denied-exception "#session-manager-troubleshooting-access-denied-exception")
- [Document
  process failed unexpectedly: document worker timed out](#session-manager-troubleshooting-document-worker-timed-out "#session-manager-troubleshooting-document-worker-timed-out")
- [Session Manager can't connect
  from the Amazon EC2 console](#session-manager-troubleshooting-EC2-console "#session-manager-troubleshooting-EC2-console")
- [No permission to
  start a session](#session-manager-troubleshooting-start-permissions "#session-manager-troubleshooting-start-permissions")
- [SSM Agent not
  online](#session-manager-troubleshooting-agent-not-online "#session-manager-troubleshooting-agent-not-online")
- [No
  permission to change session preferences](#session-manager-troubleshooting-preferences-permissions "#session-manager-troubleshooting-preferences-permissions")
- [Managed node not
  available or not configured for Session Manager](#session-manager-troubleshooting-instances "#session-manager-troubleshooting-instances")
- [Session Manager plugin not found](#plugin-not-found "#plugin-not-found")
- [Session Manager plugin not automatically added to
  command line path (Windows)](#windows-plugin-env-var-not-set "#windows-plugin-env-var-not-set")
- [Session Manager plugin becomes unresponsive](#plugin-unresponsive "#plugin-unresponsive")
- [TargetNotConnected](#ssh-target-not-connected "#ssh-target-not-connected")
- [Blank screen
  displays after starting a session](#session-manager-troubleshooting-start-blank-screen "#session-manager-troubleshooting-start-blank-screen")
- [Managed node becomes
  unresponsive during long running sessions](#session-manager-troubleshooting-log-retention "#session-manager-troubleshooting-log-retention")
- [An error occurred
  (InvalidDocument) when calling the StartSession operation](#session-manager-troubleshooting-invalid-document "#session-manager-troubleshooting-invalid-document")

## AccessDeniedException when calling the TerminateSession operation

**Problem**: When attempting to terminate a session,
Systems Manager returns the following error:

```
An error occurred (AccessDeniedException) when calling the TerminateSession operation:
User: <user_arn> is not authorized to perform: ssm:TerminateSession on resource:
<ssm_session_arn> because no identity-based policy allows the ssm:TerminateSession action.
```

**Solution A: Confirm that the [latest
version of the Session Manager plugin](plugin-version-history.md "plugin-version-history.md") is installed on the node**

Enter the following command in the terminal and press Enter.

```
session-manager-plugin --version
```

**Solution B: Install or reinstall the latest version of the
plugin**

For more information, see [Install the Session Manager plugin
for the AWS CLI](session-manager-working-with-install-plugin.md "session-manager-working-with-install-plugin.md").

**Solution C: Attempt to reestablish a connection to the
node**

Verify that the node is responding to requests. Try reestablishing the session.
Or, if necessary, open the Amazon EC2 console and verify the status of the instance is
running.

## Document

process failed unexpectedly: document worker timed out

**Problem**: When starting a session to a Linux host,
Systems Manager returns the following error:

```
document process failed unexpectedly: document worker timed out,
check [ssm-document-worker]/[ssm-session-worker] log for crash reason
```

If you configured SSM Agent logging, as described in [Viewing SSM Agent logs](ssm-agent-logs.md "ssm-agent-logs.md"), you can view more details in the debugging
log. For this issue, Session Manager shows the following log entry:

```
failed to create channel: too many open files
```

This error typically indicates that there are too many Session Manager worker processes
running and the underlying operating system reached a limit. You have two options
for resolving this issue.

**Solution A: Increase the operating system file notification
limit**

You can increase the limit by running the following command from a separate Linux
host. This command uses Systems Manager Run Command. The specified value increases
`max_user_instances` to 8192. This value is considerably higher than
the default value of 128, but it won't strain host resources:

```
aws ssm send-command --document-name AWS-RunShellScript \
--instance-id `i-02573cafcfEXAMPLE`  --parameters \
"commands=sudo sysctl fs.inotify.max_user_instances=8192"
```

**Solution B: Decrease the file notifications used by Session Manager
in the target host**

Run the following command from a separate Linux host to list sessions running on
the target host:

```
aws ssm describe-sessions --state Active --filters key=Target,value=`i-02573cafcfEXAMPLE`
```

Review the command output to identify sessions that are no longer needed. You can
terminate those session by running the following command from a separate Linux
host:

```
aws ssm terminate-session —session-id `session ID`
```

Optionally, once there are no more sessions running on the remote server, you can
free additional resources by running the following command from a separate Linux
host. This command terminates all Session Manager processes running on the remote host, and
consequently all sessions to the remote host. Before you run this command, verify
there are no ongoing sessions you would like to keep:

```
aws ssm send-command --document-name AWS-RunShellScript \
            --instance-id `i-02573cafcfEXAMPLE` --parameters \
'{"commands":["sudo kill $(ps aux | grep ssm-session-worker | grep -v grep | awk '"'"'{print $2}'"'"')"]}'


```

## Session Manager can't connect

from the Amazon EC2 console

**Problem**: After creating a new instance, the
**Connect** button > **Session Manager** tab
in the Amazon Elastic Compute Cloud (Amazon EC2) console doesn't give you the option to connect.

**Solution A: Create an instance profile**: If you
haven't already done so (as instructed by the information on the **Session
Manager** tab in the EC2 console), create an AWS Identity and Access Management (IAM) instance
profile by using Quick Setup. Quick Setup is a tool in AWS Systems Manager.

Session Manager requires an IAM instance profile to connect to your instance. You can
create an instance profile and assign it to your instance by creating a [host
management configuration](quick-setup-host-management.md "quick-setup-host-management.md") with Quick Setup. A _host management
configuration_ creates an instance profile with the required
permissions and assigns it to your instance. A host management configuration also
enables other Systems Manager tools and creates IAM roles for running those tools. There is
no charge to use Quick Setup or the tools enabled by the host management configuration.
[Open Quick Setup and create a host management configuration](https://console.aws.amazon.com/systems-manager/quick-setup/create-configuration&configurationType=SSMHostMgmt "https://console.aws.amazon.com/systems-manager/quick-setup/create-configuration&configurationType=SSMHostMgmt").

###### Important

After you create the host management configuration, Amazon EC2 can take several
minutes to register the change and refresh the **Session
Manager** tab. If the tab doesn't show you a
**Connect** button after two minutes, reboot your instance.
After it reboots, if you still don't see the option to connect, open [Quick Setup](https://console.aws.amazon.com/systems-manager/quick-setup/create-configuration&configurationType=SSMHostMgmt "https://console.aws.amazon.com/systems-manager/quick-setup/create-configuration&configurationType=SSMHostMgmt") and verify you have only one host management
configuration. If there are two, delete the older configuration and wait a few
minutes.

If you still can't connect after creating a host management configuration, or if
you receive an error, including an error about SSM Agent, see one of the following
solutions:

- [Solution
  B: No error, but still can't connect](#session-manager-troubleshooting-EC2-console-no-error "#session-manager-troubleshooting-EC2-console-no-error")
- [Solution
  C: Error about missing SSM Agent](#session-manager-troubleshooting-EC2-console-no-agent "#session-manager-troubleshooting-EC2-console-no-agent")

### Solution

B: No error, but still can't connect

If you created the host management configuration, waited several minutes
before trying to connect, and still can't connect, then you might need to
manually apply the host management configuration to your instance. Use the
following procedure to update a Quick Setup host management configuration and apply
changes to an instance.

###### To update a host management configuration using Quick Setup

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Quick Setup**.
3. In the **Configurations** list, choose the
   **Host Management** configuration you
   created.
4. Choose **Actions**, and then choose **Edit
   configuration**.
5. Near the bottom of the **Targets** section, under
   **Choose how you want to target instances**, choose
   **Manual**.
6. In the **Instances** section, choose the instance you
   created.
7. Choose **Update**.

Wait a few minutes for EC2 to refresh the **Session Manager**
tab. If you still can't connect or if you receive an error, review the remaining
solutions for this issue.

### Solution

C: Error about missing SSM Agent

If you weren't able to create a host management configuration by using
Quick Setup, or if you received an error about SSM Agent not being installed, you
may need to manually install SSM Agent on your instance. SSM Agent is Amazon
software that enables Systems Manager to connect to your instance by using Session Manager.
SSM Agent is installed by default on most Amazon Machine Images (AMIs). If your
instance was created from a non-standard AMI or an older AMI, you might have to
manually install the agent. For the procedure to install SSM Agent, see the
following topic that corresponds to your instance operating system.

- [Windows Server](manually-install-ssm-agent-windows.md "manually-install-ssm-agent-windows.md")
- [macOS](manually-install-ssm-agent-macos.md "manually-install-ssm-agent-macos.md")
- [AlmaLinux](agent-install-alma.md "agent-install-alma.md")
- [Amazon Linux 2
  and AL2023](agent-install-al2.md "agent-install-al2.md")
- [Debian Server](agent-install-deb.md "agent-install-deb.md")
- [Oracle Linux](agent-install-oracle.md "agent-install-oracle.md")
- [Red Hat Enterprise Linux](agent-install-rhel.md "agent-install-rhel.md")
- [Rocky Linux](agent-install-rocky.md "agent-install-rocky.md")
- [Ubuntu Server](agent-install-ubuntu.md "agent-install-ubuntu.md")

For issues with SSM Agent, see [Troubleshooting SSM Agent](troubleshooting-ssm-agent.md "troubleshooting-ssm-agent.md").

## No permission to

start a session

**Problem**: You try to start a session, but the
system tells you that you don't have the necessary permissions.

- **Solution**: A system administrator hasn't
  granted you AWS Identity and Access Management (IAM) policy permissions for starting Session Manager
  sessions. For information, see [Control user session access to instances](session-manager-getting-started-restrict-access.md "session-manager-getting-started-restrict-access.md").

## SSM Agent not

online

**Problem**: You see a message on the Amazon EC2 instance
**Session Manager** tab that states: "SSM Agent is not online. The
SSM Agent was unable to connect to a Systems Manager endpoint to register itself with the
service."

**Solution**: SSM Agent is Amazon software that runs
on Amazon EC2 instances so that Session Manager can connect to them. If you see this error,
SSM Agent is unable to establish a connection with the Systems Manager endpoint. Possible
sources of the problem could be firewall restrictions, routing problems, or lack of
internet connectivity. To resolve this issue, investigate network connectivity
problems. For more information, see [Troubleshooting SSM Agent](troubleshooting-ssm-agent.md "troubleshooting-ssm-agent.md") and [Troubleshooting managed
node availability](fleet-manager-troubleshooting-managed-nodes.md "fleet-manager-troubleshooting-managed-nodes.md"). For information
about Systems Manager endpoints, see [AWS Systems Manager endpoints and quotas](../../../general/latest/gr/ssm.md "../../../general/latest/gr/ssm.md") in the
AWS General Reference.

## No

permission to change session preferences

**Problem**: You try to update global session
preferences for your organization, but the system tells you that you don't have the
necessary permissions.

- **Solution**: A system administrator hasn't
  granted you IAM policy permissions for setting Session Manager preferences. For
  information, see [Grant or deny a user
  permissions to update Session Manager preferences](preference-setting-permissions.md "preference-setting-permissions.md").

## Managed node not

available or not configured for Session Manager

**Problem 1**: You want to start a session on the
**Start a session** console page, but a managed node isn't in
the list.

- **Solution A**: The managed node you want to
  connect to might not have been configured for AWS Systems Manager. For more
  information, see [Setting up Systems Manager unified console
  for an organization](systems-manager-setting-up-organizations.md "systems-manager-setting-up-organizations.md").

###### Note

If AWS Systems Manager SSM Agent is already running on a managed node when you
attach the IAM instance profile, you might need to restart the agent
before the instance is listed on the **Start a
session** console page.

- **Solution B**: The proxy configuration you
  applied to the SSM Agent on your managed node might be incorrect. If the
  proxy configuration is incorrect, the managed node won't be able to reach
  the needed service endpoints, or the node might report as a different
  operating system to Systems Manager. For more information, see [Configuring SSM Agent to use a proxy on
  Linux nodes](configure-proxy-ssm-agent.md "configure-proxy-ssm-agent.md") and [Configure SSM Agent to use a
  proxy for Windows Server instances](configure-proxy-ssm-agent-windows.md "configure-proxy-ssm-agent-windows.md").

**Problem 2**: A managed node you want to connect is
in the list on the **Start a session** console page, but the page
reports that "The instance you selected isn't configured to use Session Manager."

- **Solution A**: The managed node has been
  configured for use with the Systems Manager service, but the IAM instance profile
  attached to the node might not include permissions for the Session Manager tool.
  For information, see [Verify or
  Create an IAM Instance Profile with Session Manager
  Permissions](session-manager-getting-started-instance-profile.md "session-manager-getting-started-instance-profile.md").
- **Solution B**: The managed node isn't
  running a version of SSM Agent that supports Session Manager. Update SSM Agent on the
  node to version 2.3.68.0 or later.

Update SSM Agent manually on a managed node by following the steps in [Manually installing and
uninstalling SSM Agent on EC2 instances for Windows Server](manually-install-ssm-agent-windows.md "manually-install-ssm-agent-windows.md"), [Manually installing and
uninstalling SSM Agent on EC2 instances for Linux](manually-install-ssm-agent-linux.md "manually-install-ssm-agent-linux.md"), or [Manually installing and
uninstalling SSM Agent on EC2 instances for macOS](manually-install-ssm-agent-macos.md "manually-install-ssm-agent-macos.md"), depending on the
operating system.

Alternatively, use the Run Command document `AWS-UpdateSSMAgent`
to update the agent version on one or more managed nodes at a time. For
information, see [Updating the SSM Agent using
Run Command](run-command-tutorial-update-software.md#rc-console-agentexample "run-command-tutorial-update-software.md#rc-console-agentexample").

###### Tip

To always keep your agent up to date, we recommend updating SSM Agent
to the latest version on an automated schedule that you define using
either of the following methods:

    + Run `AWS-UpdateSSMAgent` as part of a State Manager
     association. For information, see [Walkthrough: Automatically update
     SSM Agent with the AWS CLI](state-manager-update-ssm-agent-cli.md "state-manager-update-ssm-agent-cli.md").
    + Run `AWS-UpdateSSMAgent` as part of a maintenance
     window. For information about working with maintenance windows,
     see [Create and manage maintenance windows using
     the console](sysman-maintenance-working.md "sysman-maintenance-working.md") and [Tutorial: Create and
     configure a maintenance window using the AWS CLI](maintenance-windows-cli-tutorials-create.md "maintenance-windows-cli-tutorials-create.md").

- **Solution C**: The managed node can't reach
  the requisite service endpoints. You can improve the security posture of
  your managed nodes by using interface endpoints powered by AWS PrivateLink to
  connect to Systems Manager endpoints. The alternative to using interface endpoints is
  to allow outbound internet access on your managed nodes. For more
  information, see [Use PrivateLink to set up a VPC endpoint for Session Manager](session-manager-getting-started-privatelink.md "session-manager-getting-started-privatelink.md").
- **Solution D**: The managed node has limited
  available CPU or memory resources. Although your managed node might
  otherwise be functional, if the node doesn't have enough available
  resources, you can't establish a session. For more information, see [Troubleshooting an Unreachable Instance](../../../AWSEC2/latest/UserGuide/instance-console.md "../../../AWSEC2/latest/UserGuide/instance-console.md").

## Session Manager plugin not found

To use the AWS CLI to run session commands, the Session Manager plugin must also be installed on your
local machine. For information, see [Install the Session Manager plugin
for the AWS CLI](session-manager-working-with-install-plugin.md "session-manager-working-with-install-plugin.md").

## Session Manager plugin not automatically added to

command line path (Windows)

When you install the Session Manager plugin on Windows, the
`session-manager-plugin` executable should be automatically
added to your operating system's `PATH` environment variable. If
the command failed after you ran it to check whether the Session Manager plugin installed
correctly (`aws ssm start-session --target
 `instance-id``), you might need to set it
manually using the following procedure.

###### To modify your PATH variable (Windows)

1. Press the Windows key and enter `environment
variables`.
2. Choose **Edit environment variables for your
   account**.
3. Choose **PATH** and then choose
   **Edit**.
4. Add paths to the **Variable value** field, separated by
   semicolons, as shown in this example:
   `C:\existing\path`;`**C:\new\path**`

`C:\existing\path`
represents the value already in the field. `**C:\new\path**`
represents the path you want to add, as shown in the following
example.

    * **64-bit machines**:
     `C:\Program
     Files\Amazon\SessionManagerPlugin\bin\`

5. Choose **OK** twice to apply the new settings.
6. Close any running command prompts and re-open.

## Session Manager plugin becomes unresponsive

During a port forwarding session, traffic might stop forwarding if you have
antivirus software installed on your local machine. In some cases, antivirus
software interferes with the Session Manager plugin causing process deadlocks. To resolve this
issue, allow or exclude the Session Manager plugin from the antivirus software. For information
about the default installation path for the Session Manager plugin, see [Install the Session Manager plugin
for the AWS CLI](session-manager-working-with-install-plugin.md "session-manager-working-with-install-plugin.md").

## TargetNotConnected

**Problem**: You try to start a session, but the
system returns the error message, "An error occurred (TargetNotConnected) when
calling the StartSession operation: `InstanceID` isn't
connected."

- **Solution A**: This error is returned when
  the specified target managed node for the session isn't fully configured for
  use with Session Manager. For information, see [Setting up Session Manager](session-manager-getting-started.md "session-manager-getting-started.md").
- **Solution B**: This error is also returned
  if you attempt to start a session on a managed node that is located in a
  different AWS account or AWS Region.

## Blank screen

displays after starting a session

**Problem**: You start a session and Session Manager
displays a blank screen.

- **Solution A**: This issue can occur when the
  root volume on the managed node is full. Due to lack of disk space, SSM Agent
  on the node stops working. To resolve this issue, use Amazon CloudWatch to collect
  metrics and logs from the operating systems. For information, see [Collect metrics, logs, and traces with the CloudWatch agent](../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md "../../../AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.md") in the
  _Amazon CloudWatch User Guide_.
- **Solution B**: A blank screen might display
  if you accessed the console using a link that includes a mismatched endpoint
  and Region pair. For example, in the following console URL,
  `us-west-2` is the specified endpoint, but
  `us-west-1` is the specified AWS Region.

```
https://**us-west-2**.console.aws.amazon.com/systems-manager/session-manager/sessions?region=**us-west-1**
```

- **Solution C**: The managed node is
  connecting to Systems Manager using VPC endpoints, and your Session Manager preferences write
  session output to an Amazon S3 bucket or Amazon CloudWatch Logs log group, but an
  `s3` gateway endpoint or `logs` interface endpoint
  doesn't exist in the VPC. An `s3` endpoint in the format
  **`com.amazonaws.`region`.s3`**
  is required if your managed nodes are connecting to Systems Manager using VPC
  endpoints, and your Session Manager preferences write session output to an Amazon S3
  bucket. Alternatively, a `logs` endpoint in the format **`com.amazonaws.`region`.logs`**
  is required if your managed nodes are connecting to Systems Manager using VPC
  endpoints, and your Session Manager preferences write session output to a CloudWatch Logs log
  group. For more information, see [Creating VPC endpoints for Systems Manager](setup-create-vpc.md#create-vpc-endpoints "setup-create-vpc.md#create-vpc-endpoints").
- **Solution D**: The log group or Amazon S3 bucket
  you specified in your session preferences has been deleted. To resolve this
  issue, update your session preferences with a valid log group or S3
  bucket.
- **Solution E**: The log group or Amazon S3 bucket
  you specified in your session preferences isn't encrypted, but you have set
  the `cloudWatchEncryptionEnabled` or
  `s3EncryptionEnabled` input to `true`. To resolve
  this issue, update your session preferences with a log group or Amazon S3 bucket
  that is encrypted, or set the `cloudWatchEncryptionEnabled` or
  `s3EncryptionEnabled` input to `false`. This
  scenario is only applicable to customers who create session preferences
  using command line tools.

## Managed node becomes

unresponsive during long running sessions

**Problem**: Your managed node becomes unresponsive
or crashes during a long running session.

**Solution**: Decrease the SSM Agent log retention
duration for Session Manager.

###### To decrease the SSM Agent log retention duration for sessions

1. Locate the `amazon-ssm-agent.json.template` in the
   `/etc/amazon/ssm/` directory for
   Linux, or `C:\Program Files\Amazon\SSM`
   for Windows.
2. Copy the contents of the
   `amazon-ssm-agent.json.template` to a new file in the
   same directory named `amazon-ssm-agent.json`.
3. Decrease the default value of the
   `SessionLogsRetentionDurationHours` value in the
   `SSM` property, and save the file.
4. Restart the SSM Agent.

## An error occurred

(InvalidDocument) when calling the StartSession operation

**Problem**: You receive the following error when
starting a session by using the AWS CLI.

```
An error occurred (InvalidDocument) when calling the StartSession operation: Document type: 'Command' is not supported. Only type: 'Session' is supported for Session Manager.
```

**Solution**: The SSM document you specified for
the `--document-name` parameter isn't a _Session_
document. Use the following procedure to view a list of Session documents in the
AWS Management Console.

###### To view a list of Session documents

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Documents**.
3. In the **Categories** list, choose **Session
   documents**.
