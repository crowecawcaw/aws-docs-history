

# Nested virtualization for WorkSpaces Personal

Nested virtualization allows you to run hypervisors such as Hyper-V and KVM inside your WorkSpace. This enables you to use development tools and workflows that require hardware virtualization support, including:
+ Docker Desktop
+ Windows Subsystem for Linux 2 (WSL2)
+ Android Studio emulators
+ QEMU

With nested virtualization enabled, your WorkSpace gains processor-level virtualization support, allowing a hypervisor running inside the WorkSpace to create and manage virtual machines.

For more information about how nested virtualization works at the infrastructure level, see [Use nested virtualization to run hypervisors in Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/amazon-ec2-nested-virtualization.html) in the *Amazon EC2 User Guide*.

**Topics**
+ [Supported configurations](#nested-virt-supported-configurations)
+ [Prerequisites](#nested-virt-prerequisites)
+ [Recommendations](#nested-virt-recommendations)
+ [Known limitations](#nested-virt-known-limitations)
+ [Behavior during lifecycle operations](#nested-virt-lifecycle-operations)
+ [Enable or disable nested virtualization](#nested-virt-enable-disable)

## Supported configurations
<a name="nested-virt-supported-configurations"></a>

**Note**  
There is no additional cost for using nested virtualization. For pricing information, see [Amazon WorkSpaces pricing](https://aws.amazon.com/workspaces/pricing/).

Nested virtualization is supported with the following configurations:

Licensing models  
+ Public (AWS-provided) bundles
+ Bring Your Own License (BYOL)
+ Bring Your Own Protocol (BYOP)

Operating systems  
+ Windows Server 2019
+ Windows Server 2022
+ Windows Server 2025
+ Windows 11
+ Ubuntu 22.04 and newer
+ Red Hat Enterprise Linux 8 and newer
+ Rocky 8 and newer

Protocol  
+ DCV (WSP)
+ Bring Your Own Protocol (BYOP)

Bundle sizes  
+ Most non-GPU bundle sizes (Standard, Performance, Power, PowerPro, GeneralPurpose). The Value bundle is not supported.

Regions  
+ All AWS Regions where WorkSpaces Personal is available, excluding the China (Ningxia) Region and the Israel (Tel Aviv) Region.

## Prerequisites
<a name="nested-virt-prerequisites"></a>

Before you enable nested virtualization on a WorkSpace, ensure the following requirements are met:
+ The WorkSpace must use either DCV (WSP) or Bring Your Own Protocol (BYOP). WorkSpaces using the PCoIP protocol are not supported.
+ The WorkSpace must use a non-GPU bundle.
+ The WorkSpace must not use the Value bundle size.
+ The WorkSpace must run a supported operating system: Windows Server 2019 or later, Windows 11, Ubuntu 22.04 or later, Red Hat Enterprise Linux 8 or later, or Rocky 8 or later. WorkSpaces based on Windows Server 2016, Windows 10, and Amazon Linux 2 do not support nested virtualization.

## Recommendations
<a name="nested-virt-recommendations"></a>
+ **Use Power (4 vCPU) or higher bundle sizes.** While nested virtualization is supported on most non-GPU bundle sizes, hypervisors and nested virtual machines consume additional compute resources. For the best experience, we recommend Power or larger bundles.
+ **Validate application performance.** Test and validate your workloads with nested virtualization enabled to make sure they meet your performance requirements.

## Known limitations
<a name="nested-virt-known-limitations"></a>
+ **Credential Guard and Virtualization-Based Security (VBS)** — Enabling nested virtualization automatically disables Credential Guard and VBS, because nested virtualization uses the hardware virtualization extensions that VBS relies on. For more information, see [Credential Guard / Virtualization-Based Security (VBS)](credential-guard-vbs.md) and [Credential Guard](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/credential-guard.html) in the *Amazon EC2 User Guide*.
+ **GPU-based bundles** — Nested virtualization is not supported on GPU WorkSpaces.
+ **Unsupported operating systems** — Nested virtualization is not supported on WorkSpaces running Windows Server 2016, Windows 10, or Amazon Linux 2.
+ **Standby WorkSpaces** — Nested virtualization is not supported on Standby WorkSpaces.

## Behavior during lifecycle operations
<a name="nested-virt-lifecycle-operations"></a>

The nested virtualization setting is preserved during the following WorkSpace lifecycle operations:
+ **Restore** — When you restore a WorkSpace, the nested virtualization setting is preserved and applied to the restored WorkSpace.
+ **Rebuild** — When you rebuild a WorkSpace, the nested virtualization setting is preserved and applied to the rebuilt WorkSpace.
+ **Migrate** — When you migrate a WorkSpace to a new bundle, the nested virtualization setting is carried over to the migrated WorkSpace, as long as the new bundle is compatible with nested virtualization.

## Enable or disable nested virtualization
<a name="nested-virt-enable-disable"></a>

You can enable or disable nested virtualization using the AWS Management Console, AWS CLI, or Amazon WorkSpaces API.

**To enable nested virtualization during WorkSpace creation**

1. Open the WorkSpaces AWS Management Console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home).

1. Follow the steps to create a WorkSpace.

1. Under **Customization**, expand the **Nested virtualization** section.

1. Select **Enable Nested Virtualization**.

1. Complete the remaining steps to create the WorkSpace.

**To enable or disable nested virtualization on an existing WorkSpace using the AWS Management Console**

1. Open the WorkSpaces AWS Management Console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home).

1. In the navigation pane, choose **WorkSpaces**.

1. Select the WorkSpace.

1. Choose **Actions**, and then choose **Enable Nested Virtualization** or **Disable Nested Virtualization**.

The modification may take several minutes to complete. During the modification, the WorkSpace status shows as `Modifying`. After the modification completes, start the WorkSpace to use nested virtualization.

**Tip**  
To verify the current nested virtualization state of a WorkSpace, select it in the AWS Management Console. In the detail view, the **Summary** section displays a **Nested Virtualization** field showing either `Enabled` or `Disabled`.

**To enable or disable nested virtualization using the AWS CLI**  


1. (Optional) Use the `describe-workspaces` command to verify the current state of the WorkSpace. The response includes a `NestedVirtualizationEnabled` property with a value of `true` or `false`.

   ```bash
   aws workspaces describe-workspaces \
       --workspace-id {{ws-example123456}} \
       --region {{us-west-2}}
   ```

   Example output (relevant fields):

   ```json
   {
       "Workspaces": [
           {
               "WorkspaceId": "ws-example123456",
               "State": "STOPPED",
               "WorkspaceProperties": {
                   "RunningMode": "AUTO_STOP",
                   "RunningModeAutoStopTimeoutInMinutes": 60,
                   "RootVolumeSizeGib": 175,
                   "UserVolumeSizeGib": 100,
                   "ComputeTypeName": "POWER",
                   "Protocols": [
                       "WSP"
                   ],
                   "NestedVirtualizationEnabled": true
               },
               "ModificationStates": []
           }
       ]
   }
   ```

1. Use the `modify-workspace-properties` command with the `NestedVirtualizationEnabled` property.

   To enable:

   ```bash
   aws workspaces modify-workspace-properties \
       --workspace-id {{ws-example123456}} \
       --region {{us-west-2}} \
       --workspace-properties NestedVirtualizationEnabled=true
   ```

   To disable:

   ```bash
   aws workspaces modify-workspace-properties \
       --workspace-id {{ws-example123456}} \
       --region {{us-west-2}} \
       --workspace-properties NestedVirtualizationEnabled=false
   ```

1. Use the `describe-workspaces` command to verify that the modification completed successfully and the `NestedVirtualizationEnabled` property shows the expected value.

**To enable or disable nested virtualization using AWS Tools for PowerShell**  


1. (Optional) Use the `Get-WKSWorkspace` cmdlet to check the current nested virtualization state:

   ```powershell
   (Get-WKSWorkspace -WorkspaceId {{$WORKSPACE_ID}} -Region {{$REGION}}).WorkspaceProperties.NestedVirtualizationEnabled
   ```

   This returns `True` or `False`.

1. Use the `Edit-WKSWorkspaceProperty` cmdlet.

   To enable:

   ```powershell
   Edit-WKSWorkspaceProperty -Region {{$REGION}} -WorkspaceId {{$WORKSPACE_ID}} `
       -WorkspaceProperties_NestedVirtualizationEnabled $true
   ```

   To disable:

   ```powershell
   Edit-WKSWorkspaceProperty -Region {{$REGION}} -WorkspaceId {{$WORKSPACE_ID}} `
       -WorkspaceProperties_NestedVirtualizationEnabled $false
   ```

1. Use the `Get-WKSWorkspace` cmdlet to verify the modification completed successfully:

   ```powershell
   (Get-WKSWorkspace -WorkspaceId {{$WORKSPACE_ID}} -Region {{$REGION}}).WorkspaceProperties.NestedVirtualizationEnabled
   ```

**To enable or disable nested virtualization using the API**  
Use the `ModifyWorkspaceProperties` API action with the `NestedVirtualizationEnabled` parameter set to `true` or `false`.

To check the current state, use the `DescribeWorkspaces` API action and inspect the `NestedVirtualizationEnabled` property in the response.