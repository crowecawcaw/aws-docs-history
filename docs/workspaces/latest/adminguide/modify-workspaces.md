# Modify a WorkSpace in WorkSpaces Personal

After you launch a WorkSpace, you can modify its configuration in three ways:

- You can change the size of its root volume (for Windows, drive C; for Linux, /)
  and its user volume (for Windows, drive D; for Linux /home).
- You can change its compute type to select a new bundle.
- You can modify the streaming protocol using the AWS CLI or Amazon WorkSpaces
  API if your WorkSpace was created with PCoIP bundles.
  To see the current modification state of a WorkSpace, select the arrow to show more
  details about that WorkSpace. The possible values for **State** are
  **Modifying Compute**, **Modifying Storage,** and
  **None**.

If you want to modify a WorkSpace, it must have a status of `AVAILABLE` or
`STOPPED`. You can't change the volume size and the compute type at the same
time.

Changing the volume size or compute type of a WorkSpace will change the billing rate for
the WorkSpace.

To allow your users to modify their volumes and compute types themselves, see [Enable self-service WorkSpaces
management capabilities for your users in WorkSpaces Personal](enable-user-self-service-workspace-management.md "enable-user-self-service-workspace-management.md").

## Modify volume sizes

You can increase the size of the root and user volumes for a WorkSpace, up to 2000 GB
each. WorkSpace root and user volumes come in set groups that can't be changed. The
available groups are:

| [Root (GB), User (GB)]     |
| -------------------------- |
| [80, 10]                   |
| [80, 50]                   |
| [80, 100]                  |
| [175 to 2000, 100 to 2000] |

