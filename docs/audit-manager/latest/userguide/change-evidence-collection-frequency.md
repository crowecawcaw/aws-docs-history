# Changing how often a control collects

evidence

AWS Audit Manager can collect evidence from various data sources. The frequency of evidence
collection depends on the type of data source that the control uses.

The following sections provide more information about the evidence collection frequency
for each control data source type, and how to change it (if applicable).

###### Topics

- [Key points](#change-evidence-collection-frequency-key-points "#change-evidence-collection-frequency-key-points")
- [Configuration snapshots from API calls](#change-evidence-collection-frequency-api-calls "#change-evidence-collection-frequency-api-calls")
- [Compliance checks from AWS Config](#change-evidence-collection-frequency-config "#change-evidence-collection-frequency-config")
- [Compliance checks from Security Hub](#change-evidence-collection-frequency-security-hub "#change-evidence-collection-frequency-security-hub")
- [User activity logs from AWS CloudTrail](#change-evidence-collection-frequency-cloudtrail "#change-evidence-collection-frequency-cloudtrail")

## Key points

- For **AWS API calls**, Audit Manager collects evidence using
  a describe API call to another AWS service. You can specify the evidence collection
  frequency directly in Audit Manager (for custom controls only).
- For **AWS Config**, Audit Manager reports the result of a
  compliance check directly from AWS Config. The frequency follows the triggers that are
  defined in the AWS Config rule.
- For **AWS Security Hub**, Audit Manager reports the result of a
  compliance check directly from Security Hub. The frequency follows the schedule of the Security Hub
  check.
- For **AWS CloudTrail**, Audit Manager collects evidence continuously
  from CloudTrail. You can’t change the frequency for this evidence type.

## Configuration snapshots

from AWS API calls

###### Note

The following applies only to custom controls. You can't change the evidence
collection frequency for a standard control.

If a custom control uses AWS API calls as a data source type, you can change the
evidence collection frequency in Audit Manager by following these steps.

###### To change the evidence collection frequency for a custom control with an API call

data source

1. Open the AWS Audit Manager console at [https://console.aws.amazon.com/auditmanager/home](https://console.aws.amazon.com/auditmanager/home "https://console.aws.amazon.com/auditmanager/home").
2. In the navigation pane, choose **Control library**, and then
   choose the **Custom** tab.
3. Choose the custom control that you want to edit, and then choose
   **Edit**.
4. On the **Edit control details** page, choose
   **Next**.
5. Under **Customer managed sources**, look for the API call data
   source that you want to update.
6. Select the data source from the table, then choose
   **Remove**.
7. Choose **Add**.
8. Choose **AWS API calls**.
9. Choose the same API call that you removed in step 5, and then select your
   preferred evidence collection frequency.
10. Under **Data source name**, provide a descriptive name.
11. (Optional) Under **Additional details**, enter a data source
    description and a troubleshooting description.
12. Choose **Next**.
13. On the **Edit an action plan** page, choose
    **Next**.
14. On the **Review and update** page, review the information for the
    custom control. To change the information for a step, choose
    **Edit**.
15. When you're finished, choose **Save changes**.

After you edit a control, the changes take effect at 00:00 UTC the following day in
all active assessments that include the control.

## Compliance checks from

AWS Config

###### Note

The following applies to both standard controls and custom controls that use
AWS Config Rules as a data source.

If a control uses AWS Config as a data source type, you can’t change the evidence collection
frequency directly in Audit Manager. This is because the frequency follows the triggers that are
defined in the AWS Config rule.

There are two types of triggers for AWS Config Rules:

1. **Configuration changes** - AWS Config runs evaluations for
   the rule when certain types of resources are created, changed, or deleted.
2. **Periodic** - AWS Config runs evaluations for the rule at
   a frequency that you choose (for example, every 24 hours).

To learn more about the triggers for AWS Config Rules, see [Trigger types](../../../config/latest/developerguide/evaluate-config-rules.md#aws-config-rules-trigger-types "../../../config/latest/developerguide/evaluate-config-rules.md#aws-config-rules-trigger-types") in the _AWS Config Developer Guide_.

For instructions on how to manage AWS Config Rules, see [Managing your AWS Config
rules](../../../config/latest/developerguide/evaluate-config_manage-rules.md "../../../config/latest/developerguide/evaluate-config_manage-rules.md").

## Compliance checks from

Security Hub

###### Note

The following applies to both standard controls and custom controls that use Security Hub
checks as a data source.

If a control uses Security Hub as a data source type, you can’t change the evidence
collection frequency directly in Audit Manager. This is because the frequency follows the schedule
of the Security Hub checks.

- **Periodic checks** run automatically within 12 hours
  after the most recent run. You cannot change the periodicity.
- **Change-triggered checks** run when the associated
  resource changes state. Even if the resource doesn't change state, the updated at time
  for change-triggered checks is refreshed every 18 hours. This helps to indicate that
  the control is still enabled. In general, Security Hub uses change-triggered rules whenever
  possible.

To learn more, see [Schedule for
running security checks](../../../securityhub/latest/userguide/securityhub-standards-schedule.md "../../../securityhub/latest/userguide/securityhub-standards-schedule.md") in the _AWS Security Hub User
Guide_.

## User activity logs from

AWS CloudTrail

###### Note

The following applies to both standard controls and custom controls that use
AWS CloudTrail user activity logs as a data source.

You can’t change the evidence collection frequency for controls that use activity logs
from CloudTrail as a data source type. Audit Manager collects this evidence type from CloudTrail in a
continuous manner. The frequency is continuous because user activity can happen at any
time of the day.
