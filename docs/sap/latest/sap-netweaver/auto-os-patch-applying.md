# Applying patches

After you have created the patch baseline and tagged your Amazon EC2 instances to the patch group, you can apply patches. You can schedule patches or run them on-demand.

## Scheduled patching

SAP maintenance activities are usually scheduled in advance. The non-critical SAP systems can be patched in an ad-hoc manner, such as a sandbox system. The patching process should be documented in runbooks. After the system is successfully patched, the patching activities for the downstream SAP systems can be scheduled, either using maintenance windows or directly from Patch Manager.

For more information about patching schedules, see the following documentation:

- [About patching schedules using maintenance windows](../../../systems-manager/latest/userguide/sysman-patch-scheduletasks.md "../../../systems-manager/latest/userguide/sysman-patch-scheduletasks.md") in the _AWS Systems Manager User Guide_
- [Walkthrough: Creating a maintenance window for patching (console)](../../../systems-manager/latest/userguide/sysman-patch-mw-console.md "../../../systems-manager/latest/userguide/sysman-patch-mw-console.md") in the _AWS Systems Manager User Guide_

## On-demand patching

The **Patch now** option in Patch Manager allows you to run on-demand patching operations directly from the Systems Manager console. With this option, you do not need to create a schedule to update the compliance status of your managed nodes or to install patches on non-compliant nodes.

Scanning the Amazon EC2 instances allows you to identify systems that are potentially non-compliant, vulnerable, or un-patched. We recommend that you schedule system scans frequently, such as weekly.

For detailed instructions on how to run on-demand patching, see [Patching managed nodes on demand](../../../systems-manager/latest/userguide/patch-on-demand.md "../../../systems-manager/latest/userguide/patch-on-demand.md") in the _AWS Systems Manager User Guide_.

## Patch summary

After the patch baseline has run, you can view the patch status in Patch Manager. For details about the patch summary and how to access it in Patch Manager, see [Viewing patch Dashboard summaries (console)](../../../systems-manager/latest/userguide/view-patch-dashboard-summaries.md "../../../systems-manager/latest/userguide/view-patch-dashboard-summaries.md") in the _AWS Systems Manager User Guide_.

## Patch compliance reports

Patch compliance reports allow you to view the status of managed nodes. For more information about compliance reports, including detailed instructions on how to view them, see the following documentation:

- [Working with patch compliance reports](../../../systems-manager/latest/userguide/patch-compliance-reports.md "../../../systems-manager/latest/userguide/patch-compliance-reports.md") in the _AWS Systems Manager User Guide_
- [Viewing patch compliance results (console)](../../../systems-manager/latest/userguide/viewing-patch-compliance-results.md "../../../systems-manager/latest/userguide/viewing-patch-compliance-results.md") in the _AWS Systems Manager User Guide_
