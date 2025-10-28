# Restore a WorkSpace in WorkSpaces Personal

Restoring a WorkSpace recreates both the root volume and user volume using a snapshot of
each volume that was taken when the WorkSpace was health. Restoring a WorkSpace rolls back
the data on both the root and user volumes to the point in time when the snapshots were
created. Rebuilding a WorkSpace only rolls back the data on the user volume. This means
that restoring requires you to have snapshots of both the root volume and user volume,
while rebuilding a WorkSpace only requires a snapshot of the user volume. To rebuild a
WorkSpace, see [Rebuild a WorkSpace in WorkSpaces Personal](rebuild-workspace.md "rebuild-workspace.md").

Restoring a WorkSpace causes the following to occur:

- The root volume (for Microsoft Windows, drive C; for Linux, /) is restored to the
  date and time specified using a snapshot. Any applications that were installed, or
  system settings that were changed after the snapshot was created, are lost.
- The user volume (for Microsoft Windows, the D drive; for Linux, /home) is
  recreated to the date and time specified using a snapshot. The current contents of
  the user volume are overwritten.

###### The restore point

When you choose **Actions** and **Rebuild / Restore
WorkSpace**, the date and time of the snapshots used for the operation are
shown. To verify the date and time of the snapshots used for the operation using the
AWS CLI, use the [describe-workspace-snapshots](../../../cli/latest/reference/workspaces/describe-workspace-snapshots.md "../../../cli/latest/reference/workspaces/describe-workspace-snapshots.md") command.

###### When snapshots are taken

Snapshots of the root and user volume are taken on the following basis.

- **After a WorkSpace is first created** —
  Typically, the initial snapshots of the root and user volumes are taken soon after a
  WorkSpace is created (often within 30 minutes). In some AWS Regions, it might take
  several hours to take the initial snapshots after a WorkSpace is created.

If a WorkSpace becomes unhealthy before the initial snapshots are taken, the
WorkSpace can't be restored. In that case, you can try [rebuilding the WorkSpace](rebuild-workspace.md "rebuild-workspace.md") or contact AWS
Support for assistance.

- **During regular use** — Automatic snapshots
  for use when restoring a WorkSpace are scheduled every 12 hours. If the WorkSpace is
  healthy, snapshots of both the root volume and user volume are created around the
  same time. If the WorkSpace is unhealthy, snapshots are created only for the user
  volume.
- **After a WorkSpace has been restored** — When
  you restore a WorkSpace, new snapshots are taken soon after the restore is finished
  (often within 30 minutes). In some AWS Regions, it might take several hours to take
  these snapshots after a WorkSpace is restored.

After a WorkSpace has been restored, if the WorkSpace becomes unhealthy before new
snapshots can be taken, the WorkSpace can't be restored again. In that case, you can
try [rebuilding the WorkSpace](rebuild-workspace.md "rebuild-workspace.md") or contact
AWS Support for assistance.
You can restore a WorkSpace only if the following conditions are met:

- The WorkSpace must have a state of `AVAILABLE`, `ERROR`,
  `UNHEALTHY`, or `STOPPED`.
- Snapshots of the root and user volumes must exist.

###### To restore a WorkSpace

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **WorkSpaces**.
3. Select the WorkSpace to restore and choose **Actions**,

**Rebuild / Restore WorkSpace**. 4. Under **Snapshot**, select the snapshot's time stamp. 5. Choose **Restore**.

###### To restore a WorkSpace using the AWS CLI

Use the [restore-workspace](../../../cli/latest/reference/workspaces/restore-workspace.md "../../../cli/latest/reference/workspaces/restore-workspace.md") command.
