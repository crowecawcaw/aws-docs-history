# Quota Management

You can use File Server Resource Manager (FSRM) quota management to control the amount of
storage space that users consume on your FSx for Windows File Server file system. Quotas help
you manage storage capacity by limiting the amount of data that can be stored in specific
folders and by generating notifications when storage usage approaches or exceeds defined
thresholds.

## How quota management works

Quota management provides two types of quotas that you can apply to folders on your file
system:

Hard quotas

Prevent users from saving files after the quota limit is reached. When a user
attempts to save a file that would exceed the quota limit, the operation fails
and the user receives an error message.

Soft quotas

Allow users to exceed the quota limit while logging the violation. Soft quotas
are useful for monitoring storage usage without enforcing strict limits.

## Quota templates

Quota templates provide a reusable configuration that defines quota settings, including
size limits, quota type (hard or soft), and threshold notifications. After you create a
quota template, you can apply it to multiple folders without having to reconfigure the same
settings each time. When you update a quota template, you can optionally apply the changes
to all quotas that were created from that template.

Using quota templates offers several benefits:

- **Consistency** - Ensure that similar folders have
  identical quota configurations
- **Efficiency** - Apply quota settings to multiple
  folders quickly
- **Maintainability** - Update quota settings across
  multiple folders by modifying the template

## Auto apply quotas

Auto apply quotas automatically create quotas for subfolders based on a specified
template. When you create an auto apply quota on a parent folder, FSRM automatically
generates a quota for each existing subfolder and for any new subfolders that users create
in the future. This approach is useful for scenarios where you want to apply consistent
quota limits across multiple user directories or departmental folders.

## Threshold notifications

Thresholds define usage levels at which FSRM takes specific actions. You can configure
multiple thresholds for each quota, with each threshold set to a percentage of the quota
limit. When storage usage reaches a threshold percentage, FSRM can perform the following
actions:

Event logging

Log an event to Amazon CloudWatch or Amazon Kinesis Data Firehose for
monitoring and analysis. You can specify the event severity level (Information,
Warning, or Error) and provide a custom message body. Event logging is useful
for monitoring quota usage and integrating with existing monitoring systems.

Storage reports

Generate a storage usage report that provides detailed information about the
files and folders consuming storage space. Storage reports help you identify
which users or applications are consuming the most storage and make informed
decisions about storage management. For more information, see [Storage Reports](fsrm-storage-reports.md "fsrm-storage-reports.md").

You can configure multiple thresholds with different actions for each quota. For example,
you might configure a quota with an Information event at 75 percent usage and a Warning
event at 90 percent usage.

## Quota Management commands

You can access three families of FSx remote PowerShell commands for managing Quotas:

1. **Quota commands** - Create, retrieve, modify,
   remove, and update quotas on specific folders. Use these commands when you need to
   manage quotas on a folder-by-folder basis.
2. **Quota Template commands** - Create, retrieve, and
   modify quota templates that define reusable quota configurations. Use these commands
   to establish standard quota policies that you can apply across multiple folders.
3. **Auto Quota commands** - Create, retrieve, modify,
   remove, and update auto apply quotas that automatically generate quotas for
   subfolders. Use these commands when you need to apply consistent quota limits across
   multiple subfolders without manually creating individual quotas.

### List of Quota Management FSx remote

PowerShell commands

###### Note

All the examples in this page assume that you have defined the `$FSxWindowsRemotePowerShellEndpoint` variable with your file system's Windows Remote
PowerShell endpoint. You can find this endpoint in the Amazon FSx console on your file system's
details page, or by using the AWS CLI `describe-file-systems` command.

### Quota Commands

#### New-FSxFSRMQuota

Creates a new quota on a folder. A quota limits the amount of data that users can
store in a folder. You can optionally configure the quota to generate notifications
when users exceed quota thresholds.

**Parameters:**

- `Folder (string)` - Required. The folder path where the quota will be applied.
- `Size (string)` - Required when not using a Template: The quota size limit.
- `Template (string)` - Optional. The name of an existing quota template to use. When you
  specify a template, you can only use the Description parameter; all
  other settings are inherited from the template.
- `Description (string)` - Optional. A description for the quota.
- `SoftLimit (boolean)` - Optional. If set to true, creates a soft quota that allows users to
  exceed the limit while logging violations.
