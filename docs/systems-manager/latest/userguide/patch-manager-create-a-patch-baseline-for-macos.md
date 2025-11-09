AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Creating a

custom patch baseline for macOS

Use the following procedure to create a custom patch baseline for macOS
managed nodes in Patch Manager, a tool in AWS Systems Manager.

For information about creating a patch baseline for Windows Server managed
nodes, see [Creating
a custom patch baseline for Windows Server](patch-manager-create-a-patch-baseline-for-windows.md "patch-manager-create-a-patch-baseline-for-windows.md"). For
information about creating a patch baseline for Linux managed nodes, see
[Creating a
custom patch baseline for Linux](patch-manager-create-a-patch-baseline-for-linux.md "patch-manager-create-a-patch-baseline-for-linux.md").

###### Note

macOS is not supported in all AWS Regions. For more information
about Amazon EC2 support for macOS, see [Amazon EC2 Mac
instances](../../../AWSEC2/latest/UserGuide/ec2-mac-instances.md "../../../AWSEC2/latest/UserGuide/ec2-mac-instances.md") in the
_Amazon EC2 User Guide_.

###### To create a custom patch baseline for macOS managed nodes

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Patch Manager**.
3. Choose the **Patch baselines** tab, and then
   choose **Create patch baseline**.

-or-

If you are accessing Patch Manager for the first time in the current
AWS Region, choose **Start with an overview**,
choose the **Patch baselines** tab, and then choose
**Create patch baseline**. 4. For **Name**, enter a name for your new patch
baseline, for example, `MymacOSPatchBaseline`. 5. (Optional) For **Description**, enter a
description for this patch baseline. 6. For **Operating system**, choose macOS. 7. If you want to begin using this patch baseline as the default for
macOS as soon as you create it, check the box next to
**Set this patch baseline as the default patch baseline
for macOS instances**.

###### Note

This option is available only if you first accessed Patch Manager
before the [patch
policies](patch-manager-policies.md "patch-manager-policies.md") release on December 22, 2022.

For information about setting an existing patch baseline as
the default, see [Setting an existing patch
baseline as the default](patch-manager-default-patch-baseline.md "patch-manager-default-patch-baseline.md"). 8. In the **Approval rules for operating-systems**
section, use the fields to create one or more auto-approval
rules.

    * **Products**: The version of the
     operating systems the approval rule applies to, such as
     `BigSur11.3.1` or `Ventura13.7`.
     The default selection is `All`.
    * **Classification**: The package manager
     or package managers that you want to apply packages during
     the patching process. You can choose from the
     following:




    	+ softwareupdate
    	+ installer
    	+ brew
    	+ brew cask
    The default selection is `All`.
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

For more information about working with approval rules in a custom
patch baseline, see [Custom baselines](patch-manager-predefined-and-custom-patch-baselines.md#patch-manager-baselines-custom "patch-manager-predefined-and-custom-patch-baselines.md#patch-manager-baselines-custom"). 9. If you want to explicitly approve any patches in addition to those
meeting your approval rules, do the following in the **Patch
exceptions** section:

    * For **Approved patches**, enter a
     comma-separated list of the patches you want to
     approve.


    For information about accepted formats for lists of approved patches and rejected patches,
     see [Package name
     formats for approved and rejected patch lists](patch-manager-approved-rejected-package-name-formats.md "patch-manager-approved-rejected-package-name-formats.md").
    * (Optional) For **Approved patches compliance
     level**, assign a compliance level to the
     patches in the list.

10. If you want to explicitly reject any patches that otherwise meet
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
      - **Allow as
        dependency**: A package in the
        **Rejected patches** list is
        installed only if it's a dependency of another
        package. It's considered compliant with the patch
        baseline and its status is reported as
        _InstalledOther_. This is the
        default action if no option is specified.
      - **Block**: Packages
        in the **Rejected patches** list,
        and packages that include them as dependencies,
        aren't installed by Patch Manager under any
        circumstances. If a package was installed before it
        was added to the **Rejected
        patches** list, or is installed outside
        of Patch Manager afterward, it's considered noncompliant
        with the patch baseline and its status is reported
        as _InstalledRejected_.

11. (Optional) For **Manage tags**, apply one or more
    tag key name/value pairs to the patch baseline.

Tags are optional metadata that you assign to a resource. Tags
allow you to categorize a resource in different ways, such as by
purpose, owner, or environment. For example, you might want to tag a
patch baseline to identify the severity level of patches it
specifies, the package manager it applies to, and the environment
type. In this case, you could specify tags similar to the following
key name/value pairs:

    * `Key=PatchSeverity,Value=Critical`
    * `Key=PackageManager,Value=softwareupdate`
    * `Key=Environment,Value=Production`

12. Choose **Create patch baseline**.
