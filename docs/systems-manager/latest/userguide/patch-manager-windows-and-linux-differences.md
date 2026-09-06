

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Patching operation differences between Linux and Windows Server
<a name="patch-manager-windows-and-linux-differences"></a>

This topic describes important differences between Linux and Windows Server patching in Patch Manager.

**Note**  
To patch Linux managed nodes, your nodes must be running SSM Agent version 2.0.834.0 or later.  
An updated version of SSM Agent is released whenever new tools are added to Systems Manager or updates are made to existing tools. Failing to use the latest version of the agent can prevent your managed node from using various Systems Manager tools and features. For that reason, we recommend that you automate the process of keeping SSM Agent up to date on your machines. For information, see [Automating updates to SSM Agent](ssm-agent-automatic-updates.md). Subscribe to the [SSM Agent Release Notes](https://github.com/aws/amazon-ssm-agent/blob/mainline/RELEASENOTES.md) page on GitHub to get notifications about SSM Agent updates.

## Difference 1: Patch evaluation
<a name="patch-evaluation_diff"></a>

Patch Manager uses different processes on Windows managed nodes and Linux managed nodes to evaluate which patches should be present. 

**Linux**  
For Linux patching, Systems Manager evaluates patch baseline rules and the list of approved and rejected patches on *each* managed node. Systems Manager must evaluate patching on each node because the service retrieves the list of known patches and updates from the repositories that are configured on the managed node.

**Windows**  
For Windows patching, Systems Manager evaluates patch baseline rules and the list of approved and rejected patches *directly in the service*. It can do this because Windows patches are pulled from a single repository (Windows Update).

## Difference 2: `Not Applicable` patches
<a name="not-applicable-diff"></a>

Due to the large number of available packages for Linux operating systems, Systems Manager doesn't report details about patches in the *Not Applicable* state. A `Not Applicable` patch is, for example, a patch for Apache software when the instance doesn't have Apache installed. Systems Manager does report the number of `Not Applicable` patches in the summary, but if you call the [DescribeInstancePatches](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeInstancePatches.html) API for a managed node, the returned data doesn't include patches with a state of `Not Applicable`. This behavior is different from Windows.

## Difference 3: SSM document support
<a name="document-support-diff"></a>

The `AWS-ApplyPatchBaseline` Systems Manager document (SSM document) doesn't support Linux managed nodes. For applying patch baselines to Linux, macOS, and Windows Server managed nodes, the recommended SSM document is `AWS-RunPatchBaseline`. For more information, see [SSM Command documents for patching managed nodes](patch-manager-ssm-documents.md) and [SSM Command document for patching: `AWS-RunPatchBaseline`](patch-manager-aws-runpatchbaseline.md).

## Difference 4: Application patches
<a name="application-patches-diff"></a>

The primary focus of Patch Manager is applying patches to operating systems. However, you can also use Patch Manager to apply patches to some applications on your managed nodes.

**Linux**  
On Linux operating systems, Patch Manager uses the configured repositories for updates, and doesn't differentiate between operating systems and application patches. You can use Patch Manager to define which repositories to fetch updates from. For more information, see [How to specify an alternative patch source repository (Linux)](patch-manager-alternative-source-repository.md).

**Windows**  
On Windows Server managed nodes, you can apply approval rules, and *Approved* and *Rejected* patch exceptions, for applications released by Microsoft, such as Microsoft Word 2016 and Microsoft Exchange Server 2016. For more information, see [Working with custom patch baselines](patch-manager-manage-patch-baselines.md).

## Difference 5: Rejected patch list options in custom patch baselines
<a name="rejected-patches-diff"></a>

When you create a custom patch baseline, you can specify one or more patches for a **Rejected patches** list. For Linux managed nodes, you can also choose to allow them to be installed if they're dependencies for another patch allowed by the baseline.

Windows Server, however, doesn't support the concept of patch dependencies. You can add a patch to the **Rejected patches** list in a custom baseline for Windows Server, but the result depends on (1) whether the rejected patch is already installed on a managed node, and (2) which option you choose for **Rejected patches action**.

**Rejected patches in bundled Windows updates**  
Microsoft combines some Windows updates into a single update under a parent Microsoft Knowledge Base (KB) ID. This update contains multiple component updates (child KB IDs) and installs the component applicable to the managed node.  
On Windows Server, Patch Manager applies the **Rejected patches** list to the update that Windows Update makes available, which is the parent update. If you add only a child KB to the **Rejected patches** list while its parent update is approved by the baseline, Patch Manager approves the parent update. Windows Update then installs the applicable child component as part of the parent update.

Refer to the following table for details about rejected patch options on Windows Server.


| Installation status | Option: "Allow as dependency" | Option: "Block" | 
| --- | --- | --- | 
| Patch is already installed | Reported status: INSTALLED\_OTHER | Reported status: INSTALLED\_REJECTED | 
| Patch is not already installed | Patch skipped | Patch skipped | 

Each patch for Windows Server that Microsoft releases typically contains all the information needed for the installation to succeed. Occasionally, however, a prerequisite package might be required, which you must install manually. Patch Manager doesn't report information about these prerequisites. For related information, see [Windows Update issues troubleshooting](https://learn.microsoft.com/en-us/troubleshoot/windows-client/installing-updates-features-roles/windows-update-issues-troubleshooting) on the Microsoft website.