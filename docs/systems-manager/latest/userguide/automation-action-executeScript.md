AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# `aws:executeScript`

– Run a script

Runs the Python or PowerShell script provided using the specified runtime and handler.
Each `aws:executeScript` action can run up to a maximum duration of 600
seconds (10 minutes). You can limit the timeout by specifying the
`timeoutSeconds` parameter for an `aws:executeScript`
step.

Use return statements in your function to add outputs to your output payload. For
examples of defining outputs for your `aws:executeScript` action, see [Example 2:
Scripted runbook](automation-authoring-runbooks-scripted-example.md "automation-authoring-runbooks-scripted-example.md"). You can also send
the output from `aws:executeScript` actions in your runbooks to the Amazon CloudWatch Logs
log group you specify. For more information, see [Logging Automation action output with
CloudWatch Logs](automation-action-logging.md "automation-action-logging.md").

If you want to send output from `aws:executeScript` actions to CloudWatch Logs, or if
the scripts you specify for `aws:executeScript` actions call AWS API
operations, an AWS Identity and Access Management (IAM) service role (or assume role) is always required to run
the runbook.

###### Note

The `aws:executeScript` action does not support automatic throttling
retry. If your script makes AWS API calls that might be throttled, you must
implement your own retry logic in your script code.

The `aws:executeScript` action contains the following preinstalled
PowerShell Core modules:

- Microsoft.PowerShell.Host
- Microsoft.PowerShell.Management
- Microsoft.PowerShell.Security
- Microsoft.PowerShell.Utility
- PackageManagement
- PowerShellGet
  To use PowerShell Core modules that aren't preinstalled, your script must install the
  module with the `-Force` flag, as shown in the following command. The
  `AWSPowerShell.NetCore` module isn't supported. Replace
  `ModuleName` with the module you want to install.

```
Install-Module `ModuleName` -Force
```

To use PowerShell Core cmdlets in your script, we recommend using the
`AWS.Tools` modules, as shown in the following commands. Replace each
`example resource placeholder` with your own
information.

- Amazon S3 cmdlets.

```
Install-Module AWS.Tools.S3 -Force
Get-S3Bucket -BucketName `amzn-s3-demo-bucket`
```

- Amazon EC2 cmdlets.

```
Install-Module AWS.Tools.EC2 -Force
Get-EC2InstanceStatus -InstanceId `instance-id`
```

- Common, or service independent AWS Tools for Windows PowerShell cmdlets.

```
Install-Module AWS.Tools.Common -Force
Get-AWSRegion
```

If your script initializes new objects in addition to using PowerShell Core cmdlets,
you must also import the module as shown in the following command.

```
Install-Module AWS.Tools.EC2 -Force
Import-Module AWS.Tools.EC2

$tag = New-Object Amazon.EC2.Model.Tag
$tag.Key = "Tag"
$tag.Value = "TagValue"

New-EC2Tag -Resource `i-02573cafcfEXAMPLE` -Tag $tag
```

For examples of installing and importing `AWS.Tools` modules, and using
PowerShell Core cmdlets in runbooks, see [Visual design experience for Automation runbooks](automation-visual-designer.md "automation-visual-designer.md").

###### Input

Provide the information required to run your script. Replace each
`example resource placeholder` with your own
information.

###### Note

The attachment for a Python script can be a .py file or a .zip file that contains
the script. PowerShell scripts must be stored in .zip files.

YAML

```
action: "aws:executeScript"
inputs:
 Runtime: `runtime`
 Handler: "`functionName`"
 InputPayload:
  `scriptInput`: '{{`parameterValue`}}'
 Script: |-
   def `functionName`(events, context):
   ...
 Attachment: "`scriptAttachment`.zip"
```

JSON

```
{
    "action": "aws:executeScript",
    "inputs": {
        "Runtime": "`runtime`",
        "Handler": "`functionName`",
        "InputPayload": {
            "`scriptInput`": "{{`parameterValue`}}"
        },
        "Attachment": "`scriptAttachment`.zip"
    }
}
```

Runtime

The runtime language to be used for running the provided script.
`aws:executeScript` supports the runtimes in the following
table.

| Runtime name               | Runtime value for `runtime`<br>input |
| -------------------------- | ------------------------------------ |
| Python 3.10                | `python3.10`                         |
| Python 3.11                | `python3.11`                         |
| PowerShell 7.4 (`dotnet8`) | `PowerShell 7.4`                     |

