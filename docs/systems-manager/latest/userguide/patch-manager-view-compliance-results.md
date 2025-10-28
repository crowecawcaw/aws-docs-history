# Viewing patch compliance

results

Use these procedures to view patch compliance information about your managed
nodes.

This procedure applies to patch operations that use the
`AWS-RunPatchBaseline` document. For information about viewing
patch compliance information for patch operations that use the
`AWS-RunPatchBaselineAssociation` document, see [Identifying
noncompliant managed nodes](patch-manager-find-noncompliant-nodes.md "patch-manager-find-noncompliant-nodes.md").

###### Note

The patch scanning operations for Quick Setup and Explorer use the
`AWS-RunPatchBaselineAssociation` document. Quick Setup and
Explorer are both tools in AWS Systems Manager.

###### Identify the patch solution for a specific CVE issue (Linux)

For many Linux-based operating systems, patch compliance results indicate
which Common Vulnerabilities and Exposure (CVE) bulletin issues are resolved
by which patches. This information can help you determine how urgently you
need to install a missing or failed patch.

CVE details are included for supported versions of the following operating
system types:

- AlmaLinux
- Amazon Linux 2
- Amazon Linux 2023
- Oracle Linux
- Red Hat Enterprise Linux (RHEL)
- Rocky Linux

###### Note

By default, CentOS Stream doesn't provide CVE information
about updates. You can, however, allow this support by using third-party
repositories such as the Extra Packages for Enterprise Linux (EPEL)
repository published by Fedora. For information, see [EPEL](https://fedoraproject.org/wiki/EPEL "https://fedoraproject.org/wiki/EPEL") on the Fedora
Wiki.

Currently, CVE ID values are reported only for patches with a status of
`Missing` or `Failed`.

You can also add CVE IDs to your lists of approved or rejected patches in your
patch baselines, as the situation and your patching goals warrant.

For information about working with approved and rejected patch lists, see the
following topics:

- [Working with custom patch
  baselines](patch-manager-manage-patch-baselines.md "patch-manager-manage-patch-baselines.md")
- [Package name
  formats for approved and rejected patch lists](patch-manager-approved-rejected-package-name-formats.md "patch-manager-approved-rejected-package-name-formats.md")
- [How patch baseline rules work on
  Linux-based systems](patch-manager-linux-rules.md "patch-manager-linux-rules.md")
- [How patches are installed](patch-manager-installing-patches.md "patch-manager-installing-patches.md")

###### Note

In some cases, Microsoft releases patches for applications that don't specify an
updated date and time. In these cases, an updated date and time of
`01/01/1970` is supplied by default.

## Viewing patching

compliance results

Use the following procedures to view patch compliance results in the
AWS Systems Manager console.

###### Note

For information about generating patch compliance reports that are
downloaded to an Amazon Simple Storage Service (Amazon S3) bucket, see [Generating .csv
patch compliance reports](patch-manager-store-compliance-results-in-s3.md "patch-manager-store-compliance-results-in-s3.md").

###### To view patch compliance results

1. Do one of the following.

**Option 1** (recommended) –
Navigate from Patch Manager, a tool in AWS Systems Manager:

    * In the navigation pane, choose **Patch Manager**.
    * Choose the **Compliance reporting**
     tab.
    * In the **Node patching details** area,
     choose the node ID of the managed node for which you want to
     review patch compliance results.
    * In the **Details** area, in the
     **Properties** list, choose
     **Patches**.

**Option 2** – Navigate from
Compliance, a tool in AWS Systems Manager:

    * In the navigation pane, choose **Compliance**.
    * For **Compliance resources summary**,
     choose a number in the column for the types of patch
     resources you want to review, such as
     **Non-Compliant resources**.
    * Below, in the **Resource** list, choose
     the ID of the managed node for which you want to review
     patch compliance results.
    * In the **Details** area, in the
     **Properties** list, choose
     **Patches**.

**Option 3** – Navigate from
Fleet Manager, a tool in AWS Systems Manager.

    * In the navigation pane, choose **Fleet Manager**.
    * In the **Managed instances** area, choose
     the ID of the managed node for which you want to review
     patch compliance results.
    * In the **Details** area, in the
     **Properties** list, choose
     **Patches**.

2. (Optional) In the Search box (
   ![The Search icon](images/search-icon.png)
   ), choose from the available filters.

For example, for Red Hat Enterprise Linux (RHEL), choose from the
following:

    * Name
    * Classification
    * State
    * Severity

For Windows Server, choose from the following:

    * KB
    * Classification
    * State
    * Severity

3. Choose one of the available values for the filter type you chose.
   For example, if you chose **State**, now choose a
   compliance state such as
   **InstalledPendingReboot**,
   **Failed** or
   **Missing**.

###### Note

Currently, CVE ID values are reported only for patches with a
status of `Missing` or `Failed`. 4. Depending on the compliance state of the managed node, you can
choose what action to take to remedy any noncompliant nodes.

For example, you can choose to patch your noncompliant managed
nodes immediately. For information about patching your managed nodes
on demand, see [Patching managed nodes on
demand](patch-manager-patch-now-on-demand.md "patch-manager-patch-now-on-demand.md").

For information about patch compliance states, see [Patch compliance state
values](patch-manager-compliance-states.md "patch-manager-compliance-states.md").
