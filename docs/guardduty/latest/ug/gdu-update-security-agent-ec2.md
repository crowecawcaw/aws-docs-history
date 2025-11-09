# Updating the GuardDuty security agent for

Amazon EC2 instance manually

GuardDuty releases updates to the security agent versions. When you manage the security
agent manually, you're responsible to update the agent for your Amazon EC2 instances. For
information about new agent versions, see [GuardDuty security agent release
versions](runtime-monitoring-agent-release-history.md "runtime-monitoring-agent-release-history.md") for Amazon EC2 instances. To
receive notifications about a new agent version release, see [Subscribing to Amazon SNS GuardDuty announcements](guardduty_sns.md "guardduty_sns.md").

**To update the security agent for Amazon EC2 instance
manually**

The process to update the security agent is the same as installing the
security agent. Depending on the method that you used to install the agent,
you can perform the steps in [Installing the security
agent manually](installing-gdu-security-agent-ec2-manually.md "installing-gdu-security-agent-ec2-manually.md") for Amazon EC2
instances.

If you use [Method 1 - By using AWS Systems Manager](managing-gdu-agent-ec2-manually.md#manage-ssm-ec2-instance-runtime-monitoring "managing-gdu-agent-ec2-manually.md#manage-ssm-ec2-instance-runtime-monitoring"), then you can update the security
agent by using the **Run command**. Use the agent version
to which you want to update.

If you use [Method 2 - By using Linux Package Managers](managing-gdu-agent-ec2-manually.md#heading:r2l: "managing-gdu-agent-ec2-manually.md#heading:r2l:"), you can use the
scripts as specified in the [Installing the security
agent manually](installing-gdu-security-agent-ec2-manually.md "installing-gdu-security-agent-ec2-manually.md") section.
The scripts already include the latest agent release version. For
information about recently released agent versions, see [GuardDuty security agent versions for Amazon EC2
instances](runtime-monitoring-agent-release-history.md#ec2-gdu-agent-release-history "runtime-monitoring-agent-release-history.md#ec2-gdu-agent-release-history").

After you update the security agent, you can check the installation status by looking
at the logs. For more information, see [Validating GuardDuty
security agent installation status](installing-gdu-security-agent-ec2-manually.md#validate-ec2-gdu-agent-installation-healthy "installing-gdu-security-agent-ec2-manually.md#validate-ec2-gdu-agent-installation-healthy").
