# Viewing existing shadow copies

To view the set of existing shadow copies on your file system, enter the following command
in a remote PowerShell session on your file system. For instructions on launching a remote
PowerShell session on your file system, see [Using the Amazon FSx CLI for PowerShell](administering-file-systems.md#remote-pwrshell "administering-file-systems.md#remote-pwrshell").

```
`[fs-0123456789abcdef1]PS>``Get-FsxShadowCopies`
FSx Shadow Copies: 2 total

Shadow Copy ID                        Creation Time
--------------                        -----------------
{ABCDEF12-3456-7890-ABCD-EF1234567890} 6/17/2019 7:11:09 AM
{FEDCBA21-6543-0987-0987-EF3214567892} 6/19/2019 11:24:19 AM
```
