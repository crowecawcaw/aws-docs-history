# Creating

a custom patch baseline for Windows Server

Use the following procedure to create a custom patch baseline for Windows
managed nodes in Patch Manager, a tool in AWS Systems Manager.

For information about creating a patch baseline for Linux managed nodes,
see [Creating a
custom patch baseline for Linux](patch-manager-create-a-patch-baseline-for-linux.md "patch-manager-create-a-patch-baseline-for-linux.md"). Fo
information about creating a patch baseline for macOS managed nodes, see
[Creating a
custom patch baseline for macOS](patch-manager-create-a-patch-baseline-for-macos.md "patch-manager-create-a-patch-baseline-for-macos.md").

For an example of creating a patch baseline that is limited to installing
Windows Service Packs only, see [Tutorial: Create a patch baseline for installing Windows Service Packs using
the console](patch-manager-windows-service-pack-patch-baseline-tutorial.md "patch-manager-windows-service-pack-patch-baseline-tutorial.md").

###### To create a custom patch baseline (Windows)

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Patch Manager**.
3. Choose the **Patch baselines** tab, and then
   choose **Create patch baseline**.

-or-

If you are accessing Patch Manager for the first time in the current
AWS Region, choose **Start with an overview**,
choose the **Patch baselines** tab, and then choose
**Create patch baseline**. 4. For **Name**, enter a name for your new patch
baseline, for example, `MyWindowsPatchBaseline`. 5. (Optional) For **Description**, enter a
description for this patch baseline. 6. For **Operating system**, choose
`Windows`. 7. For **Available security updates compliance
status**, choose the status you want to assign to
security patches that are available but not approved because they
don't meet the installation criteria specified in the patch
baseline, **Non-Compliant** or
**Compliant**.

Example scenario: Security patches that you might want installed
can be skipped if you have specified a long period to wait after a
patch is released before installation. If an update to the patch is
released during your specified waiting period, the waiting period
for installing the patch starts over. If the waiting period is too
long, multiple versions of the patch could be released but never
installed. 8. If you want to begin using this patch baseline as the default for
Windows as soon as you create it, select **Set this patch
baseline as the default patch baseline for Windows Server
instances** .

###### Note

This option is available only if you first accessed Patch Manager
before the [patch
policies](patch-manager-policies.md "patch-manager-policies.md") release on December 22, 2022.

For information about setting an existing patch baseline as
the default, see [Setting an existing patch
baseline as the default](patch-manager-default-patch-baseline.md "patch-manager-default-patch-baseline.md"). 9. In the **Approval rules for operating systems**
section, use the fields to create one or more auto-approval
rules.

    * **Products**: The version of the
     operating systems the approval rule applies to, such as
     `WindowsServer2012`. The default selection is
     `All`.
    * **Classification**: The type of patches
     the approval rule applies to, such as
     `CriticalUpdates`, `Drivers`, and
     `Tools`. The default selection is
     `All`.


    ###### Tip

    You can include Windows Service Pack installations in
     your approval rules by including
     `ServicePacks` or by choosing
     `All` in your
     **Classification** list. For an
     example, see [Tutorial: Create a patch baseline for installing Windows Service Packs using
     the console](patch-manager-windows-service-pack-patch-baseline-tutorial.md "patch-manager-windows-service-pack-patch-baseline-tutorial.md").
    * **Severity**: The severity value of
     patches the rule is to apply to, such as
     `Critical`. The default selection is
     `All`.
    * **Auto-approval**: The method for
     selecting patches for automatic approval.




    	+ **Approve patches after a specified number
    	 of days**: The number of days for
    	 Patch Manager to wait after a patch is released or
    	 updated before a patch is automatically approved.
    	 You can enter any integer from zero (0) to 360. For
    	 most scenarios, we recommend waiting no more than
    	 100 days.
    	+ **Approve patches released up to a
    	 specific date**: The patch release date
    	 for which Patch Manager automatically applies all patches
    	 released or updated on or before that date. For
    	 example, if you specify July 7, 2023, no patches
    	 released or last updated on or after July 8, 2023,
    	 are installed automatically.
    * (Optional) **Compliance reporting**: The
     severity level you want to assign to patches approved by the
     baseline, such as `High`.


    ###### Note

    If you specify a compliance reporting level and the
     patch state of any approved patch is reported as
     `Missing`, then the patch baseline's
     overall reported compliance severity is the severity
     level you specified.

