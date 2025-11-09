# Use the AWSTOE component document framework for custom components

To build a component using the AWS Task Orchestrator and Executor (AWSTOE) component framework, you must
provide a YAML-based document that represents the phases and steps that apply for
the component you create. AWS services use your component when they create a new
Amazon Machine Image (AMI) or container image.

###### Topics

- [Component document workflow](#component-doc-workflow "#component-doc-workflow")
- [Component logging](#component-logging "#component-logging")
- [Input and output chaining](#document-chaining "#document-chaining")
- [Document schema and definitions](#document-schema "#document-schema")
- [Document examples](#document-example "#document-example")
- [Use variables in your custom component document](toe-user-defined-variables.md "toe-user-defined-variables.md")
- [Use conditional constructs in
  AWSTOE](toe-conditional-constructs.md "toe-conditional-constructs.md")
- [Use comparison operators in
  AWSTOE component documents](toe-comparison-operators.md "toe-comparison-operators.md")
- [Use logical operators in
  AWSTOE component documents](toe-logical-operators.md "toe-logical-operators.md")
- [Use looping constructs in
  AWSTOE](toe-looping-constructs.md "toe-looping-constructs.md")

## Component document workflow

The AWSTOE component document uses phases and steps to group related tasks, and
organize those tasks into a logical workflow for the component.

###### Tip

The service that uses your component to build an image might implement rules
about what phases to use for their build process, and when those phases are
allowed to run. This is important to consider when you design your component.

###### Phases

Phases represent the progression of your workflow through the image build
process. For example, the Image Builder service uses `build` and
`validate` phases during its _build stage_ for
the images it produces. It uses the `test` and
`container-host-test` phases during its _test stage_
to ensure that the image snapshot or container image produces the expected results
before creating the final AMI or distributing the container image.

When the component runs, the associated commands for each phase are applied
in the order that they appear in the component document.

###### Rules for phases

- Each phase name must be unique within a document.
- You can define many phases in your document.
- You must include at least one of the following phases in your
  document:
  - build – for Image Builder, this
    phase is generally used during the _build stage_.
  - validate – for Image Builder, this
    phase is generally used during the _build stage_.
  - test – for Image Builder, this
    phase is generally used during the _test stage_.

- Phases always run in the order that they are defined in the document.
  The order in which they are specified for AWSTOE commands in the AWS CLI
  has no effect.

###### Steps

Steps are individual units of work that define the workflow
within each phase. Steps run in sequential order. However, input
or output for one step can also feed into a subsequent step
as input. This is called "chaining".

###### Rules for steps

- The step name must be unique for the phase.
- The step must use a supported action (action module)
  that returns an exit code.

For a complete list of supported action modules, how
they work, input/output values, and examples, see
[Action modules supported by AWSTOE
component manager](toe-action-modules.md "toe-action-modules.md").

## Component logging

AWSTOE creates a new log folder on the EC2 instances that are
used for building and testing a new image, each time your component
runs. For container images, the log folder is stored in the container.

To assist with troubleshooting if something goes wrong during the image creation
process, the input document and all of the output files AWSTOE creates while running the
component are stored in the log folder.

The log folder name is comprised of the following parts:

1. **Log directory** – when
   a service runs a AWSTOE component, it passes in the log directory,
   along with other settings for the command. For the following
   examples, we show the log file format that Image Builder uses.
   - **Linux and macOS**: `/var/lib/amazon/toe/`
   - **Windows**:
     `$env:ProgramFiles\Amazon\TaskOrchestratorAndExecutor\`

2. **File prefix** – This is a
   standard prefix used for all components: "`TOE_`".
3. **Run time** – This is a timestamp
   in YYYY-MM-DD_HH-MM-SS_UTC-0 format.
4. **Execution ID** – This is the
   GUID that is assigned when AWSTOE runs one or more components.

Example: ``/var/lib/amazon/toe/`TOE_`2021-07-01_12-34-56_UTC-0`_`a1bcd2e3-45f6-789a-bcde-0fa1b2c3def4``

AWSTOE stores the following core files in the log folder:

###### Input files

- **document.yaml** – The
  document that is used as input for the command. After the component
  runs, this file is stored as an artifact.

###### Output files

- **application.log** – The
  application log contains timestamped debug level information from
  AWSTOE about what's happening as the component is running.
- **detailedoutput.json** –
  This JSON file has detailed information about run status, inputs,
  outputs, and failures for all documents, phases, and steps that
  apply for the component as it runs.
- **console.log** – The
  console log contains all of the standard out (stdout) and
  standard error (stderr) information that AWSTOE writes to the
  console while the component is running.
- **chaining.json** –
  This JSON file represents optimizations that AWSTOE applied
  to resolve chaining expressions.

###### Note

The log folder might also contain other temporary
files that are not covered here.

## Input and output chaining

The AWSTOE configuration management application provides a feature for chaining inputs
and outputs by writing references in the following formats:

`{{ phase_name.step_name.inputs/outputs.variable
 }}`

or

`{{ phase_name.step_name.inputs/outputs[index].variable
 }}`

The chaining feature allows you to recycle code and improve the maintainability of
the document.

###### Rules for chaining

- Chaining expressions can be used only in the inputs section of each
  step.
- Statements with chaining expressions must be enclosed in quotes. For
  example:
  - **Invalid expression**: `echo {{ phase.step.inputs.variable
}}`
  - **Valid expression**: `"echo {{ phase.step.inputs.variable
}}"`
  - **Valid expression**: `'echo {{ phase.step.inputs.variable
}}'`

- Chaining expressions can reference variables from other steps and phases
  in the same document. However, the calling service might have rules that
  require chaining expressions to operate only within the context of a single
  stage. For example, Image Builder does not support chaining from the
  _build stage_ to the _test stage_,
  as it runs each stage independently.
- Indexes in chaining expressions follow zero-based indexing. The
  index starts with zero (0) to reference the first element.

**Examples**

To refer to the source variable in the second entry of the following example step,
the chaining pattern is `{{
 build.`SampleS3Download`.inputs[1].source
 }}`.

```
phases:
  - name: 'build'
    steps:
      - name: `SampleS3Download`
        action: S3Download
        timeoutSeconds: 60
        onFailure: Abort
        maxAttempts: 3
        inputs:
          - source: 's3://`sample-bucket`/`sample1`.ps1'
            destination: 'C:\`sample1`.ps1'
          - source: 's3://`sample-bucket`/`sample2`.ps1'
            destination: 'C:\`sample2`.ps1'
```

To refer to the output variable (equal to "Hello") of the following example step,
the chaining pattern is `{{
 build.`SamplePowerShellStep`.outputs.stdout
 }}`.

```
phases:
  - name: 'build'
    steps:
      - name: `SamplePowerShellStep`
        action: ExecutePowerShell
        timeoutSeconds: 120
        onFailure: Abort
        maxAttempts: 3
        inputs:
          commands:
            - 'Write-Host "Hello"'
```

## Document schema and definitions

The following is the YAML schema for a document.

```
name: (optional)
description: (optional)
schemaVersion: "string"

phases:
  - name: "string"
    steps:
      - name: "string"
        action: "string"
        timeoutSeconds: integer
        onFailure: "Abort|Continue|Ignore"
        maxAttempts: integer
        inputs:
```

The schema definitions for a document are as follows.

| Field         | Description                                    | Type   | Required |
| ------------- | ---------------------------------------------- | ------ | -------- |
| name          | Name of the document.                          | String | No       |
| description   | Description of the document.                   | String | No       |
| schemaVersion | Schema version of the document, currently 1.0. | String | Yes      |
| phases        | A list of phases with their steps.             | List   | Yes      |

The schema definitions for a phase are as follows.

| Field | Description                     | Type   | Required |
| ----- | ------------------------------- | ------ | -------- |
| name  | Name of the phase.              | String | Yes      |
| steps | List of the steps in the phase. | List   | Yes      |

The schema definitions for a step are as follows.

| Field          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Type    | Required | Default value        |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | -------- | -------------------- |
| name           | User-defined name for the step.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | String  |          |                      |
| action         | Keyword pertaining to the module that runs the step.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | String  |          |                      |
| timeoutSeconds | Number of seconds that the step runs before failing or<br>retrying.<br>Also, supports -1 value, which indicates infinite timeout. 0<br>and other negative values are not allowed.                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Integer | No       | 7,200 sec (120 mins) |
| onFailure      | Specifies what the step should do in case of failure.<br>Valid values are as follows:<br>• **Abort** – Fails the step<br>after the maximum number of attempts, and stops running.<br>Sets status for phase and document to<br>`Failed`.<br>• **Continue** – Fails the<br>step after the maximum number of attempts, and continues<br>to run remaining steps. Sets status for phase and<br>document to `Failed`.<br>• **Ignore** – Sets the step<br>to `IgnoredFailure` after the the maximum number<br>of failed attempts, and continues to run remaining steps.<br>Sets status for phase and document to<br>`SuccessWithIgnoredFailure`. | String  | No       | Abort                |
| maxAttempts    | Maximum number of attempts allowed before failing the<br>step.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Integer | No       | 1                    |
| inputs         | Contains parameters required by the action module to run the<br>step.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Dict    | Yes      |                      |

## Document examples

The following examples show AWSTOE component documents that perform tasks
for the target operating system.

Linux

###### Example 1: Run a custom binary file

The following is an example document that downloads and runs
a custom binary file on a Linux instance.

```
name: LinuxBin
description: Download and run a custom Linux binary file.
schemaVersion: 1.0
phases:
  - name: build
    steps:
      - name: Download
        action: S3Download
        inputs:
          - source: s3://<replaceable>amzn-s3-demo-source-bucket</replaceable>/<replaceable>myapplication</replaceable>
            destination: /tmp/<replaceable>myapplication</replaceable>
      - name: Enable
        action: ExecuteBash
        onFailure: Continue
        inputs:
          commands:
            - 'chmod u+x {{ build.Download.inputs[0].destination }}'
      - name: Install
        action: ExecuteBinary
        onFailure: Continue
        inputs:
          path: '{{ build.Download.inputs[0].destination }}'
          arguments:
            - '--install'
      - name: Delete
        action: DeleteFile
        inputs:
          - path: '{{ build.Download.inputs[0].destination }}'
```

Windows

###### Example 1: Install Windows updates

The following is an example document that installs all available Windows
updates, runs a configuration script, validates the changes before the AMI
is created, and tests the changes after the AMI is created.

```
name: RunConfig_UpdateWindows
description: 'This document will install all available Windows updates and run a config script. It will then validate the changes before an AMI is created. Then after AMI creation, it will test all the changes.'
schemaVersion: 1.0
phases:
  - name: build
    steps:
      - name: DownloadConfigScript
        action: S3Download
        timeoutSeconds: 60
        onFailure: Abort
        maxAttempts: 3
        inputs:
          - source: 's3://customer-bucket/config.ps1'
            destination: 'C:\config.ps1'

      - name: RunConfigScript
        action: ExecutePowerShell
        timeoutSeconds: 120
        onFailure: Abort
        maxAttempts: 3
        inputs:
          file: '{{build.DownloadConfigScript.inputs[0].destination}}'

      - name: Cleanup
        action: DeleteFile
        onFailure: Abort
        maxAttempts: 3
        inputs:
          - path: '{{build.DownloadConfigScript.inputs[0].destination}}'

      - name: RebootAfterConfigApplied
        action: Reboot
        inputs:
          delaySeconds: 60

      - name: InstallWindowsUpdates
        action: UpdateOS

  - name: validate
    steps:
      - name: DownloadTestConfigScript
        action: S3Download
        timeoutSeconds: 60
        onFailure: Abort
        maxAttempts: 3
        inputs:
          - source: 's3://customer-bucket/testConfig.ps1'
            destination: 'C:\testConfig.ps1'

      - name: ValidateConfigScript
        action: ExecutePowerShell
        timeoutSeconds: 120
        onFailure: Abort
        maxAttempts: 3
        inputs:
          file: '{{validate.DownloadTestConfigScript.inputs[0].destination}}'

      - name: Cleanup
        action: DeleteFile
        onFailure: Abort
        maxAttempts: 3
        inputs:
          - path: '{{validate.DownloadTestConfigScript.inputs[0].destination}}'

  - name: test
    steps:
      - name: DownloadTestConfigScript
        action: S3Download
        timeoutSeconds: 60
        onFailure: Abort
        maxAttempts: 3
        inputs:
          - source: 's3://customer-bucket/testConfig.ps1'
            destination: 'C:\testConfig.ps1'

      - name: ValidateConfigScript
        action: ExecutePowerShell
        timeoutSeconds: 120
        onFailure: Abort
        maxAttempts: 3
        inputs:
          file: '{{test.DownloadTestConfigScript.inputs[0].destination}}'
```

###### Example 2: Install the AWS CLI on a Windows instance

The following is an example document that installs the AWS CLI on
a Windows instance, using the setup file.

```
name: InstallCLISetUp
description: Install &CLI; using the setup file
schemaVersion: 1.0
phases:
  - name: build
    steps:
      - name: Download
        action: S3Download
        inputs:
          - source: s3://aws-cli/AWSCLISetup.exe
            destination: C:\Windows\temp\AWSCLISetup.exe
      - name: Install
        action: ExecuteBinary
        onFailure: Continue
        inputs:
          path: '{{ build.Download.inputs[0].destination }}'
          arguments:
            - '/install'
            - '/quiet'
            - '/norestart'
      - name: Delete
        action: DeleteFile
        inputs:
          - path: '{{ build.Download.inputs[0].destination }}'
```

###### Example 3: Install the AWS CLI with the MSI installer

The following is an example document that installs the AWS CLI with
the MSI installer.

```
name: InstallCLIMSI
description: Install &CLI; using the MSI installer
schemaVersion: 1.0
phases:
  - name: build
    steps:
      - name: Download
        action: S3Download
        inputs:
          - source: s3://aws-cli/AWSCLI64PY3.msi
            destination: C:\Windows\temp\AWSCLI64PY3.msi
      - name: Install
        action: ExecuteBinary
        onFailure: Continue
        inputs:
          path: 'C:\Windows\System32\msiexec.exe'
          arguments:
            - '/i'
            - '{{ build.Download.inputs[0].destination }}'
            - '/quiet'
            - '/norestart'
      - name: Delete
        action: DeleteFile
        inputs:
          - path: '{{ build.Download.inputs[0].destination }}'
```

macOS

###### Example 1: Run a custom macOS binary file

The following is an example document that downloads and runs a custom
binary file on a macOS instance.

```
name: macOSBin
description: Download and run a binary file on macOS.
schemaVersion: 1.0
phases:
  - name: build
    steps:
      - name: Download
        action: S3Download
        inputs:
          - source: s3://<replaceable>amzn-s3-demo-source-bucket</replaceable>/<replaceable>myapplication</replaceable>
            destination: /tmp/<replaceable>myapplication</replaceable>
      - name: Enable
        action: ExecuteBash
        onFailure: Continue
        inputs:
          commands:
            - 'chmod u+x {{ build.Download.inputs[0].destination }}'
      - name: Install
        action: ExecuteBinary
        onFailure: Continue
        inputs:
          path: '{{ build.Download.inputs[0].destination }}'
          arguments:
            - '--install'
      - name: Delete
        action: DeleteFile
        inputs:
          - path: '{{ build.Download.inputs[0].destination }}'
```