You can expand the root and user volumes whether they are encrypted or unencrypted,
and you can expand both volumes once in a 6-hour period. However, you can't increase the
size of the root and user volumes at the same time. For more information, see [Limitations for Increasing
Volumes](#limitations_increasing_volumes "#limitations_increasing_volumes").

###### Note

When you expand a volume for a WorkSpace, WorkSpaces automatically extends the volume's
partition within Windows or Linux. When the process is finished, you must reboot the
WorkSpace for the changes to take effect.

To ensure that your data is preserved, you cannot decrease the
size of the root or user volumes after you launch a WorkSpace.
Instead, make sure that you specify the minimum sizes for these
volumes when launching a WorkSpace.

- You can launch a Value, Standard, Performance, Power,
  or PowerPro WorkSpace with a minimum of 80 GB for the root
  volume and 10 GB for the user volume.
- You can launch a GeneralPurpose.4xlarge or GeneralPurpose.8xlarge
  WorkSpace with a minimum of 175GB for the root volume and 100 GB
  for the user volume.
- You can launch a Graphics.g4dn, GraphicsPro.g4dn,
  Graphics, or GraphicsPro WorkSpace with a minimum of 100 GB for
  the root volume and 100 GB for the user volume.

While a WorkSpace disk size increase is in progress, users can perform most tasks on
their WorkSpace. However, they can't change their WorkSpace compute type, switch the
WorkSpace running mode, rebuild their WorkSpace, or reboot (restart) their
WorkSpace.

###### Note

If you want your users to be able to use their WorkSpaces while the disk size increase
is in progress, make sure the WorkSpaces have a status of `AVAILABLE` instead
of `STOPPED` before you resize the volumes of the WorkSpaces. If the WorkSpaces are
`STOPPED`, they can't be started while the disk size increase is in
progress.

In most cases, the disk size increase process might take up to two hours. However, if
you're modifying the volume sizes for a large number of WorkSpaces, the process can take
significantly longer. If you have a large number of WorkSpaces to modify, we recommend
contacting AWS Support for assistance.

###### Limitations for increasing

volumes

- You can resize only SSD volumes.
- When you launch a WorkSpace, you must wait 6 hours before you can modify the
  sizes of its volumes.
- You cannot increase the size of the root and user volumes at the same time. To
  increase the root volume, you must first change the user volume to 100 GB. After
  that change is made, you can then update the root volume to any value between 175
  and 2000 GB. After the root volume has been changed to any value between 175 and
  2000 GB, you can then update the user volume further, to any value between 100 and
  2000 GB.

###### Note

If you want to increase both volumes, you must wait 20-30 minutes for the
first operation to finish before you can start the second operation.

- Unless the WorkSpace is a Graphics.g4dn, GraphicsPro.g4dn, Graphics, or
  GraphicsPro WorkSpace, the root volume cannot be less than 175 GB when the user
  volume is 100 GB. Graphics.g4dn, GraphicsPro.g4dn, Graphics, and GraphicsPro WorkSpaces
  can have the root and user volumes both set to 100 GB minimum.
- If the user volume is 50 GB, you cannot update the root volume to anything
  other than 80 GB. If the root volume is 80 GB, the user volume can only be 10, 50,
  or 100 GB.

###### To modify the root volume of a WorkSpace

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **WorkSpaces**.
3. Select the WorkSpace and choose **Actions**, **Modify
   root volume.**.
4. Under **Root volume sizes**, choose a volume size or choose
   **Custom** to enter a custom volume size.
5. Choose **Save changes**.
6. When the disk size increase is finished, you must [reboot the WorkSpace](reboot-workspaces.md "reboot-workspaces.md") for the changes to
   take effect. To avoid data loss, make sure the user saves any open files before
   you reboot the WorkSpace.

###### To modify the user volume of a WorkSpace

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **WorkSpaces**.
3. Select the WorkSpace and choose **Actions**, **Modify
   user volume.**.
4. Under **User volume sizes**, choose a volume size or choose
   **Custom** to enter a custom volume size.
5. Choose **Save changes**.
6. When the disk size increase is finished, you must [reboot the WorkSpace](reboot-workspaces.md "reboot-workspaces.md") for the changes to
   take effect. To avoid data loss, make sure the user saves any open files before
   you reboot the WorkSpace.

###### To change the volume sizes of a WorkSpace

Use the [modify-workspace-properties](../../../cli/latest/reference/workspaces/modify-workspace-properties.md "../../../cli/latest/reference/workspaces/modify-workspace-properties.md") command with the
`RootVolumeSizeGib` or `UserVolumeSizeGib` property.

## Modify compute type

You can switch a WorkSpace between the Standard, Power, Performance, PowerPro
GeneralPurpose.4xlarge, and GeneralPurpose.8xlarge compute types. For more information
about these compute types, see [Amazon WorkSpaces
Bundles](https://aws.amazon.com/workspaces/features/#Amazon_WorkSpaces_Bundles "https://aws.amazon.com/workspaces/features/#Amazon_WorkSpaces_Bundles").

###### Note

- If your source operating system is anything other than Windows Server 2022
  or Windows 11, you cannot change your compute type from PowerPro to
  GeneralPurpose.
- If you are modifying the compute type from a non-GPU-enabled bundles to
  GeneralPurpose.4xlarge or GeneralPurpose.8xlarge, your WorkSpaces must meet
  the minimum root volume size of 175 GB and user volume size of 100 GB. To
  increase the volume size of your WorkSpaces, see [Modify volume sizes](#modify_volume_sizes "#modify_volume_sizes").
- You can change the compute type from Graphics.g4dn to GraphicsPro.g4dn, or
  from GraphicsPro.g4dn to Graphics.g4dn. You cannot change the compute type of
  Graphics.g4dn and GraphicsPro.g4dn to any other value.
- Graphics bundle is no longer supported after November 30, 2023. We recommend migrating your WorkSpaces
  to Graphics.g4dn bundle. For more information, see
  [Migrate a WorkSpace in WorkSpaces Personal](migrate-workspaces.md "migrate-workspaces.md").
- GraphicsPro bundle reaches end-of-life on October 31, 2025. We recommend
  migrating your GraphicsPro WorkSpaces to supported bundles before October 31, 2025.
  For more information, see [Migrate a WorkSpace in WorkSpaces Personal](migrate-workspaces.md "migrate-workspaces.md").
- You cannot change the compute type of Graphics and GraphicsPro to any other
  value.

When you request a compute change, WorkSpaces reboots the WorkSpace using the new compute type.

WorkSpaces preserves the operating system, applications, data, and storage settings for the
WorkSpace.

You can request a larger compute type once in a 6-hour period or a smaller compute type once
every 30 days. For a newly launched WorkSpace, you must wait 6 hours before requesting a
larger compute type.

When a WorkSpace compute type change is in progress, users are disconnected from
their WorkSpace, and they can't use or change the WorkSpace. The WorkSpace is
automatically rebooted during the compute type change process.

###### Important

To avoid data loss, make sure users save any open documents and other application
files before you change the WorkSpace compute type.

The compute type change process might take up to an hour.

###### To change the compute type of a WorkSpace

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **WorkSpaces**.
3. Select the WorkSpace and choose **Actions**, **Modify
   compute type**.
4. Under **Compute type**, choose a compute type.
5. Choose **Save changes**.

###### To change the compute type of a WorkSpace

Use the [modify-workspace-properties](../../../cli/latest/reference/workspaces/modify-workspace-properties.md "../../../cli/latest/reference/workspaces/modify-workspace-properties.md") command with the `ComputeTypeName`
property.

## Modify protocols

If your WorkSpace is created with PCoIP bundles, you can modify their streaming
protocol using the AWS CLI or the Amazon WorkSpaces API. This allows you to migrate the protocol
using your existing WorkSpace without using the WorkSpace migration feature. This also allows you
to use DCV and maintain your root volume without
re-creating existing PCoIP WorkSpaces during the migration process.

- You can only modify your protocol if your WorkSpace was created with PCoIP bundles
  and is not a GPU-enabled WorkSpace.
- Before you modify the protocol to DCV, ensure that your WorkSpace meets the
  following requirements for a DCV WorkSpace.
  - Your WorkSpaces client supports DCV
  - The region where your WorkSpace is deployed supports DCV
  - The IP address and port requirements for DCV are open. For more information,
    see [IP address and port requirements for WorkSpaces](workspaces-port-requirements.md "workspaces-port-requirements.md").
  - Ensure your current bundle is available with DCV.
  - For the best experience with video conferencing we recommend using Power, PowerPro, GeneralPurpose.4xlarge, or GeneralPurpose.8xlarge only.

###### Note

- We highly recommend testing with your non-production WorkSpaces before you start changing the protocol.
- If you modify the protocol from PCoIP to DCV, and then modify the protocol back to PCoIP,
  you won't be able to connect to WorkSpaces through Web Access.

###### To change the protocol of a WorkSpace

1. [Optional] Reboot your WorkSpace and wait until it’s in the `AVAILABLE` state before
   modifying the protocol.
2. [Optional] Use the `describe-workspaces` command to list the
   WorkSpace properties. Ensure that it’s in the `AVAILABLE` state and its
   current `Protocol` is accurate.
3. Use the `modify-workspace-properties` command and modify the
   `Protocols` property from `PCOIP` to `DCV`, or the other way around.

```
aws workspaces modify-workspace-properties
--workspace-id <value>
--workspace-properties "Protocols=[WSP]"
```

###### Important

The `Protocols` property is case-sensitive. Ensure that you use `PCOIP`
or `DCV`. 4. After you run the command, it can take up to 20 minutes for the WorkSpace to reboot and
complete the necessary configurations. 5. Use the `describe-workspaces` command again to list the WorkSpace
properties and verify that it’s in an `AVAILABLE` state and the current
`Protocols` property has been changed to the correct
protocol.

###### Note

    * Modifying the WorkSpace's protocol will not update the bundle description in the console.
     The **Launch Bundle** description will not change.
    * If the WorkSpace remains in an `UNHEALTHY` state after 20
     min, reboot the WorkSpace in the console.

6. You can now connect to your WorkSpace.
