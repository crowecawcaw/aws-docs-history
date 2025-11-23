# FSRM Settings

FSRM settings provide system-wide configuration that allows you to customize behavior and
streamline feature management. Use these settings to control how FSRM operates across your file
system and to set default values that simplify creating and configuring features like storage
reports and file screening.

## Settings categories

FSRM settings are organized into three categories:

### File screen auditing

File screen auditing records when users attempt to save files that are blocked by
active file screens. This information is essential for monitoring compliance with file
screening policies and identifying users who frequently attempt to save unauthorized
file types.

- `ReportFileScreenAuditEnable`

* This setting controls whether FSRM logs file screening violations at all.
  If disabled, FSRM does not record file screen violations, and
  `FileScreenAuditFiles` reports will have no data to display. You must enable
  this setting to use file screen audit reports.

- `ReportFileScreenAuditDaysSince`

* This setting provides the default time range for file screen audit
  reports. When you create a `FileScreenAuditFiles` report without specifying
  how far back to look, FSRM uses this value. Setting an appropriate default
  (such as 30 days) ensures that reports focus on recent violations without
  including excessive historical data.

- `ReportFileScreenAuditUser`

* This setting provides the default list of users to include in file screen
  audit reports. When you create a `FileScreenAuditFiles` report without
  specifying which users to include, FSRM uses this list. If empty, reports
  include all users by default. You can use this setting to focus reports on
  specific user groups or departments.

### Default report filters

Default report filter settings provide values that are used when you create storage
reports without specifying certain parameters. These defaults simplify report creation
and ensure consistency across similar reports.

Each report type has associated default settings:

- Large file reports -
  `ReportLargeFileMinimum` sets the default minimum file size,
  and `ReportLargeFilePattern` sets the default file pattern
  filter.
- Least accessed file reports -
  `ReportLeastAccessedMinimum` sets the default number of days
  since last access, and `ReportLeastAccessedFilePattern` sets the
  default file pattern filter.
- Most accessed file reports -
  `ReportMostAccessedMaximum` sets the default maximum number of
  days since last access, and `ReportMostAccessedFilePattern` sets
  the default file pattern filter.
- Files by owner reports -
  `ReportFileOwnerFilePattern` sets the default file pattern
  filter, and `ReportFileOwnerUser` sets the default list of users
  to include.
- Files by property reports -
  `ReportPropertyName` sets the default classification property
  to analyze, and `ReportPropertyFilePattern` sets the default file
  pattern filter.
- Files by file group reports -
  `ReportFileGroupIncluded` sets the default list of file groups
  to include.
- Quota usage reports -
  `ReportQuotaMinimumUsage` sets the default minimum quota usage
  percentage.

When you create a report, you can override any of these defaults by specifying the
parameter explicitly in the report configuration. The global defaults only apply when
you don't specify a value.

### Report limits

Report limit settings control the maximum number of items to include in storage
reports. These limits serve two purposes:

1. Performance management - Limiting the number of items in reports prevents
   reports from taking too long to generate or consuming excessive system
   resources. Large reports that analyze millions of files can take hours to
   complete and impact system performance.
2. Report usability - Reports with thousands of entries are difficult to review
   and analyze. Report limits ensure that reports remain focused on the most
   relevant data.

You can set up granular control over report limits:

- Overall limits -
  `ReportLimitMaxFile` limits the total number of files in any
  report, regardless of type.
- Per-report-type limits -
  Settings like `ReportLimitMaxFileGroup`, `ReportLimitMaxOwner`, and `ReportLimitMaxPropertyValue`
  limit the number of groups, owners, or property values to include in
  specific report types.
- Per-group limits -
  Settings like `ReportLimitMaxFilesPerFileGroup`, `ReportLimitMaxFilesPerOwner`, and `ReportLimitMaxFilesPerPropertyValue` limit how many files to show
  within each group in the report.

When a report reaches a limit, FSRM includes the items that consume the most storage
space or are most relevant to the report type and indicates in the report that the limit
was reached.

## FSRM settings commands

You can access commands for retrieving and modifying global settings. Use these commands
to configure system-wide FSRM behavior.

### List of FSRM Settings FSx remote

PowerShell commands

###### Note

All the examples in this page assume that you have defined the `$FSxWindowsRemotePowerShellEndpoint` variable with your file system's Windows Remote
PowerShell endpoint. You can find this endpoint in the Amazon FSx console on your file system's
details page, or by using the AWS CLI `describe-file-systems` command.