Type: String

Required: Yes

###### Note

For python runtimes, the environment provides 512MB of memory and
512MB of disk space. For PowerShell runtimes, the environment provides
1024MB of memory and 512MB of disk space.

Handler

The name of your function. You must ensure the function defined in the
handler has two parameters, `events` and `context`.
The PowerShell runtime does not support this parameter.

Type: String

Required: Yes (Python) | Not supported (PowerShell)

InputPayload

A JSON or YAML object that will be passed to the first parameter of the
handler. This can be used to pass input data to the script.

Type: String

Required: No

Python

```
description: Tag an instance
schemaVersion: '0.3'
assumeRole: '{{AutomationAssumeRole}}'
parameters:
    AutomationAssumeRole:
        type: String
        description: '(Required) The Amazon Resource Name (ARN) of the IAM role that allows Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses your IAM permissions to operate this runbook.'
    InstanceId:
        type: String
        description: (Required) The ID of the EC2 instance you want to tag.
mainSteps:
  - name: tagInstance
    action: 'aws:executeScript'
    inputs:
        Runtime: "python3.11"
        Handler: tagInstance
        InputPayload:
            instanceId: '{{InstanceId}}'
        Script: |-
          def tagInstance(events,context):
            import boto3

            #Initialize client
            ec2 = boto3.client('ec2')
            instanceId = events['instanceId']
            tag = {
                "Key": "Env",
                "Value": "ExamplePython"
            }
            print(f"Adding tag {tag} to instance id {instanceId}")
            ec2.create_tags(
                Resources=[instanceId],
                Tags=[tag]
            )
            return tag
    outputs:
      - Type: String
        Name: TagKey
        Selector: $.Payload.Key
outputs:
  - tagInstance.TagKey
```

PowerShell

```
description: Tag an instance
schemaVersion: '0.3'
assumeRole: '{{AutomationAssumeRole}}'
parameters:
  AutomationAssumeRole:
    type: String
    description: (Required) The Amazon Resource Name (ARN) of the IAM role that allows Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses your IAM permissions to operate this runbook.
  InstanceId:
    type: String
    description: (Required) The ID of the EC2 instance you want to tag.
mainSteps:
  - name: tagInstance
    action: aws:executeScript
    isEnd: true
    inputs:
      Runtime: PowerShell 7.4
      InputPayload:
        instanceId: '{{InstanceId}}'
      Script: |-
        Install-Module AWS.Tools.EC2 -Force
        Import-Module AWS.Tools.EC2

        $input = $env:InputPayload | ConvertFrom-Json

        $tag = New-Object Amazon.EC2.Model.Tag
        $tag.Key = "Env"
        $tag.Value = "ExamplePowerShell"

        Write-Information "Adding tag key: $($tag.Key) and value: $($tag.Value) to instance id $($input.instanceId)"
        New-EC2Tag -Resource $input.instanceId -Tag $tag

        return $tag
    outputs:
      - Type: String
        Name: TagKey
        Selector: $.Payload.Key
outputs:
  - tagInstance.TagKey
```

Script

An embedded script that you want to run during the automation.

Type: String

Required: No (Python) | Yes (PowerShell)

Attachment

