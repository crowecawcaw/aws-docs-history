# Viewing findings from a Security Hub CSPM

integration

When you start accepting findings from an AWS Security Hub CSPM integration, the
**Integrations** page of the Security Hub CSPM console displays the
**Status** of the integration as **Accepting
findings**. To review a list of findings from the integration, choose
**See findings**.

The findings list shows the active findings for the selected integration that have a
workflow status of `NEW` or `NOTIFIED`.

If you enable cross-Region aggregation, then in the aggregation Region, the list
includes findings from the aggregation Region and from linked Regions where the
integration is enabled. Security Hub does not automatically enable integrations based on
the cross-Region aggregation configuration.

In other Regions, the finding list for an integration only contains findings from the
current Region.

For information on how to configure cross-Region aggregation, see [Understanding cross-Region aggregation in Security Hub CSPM](finding-aggregation.md "finding-aggregation.md").

From the findings list, you can perform the following actions.

- [Change the filters and grouping
  for the list](securityhub-findings-manage.md "securityhub-findings-manage.md")
- [View details for individual
  findings](securityhub-findings-viewing.md#finding-view-details-console "securityhub-findings-viewing.md#finding-view-details-console")
- [Update the workflow status of
  findings](findings-workflow-status.md "findings-workflow-status.md")
- [Send findings to custom
  actions](findings-custom-action.md "findings-custom-action.md")
