• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# SSM Command documents for patching

managed nodes

This topic describes the nine Systems Manager documents (SSM documents) available to help you
keep your managed nodes patched with the latest security-related updates.

We recommend using just five of these documents in your patching operations. Together,
these five SSM documents provide you with a full range of patching options using
AWS Systems Manager. Four of these documents were released later than the four legacy SSM
documents they replace and represent expansions or consolidations of
functionality.

###### Recommended SSM documents for patching

We recommend using the following five SSM documents in your patching
operations.

- `AWS-ConfigureWindowsUpdate`
- `AWS-InstallWindowsUpdates`
- `AWS-RunPatchBaseline`
- `AWS-RunPatchBaselineAssociation`
- `AWS-RunPatchBaselineWithHooks`

###### Legacy SSM documents for patching

The following four legacy SSM documents remain available in some AWS Regions
but are no longer updated or supported. These documents aren't guaranteed to work in
IPv6 environments and support only IPv4. They can't be guaranteed to work in all
scenarios and might lose support in the future. We recommend that you don't use
these documents for patching operations.

- `AWS-ApplyPatchBaseline`
- `AWS-FindWindowsUpdates`
- `AWS-InstallMissingWindowsUpdates`
- `AWS-InstallSpecificWindowsUpdates`
  For steps to set up patching operations in an environment that supportsonly IPv6, see
  [Tutorial: Patching a
  server in an IPv6 only environment](patch-manager-server-patching-iPv6-tutorial.md "patch-manager-server-patching-iPv6-tutorial.md").

Refer to the following sections for more information about using these SSM documents
in your patching operations.

###### Topics

