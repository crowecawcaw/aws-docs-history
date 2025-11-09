# EUCPERF01-BP03 Consider disaster recovery (DR) requirements when architecting your AWS

EUC solution

Will a secondary Region support the latency that is acceptable to support the selected
AWS EUC service in a DR scenario, or can you accept degraded performance and relaxed
service level agreements to continue to do business?

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

For WorkSpaces, the use of cross-Region redirection or Multi-Region Resilience allows the
manual or partially automated process of using alternate regions to support your WorkSpaces
users in the event of a serious outage.

For WorkSpaces Applications, the master images created in one Region can be copied to a
secondary Region to enable the configuration of identical regional deployment for DR
purposes.

Review each of these DR features to be sure that they offer adequate performance and
capabilities depending on the Region that is selected for the purpose.

You should also replicate user data and other critical backend services in each
Region to provide localized access if similar levels of performance are expected in a DR
scenario.

For more detail on Cross-Region redirection and Multi-Region Resilience, see [Business continuity for WorkSpaces Personal](../../../workspaces/latest/adminguide/business-continuity.md "../../../workspaces/latest/adminguide/business-continuity.md").