10. (Optional) In the **Approval rules for
    applications** section, use the fields to create one or
    more auto-approval rules.

###### Note

Instead of specifying approval rules, you can specify lists of
approved and rejected patches as patch exceptions. See steps 10
and 11.

    * **Product family**: The general Microsoft
     product family for which you want to specify a rule, such as
     `Office` or `Exchange
     Server`.
    * **Products**: The version of the
     application the approval rule applies to, such as
     `Office 2016` or `Active Directory
     Rights Management Services Client 2.0 2016`. The
     default selection is `All`.
    * **Classification**: The type of patches
     the approval rule applies to, such as
     `CriticalUpdates`. The default selection is
     `All`.
    * **Severity**: The severity value of
     patches the rule applies to, such as `Critical`.
     The default selection is `All`.
    * **Auto-approval**: The method for
     selecting patches for automatic approval.




    	+ **Approve patches after a specified number
    	 of days**: The number of days for
    	 Patch Manager to wait after a patch is released or
    	 updated before a patch is automatically approved.
    	 You can enter any integer from zero (0) to 360. For
    	 most scenarios, we recommend waiting no more than
    	 100 days.
    	+ **Approve patches released up to a
    	 specific date**: The patch release date
    	 for which Patch Manager automatically applies all patches
    	 released or updated on or before that date. For
    	 example, if you specify July 7, 2023, no patches
    	 released or last updated on or after July 8, 2023,
    	 are installed automatically.
    * (Optional) **Compliance reporting**: The
     severity level you want to assign to patches approved by the
     baseline, such as `Critical` or
     `High`.


    ###### Note

    If you specify a compliance reporting level and the
     patch state of any approved patch is reported as
     `Missing`, then the patch baseline's
     overall reported compliance severity is the severity
     level you specified.

11. (Optional) If you want to explicitly approve any patches instead
    of letting patches be selected according to approval rules, do the
    following in the **Patch exceptions**
    section:
    - For **Approved patches**, enter a
      comma-separated list of the patches you want to
      approve.

    For information about accepted formats for lists of approved patches and rejected patches,
    see [Package name
    formats for approved and rejected patch lists](patch-manager-approved-rejected-package-name-formats.md "patch-manager-approved-rejected-package-name-formats.md").
    - (Optional) For **Approved patches compliance
      level**, assign a compliance level to the
      patches in the list.

12. If you want to explicitly reject any patches that otherwise meet
    your approval rules, do the following in the **Patch
    exceptions** section:
    - For **Rejected patches**, enter a
      comma-separated list of the patches you want to
      reject.

    For information about accepted formats for lists of approved patches and rejected patches,
    see [Package name
    formats for approved and rejected patch lists](patch-manager-approved-rejected-package-name-formats.md "patch-manager-approved-rejected-package-name-formats.md").
    - For **Rejected patches action**, select
      the action for Patch Manager to take on patches included in the
      **Rejected patches** list.

          + **Allow as
           dependency**: Windows Server doesn't support
           the concept of package dependencies. If a package in
           the **Rejected patches** list and
           already installed on the node, its status is
           reported as `INSTALLED_OTHER`. Any
           package not already installed on the node is
           skipped.
          + **Block**: Packages
           in the **Rejected patches** list
           aren't installed by Patch Manager under any
           circumstances. If a package was installed before it
           was added to the **Rejected
           patches** list, or is installed outside
           of Patch Manager afterward, it's considered noncompliant
           with the patch baseline and its status is reported
           as `INSTALLED_REJECTED`.

      For more information about rejected package actions, see
      [Rejected patch
      list options in custom patch baselines](patch-manager-windows-and-linux-differences.md#rejected-patches-diff "patch-manager-windows-and-linux-differences.md#rejected-patches-diff").

13. (Optional) For **Manage tags**, apply one or more
    tag key name/value pairs to the patch baseline.

Tags are optional metadata that you assign to a resource. Tags
allow you to categorize a resource in different ways, such as by
purpose, owner, or environment. For example, you might want to tag a
patch baseline to identify the severity level of patches it
specifies, the operating system family it applies to, and the
environment type. In this case, you could specify tags similar to
the following key name/value pairs:

    * `Key=PatchSeverity,Value=Critical`
    * `Key=OS,Value=RHEL`
    * `Key=Environment,Value=Production`

14. Choose **Create patch baseline**.