- `Disabled (boolean)` - Optional. If set to true, creates the quota in a disabled state.
- `ThresholdConfigurations (array)` - Optional. An array of threshold configurations that specify actions to
  take at different usage levels. Each configuration has the following
  properties:
  - `ThresholdPercentage (number)`:
    The percentage of the quota limit at which to trigger actions.
    Enter a value between 0 and 250.
  - `Action (array)`: One or more
    actions to take when the threshold is reached. Each action has
    the following properties:
    - `ActionType`: The type
      of action to perform. You can specify the following
      values:
      1.  `Event`: Logs
          an event to the file system's event log. When
          you specify Event, you must also specify the
          following properties:
          - `EventType`:
            Information, Warning, or Error
          - `MessageBody`:
            The message text to log with the event.

      2.  `Report`:
          Generates a storage usage report.

**Examples:**

**1. Create a hard 5GB quota without using a quota template.**

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    New-FSxFSRMQuota -Folder "share\test" -Size 5GB
}
```

**2. Create soft quota with a threshold notification**

```
$thresholds = [System.Collections.ArrayList]@()
$warning = @{
    ThresholdPercentage = 75
    Action = @(
        @{
            ActionType = "Event"
            EventType = "Warning"
            MessageBody = "Quota usage has reached 75%"
        }
    )
}

$thresholds.Add($warning)

Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ArgumentList ($thresholds) -ScriptBlock {
        param($thresholds)
        New-FSxFSRMQuota -Folder "share/test" -Size 1GB -Description "Test quota" -SoftLimit -ThresholdConfigurations $Using:thresholds
}
```

#### Get-FSxFSRMQuota

Retrieves one or more quotas from your file system. The command returns details
about quota configurations, including size limits, thresholds, and current usage.

**Parameters:**

- `Folder (string)` - Optional. The folder path from which to retrieve quotas. If you don't
  specify a folder path, the command returns all quotas on the file
  system.

**Examples:**

**1. Get all existing quotas on the file system.**

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Get-FSxFSRMQuota
}

```

#### Remove-FSxFSRMQuota

Removes a quota from a specified folder on your file system.

**Parameters:**

- `Folder (string)` - Required. The folder path from which to remove the quota.
- `PassThru (boolean)` - Optional. If set to true, returns the removed quota object.

**Examples:**

**1. Remove a quota.**

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Remove-FSxFSRMQuota -Folder "share\test" -PassThru
}

```

#### Set-FSxFSRMQuota

Modifies the configuration of an existing quota.

**Parameters:**

- `Folder (string)` - Required. The folder path that contains the quota to modify.
- `Description (string)` - Optional. A new description for the quota.
- `Size (string)` - Optional. The new size limit for the quota.
- `SoftLimit (boolean)` - Optional. If set to true, changes the quota to a soft limit, allowing
  users to exceed the limit while logging violations.
- `Disabled (boolean)` - Optional. If set to true, disables the quota. If set to false, enables
  the quota.
- `ThresholdConfigurations (array)` - Optional. An array of new threshold configurations. Each threshold
  configuration has the following properties:
  - `ThresholdPercentage (number)`:
    The percentage of the quota limit at which to trigger actions.
    Enter a value between 0 and 250.
  - `Action (array)`: One or more
    actions to take when the threshold is reached. Each action has
    the following properties:
    - `ActionType`: The type
      of action to perform. You can specify the following
      values:
      1.  `Event`: Logs
          an event to the file system's event log. When
          you specify Event, you must also specify the
          following properties:
          - `EventType`:
            Information, Warning, or Error
          - `MessageBody`:
            The message text to log with the event.

      2.  `Report`:
          Generates a storage usage report.

- `PassThru (boolean)` - Optional. If set to true, returns the modified quota object.

**Examples:**

**1. Modify quota size and description.**

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Set-FSxFSRMQuota 	-Folder "share\department" 	-Size 2GB 	-Description "Updated quota for department share"
}

```

**2. Disable a Quota**

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Set-FSxFSRMQuota -Folder "share\department" -Disabled: $true
}

```

#### Update-FSxFSRMQuota

Recalculates the current usage statistics for a quota by scanning the folder to
determine the actual amount of space being used.

**Parameters:**

- `Folder (string)` - Required. The folder path that contains the quota to update.
- `PassThru (boolean)` - Optional. If set to true, returns the updated quota object.

**Examples:**

**1. Recalculates the current usage statistics for a specified
quota.**

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Update-FSxFSRMQuota -Folder "share\department" -PassThru
}

```

