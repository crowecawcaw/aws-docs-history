# Update the CodeDeploy agent on Windows Server

You can enable automatic updates of the CodeDeploy agent with AWS Systems Manager. With Systems Manager, you can
configure an update schedule for your Amazon EC2 or on-premises instances by creating an
association with Systems Manager State Manager. You can also manually update the CodeDeploy agent by
uninstalling the current version and installing a newer one.

###### Topics

- [Set up automatic CodeDeploy agent update with AWS Systems Manager](#codedeploy-agent-operations-update-windows-ssm "#codedeploy-agent-operations-update-windows-ssm")
- [Update the CodeDeploy agent manually](#codedeploy-agent-operations-update-windows-manual "#codedeploy-agent-operations-update-windows-manual")

## Set up automatic CodeDeploy agent update with AWS Systems Manager

To configure Systems Manager and enable automatic updates of the CodeDeploy agent, follow the
instructions in [Install the CodeDeploy agent using AWS Systems Manager](codedeploy-agent-operations-install-ssm.md "codedeploy-agent-operations-install-ssm.md").

## Update the CodeDeploy agent manually

To update the CodeDeploy agent manually, you can install the latest version from the CLI or
using Systems Manager. Follow the instructions in [Install the CodeDeploy
agent.](codedeploy-agent-operations-install.md "codedeploy-agent-operations-install.md") It is recommended that you uninstall older versions of the CodeDeploy agent by
following the instructions in [Uninstall the CodeDeploy
agent](codedeploy-agent-operations-uninstall.md "codedeploy-agent-operations-uninstall.md").
