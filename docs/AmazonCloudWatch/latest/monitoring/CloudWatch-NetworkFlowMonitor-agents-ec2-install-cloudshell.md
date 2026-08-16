# Install agents via CloudShell script

The Network Flow Monitor console provides a one-click installation option that uses to automatically
install and configure the Network Flow Monitor agent on your EC2 instances. This is the fastest way to get started
with Network Flow Monitor, because the script handles the entire setup process for you—including configuring
permissions, installing the agent, and activating it.

When you use this feature, you simply select the EC2 instances you want to monitor, and the console
opens with a script that completes the full installation automatically. You don't need to
manually configure IAM roles, run SSM commands, or download packages.

###### To install agents using the CloudShell script

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, under **Network Monitoring**,
   choose **Flow monitors**.
3. On the **Install agents** page, in the **Install via script** panel,
   select one or more EC2 instances from the instance list.

Only instances in a **running** state can be selected. Instances in other states
(such as stopped or terminated) are shown but cannot be selected. 4. Choose **Install via CloudShell**. 5. opens and runs the installation script automatically. The script output shows
the progress as it configures your instances.
After the script completes successfully, the agents begin collecting and sending performance metrics to the
Network Flow Monitor backend. You should begin seeing data on the **Workload insights** page within approximately
20 minutes.

###### Important

The installation script requires that the AWS Systems Manager agent is installed and running on your EC2 instances.
If your instances are in a private subnet, you must also have VPC endpoints configured for Systems Manager.
For more information, see [Working with Systems Manager Agent](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md") and
[Create VPC endpoints](../../../systems-manager/latest/userguide/setup-create-vpc.md "../../../systems-manager/latest/userguide/setup-create-vpc.md") in the
AWS Systems Manager User Guide.
