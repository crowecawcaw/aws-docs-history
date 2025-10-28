# Deleting SnapLock volumes

This section explains how to delete a SnapLock volume.

You can delete a SnapLock Compliance volume if the retention periods of all the write
once, read many (WORM) files on it are expired.

###### Note

When you close an AWS account that contains SnapLock Enterprise or Compliance volumes,
AWS and FSx for ONTAP suspend your account for 90 days leaving your data intact. If you don't reopen your account during those 90
days, AWS deletes your data including data in SnapLock volumes regardless of your retention settings.

You can delete a SnapLock Enterprise volume at any time if you have the required
permissions. To delete a SnapLock Enterprise volume using the ONTAP CLI, you must have the
`fsxadmin` role. For more information, see [File system administrator roles and users](roles-and-users.md#file-system-admin-roles "roles-and-users.md#file-system-admin-roles").

To delete a SnapLock Enterprise volume that contains WORM data with an active retention
policy using the Amazon FSx console, CLI, or Amazon FSx API, you must have the `fsx:BypassSnapLockEnterpriseRetention` IAM permission.

###### Warning

The minimum retention period for a SnapLock audit log volume is six months. Until
this retention period expires you can't delete the SnapLock audit log volume, the
storage virtual machine (SVM), or the file system that's associated with the SVM—even if the volume was
created in SnapLock Enterprise mode. For more information, see
[SnapLock audit log volumes](how-snaplock-works.md#snaplock-audit-log-volume "how-snaplock-works.md#snaplock-audit-log-volume").
