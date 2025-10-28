# Prerequisites for automated instance configuration

For AMS Advanced customers who deploy instances with Change Management, the following
prerequisites must be met:

- The SSM Agent is installed, and in a managed state.
- The instance is tagged as a managed instance. (The `aws:cloudformation:stack-name` tag has a value
  starting with `stack-` or `sc-`.)
  If the SSM Agent is not already installed on your instance, you can install it using the AMS SSM Agent auto installation feature. For more information, see [SSM Agent automatic installation](ssm-agent-auto-install.md "ssm-agent-auto-install.md").

Or, you can install the SSM Agent manually. For more information, see the following:

- Linux: [Manually
  install SSM Agent on EC2 instances for Linux - AWS Systems Manager](../../../systems-manager/latest/userguide/sysman-manual-agent-install.md "../../../systems-manager/latest/userguide/sysman-manual-agent-install.md")
- Windows: [Manually install SSM
  Agent on EC2 instances for Windows Server - AWS Systems Manager](../../../systems-manager/latest/userguide/sysman-install-win.md "../../../systems-manager/latest/userguide/sysman-install-win.md")
  For more information on SSM agent, see the AWS documentation
  [Working with SSM Agent](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md").
