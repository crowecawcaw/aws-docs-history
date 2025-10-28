# Prerequisites for automated instance configuration in Accelerate

These conditions must be met to enable AMS Accelerate to perform the previously described automated actions on managed instances.

**The SSM Agent is installed**

AMS Accelerate automated instance configuration requires that the AWS Systems Manager SSM Agent is installed.

For information on using the AMS SSM Agent auto installation feature see [SSM Agent automatic installation](ssm-agent-auto-install.md "ssm-agent-auto-install.md").

For information on manually installing the SSM Agent, see the following:

- Linux: [Manually install SSM Agent on Amazon EC2 instances for Linux - AWS Systems Manager](../../../systems-manager/latest/userguide/sysman-manual-agent-install.md "../../../systems-manager/latest/userguide/sysman-manual-agent-install.md")
- Windows: [Manually install SSM Agent on Amazon EC2 instances for Windows Server - AWS Systems Manager](../../../systems-manager/latest/userguide/sysman-install-win.md "../../../systems-manager/latest/userguide/sysman-install-win.md")
  **The SSM Agent is in the managed state**

AMS Accelerate automated instance configuration requires an operational SSM Agent. The SSM Agent must be installed, and the Amazon EC2 instance must be in the managed state.
For more information, see the AWS documentation,
[Working with SSM Agent](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md").
