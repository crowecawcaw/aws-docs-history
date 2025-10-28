# Creating a custom shadow copy schedule

Shadow copy schedules use scheduled task triggers in Microsoft Windows to specify when
shadow copies are automatically taken. A shadow copy schedule can have multiple triggers,
providing you with a lot of scheduling flexibility. Only one shadow copy schedule can exist at a
time. Before you can create a shadow copy schedule, you must first set the amount of [shadow copy storage](shadow-copy-storage.md "shadow-copy-storage.md").

When you run the `Set-FsxShadowCopySchedule` command on a file system, you
overwrite any existing shadow copy schedule. If your client computer is in the UTC time zone,
you can also specify the time zone for a
trigger using Windows time zones and the `-TimezoneId` option. For a list of Windows
time zones, see Microsoft's [Default Timezone](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/default-time-zones "https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/default-time-zones") documentation or run the following at a Windows command prompt:
`tzutil /l`. To learn more about Windows task triggers, see [Task
Triggers](https://docs.microsoft.com/en-us/windows/win32/taskschd/task-triggers "https://docs.microsoft.com/en-us/windows/win32/taskschd/task-triggers") in Microsoft Windows Developer Center documentation.

You can also use the `-Default` option to quickly set up a default shadow copy
schedule. To learn more, see [Configuring shadow copies to use the default storage and schedule](setting-up-fsx-shadow-copies.md "setting-up-fsx-shadow-copies.md").

###### To create a custom shadow copy schedule

1. Create a set of Windows scheduled task triggers to define when shadow copies are taken in
   the shadow copy schedule. Use the `new-scheduledTaskTrigger` command in a PowerShell
   on your local machine to set multiple triggers.

This following example creates a custom shadow copy schedule that takes shadow copies
every Monday–Friday, at 6:00 AM and at 6:00 PM UTC. By default, times are in UTC, unless
you specify a time zone in the Windows scheduled task triggers you create.

```
`PS C:\Users\delegateadmin>` `$trigger1 = new-scheduledTaskTrigger -weekly -DaysOfWeek Monday,Tuesday,Wednesday,Thursday,Friday -at 06:00`
`PS C:\Users\delegateadmin>` `$trigger2 = new-scheduledTaskTrigger -weekly -DaysOfWeek Monday,Tuesday,Wednesday,Thursday,Friday -at 18:00`

```

2. Use `invoke-command` to run the `scriptblock` command. Doing so
   writes a script that sets the shadow copy schedule with the
   `new-scheduledTaskTrigger` value that you just created. Replace
   `FSxFileSystem-Remote-PowerShell-Endpoint` with the Windows Remote PowerShell endpoint of file system that you want to administer.
   You can find the Windows Remote PowerShell endpoint in the Amazon FSx console, in the **Network & Security** section of the file system details screen,
   or in the response of the `DescribeFileSystem` API operation.

```
`PS C:\Users\delegateadmin>` `invoke-command -ComputerName `FSxFileSystem-Remote-PowerShell-Endpoint` -ConfigurationName FSxRemoteAdmin -scriptblock {`
```

3. Enter the following line at the `>>` prompt to set your shadow copy schedule
   using the `set-fsxshadowcopyschedule` command.

```
`>>` `set-fsxshadowcopyschedule -scheduledtasktriggers $Using:trigger1,$Using:trigger2 -Confirm:$false }`
```

The response displays the shadow copy schedule that you configured on the file system.

```
FSx Shadow Copy Schedule


Start Time:    : 2019-07-16T06:00:00+00:00
Days of Week   : Monday,Tuesday,Wednesday,Thursday,Friday
WeeksInterval  : 1
PSComputerName : fs-0123456789abcdef1
RunspaceId     : 12345678-90ab-cdef-1234-567890abcde1

Start Time:    : 2019-07-16T18:00:00+00:00
Days of Week   : Monday,Tuesday,Wednesday,Thursday,Friday
WeeksInterval  : 1
PSComputerName : fs-0123456789abcdef1
RunspaceId     : 12345678-90ab-cdef-1234-567890abcdef

```
