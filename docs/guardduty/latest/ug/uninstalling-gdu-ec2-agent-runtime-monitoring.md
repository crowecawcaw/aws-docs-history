# Uninstalling security agent

manually for Amazon EC2 resources

This section provides methods to uninstall the GuardDuty security agent from your Amazon EC2
resources. When you manage the security agent manually, you're responsible to remove the agent
from the resources. GuardDuty will not take any action on the resources that you manage.

If you created an Amazon VPC endpoint manually, then after you uninstall the security agent on all the
monitored resource types in your account, you can choose to delete the VPC endpoint. This is a separate step. For
more information, see [To delete a VPC endpoint](clean-up-guardduty-agent-resources-process.md#runtime-monitoring-delete-vpc-endpoint "clean-up-guardduty-agent-resources-process.md#runtime-monitoring-delete-vpc-endpoint").

Based on how you installed the security agent in your resource, choose one of the following methods to uninstall
it.

###### Topics

- [Method 1 - By using the Run
  command](#remove-gdu-ec2-agent-run-command "#remove-gdu-ec2-agent-run-command")
- [Method 2 - By using Linux Package
  Managers](#remove-gdu-ec2-agent-rpm-script "#remove-gdu-ec2-agent-rpm-script")

## Method 1 - By using the Run

command

When you installed the security agent with [Method 1 - Using AWS Systems Manager](installing-gdu-security-agent-ec2-manually.md#install-gdu-by-using-sys-runtime-monitoring "installing-gdu-security-agent-ec2-manually.md#install-gdu-by-using-sys-runtime-monitoring"), perform the following steps to uninstall the
agent:

###### To uninstall the GuardDuty security agent

1. You can uninstall the GuardDuty security agent by following the steps as specified in
   [AWS Systems Manager Run Command](../../../systems-manager/latest/userguide/run-command.md "../../../systems-manager/latest/userguide/run-command.md") in the _AWS Systems Manager User Guide_. Use the
   Uninstall action in the parameters to uninstall the GuardDuty security agent.

In the **Targets** section, make sure that the impact is only on
those Amazon EC2 instances from which you want to uninstall the security agent.

Use the following GuardDuty document and distributor:

    * Document name:
     `AmazonGuardDuty-ConfigureRuntimeMonitoringSsmPlugin`
    * Distributor: `AmazonGuardDuty-RuntimeMonitoringSsmPlugin`

2. After providing all the details, when you choose **Run**, the
   security agent that it deployed on the targeted Amazon EC2 instances is removed.

To remove the Amazon VPC endpoint configuration, you must disable both Runtime Monitoring and Amazon EKS
Runtime Monitoring. 3. If you also want to delete the VPC endpoint that is associated with this security agent, then
see [To delete a VPC endpoint](clean-up-guardduty-agent-resources-process.md#runtime-monitoring-delete-vpc-endpoint "clean-up-guardduty-agent-resources-process.md#runtime-monitoring-delete-vpc-endpoint").

## Method 2 - By using Linux Package

Managers

When you installed the security agent with [Method 2 - Using Linux Package Managers](installing-gdu-security-agent-ec2-manually.md#install-gdu-by-rpm-scripts-runtime-monitoring "installing-gdu-security-agent-ec2-manually.md#install-gdu-by-rpm-scripts-runtime-monitoring"), perform the following steps
to uninstall the agent:

###### To uninstall the GuardDuty security agent

1. Connect to the your instance. For steps on how to do this, see [Connect to your Linux instance
   using an SSH client](../../../AWSEC2/latest/UserGuide/connect-linux-inst-ssh.md "../../../AWSEC2/latest/UserGuide/connect-linux-inst-ssh.md") in the _Amazon EC2 User Guide_.
2. ###### Command to uninstall

The following command will uninstall the GuardDuty security agent from the Amazon EC2
instance to which you connect:

    * For RPM:



    ```
    sudo rpm -e amazon-guardduty-agent
    ```
    * For Debian:



    ```
    sudo dpkg --purge amazon-guardduty-agent
    ```

After you run the command, you can also check the logs associated with the
command. 3. If you also want to delete the VPC endpoint that is associated with this security agent, then
see [To delete a VPC endpoint](clean-up-guardduty-agent-resources-process.md#runtime-monitoring-delete-vpc-endpoint "clean-up-guardduty-agent-resources-process.md#runtime-monitoring-delete-vpc-endpoint").
