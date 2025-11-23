# File Screening

File screening controls which types of files users can save to folders on your file
system.
File screening helps you enforce storage policies, prevent unauthorized file types, and
maintain
compliance with organizational requirements.

###### Note

File screens use file groups to define which file types to block or monitor. For more
information about creating and managing file groups, see [File Groups](fsrm-file-groups.md "fsrm-file-groups.md").

FSRM supports two types of file screens:

1. **Active file screens** - Block users from saving
   files that match the specified file groups and generate notifications when users
   attempt to save blocked files. Use active file screens when you need to enforce
   strict policies about which file types are allowed in specific folders.
2. **Passive file screens** - Monitor and log when users
   save files that match the specified file groups, but do not prevent the save
   operation. Use passive file screens when you want to track file usage patterns
   without disrupting user workflows.

## File screen templates

File screen templates provide a reusable configuration that defines file screening
settings, including which file groups to block or monitor and what notifications to
generate. After you create a file screen template, you can apply it to multiple folders
without having to reconfigure the same settings each time. When you update a file screen
template, you can optionally apply the changes to all file screens that were created
from
that template.

Using file screen templates offers several benefits:

- **Consistency** - Ensure that similar folders
  have identical file screening configurations
- **Efficiency** - Apply file screening settings to
  multiple folders quickly
- **Maintainability** - Update file screening
  settings across multiple folders by modifying the template

## File screen exceptions

File screen exceptions override file screening rules that would otherwise apply to a
folder and all its subfolders. When you create a file screen exception, you specify
which
file groups to allow despite any blocking file screens in parent folders. File screen
exceptions are useful when you need to permit specific file types in certain subfolders
while maintaining broader restrictions at higher levels of the folder hierarchy.

For example, you might block executable files across an entire share but create an
exception for a specific subfolder where administrators need to store installation
files.

## File screening notifications

When users attempt to save files that are blocked by an active file screen, FSRM can
generate notifications to alert administrators or provide information to users. You can
configure the following types of notifications:

- **Event logging** - Log an event to Amazon
  CloudWatch or Amazon Kinesis Data Firehose for monitoring and analysis. You can
  specify the event's severity level (Information, Warning, or Error) and provide
  a custom message body. Event logging is useful for tracking file screen
  violations and integrating with existing monitoring systems.
- **Storage reports** - Generate a storage usage
  report that provides detailed information about file screening activity. Storage
  reports help you identify patterns in file save attempts and make informed
  decisions about file screening policies. For more information, see [Storage Reports](fsrm-storage-reports.md "fsrm-storage-reports.md").

## File screening management

commands

You can access three families of FSx remote PowerShell commands for managing file
screens:

1. **File screen commands** - Create, retrieve,
   modify, remove, and reset individual file screens on specific folders. Use these
   commands when you need to manage file screens on a folder-by-folder basis.
2. **File screen template commands** - Create,
   retrieve, modify, and remove file screen templates that define reusable file
   screening configurations. Use these commands to establish standard file
   screening policies that you can apply across multiple folders.
3. **File screen exception commands** - Create,
   retrieve, modify, and remove file screen exceptions that override file screening
   rules in parent folders. Use these commands when you need to allow specific file
   types in certain subfolders while maintaining broader restrictions.

### List of File Screening FSx

remote
PowerShell commands

###### Note

All the examples in this page assume that you have defined the `$FSxWindowsRemotePowerShellEndpoint` variable with your file system's Windows Remote
PowerShell endpoint. You can find this endpoint in the Amazon FSx console on your file system's
details page, or by using the AWS CLI `describe-file-systems` command.

### File screen commands

#### New-FSxFSRMFileScreen

Creates a file screen that blocks users
from saving specified types of files to a folder.

**Parameters:**

- `Folder (string)` - Required. The folder path where the
  file screen will be applied.
- `Description (string)` - Optional. A description for the
  file screen.
- `IncludeGroup (array)` - Optional. An array of file group
  names that specify which files to block or monitor.
- `Active (boolean)` - Optional. If set to true, creates an
  active file screen that blocks files. If set to false, creates a passive
  file screen that only monitors files. Default is true.
- `Template (string)` - Optional. The name of an existing
  file screen template to use.
