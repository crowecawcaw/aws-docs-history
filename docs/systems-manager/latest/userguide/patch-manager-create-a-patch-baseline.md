# Working with patch

baselines

A patch baseline in Patch Manager, a tool in AWS Systems Manager, defines which patches are
approved for installation on your managed nodes. You can specify approved or
rejected patches one by one. You can also create auto-approval rules to specify that
certain types of updates (for example, critical updates) should be automatically
approved. The rejected list overrides both the rules and the approve list. To use a
list of approved patches to install specific packages, you first remove all
auto-approval rules. If you explicitly identify a patch as rejected, it won't be
approved or installed, even if it matches all of the criteria in an auto-approval
rule. Also, a patch is installed on a managed node only if it applies to the
software on the node, even if the patch has otherwise been approved for the managed
node.

###### Topics

- [Viewing AWS
  predefined patch baselines](patch-manager-view-predefined-patch-baselines.md "patch-manager-view-predefined-patch-baselines.md")
- [Working with custom patch
  baselines](patch-manager-manage-patch-baselines.md "patch-manager-manage-patch-baselines.md")
- [Setting an existing patch
  baseline as the default](patch-manager-default-patch-baseline.md "patch-manager-default-patch-baseline.md")

**More info**

- [Patch baselines](patch-manager-patch-baselines.md "patch-manager-patch-baselines.md")
