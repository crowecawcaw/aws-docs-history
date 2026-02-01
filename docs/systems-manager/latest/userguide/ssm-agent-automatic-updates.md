• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Automating updates to SSM Agent

AWS releases a new version of AWS Systems Manager Agent (SSM Agent) when we add or update Systems Manager
tools. If your managed nodes use an older version of the agent, then you can't use the
new tools or benefit from the updated tools. For these reasons, we recommend that you
automate the process of updating SSM Agent on your managed nodes using any of the
following methods.

###### Agent updates on the Bottlerocket operating system

SSM Agent on the Bottlerocket operating system can't be updated using the Systems Manager
Command document `AWS-UpdateSSMAgent`. Updates are managed within
the Bottlerocket control container. For more information, see [Bottlerocket Control Container](https://github.com/bottlerocket-os/bottlerocket-control-container/blob/develop/README.md "https://github.com/bottlerocket-os/bottlerocket-control-container/blob/develop/README.md") and [Bottlerocket update operator](https://github.com/bottlerocket-os/bottlerocket-update-operator/blob/develop/README.md "https://github.com/bottlerocket-os/bottlerocket-update-operator/blob/develop/README.md") on GitHub.

###### macOS version requirement

If an instance is running macOS version 11.0 (Big Sur) or later, the instance
must have the SSM Agent version 3.1.941.0 or higher to run the
AWS-UpdateSSMAgent document. If the instance is running a version
of SSM Agent released before 3.1.941.0, update your SSM Agent to run the
AWS-UpdateSSMAgent by running `brew update` and
`brew upgrade amazon-ssm-agent` commands.

| Method                                                           | Details                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| One-click automated update on all managed nodes<br>(Recommended) | You can configure all managed nodes in your AWS account to<br>automatically check for and download new versions of SSM Agent. To do<br>this, choose **Auto update SSM Agent\*<br>• on the<br>**Settings\*<br>• tab in Fleet Manager, as described<br>later in this topic.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Global or selective update                                       | You can use State Manager, a tool in AWS Systems Manager, to create an<br>association that automatically downloads and installs SSM Agent on<br>your managed nodes. If you want to limit the disruption to your<br>workloads, you can create a Systems Manager maintenance window to perform the<br>installation during designated time periods. Both methods allow you<br>to create either a global update configuration for all of your<br>managed nodes or selectively choose which instances get updated. For<br>information about creating a State Manager association, see [Walkthrough: Automatically update<br>SSM Agent with the AWS CLI](state-manager-update-ssm-agent-cli.md "state-manager-update-ssm-agent-cli.md"). For<br>information about creating a maintenance window, see [Tutorial: Create a<br>maintenance window for patching using the console](maintenance-window-tutorial-patching.md "maintenance-window-tutorial-patching.md"). |
| Global or selective update for new environments                  | If you're getting started with Systems Manager, we recommend that you use<br>the **Update Systems Manager (SSM) Agent every two weeks**<br>option in Quick Setup, a tool in AWS Systems Manager. Quick Setup allows you to<br>create either a global update configuration for all of your managed<br>nodes or selectively choose which managed nodes get updated. For<br>more information, see [Set up Amazon EC2 host management using<br>Quick Setup](quick-setup-host-management.md "quick-setup-host-management.md").                                                                                                                                                                                                                                                                                                                                                                                                                                    |

If you prefer to update SSM Agent on your managed nodes manually, you can subscribe to
notifications that AWS publishes when a new version of the agent is released. For
information, see [Subscribing to SSM Agent
notifications](ssm-agent-subscribe-notifications.md "ssm-agent-subscribe-notifications.md"). After you subscribe to
notifications, you can use Run Command to manually update one or more managed nodes with
the latest version. For more information, see [Updating the SSM Agent using
Run Command](run-command-tutorial-update-software.md#rc-console-agentexample "run-command-tutorial-update-software.md#rc-console-agentexample").

## Automatically updating

SSM Agent

You can configure Systems Manager to automatically update SSM Agent on all Linux-based and
Windows-based managed nodes in your AWS account. If you turn on this
option, then Systems Manager automatically checks every two weeks for a new version of the
agent. If there is a new version, then Systems Manager automatically updates the agent to the
latest released version using the SSM document `AWS-UpdateSSMAgent`. We
encourage you to choose this option to ensure that your managed nodes are always
running the most up-to-date version of SSM Agent.

###### Note

If you use a `yum` command to update SSM Agent on a managed node after the agent
has been installed or updated using the SSM document `AWS-UpdateSSMAgent`, you
might see the following message: `"Warning: RPMDB altered outside of yum."` This
message is expected and can be safely ignored.

###### To automatically update SSM Agent

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Fleet Manager**.
3. Choose the **Settings** tab.
4. In the **Agent auto update** area, choose **Auto
   update SSM Agent**.

To change the version of SSM Agent your fleet updates to, choose **Edit** under **Agent auto
update** on the **Settings** tab. Then
enter the version number of SSM Agent you want to update to in **Version** under **Parameters**. If not
specified, the agent updates to the latest version.

To stop automatically deploying updated versions of SSM Agent to all managed nodes
in your account, choose **Delete** under **Agent auto
update** on the **Settings** tab. This action deletes
the State Manager association that automatically updates SSM Agent on your managed
nodes.