- `NotificationConfigurations (array)` - Optional. An array
  of configurations for notifications when users attempt to save blocked
  files. Each configuration has the following properties:
  - `ActionType (string)`: The type of action to
    perform. You can specify the following values:
    1. `Event`: Logs an event
       to the file system's event log. When you specify Event,
       you must also specify the following properties:
       - `EventType (string)`: Information,
         Warning, or Error
       - `MessageBody (string)`: The message
         text to log with the event.

    2. `Report`: Generates a
       storage usage report. When you specify Report, you must
       also specify:
       - `ReportType (string)`: The type of
         report. You can specify the following values:
         `DuplicateFiles`, `FilesByFileGroup`, `FilesByOwner`, `FilesByProperty`, `LargeFiles`, `LeastRecentlyAccessed`, `MostRecentlyAccessed`, or `QuotaUsage`.

**Examples:**

1. Create a basic active file screen that blocks Audio Files.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    New-FSxFSRMFileScreen -Folder "share\department" -IncludeGroup "Audio and Video Files"
}

```

2. Create a file screen that blocks video files and generates an
   event
   log entry
   when a user attempts to save a video file.

```
$notifications = [System.Collections.ArrayList]@()
$eventNotification = @{
    ActionType = "Event"
    EventType = "Warning"
    MessageBody = "File screen violation detected"
}
$null = $notifications.Add($eventNotification)

Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ArgumentList $notifications -ScriptBlock {
    param($notifications)
    New-FSxFSRMFileScreen -Folder "share\projects" -IncludeGroup "Audio and Video Files" -NotificationConfigurations $Using:notifications
}

```

#### Get-FSxFSRMFileScreen

Retrieves one or more file screens from
your file system.

**Parameters:**

- `Folder (string)` - Optional. The folder path from which to
  retrieve file screens. If you don't specify a folder path, the command
  returns all file screens on the file system.

**Examples:**

1. Retrieve all file screens on the file system.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Get-FSxFSRMFileScreen
}

```

#### Set-FSxFSRMFileScreen

Modifies the properties of an existing
file screen.

**Parameters:**

- `Folder (string)` - Required. The folder path that contains
  the file screen to modify.
- `Description (string)` - Optional. A new description for
  the file screen.
- `IncludeGroup (array)` - Optional. A new array of file
  group names that define which files to block or monitor.
- `Active (boolean)` - Optional. If set to true, sets the
  file screen to active mode (blocking). If set to false, sets the file
  screen to passive mode (monitoring only). Default is true.
- `NotificationConfigurations (array)` - Optional. A new
  array of notification configurations.
- `PassThru (boolean)` - Optional. If set to true, returns
  the modified file screen object.

**Examples:**

1. Modify the description and file groups for a file screen.

```
$includeGroups = @("Audio and Video Files")
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ArgumentList $includeGroups -ScriptBlock {
    param($includeGroups)
    Set-FSxFSRMFileScreen -Folder "share\projects" -Description "Updated screen" -IncludeGroup $includeGroups
}

```

2. Set a file screen to active mode and add notifications.

```
$notifications = [System.Collections.ArrayList]@()
$eventNotification = @{
    ActionType = "Event"
    EventType = "Warning"
    MessageBody = "File screen violation detected"
}
$null = $notifications.Add($eventNotification)

Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ArgumentList $notifications -ScriptBlock {
    param($notifications)
    Set-FSxFSRMFileScreen -Folder "share\projects" -Active: $true -NotificationConfigurations $Using:notifications -PassThru
}

```

#### Remove-FSxFSRMFileScreen

Removes a file screen from a specified
folder.

**Parameters:**

- `Folder (string)` - Required. The folder path from which to
  remove the file screen.
- `PassThru (boolean)` - Optional. If set to true, returns
  the removed file screen object.

**Examples:**

1. Remove a file screen from a specific folder.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Remove-FSxFSRMFileScreen -Folder "share\projects" -PassThru
}

