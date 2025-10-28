# Troubleshooting data deduplication

Use the following information to help troubleshoot some common issues when configuring and using data deduplication.

###### Topics

- [Data deduplication is not working](#data-dedup-not-working "#data-dedup-not-working")
- [Deduplication values are unexpectedly set to 0](#data-dedup-stopped "#data-dedup-stopped")
- [Space is not freed up on file system after deleting files](#data-dedup-freed-space "#data-dedup-freed-space")

## Data deduplication is not working

To see the current status of data deduplication,
run the `Get-FSxDedupStatus` PowerShell command to view the completion status for the most recent
deduplication jobs. If one or more jobs is failing, you may not see an increase in free storage capacity
on your file system.

The most common reason for deduplication jobs failing is insufficient memory.

- Microsoft
  [recommends](https://docs.microsoft.com/en-us/windows-server/storage/data-deduplication/install-enable#faq "https://docs.microsoft.com/en-us/windows-server/storage/data-deduplication/install-enable#faq")
  optimally having 1 GB of memory per 1 TB of logical data (or at a minimum 350 MB per 1 TB
  of logical data). Use the
  [Amazon FSx performance table](performance.md#performance-table "performance.md#performance-table") to determine the memory associated
  with your file system's throughput capacity and ensure the memory resources are sufficient
  for the size of your data. If it is not, you need to [increase the file system's throughput capacity](managing-throughput-capacity.md "managing-throughput-capacity.md")
  to the level that meets the memory requirements of 1 GB per 1 TB of logical data.
- Deduplication jobs are configured with the Windows recommended default of 25% memory
  allocation, which means that for a file system with 32 GB of memory, 8 GB will be available for
  deduplication. The memory allocation is configurable (using the `Set-FSxDedupSchedule`
  command with parameter `–Memory`). Be aware that using a higher memory allocation for dedup
  may impact file system performance.
- You can modify the configuration of deduplication jobs to reduce the amount of memory
  required. For example, you can constrain the optimization to run on specific file types or
  folders, or set a minimum file size and age for optimization. We also recommend configuring
  deduplication jobs to run during idle periods when there is minimal load on your file system.

You may also see errors if deduplication jobs have insufficient time to complete. You may need to
change the maximum duration of jobs, as described in
[Modifying a data deduplication schedule](managing-data-dedup.md#set-dedup-sched "managing-data-dedup.md#set-dedup-sched").

If deduplication jobs have been failing for a long period of time, and there have been changes
to the data on the file system during this period, subsequent deduplication jobs may require more
resources to complete successfully for the first time.

## Deduplication values are unexpectedly set to 0

The values for `SavedSpace` and `OptimizedFilesSavingsRate` are unexpectedly 0 for a file
system on which you have configured data deduplication.

This can occur during the storage optimization process when you increase the file system's storage capacity.
When you increase a file system's storage capacity,
Amazon FSx cancels existing data deduplication jobs during the storage optimization process, which migrates data from the old disks to the new, larger disks.
Amazon FSx resumes data deduplication on the file system once the storage optimization job completes. For more information about increasing storage capacity and storage optimization,
see [Managing storage capacity](managing-storage-configuration.md#managing-storage-capacity "managing-storage-configuration.md#managing-storage-capacity").

## Space is not freed up on file system after deleting files

The expected behavior of data deduplication is that if the data that was deleted was something
that dedup had saved space on, then the space is not actually freed up on your file system until
the garbage collection job runs.

A practice you may find helpful is to set the schedule to run the garbage collection job right
after you delete a large number of files. After the garbage collection job finishes, you can set
the garbage collection schedule back to its original settings. This ensures you can quickly see the
space from your deletions immediately.

Use the following procedure to set the garbage collection job to run in 5 minutes.

1. To verify that data deduplication is enabled, use the `Get-FSxDedupStatus` command.
   For more information on the command and its expected output,
   see [Viewing the amount of saved space](managing-data-dedup.md#get-dedup-status "managing-data-dedup.md#get-dedup-status").
2. Use the following to set the schedule to run the garbage collection job 5 minutes from now.

```
$FiveMinutesFromNowUTC = ((get-date).AddMinutes(5)).ToUniversalTime()
$DayOfWeek = $FiveMinutesFromNowUTC.DayOfWeek
$Time = $FiveMinutesFromNowUTC.ToString("HH:mm")

Invoke-Command -ComputerName ${RPS_ENDPOINT} -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Set-FSxDedupSchedule -Name "WeeklyGarbageCollection" -Days $Using:DayOfWeek -Start $Using:Time -DurationHours 9
}
```

3. After the garbage collection job has run and the space has been freed up, set the schedule
   back to its original settings.
