# guardduty-non-archived-findings

Checks if Amazon GuardDuty has findings that are non-archived. The rule is NON_COMPLIANT if GuardDuty has non-archived low/medium/high severity findings older than the specified number in the daysLowSev/daysMediumSev/`daysHighSev` parameter.

**Identifier:** GUARDDUTY_NON_ARCHIVED_FINDINGS

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Asia Pacific (Thailand), AWS Secret - West, Mexico (Central), Asia Pacific (Taipei) Region

**Parameters:**

daysLowSev (Optional)
Type: int
Default: 30

The number of days Amazon GuardDuty low severity findings are allowed to stay non archived. The default is 30 days.

daysMediumSev (Optional)
Type: int
Default: 7

The number of days Amazon GuardDuty medium severity findings are allowed to stay non archived. The default is 7 days.

daysHighSev (Optional)
Type: int
Default: 1

The number of days Amazon GuardDuty high severity findings are allowed to stay non archived. The default is 1 day.

## AWS CloudFormation template

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed
Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md "aws-config-managed-rules-cloudformation-templates.md").
