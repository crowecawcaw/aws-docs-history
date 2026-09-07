

# Migrate a WorkSpace in WorkSpaces Personal
<a name="migrate-workspaces"></a>

**Note**  
If you want to unsubscribe from or uninstall Microsoft Office version licenses through AWS from your WorkSpace, we recommend using [Manage applications](manage-applications).

You can migrate a WorkSpace from one bundle to another, while retaining the data on the user volume. The following are example scenarios:
+ You can migrate WorkSpaces from the Windows 7 desktop experience to the Windows 10 desktop experience.
+ You can migrate WorkSpaces from the PCoIP protocol to DCV. If you want to change only the streaming protocol, use the Modify protocols feature instead. Modify protocols retains your root volume and does not require a rebuild. For more information, see [Modify protocols](https://docs.aws.amazon.com/workspaces/latest/adminguide/modify-workspaces.html#modify_protocols). Use the Migrate feature described in this section when you need to change the bundle or operating system.
+ You can migrate WorkSpaces from the 32-bit Microsoft Office on Windows Server 2016-powered WorkSpaces bundle to the 64-bit Microsoft Office on Windows Server 2019 and Windows Server 2022-powered WorkSpaces bundles.
+ You can migrate WorkSpaces from one public or custom bundle to another. For example, you can migrate from GPU-enabled (Graphics.g6, Graphics.g4dn. GraphicsPro.g4dn, Graphics, and GraphicsPro) bundles to non-GPU-enabled bundles, as well as in the other direction.
+ You can migrate WorkSpaces from the Windows 10 BYOL to the Windows 11 BYOL but migration from Windows 11 to Windows 10 is not supported.
+ Value bundles are not supported on Windows 11. To migrate your Windows 7 or 10 value bundle WorkSpaces to Windows 11, you need to switch your Value WorkSpaces to a bigger bundle offering first. 
+ Before migrating WorkSpaces from Windows 7 to Windows 11, you need to migrate it to Windows 10. Log in to Windows 10 WorkSpace at least once before migrating it to Windows 11. Migrating from Windows 7 WorkSpaces directly to Windows 11 is not supported.
+ You can migrate Windows WorkSpaces that use Microsoft Office through AWS to a custom WorkSpaces bundle with Microsoft 365 applications. After the migration, your WorkSpaces are unsubscribed from Microsoft Office.
+ You can migrate Windows WorkSpaces that use Microsoft Office through AWS to a WorkSpaces bundle with no Office 2016/2019 subscription. After the migration, your WorkSpaces are unsubscribed from Microsoft Office.
+ You can migrate BYOL BYOP WorkSpaces from Windows 10 to Windows 11, and license-included BYOP WorkSpaces from Windows Server 2019 to Windows Server 2022.
+ You can migrate any Windows Server powered WorkSpace bundle to Windows Server 2025. Once migrated, you will be using DCV streaming protocol to enable high-performance remote desktop streaming, even with graphics-intensive applications, over varying network conditions, even with less powerful client devices.
+ You can migrate any Windows Server license-included BYOP WorkSpace bundle to BYOP Windows Server 2025. 
+ You can migrate Linux WorkSpaces between operating systems, including Amazon Linux 2, Ubuntu, Red Hat Enterprise Linux, and Rocky Linux. For more information, see [Migrate a Linux WorkSpace to a different operating system](migrate-linux-workspaces.md).

For more information about Amazon WorkSpaces bundles, see [Bundles and images for WorkSpaces Personal](amazon-workspaces-bundles.md).

The migration process recreates the WorkSpace by using a new root volume from the target bundle image and the user volume from the last available snapshot of the original WorkSpace. A new user profile is generated during migration for better compatibility. The old user profile is renamed, and then certain files in the old user profile are moved to the new user profile. (For details about what gets moved, see [What happens during migration](#during-migration).)

The migration process takes up to one hour per WorkSpace. When you initiate the migration process, a new WorkSpace is created. If an error occurs that prevents successful migration, the original WorkSpace is recovered and returned to its original state, and the new WorkSpace is terminated.

**Contents**
+ [Migration limits](#migration-limits)
+ [Migration scenarios](#migration-scenarios)
+ [What happens during migration](#during-migration)
+ [Best practices](#migration-best-practices)
+ [Troubleshooting](#migration_troubleshooting)
+ [How billing is affected](#migration-billing)
+ [Migrating a WorkSpace](#migration-workspaces)

## Migration limits
<a name="migration-limits"></a>
+ You cannot migrate to a public or custom Windows 7 desktop experience bundle. You also cannot migrate to Bring Your Own License (BYOL) Windows 7 bundles.
+ You can migrate BYOL WorkSpaces only to other BYOL bundles. To migrate a BYOL WorkSpace from PCoIP to DCV, you must first create a BYOL bundle with the DCV protocol. You can then migrate your PCoIP BYOL WorkSpaces to that DCV BYOL bundle. 
+ You cannot migrate a WorkSpace created from public or custom bundles to a BYOL bundle.
+ DCV Protocol supports Graphics G6 bundles, Graphics.g4dn, and GraphicsPro.g4dn on Windows. On Ubuntu, only Graphics.g4dn and GraphicsPro.g4dn are available.
+ PCoIP Protocol supports Graphics.g4dn and GraphicsPro.g4dn bundles on Windows only.
+ For information about migrating Linux WorkSpaces, see [Migrate a Linux WorkSpace to a different operating system](migrate-linux-workspaces.md).
+ In AWS Regions that support more than one language, you can migrate WorkSpaces between language bundles.
+ The source and target bundles must be different. (However, in Regions that support more than one language, you can migrate to the same Windows 10 bundle as long as the languages differ.) If you want to refresh your WorkSpace using the same bundle, [rebuild the WorkSpace](rebuild-workspace.md) instead.
+ You cannot migrate WorkSpaces across Regions.
+ In some cases, if migration is unable to finish successfully, you might not receive an error message, and it might appear that the migration process did not start. If the WorkSpace bundle remains the same one hour after attempting migration, the migration is unsuccessful. Contact the [AWS Support Center](https://console.aws.amazon.com/support/home#/) for assistance.
+ You cannot migrate BYOP WorkSpaces to PCoIP or DCV WorkSpaces.
+ You cannot migrate Active Directory domain-joined WorkSpaces to Microsoft Entra-joined WorkSpaces.

## Migration scenarios
<a name="migration-scenarios"></a>

The following table shows which migration scenarios are available:


| Source OS | Target OS | Available? | 
| --- | --- | --- | 
| Public or custom bundle Windows 7 | Public or custom bundle Windows 10 | Yes | 
| Custom bundle Windows 7 | Public bundle Windows 7 | No | 
| Custom bundle Windows 7 | Custom bundle Windows 7 | No | 
| Public bundle Windows 7 | Custom bundle Windows 7 | No | 
| Public or custom bundle Windows 10 | Public or custom bundle Windows 7 | No | 
| Public or custom bundle Windows 10 | Custom bundle Windows 10 | Yes | 
| Windows 7 BYOL bundle | Windows 7 BYOL bundle | No | 
| Windows 7 BYOL bundle | Windows 10 BYOL bundle | Yes | 
| Windows 10 BYOL bundle | Windows 7 BYOL bundle | No | 
| Windows 10 BYOL bundle | Windows 10 BYOL bundle | Yes | 
| Windows Server 2016-powered Public Windows 10 bundle | Windows Server 2019-powered Public Windows 10 bundle | Yes | 
| Windows Server 2019-powered Public Windows 10 bundle | Windows Server 2016-powered Public Windows 10 bundle | Yes | 
| Windows 10 BYOL bundle | Windows 11 BYOL bundle | Yes | 
| Windows 11 BYOL bundle | Windows 10 BYOL bundle | No | 
| Windows Server 2016-powered custom Windows 10 bundle | Windows Server 2019-powered Public Windows 10 bundle | Yes | 
| Windows Server 2016-powered custom Windows 10 bundle | Windows Server 2022-powered Public Windows 10 bundle | Yes | 
| Windows Server 2019-powered custom Windows 10 bundle | Windows Server 2022-powered Public Windows 10 bundle | Yes | 
| Windows 10 BYOP BYOL | Windows 11 BYOP BYOL | Yes | 
| Windows 11 BYOP BYOL | Windows 10 BYOP BYOL | No | 
| Windows Server 2016-powered Public Windows 10 bundle | Windows Server 2025-powered Public Windows Server bundle | Yes | 
| Windows Server 2019-powered Public Windows 10 bundle | Windows Server 2025-powered Public Windows Server bundle | Yes | 
| Windows Server 2022-powered Public Windows 10 bundle | Windows Server 2025-powered Public Windows Server bundle | Yes | 
| Windows Server 2016-powered custom Windows 10 bundle | Windows Server 2025-powered Public Windows Server bundle | Yes | 
| Windows Server 2019-powered custom Windows 10 bundle | Windows Server 2025-powered Public Windows Server bundle | Yes | 
| Windows Server 2022-powered custom Windows 10 bundle | Windows Server 2025-powered Public Windows Server bundle | Yes | 
| Windows Server 2019-powered Public BYOP  | Windows Server 2022-powered Public BYOP  | Yes | 
| Windows Server 2022-powered Public BYOP  | Windows Server 2019-powered Public BYOP  | No | 
| Windows Server 2019-powered Public BYOP  | Windows Server 2025-powered Public BYOP  | Yes | 
| Windows Server 2025-powered Public BYOP  | Windows Server 2019-powered Public BYOP  | No | 
| Windows Server 2022-powered Public BYOP  | Windows Server 2025-powered Public BYOP  | Yes | 
| Windows Server 2025-powered Public BYOP  | Windows Server 2022-powered Public BYOP  | No | 
| Windows Server 2019-powered Public Windows 10 bundle  | Windows Server 2025-powered Public BYOP  | Yes | 
| Windows Server 2019-powered Custom Windows 10 bundle  | Windows Server 2025-powered Public BYOP  | Yes | 
| Windows Server 2022-powered Public Windows 10 bundle  | Windows Server 2025-powered Public BYOP  | Yes | 
| Windows Server 2022-powered Custom Windows 10 bundle  | Windows Server 2025-powered Public BYOP  | Yes | 

**Note**  
Web access is not available for the Windows Server 2019-powered Public Windows 10 bundle PCoIP branch.

**Note**  
If you migrate a WorkSpace with nested virtualization enabled, the target bundle must meet the requirements for nested virtualization: DCV (WSP) protocol, a supported operating system, and a non-GPU-enabled bundle. If the target bundle does not meet these requirements, nested virtualization is disabled on the migrated WorkSpace. For more information, see [Nested virtualization for WorkSpaces Personal](nested-virtualization.md).

## What happens during migration
<a name="during-migration"></a>

During migration, the data on the user volume (drive D) is preserved, but all of the data on the root volume (drive C) is lost. This means that none of the installed applications, settings, and changes to the registry are preserved. The old user profile folder is renamed with the `.NotMigrated` suffix, and a new user profile is created.

The migration process recreates drive D based on the last snapshot of the original user volume. During the first boot of the new WorkSpace, the migration process moves the original `D:\Users\%USERNAME%` folder to a folder named `D:\Users\%USERNAME%MMddyyTHHmmss%.NotMigrated`. A new `D:\Users\%USERNAME%\` folder is generated by the new OS.

After the new user profile is created, the files in the following user shell folders are moved from the old `.NotMigrated` profile to the new profile:
+ `D:\Users\%USERNAME%\Desktop`
+ `D:\Users\%USERNAME%\Documents`
+ `D:\Users\%USERNAME%\Downloads`
+ `D:\Users\%USERNAME%\Favorites`
+ `D:\Users\%USERNAME%\Music`
+ `D:\Users\%USERNAME%\Pictures`
+ `D:\Users\%USERNAME%\Videos`

**Important**  
The migration process attempts to move the files from the old user profile to the new profile. Any files that weren't moved during migration remain in the `D:\Users\%USERNAME%MMddyyTHHmmss%.NotMigrated` folder. If the migration is successful, you can see which files got moved in `C:\Program Files\Amazon\WorkspacesConfig\Logs\MigrationLogs`. You can manually move any files that didn't get moved automatically.  
By default, the public bundles have local search indexing disabled. If you were to enable it, the default is to search `C:\Users` and not `D:\Users`, so you need to adjust that as well. If you've set local search indexing specifically to `D:\Users\{{username}}` and not to `D:\Users`, then local search indexing might not work post-migration for any user files that are in the `D:\Users\%USERNAME%MMddyyTHHmmss%.NotMigrated` folder.

Any tags assigned to the original WorkSpace are carried over during migration, and the running mode of the WorkSpace is preserved. However, the new WorkSpace gets a new WorkSpace ID, computer name, and IP address.

The nested virtualization setting is preserved during migration. If nested virtualization was enabled on the source WorkSpace, it remains enabled on the migrated WorkSpace, provided the target bundle meets the requirements for nested virtualization.

## Best practices
<a name="migration-best-practices"></a>

Before you migrate a WorkSpace, do the following:
+ Back up any important data on drive C to another location. All data on drive C is erased during migration.
+ Make sure that the WorkSpace being migrated is at least 12 hours old, to ensure that a snapshot of the user volume has been created. On the **Migrate WorkSpaces** page in the Amazon WorkSpaces console, you can see the time of the last snapshot. Any data created after the last snapshot is lost during migration.
+ To avoid potential data loss, make sure that your users log out of their WorkSpaces and don't log back in until after the migration process is finished. Note that WorkSpaces cannot be migrated when they are in `ADMIN_MAINTENANCE` mode.
+ Make sure that the WorkSpaces you want to migrate have a status of `AVAILABLE`, `STOPPED`, or `ERROR`.
+ Make sure that you have enough IP addresses for the WorkSpaces you are migrating. During migration, new IP addresses will be allocated for the WorkSpaces.
+ If you are using scripts to migrate WorkSpaces, migrate them in batches of no more than 25 WorkSpaces at a time.

## Troubleshooting
<a name="migration_troubleshooting"></a>
+ If your users report missing files after migration, check to see if their user profile files did not get moved during the migration process. You can see which files got moved in `C:\Program Files\Amazon\WorkspacesConfig\Logs\MigrationLogs`. The files that didn't get moved will be located in the `D:\Users\%USERNAME%MMddyyTHHmmss%.NotMigrated` folder. You can manually move any files that didn't get moved automatically. 
+ If you are using the API to migrate WorkSpaces and the migration does not succeed, the target WorkSpace ID returned by the API will not be used, and the WorkSpace will still have the original WorkSpace ID.
+ If a migration does not successfully finish, check the Active Directory to see if it was cleaned up accordingly. You might need to manually remove WorkSpaces that you no longer need.

## How billing is affected
<a name="migration-billing"></a>

During the month in which migration occurs, you are charged prorated amounts for both the new and the original WorkSpaces. For example, if you migrate WorkSpace A to WorkSpace B on May 10, you will be charged for WorkSpace A from May 1 to May 10, and you will be charged for WorkSpace B from May 11 to May 30.

**Note**  
If you are migrating a WorkSpace to a different bundle type (for example, from Performance to Power, or Value to Standard), the size of the root volume (drive C) and the user volume (drive D) might increase during the migration process. If necessary, the root volume increases to match the default root volume size for the new bundle. However, if you had already specified a different size (higher or lower) for the user volume than the default for the original bundle, that same user volume size is retained during the migration process. Otherwise, the migration process uses the larger of the source WorkSpace user volume size and the default user volume size for the new bundle.

## Migrating a WorkSpace
<a name="migration-workspaces"></a>

You can migrate WorkSpaces through the Amazon WorkSpaces console, the AWS CLI or the Amazon WorkSpaces API.

**To migrate a WorkSpace**

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home).

1. In the navigation pane, choose **WorkSpaces**.

1. Select your WorkSpace and choose **Actions**, **Migrate WorkSpaces**.

1. Under **Bundles**, select the bundle that you'd like to migrate your WorkSpace to.
**Note**  
To migrate a BYOL WorkSpace from PCoIP to DCV, you must first create a BYOL bundle with the DCV protocol. You can then migrate your PCoIP BYOL WorkSpaces to that DCV BYOL bundle. 

1. Choose **Migrate WorkSpaces**.

   A new WorkSpace with a status of `PENDING` appears in the Amazon WorkSpaces console. When the migration is finished, the original WorkSpace is terminated, and the status of the new WorkSpace is set to `AVAILABLE`.

1. (Optional) To delete any custom bundles and images that you no longer need, see [Delete a custom bundle or image in WorkSpaces Personal](delete_bundle.md).

To migrate WorkSpaces through the AWS CLI, use the [migrate-workspace](https://docs.aws.amazon.com/cli/latest/reference/workspaces/migrate-workspace.html) command. To migrate WorkSpaces through the Amazon WorkSpaces API, see [MigrateWorkSpace](https://docs.aws.amazon.com/workspaces/latest/api/API_MigrateWorkspace.html) in the *Amazon WorkSpaces API Reference*.