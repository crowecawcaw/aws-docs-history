

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Patch compliance state values
<a name="patch-manager-compliance-states"></a>

The information about patches for a managed node include a report of the state, or status, of each individual patch.

**Tip**  
If you want to assign a specific patch compliance state to a managed node, you can use the [put-compliance-items](https://docs.aws.amazon.com/cli/latest/reference/ssm/put-compliance-items.html) AWS Command Line Interface (AWS CLI) command or the [PutComplianceItems](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PutComplianceItems.html) API operation. Assigning compliance state isn't supported in the console.

Use the information in the following tables to help you identify why a managed node might be out of patch compliance.

## Patch compliance values for Debian Server and Ubuntu Server
<a name="patch-compliance-values-ubuntu"></a>

For Debian Server and Ubuntu Server, the rules for package classification into the different compliance states are described in the following table.

**Note**  
Keep the following in mind when you're evaluating the `INSTALLED`, `INSTALLED_OTHER`, and `MISSING` status values: If you don't select the **Include nonsecurity updates** check box when creating or updating a patch baseline, patch candidate versions are limited to patches in the following repositories: .   
`bionic-security` (Ubuntu Server 18.04 LTS)
`focal-security` (Ubuntu Server 20.04 LTS)
`jammy-security` (Ubuntu Server 22.04 LTS)
`noble-security` (Ubuntu Server 24.04 LTS)
`plucky-security` (Ubuntu Server 25.04)
`debian-security` (Debian Server)
If you do select the **Include nonsecurity updates** check box, patches from other repositories are considered as well.


| Patch state | Description | Compliance status | 
| --- | --- | --- | 
| **`INSTALLED`** | The patch is listed in the patch baseline and is installed on the managed node. It could have been installed either manually by an individual or automatically by Patch Manager when the `AWS-RunPatchBaseline` document was run on the managed node. | Compliant | 
| **`INSTALLED_OTHER`** | The patch isn't included in the baseline or isn't approved by the baseline but is installed on the managed node. The patch might have been installed manually, the package could be a required dependency of another approved patch, or the patch might have been included in an InstallOverrideList operation. If you don't specify `Block` as the **Rejected patches** action, `INSTALLED_OTHER` patches also includes installed but rejected patches.  | Compliant | 
| **`INSTALLED_PENDING_REBOOT`** | `INSTALLED_PENDING_REBOOT` can mean either of two things:+  The Patch Manager `Install` operation applied the patch to the managed node, but the node has not been rebooted since the patch was applied. This typically means the `NoReboot` option was selected for the `RebootOption` parameter when the `AWS-RunPatchBaseline` document was last run on the managed node. <br />For more information, see [Parameter name: `RebootOption`](patch-manager-aws-runpatchbaseline.md#patch-manager-aws-runpatchbaseline-parameters-norebootoption). <br />+  A patch was installed outside of Patch Manager since the last time the managed node was rebooted. <br />In neither case does it mean that a patch with this status *requires* a reboot, only that the node hasn't been rebooted since the patch was installed. | Non-Compliant | 
| **`INSTALLED_REJECTED`** | The patch is installed on the managed node but is specified in a **Rejected patches** list. This typically means the patch was installed before it was added to a list of rejected patches. | Non-Compliant | 
| **`MISSING`** | The patch is approved in the baseline, but it isn't installed on the managed node. If you configure the `AWS-RunPatchBaseline` document task to scan (instead of install), the system reports this status for patches that were located during the scan but haven't been installed. | Non-Compliant | 
| **`FAILED`** | The patch is approved in the baseline, but it couldn't be installed. To troubleshoot this situation, review the command output for information that might help you understand the problem. | Non-Compliant | 

## Patch compliance values for other operating systems
<a name="patch-compliance-values"></a>

For all operating systems besides Debian Server and Ubuntu Server, the rules for package classification into the different compliance states are described in the following table. 


|  Patch state | Description | Compliance value | 
| --- | --- | --- | 
| **`INSTALLED`** | The patch is listed in the patch baseline and is installed on the managed node. It could have been installed either manually by an individual or automatically by Patch Manager when the `AWS-RunPatchBaseline` document was run on the node. | Compliant | 
| **`INSTALLED_OTHER`**¹ | The patch isn't in the baseline, but it is installed on the managed node. There are two possible reasons for this:1.  The patch might have been installed manually. <br />2.  Linux only: The package might have been installed as a required *dependency* of a different, approved patch. If you specify `Allow as dependency` as the **Rejected patches** action, patches that are installed as dependencies are given the reporting status `INSTALLED_OTHER`. <br />Note that Windows Server doesn't support the concept of patch dependencies. For information about how Patch Manager handles patches in the **Rejected patches** list on Windows Server, see [Rejected patch list options in custom patch baselines](patch-manager-windows-and-linux-differences.md#rejected-patches-diff).  | Compliant | 
| **`INSTALLED_REJECTED`** | The patch is installed on the managed node but is specified in a rejected patches list. This typically means the patch was installed before it was added to a list of rejected patches. | Non-Compliant | 
| **`INSTALLED_PENDING_REBOOT`** | `INSTALLED_PENDING_REBOOT` can mean either of two things:+  The Patch Manager `Install` operation applied the patch to the managed node, but the node has not been rebooted since the patch was applied. This typically means the `NoReboot` option was selected for the `RebootOption` parameter when the `AWS-RunPatchBaseline` document was last run on the managed node. <br />For more information, see [Parameter name: `RebootOption`](patch-manager-aws-runpatchbaseline.md#patch-manager-aws-runpatchbaseline-parameters-norebootoption). <br />+  A patch was installed outside of Patch Manager since the last time the managed node was rebooted. <br />In neither case does it mean that a patch with this status *requires* a reboot, only that the node hasn't been rebooted since the patch was installed. | Non-Compliant | 
| **`MISSING`** | The patch is approved in the baseline, but it isn't installed on the managed node. If you configure the `AWS-RunPatchBaseline` document task to scan (instead of install), the system reports this status for patches that were located during the scan but haven't been installed. | Non-Compliant | 
| **`FAILED`** | The patch is approved in the baseline, but it couldn't be installed. To troubleshoot this situation, review the command output for information that might help you understand the problem. | Non-Compliant | 
| **`NOT_APPLICABLE`**¹ | *This compliance state is reported only for Windows Server operating systems.*<br />The patch is approved in the baseline, but the service or feature that uses the patch isn't installed on the managed node. For example, a patch for a web server service such as Internet Information Services (IIS) would show `NOT_APPLICABLE` if it was approved in the baseline, but the web service isn't installed on the managed node. A patch can also be marked `NOT_APPLICABLE` if it has been superseded by a subsequent update. This means that the later update is installed and the `NOT_APPLICABLE` update is no longer required. | Not applicable | 
| AVAILABLE\_SECURITY\_UPDATES | *This compliance state is reported only for Windows Server operating systems.*<br />An available security update patch that is not approved by the patch baseline can have a compliance value of `Compliant` or `Non-Compliant`, as defined in a custom patch baseline.<br />When you create or update a patch baseline, you choose the status you want to assign to security patches that are available but not approved because they don't meet the installation criteria specified in the patch baseline. For example, security patches that you might want installed can be skipped if you have specified a long period to wait after a patch is released before installation. If an update to the patch is released during your specified waiting period, the waiting period for installing the patch starts over. If the waiting period is too long, multiple versions of the patch could be released but never installed.<br />For patch summary counts, when a patch is reported as `AvailableSecurityUpdate`, it will always be included in `AvailableSecurityUpdateCount`. If the baseline is configured to report these patches as `NonCompliant`, it is also included in `SecurityNonCompliantCount`. If the baseline is configured to report these patches as `Compliant`, they are not included in `SecurityNonCompliantCount`. These patches are always reported with an unspecified severity and are never included in the `CriticalNonCompliantCount`. | Compliant or Non-Compliant, depending on the option selected for available security updates. Using the console to create or update a patch baseline, you specify this option in the **Available security updates compliance status** field. Using the AWS CLI to run the [create-patch-baseline](https://docs.aws.amazon.com/cli/latest/reference/ssm/create-patch-baseline.html) or [update-patch-baseline](https://docs.aws.amazon.com/cli/latest/reference/ssm/update-patch-baseline.html) command, you specify this option in the `available-security-updates-compliance-status` parameter.  | 

¹ For patches with the state `INSTALLED_OTHER` and `NOT_APPLICABLE`, Patch Manager omits some data from query results based on the [describe-instance-patches](https://docs.aws.amazon.com/cli/latest/reference/ssm/describe-instance-patches.html) command, such as the values for `Classification` and `Severity`. This is done to help prevent exceeding the data limit for individual nodes in Inventory. To view all patch details, you can use the [describe-available-patches](https://docs.aws.amazon.com/cli/latest/reference/ssm/describe-available-patches.html) command. 