### Get-FSxFSRMSetting

`Get-FSxFSRMSetting`: Retrieves the current File Server Resource
Manager settings on your file system. Returns only the settings that can be modified
using Set-FSxFSRMSetting.

**Parameters:**

None

**Examples:**

1. Retrieve all current FSRM settings.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
Get-FSxFSRMSetting
}

```

### Set-FSxFSRMSetting

`Set-FSxFSRMSetting`: Modifies global File Server Resource Manager
settings on your file system. These settings provide default values for storage
reports and control FSRM behavior.

**Parameters:**

**File screen audit settings:**

- `ReportFileScreenAuditEnable (boolean)` - Optional. Controls whether file screening audit events are included in
  FSRM reports.
- `ReportFileScreenAuditDaysSince (number)` - Optional. The default number of days to look back for file screening
  violations when generating FileScreenAuditFiles reports.
- `ReportFileScreenAuditUser (array)` - Optional. An array of the default list of user accounts to include in
  FileScreenAuditFiles reports.

**Default report filter settings:**

- `ReportFileGroupIncluded (array)` - Optional. An array of file group names to include in reports by
  default.
- `ReportFileOwnerFilePattern (string)` - Optional. The default file pattern for files by owner reports.
  Supports wildcards (`*` and `?`).
- `ReportFileOwnerUser (array)` - Optional. An array of users in Domain\User format for files by owner
  reports.
- `ReportLargeFileMinimum (number)` - Optional. The default minimum file size in bytes for large file
  reports.
- `ReportLargeFilePattern (string)` - Optional. The default file pattern for large file reports. Supports
  wildcards (`*` and `?`).
- `ReportLeastAccessedFilePattern (string)` - Optional. The default file pattern for least accessed file reports.
  Supports wildcards (`*` and `?`).
- `ReportLeastAccessedMinimum (number)` - Optional. The default minimum number of days since last access for
  least accessed file reports.
- `ReportMostAccessedFilePattern (string)` - Optional. The default file pattern for most accessed file reports.
  Supports wildcards (`*` and `?`).
- `ReportMostAccessedMaximum (number)` - Optional. The default maximum number of days since last access for
  most accessed file reports.
- `ReportPropertyFilePattern (string)` - Optional. The default file pattern for property reports. Supports
  wildcards (`*` and `?`).
- `ReportPropertyName (string)` - Optional. The default property name for property reports.
- `ReportQuotaMinimumUsage (number)` - Optional. The default minimum quota usage percentage for quota usage
  reports.

**Report limit settings:**

- `ReportLimitMaxDuplicateGroup (number)` - Optional. The maximum number of duplicate file groups to include in
  duplicate file reports.
- `ReportLimitMaxFile (number)` - Optional. The maximum number of files to include in storage reports.
- `ReportLimitMaxFileGroup (number)` - Optional. The maximum number of file groups to include in reports.
- `ReportLimitMaxFileScreenEvent (number)` - Optional. The maximum number of file screen events to include in file
  screen audit reports.
- `ReportLimitMaxFilesPerDuplicateGroup (number)` - Optional. The maximum number of files per duplicate group in duplicate
  file reports.
- `ReportLimitMaxFilesPerFileGroup (number)` - Optional. The maximum number of files per file group in files by file
  group reports.
- `ReportLimitMaxFilesPerOwner (number)` - Optional. The maximum number of files per owner in files by owner
  reports.
- `ReportLimitMaxFilesPerPropertyValue (number)` - Optional. The maximum number of files per property value in files by
  property reports.
- `ReportLimitMaxOwner (number)` - Optional. The maximum number of owners to include in files by owner
  reports.
- `ReportLimitMaxPropertyValue (number)` - Optional. The maximum number of property values to include in files by
  property reports.
- `ReportLimitMaxQuota (number)` - Optional. The maximum number of quotas to include in quota usage
  reports.

**Other settings:**

- `PassThru (boolean)` - Optional. If set to true, returns the modified settings object.

**Examples:**

1. Configure default file screen auditing with a 30-day history.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Set-FSxFSRMSetting -ReportFileScreenAuditDaysSince 30 -PassThru
}

```

2. Configure default large file report settings.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Set-FSxFSRMSetting -ReportLargeFileMinimum 100MB -ReportLargeFilePattern "*.iso" -PassThru
}

```