The name of a standalone script file or .zip file that can be invoked by
the action. Specify the same value as the `Name` of the document
attachment file you specify in the `Attachments` request
parameter. For more information, see [Attachments](../APIReference/API_CreateDocument.md#systemsmanager-CreateDocument-request-Attachments "../APIReference/API_CreateDocument.md#systemsmanager-CreateDocument-request-Attachments") in the _AWS Systems Manager API Reference_. If you're providing a script using an
attachment, you must also define a `files` section in the
top-level elements of your runbook. For more information, see [Schema version 0.3](documents-schemas-features.md#automation-doc-syntax-examples "documents-schemas-features.md#automation-doc-syntax-examples").

To invoke a file for Python, use the `filename.method_name`
format in `Handler`.

###### Note

The attachment for a Python script can be a .py file or a .zip file
that contains the script. PowerShell scripts must be stored in .zip
files.

When including Python libraries in your attachment, we recommend adding an
empty `__init__.py` file in each module directory. This
allows you to import the modules from the library in your attachment within
your script content. For example: `from library import
 module`

Type: String

Required: No

###### Output

Payload

The JSON representation of the object returned by your function. Up to
100KB is returned. If you output a list, a maximum of 100 items is
returned.

## Using attachments with aws:executeScript

Attachments provide a powerful way to package and reuse complex scripts, multiple
modules, and external dependencies with your `aws:executeScript` actions.
Use attachments when you need to:

- Package multiple Python modules or PowerShell scripts together.
- Reuse the same script logic across multiple runbooks.
- Include external libraries or dependencies with your scripts.
- Keep your runbook definition clean by separating complex script
  logic.
- Share script packages across teams or automation workflows.

### Attachment structure and packaging

You can attach either single files or zip packages containing multiple files.
The structure depends on your use case:

###### Single file attachments

For simple scripts, you can attach a single `.py` file
(Python) or a `.zip` file containing a single PowerShell
script.

###### Multi-module packages

For complex automation that requires multiple modules, create a zip
package with the following recommended structure:

```
my-automation-package.zip
├── main.py                    # Entry point script
├── utils/
│   ├── __init__.py           # Required for Python module imports
│   ├── helper_functions.py   # Utility functions
│   └── aws_operations.py     # AWS-specific operations
├── config/
│   ├── __init__.py
│   └── settings.py           # Configuration settings
└── requirements.txt          # Optional: document dependencies
```

###### Important

For Python packages, you must include an empty
`__init__.py` file in each directory that contains
Python modules. This allows you to import modules using standard Python
import syntax like `from utils import helper_functions`.

###### PowerShell package structure

PowerShell attachments must be packaged in zip files with the following
structure:

```
my-powershell-package.zip
├── Main.ps1                  # Entry point script
├── Modules/
│   ├── HelperFunctions.ps1   # Utility functions
│   └── AWSOperations.ps1     # AWS-specific operations
└── Config/
    └── Settings.ps1          # Configuration settings
```

### Creating runbooks with attachments

Follow these steps to create runbooks that use attachments:

1. **Upload your attachment to Amazon
   S3**

Upload your script file or zip package to an S3 bucket that your
automation role can access. Note the S3 URI for use in the next
step.

```
aws s3 cp my-automation-package.zip s3://my-automation-bucket/scripts/
```

2. **Calculate the attachment
   checksum**

Calculate the SHA-256 checksum of your attachment file for security
verification:

```
# Linux/macOS
shasum -a 256 my-automation-package.zip

# Windows PowerShell
Get-FileHash -Algorithm SHA256 my-automation-package.zip
```

3. **Define the files section in your
   runbook**

Add a `files` section at the top level of your runbook to
reference your attachment:

```
files:
  my-automation-package.zip:
    checksums:
      sha256: "your-calculated-checksum-here"
```

4. **Reference the attachment in your executeScript
   step**

Use the `Attachment` parameter to reference your uploaded
file:

```
- name: runMyScript
  action: aws:executeScript
  inputs:
    Runtime: python3.11
    Handler: main.process_data
    Attachment: my-automation-package.zip
    InputPayload:
      inputData: "{{InputParameter}}"
```

## aws:executeScript attachment examples

The following examples demonstrate different ways to use attachments with the
`aws:executeScript` action.

### Example 1: Single file attachment

This example shows how to use a single Python file as an attachment to process
EC2 instance data.

###### Attachment file: process_instance.py

Create a Python file with the following content:

```
import boto3
import json

def process_instance_data(events, context):
    """Process EC2 instance data and return formatted results."""
    try:
        instance_id = events.get('instanceId')
        if not instance_id:
            raise ValueError("instanceId is required")

        ec2 = boto3.client('ec2')

        # Get instance details
        response = ec2.describe_instances(InstanceIds=[instance_id])
        instance = response['Reservations'][0]['Instances'][0]

        # Format the response
        result = {
            'instanceId': instance_id,
            'instanceType': instance['InstanceType'],
            'state': instance['State']['Name'],
            'availabilityZone': instance['Placement']['AvailabilityZone'],
            'tags': {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
        }

        print(f"Successfully processed instance {instance_id}")
        return result

    except Exception as e:
        print(f"Error processing instance: {str(e)}")
        raise
```

###### Complete runbook

Here's the complete runbook that uses the single file attachment:

```
description: Process EC2 instance data using single file attachment
schemaVersion: '0.3'
assumeRole: '{{AutomationAssumeRole}}'
parameters:
  AutomationAssumeRole:
    type: String
    description: (Required) IAM role for automation execution
  InstanceId:
    type: String
    description: (Required) EC2 instance ID to process

files:
  process_instance.py:
    checksums:
      sha256: "abc123def456..."

mainSteps:
  - name: processInstance
    action: aws:executeScript
    inputs:
      Runtime: python3.11
      Handler: process_instance.process_instance_data
      Attachment: process_instance.py
      InputPayload:
        instanceId: '{{InstanceId}}'
    outputs:
      - Type: StringMap
        Name: InstanceData
        Selector: $.Payload

outputs:
  - processInstance.InstanceData
```

### Example 2: Multi-module package

This example demonstrates using a zip package containing multiple Python
modules for complex S3 bucket operations.

###### Package structure

Create a zip package with the following structure:

```
s3-operations.zip
├── main.py
├── utils/
│   ├── __init__.py
│   ├── s3_helper.py
│   └── validation.py
└── config/
    ├── __init__.py
    └── settings.py
```

###### main.py (entry point)

The main script that orchestrates the operations:

```
from utils.s3_helper import S3Operations
from utils.validation import validate_bucket_name
from config.settings import get_default_settings

def cleanup_s3_bucket(events, context):
    """Clean up S3 bucket based on specified criteria."""
    try:
        bucket_name = events.get('bucketName')
        max_age_days = events.get('maxAgeDays', 30)

        # Validate inputs
        if not validate_bucket_name(bucket_name):
            raise ValueError(f"Invalid bucket name: {bucket_name}")

        # Initialize S3 operations
        s3_ops = S3Operations()
        settings = get_default_settings()

        # Perform cleanup
        deleted_objects = s3_ops.delete_old_objects(
            bucket_name,
            max_age_days,
            settings['dry_run']
        )

        result = {
            'bucketName': bucket_name,
            'deletedCount': len(deleted_objects),
            'deletedObjects': deleted_objects[:10],  # Return first 10 for brevity
            'dryRun': settings['dry_run']
        }

        print(f"Cleanup completed for bucket {bucket_name}")
        return result

    except Exception as e:
        print(f"Error during S3 cleanup: {str(e)}")
        raise
```

## Troubleshooting aws:executeScript attachments

Use the following guidance to resolve common issues with
`aws:executeScript` attachments:

###### Module import errors

If you receive import errors when using multi-module packages:

- Ensure you have included an empty `__init__.py` file in
  each directory containing Python modules.
- Verify that your import statements match the actual file and directory
  structure in your zip package.
- Use relative imports (e.g., `from .utils import helper`) or
  absolute imports (e.g., `from utils import helper`)
  consistently.

###### Attachment not found errors

If your automation fails to find the attachment:

- Verify that the `Attachment` parameter value exactly matches
  the key in your `files` section.
- Check that your S3 bucket path and file name are correct in the
  `files` section.
- Ensure your automation role has `s3:GetObject` permission for
  the attachment S3 location.
- Verify that the checksum in your runbook matches the actual file
  checksum.

###### Handler function errors

If you receive handler-related errors:

- For Python: Use the format `filename.function_name` in the
  `Handler` parameter (e.g.,
  `main.process_data`).
- Ensure your handler function accepts exactly two parameters:
  `events` and `context`.
- For PowerShell: Do not specify a `Handler` parameter; the
  script runs directly.

###### Script execution failures

If your script fails during execution:

- Check the automation execution history for detailed error messages and
  stack traces.
- Use `print()` statements (Python) or
  `Write-Information` (PowerShell) to add debugging
  output.
- Verify that all required AWS permissions are granted to your automation
  role.
- Test your script logic locally before packaging it as an
  attachment.

###### Exit codes and error handling

To properly handle errors and return exit codes:

- In Python: Use `raise Exception("error message")` to indicate
  script failure.
- In PowerShell: Use `throw "error message"` or
  `Write-Error` to indicate failure.
- Return structured data from your functions to provide detailed
  success/failure information.
- Use try-catch blocks to handle exceptions gracefully and provide
  meaningful error messages.
