# Viewing the shadow copy schedule

To view the existing shadow copy schedule on your file system, enter the following command
in a remote PowerShell session on your file system. For instructions on launching a remote
PowerShell session on your file system, see [Using the Amazon FSx CLI for PowerShell](administering-file-systems.md#remote-pwrshell "administering-file-systems.md#remote-pwrshell").

```
`[fs-0123456789abcdef1]PS>` `Get-FsxShadowCopySchedule`
FSx Shadow Copy Schedule

Start Time                Days of week                             WeeksInterval
----------                ------------                             -------------
2019-07-16T07:00:00+00:00 Monday,Tuesday,Wednesday,Thursday,Friday             1
2019-07-16T12:00:00+00:00 Monday,Tuesday,Wednesday,Thursday,Friday             1

```
