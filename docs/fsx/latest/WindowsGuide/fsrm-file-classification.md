# File Classification

File classification automatically assigns metadata properties to files based on their content, location, or other attributes. Classification helps you organize files, enforce data management policies, and meet compliance requirements by identifying files that contain sensitive information, belong to specific business categories, or require retention periods.

## How file classification works

File classification uses a three-step process:

1. **Define properties** - Create classification
   property definitions that specify the types of metadata you want to assign to
   files, such as `"Data Sensitivity"` or `"ContainsPII"`.
2. **Create rules** - Configure classification rules
   that automatically assign property values to files based on criteria you
   specify, such as file content patterns or folder locations. For example, files
   that contain a pattern such as a Social Security Number `(XXX-XX-XXXX)` can be
   automatically classified as `ContainsPII=Yes`.
3. **Run classification** - Execute the
   classification process to scan files and apply the rules. You can run
   classification manually on demand, on a schedule, or continuously in the
   background.

After classification is completed, you can use the assigned properties to generate
storage
reports, apply [File Management Tasks](fsrm-file-management.md "fsrm-file-management.md"), or search for files with specific characteristics.

## Classification property

definitions

Classification property definitions specify the types of metadata that can be assigned
to
files. Each property definition has a name, a property type, and optionally a list of
allowed values. For example, you might create a property called `"Data Sensitivity"` with
an
`OrderedList` Type and possible values: `Public`, `Internal`, `Confidential`, and `Restricted`.

The following property types are supported:

- `OrderedList` - An ordered list where values have a specific sequence (for example, Low,
  Medium, High). Use this type when the order of values matters for reporting
  or
  policy decisions.
- `MultiChoice` - Allows multiple values to be selected from a list (for example, a file
  might
  be tagged with both "Financial" and "Legal" categories).
- `SingleChoice` - Allows only one value to be selected from a list.
- `String` - A single text value with no predefined options.
- `MultiString` - Multiple text values with no predefined options.
- `Integer` - A numeric value.
- `YesNo` - A boolean value (true or false).
- `DateTime` - A date and time value.

Property definitions are reusable across multiple classification rules. After you
create a
property definition, you can reference it in any classification rule that needs to
assign
values for that property.

## Classification rules

Classification rules define the logic for automatically assigning property values to
files. Each rule specifies:

- Which property to set
- What value to assign to that property
- Where to apply the rule (which folders)
- How to identify files that should receive the property value. You can use two classification mechanisms:

### Content Classifier

Content Classifier scans file content for specific text patterns or regular
expressions. Use this mechanism to identify files based on what they contain.
Content
Classifier provides three ways to match file content:

- `ContentString` - Searches for case-insensitive text strings. Use this option when you
  want
  to find specific words or phrases regardless of capitalization. For
  example,
  searching for "confidential" will match "Confidential", "CONFIDENTIAL",
  and
  "confidential".
- `ContentStringCaseSensitive` - Searches for case-sensitive text strings. Use this option when
  capitalization matters for your search. For example, searching for "SSN"
  will match "SSN" but not "ssn" or "Ssn". This is useful for acronyms,
  product codes, or other identifiers where case is significant.
- `ContentRegularExpression` - Searches for patterns using regular expressions. Use this option when
  you
  need to match complex patterns or variable formats. For example, you can
  use
  regular expressions to detect:
  - Social Security numbers in the format 123-45-6789: `\b\d{3}-\d{2}-\d{4}\b`
  - Credit card numbers with optional spaces or dashes: `\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b`
  - Email addresses, phone numbers, or other structured data

You can specify multiple strings or patterns in a single rule and files will be
classified if their content matches any of the specified values.

### Folder Classifier

Folder Classifier assigns property values based on where files are stored. Use
this
mechanism to classify files by their location in the folder hierarchy. For example:

- Set a retention period property for all files in the Legal Documents
  folder
- Mark all files in a specific project folder with a project identifier

Additionally, you can use the `ReevaluateProperty` parameter to control what happens
when
classification runs on a file that already has a value for the property. You can select
the
following configurations:

- `Never` - Only classify files that don't have a value for this property
- `Overwrite` - Replace existing values when files change
- `Aggregate` - Combine new values with existing values (for multi-value properties)

## Management properties

Management properties are classification properties that apply to folders instead of
files. You use management properties to organize and categorize folders in your file
system hierarchy. Unlike file properties that are assigned automatically through
classification rules, you set management properties manually using the `Set-FSxFSRMMgmtProperty` command.

