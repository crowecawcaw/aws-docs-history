# Deleting a shadow copy schedule

To delete the existing shadow copy schedule on your file system, enter the following command
in a remote PowerShell session on your file system. For instructions on launching a remote
PowerShell session on your file system, see [Using the Amazon FSx CLI for PowerShell](administering-file-systems.md#remote-pwrshell "administering-file-systems.md#remote-pwrshell").

```
`[fs-0123456789abcdef1]PS>``Remove-FsxShadowCopySchedule`

Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-FsxShadowCopySchedule" on target "Removing FSx Shadow Copy Schedule".
[Y] Yes [A] Yes to All [N] No [L] No to All [?] Help (Default is "Y"): `Y`
`[fs-0123456789abcdef1]PS>`
```