```

#### Reset-FSxFSRMFileScreen

Resets a file screen to match the
settings of a specified template.

**Parameters:**

- `Folder (string)` - Required. The folder path that contains
  the file screen to reset.
- `Template (string)` - Required. The name of an existing
  file screen template to apply.

**Examples:**

1. Reset a file screen to match the settings defined in a file screen
   template.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Reset-FSxFSRMFileScreen -Folder "share\department" -Template "Block Audio Files"
}

```

### File Screen Template Commands

####

Get-FSxFSRMFileScreenTemplate

The `Get-FSxFSRMFileScreenTemplate` command retrieves one or more
file screen templates from your file system.

##### Parameters

- `Name (array)` - Optional. An array of names of file screen templates to
  retrieve.
  If you don't specify a name, the command returns all file
  screen
  templates on the file system.

##### Examples

1.  Retrieve all file screen templates.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Get-FSxFSRMFileScreenTemplate
}

```

####

New-FSxFSRMFileScreenTemplate

The `New-FSxFSRMFileScreenTemplate` command creates a file screen
template that defines a reusable configuration for file screens. The template
specifies which file groups to block and what notifications to generate when
users attempt to save blocked files.

##### Parameters

- `Name (string)` - Required. A name for the file screen template.
- `Description (string)` - Optional. A description for the file screen template.
- `IncludeGroup (array)` - Optional. An array of file group names that specify which
  files to
  block or monitor.
- `Active (boolean)` - Optional. If set to true, creates an active file screen
  template
  that blocks files. If set to false, creates a passive
  template
  that
  only monitors files. Default is true.
- `NotificationConfigurations (array)` - Optional. An array of configurations for notifications
  when
  users
  attempt to save blocked files. Each configuration has the
  following
  properties:
  - `ActionType (string)`:
    The type of action to perform. You can specify the
    following values:
    1. `Event`: Logs
       an event to the file system's event log. When
       you specify Event, you must also specify the
       following properties:
       - `EventType
(string)`: Information,
         Warning, or Error
       - `MessageBody
(string)`: The message text to
         log with the event.

    2. `Report`:
       Generates a storage usage report. When you
       specify Report, you must also specify:
       - `ReportType
(string)`: The type of report.
         You can specify the following values:
         `DuplicateFiles`,
         `FilesByFileGroup`, `FilesByOwner`, `FilesByProperty`, `LargeFiles`, `LeastRecentlyAccessed`, `MostRecentlyAccessed`, or `QuotaUsage`

##### Examples

1.  Create a file screen template with notifications.

```
$notifications = [System.Collections.ArrayList]@()
$eventNotif = @{
    ActionType = "Event"
    EventType = "Warning"
    MessageBody = "Blocked file detected"
}
$null = $notifications.Add($eventNotif)

Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ArgumentList $notifications -ScriptBlock {
    param($notifications)
    New-FSxFSRMFileScreenTemplate -Name "Block Executables" -Description "Blocks executable files" -IncludeGroup "Executable Files" -Active: $true -NotificationConfigurations $Using:notifications
}

```

####

Remove-FSxFSRMFileScreenTemplate

The `Remove-FSxFSRMFileScreenTemplate` command removes one or more
file screen templates from your file system. When you remove a template, file
screens that were created from that template remain unchanged.

##### Parameters

- `Name (array)` - Required. An array of names of file screen templates to
  remove.
- `PassThru (boolean)` - Optional. If set to true, returns the removed file screen
  template
  object.

##### Examples

1.  Remove a single file screen template.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Remove-FSxFSRMFileScreenTemplate -Name "Block Executables" -PassThru
}

```

####

Set-FSxFSRMFileScreenTemplate

The `Set-FSxFSRMFileScreenTemplate` command modifies the properties
of existing file screen templates. Optionally updates file screens that were
created using the modified templates.

##### Parameters

- `Name (array)` - Required. An array of names of file screen templates to
  modify.
- `Description (string)` - Optional. A new description for the template.
- `IncludeGroup (array)` - Optional. A new array of file group names that define
  which
  files
  to block or monitor.
- `Active (boolean)` - Optional. If set to true, sets the template to active mode
  (blocking). If set to false, sets the template to passive
  mode
  (monitoring). Default is true.
- `NotificationConfigurations (array)` - Optional. A new array of notification configurations.
- `UpdateDerived (boolean)` - Optional. If set to true, updates all existing file
  screens
  created from this template, regardless of any modifications
  made
  to
  those file screens.