### Quota Template Commands

#### New-FSxFSRMQuotaTemplate

Creates a new quota template that defines a reusable configuration for quotas.

**Parameters:**

- `Name (string)` - Required. A name for the quota template.
- `Size (string)` - Required. The size limit that the quota template enforces.
- `Description (string)` - Optional. A description for the quota template.
- `SoftLimit (boolean)` - Optional. If set to true, creates a template for soft quotas that
  report usage but don't enforce the limit.
- `ThresholdConfigurations (array)` - Optional. An array of threshold configurations that specify actions to
  take at different usage levels. Each configuration has the following
  properties:
  - `ThresholdPercentage (number)`:
    The percentage of the quota limit at which to trigger actions.
    Enter a value between 0 and 250.
  - `Action (array)`: One or more
    actions to take when the threshold is reached. Each action has
    the following properties:
    - `ActionType`: The type
      of action to perform. You can specify the following
      values:
      1.  `Event`: Logs
          an event to the file system's event log. When
          you specify Event, you must also specify the
          following properties:
          - `EventType`:
            Information, Warning, or Error
          - `MessageBody`:
            The message text to log with the event.

      2.  `Report`:
          Generates a storage usage report.

**Examples:**

**1. Create hard 1 GB limit template.**

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    New-FSxFSRMQuotaTemplate -Name "1GB Hard Limit" -Size 1GB -Description "Standard 1GB hard limit template"
}

```

**2. Create a 5 GB soft limit template with a warning threshold
at 90% usage**

```
$threshold = @{
    ThresholdPercentage = 90
    Action = @(
        @{
            ActionType = "Event"
            EventType = "Warning"
            MessageBody = "Quota usage has reached 90% of the limit"
        }
    )
}

$thresholds = [System.Collections.ArrayList]@()
$thresholds.Add($threshold)

Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ArgumentList $thresholds -ScriptBlock {
    param($thresholds)

    New-FSxFSRMQuotaTemplate -Name "5GB Soft Limit" -Size 5GB -Description "5GB soft limit with 90% warning" -SoftLimit -ThresholdConfigurations $Using:thresholds
}

```

#### Get-FSxFSRMQuotaTemplate

Retrieves one or more quota templates from your file system.

**Parameters:**

- `Name (string)` - Optional. The name of a specific quota template to retrieve. If you
  don't specify a name, the command returns all quota templates.

**Examples:**

**1. Retrieve all quota templates on the file system.**

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Get-FSxFSRMQuotaTemplate
}

```

#### Set-FSxFSRMQuotaTemplate

Modifies the properties of a quota template.

**Parameters:**

- `Name (string)` - Required. The name of the quota template to modify.
- `Description (string)` - Optional. A new description for the template.
- `Size (string)` - Optional. The new size limit for the template.
- `SoftLimit (boolean)` - Optional. If set to true, changes the template to create soft quotas
  that report usage but don't enforce the limit.
- `ThresholdConfigurations (array)` - Optional. An array of threshold configurations that specify actions to
  take at different usage levels. Each configuration has the following
  properties:
  - `ThresholdPercentage (number)`:
    The percentage of the quota limit at which to trigger actions.
    Enter a value between 0 and 250.
  - `Action (array)`: One or more
    actions to take when the threshold is reached. Each action has
    the following properties:
    - `ActionType`: The type
      of action to perform. You can specify the following
      values:
      1.  `Event`: Logs
          an event to the file system's event log. When
          you specify Event, you must also specify the
          following properties:
          - `EventType`:
            Information, Warning, or Error
          - `MessageBody`:
            The message text to log with the event.

      2.  `Report`:
          Generates a storage usage report.

- `UpdateDerived (boolean)` - Optional. If set to true, updates all quotas that were created from
  this template.
- `UpdateDerivedMatching (boolean)` - Optional. If set to true, updates only quotas that were created from
  this template and have not been modified since creation.
- `PassThru (boolean)` - Optional. If set to true, returns the modified template object.

**Examples:**

**1. Modifies the size and description of a quota template.**

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Set-FSxFSRMQuotaTemplate -Name "5GB Soft Limit" -Size 10GB -Description "Updated to 10GB soft limit"
}

