# Deleting shadow copy storage, schedule, and all shadow

copies

You can delete your shadow copy configuration, including all existing shadow copies and
the shadow copy schedule. At the same time, you can release the shadow copy storage on the
file system.

To do this, enter the `Remove-FsxShadowStorage` command in a remote PowerShell
session on your file system. For instructions on launching a remote PowerShell session on your
file system, see [Using the Amazon FSx CLI for PowerShell](administering-file-systems.md#remote-pwrshell "administering-file-systems.md#remote-pwrshell").

```
`[fs-0123456789abcdef1]PS>``Remove-FsxShadowStorage`

Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-FsxShadowStorage" on target "Removing all Shadow Copies, Shadow Copy Schedule, and Shadow Storage".
[Y] Yes [A] Yes to All [N] No [L] No to All [?] Help (Default is "Y": `Y`
FSx Shadow Storage Configuration
Removing Shadow Copy Schedule
Removing Shadow Copies
All shadow copies removed.
Removing Shadow Storage
Shadow Storage removed successfully.
```