To classify folders, use the `FolderUsage_MS` property. You can specify the following
values:

- `User Files`
- `Group Share`
- `Application Files`
- `Backup and Archival`

## Running classification

You can run file classification in three ways:

1. **Manual classification** - Use
   [Start-FSxFSRMClassification](#start-fsxfsrmclassification "#start-fsxfsrmclassification") to run classification immediately. This
   approach is useful for testing new rules or performing one-time classification
   tasks.
2. **Scheduled classification** - Use
   [Set-FSxFSRMClassification](#set-fsxfsrmclassification "#set-fsxfsrmclassification") to configure a schedule for automatic
   classification. You can schedule classification to run weekly or monthly at
   specific times. Scheduled classification is appropriate for most production
   environments where you want regular, predictable classification runs.
3. **Continuous classification** - Use
   [Set-FSxFSRMClassification](#set-fsxfsrmclassification "#set-fsxfsrmclassification") with the `Continuous` parameter to enable
   background classification that runs continuously. Continuous classification
   automatically classifies new and modified files shortly after they're created or
   changed. This approach provides the most up-to-date classification but consumes
   more system resources.

When you start classification, you can specify a `RunDuration` to limit how long the
process
runs. If classification doesn't complete within the specified time, it stops and resumes
during the next scheduled run or when you manually start it again.

After classification completes, you can view the classification properties assigned to
files by right clicking a file in Windows File Explorer, selecting **Properties**, and
choosing
the **Classification** tab. This tab displays all classification properties and their values
for
the file.

## Classification process

management

You can monitor and control the classification process with the following commands:

- [Get-FSxFSRMClassification](#get-fsxfsrmclassification "#get-fsxfsrmclassification") -
  Check the current status of classification (`Running`, `Queued`, `NotRunning`,
  or `Unknown`)
- [Stop-FSxFSRMClassification](#stop-fsxfsrmclassification "#stop-fsxfsrmclassification") -
  Stop a running or queued classification job
- [Wait-FSxFSRMClassification](#wait-fsxfsrmclassification "#wait-fsxfsrmclassification") -
  Pause script execution until classification completes or a timeout expires

Use these commands to coordinate classification with other tasks. For example, you
might
wait for classification to complete before generating a storage report that depends on
classified file properties.

## Classification best practices

Follow these best practices to ensure efficient and effective file classification.

### 1. Performance considerations

Content-based classification is resource-intensive because FSRM must read and scan
file content.

- **Test rules on a small dataset first** -
  Before applying classification rules to your entire file system, test them
  on a representative sample of files to verify they work as expected and to
  estimate how long classification will take.
- **Limit content scanning scope** -
  Content-based classification is resource-intensive because it requires
  reading file content. Use the `Namespace` parameter to limit rules to specific
  folders rather than scanning the entire file system.
- **Use folder classification when possible** -
  Folder Classifier is much faster than Content Classifier because it doesn't
  need to read file contents. When files can be classified based on their
  location, use the Folder Classifier instead of Content Classifier.
- **Schedule classification during off-peak hours**

* Run scheduled classification during periods of low system activity to
  minimize impact on user performance. Avoid running classification during
  backup windows or other maintenance tasks.

- **Set appropriate RunDuration limits** - Use
  the `RunDuration` parameter to prevent classification from running too long
  and impacting system performance. If classification doesn't complete within
  the time limit, it will resume during the next scheduled run.
- **Monitor classification performance** - Use `Get-FSxFSRMClassification` to check classification status and identify
  if classification is taking longer than expected. Long-running
  classification may indicate that rules need to be optimized or that the
  system needs more resources.

### 2. Rule design

- **Use specific regular expressions** - When
  using `ContentRegularExpression`, write patterns that are as specific as
  possible to avoid false matches. Test regular expressions thoroughly before
  deploying them in production.
- **Combine multiple patterns efficiently** -
  Instead of creating separate rules for similar patterns, combine them into a
  single rule with multiple `ContentString` or `ContentRegularExpression` values.
  This reduces the number of times FSRM needs to scan each file.
- **Exclude unnecessary folders** - Use the
  `ExcludeNamespace` parameter in `Set-FSxFSRMClassification` to
  exclude temporary directories, and other locations that don't need
  classification.

### 3. Property management

- **Plan your property schema** - Design your
  classification properties before creating rules. Consider what properties
  you need for reporting, compliance, and file management policies.
- **Document property definitions** - Use the
  Description field to explain what each property means and how it should be
  used. This helps other administrators understand your classification schema.

### 4. Ongoing maintenance

- **Review classification results regularly** -
  Generate storage reports to verify that classification is working as
  expected and that files are receiving the correct property values.
- **Update rules as needed** - As your
  organization's data management requirements change, update classification
  rules to reflect new policies or compliance requirements.
- **Clean up unused properties** - Remove
  property definitions and rules that are no longer needed to keep your
  classification configuration manageable.

## Classification management

commands

You can access four families of FSx remote PowerShell commands for managing file
classification:

1. **Property definition commands** - Create and
   manage classification property definitions that specify the types of metadata
   you can assign to files.
2. **Classification rule commands** - Create and
   manage automatic classification rules that assign property values based on file
   content or location.
3. **Management property commands** - Set and
   retrieve classification properties on folders rather than files.
4. **Classification process commands** - Start,
   stop, monitor, and configure the classification process.

### List of File

Classification FSx
remote PowerShell commands

###### Note

All the examples in this page assume that you have defined the `$FSxWindowsRemotePowerShellEndpoint` variable with your file system's Windows Remote
PowerShell endpoint. You can find this endpoint in the Amazon FSx console on your file system's
details page, or by using the AWS CLI `describe-file-systems` command.

### Property Definition Commands

####

New-FSxFSRMClassificationPropertyDefinition

`New-FSxFSRMClassificationPropertyDefinition`: Creates a
classification property definition that can be used to classify files. Property
definitions define the attributes that can be assigned to files through
classification rules.

**Parameters:**

- `Name (string)` - Required. A name for the property definition.
- `DisplayName (string)` - Optional. A display name for the property definition.
- `Description (string)` - Optional. A description for the property definition.
- `Type (string)` - Required. The type of the classification property. You can specify
  the
  following values:
  - `OrderedList`: An ordered list of possible values
  - `MultiChoice`: Multiple choice selection from possible
    values
  - `SingleChoice`: Single choice from possible values
  - `String`: Single text string
  - `MultiString`: Multiple text strings
  - `Integer`: Numeric value
  - `YesNo`: Boolean value
  - `DateTime`: Date and time value

- `PossibleValueConfigurations (array)` - Optional. An array of configurations for OrderedList, MultiChoice,
  or
  SingleChoice property types. Each configuration has the following
  properties:
  - `Name (string)`: The name of the value (required)
  - `Description (string)`: A description of the value
    (optional)

- `Parameters (array)` - Optional. An array of strings in `"name=value"` format for
  additional
  configuration.

**Examples:**

**1. Create a property list for PII data.**

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    New-FSxFSRMClassificationPropertyDefinition -Name "ContainsPII" -Type OrderedList -PossibleValueConfigurations @(
            @{ Name = "Yes" },
            @{ Name = "No" })
}

```

**2. Create an ordered list property for Data Sensitivity.**

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    New-FSxFSRMClassificationPropertyDefinition -Name "DataSensitivity" -Type OrderedList -PossibleValueConfigurations @(
            @{ Name = "Public" },
            @{ Name = "Internal" },
            @{ Name = "Confidential" },
            @{ Name = "Restricted" }
        )
}

```

####

Get-FSxFSRMClassificationPropertyDefinition

`Get-FSxFSRMClassificationPropertyDefinition`: Retrieves one or
more classification property definitions from your file system.

**Parameters:**

- `Name (array)` - Optional. An array of names of property definitions to retrieve.
  If you
  don't specify a name, the command returns all property definitions
  on the
  file system.

**Examples:**

**1. Retrieve all classification property definitions on the
file
system.**

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Get-FSxFSRMClassificationPropertyDefinition
}

```

####

Set-FSxFSRMClassificationPropertyDefinition

Modifies the properties of an existing classification property definition.

#####

Parameters

- `Name (array)` - Required. An array of property names to modify.
- `DisplayName (string)` - Optional. A new display name for the property definition.
- `Description (string)` - Optional. A new description for the property definition.
- `PossibleValueConfigurations (array)` - Optional. A new array of configurations for OrderedList,
  MultiChoice,
  or SingleChoice properties. Each configuration has the following
  properties:
  - `Name (string)`: The name of the value (required)
  - `Description (string)`: A description of the value
    (optional)

- `Parameters (array)` - Optional. A new array of strings in "name=value" format.
- `PassThru (boolean)` - Optional. If set to true, returns the modified property
  definition
  object.

**Examples:**

1. Update possible values with descriptions on an existing Property
   Definition.

```
$values = [System.Collections.ArrayList]@()
$null = $values.Add(@{
    Name = "High"
    Description = "High Risk Content"
})
$null = $values.Add(@{
    Name = "Medium"
    Description = "Medium Risk Content"
})

Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ArgumentList $values -ScriptBlock {
    param($values)
    Set-FSxFSRMClassificationPropertyDefinition -Name "RiskLevel" -PossibleValueConfigurations $Using:values -PassThru
}

```

####

Remove-FSxFSRMClassificationPropertyDefinition

Removes one or more classification property definitions from your file system.
Only
locally defined property definitions can be removed.

#####

Parameters

- `Name (array)` - Required. An array of property names to remove.
- `PassThru (boolean)` - Optional. If set to true, returns the removed property
  definition
  object.

**Examples:**

1.  Remove a single property definition.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Remove-FSxFSRMClassificationPropertyDefinition -Name "RiskLevel" -PassThru
}

```

### Classification Rule Commands

#### New-FSxFSRMClassificationRule

Creates an automatic classification rule that assigns property values to files
based on
specified criteria. Each rule sets a value for a single property.

##### Parameters

- `Name (string)` - Required. A name for the classification rule.
- `Description (string)` - Optional. A description for the classification rule.
- `Property (string)` - Required. The name of the classification property to set. Must
  be an
  existing property definition name.
- `PropertyValue (string)` - Optional. The value to assign to the property. Must be valid
  for the
  specified classification mechanism.
- `Namespace (array)` - Required. An array of paths or folder types where the rule
  applies.
- `Disabled (boolean)` - Optional. If set to true, creates the rule in a disabled
  state.
- `ReevaluateProperty (string)` - Optional. Specifies when to re-evaluate files. You can specify
  the
  following values:
  - `Never`: Only evaluate files without existing property
    value
  - `Overwrite`: Re-evaluate when files change and overwrite
    existing
    value
  - `Aggregate`: Re-evaluate when files change and combine
    with existing
    value

- `Flags (array)` - Optional. Specifies special behaviors for the rule. You can
  specify the
  following values:
  - `ClearAutomaticallyClassifiedProperty`
  - `ClearManuallyClassifiedProperty`
  - `Deprecated`

- `ContentRegularExpression (array)` - Optional. An array of regular expressions to match file
  content.
- `ContentString (array)` - Optional. An array of case-insensitive strings to search for
  in file
  content.
- `ClassificationMechanism (string)` - Required. The mechanism to use for classifying files. You can
  specify the
  following values:
  - `Content Classifier`: Scans file content for specific
    strings or
    regular expression patterns. When you specify Content
    Classifier,
    you can use the ContentString,
    ContentStringCaseSensitive, or
    ContentRegularExpression parameters to define the
    content to search
    for.
  - `Folder Classifier`: Classifies files based on their
    folder location

- `Parameters (array)` - Optional. An array of `"name=value"` strings for additional
  configuration.

**Examples:**

1.  Detect Social Security Numbers using a Regular Expression.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    New-FSxFSRMClassificationRule -Name "Detect_SSN" -Property "ContainsPII" -PropertyValue "Yes" -Namespace "share" -ClassificationMechanism "Content Classifier" -ContentRegularExpression "\b\d{3}-\d{2}-\d{4}\b"
}

```

2.  Detect Credit Card Numbers using a regular Expression.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    New-FSxFSRMClassificationRule -Name "Detect_CreditCard" -Property "ContainsPII" -PropertyValue "Yes" -Namespace "share" -ClassificationMechanism "Content Classifier" -ContentRegularExpression "\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b"
}

```

3.  Classify every file under a folder with a 7-year retention period
    Property.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    New-FSxFSRMClassificationRule -Name "Contracts_Records_7Year" -Property "RetentionPeriod" -PropertyValue "7 years" -Namespace "share/Legal Documents" -ClassificationMechanism "Folder Classifier"
}

```

#### Get-FSxFSRMClassificationRule

Retrieves one or more classification rules from your file system.

##### Parameters

- `Name (array)` - Optional. An array of names of classification rules to
  retrieve. If you
  don't specify a name, the command returns all rules on the file
  system.

**Examples:**

1.  Retrieve all classification rules on the file system.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Get-FSxFSRMClassificationRule
}

```

#####

Set-FSxFSRMClassificationRule

Modifies the properties of existing classification rules.

##### Parameters

- `Name (array)` - Required. An array of names of classification rules to
  modify.
- `Description (string)` - Optional. A new description for the rule.
- `Property (string)` - Optional. The name of the classification property to set.
- `PropertyValue (string)` - Optional. A new value to assign to the property.
- `Namespace (array)` - Optional. A new array of paths or folder types where the
  rule applies.
- `Disabled (boolean)` - Optional. If set to true, disables the rule. If set to
  false, enables
  the rule.
- `ReevaluateProperty (string)` - Optional. Changes when to re-evaluate files. You can
  specify the
  following values:
  - `Never`: Only evaluate files without existing
    property value
  - `Overwrite`: Re-evaluate when files change and
    overwrite
    existing value
  - `Aggregate`: Re-evaluate when files change and
    combine with
    existing value

- `Flags (array)` - Optional. New special behaviors for the rule. You can
  specify the
  following values:
  - `ClearAutomaticallyClassifiedProperty`
  - `ClearManuallyClassifiedProperty`
  - `Deprecated`

- `ContentRegularExpression (array)` - Optional. A new array of regular expressions.
- `ContentString (array)` - Optional. A new array of case-insensitive search strings.
- `ContentStringCaseSensitive (array)` - Optional. A new array of case-sensitive search strings.
- `ClassificationMechanism (string)` - Optional. A new classification mechanism to use. You can
  specify the
  following values:
  - `Content Classifier`: Scans file content for
    specific strings or
    regular expression patterns. When you specify
    Content
    Classifier, you can use the ContentString,
    ContentStringCaseSensitive, or
    ContentRegularExpression
    parameters to define the content to search for.
  - `Folder Classifier`: Classifies files based on their
    folder
    location

- `Parameters (array)` - Optional. A new array of `"name=value"` configuration
  strings.
- `PassThru (boolean)` - Optional. If set to true, returns the modified rule
  object.

**Examples:**

1.  Update rule properties and namespace of an existing
    Classification Rule.

```
$namespaces = @("share\finance", "share\accounting")

Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ArgumentList $namespaces -ScriptBlock {
    param($namespaces)
    Set-FSxFSRMClassificationRule -Name "Detect_CreditCard" -Description "Updated PII detection" -Namespace $Using:namespaces -ReevaluateProperty "Overwrite"
}

```

#####

Remove-FSxFSRMClassificationRule

Removes one or more classification rules from your file system.

##### Parameters

- `Name (array)` - Required. An array of names of classification rules to
  remove.
- `PassThru (boolean)` - Optional. If set to true, returns the removed rule object.

**Examples:**

1.  Remove a single classification rule.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Remove-FSxFSRMClassificationRule -Name "Find Confidential Files" -PassThru
}

```

### Management Property Commands

#### Get-FSxFSRMMgmtProperty

Retrieves management properties from specified folders. Management
properties are
classification properties that apply to folders rather than files.

##### Parameters

- `Namespace (string)` - Optional. A path to a folder.
- `Name (string)` - Optional. The name of a management property to retrieve.
  If you don't
  specify a name, the command retrieves all management
  properties.
- `Recurse (boolean)` - Optional. If set to true, retrieves management properties
  for all
  folders within the namespace. Requires the Namespace
  parameter.
- `Effective (boolean)` - Optional. If set to true, retrieves the management
  property for the
  nearest folder with the specified name. The search includes
  the
  specified namespace and its parent hierarchy. Requires the
  Name
  parameter.

**Examples:**

1.  Retrieve all management properties on the file system.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Get-FSxFSRMMgmtProperty
}

```

2.  Retrieve management properties for a specific folder.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Get-FSxFSRMMgmtProperty -Namespace "share\department"
}

