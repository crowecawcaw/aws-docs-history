# Common Use Cases

This topic provides step-by-step examples for common File Server Resource Manager tasks.
These examples demonstrate how to use and implement FSRM features to solve typical file
management challenges.

###### Note

All the examples in this page assume that you have defined the `$FSxWindowsRemotePowerShellEndpoint` variable with your file system's Windows Remote
PowerShell endpoint. You can find this endpoint in the Amazon FSx console on your file system's
details page, or by using the AWS CLI `describe-file-systems` command.

## Setting a hard quota on a folder

This example shows how to create a hard quota that prevents users from storing more
than 10 GB in a 'department' folder.

###### To set a quota on a folder:

1. Create a hard quota with a 10 GB limit:

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    New-FSxFSRMQuota -Folder "share\department" -Size 10GB -Description "10 GB hard limit for department folder"
}

```

2. (Optional) Modify the quota to add a threshold notification at 85% usage:

```
$thresholds = [System.Collections.ArrayList]@()
$threshold = @{
    ThresholdPercentage = 85
    Action = @(
        @{
            ActionType = "Event"
            EventType = "Warning"
            MessageBody = "Department folder has reached 85% of quota limit"
        }
    )
}

$null = $thresholds.Add($threshold)

Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ArgumentList ($thresholds) -ScriptBlock {
    param($thresholds)
    Set-FSxFSRMQuota -Folder "share\department" -ThresholdConfigurations $Using:thresholds
}

```

3. Verify the quota was created:

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Get-FSxFSRMQuota -Folder "share\department"
}

```

## Restricting specific file types using file

groups

This example shows how to block users from saving audio and video files to a business
documents folder using the default "`Audio and Video Files`" file group.

###### To restrict file types using file groups:

1. Create an active file screen that blocks audio and video files:

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
New-FSxFSRMFileScreen -Folder "share\business-documents" -IncludeGroup "Audio and Video Files" -Description "Block media files in business documents folder"
}

```

2. (Optional) Update the file screen to add a notification when users attempt to
   save blocked files:

```
$notifications = [System.Collections.ArrayList]@()

$eventNotification = @{
    ActionType = "Event"
    EventType = "Warning"
    MessageBody = "User attempted to save blocked media file"
}
$null = $notifications.Add($eventNotification)

Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ArgumentList $notifications -ScriptBlock {
    param($notifications)
    Set-FSxFSRMFileScreen -Folder "share\business-documents" -NotificationConfigurations $Using:notifications
}

```

3. Verify the file screen was created:

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Get-FSxFSRMFileScreen -Folder "share\business-documents"
}

```

## Identify and classify PII data

This example shows how to automatically identify files containing Social Security
numbers and classify them as containing personally identifiable information (PII).

###### To identify and classify PII data:

1. Create a classification property for PII:

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    New-FSxFSRMClassificationPropertyDefinition -Name "ContainsPII" -Type OrderedList -PossibleValueConfigurations @(
        @{ Name = "Yes" },
        @{ Name = "No" })
}

```

2. Create a classification rule to detect Social Security numbers:

###### Note

The following Regular Expression will search files for text with the
pattern XXX-XX-XXXX. For production use, consider using more sophisticated
patterns or combining multiple detection methods.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    New-FSxFSRMClassificationRule -Name "Detect_SSN" -Property "ContainsPII" -PropertyValue "Yes" -Namespace "share" -ClassificationMechanism "Content Classifier" -ContentRegularExpression "\b\d{3}-\d{2}-\d{4}\b"
}

```

3. Run classification:

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Start-FSxFSRMClassification
}

```

4. (Optional) Configure continuous classification to automatically classify new
   files:

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Set-FSxFSRMClassification -Continuous $true
}

```

5. Check for status (1 means completed):

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Get-FSxFSRMClassification
}