- `UpdateDerivedMatching (boolean)` - Optional. If set to true, updates only file screens that
  have
  not
  been modified since their creation from this template.
- `PassThru (boolean)` - Optional. If set to true, returns the modified file screen
  template object.

##### Examples

1.  Update a file screen template with new file groups.

```
$includeGroups = @("Audio and Video Files")
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ArgumentList $includeGroups -ScriptBlock {
    param($includeGroups)
    Set-FSxFSRMFileScreenTemplate -Name "Block Executables" -IncludeGroup $includeGroups
}

```

2.  Update a file screen template to active mode and update all
    derived
    file
    screens.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Set-FSxFSRMFileScreenTemplate -Name "Block Executables" -Active: $true -UpdateDerived
}

```

### File Screen Exception Commands

####

New-FSxFSRMFileScreenException

The `New-FSxFSRMFileScreenException` command creates a file screen
exception that overrides any file screening rules that would otherwise apply to
a folder and all its subfolders. This allows specific file types to be created
in the exception folder even if they are blocked by file screens in parent
folders.

##### Parameters

- `Folder (string)` - Required. The folder path where the file screen exception
  will
  be
  applied. The exception applies to this folder and all its
  subfolders.
- `Description (string)` - Optional. A description for the file screen exception.
- `IncludeGroup (array)` - Optional. An array of file group names that specify which
  files to
  allow despite any blocking file screens that would otherwise
  apply
  from parent folders.

##### Examples

1.  Create a file screen exception for a specific folder and file
    group.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    New-FSxFSRMFileScreenException -Folder "share\department" -IncludeGroup "Text Files"
}

```

2.  Create a file screen exception with multiple file groups.

```
$includeGroups = @("Audio and Video Files", "Documents")
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ArgumentList $includeGroups -ScriptBlock {
    param($includeGroups)
    New-FSxFSRMFileScreenException -Folder "share\projects" -Description "Allow media files in project folder" -IncludeGroup $includeGroups
    }

```

####

Get-FSxFSRMFileScreenException

The `Get-FSxFSRMFileScreenException` command retrieves one or more
file screen exceptions from your file system.

##### Parameters

- `Folder (string)` - Optional. The folder path from which to retrieve file
  screen
  exceptions. If you don't specify a folder path, the command
  returns
  all file screen exceptions on the file system.

##### Examples

1.  Retrieve all file screen exceptions on the file system.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Get-FSxFSRMFileScreenException
}

```

2.  Retrieve the file screen exception for a specific folder.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Get-FSxFSRMFileScreenException -Folder "share\department"
}

```

####

Remove-FSxFSRMFileScreenException

The `Remove-FSxFSRMFileScreenException` command removes a file
screen exception from a specified folder. After removal, the folder and its
subfolders will be subject to any file screening rules from parent folders that
were previously overridden by the exception.

#####

Parameters

- `Folder (string)` - Required. The folder path from which to remove the file
  screen
  exception.
- `PassThru (boolean)` - Optional. If set to true, returns the removed file screen
  exception object.

##### Examples

1.  Remove a file screen exception from a specific folder.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Remove-FSxFSRMFileScreenException -Folder "share\projects" -PassThru
}

```

####

Set-FSxFSRMFileScreenException

The `Set-FSxFSRMFileScreenException` command modifies the
properties of a file screen exception.

##### Parameters

- `Folder (string)` - Required. The folder path that contains the file screen
  exception
  to modify.
- `Description (string)` - Optional. A new description for the file screen exception.
- `IncludeGroup (array)` - Optional. A new array of file group names that define
  which
  files
  to allow despite any blocking file screens that would
  otherwise
  apply from parent folders.
- `PassThru (boolean)` - Optional. If set to true, returns the modified file screen
  exception object.

##### Examples

1.  Update the allowed file groups for a file screen exception.

```
$includeGroups = @("Audio and Video Files")
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ArgumentList $includeGroups -ScriptBlock {
    param($includeGroups)
    Set-FSxFSRMFileScreenException -Folder "share\projects" -IncludeGroup $includeGroups -PassThru
}

```
