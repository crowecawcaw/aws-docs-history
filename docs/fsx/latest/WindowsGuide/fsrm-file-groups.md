# File Groups

File groups define logical collections of file name patterns that you must use when
configuring [file screens](fsrm-file-screening.md "fsrm-file-screening.md"), and that you can optionally use when generating [storage reports](fsrm-storage-reports.md "fsrm-storage-reports.md"). A
file group contains include patterns (files to match) and exclude patterns (files to exclude
from matches), which you reference by the file group name rather than specifying individual
patterns each time.

## How file groups are used

File groups are required for the following FSRM features:

- **File screens** - You must specify one or more
  file groups to define which file types to block or monitor.
- **File screen exceptions** - You must specify one
  or more file groups to define which file types to allow despite blocking file
  screens in parent folders.
- **File screen templates** - You must specify one
  or more file groups to define which file types the template will block or
  monitor.

File groups are optional for the following FSRM features:

- **Storage reports** - You can optionally filter
  reports by file group to analyze storage usage for specific file types. For
  example, you can generate a report showing only audio and video files.

## File name patterns

File groups use wildcard patterns to match file names. You can specify both include
patterns (files to match) and exclude patterns (files to exclude from matches).

FSRM supports the following wildcards:

- **Asterisk (\*)** - Matches zero or more
  characters
- **Question mark (?)** - Matches exactly one
  character

For example, the pattern `*.doc*` matches files like `report.doc`
, `report.docx`, and `document.doc`, while the exclude pattern `~$*` excludes temporary files created by Microsoft Office applications.

## Default file groups

When you enable FSRM on your file system, the following file groups are created
automatically:

**Audio and Video Files**

Matches common audio and video file formats including `*.mp3`, `*.wav`, `*.avi`, `*.mp4`, `*.mpeg`,
and `*.wmv`

**Backup Files**

Matches backup file formats including `*.bak`, `*.backup`,
and `*.old`

**Compressed Files**

Matches archive and compressed file formats including `*.zip`, `*.rar`, `*.7z`, `*.gz`, and `*.tar`

**E-mail Files**

Matches email message and mailbox formats including `*.eml`, `*.msg`, and `*.pst`

**Executable Files**

Matches executable and script file formats including `*.exe`, `*.dll`, `*.com`, `*.bat`, `*.cmd`,
and `*.vbs`

**Image Files**

Matches common image file formats including `*.jpg`, `*.jpeg`, `*.png`, `*.gif`, `*.bmp`,
and `*.tif`

**Office Files**

Matches Microsoft Office document formats including `*.doc`, `*.docx`, `*.xls`, `*.xlsx`, `*.ppt`,
and `*.pptx`

**System Files**

Matches Windows system file formats including `*.sys`, `*.dll`, `*.ocx`, and `*.drv`

**Temporary Files**

Matches temporary file formats including `*.tmp`, `*.temp`,
and `~*`

**Text Files**

Matches text-based file formats including `*.txt`, `*.log`
, `*.csv`, and `*.xml`

**Web Page Files**

Matches web content file formats including `*.html`, `*.htm`, `*.asp`, `*.aspx`, `*.php`,
and `*.js`

You can use these default file groups immediately in file screens and storage reports,
or you can modify them to match your specific requirements.

## File group management commands

FSRM provides PowerShell commands for creating and managing file groups. Use these
commands to define custom file groups that match your organization's file management
policies.

###### Note

All the examples in this page assume that you have defined the `$FSxWindowsRemotePowerShellEndpoint` variable with your file system's Windows
Remote PowerShell endpoint. You can find this endpoint in the AWS FSx console on
your file system's details page, or by using the AWS CLI `describe-file-systems` command.

### New-FSxFSRMFileGroup

Creates a file group that defines a logical collection of file name patterns.
These patterns can be used for file screens, file screen exceptions, and storage
reports.

**Parameters:**

- `Name (string)` - Required. A name for the file group.
- `Description (string)` - Optional. A description for the file
  group.
- `IncludePattern (array)` - Optional. An array of pattern
  strings that specify files to include.
- `ExcludePattern (array)` - Optional. An array of pattern
  strings that specify files to exclude.

**Examples:**

1. Create a file group for text files.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    New-FSxFSRMFileGroup -Name "My Text Files" -IncludePattern "*.txt"
}

```

2. Create a file group for source code with include and exclude patterns.

```
$includePatterns = @("*.cpp", "*.h", "*.cs", "*.py")
$excludePatterns = @("*.tmp", "*.bak")

Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ArgumentList @($includePatterns, $excludePatterns) -ScriptBlock {
    param($includePatterns, $excludePatterns)
    New-FSxFSRMFileGroup -Name "Source Code" -Description "Programming source files" -IncludePattern $includePatterns -ExcludePattern $excludePatterns
}

```

### Get-FSxFSRMFileGroup

Retrieves one or more file groups from your file system. File groups define
collections of file patterns used in file screening and reporting.

**Parameters:**

- `Name (array)` - Optional. An array of names of file groups to
  retrieve. If you don't specify a name, the command returns all file groups
  on the file system.

**Examples:**

1. Retrieve all file groups on the file system.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Get-FSxFSRMFileGroup
}

```

### Remove-FSxFSRMFileGroup

Removes one or more file groups from your file system. After removal, the file
group cannot be used in file screens or file screen exceptions.

**Parameters:**

- `Name (array)` - Required. An array of names of file groups to
  remove.
- `PassThru (boolean)` - Optional. If set to true, returns the
  removed file group object.

**Examples:**

1. Remove a single file group.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Remove-FSxFSRMFileGroup -Name "My Text Files" -PassThru
}

```

### Set-FSxFSRMFileGroup

Modifies the properties of existing file groups.

**Parameters:**

- `Name (array)` - Required. An array of names of file groups to
  modify.
- `Description (string)` - Optional. A new description for the
  file group.
- `IncludePattern (array)` - Optional. A new array of pattern
  strings that specify files to include.
- `ExcludePattern (array)` - Optional. A new array of pattern
  strings that specify files to exclude.
- `PassThru (boolean)` - Optional. If set to true, returns the
  modified file group object.

**Examples:**

1. Update the description and patterns for a file group.

```
$includePatterns = @("*.docx", "*.pdf", "*.rtf")
$excludePatterns = @("~$*", "*.tmp")

Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ArgumentList @($includePatterns, $excludePatterns) -ScriptBlock {
    param($includePatterns, $excludePatterns)
    Set-FSxFSRMFileGroup -Name "Documents" -Description "Updated document types" -IncludePattern $includePatterns -ExcludePattern $excludePatterns -PassThru
}

```