```

#### Remove-FSxFSRMMgmtProperty

Removes management properties from specified folders.

##### Parameters

- `Namespace (string)` - Optional. A path to a folder.
- `Name (string)` - Required. The name of the management property to remove.
- `Recurse (boolean)` - Optional. If set to true, removes management properties
  for all
  folders within the namespace. Requires the Namespace
  parameter.

**Examples:**

1.  Remove all instances of a management property.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Remove-FSxFSRMMgmtProperty -Name "FolderUsage_MS"
}

```

2.  Remove a management property from a specific folder.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Remove-FSxFSRMMgmtProperty -Name "FolderUsage_MS" -Namespace "share\department"
}

```

#### Set-FSxFSRMMgmtProperty

Changes the value of a management property for a specified namespace.
Management
properties are classification properties that apply to folders and don't
have the Secure
flag set.

##### Parameters

- `Namespace (string)` - Optional. The folder path.
- `Name (string)` - Required. The name of the management property to modify.
  Must be an
  existing classification property that applies to folders.
- `Value (string)` - Required. The new value to assign to the management
  property.

**Examples:**

1.  Set a folder usage property.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Set-FSxFSRMMgmtProperty -Namespace "share\department" -Name "FolderUsage_MS" -Value "User Files"
}

```

### Classification Process

