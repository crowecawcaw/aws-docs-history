# Supported step actions for your workflow document

This section includes details for the step actions that Image Builder supports.

###### Terms used in this section

AMI

Amazon Machine Image

ARN

Amazon Resource Name

###### Supported actions

- [BootstrapInstanceForContainer](#wfdoc-step-action-bootstrap-container "#wfdoc-step-action-bootstrap-container")
- [CollectImageMetadata](#wfdoc-step-action-collect-image-metadata "#wfdoc-step-action-collect-image-metadata")
- [CollectImageScanFindings](#wfdoc-step-action-collect-findings "#wfdoc-step-action-collect-findings")
- [CreateImage](#wfdoc-step-action-create-img-from-inst "#wfdoc-step-action-create-img-from-inst")
- [ExecuteComponents](#wfdoc-step-action-exec-components "#wfdoc-step-action-exec-components")
- [ExecuteStateMachine](#wfdoc-step-action-exec-state-machine "#wfdoc-step-action-exec-state-machine")
- [LaunchInstance](#wfdoc-step-action-launch-instance "#wfdoc-step-action-launch-instance")
- [RegisterImage](#wfdoc-step-action-register-image "#wfdoc-step-action-register-image")
- [RunCommand](#wfdoc-step-action-run-command "#wfdoc-step-action-run-command")
- [RunSysPrep](#wfdoc-step-action-run-sysprep "#wfdoc-step-action-run-sysprep")
- [SanitizeInstance](#wfdoc-step-action-sanitize-instance "#wfdoc-step-action-sanitize-instance")
- [TerminateInstance](#wfdoc-step-action-terminate-instance "#wfdoc-step-action-terminate-instance")
- [WaitForAction](#wfdoc-step-action-waitfor "#wfdoc-step-action-waitfor")
- [WaitForSSMAgent](#wfdoc-step-action-wait-for-ssm-agent "#wfdoc-step-action-wait-for-ssm-agent")

## BootstrapInstanceForContainer

This step action runs a service script to bootstrap the instance with minimum
requirements to run container workflows. Image Builder uses the **sendCommand** in the Systems Manager API to run this
script. For more information, see [AWS Systems Manager Run
Command](../../../systems-manager/latest/userguide/execute-remote-commands.md "../../../systems-manager/latest/userguide/execute-remote-commands.md").

###### Note

The bootstrap script installs the AWS CLI and Docker packages that are prerequisites
for Image Builder to successfully build Docker containers. If you don't include this step action,
the image build could fail.

**Default Timeout:** 60 minutes

**Rollback:** There is no rollback for this
step action.

**Inputs:** The following table includes
supported inputs for this step action.

| Input name | Description                          | Type   | Required | Default | Constraints                                                                                                 |
| ---------- | ------------------------------------ | ------ | -------- | ------- | ----------------------------------------------------------------------------------------------------------- |
| instanceId | The ID of the instance to bootstrap. | String | Yes      |         | This must be the output instance ID from the workflow step that<br>launched the instance for this workflow. |

**Outputs:** The following table includes
outputs for this step action.

| Output name  | Description                                                                                          | Type   |
| ------------ | ---------------------------------------------------------------------------------------------------- | ------ |
| runCommandId | The ID of the Systems Manager \*_sendCommand_<br>• that ran the bootstrap<br>script on the instance. | String |
| status       | The status returned from the Systems Manager **sendCommand**.                                        | String |
| output       | Output returned from the Systems Manager **sendCommand**.                                            | String |

**Example**

Specify the step action in the workflow document.

```
`- name: `ContainerBootstrapStep`
 action: BootstrapInstanceForContainer
 onFailure: Abort
 inputs:
 instanceId.$: $.stepOutputs.`LaunchStep`.instanceId`
```

Use the output of the step action value in the workflow document.

```
`$.stepOutputs.`ContainerBootstrapStep`.status`
```

## CollectImageMetadata

This step action is only valid for build workflows.

EC2 Image Builder runs [AWS Systems Manager (Systems Manager)
Agent](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md") on the EC2 instances it launches to build and test your image.
Image Builder collects additional information about the instance used during the build phase
with [Systems Manager Inventory](../../../systems-manager/latest/userguide/systems-manager-inventory.md "../../../systems-manager/latest/userguide/systems-manager-inventory.md").
This information includes the operating system (OS) name and version, as well as the
list of packages and their respective versions as reported by your operating system.

###### Note

This step action only works for images that create AMIs.

**Default Timeout:** 30 minutes

**Rollback:** Image Builder rolls back any Systems Manager resources
that were created during this step.

**Inputs:** The following table includes
supported inputs for this step action.

| Input name | Description                                           | Type   | Required | Default | Constraints                                                                                                       |
| ---------- | ----------------------------------------------------- | ------ | -------- | ------- | ----------------------------------------------------------------------------------------------------------------- |
| instanceId | The build instance to apply the metadata settings to. | String | Yes      |         | This must be the output instance ID from the workflow step that<br>launched the build instance for this workflow. |

**Outputs:** The following table includes
outputs for this step action.

| Output name   | Description                                                                 | Type   |
| ------------- | --------------------------------------------------------------------------- | ------ |
| osVersion     | The operating system name and version collected from the build<br>instance. | String |
| associationId | The Systems Manager association ID used for inventory collection.           | String |

**Example**

Specify the step action in the workflow document.

```
`- name: `CollectMetadataStep`
 action: CollectImageMetadata
 onFailure: Abort
 inputs:
 instanceId: $.stepOutputs.`LaunchStep`.instanceId`
```

Use output from the step action in the workflow document.

```
`$.stepOutputs.`CollectMetadataStep`.osVersion`
```

## CollectImageScanFindings

If Amazon Inspector is enabled for your account and image scanning is enabled for
your pipeline, this step action collects image scan findings reported by Amazon Inspector
for your test instance. This step action is not available for build workflows.

**Default Timeout:** 120 minutes

**Rollback:** There is no rollback for this
step action.

**Inputs:** The following table includes
supported inputs for this step action.

| Input name | Description                                   | Type   | Required | Default | Constraints                                                                                                 |
| ---------- | --------------------------------------------- | ------ | -------- | ------- | ----------------------------------------------------------------------------------------------------------- |
| instanceId | The ID for the instance that scanning ran on. | String | Yes      |         | This must be the output instance ID from the workflow step<br>that launched the instance for this workflow. |

**Outputs:** The following table includes
outputs for this step action.

| Output name  | Description                                                                                    | Type   |
| ------------ | ---------------------------------------------------------------------------------------------- | ------ |
| runCommandId | The ID of the Systems Manager \*_sendCommand_<br>• that ran the script to<br>collect findings. | String |
| status       | The status returned from the Systems Manager **sendCommand**.                                  | String |
| output       | Output returned from the Systems Manager **sendCommand**.                                      | String |

**Example**

Specify the step action in the workflow document.

```
`- name: `CollectFindingsStep`
 action: CollectImageScanFindings
 onFailure: Abort
 inputs:
 instanceId.$: $.stepOutputs.`LaunchStep`.instanceId`
```

Use the output of the step action value in the workflow document.

```
`$.stepOutputs.`CollectFindingsStep`.status`
```

## CreateImage

This step action creates an image from a running instance with the Amazon EC2
`CreateImage` API. During the creation process, the step action
waits as necessary to verify that the resources have reached the correct state
before it continues.

**Default Timeout:** 720 minutes

**Rollback:** There is no rollback for this
step action.

**Inputs:** The following table includes
supported inputs for this step action.

| Input name | Description                                | Type   | Required | Default | Constraints                                                                                      |
| ---------- | ------------------------------------------ | ------ | -------- | ------- | ------------------------------------------------------------------------------------------------ |
| instanceId | The instance to create the new image from. | String | Yes      |         | The instance for the provided instance ID must be in<br>a `running` state when this step starts. |

**Outputs:** The following table includes
outputs for this step action.

| Output name | Description                             | Type   |
| ----------- | --------------------------------------- | ------ |
| imageId     | The AMI ID of the image that's created. | String |

**Example**

Specify the step action in the workflow document.

```
`- name: `CreateImageFromInstance`
 action: CreateImage
 onFailure: Abort
 inputs:
 instanceId.$: "i-1234567890abcdef0"`
```

Use the output of the step action value in the workflow document.

```
`$.stepOutputs.`CreateImageFromInstance`.imageId`
```

## ExecuteComponents

This step action runs components that are specified in the recipe for
the current image being built. Build workflows run build components
on the build instance. Test workflows only run test components on the test
instance.

Image Builder uses the **sendCommand** in the Systems Manager API to run
components. For more information, see [AWS Systems Manager Run
Command](../../../systems-manager/latest/userguide/execute-remote-commands.md "../../../systems-manager/latest/userguide/execute-remote-commands.md").

**Default Timeout:** 720 minutes

**Rollback:** There is no rollback for this
step action.

**Inputs:** The following table includes
supported inputs for this step action.

| Input name | Description                                                | Type   | Required | Default | Constraints                                                                                                 |
| ---------- | ---------------------------------------------------------- | ------ | -------- | ------- | ----------------------------------------------------------------------------------------------------------- |
| instanceId | The ID for the instance that the components should run on. | String | Yes      |         | This must be the output instance ID from the workflow step that<br>launched the instance for this workflow. |

**Outputs:** The following table includes
outputs for this step action.

| Output name  | Description                                                                                    | Type   |
| ------------ | ---------------------------------------------------------------------------------------------- | ------ |
| runCommandId | The ID of the Systems Manager \*_sendCommand_<br>• that ran the components<br>on the instance. | String |
| status       | The status returned from the Systems Manager **sendCommand**.                                  | String |
| output       | Output returned from the Systems Manager **sendCommand**.                                      | String |

**Example**

Specify the step action in the workflow document.

```
`- name: `ExecComponentsStep`
 action: ExecuteComponents
 onFailure: Abort
 inputs:
 instanceId: $.stepOutputs.`LaunchStep`.instanceId`
```

Use output from the step action in the workflow document.

```
`$.stepOutputs.`ExecComponentsStep`.status`
```

## ExecuteStateMachine

This step action starts execution of an AWS Step Functions state machine from an
Image Builder workflow. Image Builder uses the Step Functions `StartExecution` API to
initiate the state machine and waits for it to complete. This is useful for
integrating complex workflows, compliance validation, or certification processes
into your image building pipeline.

For more information, see [Learn about state machines
in Step Functions](../../../step-functions/latest/dg/concepts-statemachines.md "../../../step-functions/latest/dg/concepts-statemachines.md") in the _AWS Step Functions Developer Guide_.

**Default Timeout:** 6 hours

**Max Timeout:** 24 hours

**Rollback:** There is no rollback for this
step action.

**Inputs:** The following table includes
supported inputs for this step action.

| Input name      | Description                                             | Type   | Required | Default | Constraints                                        |
| --------------- | ------------------------------------------------------- | ------ | -------- | ------- | -------------------------------------------------- |
| stateMachineArn | The ARN of the Step Functions state machine to execute. | String | Yes      |         | Must be a valid state machine ARN.                 |
| input           | JSON input data to provide to the state machine.        | String | No       | {}      | Must be valid JSON string, maximum length: 16 KiB. |

**Outputs:** The following table includes
outputs for this step action.

| Output name  | Description                             | Type   |
| ------------ | --------------------------------------- | ------ |
| executionArn | The ARN of the state machine execution. | String |

**IAM permissions required**

Your custom execution role must have the following permissions to use this step action:

###### Allow actions

- `states:StartExecution`
- `states:DescribeExecution`

###### Specify resources

- `arn:aws:states:`us-west-2`:`111122223333`:stateMachine:`state-machine-name``
- `arn:aws:states:`us-west-2`:`111122223333`:execution:`state-machine-name`:*`

**Example**

Specify the step action in the workflow document.

```
`- name: `ValidateImageCompliance`
 action: ExecuteStateMachine
 timeoutSeconds: 3600
 onFailure: Abort
 inputs:
 stateMachineArn: arn:aws:states:`us-west-2`:`111122223333`:stateMachine:`ImageComplianceValidation`
 input: |
 {
 "imageId": "{{ $.stepOutputs.CreateImageFromInstance.imageId }}",
 "region": "us-west-2",
 "complianceLevel": "high",
 "requiredScans": ["cve", "benchmark", "configuration"]
 }`
```

Use the output of the step action value in the workflow document.

```
`$.stepOutputs.`ValidateImageCompliance`.executionArn`
```

## LaunchInstance

This step action launches an instance in your AWS account and waits until the
Systems Manager agent is running on the instance before moving on to the next step. The launch
action uses settings from your recipe and infrastructure configuration resources that
are associated with your image. For example, the instance type to launch comes from
the infrastructure configuration. The output is the instance ID of the instance that
it launched.

The `waitFor` input configures the condition that satisfies the
step completion requirement.

**Default Timeout:** 60 minutes

**Rollback:** For build instances, rollback
performs the action that you've configured in your infrastructure configuration
resource. By default, build instances are terminated if image creation fails.
However, there is a setting in the infrastructure configuration to keep
the build instance for troubleshooting.

**Inputs:** The following table includes
supported inputs for this step action.

| Input name            | Description                                                                                      | Type           | Required | Default                                                                             | Constraints                        |
| --------------------- | ------------------------------------------------------------------------------------------------ | -------------- | -------- | ----------------------------------------------------------------------------------- | ---------------------------------- |
| imageIdOverride       | The image to use for launching the instance                                                      | String         | No       | Build stage: Image recipe base image<br>Test stage: Output AMI from the build stage | Must be a valid AMI ID             |
| instanceTypesOverride | Image Builder tries each instance type in the list until it finds one that launches successfully | List of String | No       | Instance types specified in your Infrastructure Configuration                       | Must be valid instance types       |
| waitFor               | The condition to wait for before completing the<br>workflow step and moving on to the next step  | String         | Yes      |                                                                                     | Image Builder supports `ssmAgent`. |

**Outputs:** The following table includes
outputs for this step action.

| Output name | Description                                    | Type   |
| ----------- | ---------------------------------------------- | ------ |
| instanceId  | The instance ID of the instance that launched. | String |

**Example**

Specify the step action in the workflow document.

```
`- name: `LaunchStep`
 action: LaunchInstance
 onFailure: Abort
 inputs:
 waitFor: `ssmAgent``
```

Use output from the step action in the workflow document.

```
`$.stepOutputs.`LaunchStep`.instanceId`
```

## RegisterImage

This step action registers a new Amazon Machine Image (AMI) using the Amazon EC2 RegisterImage API. It allows you to create an AMI from an existing snapshot or set of snapshots, specifying various image attributes.

**Default Timeout:** 720 minutes

**Rollback:** There is no rollback for this step action.

**Inputs:** The following table includes supported inputs for this step action.

| Input name          | Description                                                                          | Type    | Required | Default | Constraints                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------- | ------------------------------------------------------------------------------------ | ------- | -------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| architecture        | The architecture of the AMI.                                                         | String  | No       |         | Valid values: i386, x86_64, arm64, x86_64_mac, arm64_mac                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| blockDeviceMapping  | The block device mapping entries for the AMI.                                        | Array   | No       |         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| bootMode            | The boot mode of the AMI.                                                            | String  | No       |         | Valid values: legacy-bios, uefi, uefi-preferred                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| description         | A description for the AMI.                                                           | String  | No       |         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| enaSupport          | Whether enhanced networking with ENA is enabled.                                     | Boolean | No       |         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| imageLocation       | The location of the AMI manifest.                                                    | String  | No       |         | Required for S3-backed AMIs                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| imdsSupport         | The IMDSv2 support level.                                                            | String  | No       |         | Valid values: v2.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| includeSnapshotTags | Whether to include tags from the first snapshot defined in the block device mapping. | Boolean | No       | FALSE   | When set to true, tags are included as follows:<br>• Tags from the `SnapshotId` of the first EBS volume in the `blockDeviceMapping`<br>list that contains a `SnapshotId` is merged with the AMI registration tags.<br>• AMI registration tags take precedence over snapshot tags with the same key.<br>• AWS reserved tags (those with keys starting with `aws:`) are automatically excluded.<br>• If multiple EBS volumes with `SnapshotId` are defined, only tags from the<br>first EBS volume in the list that contains a `SnapshotId` is included. |
| kernelId            | The ID of the kernel to use.                                                         | String  | No       |         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ramdiskId           | The ID of the RAM disk to use.                                                       | String  | No       |         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| rootDeviceName      | The device name of the root device.                                                  | String  | No       |         | Example: /dev/sda1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| sriovNetSupport     | Enhanced networking with the Intel 82599 VF interface.                               | String  | No       |         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| tpmSupport          | TPM version support.                                                                 | String  | No       |         | Valid values: v2.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| uefiData            | Base64-encoded UEFI data.                                                            | String  | No       |         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| virtualizationType  | The virtualization type.                                                             | String  | No       |         | Valid values: hvm, paravirtual                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

**Outputs:** The following table includes outputs for this step action.

| Output name | Description                         | Type   |
| ----------- | ----------------------------------- | ------ |
| imageId     | The AMI ID of the registered image. | String |

**Example**

Specify the step action in the workflow document.

```
- name: RegisterNewImage
  action: RegisterImage
  onFailure: Abort
  inputs:
    architecture: "x86_64"
    bootMode: "uefi"
    blockDeviceMapping:
      - DeviceName: "/dev/sda1"
        Ebs:
          SnapshotId: "`snap-1234567890abcdef0`"
          VolumeSize: 100
          VolumeType: "gp3"
    rootDeviceName: "/dev/sda1"
    virtualizationType: "hvm"
```

Use the output of the step action value in the workflow document.

```
$.stepOutputs.RegisterNewImage.imageId
```

**Example with a SnapshotId from another step and snapshot tags included in the generated AMI**

```
- name: CreateSnapshot
  action: RunCommand
  onFailure: Abort
  inputs:
    instanceId: "`i-1234567890abcdef0`"
    documentName: "AWS-RunShellScript"
    parameters:
      commands:
        - "aws ec2 create-snapshot --volume-id `vol-1234567890abcdef0` --description 'Snapshot for AMI' --query 'SnapshotId' --output text"

- name: RegisterImageFromSnapshot
  action: RegisterImage
  onFailure: Abort
  inputs:
    architecture: "x86_64"
    bootMode: "uefi"
    blockDeviceMapping:
      - DeviceName: "/dev/sda1"
        Ebs:
          SnapshotId.$: "$.stepOutputs.CreateSnapshot.output[0]"
          VolumeSize: 100
          VolumeType: "gp3"
    includeSnapshotTags: true
    rootDeviceName: "/dev/sda1"
    virtualizationType: "hvm"
```

## RunCommand

This step action runs a command document for your workflow. Image Builder uses the
**sendCommand** in the Systems Manager API to run it for you.
For more information, see [AWS Systems Manager Run
Command](../../../systems-manager/latest/userguide/run-command.md "../../../systems-manager/latest/userguide/run-command.md").

**Default Timeout:** 12 hours

**Rollback:** There is no rollback for this
step action.

**Inputs:** The following table includes
supported inputs for this step action.

| Input name      | Description                                                                         | Type                             | Required    | Default  | Constraints                                                                                                 |
| --------------- | ----------------------------------------------------------------------------------- | -------------------------------- | ----------- | -------- | ----------------------------------------------------------------------------------------------------------- |
| instanceId      | The ID of the instance to run the command document on.                              | String                           | Yes         |          | This must be the output instance ID from the workflow step that<br>launched the instance for this workflow. |
| documentName    | The name of the Systems Manager command document to run.                            | String                           | Yes         |          |                                                                                                             |
| parameters      | A list of key value pairs for any parameters that the command<br>document requires. | dictionary<string, list<string>> | Conditional |          |                                                                                                             |
| documentVersion | The command document version to run.                                                | String                           | No          | $DEFAULT |                                                                                                             |

**Outputs:** The following table includes
outputs for this step action.

| Output name  | Description                                                                                          | Type            |
| ------------ | ---------------------------------------------------------------------------------------------------- | --------------- |
| runCommandId | The ID of the Systems Manager \*_sendCommand_<br>• that ran the command<br>document on the instance. | String          |
| status       | The status returned from the Systems Manager **sendCommand**.                                        | String          |
| output       | Output returned from the Systems Manager **sendCommand**.                                            | List of strings |

**Example**

Specify the step action in the workflow document.

```
`- name: `RunCommandDoc`
 action: RunCommand
 onFailure: Abort
 inputs:
 documentName: `SampleDocument`
 parameters:
 osPlatform:
 - "`linux`"
 instanceId.$: $.stepOutputs.`LaunchStep`.instanceId`
```

Use the output of the step action value in the workflow document.

```
`$.stepOutputs.`RunCommandDoc`.status`
```

## RunSysPrep

This step action uses the **sendCommand** in the Systems Manager API to
run the `AWSEC2-RunSysprep` document for Windows
instances before the build instance shuts down for the snapshot.
These actions follow [AWS best practices for
hardening and cleaning the image](https://aws.amazon.com/articles/public-ami-publishing-hardening-and-clean-up-requirements/ "https://aws.amazon.com/articles/public-ami-publishing-hardening-and-clean-up-requirements/").

**Default Timeout:** 60 minutes

**Rollback:** There is no rollback for this
step action.

**Inputs:** The following table includes
supported inputs for this step action.

| Input name | Description                                                           | Type   | Required | Default | Constraints                                                                                                 |
| ---------- | --------------------------------------------------------------------- | ------ | -------- | ------- | ----------------------------------------------------------------------------------------------------------- |
| instanceId | The ID of the instance to run the<br>`AWSEC2-RunSysprep` document on. | String | Yes      |         | This must be the output instance ID from the workflow step that<br>launched the instance for this workflow. |

**Outputs:** The following table includes
outputs for this step action.

| Output name  | Description                                                                                                      | Type   |
| ------------ | ---------------------------------------------------------------------------------------------------------------- | ------ |
| runCommandId | The ID of the Systems Manager \*_sendCommand_<br>• that ran the<br>`AWSEC2-RunSysprep` document on the instance. | String |
| status       | The status returned from the Systems Manager **sendCommand**.                                                    | String |
| output       | Output returned from the Systems Manager **sendCommand**.                                                        | String |

**Example**

Specify the step action in the workflow document.

```
`- name: `RunSysprep`
 action: RunSysPrep
 onFailure: Abort
 inputs:
 instanceId.$: $.stepOutputs.`LaunchStep`.instanceId`
```

Use the output of the step action value in the workflow document.

```
`$.stepOutputs.`RunSysprep`.status`
```

## SanitizeInstance

This step action runs the recommended sanitize script for Linux instances
before the build instance shuts down for the snapshot. The sanitize script
helps ensure that the final image follows security best practices, and that
build artifacts or settings that should not carry over to your snapshot are
removed. For more information about the script, see [Required post-build clean up](security-best-practices.md#post-build-cleanup "security-best-practices.md#post-build-cleanup"). This
step action does not apply to container images.

Image Builder uses the **sendCommand** in the Systems Manager API to run this
script. For more information, see [AWS Systems Manager Run
Command](../../../systems-manager/latest/userguide/execute-remote-commands.md "../../../systems-manager/latest/userguide/execute-remote-commands.md").

**Default Timeout:** 60 minutes

**Rollback:** There is no rollback for this
step action.

**Inputs:** The following table includes
supported inputs for this step action.

| Input name | Description                         | Type   | Required | Default | Constraints                                                                                                 |
| ---------- | ----------------------------------- | ------ | -------- | ------- | ----------------------------------------------------------------------------------------------------------- |
| instanceId | The ID of the instance to sanitize. | String | Yes      |         | This must be the output instance ID from the workflow step that<br>launched the instance for this workflow. |

**Outputs:** The following table includes
outputs for this step action.

| Output name  | Description                                                                                         | Type   |
| ------------ | --------------------------------------------------------------------------------------------------- | ------ |
| runCommandId | The ID of the Systems Manager \*_sendCommand_<br>• that ran the sanitize<br>script on the instance. | String |
| status       | The status returned from the Systems Manager **sendCommand**.                                       | String |
| output       | Output returned from the Systems Manager **sendCommand**.                                           | String |

**Example**

Specify the step action in the workflow document.

```
`- name: `SanitizeStep`
 action: SanitizeInstance
 onFailure: Abort
 inputs:
 instanceId: $.stepOutputs.`LaunchStep`.instanceId`
```

Use the output of the step action value in the workflow document.

```
`$.stepOutputs.`SanitizeStep`.status`
```

## TerminateInstance

This step action terminate the instance with the instance id that's passed in as input.

**Default Timeout:** 30 minutes

**Rollback:** There is no rollback for this step action.

**Inputs:** The following table includes
supported inputs for this step action.

| Input name | Description                          | Type   | Required | Default | Constraints |
| ---------- | ------------------------------------ | ------ | -------- | ------- | ----------- |
| instanceId | The ID of the instance to terminate. | String | Yes      |         |             |

**Outputs:** There are no outputs for
this step action.

**Example**

Specify the step action in the workflow document.

```
`- name: `TerminateInstance`
 action: TerminateInstance
 onFailure: Continue
 inputs:
 instanceId.$: `i-1234567890abcdef0``
```

## WaitForAction

This step action pauses the running workflow and waits to receive an
external action from the Image Builder **SendWorkflowStepAction**
API action. This step publishes an EventBridge event to your default EventBridge event
bus with detail type `EC2 Image Builder Workflow Step Waiting`.
The step can also send an SNS notification if you provide an SNS Topic ARN,
or invoke a Lambda function asynchronously if you provide a Lambda function name.

**Default Timeout:** 3 days

**Rollback:** There is no rollback for this
step action.

**Inputs:** The following table includes
supported inputs for this step action.

| Input name         | Description                                                                                                                                                                                                                | Type   | Required | Default | Constraints                           |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | -------- | ------- | ------------------------------------- |
| snsTopicArn        | An optional SNS topic ARN to send a notification to when the workflow step is pending.                                                                                                                                     | String | No       |         |                                       |
| lambdaFunctionName | An optional name or ARN of the Lambda function to invoke asynchronously when the workflow step is pending.                                                                                                                 | String | No       |         |                                       |
| payload            | JSON string used as message for SNS and payload for Lambda. If provided, a custom payload is wrapped in default message/payload, used for SNS and Lambda respectively. If not provided, generates default message/payload. | String | No       |         | Must be valid JSON string, max 16 KiB |

**Outputs:** The following table includes
outputs for this step action.

| Output name | Description                                                           | Type                        |
| ----------- | --------------------------------------------------------------------- | --------------------------- |
| action      | The action that the **SendWorkflowStepAction**<br>API action returns. | String (`RESUME` or `STOP`) |
| reason      | The reason for the returned action.                                   | String                      |

**Example**

Specify the step action in the workflow document with SNS notification.

```
`- name: `SendEventAndWait`
 action: WaitForAction
 onFailure: Abort
 inputs:
 snsTopicArn: arn:aws:sns:`us-west-2`:`111122223333`:`ExampleTopic``
```

Specify the step action in the workflow document with Lambda function invocation.

```
`- name: `SendEventAndWaitWithLambda`
 action: WaitForAction
 onFailure: Abort
 inputs:
 lambdaFunctionName: `ExampleFunction`
 payload: |
 {
 "imageId": "{{ $.stepOutputs.CreateImageFromInstance.imageId }}",
 "region": "us-west-2"
 }`
```

Use the output of the step action value in the workflow document.

```
`$.stepOutputs.`SendEventAndWait`.reason`
```

## WaitForSSMAgent

This step action waits for an EC2 instance to become manageable by AWS Systems Manager
after expected periods of unresponsiveness. It's particularly valuable for
workflows with known instance interruptions, such as system reboots, OS upgrades,
or platform-specific operations that temporarily disconnect the instance from SSM.
Image Builder monitors the instance until it regains SSM connectivity or times out.

**Default Timeout:** 60 minutes

**Max Timeout:** 3 hours

**Rollback:** There is no rollback for this
step action.

**Inputs:** The following table includes
supported inputs for this step action.

| Input name | Description                                             | Type   | Required | Default | Constraints                     |
| ---------- | ------------------------------------------------------- | ------ | -------- | ------- | ------------------------------- |
| instanceId | The ID of the instance to monitor for SSM connectivity. | String | Yes      |         | Must be a valid EC2 instance ID |

**Outputs:** The following table includes
outputs for this step action.

| Output name | Description                     | Type   |
| ----------- | ------------------------------- | ------ |
| Status      | Connection status of SSM Agent. | String |

**Example**

Specify the step action in the workflow document.

```
`- name: `WaitForInstanceAfterReboot`
 action: WaitForSSMAgent
 onFailure: Abort
 timeoutInSeconds: 900 # 15 minutes
 inputs:
 instanceId.$: $.stepOutputs.LaunchStep.instanceId`
```

Use the output of the step action value in the workflow document.

```
`$.stepOutputs.`WaitForInstanceAfterReboot`.Status`
```
