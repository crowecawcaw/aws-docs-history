# Understanding SnapLock Enterprise

This section describes use cases and considerations for the SnapLock Enterprise retention mode.

You might choose the SnapLock Enterprise retention mode for the following use cases.

- You
  can use SnapLock Enterprise to authorize only specific users to delete
  files.
- You can use SnapLock Enterprise to advance your organization's data
  integrity and internal compliance.
- You can use SnapLock Enterprise to test retention settings before using
  SnapLock Compliance.
  Here are some important items to consider about the SnapLock Enterprise retention mode.

- You can use SnapMirror to replicate WORM files, but the source volume and destination volume must have
  the same retention mode (for example, both must be Enterprise).
- A SnapLock volume can't be converted from
  Enterprise to Compliance, or from Compliance to
  Enterprise.
- SnapLock Enterprise
  doesn't support Legal Hold.

## Using privileged delete

One of the key differences between SnapLock Enterprise and SnapLock Compliance is
that a SnapLock administrator can turn on privileged delete on a SnapLock Enterprise
volume to allow a file to be deleted before the file's retention period expires. The
SnapLock administrator is the only user who can delete files from a SnapLock
Enterprise volume that has active retention policies placed on it. For more
information, see [SnapLock administrator](how-snaplock-works.md#snaplock-admin "how-snaplock-works.md#snaplock-admin").

You can turn on or turn off privileged delete with the Amazon FSx console, the AWS CLI, the
Amazon FSx API, and the ONTAP CLI and REST API. To turn on privileged delete, you must
first create a SnapLock audit log volume in the same SVM as the SnapLock volume. For
more information, see [SnapLock audit log volumes](how-snaplock-works.md#snaplock-audit-log-volume "how-snaplock-works.md#snaplock-audit-log-volume").

To turn on privileged delete with the Amazon FSx API, use `PrivilegedDelete`
in the [`CreateSnaplockConfiguration`](../APIReference/API_CreateSnaplockConfiguration.md "../APIReference/API_CreateSnaplockConfiguration.md"). In the Amazon FSx console, for **Privileged Delete**, choose
**Enabled**.

###### Note

You can't issue a privileged delete command to delete a write once, read many
(WORM) file that has an expired retention period. You can issue a normal delete
operation after the retention period expires.

You can opt to turn off privileged delete permanently, but this action is
irreversible. If privileged delete is permanently turned off, you don't need to have
a SnapLock audit log volume associated with the SnapLock Enterprise volume.

To permanently turn off privileged delete with the Amazon FSx API, use
`PrivilegedDelete` in the [`CreateSnaplockConfiguration`](../APIReference/API_CreateSnaplockConfiguration.md "../APIReference/API_CreateSnaplockConfiguration.md"). In the Amazon FSx console, for **Privileged Delete**, choose **Permanently
disabled**.

## Bypassing SnapLock Enterprise mode

If you are using the Amazon FSx console or Amazon FSx API, you must have the
IAM `fsx:BypassSnapLockEnterpriseRetention` permission to delete a
SnapLock Enterprise volume that contains WORM files with active retention policies.

For more information, see [Deleting SnapLock volumes](snaplock-delete-volume.md "snaplock-delete-volume.md").