Commands

#### Get-FSxFSRMClassification

Retrieves the status of the running file classification process. The
status can be one of
the following values:

- `Unknown`: The classification status cannot be determined
- `NotRunning`: No classification is currently running
- `Queued`: Classification is queued to start
- `Running`: Classification is currently in progress

##### Parameters

None

**Examples:**

1.  Retrieve the current classification status.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Get-FSxFSRMClassification
}

```

#### Start-FSxFSRMClassification

Initiates the file classification process, which applies classification
rules to files and
generates a classification report.

##### Parameters

- `Queue (boolean)` - Optional. If set to true, adds the classification task to
  a queue to run
  within the next 5 minutes. Any tasks queued during this
  period will run
  together. If set to false or not specified, classification
  starts
  immediately.
- `RunDuration (number)` - Optional. Specifies how many hours the classification
  process should run
  before being canceled. Valid values: `-1` to `2147483`. Special
  values:
  - `-1`: Run until canceled
  - `0`: Run to completion
  - If not specified, runs to completion.

**Examples:**

1.  Start classification with no time limit.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Start-FSxFSRMClassification -RunDuration 0
}

```

#### Stop-FSxFSRMClassification

Stops any running or queued classification job on your file system.

##### Parameters

None

**Examples:**

1.  Stop a running classification.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Stop-FSxFSRMClassification
}