```

**2. Modifies a quota template and updates all quotas that were
created from the template.**

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Set-FSxFSRMQuotaTemplate -Name "1GB Hard Limit" -Size 2GB -UpdateDerived
}

```

#### Reset-FSxFSRMQuota

Resets a quota to match the settings of a specified template.

#### Parameters

- `Folder (string)` - Required. The folder path that contains the
  quota to reset.
- `Template (string)` - Required. The name of the quota template
  to apply.

#### Examples

**Examples: Reset a quota to match the settings defined in a
quota template.**

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Reset-FSxFSRMQuota -Folder "share\department" -Template "1GB Hard Limit"
}

```

### Auto Quota Commands

#### New-FSxFSRMAutoQuota

The `New-FSxFSRMAutoQuota` command creates an auto apply quota on a
specified folder. An auto apply quota automatically generates quotas based on the
specified template for each existing subfolder and any new subfolders created in the
specified folder.

##### Parameters

- `Folder (string)` - Required. The folder path where the
  auto apply quota will be created.
- `Template (string)` - Optional. The name of an existing
  quota template to use for the auto apply quota.
- `Disabled (boolean)` - Optional. If set to true, creates
  the auto apply quota in a disabled state.

##### Examples

**1. Create an auto apply quota that automatically applies a
specified template to all subfolders.**

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    New-FSxFSRMAutoQuota -Folder "share\department" -Template "250 MB Extended Limit"
}

```

#### Get-FSxFSRMAutoQuota

The `Get-FSxFSRMAutoQuota` command retrieves one or more auto apply
quotas from your file system.

##### Parameters

- `Folder (string)` - Optional. The folder path from which to
  retrieve auto apply quotas. You can also use `...` at the end
  of the path to include all subfolders.

If you don't specify a folder path, the command returns all auto apply quotas
on the file system.

##### Examples

**1. Retrieve all auto apply quotas on the file system.**

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Get-FSxFSRMAutoQuota
}

```

#### Remove-FSxFSRMAutoQuota

The `Remove-FSxFSRMAutoQuota` command removes an auto-apply quota from
a specified folder. When you remove an auto apply quota, the command also removes
all quotas from subfolders that were derived from the associated quota template.

##### Parameters

- `Folder (string)` - Required. The folder path from which to
  remove the auto apply quota.
- `PassThru (boolean)` - Optional. If set to true, returns
  the removed auto apply quota object.

##### Examples

**1. Remove an auto apply quota from a specific folder.**

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Remove-FSxFSRMAutoQuota -Folder "share\department" -PassThru
}

```

#### Set-FSxFSRMAutoQuota

The `Set-FSxFSRMAutoQuota` command modifies the configuration settings
of an auto apply quota.

##### Parameters

- `Folder (string)` - Required. The folder path that contains
  the auto apply quota to modify.
- `Template (string)` - Optional. The name of a quota
  template to apply.
- `Disabled (boolean)` - Optional. If set to true, disables
  the auto apply quota. If set to false, enables the auto apply quota.
- `UpdateDerived (boolean)` - Optional. If set to true,
  updates all existing quotas that were derived from this auto apply
  quota.
- `UpdateDerivedMatching (boolean)` - Optional. If set to
  true, updates only derived quotas that have not been modified since
  creation.
- `PassThru (boolean)` - Optional. If set to true, returns
  the modified auto apply quota object.

##### Examples

**1. Change the quota template used by an auto apply quota.**

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Set-FSxFSRMAutoQuota -Folder "share\department" -Template "100 MB Limit"
}

```

**2. Disable an auto apply quota and update all quotas that
were derived from it.**

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Set-FSxFSRMAutoQuota -Folder "share\department" -Disabled: $true -UpdateDerived
}

```

#### Update-FSxFSRMAutoQuota

The `Update-FSxFSRMAutoQuota` command recalculates the properties of an
auto apply quota and the quotas that are derived from it by scanning the folder to
determine the actual amount of space being used.

##### Parameters

- `Folder (string)` - Required. The folder path that contains
  the auto apply quota to update.
- `PassThru (boolean)` - Optional. If set to true, returns
  the updated auto apply quota object.

##### Examples

**1. Recalculate the usage statistics and return the updated
auto apply quota object.**

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Update-FSxFSRMAutoQuota -Folder "share\department" -PassThru
}

```
