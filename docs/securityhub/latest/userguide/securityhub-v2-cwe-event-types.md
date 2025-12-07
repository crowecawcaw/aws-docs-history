# EventBridge event types

Security Hub uses the following Amazon EventBridge event types to integrate with EventBridge.

On the EventBridge dashboard for Security Hub, **All Events** includes
all of these event types.

## Findings Imported V2

Security Hub automatically sends all new findings and all updates to existing findings
to EventBridge as **Findings Imported V2** events.
Each **Findings Imported V2** event contains a single finding.

Every finding that's imported and every finding updated through a [`BatchUpdateFindingsV2`](../../../index.md "../../../index.md") request triggers a **Findings Imported V2** event.

For administrator accounts, the event feed in EventBridge includes events for findings
from both their account and from their member accounts.

In an aggregation Region, the event feed includes events for findings from the
aggregation Region and the linked Regions. Cross-Region findings are included in the
event feed in near real time.

You can define rules in EventBridge that automatically route findings to
a remediation workflow, third-party tool, or [other supported EventBridge target](../../../eventbridge/latest/userguide/eb-targets.md "../../../eventbridge/latest/userguide/eb-targets.md"). The rules can include filters that
only apply the rule if the finding has specific attribute values.

You use this method to automatically send all findings, or all findings that have
specific characteristics, to a response or remediation workflow.

###### Note

Security Hub and Security Hub CSPM both send findings to EventBridge under the source of `aws.securityhub`.
Ensure that your EventBridge rules use the detail-type that is specific to Security Hub in order to avoid duplicate notifications related to Security Hub CSPM findings.
