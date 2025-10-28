# Deleting shadow copies

You can delete one or more existing shadow copies on your file system using the
`Remove-FsxShadowCopies` command in a remote PowerShell session on your file system.
For instructions on launching a remote PowerShell session on your file system, see [Using the Amazon FSx CLI for PowerShell](administering-file-systems.md#remote-pwrshell "administering-file-systems.md#remote-pwrshell").

Specify which shadow copies to delete by using one of the following required options:

- `-Oldest` deletes the oldest shadow copy
- `-All` deletes all existing shadow copies
- `-ShadowCopyId` deletes a specific shadow copy by ID.
  You can use only one option with the command. An error occurs if you don't specify which
  shadow copy to delete, if you specify multiple shadow copy IDs, or if you specify an invalid
  shadow copy ID.

To delete the oldest shadow copy on your file system, enter the following
command in a remote PowerShell session on your file system.

```
`[fs-0123456789abcdef1]PS>``Remove-FsxShadowCopies -Oldest`
Confirm
Are you sure you want to perform this action?
Performing the operation "Remove-FSxShadowCopies" on target "Removing oldest shadow copy".
[Y] Yes [A] Yes to All [N] No [L] No to All [?] Help (Default is "Y": `Y`
Shadow Copy {ABCDEF12-3456-7890-ABCD-EF1234567890} deleted
```

To delete a specific shadow copy on your file system, enter the following
command in a remote PowerShell session on your file system.

```
`[fs-0123456789abcdef1]PS>``Remove-FsxShadowCopies -ShadowCopyId "{ABCDEF12-3456-7890-ABCD-EF1234567890}"`
Are you sure you want to perform this action?
Performing the operation "Remove-FSxShadowCopies" on target "Removing shadow copy {ABCDEF12-3456-7890-ABCD-EF1234567890}".
[Y] Yes [A] Yes to All [N] No [L] No to All [?] Help (Default is "Y":>`Y`
Shadow Copy \\AMZNFSXABCDE123\root\cimv2:Wind32_ShadowCopy.ID{ABCDEF12-3456-7890-ABCD-EF1234567890}".ID deleted.
```

To delete a certain number of the oldest shadow copies on your file system, update your
`-MaxShadowCopyNumber` parameter to the desired number of shadow copies that you would
like to have remaining. However, this change will only take effect after the next shadow copy snapshot
is taken, when the system will automatically delete the excess shadow copies.
Use the following command in a remote PowerShell session on your file system.

```
`[fs-1234567890abcef12]: PS>``Get-fsxshadowstorage`
FSx Shadow Storage Configuration

AllocatedSpace UsedSpace MaxSpace    MaxShadowCopyNumber
-------------- --------- ----------- -------------------
     556679168  21659648 10737418240                  50

[fs-1234567890abcef12]: PS>Set-FsxShadowStorage  -MaxShadowCopyNumber 5
Validation
You have 50 shadow copies. Older versions of shadow copies will be deleted, keeping 5 latest shadow copies on your file system.
Do you want to continue?
[Y] Yes  [N] No  [?] Help (default is "N"): y
FSx Shadow Storage Configuration

AllocatedSpace UsedSpace    MaxSpace MaxShadowCopyNumber
-------------- ---------    -------- -------------------
     556679168  21659648 10737418240                   5


```
