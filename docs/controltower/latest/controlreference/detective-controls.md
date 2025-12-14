# Detective controls

A detective control detects noncompliance of resources within your accounts, such as
policy violations, and provides alerts through the dashboard. The status of a detective
control is either **clear**, **in
violation**, or **not enabled**. Detective
controls apply only in those AWS Regions supported by AWS Control Tower.

- Detective controls are implemented using AWS Config rules. Most of the
  **Strongly recommended** controls, and many of the
  **Elective** controls, that are owned by AWS Control Tower are detective
  controls. The name of these controls typically begins with the word
  _Detect_, to denote a detective control.
- The integrated, detective Security Hub CSPM controls are implemented using AWS Config rules, similarly to
  all Security Hub CSPM controls. These controls are owned by the **Service-Managed
  Standard: AWS Control Tower**, which is part of Security Hub CSPM.
- Certain AWS Config controls are manageable directly from the AWS Control Tower console, implemented with AWS Config rules.
- When you enable controls on an organizational unit (OU) that is registered
  with AWS Control Tower, detective controls apply to enrolled accounts
  only, not to all member accounts in the OU, if some accounts are not enrolled in AWS Control Tower.

###### Note

For information about how detective controls are applied to nested OUs, in AWS Control Tower, see
[Nested Ous and controls](../userguide/nested-ous.md#nested-ous-and-controls "../userguide/nested-ous.md#nested-ous-and-controls").

## More about detective controls

Most of the AWS Control Tower **Strongly recommended** controls are detective. By
default, **Strongly recommended** controls are not enabled. For more information, see [Strongly recommended controls](strongly-recommended-controls.md "strongly-recommended-controls.md").

Three of the AWS Control Tower **Elective** controls are detective. By default,
**Elective** controls are not enabled. For more information, see [Elective controls](elective-controls.md "elective-controls.md").

###### Detective controls with Elective guidance

- Detect Whether MFA is Enabled for AWS IAM Users
- Detect Whether MFA is Enabled for AWS IAM Users of the AWS Console
- Detect Whether Versioning for Amazon S3 Buckets is Enabled

The integrated AWS Config controls in AWS Control Tower have **Elective** guidance. For more information, see [Integrated AWS Config controls available in AWS Control Tower](config-controls.md "config-controls.md").

###### Topics

- [The Security Hub CSPM standard](security-hub-controls.md "security-hub-controls.md")
- [Integrated AWS Config controls available in AWS Control Tower](config-controls.md "config-controls.md")
