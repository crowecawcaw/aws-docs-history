# STIG compliance for your EC2 instance

Security Technical Implementation Guides (STIGs) are the configuration hardening standards
created by the Defense Information Systems Agency (DISA) to secure information systems
and software. To make your systems compliant with STIG standards, you must install,
configure, and test a variety of security settings.

STIGs are applied based on the following vulnerability classifications. When you create a
STIG hardened image or apply STIG settings to an existing instance, you can choose which
level to apply for hardening. Higher levels include STIG settings from all lower levels. For
example, the _High (Category I)_ level includes settings from both the Medium
and Low categories.

###### Compliance levels

- **High (Category I)**

The most severe risk. Includes any vulnerability that can result in loss of
confidentiality, availability, or integrity.

- **Medium (Category II)**

Includes any vulnerability that can result in loss of confidentiality, availability,
or integrity but the risk can be mitigated.

- **Low (Category III)**

Includes any vulnerability that degrades measures to protect against loss of
confidentiality, availability, or integrity.
Amazon EC2 provides the following methods to create STIG hardened instances:

- You can launch Windows instances that are pre-configured for STIG hardening
  from specialized public AWS Windows AMIs. For more information, see [STIG Hardened AWS
  Windows Server AMIs](../../../ec2/latest/windows-ami-reference/ami-windows-stig.md "../../../ec2/latest/windows-ami-reference/ami-windows-stig.md") in the _AWS Windows AMI reference_.
- You can create a customized AMI to launch pre-configured instances that are built
  with EC2 Image Builder STIG hardening components. For more information, see [STIG hardening components](../../../imagebuilder/latest/userguide/ib-stig.md "../../../imagebuilder/latest/userguide/ib-stig.md")
  in the _Image Builder User Guide_.
- You can use the AWSEC2-ConfigureSTIG Systems Manager command document to apply
  STIG settings to an existing EC2 instance. The Systems Manager STIG command document scans for
  misconfigurations and runs a remediation script to install and update the DoD certificates
  and to remove unnecessary certificates to maintain STIG compliance. There are no additional
  charges for using the STIG Systems Manager document.

###### Topics

- [STIG hardening settings for EC2 instances](ec2-stig-settings.md "ec2-stig-settings.md")
- [STIG hardening script downloads](ec2-stig-downloads.md "ec2-stig-downloads.md")
- [Use AWS Systems Manager to apply STIG settings to your instance](ec2-stig-ssm-cmd-doc.md "ec2-stig-ssm-cmd-doc.md")
