# Troubleshooting license type conversion in

License Manager

###### Troubleshooting topics

- [Windows activation](#conversion-troubleshooting-kms "#conversion-troubleshooting-kms")
- [Instance [instance] is launched
  from an Amazon owned AMI. Provide an instance launched originally from a BYOL
  AMI.](#conversion-troubleshooting-aws-ami "#conversion-troubleshooting-aws-ami")
- [Failed to validate that
  instance [instance] was launched from a BYOL AMI. Ensure that the SSM Agent is
  running on your instance.](#conversion-troubleshooting-validate-byol "#conversion-troubleshooting-validate-byol")
- [An error occurred
  (InvalidParameterValueException) when calling the
  CreateLicenseConversionTaskForResource operation: ResourceId -
  [instance] is in an invalid state for changing license type.](#conversion-troubleshooting-invalid-state "#conversion-troubleshooting-invalid-state")
- [EC2 instance [instance]
  failed to stop. Ensure that you have permissions for EC2
  StopInstances.](#conversion-troubleshooting-failed-to-stop "#conversion-troubleshooting-failed-to-stop")

## Windows activation

A license type conversion contains multiple steps. In some cases, when you convert
Windows Server instances from BYOL to license included, the billing products on an
instance are successfully updated. However, the KMS server might not switch to the
AWS KMS server.

To remediate this issue, follow the steps in [Why did Windows
activation fail on my EC2 Windows instance?](https://aws.amazon.com/premiumsupport/knowledge-center/windows-activation-fails/ "https://aws.amazon.com/premiumsupport/knowledge-center/windows-activation-fails/") to activate Windows either
with the Systems Manager [AWSSupport-ActivateWindowsWithAmazonLicense](../../../systems-manager-automation-runbooks/latest/userguide/automation-awssupport-activatewindowswithamazonlicense.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-awssupport-activatewindowswithamazonlicense.md")
Automation runbook, or log in to the instance and manually make the switch to the
AWS KMS server.

## Instance [instance] is launched

from an Amazon owned AMI. Provide an instance launched originally from a BYOL
AMI.

You must launch your Amazon EC2 Windows instance from an AMI that you have imported to
perform a license type conversion to Bring Your Own License model (BYOL). Instances
originally launched from an Amazon-owned AMI aren't eligible for license type
conversion to BYOL. For more information, see [Conversion prerequisites for License Manager license
types](conversion-prerequisites.md "conversion-prerequisites.md").

## Failed to validate that

instance [instance] was launched from a BYOL AMI. Ensure that the SSM Agent is
running on your instance.

In order for the license type conversion to succeed, your instance must first have
been online and managed by Systems Manager to have its inventory collected. The
AWS Systems Manager Agent (SSM Agent) will gather inventory from your instance, which includes
details about the operating system. For more information, see [Checking SSM Agent status and starting the agent](../../../systems-manager/latest/userguide/ssm-agent-status-and-restart.md "../../../systems-manager/latest/userguide/ssm-agent-status-and-restart.md") and [Troubleshooting SSM Agent](../../../systems-manager/latest/userguide/troubleshooting-ssm-agent.md "../../../systems-manager/latest/userguide/troubleshooting-ssm-agent.md") in the _AWS Systems Manager User Guide_.

## An error occurred

(InvalidParameterValueException) when calling the
`CreateLicenseConversionTaskForResource` operation: ResourceId -
[instance] is in an invalid state for changing license type.

To perform a license type conversion, the target instance must be in the stopped
state. For more information, see [Conversion prerequisites for License Manager license
types](conversion-prerequisites.md "conversion-prerequisites.md") and [Troubleshoot
stopping your instance](../../../AWSEC2/latest/UserGuide/TroubleshootingInstancesStopping.md "../../../AWSEC2/latest/UserGuide/TroubleshootingInstancesStopping.md") in the _Amazon Elastic Compute Cloud User Guide_.

## EC2 instance [instance]

failed to stop. Ensure that you have permissions for EC2
`StopInstances.`

You must have permissions to perform the `StopInstances` EC2 API action
on the target instance. Also, If stop protection is enabled on the target instance,
the conversion process will fail. For more information, see [Disable stop protection for a running or stopped instance](../../../AWSEC2/latest/WindowsGuide/Stop_Start.md#disable-stop-protection-on-running-or-stopped-instance "../../../AWSEC2/latest/WindowsGuide/Stop_Start.md#disable-stop-protection-on-running-or-stopped-instance") in the
_Amazon Elastic Compute Cloud User Guide_.
