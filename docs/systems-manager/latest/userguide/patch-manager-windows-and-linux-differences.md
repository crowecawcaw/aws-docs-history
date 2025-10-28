# Patching operation

differences between Linux and Windows Server

This topic describes important differences between Linux and Windows Server patching in
Patch Manager, a tool in AWS Systems Manager.

###### Note

To patch Linux managed nodes, your nodes must be running SSM Agent version
2.0.834.0 or later.

An updated version of SSM Agent is released whenever new tools are added to Systems Manager or
updates are made to existing tools. Failing to use the latest version of the agent can
prevent your managed node from using various Systems Manager tools and features. For that reason, we
recommend that you automate the process of keeping SSM Agent up to date on your machines. For
information, see [Automating updates to SSM Agent](ssm-agent-automatic-updates.md "ssm-agent-automatic-updates.md"). Subscribe to the [SSM Agent
Release Notes](https://github.com/aws/amazon-ssm-agent/blob/mainline/RELEASENOTES.md "https://github.com/aws/amazon-ssm-agent/blob/mainline/RELEASENOTES.md") page on GitHub to get notifications about SSM Agent
updates.

## Difference 1: Patch evaluation

Patch Manager uses different processes on Windows managed nodes and Linux managed
nodes in order to evaluate which patches should be present.

###### Linux

For Linux patching, Systems Manager evaluates patch baseline rules and the list of
approved and rejected patches on _each_ managed node.
Systems Manager must evaluate patching on each node because the service retrieves the
list of known patches and updates from the repositories that are configured
on the managed node.

###### Windows

For Windows patching, Systems Manager evaluates patch baseline rules and the list of
approved and rejected patches _directly in the service_.
It can do this because Windows patches are pulled from a single repository
(Windows Update).

## Difference 2: `Not Applicable`

patches

Due to the large number of available packages for Linux operating systems,
Systems Manager doesn't report details about patches in the _Not
Applicable_ state. A `Not Applicable` patch is, for
example, a patch for Apache software when the instance doesn't have Apache
installed. Systems Manager does report the number of `Not Applicable` patches
in the summary, but if you call the [DescribeInstancePatches](../APIReference/API_DescribeInstancePatches.md "../APIReference/API_DescribeInstancePatches.md") API for a managed node, the returned data
doesn't include patches with a state of `Not Applicable`. This
behavior is different from Windows.

## Difference 3: SSM document

support

The `AWS-ApplyPatchBaseline` Systems Manager document (SSM document)
doesn't support Linux managed nodes. For applying patch baselines to Linux,
macOS, and Windows Server managed nodes, the recommended SSM document is
`AWS-RunPatchBaseline`. For more information, see [SSM Command documents for patching
managed nodes](patch-manager-ssm-documents.md "patch-manager-ssm-documents.md") and [SSM Command document for
patching: AWS-RunPatchBaseline](patch-manager-aws-runpatchbaseline.md "patch-manager-aws-runpatchbaseline.md").

## Difference 4: Application

patches

The primary focus of Patch Manager is applying patches to operating systems.
However, you can also use Patch Manager to apply patches to some applications on your
managed nodes.

###### Linux

On Linux operating systems, Patch Manager uses the configured repositories for
updates, and doesn't differentiate between operating systems and application
patches. You can use Patch Manager to define which repositories to fetch updates
from. For more information, see [How to specify an
alternative patch source repository (Linux)](patch-manager-alternative-source-repository.md "patch-manager-alternative-source-repository.md").

###### Windows

On Windows Server managed nodes, you can apply approval rules, as well as
_Approved_ and _Rejected_ patch exceptions, for applications released by
Microsoft, such as Microsoft Word 2016 and Microsoft Exchange Server 2016.
For more information, see [Working with custom patch
baselines](patch-manager-manage-patch-baselines.md "patch-manager-manage-patch-baselines.md").

## Difference 5: Rejected patch list

options in custom patch baselines

When you create a custom patch baseline, you can specify one or more patches
for a **Rejected patches** list. For Linux managed nodes, you
can also choose to allow them to be installed if they're dependencies for
another patch allowed by the baseline.

Windows Server, however, doesn't support the concept of patch dependencies. You can
add a patch to the **Rejected patches** list in a custom
baseline for Windows Server, but the result depends on (1) whether or not the rejected
patch is already installed on a managed node, and (2) which option you choose
for **Rejected patches action**.

Refer to the following table for details about rejected patch options on
Windows Server.

| Installation status            | Option: "Allow as dependency"      | Option: "Block"                       |
| ------------------------------ | ---------------------------------- | ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Patch is already installed     | Reported status: `INSTALLED_OTHER` | Reported status: `INSTALLED_REJECTED` |
| Patch is not already installed | Patch skipped                      | Patch skipped                         | Each patch for Windows Server that Microsoft releases typically contains all the information needed for the installation to succeed. Occasionally, however, a prerequisite package might be required, which you must install manually. Patch Manager doesn't report information about these prerequisites. For related information, see [Windows Update issues troubleshooting](https://learn.microsoft.com/en-us/troubleshoot/windows-client/installing-updates-features-roles/windows-update-issues-troubleshooting "https://learn.microsoft.com/en-us/troubleshoot/windows-client/installing-updates-features-roles/windows-update-issues-troubleshooting") on the Microsoft website. |
