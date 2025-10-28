# Preventive controls

A preventive control ensures that your accounts maintain compliance, because it disallows
actions that lead to policy violations. The status of a preventive control is either
**enforced** or **not enabled**. Preventive controls
are supported in all AWS Regions.

- Preventive controls are implemented using service control policies (SCPs), or resource control policies (RCPs), each of which
  are part of AWS Organizations.
- Regarding nested OUs, preventive controls enabled on any OUs higher in the tree
  will apply to unregistered OUs in that tree.
- When you enable controls on an organizational unit (OU) that is registered with
  AWS Control Tower, preventive controls apply to all member accounts under the OU, enrolled
  and unenrolled.

###### Note

###### The AWS Control Tower mandatory controls have preventive behavior, except three that are detective. See [Mandatory controls](mandatory-controls.md "mandatory-controls.md").

- Detect Public Read Access Setting for Log Archive
- Detect Public Write Access Setting for Log Archive
- Detect whether shared accounts under the Security organizational unit have AWS CloudTrail or CloudTrail Lake enabled

###### Topics

- [Controls implemented with resource control policies
  (RCPs)](rcp-controls.md "rcp-controls.md")
- [Controls implemented with declarative policies](declarative-controls.md "declarative-controls.md")
- [Controls for AWS Backup](backup-controls.md "backup-controls.md")
- [Digital sovereignty
  controls](digital-sovereignty-controls.md "digital-sovereignty-controls.md")