```

#### Wait-FSxFSRMClassification

Waits for the file classification process to complete. Use this command
when you need to
perform actions that depend on classification finishing, such as generating
reports based on
classified files.

##### Parameters

- `Timeout (number)` - Optional. Specifies how long to wait, in seconds, for the
  classification
  to complete. If the timeout expires before classification
  finishes, the
  command returns but classification continues running in the
  background.
  Valid values: `-1` to `2147483`. Special values:
  - `-1`: Wait indefinitely until classification
    completes (default)
  - `0`: Check the current status and return immediately
    without waiting

**Examples:**

1.  Wait indefinitely for classification to complete.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Wait-FSxFSRMClassification
}

```

#### Set-FSxFSRMClassification

Modifies the configuration settings for file classification.

##### Parameters

- `ExcludeNamespace (array)` - Optional. An array of additional folders to exclude from
  classification.
- `ScheduleConfigurations (hashtable)` - Optional. A hashtable containing schedule configuration
  with the following
  properties:
  - `Time (datetime)`: DateTime object
    specifying when to run the task (required)
  - `RunDuration (number)`: Number of hours
    to run the task (optional)
  - `Weekly (array)`: Array of weekdays
    (optional)
  - `Monthly (array)`: Array of days of
    month, use -1 for last day (optional)

