# Patching noncompliant

managed nodes

Many of the same AWS Systems Manager tools and processes you can use to check
managed nodes for patch compliance can be used to bring nodes into
compliance with the patch rules that currently apply to them. To bring
managed nodes into patch compliance, Patch Manager, a tool in AWS Systems Manager, must run
a `Scan and install` operation. (If your goal is only to identify
noncompliant managed nodes and not remediate them, run a `Scan`
operation instead. For more information, see [Identifying
noncompliant managed nodes](patch-manager-find-noncompliant-nodes.md "patch-manager-find-noncompliant-nodes.md").)

###### Install patches using Systems Manager

You can choose from several tools to run a `Scan and
 install` operation:

- (Recommended) Configure a patch policy in Quick Setup, a tool in
  Systems Manager, that lets you install missing patches on a schedule for an
  entire organization, a subset of organizational units, or a single
  AWS account. For more information, see [Configure patching for instances in an
  organization using a Quick Setup patch policy](quick-setup-patch-manager.md "quick-setup-patch-manager.md").
- Create a maintenance window that uses the Systems Manager document (SSM
  document) `AWS-RunPatchBaseline` in a Run Command task type.
  For information, see [Tutorial: Create a
  maintenance window for patching using the console](maintenance-window-tutorial-patching.md "maintenance-window-tutorial-patching.md").
- Manually run `AWS-RunPatchBaseline` in a Run Command
  operation. For information, see [Running commands from the console](running-commands-console.md "running-commands-console.md").

- Install patches on demand using the **Patch now**
  option. For information, see [Patching managed nodes on
  demand](patch-manager-patch-now-on-demand.md "patch-manager-patch-now-on-demand.md").
