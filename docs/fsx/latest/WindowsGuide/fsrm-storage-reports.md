# Storage Reports

Storage reports provide detailed analysis of file system usage, helping you understand how
storage is being consumed, identify files that can be archived or deleted, and monitor
compliance with file management policies. You can generate multiple types of reports that
analyze file ownership, file types, duplicate files, large files, file screening and quota
usage.

## Report types

You can create the following report types:

- `DuplicateFiles`

Identifies files that have identical content based on file size and hash
comparison. Use this report to find redundant files that consume unnecessary
storage space. The report groups duplicate files together and shows the
total
space that could be recovered by removing duplicates.

- `FilesByFileGroup`

Groups files by their [file group](fsrm-file-groups.md "fsrm-file-groups.md") membership and shows storage consumption
for
each file group. Use this report to understand which types of files
(documents,
media, executables, etc.) consume the most storage space.

- `FilesByOwner`

Groups files by owner and shows how much storage each user or group
consumes.
Use this report to identify users who are consuming the most storage space
and
to allocate storage costs or quotas appropriately.

- `FilesByProperty`

Groups files by classification property values and shows file count and
storage consumption for each property value. Use this report to analyze
files
based on their classification, such as data sensitivity level, department,
or
retention period. This report requires that files have been classified using
[Classification rules](fsrm-file-classification.md#fsrm-classification-rules "fsrm-file-classification.md#fsrm-classification-rules").

- `FileScreenAuditFiles`

Lists [File Screening](fsrm-file-screening.md "fsrm-file-screening.md") violations where users attempted to save files that
were
blocked by active file screens. Use this report to monitor compliance with
file
screening policies and identify users who frequently attempt to save
unauthorized file types.

- `FoldersByProperty`

Groups folders by management property values and shows storage consumption
for
each property value. Use this report to analyze storage usage by folder
purpose,
such as user files, group shares, or application files.

- `LargeFiles`

Lists files that exceed a specified size threshold. Use this report to
identify files that consume significant storage space and may be candidates
for
archiving, compression, or deletion.

- `LeastRecentlyAccessed`

Lists files that haven't been accessed for a specified number of days. Use
this report to identify inactive files that can be archived or moved to
lower-cost storage tiers.

- `MostRecentlyAccessed`

Lists files that were accessed within a specified number of days.

- `QuotaUsage`

Shows quota usage statistics for folders with [quotas](fsrm-quota-management.md "fsrm-quota-management.md") configured. Use this
report to monitor quota compliance and identify folders approaching their
quota
limits.

## Report formats

You can generate reports in multiple formats to suit different use cases:

- `DHTML` - Dynamic HTML format with interactive
  features like sorting and filtering.
- `HTML` - Static HTML format suitable for
  archiving or emailing.
- `XML` - Structured data format for programmatic
  processing.
- `CSV` - Comma-separated values format for
  importing into spreadsheet applications.
- `Text` - Plain text format for simple viewing
  or processing.

You can specify multiple formats for a single report.

## Interactive and scheduled

reports

You can create two types of storage reports:

1. **Interactive reports** - Run immediately when
   created and execute only once. Use interactive reports for ad-hoc analysis or
   troubleshooting. Interactive reports do not have schedules and cannot be
   modified after creation. To run another interactive report, you must create a
   new report with a different name.
2. **Scheduled reports** - Run automatically
   according to a configured schedule. Use scheduled reports for regular monitoring
   and compliance reporting. You can schedule reports to run weekly or monthly at
   specific times. Scheduled reports can be modified to change their configuration,
   and you can also run them on-demand using the [Start-FSxFSRMStorageReport](#start-fsxfsrmstoragereport "#start-fsxfsrmstoragereport")
   command without waiting for the scheduled time.

## Running reports

After you create a scheduled report, you can run it in several ways:

- **Automatic execution** - Scheduled reports run
  automatically at their configured schedule time.
- **Manual execution** - Use [Start-FSxFSRMStorageReport](#start-fsxfsrmstoragereport "#start-fsxfsrmstoragereport") to run a scheduled report on-demand without
  waiting for the scheduled time.

You can monitor report execution using [Get-FSxFSRMStorageReport](#get-fsxfsrmstoragereport "#get-fsxfsrmstoragereport") to check
the status.

## Accessing storage reports

After FSRM generates storage reports, the report files are saved to a default location
on
your file system. To access these reports, you need to map the administrative D$ share
of
your file system.

###### To access storage reports

1. Map the administrative D$ share using the following path format:

```
\\file-system-dns-name\D$
```

For example:

```
\\amznfsxaa11bb22.corp.example.com\D$
```

2. Navigate to the StorageReports folder. This folder contains subfolders
   organized
   by report type and execution date.

###### Note

Accessing the administrative D$ share requires administrator credentials.

## Storage report best practices

Follow these best practices to ensure efficient and effective storage reporting:

### Performance considerations

Storage report generation is resource-intensive because FSRM must scan large
amounts
of files.

- **Limit report scope** - Use the `Namespace`
  parameter to limit reports to specific folders rather than scanning the
  entire file system. Scanning large directory structures is
  resource-intensive and can take hours to complete.
- **Schedule reports during off-peak hours** -
  Run scheduled reports during periods of low system activity, to minimize
  impact on performance. Avoid running reports during backup windows or other
  maintenance tasks.
- **Set reasonable thresholds** - Use threshold
  parameters to limit report output to actionable data. For example, set
  `LargeFileMinimum` to a value that identifies files worth investigating, not
  every file over 1MB.
- **Use RunDuration limits** - Set the
  `RunDuration` parameter to prevent reports from running too long and impacting
  system performance. If a report doesn't complete within the time limit, it
  will resume during the next scheduled run.
- **Monitor report performance** - Use [Get-FSxFSRMStorageReport](#get-fsxfsrmstoragereport "#get-fsxfsrmstoragereport") to check how long reports take to complete.
  If reports consistently take too long, consider narrowing their scope or
  running them less frequently.

### Report design

- **Use descriptive names** - Give reports
  clear, descriptive names that indicate what they analyze and when they run,
  such as "Weekly Large Files - Finance Share" or "Monthly Duplicate Files -
  All Shares".
- **Combine related analysis** - When
  generating multiple report types for the same namespace, create a single
  report with multiple `ReportType` values rather than separate reports. This is
  more efficient because FSRM only needs to scan the directory structure once.
- **Filter by file patterns** - Use file
  pattern parameters to focus reports on specific file types. For example,
  when analyzing large files, you might create separate reports for video
  files, database files, and archive files to better understand storage
  consumption patterns.
- **Leverage classification properties** - Use
  `FilesByProperty` reports to analyze files based on their classification. This
  provides more meaningful insights.

### Report management

- **Review reports regularly** - Schedule time
  to review report results and take action on findings. Reports are only
  valuable if you use them to make storage management decisions.
- **Archive old reports** - Report files
  accumulate over time and consume storage space. Establish a retention policy
  for report files and delete or archive old reports that are no longer
  needed.
- **Test reports before scheduling** - Create
  interactive reports to test report configurations and verify they produce
  the expected results before creating scheduled versions.

## Storage report management commands

You can access two families of FSx remote PowerShell commands for managing storage
reports:

1. **Report definition commands** - Create,
   retrieve, modify, and remove storage report configurations that specify what
   data to analyze, when to run reports, and what formats to generate.
2. **Report execution commands** - Start, stop,
   monitor, and wait for storage report generation. Use these commands to run
   reports on-demand or manage long-running report jobs.

### List of Storage Report

FSx remote
PowerShell commands

###### Note

All the examples in this page assume that you have defined the `$FSxWindowsRemotePowerShellEndpoint` variable with your file system's Windows Remote
PowerShell endpoint. You can find this endpoint in the Amazon FSx console on your file system's
details page, or by using the AWS CLI `describe-file-systems` command.

### Report Definition

Commands

#### New-FSxFSRMStorageReport

**New-FSxFSRMStorageReport**: Creates a storage
report that analyzes specified directories to generate one or more report types.

**Parameters:**

- `Name (string)` - Required. A name for the storage report.
- `Namespace (array)` - Required. An array of paths or folder types to analyze. You can
  specify paths
  in multiple formats:
  - Folder Path
  - [Folder classification](fsrm-file-classification.md#fsrm-management-properties "fsrm-file-classification.md#fsrm-management-properties"). For example, [FolderUsage\_MS="User
    Files"]

- `ReportType (array)` - Required. An array of report types to generate. You can specify
  the following
  values:
  - `DuplicateFiles`: Identifies duplicate files based on file
    size and
    content
  - `FilesByFileGroup`: Groups files by file group membership
  - `FilesByOwner`: Groups files by owner
  - `FilesByProperty`: Groups files by classification property
  - `FileScreenAuditFiles`: Lists file screening violations
  - `FoldersByProperty`: Groups folders by management property
  - `LargeFiles`: Lists files above a specified size threshold
  - `LeastRecentlyAccessed`: Lists files that haven't been
    accessed recently
  - `MostRecentlyAccessed`: Lists files that were accessed
    recently
  - `QuotaUsage`: Shows quota usage statistics

- `ReportFormat (array)` - Optional. An array of output formats. You can specify the
  following values:
  - `DHTML`: Dynamic HTML format
  - `HTML`: Static HTML format
  - `XML`: XML format
  - `CSV`: Comma-separated values format
  - `Text`: Plain text format

- `Interactive (boolean)` - Optional. If set to true, generates an interactive report.
  Interactive reports
  cannot be modified after creation.
- `ScheduleConfigurations (hashtable)` - Required unless report is Interactive. A hashtable containing
  schedule
  configuration with the following properties:
  - `Time (datetime)`: DateTime object specifying when to run
    the task
    (required)
  - `RunDuration (number)`: Number of hours to run the task
    (optional)
  - `Weekly (array)`: Array of weekdays (optional)
  - `Monthly (array)`: Array of days of month, use `-1` for last
    day
    (optional)

**Report-specific parameters:**

- `FileScreenAuditDaysSince (number)` - Optional. For FileScreenAuditFiles reports, specifies how many
  days back to
  include audit events.
- `FileScreenAuditUser (array)` - Optional. For FileScreenAuditFiles reports, specifies an array of
  user
  accounts to include in the report. Only file screening violations by
  these users
  will be included.
- `FileGroupIncluded (array)` - Optional. For FilesByFileGroup reports, specifies which file
  groups to
  include.
- `FileOwnerFilePattern (string)` - Optional. For FilesByOwner reports, specifies a file pattern to
  filter
  results.
- `PropertyName (string)` - Optional. For FilesByProperty reports, specifies the
  classification property
  to group by.
- `FolderPropertyName (string)` - Optional. For FoldersByProperty reports, specifies the folder
  property to
  group by.
- `PropertyFilePattern (string)` - Optional. For FilesByProperty and FoldersByProperty, specifies a
  file pattern
  to filter results.
- `LargeFileMinimum (number)` - Optional. For LargeFiles reports, specifies the minimum file size
  in bytes.
- `LargeFilePattern (string)` - Optional. For LargeFiles reports, specifies a file pattern to
  filter results.
- `LeastAccessedMinimum (number)` - Optional. For LeastRecentlyAccessed reports, specifies the minimum
  number of
  days since last access.
- `LeastAccessedFilePattern (string)` - Optional. For LeastRecentlyAccessed reports, specifies a file
  pattern to
  filter results.
- `MostAccessedMaximum (number)` - Optional. For MostRecentlyAccessed reports, specifies the maximum
  number of
  days since last access.
- `MostAccessedFilePattern (string)` - Optional. For MostRecentlyAccessed reports, specifies a file
  pattern to filter
  results.
- `QuotaMinimumUsage (number)` - Optional. For QuotaUsage reports, specifies the minimum quota
  usage percentage
  to include.

**Examples:**

1. Create a monthly large files report.

```
$schedule = @{
    Time = ("3:00 AM")
    Monthly = @(1) # Run on first day
}

Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ArgumentList $schedule -ScriptBlock {
    param($schedule)
    New-FSxFSRMStorageReport -Name "Monthly Large Files" -Namespace "share\data" -ReportType "LargeFiles" -LargeFileMinimum 100MB -ReportFormat "HTML" -ScheduleConfigurations $schedule
}

```

2. Create a weekly duplicate files report with multiple namespaces and
   formats.

```
$schedule = @{
    Time = ("12:00 AM")
    Weekly = @('Sunday')
    RunDuration = 4
}

$namespaces = @("share\docs", "[FolderUsage_MS=User Files]")
$reportFormats = @("HTML", "CSV")
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ArgumentList @($schedule, $namespaces, $reportFormats) -ScriptBlock {
    param($schedule, $namespaces, $reportFormats)
    New-FSxFSRMStorageReport -Name "Weekly Duplicates" -Namespace $namespaces -ReportType "DuplicateFiles" -ReportFormat $reportFormats -ScheduleConfigurations $schedule
}

```

3. Create an interactive report that runs immediately.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    New-FSxFSRMStorageReport -Name "Find large files" -Namespace "share" -Interactive $true -ReportType "QuotaUsage"
}

```

#### Get-FSxFSRMStorageReport

**Get-FSxFSRMStorageReport**: Retrieves one or
more storage reports from your file system. Returns details about report
configurations and status.

**Parameters:**

- `Name (array)` - Optional. An array of report names to retrieve. If you don't
  specify a name,
  the command returns all storage reports on the file system.

**Examples:**

1. Retrieve all storage reports on the file system.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Get-FSxFSRMStorageReport
}

```

#### Remove-FSxFSRMStorageReport

**Remove-FSxFSRMStorageReport**: Removes one or
more storage reports from your file system. You cannot remove reports that are
currently running.

**Parameters:**

- `Name (array)` - Required. An array of report names to remove.
- `PassThru (boolean)` - Optional. If set to true, returns the removed report object.

**Examples:**

1. Remove a single storage report.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Remove-FSxFSRMStorageReport -Name "Monthly Report" -PassThru
}

```

#### Set-FSxFSRMStorageReport

##### Parameters

- `Name (array)` - Required. An array of report names to modify.
- `Namespace (array)` - Optional. An array of paths or folder types to analyze. You
  can specify
  paths in multiple formats:
  - Folder Path
  - [Folder classification](fsrm-file-classification.md#fsrm-management-properties "fsrm-file-classification.md#fsrm-management-properties"). For example,
    [FolderUsage\_MS="User Files"]

- `ReportType (array)` - Optional. An array of report types to generate. You can specify the following values:
  - `DuplicateFiles`: Identifies duplicate
    files based on file size and content
  - `FilesByFileGroup`: Groups files by file
    group membership
  - `FilesByOwner`: Groups files by owner
  - `FilesByProperty`: Groups files by
    classification property
  - `FileScreenAuditFiles`: Lists file
    screening violations
  - `FoldersByProperty`: Groups folders by
    management property
  - `LargeFiles`: Lists files above a specified
    size threshold
  - `LeastRecentlyAccessed`: Lists files that
    haven't been accessed recently
  - `MostRecentlyAccessed`: Lists files that
    were accessed recently
  - `QuotaUsage`: Shows quota usage statistics

- `ReportFormat (array)` - Optional. An array of output formats. You can specify the
  following
  values:
  - `DHTML`: Dynamic HTML format
  - `HTML`: Static HTML format
  - `XML`: XML format
  - `CSV`: Comma-separated values format
  - `Text`: Plain text format

- `ScheduleConfigurations (hashtable)` - Required unless report is Interactive. A hashtable containing
  schedule
  configuration with the following properties:
  - `Time (datetime)`: DateTime object
    specifying when to run the task (required)
  - `RunDuration (number)`: Number of hours to
    run the task (optional)
  - `Weekly (array)`: Array of weekdays
    (optional)
  - `Monthly (array)`: Array of days of month,
    use `-1` for last day (optional)

- `PassThru (boolean)` - Optional. If set to true, returns the modified report object.

##### Report-Specific Parameters

- `FileScreenAuditDaysSince (number)` - Optional. For FileScreenAuditFiles reports, specifies how many
  days back
  to include audit events.
- `FileScreenAuditUser (array)` - Optional. For FileScreenAuditFiles reports, specifies an array
  of user
  accounts to include in the report. Only file screening
  violations by these
  users will be included.
- `FileGroupIncluded (array)` - Optional. For FilesByFileGroup reports, specifies which file
  groups to
  include.
- `FileOwnerFilePattern (string)` - Optional. For FilesByOwner reports, specifies a file pattern
  to filter
  results.
- `PropertyName (string)` - Optional. For FilesByProperty reports, specifies the
  classification
  property to group by.
- `FolderPropertyName (string)` - Optional. For FoldersByProperty reports, specifies the folder
  property to
  group by.
- `PropertyFilePattern (string)` - Optional. For FilesByProperty and FoldersByProperty, specifies
  a file
  pattern to filter results.
- `LargeFileMinimum (number)` - Optional. For LargeFiles reports, specifies the minimum file
  size in
  bytes.
- `LargeFilePattern (string)` - Optional. For LargeFiles reports, specifies a file pattern to
  filter
  results.
- `LeastAccessedMinimum (number)` - Optional. For LeastRecentlyAccessed reports, specifies the
  minimum number
  of days since last access.
- `LeastAccessedFilePattern (string)` - Optional. For LeastRecentlyAccessed reports, specifies a file
  pattern to
  filter results.
- `MostAccessedMaximum (number)` - Optional. For MostRecentlyAccessed reports, specifies the
  maximum number
  of days since last access.
- `MostAccessedFilePattern (string)` - Optional. For MostRecentlyAccessed reports, specifies a file
  pattern to
  filter results.
- `QuotaMinimumUsage (number)` - Optional. For QuotaUsage reports, specifies the minimum quota
  usage
  percentage to include.

##### Examples:

1. Update schedule and format for an existing report.

```
$schedule = @{
    Time = ("3:00 AM")
    Monthly = @(1)
}
$reportFormats = @("HTML", "CSV")

Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ArgumentList @($schedule, $reportFormats) -ScriptBlock {
    param($schedule, $reportFormats)
    Set-FSxFSRMStorageReport -Name "Monthly Report" -ScheduleConfigurations $schedule -ReportFormat $reportFormats -PassThru
}

```

### Report Execution Commands

#### Start-FSxFSRMStorageReport

##### Parameters

- `Name (array)` - Required. An array of report names to start.
- `Queue (boolean)` - Optional. If set to true, adds the report to a queue to run
  within the
  next 5 minutes. Any reports queued during this period will run
  together. If
  set to false or not specified, the report starts immediately.
- `RunDuration (number)` - Optional. Specifies how many hours the report should run
  before being
  canceled. Valid values: `-1` to `2147483`. Special values:

      + `0`: Run to completion
      + `-1`: Run until canceled

  If not specified, runs to completion.

##### Examples

1. Start a storage report immediately.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Start-FSxFSRMStorageReport -Name "Monthly Report"
}

```

2. Queue a storage report with a
   duration limit.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Start-FSxFSRMStorageReport -Name "Quarterly Report" -Queue: $true -RunDuration 4
}

```

#### Stop-FSxFSRMStorageReport

##### Parameters

- `Name (array)` - Required. An array of report names to stop.

##### Examples:

1. Stop a single storage report.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Stop-FSxFSRMStorageReport -Name "Monthly Report"
}

```

#### Wait-FSxFSRMStorageReport

##### Parameters

- `Name (array)` - Required. An array of report names to wait for.
- `Timeout (number)` - Optional. Specifies how long to wait, in seconds, for the
  reports to
  complete. If the timeout expires before reports finish, the
  command returns
  but report generation continues running in the background. Valid
  values: `-1`
  to `2147483`. Special values:
  - `-1`: Wait indefinitely until reports
    complete (default)
  - `0`: Check the current status and return
    immediately without waiting

##### Examples:

1. Wait indefinitely for a storage report to complete.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Wait-FSxFSRMStorageReport -Name "Monthly Report"
}

```