```

6. After classification completes, you can view the classification properties
   assigned to files by right-clicking a file in Windows File Explorer, selecting
   **Properties**, and choosing the **Classification** tab. This tab displays all
   classification properties and their values for the file.

## Creating a retention policy for files

This example shows how to classify files by retention period based on their folder
location, which you can then use with client-side PowerShell scripts to archive or
delete files.

###### To create a retention policy for files:

1. Create a classification property for retention period:

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    New-FSxFSRMClassificationPropertyDefinition -Name "RetentionPeriod" -Type String -Description "File retention period"
}

```

2.  Create classification rules for different retention periods:

        * 7-year retention for legal documents under the folder **Legal Documents**:



        ```
        Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
            New-FSxFSRMClassificationRule -Name "Legal_7Year" -Property "RetentionPeriod" -PropertyValue "7 years" -Namespace "share/Legal Documents" -ClassificationMechanism "Folder Classifier"
        }

        ```
        * 3-year retention for financial records under the folder **Finance**:



        ```
        Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
            New-FSxFSRMClassificationRule -Name "Finance_3Year" -Property "RetentionPeriod" -PropertyValue "3 years" -Namespace "share/Finance" -ClassificationMechanism "Folder Classifier"
        }

        ```

    You can also classify by file content and search for strings like
    "Retention Period Seven Years". To achieve this, use the
    `ClassificationMechanism "Content Classifier"` and `ContentString "Retention
 seven years"`.

3.  Run classification to apply retention properties:

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Start-FSxFSRMClassification
}

```

4. (Optional) Configure continuous classification to automatically classify new
   files:

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Set-FSxFSRMClassification -Continuous $true
}

```

5. Check for status (1 means completed):

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Get-FSxFSRMClassification
}

```

6. After classification completes, you can view the classification properties
   assigned to files by right-clicking a file in Windows File Explorer, selecting
   **Properties**, and choosing the **Classification** tab. This tab displays all
   classification properties and their values for the file.
7. Once files are classified with retention periods, you can use client-side
   PowerShell scripts to archive or delete files based on their `RetentionPeriod`
   property and age. For example, you can scan the file system and compare file's
   age with their retention period classification. For more information, see [File Management Tasks](fsrm-file-management.md "fsrm-file-management.md").

## Setting up common storage reports

This section shows how to create two commonly used storage reports: a large files
report and a files by owner report.

### Large files report

This example creates a monthly report that identifies files larger than 200 MB.

###### To create a large files report:

1. Create a scheduled large files report:

```
$schedule = @{
    Time = "2:00 AM"
    Monthly = @(1) # Run on the 1st of each month
}

Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ArgumentList $schedule -ScriptBlock {
    param($schedule)
    New-FSxFSRMStorageReport -Name "Monthly Large Files Report" -Namespace "share" -ReportType "LargeFiles" -LargeFileMinimum 200MB -ReportFormat "HTML","CSV" -ScheduleConfigurations $schedule
}

```

2. (Optional) Run the report immediately to test:

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Start-FSxFSRMStorageReport -Name "Monthly Large Files Report"
}

```

### Files by owner report

This example creates a weekly report that shows storage consumption by user.

###### To create a files by owner report:

1. Create a scheduled files by owner report:

```
$schedule = @{
    Time = "3:00 AM"
    Weekly = @('Sunday')
}

Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ArgumentList $schedule -ScriptBlock {
    param($schedule)
    New-FSxFSRMStorageReport -Name "Weekly Files by Owner Report" -Namespace "share" -ReportType "FilesByOwner" -ReportFormat "HTML","CSV" -ScheduleConfigurations $schedule
}

```

2. (Optional) Run the report immediately to test:

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Start-FSxFSRMStorageReport -Name "Weekly Files by Owner Report"
}

```

Access the generated reports by mapping the administrative D$ share. For more
information, visit [Accessing storage reports](fsrm-storage-reports.md#fsrm-storage-reports-accessing "fsrm-storage-reports.md#fsrm-storage-reports-accessing").