- [SSM documents
  recommended for patching managed nodes](#patch-manager-ssm-documents-recommended "#patch-manager-ssm-documents-recommended")
- [Legacy SSM documents for
  patching managed nodes](#patch-manager-ssm-documents-legacy "#patch-manager-ssm-documents-legacy")
- [Known limitations of the SSM documents for
  patching managed nodes](#patch-manager-ssm-documents-known-limitations "#patch-manager-ssm-documents-known-limitations")
- [SSM Command document for
  patching: AWS-RunPatchBaseline](patch-manager-aws-runpatchbaseline.md "patch-manager-aws-runpatchbaseline.md")
- [SSM Command
  document for patching: AWS-RunPatchBaselineAssociation](patch-manager-aws-runpatchbaselineassociation.md "patch-manager-aws-runpatchbaselineassociation.md")
- [SSM Command document
  for patching: AWS-RunPatchBaselineWithHooks](patch-manager-aws-runpatchbaselinewithhooks.md "patch-manager-aws-runpatchbaselinewithhooks.md")
- [Sample scenario for using the
  InstallOverrideList parameter in AWS-RunPatchBaseline or
  AWS-RunPatchBaselineAssociation](patch-manager-override-lists.md "patch-manager-override-lists.md")
- [Using the
  BaselineOverride parameter](patch-manager-baselineoverride-parameter.md "patch-manager-baselineoverride-parameter.md")

## SSM documents

recommended for patching managed nodes

The following five SSM documents are recommended for use in your managed node
patching operations.

###### Recommended SSM documents

- [AWS-ConfigureWindowsUpdate](#patch-manager-ssm-documents-recommended-AWS-ConfigureWindowsUpdate "#patch-manager-ssm-documents-recommended-AWS-ConfigureWindowsUpdate")
- [AWS-InstallWindowsUpdates](#patch-manager-ssm-documents-recommended-AWS-InstallWindowsUpdates "#patch-manager-ssm-documents-recommended-AWS-InstallWindowsUpdates")
- [AWS-RunPatchBaseline](#patch-manager-ssm-documents-recommended-AWS-RunPatchBaseline "#patch-manager-ssm-documents-recommended-AWS-RunPatchBaseline")
- [AWS-RunPatchBaselineAssociation](#patch-manager-ssm-documents-recommended-AWS-RunPatchBaselineAssociation "#patch-manager-ssm-documents-recommended-AWS-RunPatchBaselineAssociation")
- [AWS-RunPatchBaselineWithHooks](#patch-manager-ssm-documents-recommended-AWS-RunPatchBaselineWithHooks "#patch-manager-ssm-documents-recommended-AWS-RunPatchBaselineWithHooks")

### `AWS-ConfigureWindowsUpdate`

Supports configuring basic Windows Update functions and using them to install
updates automatically (or to turn off automatic updates). Available in all
AWS Regions.

This SSM document prompts Windows Update to download and install the
specified updates and reboot managed nodes as needed. Use this document with
State Manager, a tool in AWS Systems Manager, to ensure Windows Update maintains its
configuration. You can also run it manually using Run Command, a tool in AWS Systems Manager,
to change the Windows Update configuration.

The available parameters in this document support specifying a category of
updates to install (or whether to turn off automatic updates), as well as
specifying the day of the week and time of day to run patching operations. This
SSM document is most useful if you don't need strict control over Windows
updates and don't need to collect compliance information.

**Replaces legacy SSM documents:**

- _None_

### `AWS-InstallWindowsUpdates`

Installs updates on a Windows Server managed node. Available in all
AWS Regions.

This SSM document provides basic patching functionality in cases where you
either want to install a specific update (using the `Include Kbs`
parameter), or want to install patches with specific classifications or
categories but don't need patch compliance information.

**Replaces legacy SSM documents:**

- `AWS-FindWindowsUpdates`
- `AWS-InstallMissingWindowsUpdates`
- `AWS-InstallSpecificWindowsUpdates`

The three legacy documents perform different functions, but you can achieve
the same results by using different parameter settings with the newer SSM
document `AWS-InstallWindowsUpdates`. These parameter settings are
described in [Legacy SSM documents for
patching managed nodes](#patch-manager-ssm-documents-legacy "#patch-manager-ssm-documents-legacy").

### `AWS-RunPatchBaseline`

Installs patches on your managed nodes or scans nodes to determine whether any
qualified patches are missing. Available in all
AWS Regions.

`AWS-RunPatchBaseline` allows you to control patch approvals
using the patch baseline specified as the
"default" for an operating system type. Reports patch compliance information
that you can view using the Systems Manager Compliance tools. These tools provide you with
insights on the patch compliance state of your managed nodes, such as which
nodes are missing patches and what those patches are. When you use
`AWS-RunPatchBaseline`, patch compliance information is recorded
using the `PutInventory` API command. For Linux operating systems,
compliance information is provided for patches from both the default source
repository configured on a managed node and from any alternative source
repositories you specify in a custom patch baseline. For more information about
alternative source repositories, see [How to specify an
alternative patch source repository (Linux)](patch-manager-alternative-source-repository.md "patch-manager-alternative-source-repository.md"). For more
information about the Systems Manager Compliance tools, see [AWS Systems Manager Compliance](systems-manager-compliance.md "systems-manager-compliance.md").

**Replaces legacy documents:**

- `AWS-ApplyPatchBaseline`

The legacy document `AWS-ApplyPatchBaseline` applies only to
Windows Server managed nodes, and doesn't provide support for application patching.
The newer `AWS-RunPatchBaseline` provides the same support for both
Windows and Linux systems. Version 2.0.834.0 or later of
SSM Agent is required in order to use the `AWS-RunPatchBaseline`
document.

For more information about the `AWS-RunPatchBaseline` SSM
document, see [SSM Command document for
patching: AWS-RunPatchBaseline](patch-manager-aws-runpatchbaseline.md "patch-manager-aws-runpatchbaseline.md").

### `AWS-RunPatchBaselineAssociation`

Installs patches on your instances or scans instances to determine whether any
qualified patches are missing. Available in all commercial AWS Regions.

`AWS-RunPatchBaselineAssociation` differs from
`AWS-RunPatchBaseline` in a few important ways:

- `AWS-RunPatchBaselineAssociation` is intended for use
  primarily with State Manager associations created using Quick Setup, a tool in
  AWS Systems Manager. Specifically, when you use the Quick Setup Host Management
  configuration type, if you choose the option **Scan instances
  for missing patches daily**, the system uses
  `AWS-RunPatchBaselineAssociation` for the
  operation.

In most cases, however, when setting up your own patching operations,
you should choose [AWS-RunPatchBaseline](patch-manager-aws-runpatchbaseline.md "patch-manager-aws-runpatchbaseline.md") or [AWS-RunPatchBaselineWithHooks](patch-manager-aws-runpatchbaselinewithhooks.md "patch-manager-aws-runpatchbaselinewithhooks.md") instead of
`AWS-RunPatchBaselineAssociation`.

For more information, see the following topics:

    + [AWS Systems Manager Quick Setup](systems-manager-quick-setup.md "systems-manager-quick-setup.md")
    + [SSM Command
     document for patching: AWS-RunPatchBaselineAssociation](patch-manager-aws-runpatchbaselineassociation.md "patch-manager-aws-runpatchbaselineassociation.md")

- `AWS-RunPatchBaselineAssociation` supports the use of tags
  to identify which patch baseline to use with a set of targets when it
  runs.
- For patching operations that use
  `AWS-RunPatchBaselineAssociation`, patch compliance data
  is compiled in terms of a specific State Manager association. The patch
  compliance data collected when
  `AWS-RunPatchBaselineAssociation` runs is recorded using
  the `PutComplianceItems` API command instead of the
  `PutInventory` command. This prevents compliance data
  that isn't associated with this particular association from being
  overwritten.

For Linux operating systems, compliance information is provided for
patches from both the default source repository configured on an
instance and from any alternative source repositories you specify in a
custom patch baseline. For more information about alternative source
repositories, see [How to specify an
alternative patch source repository (Linux)](patch-manager-alternative-source-repository.md "patch-manager-alternative-source-repository.md"). For
more information about the Systems Manager Compliance tools, see [AWS Systems Manager Compliance](systems-manager-compliance.md "systems-manager-compliance.md").

**Replaces legacy documents:**

- **None**

For more information about the `AWS-RunPatchBaselineAssociation`
SSM document, see [SSM Command
document for patching: AWS-RunPatchBaselineAssociation](patch-manager-aws-runpatchbaselineassociation.md "patch-manager-aws-runpatchbaselineassociation.md").

### `AWS-RunPatchBaselineWithHooks`

Installs patches on your managed nodes or scans nodes to determine whether any
qualified patches are missing, with optional hooks you can use to run SSM
documents at three points during the patching cycle. Available in all commercial
AWS Regions. Not supported on macOS.

`AWS-RunPatchBaselineWithHooks` differs from
`AWS-RunPatchBaseline` in its `Install`
operation.

`AWS-RunPatchBaselineWithHooks` supports lifecycle hooks that run
at designated points during managed node patching. Because patch installations
sometimes require managed nodes to reboot, the patching operation is divided
into two events, for a total of three hooks that support custom functionality.
The first hook is before the `Install with NoReboot` operation. The
second hook is after the `Install with NoReboot` operation. The third
hook is available after the reboot of the node.

**Replaces legacy documents:**

- **None**

For more information about the `AWS-RunPatchBaselineWithHooks`
SSM document, see [SSM Command document
for patching: AWS-RunPatchBaselineWithHooks](patch-manager-aws-runpatchbaselinewithhooks.md "patch-manager-aws-runpatchbaselinewithhooks.md").

## Legacy SSM documents for

patching managed nodes

The following four SSM documents are still available in some AWS Regions.
However, they are no longer updated and might be no longer supported in the future,
so we don't recommend their use. Instead, use the documents described in [SSM documents
recommended for patching managed nodes](#patch-manager-ssm-documents-recommended "#patch-manager-ssm-documents-recommended").

###### Legacy SSM Documents

- [AWS-ApplyPatchBaseline](#patch-manager-ssm-documents-legacy-AWS-ApplyPatchBaseline "#patch-manager-ssm-documents-legacy-AWS-ApplyPatchBaseline")
- [AWS-FindWindowsUpdates](#patch-manager-ssm-documents-legacy-AWS-AWS-FindWindowsUpdates "#patch-manager-ssm-documents-legacy-AWS-AWS-FindWindowsUpdates")
- [AWS-InstallMissingWindowsUpdates](#patch-manager-ssm-documents-legacy-AWS-InstallMissingWindowsUpdates "#patch-manager-ssm-documents-legacy-AWS-InstallMissingWindowsUpdates")
- [AWS-InstallSpecificWindowsUpdates](#patch-manager-ssm-documents-legacy-AWS-InstallSpecificWindowsUpdates "#patch-manager-ssm-documents-legacy-AWS-InstallSpecificWindowsUpdates")

### `AWS-ApplyPatchBaseline`

Supports only Windows Server managed nodes, but doesn't include support for patching
applications that is found in its replacement,
`AWS-RunPatchBaseline`. Not available in AWS Regions launched after
August 2017.

###### Note

The replacement for this SSM document,
`AWS-RunPatchBaseline`, requires version
2.0.834.0 or a later version of SSM Agent. You can use the
`AWS-UpdateSSMAgent` document to update your managed nodes to
the latest version of the agent.

### `AWS-FindWindowsUpdates`

Replaced by `AWS-InstallWindowsUpdates`, which can perform all the
same actions. Not available in AWS Regions launched after April 2017.

To achieve the same result that you would from this legacy SSM document, use
the following parameter configuration with the recommended replacement document,
`AWS-InstallWindowsUpdates`:

- `Action` = `Scan`
- `Allow Reboot` = `False`

### `AWS-InstallMissingWindowsUpdates`

Replaced by `AWS-InstallWindowsUpdates`, which can perform all the
same actions. Not available in any AWS Regions launched after April 2017.

To achieve the same result that you would from this legacy SSM document, use
the following parameter configuration with the recommended replacement document,
`AWS-InstallWindowsUpdates`:

- `Action` = `Install`
- `Allow Reboot` = `True`

### `AWS-InstallSpecificWindowsUpdates`

Replaced by `AWS-InstallWindowsUpdates`, which can perform all the
same actions. Not available in any AWS Regions launched after April 2017.

To achieve the same result that you would from this legacy SSM document, use
the following parameter configuration with the recommended replacement document,
`AWS-InstallWindowsUpdates`:

- `Action` = `Install`
- `Allow Reboot` = `True`
- `Include Kbs` = `comma-separated list of KB
articles`

## Known limitations of the SSM documents for

patching managed nodes

### External reboot interruptions

If a reboot is initiated by the system on the node during patch installation (for example, to apply updates to firmware or features like SecureBoot),
the patching document execution may be interrupted and marked as failed even though patches were successfully installed. This occurs because the SSM Agent cannot
persist and resume the document execution state across external reboots.

To verify patch installation status after a failed execution, run a `Scan` patching operation,
then check the patch compliance data in Patch Manager to assess the current compliance state.
