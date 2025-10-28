# Archiving an Amazon GuardDuty finding

When you complete your investigation of an Amazon GuardDuty finding, you can archive the finding
from Amazon Detective. This saves you the trouble of having to return to GuardDuty to make the update.
Archiving a finding indicates that you have finished your investigation of it.

You can only archive a GuardDuty finding from within Detective if you are also the GuardDuty
administrator account for the account associated with the finding. If you are not a GuardDuty
administrator account and you attempt to archive a finding, GuardDuty displays an error.

###### To archive a GuardDuty finding

1. Sign in to the AWS Management Console. Then open the Detective console at
   [https://console.aws.amazon.com/detective/](https://console.aws.amazon.com/detective/ "https://console.aws.amazon.com/detective/").
2. In the Detective console, in the finding details panel, choose **Archive
   finding**.
3. When prompted to confirm, choose **Archive**.
   You can view archived GuardDuty findings in the GuardDuty console. The archived
   finding is stored in GuardDuty for 90-days and can be viewed at any time during that period. You can
   view suppressed findings in the GuardDuty console by selecting Archived from the findings table,
   or through the GuardDuty API using the [ListFindings API](../../../guardduty/latest/APIReference/API_ListFindings.md "../../../guardduty/latest/APIReference/API_ListFindings.md") with a findingCriteria criterion
   of service.archived equal to true. To learn more, see [Suppression Rules](../../../guardduty/latest/ug/findings_suppression-rule.md "../../../guardduty/latest/ug/findings_suppression-rule.md") in the
   _Amazon GuardDuty User Guide_.