- `Continuous (boolean)` - Optional. If set to true, enables continuous background
  classification.
- `PassThru (boolean)` - Optional. If set to true, returns the modified
  classification
  configuration object.

**Examples:**

1. Enable continuous classification.

```
Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ScriptBlock {
    Set-FSxFSRMClassification -Continuous $true
}

```

2. Set a weekly schedule to run classification.

```
$schedule = @{
    Time = ("12:00am")
    Weekly = @('Monday', 'Wednesday', 'Friday')
}

Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ArgumentList $schedule -ScriptBlock {
    param($schedule)
    Set-FSxFSRMClassification -ScheduleConfigurations $schedule
}

```

3. Set a monthly schedule with custom exclusions.

```
$schedule = @{
    Time = ("12:00am")
    Monthly = @(1, 15, -1) # 1st, 15th, and last day
    RunDuration = 4
}
$excludeNamespaces = @("share\folder /s")

Invoke-Command -ComputerName $FSxWindowsRemotePowerShellEndpoint -ConfigurationName FSxRemoteAdmin -ArgumentList @($schedule, $excludeNamespaces) -ScriptBlock {
    param($schedule, $excludeNamespaces)
    Set-FSxFSRMClassification -ScheduleConfigurations $schedule -ExcludeNamespace $excludeNamespaces
}

```
