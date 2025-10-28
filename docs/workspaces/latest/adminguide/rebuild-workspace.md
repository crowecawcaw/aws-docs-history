# Rebuild a WorkSpace in WorkSpaces Personal

Rebuilding a WorkSpace recreates the root volume of the most recent image of the bundle that the
WorkSpace was launched from, its user volume, and its primary elastic network interface.
Rebuilding a WorkSpace deletes more data than restoring a WorkSpace, but it only requires you to have a snapshot of the
user volume. To restore a WorkSpace, see [Restore a WorkSpace in WorkSpaces Personal](restore-workspace.md "restore-workspace.md").

Rebuilding a WorkSpace causes the following to occur:

- The root volume (for Microsoft Windows, drive C; for Linux, /) is refreshed with
  the most recent image of the bundle that the WorkSpace was created from. Any
  applications that were installed, or system settings that were changed after the
  WorkSpace was created, are lost.
- The user volume (for Microsoft Windows, the D drive; for Linux, /home) is
  recreated from the most recent snapshot. The current contents of the user volume are
  overwritten.

Automatic snapshots for use when rebuilding a WorkSpace are scheduled every 12
hours. These snapshots of the user volume are taken regardless of the health of the
WorkSpace. When you choose **Actions**, **Rebuild / Restore
WorkSpace**, the date and time of the most recent snapshot is
shown.

When you rebuild a WorkSpace, new snapshots are also taken soon after the rebuild is finished (often within 30 minutes).

- The primary elastic network interface is recreated. The WorkSpace receives a new
  private IP address.

###### Important

After January 14, 2020, WorkSpaces created from a public Windows 7 bundle can no longer be
rebuilt. You might want to consider migrating your Windows 7 WorkSpaces to Windows 10. For
more information, see [Migrate a WorkSpace in WorkSpaces Personal](migrate-workspaces.md "migrate-workspaces.md").

You can rebuild a WorkSpace only if the following conditions are met:

- The WorkSpace must have a state of `AVAILABLE`, `ERROR`,
  `UNHEALTHY`, `STOPPED`, or `REBOOTING`. To
  rebuild a WorkSpace in the `REBOOTING` state, you must use the [RebuildWorkspaces](../api/API_RebuildWorkspaces.md "../api/API_RebuildWorkspaces.md") API operation or the [rebuild-workspaces](../../../cli/latest/reference/workspaces/rebuild-workspaces.md "../../../cli/latest/reference/workspaces/rebuild-workspaces.md") AWS CLI command.
- A snapshot of the user volume must exist.

###### To rebuild a WorkSpace

###### Warning

To rebuild an encrypted WorkSpace, first make sure that the AWS KMS Key is enabled;
otherwise, the WorkSpace becomes unusable. To determine whether a KMS Key is enabled,
see [Displaying KMS Key Details](../../../kms/latest/developerguide/viewing-keys-console.md#viewing-console-details "../../../kms/latest/developerguide/viewing-keys-console.md#viewing-console-details") in the
_AWS Key Management Service Developer Guide_.

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the navigation pane, choose **WorkSpaces**.
3. Select the WorkSpace to rebuild and choose **Actions**,

**Rebuild / Restore WorkSpace**. 4. Under **Snapshot**, select the snapshot's time stamp. 5. Choose **Rebuild**.

###### To rebuild a WorkSpace using the AWS CLI

Use the [rebuild-workspaces](../../../cli/latest/reference/workspaces/rebuild-workspaces.md "../../../cli/latest/reference/workspaces/rebuild-workspaces.md") command.

###### Troubleshooting

If you rebuild a WorkSpace after changing the user's **sAMAccountName** user naming attribute in Active Directory, you might
receive the following error message:

```
"ErrorCode": "InvalidUserConfiguration.Workspace"
"ErrorMessage": "The user was either not found or is misconfigured."
```

To work around this issue, either revert to the original user naming attribute and then
re-initiate the rebuild, or create a new WorkSpace for that user.

###### Rebuild Microsoft Entra ID-joined WorkSpaces

When a user logs in to their WorkSpace for the first time after rebuilding, they need
to go through the out-of-box experience (OOBE) again, similar to when they were assigned a new WorkSpace.
As a result, a new user profile folder is created on the WorkSpace, overriding the original user profile
folder. Hence, during the rebuild of an Entra joined WorkSpace, the content from the original user profile
folder is saved under `D:\Users\<USERNAME%MMddyyTHHmmss%.NotMigrated>` on the rebuilt WorkSpace.
The user needs to copy the original profile content from `D:\Users\<USERNAME%MMddyyTHHmmss%.NotMigrated>`
to the user's profile folder at D:\Users\<USERNAME> to restore all user profile data including desktop icons, shortcuts,
and data files.

###### Note

For Microsoft Entra ID-joined WorkSpaces, we recommend to always use
Restore WorkSpaces, when possible, instead of Rebuild WorkSpaces.
