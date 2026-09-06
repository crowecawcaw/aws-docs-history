

# Supported step actions for your workflow document
<a name="wfdoc-step-actions"></a>

This section includes details for the step actions that Image Builder supports.Terms used in this section

AMI  
Amazon Machine Image

ARN  
Amazon Resource Name

The following table shows which workflow stages support each step action. A check mark (X) indicates that you can use the step action in that stage. Image Builder restricts a few actions to specific stages: `ExecuteComponents` to the build and test stages, `CollectImageScanFindings` to the test stage, and `DistributeImage`, `ModifyImageAttributes`, `ApplyImageConfigurations`, and `DistributeContainerImage` to the distribution stage. You can use every other action in any stage.


| Step action | Build | Test | Distribution | Notes | 
| --- | --- | --- | --- | --- | 
| LaunchInstance | X | X | X | Launches an Amazon EC2 instance. | 
| BootstrapInstanceForContainer | X | X | X | Installs Docker and the AWS CLI for container builds. | 
| ExecuteComponents | X | X |  | Runs components on the instance. Restricted to the build and test stages. | 
| CollectImageMetadata | X | X | X | AMI builds only. | 
| RunSysPrep | X | X | X | Windows builds. | 
| SanitizeInstance | X | X | X | Linux AMI builds; not for containers. | 
| CreateImage | X | X | X | Creates an AMI from the build instance. | 
| CreateImageFromIso | X | X | X | Creates an AMI from an ISO disk image. | 
| RegisterImage | X | X | X | Registers an AMI from snapshots. | 
| DistributeContainerImage |  |  | X | Distributes a container image. Restricted to the distribution stage. | 
| CollectImageScanFindings |  | X |  | Collects image scan findings. Restricted to the test stage. Requires Amazon Inspector and image scanning. | 
| RunCommand | X | X | X | Runs an AWS Systems Manager (Systems Manager) command document. | 
| WaitForSSMAgent | X | X | X | Waits for Systems Manager connectivity after a reboot. | 
| WaitForAction | X | X | X | Pauses for an external action. | 
| ExecuteStateMachine | X | X | X | Runs a Step Functions state machine. | 
| TerminateInstance | X | X | X | Terminates an instance. For example, a container-distribution workflow terminates the build instance after it pushes the image. | 
| DistributeImage |  |  | X | Copies an AMI to Regions and accounts. Restricted to the distribution stage. | 
| ModifyImageAttributes |  |  | X | Modifies AMI launch permissions. Restricted to the distribution stage. | 
| ApplyImageConfigurations |  |  | X | Applies launch templates, licenses, exports, fast launch, and Systems Manager parameters. Restricted to the distribution stage. | 

**Important**  
A single workflow distributes either AMIs or container images, not both. If a workflow includes `DistributeContainerImage`, it cannot also include `DistributeImage`, `ModifyImageAttributes`, or `ApplyImageConfigurations`. These AMI distribution actions operate on Amazon EC2 AMIs, while `DistributeContainerImage` operates on container images in Amazon Elastic Container Registry (Amazon ECR).

**Topics**
+ [ApplyImageConfigurations](#wfdoc-step-action-apply-image-configurations)
+ [BootstrapInstanceForContainer](#wfdoc-step-action-bootstrap-container)
+ [CollectImageMetadata](#wfdoc-step-action-collect-image-metadata)
+ [CollectImageScanFindings](#wfdoc-step-action-collect-findings)
+ [CreateImage](#wfdoc-step-action-create-img-from-inst)
+ [CreateImageFromIso](#wfdoc-step-action-create-image-from-iso)
+ [DistributeContainerImage](#wfdoc-step-action-distribute-container)
+ [DistributeImage](#wfdoc-step-action-distribute-image)
+ [ExecuteComponents](#wfdoc-step-action-exec-components)
+ [ExecuteStateMachine](#wfdoc-step-action-exec-state-machine)
+ [LaunchInstance](#wfdoc-step-action-launch-instance)
+ [ModifyImageAttributes](#wfdoc-step-action-modify-image-attributes)
+ [RegisterImage](#wfdoc-step-action-register-image)
+ [RunCommand](#wfdoc-step-action-run-command)
+ [RunSysPrep](#wfdoc-step-action-run-sysprep)
+ [SanitizeInstance](#wfdoc-step-action-sanitize-instance)
+ [TerminateInstance](#wfdoc-step-action-terminate-instance)
+ [WaitForAction](#wfdoc-step-action-waitfor)
+ [WaitForSSMAgent](#wfdoc-step-action-wait-for-ssm-agent)

## ApplyImageConfigurations
<a name="wfdoc-step-action-apply-image-configurations"></a>

Use this step action to apply various configurations and integrations to distributed AMIs, such as license configurations, launch template configurations, S3 export configurations, EC2 Fast Launch configurations, and Systems Manager parameter configurations. Configurations apply to distributed images only in the source account, except for SSM parameter configs which can be applied cross-account.

**Note**  
The `configurations` input is optional. If you provide it, Image Builder uses your workflow inputs and ignores the attached distribution configuration. If you omit it, Image Builder falls back to the distribution configuration attached to the pipeline or image.

**Default Timeout: **360 minutes

**Max Timeout: **720 minutes (12 hours)

You can override the default with `timeoutSeconds`, up to the maximum shown. A value above the maximum fails validation.

**Rollback: **There is no rollback for this step action.

**Inputs: **The following table includes supported inputs for this step action. The `distributedImages.$` input is required. The remaining rows describe the fields within each item of the `configurations` array.


| Input name | Description | Type | Required | Default | Constraints | 
| --- | --- | --- | --- | --- | --- | 
| distributedImages.$ | The list of distributed images to configure. Reference the distributedImages output from a DistributeImage step in the same workflow. | String | Yes |  | A JSONPath reference that starts with $.stepOutputs. | 
| configurations | The configurations to apply to the distributed AMIs, as a list. Each item targets one AWS Region. | Array | No |  |  | 
| configurations:region | The AWS Region of the distributed AMI to configure. | String | Yes |  | Required for each item in configurations. | 
| configurations:licenseConfigurationArns | The license configuration ARN for the image. | Array | No |  |  | 
| configurations:launchTemplateConfigurations | The launch template configurations to apply to the distributed AMIs. | Array | No |  |  | 
| configurations:launchTemplateConfigurations:launchTemplateId | The launch template ID to apply to the image. | String | Yes if launchTemplateConfigurations is specified |  |  | 
| configurations:launchTemplateConfigurations:accountId | The launch template account IDs to apply to the image. | String | No |  |  | 
| configurations:launchTemplateConfigurations:setDefaultVersion | The launch template default version setting for the image. | Boolean | No |  |  | 
| configurations:s3ExportConfiguration | The Amazon S3 export configuration for the distributed AMIs. | Array | No |  |  | 
| configurations:s3ExportConfiguration:roleName | The Amazon S3 export configuration role name for the image. | String | Yes if s3ExportConfiguration is specified |  |  | 
| configurations:s3ExportConfiguration:diskImageFormat | The Amazon S3 export configuration disk image format for the image. | String | Yes if s3ExportConfiguration is specified |  | Allowed values - VMDK\|RAW\|VHD | 
| configurations:s3ExportConfiguration:s3Bucket | The Amazon S3 export configuration bucket name for the image. | String | Yes if s3ExportConfiguration is specified |  |  | 
| configurations:s3ExportConfiguration:s3Prefix | The Amazon S3 export configuration bucket prefix for the image. | String | No |  |  | 
| configurations:fastLaunchConfigurations | The Amazon EC2 Fast Launch configuration for the image. | Array | No |  |  | 
| configurations:fastLaunchConfigurations:enabled | Whether Amazon EC2 Fast Launch is enabled for the image. | Boolean | Yes if fastLaunchConfigurations is specified |  |  | 
| configurations:fastLaunchConfigurations:snapshotConfiguration | The snapshot configuration for pre-provisioning Amazon EC2 Fast Launch snapshots. | Map | No |  |  | 
| configurations:fastLaunchConfigurations:snapshotConfiguration:targetResourceCount | The Amazon EC2 Fast Launch target resource count for the image. | Integer | No |  |  | 
| configurations:fastLaunchConfigurations:maxParallelLaunches | The Amazon EC2 Fast Launch maximum parallel launches for the image. | Integer | No |  |  | 
| configurations:fastLaunchConfigurations:launchTemplate | The launch template that Amazon EC2 Fast Launch uses to prepare pre-provisioned snapshots. | Map | No |  |  | 
| configurations:fastLaunchConfigurations:launchTemplate:launchTemplateId | The Amazon EC2 Fast Launch launch template ID for the image. | String | No |  |  | 
| configurations:fastLaunchConfigurations:launchTemplate:launchTemplateName | The Amazon EC2 Fast Launch launch template name for the image. | String | No |  |  | 
| configurations:fastLaunchConfigurations:launchTemplate:launchTemplateVersion | The Amazon EC2 Fast Launch launch template version for the image. | String | No |  |  | 
| configurations:ssmParameterConfigurations | The Systems Manager parameter configuration for the image. | Map | No |  |  | 
| configurations:ssmParameterConfigurations:amiAccountId | The Systems Manager parameter AMI account ID for the image. | String | No |  |  | 
| configurations:ssmParameterConfigurations:parameterName | The Systems Manager parameter name for the image. | String | Yes if ssmParameterConfigurations is specified |  |  | 
| configurations:ssmParameterConfigurations:dataType | The Systems Manager parameter data type for the image. | String | No |  | Allowed values - text\|aws:ec2:image) | 

**Outputs: **The following table includes outputs for this step action.


| Output name | Description | Type | 
| --- | --- | --- | 
| configuredImages | A list of configured images. | Array | 
| configuredImages:accountId | The destination account ID of the distributed image. | String | 
| configuredImages:name | The name of the AMI. | String | 
| configuredImages:amiId | The AMI ID of the distributed image. | String | 
| configuredImages:dateStarted | UTC time when distribution started. | String | 
| configuredImages:dateStopped | UTC time when distribution completed. | String | 
| configuredImages:step | The step at which distribution stopped. | Completed\|AssociateLicensesRunning\|UpdateLaunchTemplateRunning\|PutSsmParametersRunning\|UpdateFastLaunchConfiguration\|ExportAmiQueued\|ExportAmiRunning | 
| configuredImages:region | The AWS Region of the distributed image. | String | 
| configuredImages:status | Distribution status. | Completed\|Failed\|Cancelled\|TimedOut | 
| configuredImages:errorMessage  | Error message, if any. | String | 

**Example**

Specify the step action in the workflow document.

```
- name: {{ApplyImageConfigurations}}
  action: ApplyImageConfigurations
  onFailure: Abort
  inputs:
    distributedImages.$: $.stepOutputs.{{DistributeImageStep}}.distributedImages
    configurations:
      - region: {{us-west-2}}
        licenseConfigurationArns:
          - arn:aws:license-manager:{{us-west-2}}:{{111122223333}}:license-configuration:{{lic-example}}
```

Use the output of the step action value in the workflow document.

```
$.stepOutputs.{{ApplyImageConfigurationsStep}}.configuredImages
```

## BootstrapInstanceForContainer
<a name="wfdoc-step-action-bootstrap-container"></a>

This step action runs a service script to bootstrap the instance with minimum requirements to run container workflows. Image Builder uses the **sendCommand** in the Systems Manager API to run this script. For more information, see [AWS Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/execute-remote-commands.html).

**Note**  
The bootstrap script installs the AWS CLI and Docker packages that are prerequisites for Image Builder to successfully build Docker containers. If you don't include this step action, the image build could fail.

**Default Timeout: **60 minutes

**Max Timeout: **720 minutes (12 hours)

You can override the default with `timeoutSeconds`, up to the maximum shown. A value above the maximum fails validation.

**Rollback: **There is no rollback for this step action.

**Inputs: **The following table includes supported inputs for this step action.


| Input name | Description | Type | Required | Default | Constraints | 
| --- | --- | --- | --- | --- | --- | 
| instanceId | The ID of the instance to bootstrap. | String | Yes |  | This must be the output instance ID from the workflow step that launched the instance for this workflow. | 

**Outputs: **The following table includes outputs for this step action.


| Output name | Description | Type | 
| --- | --- | --- | 
| runCommandId | The ID of the Systems Manager sendCommand that ran the bootstrap script on the instance. | String | 
| status | The status returned from the Systems Manager sendCommand. | String | 
| output | Output returned from the Systems Manager sendCommand. | String | 

**Example**

Specify the step action in the workflow document.

```
- name: {{ContainerBootstrapStep}}
  action: BootstrapInstanceForContainer
  onFailure: Abort
  inputs:
      instanceId.$: $.stepOutputs.{{LaunchStep}}.instanceId
```

Use the output of the step action value in the workflow document.

```
$.stepOutputs.{{ContainerBootstrapStep}}.status
```

## CollectImageMetadata
<a name="wfdoc-step-action-collect-image-metadata"></a>

This step action is only valid for build workflows.

EC2 Image Builder runs [AWS Systems Manager (Systems Manager) Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html) on the EC2 instances it launches to build and test your image. Image Builder collects additional information about the instance used during the build phase with [Systems Manager Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html). This information includes the operating system (OS) name and version, as well as the list of packages and their respective versions as reported by your operating system.

**Note**  
This step action only works for images that create AMIs.

**Default Timeout: **30 minutes

**Max Timeout: **720 minutes (12 hours)

You can override the default with `timeoutSeconds`, up to the maximum shown. A value above the maximum fails validation.

**Rollback: **Image Builder rolls back any Systems Manager resources that were created during this step.

**Inputs: **The following table includes supported inputs for this step action.


| Input name | Description | Type | Required | Default | Constraints | 
| --- | --- | --- | --- | --- | --- | 
| instanceId | The build instance to apply the metadata settings to. | String | Yes |  | This must be the output instance ID from the workflow step that launched the build instance for this workflow. | 

**Outputs: **The following table includes outputs for this step action.


| Output name | Description | Type | 
| --- | --- | --- | 
| osVersion | The operating system name and version collected from the build instance. | String | 
| associationId | The Systems Manager association ID used for inventory collection. | String | 

**Example**

Specify the step action in the workflow document.

```
- name: {{CollectMetadataStep}}
  action: CollectImageMetadata
  onFailure: Abort
  inputs:
      instanceId: $.stepOutputs.{{LaunchStep}}.instanceId
```

Use output from the step action in the workflow document.

```
$.stepOutputs.{{CollectMetadataStep}}.osVersion
```

## CollectImageScanFindings
<a name="wfdoc-step-action-collect-findings"></a>

If Amazon Inspector is enabled for your account and image scanning is enabled for your pipeline, this step action collects image scan findings reported by Amazon Inspector for your test instance. This step action is not available for build workflows.

**Default Timeout: **120 minutes

**Max Timeout: **720 minutes (12 hours)

You can override the default with `timeoutSeconds`, up to the maximum shown. A value above the maximum fails validation.

**Rollback: **There is no rollback for this step action.

**Inputs: **The following table includes supported inputs for this step action.


| Input name | Description | Type | Required | Default | Constraints | 
| --- | --- | --- | --- | --- | --- | 
| instanceId | The ID for the instance that scanning ran on. | String | Yes |  | This must be the output instance ID from the workflow step that launched the instance for this workflow. | 

**Outputs: **The following table includes outputs for this step action.


| Output name | Description | Type | 
| --- | --- | --- | 
| runCommandId | The ID of the Systems Manager sendCommand that ran the script to collect findings. | String | 
| status | The status returned from the Systems Manager sendCommand. | String | 
| output | Output returned from the Systems Manager sendCommand. | String | 

**Example**

Specify the step action in the workflow document.

```
- name: {{CollectFindingsStep}}
  action: CollectImageScanFindings
  onFailure: Abort
  inputs:
      instanceId.$: $.stepOutputs.{{LaunchStep}}.instanceId
```

Use the output of the step action value in the workflow document.

```
$.stepOutputs.{{CollectFindingsStep}}.status
```

## CreateImage
<a name="wfdoc-step-action-create-img-from-inst"></a>

This step action creates an image from a running instance with the Amazon EC2 `CreateImage` API. During the creation process, the step action waits as necessary to verify that the resources have reached the correct state before it continues.

**Default Timeout: **720 minutes

**Max Timeout: **3 days (259,200 seconds)

You can override the default with `timeoutSeconds`, up to the maximum shown. A value above the maximum fails validation.

**Rollback: **There is no rollback for this step action.

**Inputs: **The following table includes supported inputs for this step action.


| Input name | Description | Type | Required | Default | Constraints | 
| --- | --- | --- | --- | --- | --- | 
| instanceId | The instance to create the new image from. | String | Yes |  | The instance for the provided instance ID must be in a running state when this step starts. | 

**Outputs: **The following table includes outputs for this step action.


| Output name | Description | Type | 
| --- | --- | --- | 
| imageId | The AMI ID of the image that's created. | String | 

**Example**

Specify the step action in the workflow document.

```
- name: {{CreateImageFromInstance}}
  action: CreateImage
  onFailure: Abort
  inputs:
      instanceId.$: "i-1234567890abcdef0"
```

Use the output of the step action value in the workflow document.

```
$.stepOutputs.{{CreateImageFromInstance}}.imageId
```

## CreateImageFromIso
<a name="wfdoc-step-action-create-image-from-iso"></a>

Use this step action to create an Amazon Machine Image (AMI) from an ISO disk image on the build instance. Use it in a build workflow when your source is an ISO file rather than a base AMI. Image Builder converts the ISO to an AMI and waits for the resources to reach the required state before it continues.

**Note**  
This action has the same requirements as importing an ISO disk image. For more information, see [Import verified Windows ISO disk images with Image Builder](import-iso-disk.md).

**Default Timeout: **720 minutes

**Max Timeout: **720 minutes (12 hours)

You can override the default with `timeoutSeconds`, up to the maximum shown. A value above the maximum fails validation.

**Rollback: **There is no rollback for this step action.

**Inputs: **The following table includes supported inputs for this step action.


| Input name | Description | Type | Required | Default | Constraints | 
| --- | --- | --- | --- | --- | --- | 
| instanceId | The ID of the build instance that holds the ISO disk image. | String | Yes |  | This must be the output instance ID from the workflow step that launched the build instance for this workflow. | 

**Outputs: **The following table includes outputs for this step action.


| Output name | Description | Type | 
| --- | --- | --- | 
| amiName | The name of the AMI that the step created. | String | 
| snapshotId | The ID of the snapshot that backs the AMI. | String | 
| architecture | The architecture of the AMI (x86\_64 or arm64). | String | 

**Example**

Specify the step action in the workflow document.

```
- name: {{CreateImageFromIsoStep}}
  action: CreateImageFromIso
  onFailure: Abort
  inputs:
      instanceId.$: $.stepOutputs.{{LaunchStep}}.instanceId
```

Use the output of the step action value in the workflow document.

```
$.stepOutputs.{{CreateImageFromIsoStep}}.amiName
```

## DistributeContainerImage
<a name="wfdoc-step-action-distribute-container"></a>

Use this step action to distribute a container image that the build stage created to Amazon ECR repositories in the target Regions defined for the image. Use this action in a distribution workflow for container (`DOCKER`) images. It works as the container-image counterpart to `DistributeImage`.

This step action runs a Systems Manager command on the build instance to push the container image. The instance must have Docker and the AWS CLI installed. For more information, see [BootstrapInstanceForContainer](#wfdoc-step-action-bootstrap-container).

**Important**  
A workflow that includes `DistributeContainerImage` cannot also include `DistributeImage`, `ModifyImageAttributes`, or `ApplyImageConfigurations`. A single workflow distributes either container images or AMIs, not both.

**Default Timeout: **120 minutes

**Max Timeout: **720 minutes (12 hours)

You can override the default with `timeoutSeconds`, up to the maximum shown. A value above the maximum fails validation.

**Rollback: **There is no rollback for this step action.

**Inputs: **The following table includes supported inputs for this step action.


| Input name | Description | Type | Required | Default | Constraints | 
| --- | --- | --- | --- | --- | --- | 
| instanceId | The ID of the build instance that holds the container image. | String | Yes |  | This must be the output instance ID from the workflow step that launched the build instance for this workflow. | 

**Outputs: **The following table includes outputs for this step action.


| Output name | Description | Type | 
| --- | --- | --- | 
| status | The status returned from the Systems Manager sendCommand. | String | 
| succeededRegions | The Regions where distribution succeeded. | Array | 
| failedRegions | The Regions where distribution failed. | Array | 

**Example**

Specify the step action in the workflow document.

```
- name: {{DistributeContainer}}
  action: DistributeContainerImage
  onFailure: Abort
  inputs:
      instanceId.$: $.stepOutputs.{{LaunchStep}}.instanceId
```

Use the output of the step action value in the workflow document.

```
$.stepOutputs.{{DistributeContainer}}.status
```

## DistributeImage
<a name="wfdoc-step-action-distribute-image"></a>

This step action distributes an AMI to the target Regions and accounts that you specify. It uses the distribution configuration from your `CreateImage` or `CreateImagePipeline` request, or custom distribution settings in the workflow that override the default configuration.

**Note**  
The `distributions` input is optional. If you provide it, Image Builder uses your workflow inputs and ignores the attached distribution configuration. If you omit it, Image Builder falls back to the distribution configuration attached to the pipeline or image.

**Default Timeout: **360 minutes

**Max Timeout: **720 minutes (12 hours)

You can override the default with `timeoutSeconds`, up to the maximum shown. A value above the maximum fails validation.

**Rollback: **There is no rollback for this step action.

**Inputs: **The following table includes supported inputs for this step action.


| Input name | Description | Type | Required | Default | Constraints | 
| --- | --- | --- | --- | --- | --- | 
| distributions | The distribution settings for the AMI, as a list. Each item targets one AWS Region. If you omit this input, Image Builder uses the distribution configuration attached to the pipeline or image. | Array | No |  |  | 
| distributions:region | The AWS Region to distribute the AMI to. | String | Yes |  | Minimum length of 1. Maximum length of 1024. | 
| distributions:name | The name to apply to the distributed AMI. | String | No |  |  | 
| distributions:description | The description to apply to the distributed AMI. | String | No |  |  | 
| distributions:targetAccountIds | The account IDs to distribute the AMI to. | Array | No |  |  | 
| distributions:amiTags | The tags to apply to the distributed AMI. | Map | No |  | Maximum of 50 tags. | 
| distributions:kmsKeyId | The KMS key to use to encrypt the distributed AMI. | String | No |  |  | 

**Outputs: **The following table includes outputs for this step action.


| Output name | Description | Type | 
| --- | --- | --- | 
| distributedImages | A list of distributed images | Array | 
| distributedImages:region | The AWS Region of the distributed image. | String | 
| distributedImages:name | The name of the AMI. | String | 
| distributedImages:amiId | The AMI ID of the distributed image. | String | 
| distributedImages:accountId | The destination account ID of the distributed image. | String | 
| distributedImages:dateStarted | UTC time when distribution started. | String | 
| distributedImages:dateStopped | UTC time when distribution completed. | String | 
| distributedImages:status | Distribution status. | Completed\|Failed\|Cancelled\|TimedOut | 
| distributedImages:step | The step at which distribution stopped. | Completed\|CopyAmiRunning | 
| distributedImages:errorMessage  | Error message, if any. | String | 

**Example**

Specify the step action in the workflow document.

```
- name: {{DistributeImage}}
  action: DistributeImage
  onFailure: Abort
  inputs:
    distributions:
      - region.$: "$.parameters.{{SourceRegion}}"
        description: "{{AMI distribution to source region}}"
        amiTags:
          DistributionTest: "{{SourceRegion}}"
          WorkflowStep: "{{DistributeToSourceRegion}}"
          BuildDate: "{{imagebuilder:buildDate:yyyyMMHHss}}"
          BuildVersion: "{{imagebuilder:buildVersion}}"
```

Use the output of the step action value in the workflow document.

```
$.stepOutputs.{{DistributeImageStep}}.distributedImages
```

## ExecuteComponents
<a name="wfdoc-step-action-exec-components"></a>

This step action runs components that are specified in the recipe for the current image being built. Build workflows run build components on the build instance. Test workflows only run test components on the test instance.

Image Builder uses the **sendCommand** in the Systems Manager API to run components. For more information, see [AWS Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/execute-remote-commands.html).

**Default Timeout: **720 minutes

**Max Timeout: **1 day (24 hours)

You can override the default with `timeoutSeconds`, up to the maximum shown. A value above the maximum fails validation.

**Rollback: **There is no rollback for this step action.

**Inputs: **The following table includes supported inputs for this step action.


| Input name | Description | Type | Required | Default | Constraints | 
| --- | --- | --- | --- | --- | --- | 
| instanceId | The ID for the instance that the components should run on. | String | Yes |  | This must be the output instance ID from the workflow step that launched the instance for this workflow. | 

**Outputs: **The following table includes outputs for this step action.


| Output name | Description | Type | 
| --- | --- | --- | 
| runCommandId | The ID of the Systems Manager sendCommand that ran the components on the instance. | String | 
| status | The status returned from the Systems Manager sendCommand. | String | 
| output | Output returned from the Systems Manager sendCommand. | String | 

**Example**

Specify the step action in the workflow document.

```
- name: {{ExecComponentsStep}}
  action: ExecuteComponents
  onFailure: Abort
  inputs:
      instanceId: $.stepOutputs.{{LaunchStep}}.instanceId
```

Use output from the step action in the workflow document.

```
$.stepOutputs.{{ExecComponentsStep}}.status
```

## ExecuteStateMachine
<a name="wfdoc-step-action-exec-state-machine"></a>

This step action starts execution of an AWS Step Functions state machine from an Image Builder workflow. Image Builder uses the Step Functions `StartExecution` API to initiate the state machine and waits for it to complete. This is useful for integrating complex workflows, compliance validation, or certification processes into your image building pipeline.

For more information, see [Learn about state machines in Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-statemachines.html) in the *AWS Step Functions Developer Guide*.

**Default Timeout: **6 hours

**Max Timeout: **24 hours

You can override the default with `timeoutSeconds`, up to the maximum shown. A value above the maximum fails validation.

**Rollback: **There is no rollback for this step action.

**Inputs:** The following table includes supported inputs for this step action.


| Input name | Description | Type | Required | Default | Constraints | 
| --- | --- | --- | --- | --- | --- | 
| stateMachineArn | The ARN of the Step Functions state machine to execute. | String | Yes |  | Must be a valid state machine ARN. | 
| input | JSON input data to provide to the state machine. | String | No | {} | Must be valid JSON string, maximum length: 16 KiB. | 

**Outputs:** The following table includes outputs for this step action.


| Output name | Description | Type | 
| --- | --- | --- | 
| executionArn | The ARN of the state machine execution. | String | 
| output | The output of the state machine execution. | String | 

**IAM permissions required**

Your custom execution role must have the following permissions to use this step action:

**Allow actions**
+ `states:StartExecution`
+ `states:DescribeExecution`

**Specify resources**
+ `arn:aws:states:{{us-west-2}}:{{111122223333}}:stateMachine:{{state-machine-name}}`
+ `arn:aws:states:{{us-west-2}}:{{111122223333}}:execution:{{state-machine-name}}:*`

**Example**

Specify the step action in the workflow document.

```
- name: {{ValidateImageCompliance}}
  action: ExecuteStateMachine
  timeoutSeconds: 3600
  onFailure: Abort
  inputs:
    stateMachineArn: arn:aws:states:{{us-west-2}}:{{111122223333}}:stateMachine:{{ImageComplianceValidation}}
    input: |
      {
        "imageId": "{{ $.stepOutputs.CreateImageFromInstance.imageId }}",
        "region": "us-west-2",
        "complianceLevel": "high",
        "requiredScans": ["cve", "benchmark", "configuration"]
      }
```

Use the output of the step action value in the workflow document.

```
$.stepOutputs.{{ValidateImageCompliance}}.executionArn
```

## LaunchInstance
<a name="wfdoc-step-action-launch-instance"></a>

Use this step action to launch an instance in your AWS account. The action waits until the instance meets the specified health check condition and the Systems Manager agent is running before proceeding to the next step. The launch action uses settings from your recipe and infrastructure configuration resources. For example, the instance type to launch comes from the infrastructure configuration. The output is the instance ID of the instance that launched.

The `waitFor` input configures the condition that satisfies the step completion requirement. The `healthCheck` input specifies the level of EC2 instance health validation that must pass before the step proceeds.

**Default Timeout: **75 minutes

**Max Timeout: **720 minutes (12 hours)

You can override the default with `timeoutSeconds`, up to the maximum shown. A value above the maximum fails validation.

**Rollback: **For build instances, rollback performs the action that you have configured in your infrastructure configuration resource. By default, build instances are terminated if image creation fails. However, there is a setting in the infrastructure configuration to keep the build instance for troubleshooting.

**Inputs: **The following table includes supported inputs for this step action.


| Input name | Description | Type | Required | Default | Constraints | 
| --- | --- | --- | --- | --- | --- | 
| imageIdOverride | The image to use for launching the instance | String | No | Build stage: Image recipe base image<br />Test stage: Output AMI from the build stage | Must be a valid AMI ID | 
| instanceTypesOverride | Image Builder tries each instance type in the list until it finds one that launches successfully | List of String | No | Instance types specified in your Infrastructure Configuration | Must be valid instance types | 
| waitFor | The condition to wait for before completing the workflow step and moving on to the next step | String | Yes | None | Image Builder supports ssmAgent. | 
| healthCheck | The level of EC2 health validation required before the workflow step proceeds. Specify RUNNING for faster builds with minimal validation, or STATUS\_CHECK\_PASSED to wait for EC2 status checks to pass. | String | No | STATUS\_CHECK\_PASSED | Valid values: RUNNING \| STATUS\_CHECK\_PASSED. | 

**Outputs: **The following table includes outputs for this step action.


| Output name | Description | Type | 
| --- | --- | --- | 
| instanceId | The instance ID of the instance that launched. | String | 

**Example**

Specify the step action in the workflow document.

```
- name: {{LaunchStep}}
  action: LaunchInstance
  onFailure: Abort
  inputs:
    healthCheck: "{{RUNNING}}"
    waitFor: ssmAgent
```

Use output from the step action in the workflow document.

```
$.stepOutputs.{{LaunchStep}}.instanceId
```

## ModifyImageAttributes
<a name="wfdoc-step-action-modify-image-attributes"></a>

Use this step action to modify attributes of distributed AMIs, such as launch permissions and other AMI attributes. It operates on AMIs that have been distributed to target Regions and accounts.

**Note**  
The `attributes` input is optional. If you provide it, Image Builder uses your workflow inputs and ignores the attached distribution configuration. If you omit it, Image Builder falls back to the distribution configuration attached to the pipeline or image.

**Default Timeout: **120 minutes

**Max Timeout: **180 minutes (3 hours)

You can override the default with `timeoutSeconds`, up to the maximum shown. A value above the maximum fails validation.

**Rollback: **There is no rollback for this step action.

**Inputs: **The following table includes supported inputs for this step action.


| Input name | Description | Type | Required | Default | Constraints | 
| --- | --- | --- | --- | --- | --- | 
| distributedImages.$ | The list of distributed images to modify. Reference the distributedImages output from a DistributeImage step in the same workflow. | String | Yes |  | A JSONPath reference that starts with $.stepOutputs. | 
| attributes | The image attributes to modify, as a list. Each item targets one AWS Region. | Array | No |  |  | 
| attributes:region | The AWS Region of the distributed AMI to modify. | String | Yes |  | Required for each item in attributes. | 
| attributes:launchPermission | The launch permission settings to apply to the distributed AMI. | Map | No |  |  | 
| attributes:launchPermission:userIds | The account IDs to add to or remove from the launch permissions for the AMI. | Array | No |  |  | 
| attributes:launchPermission:userGroups | The user groups to add to or remove from the launch permissions for the AMI. | Array | No |  |  | 
| attributes:launchPermission:organizationArns | The AWS Organizations ARNs to add to or remove from the launch permissions for the AMI. | Array | No |  |  | 
| attributes:launchPermission:organizationalUnitArns | The organizational unit (OU) ARNs to add to or remove from the launch permissions for the AMI. | Array | No |  |  | 

**Outputs: **The following table includes outputs for this step action.


| Output name | Description | Type | 
| --- | --- | --- | 
| modifiedImages | A list of modified images | Array | 
| modifiedImages:accountId | The destination account ID of the distributed image. | String | 
| modifiedImages:name | The name of the AMI. | String | 
| modifiedImages:amiId | The AMI ID of the distributed image. | String | 
| modifiedImages:dateStarted | UTC time when distribution started. | String | 
| modifiedImages:dateStopped | UTC time when distribution completed. | String | 
| modifiedImages:step | The step at which distribution stopped. | Completed\|ModifyAmiRunning | 
| modifiedImages:region | The AWS Region of the image. | String | 
| modifiedImages:status | Distribution status. | Completed\|Failed\|Cancelled\|TimedOut | 
| modifiedImages:errorMessage  | Error message, if any. | String | 

**Example**

Specify the step action in the workflow document.

```
- name: {{ModifyImageAttributes}}
  action: ModifyImageAttributes
  onFailure: Abort
  inputs:
    distributedImages.$: $.stepOutputs.{{DistributeImageStep}}.distributedImages
    attributes:
      - region: {{us-west-2}}
        launchPermission:
          userIds:
            - "{{111122223333}}"
```

Use the output of the step action value in the workflow document.

```
$.stepOutputs.{{ModifyImageAttributesStep}}.modifiedImages
```

## RegisterImage
<a name="wfdoc-step-action-register-image"></a>

This step action registers a new Amazon Machine Image (AMI) using the Amazon EC2 RegisterImage API. It allows you to create an AMI from an existing snapshot or set of snapshots, specifying various image attributes.

**Default Timeout: **540 minutes

**Max Timeout: **720 minutes (12 hours)

You can override the default with `timeoutSeconds`, up to the maximum shown. A value above the maximum fails validation.

**Rollback: **There is no rollback for this step action.

**Inputs: **The following table includes supported inputs for this step action.


| Input name | Description | Type | Required | Default | Constraints | 
| --- | --- | --- | --- | --- | --- | 
| architecture | The architecture of the AMI. | String | No |  | Valid values: i386, x86\_64, arm64, x86\_64\_mac, arm64\_mac | 
| blockDeviceMapping | The block device mapping entries for the AMI. | Array | No |  |  | 
| bootMode | The boot mode of the AMI. | String | No |  | Valid values: legacy-bios, uefi, uefi-preferred | 
| description | A description for the AMI. | String | No |  |  | 
| enaSupport | Whether enhanced networking with ENA is enabled. | Boolean | No |  |  | 
| imageLocation | The location of the AMI manifest. | String | No |  | Required for S3-backed AMIs | 
| imdsSupport | The IMDSv2 support level. | String | No |  | Valid values: v2.0 | 
| includeSnapshotTags | Whether to include tags from the first snapshot defined in the block device mapping. | Boolean | No | FALSE | When set to true, tags are included as follows:+  Tags from the `SnapshotId` of the first EBS volume in the `blockDeviceMapping` list that contains a `SnapshotId` is merged with the output AMI tags. <br />+  Output AMI tags take precedence over snapshot tags with the same key. <br />+  AWS reserved tags (those with keys starting with `aws:`) are automatically excluded. <br />+  If multiple EBS volumes with `SnapshotId` are defined, only tags from the first EBS volume in the list that contains a `SnapshotId` is included.  | 
| kernelId | The ID of the kernel to use. | String | No |  |  | 
| ramdiskId | The ID of the RAM disk to use. | String | No |  |  | 
| rootDeviceName | The device name of the root device. | String | No |  | Example: /dev/sda1 | 
| sriovNetSupport | Enhanced networking with the Intel 82599 VF interface. | String | No |  |  | 
| tpmSupport | TPM version support. | String | No |  | Valid values: v2.0 | 
| uefiData | Base64-encoded UEFI data. | String | No |  |  | 
| virtualizationType | The virtualization type. | String | No |  | Valid values: hvm, paravirtual | 

**Outputs: **The following table includes outputs for this step action.


| Output name | Description | Type | 
| --- | --- | --- | 
| imageId | The AMI ID of the registered image. | String | 

**IAM permissions required**

Your custom execution role must have the following permissions to use this step action:

**Allow actions**
+ `ec2:DescribeSnapshots`
+ `ec2:CreateTags`

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
          SnapshotId: "{{snap-1234567890abcdef0}}"
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
    instanceId: "{{i-1234567890abcdef0}}"
    documentName: "AWS-RunShellScript"
    parameters:
      commands:
        - "aws ec2 create-snapshot --volume-id {{vol-1234567890abcdef0}} --description 'Snapshot for AMI' --query 'SnapshotId' --output text"

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
<a name="wfdoc-step-action-run-command"></a>

This step action runs a command document for your workflow. Image Builder uses the **sendCommand** in the Systems Manager API to run it for you. For more information, see [AWS Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command.html).

**Default Timeout: **720 minutes

**Max Timeout: **720 minutes (12 hours)

You can override the default with `timeoutSeconds`, up to the maximum shown. A value above the maximum fails validation.

**Rollback: **There is no rollback for this step action.

**Inputs: **The following table includes supported inputs for this step action.


| Input name | Description | Type | Required | Default | Constraints | 
| --- | --- | --- | --- | --- | --- | 
| instanceId | The ID of the instance to run the command document on. | String | Yes |  | This must be the output instance ID from the workflow step that launched the instance for this workflow. | 
| documentName | The name of the Systems Manager command document to run. | String | Yes |  |  | 
| parameters | A list of key value pairs for any parameters that the command document requires. | dictionary<string, list<string>> | Conditional |  |  | 
| documentVersion | The command document version to run. | String | No | $DEFAULT |  | 

**Outputs: **The following table includes outputs for this step action.


| Output name | Description | Type | 
| --- | --- | --- | 
| runCommandId | The ID of the Systems Manager sendCommand that ran the command document on the instance. | String | 
| status | The status returned from the Systems Manager sendCommand. | String | 
| output | Output returned from the Systems Manager sendCommand. | List of strings | 

**Example**

Specify the step action in the workflow document.

```
- name: {{RunCommandDoc}}
  action: RunCommand
  onFailure: Abort
  inputs:
    documentName: {{SampleDocument}}
    parameters:
        osPlatform: 
          - "{{linux}}"
    instanceId.$: $.stepOutputs.{{LaunchStep}}.instanceId
```

Use the output of the step action value in the workflow document.

```
$.stepOutputs.{{RunCommandDoc}}.status
```

## RunSysPrep
<a name="wfdoc-step-action-run-sysprep"></a>

This step action uses the **sendCommand** in the Systems Manager API to run the `AWSEC2-RunSysprep` document for Windows instances before the build instance shuts down for the snapshot. These actions follow [AWS best practices for hardening and cleaning the image](https://aws.amazon.com/articles/public-ami-publishing-hardening-and-clean-up-requirements/).

**Default Timeout: **60 minutes

**Max Timeout: **720 minutes (12 hours)

You can override the default with `timeoutSeconds`, up to the maximum shown. A value above the maximum fails validation.

**Rollback: **There is no rollback for this step action.

**Inputs: **The following table includes supported inputs for this step action.


| Input name | Description | Type | Required | Default | Constraints | 
| --- | --- | --- | --- | --- | --- | 
| instanceId | The ID of the instance to run the AWSEC2-RunSysprep document on. | String | Yes |  | This must be the output instance ID from the workflow step that launched the instance for this workflow. | 

**Outputs: **The following table includes outputs for this step action.


| Output name | Description | Type | 
| --- | --- | --- | 
| runCommandId | The ID of the Systems Manager sendCommand that ran the AWSEC2-RunSysprep document on the instance. | String | 
| status | The status returned from the Systems Manager sendCommand. | String | 
| output | Output returned from the Systems Manager sendCommand. | String | 

**Example**

Specify the step action in the workflow document.

```
- name: {{RunSysprep}}
  action: RunSysPrep
  onFailure: Abort
  inputs:
      instanceId.$: $.stepOutputs.{{LaunchStep}}.instanceId
```

Use the output of the step action value in the workflow document.

```
$.stepOutputs.{{RunSysprep}}.status
```

## SanitizeInstance
<a name="wfdoc-step-action-sanitize-instance"></a>

This step action runs the recommended sanitize script for Linux instances before the build instance shuts down for the snapshot. The sanitize script helps ensure that the final image follows security best practices, and that build artifacts or settings that should not carry over to your snapshot are removed. For more information about the script, see [Required post-build clean up](security-best-practices.md#post-build-cleanup). This step action does not apply to container images.

Image Builder uses the **sendCommand** in the Systems Manager API to run this script. For more information, see [AWS Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/execute-remote-commands.html).

**Default Timeout: **60 minutes

**Max Timeout: **720 minutes (12 hours)

You can override the default with `timeoutSeconds`, up to the maximum shown. A value above the maximum fails validation.

**Rollback: **There is no rollback for this step action.

**Inputs: **The following table includes supported inputs for this step action.


| Input name | Description | Type | Required | Default | Constraints | 
| --- | --- | --- | --- | --- | --- | 
| instanceId | The ID of the instance to sanitize. | String | Yes |  | This must be the output instance ID from the workflow step that launched the instance for this workflow. | 

**Outputs: **The following table includes outputs for this step action.


| Output name | Description | Type | 
| --- | --- | --- | 
| runCommandId | The ID of the Systems Manager sendCommand that ran the sanitize script on the instance. | String | 
| status | The status returned from the Systems Manager sendCommand. | String | 
| output | Output returned from the Systems Manager sendCommand. | String | 

**Example**

Specify the step action in the workflow document.

```
- name: {{SanitizeStep}}
  action: SanitizeInstance
  onFailure: Abort
  inputs:
      instanceId: $.stepOutputs.{{LaunchStep}}.instanceId
```

Use the output of the step action value in the workflow document.

```
$.stepOutputs.{{SanitizeStep}}.status
```

## TerminateInstance
<a name="wfdoc-step-action-terminate-instance"></a>

This step action terminates the instance that you specify with the `instanceId` input. By default, it initiates termination and moves to the next step without waiting. A background process handles cleanup if termination encounters EC2 service errors. To wait for full termination before proceeding, set the `waitForTermination` input to `true`.

**Default Timeout: **30 minutes

**Max Timeout: **720 minutes (12 hours)

You can override the default with `timeoutSeconds`, up to the maximum shown. A value above the maximum fails validation.

**Rollback: **There is no rollback for this step action.

**Inputs: **The following table includes supported inputs for this step action.


| Input name | Description | Type | Required | Default | Constraints | 
| --- | --- | --- | --- | --- | --- | 
| instanceId | The ID of the instance to terminate. | String | Yes | None | None | 
| waitForTermination | Specifies whether the step waits for the instance to reach the terminated state before proceeding. When set to true, the step waits for full termination (10 seconds to several minutes). | Boolean | No | false | true \| false | 

**Outputs: **There are no outputs for this step action.

**Example**

Specify the step action in the workflow document.

```
- name: {{TerminateInstance}}
  action: TerminateInstance
  onFailure: Continue
  inputs:
      instanceId.$: {{i-1234567890abcdef0}}
      waitForTermination: {{false}}
```

## WaitForAction
<a name="wfdoc-step-action-waitfor"></a>

This step action pauses the running workflow and waits to receive an external action from the Image Builder **SendWorkflowStepAction** API action. This step publishes an EventBridge event to your default EventBridge event bus with detail type `EC2 Image Builder Workflow Step Waiting`. The step can also send an SNS notification if you provide an SNS Topic ARN, or invoke a Lambda function asynchronously if you provide a Lambda function name.

**How the pause and resume works**  
When a `WaitForAction` step runs, Image Builder sets the step status to `WAITING` and publishes an EventBridge event (detail type `EC2 Image Builder Workflow Step Waiting`). If you provide `snsTopicArn`, it also sends an Amazon SNS notification. If you provide `lambdaFunctionName`, it invokes that function asynchronously. The workflow stays paused until one of the following happens:
+ You call **SendWorkflowStepAction** with `RESUME` to continue, or `STOP` to end the workflow.
+ The step reaches its timeout (default 3 days, maximum 7 days), and the workflow fails.

The `reason` that you pass to **SendWorkflowStepAction** is stored with the step and is available to later steps as the step's `reason` output.

**Default Timeout: **3 days

**Max Timeout: **7 days (604,800 seconds)

You can override the default with `timeoutSeconds`, up to the maximum shown. A value above the maximum fails validation.

**Rollback: **There is no rollback for this step action.

**Inputs: **The following table includes supported inputs for this step action.


| Input name | Description | Type | Required | Default | Constraints | 
| --- | --- | --- | --- | --- | --- | 
| snsTopicArn | An optional SNS topic ARN to send a notification to when the workflow step is pending. | String | No |  |  | 
| lambdaFunctionName | An optional name or ARN of the Lambda function to invoke asynchronously when the workflow step is pending. | String | No |  |  | 
| payload | JSON string used as message for SNS and payload for Lambda. If provided, a custom payload is wrapped in default message/payload, used for SNS and Lambda respectively. If not provided, generates default message/payload. | String | No |  | Must be valid JSON string, max 16 KiB | 

**Outputs: **The following table includes outputs for this step action.


| Output name | Description | Type | 
| --- | --- | --- | 
| action | The action that the SendWorkflowStepAction API action returns. | String (RESUME or STOP) | 
| reason | The reason for the returned action. | String | 

**IAM permissions required**

Your custom execution role must have the following permissions to use this step action:

**Allow actions**
+ `lambda:InvokeFunction`

**Specify resources**
+ `arn:aws:lambda:{{us-west-2}}:{{111122223333}}:function:{{function-name}}`
+ `arn:aws:lambda:{{us-west-2}}:{{111122223333}}:function:*`

**Example**

Specify the step action in the workflow document with SNS notification.

```
- name: {{SendEventAndWait}}
  action: WaitForAction
  onFailure: Abort
  inputs:
    snsTopicArn: arn:aws:sns:{{us-west-2}}:{{111122223333}}:{{ExampleTopic}}
```

Specify the step action in the workflow document with Lambda function invocation.

```
- name: {{SendEventAndWaitWithLambda}}
  action: WaitForAction
  onFailure: Abort
  inputs:
    lambdaFunctionName: {{ExampleFunction}}
    payload: |
      {
        "imageId": "{{ $.stepOutputs.CreateImageFromInstance.imageId }}",
        "region": "us-west-2"
      }
```

Use the output of the step action value in the workflow document.

```
$.stepOutputs.{{SendEventAndWait}}.reason
```

## WaitForSSMAgent
<a name="wfdoc-step-action-wait-for-ssm-agent"></a>

This step action waits for an EC2 instance to become manageable by AWS Systems Manager after expected periods of unresponsiveness. It's particularly valuable for workflows with known instance interruptions, such as system reboots, OS upgrades, or platform-specific operations that temporarily disconnect the instance from SSM. Image Builder monitors the instance until it regains SSM connectivity or times out.

**Default Timeout: **60 minutes

**Max Timeout: **180 minutes (3 hours)

You can override the default with `timeoutSeconds`, up to the maximum shown. A value above the maximum fails validation.

**Rollback: **There is no rollback for this step action.

**Inputs: **The following table includes supported inputs for this step action.


| Input name | Description | Type | Required | Default | Constraints | 
| --- | --- | --- | --- | --- | --- | 
| instanceId | The ID of the instance to monitor for SSM connectivity. | String | Yes |  | Must be a valid EC2 instance ID | 

**Outputs: **The following table includes outputs for this step action.


| Output name | Description | Type | 
| --- | --- | --- | 
| status | Connection status of SSM Agent. | String | 

**Example**

Specify the step action in the workflow document.

```
- name: {{WaitForInstanceAfterReboot}}
  action: WaitForSSMAgent
  onFailure: Abort
  timeoutSeconds: 900
  inputs:
    instanceId.$: $.stepOutputs.LaunchStep.instanceId
```

Use the output of the step action value in the workflow document.

```
$.stepOutputs.{{WaitForInstanceAfterReboot}}.status
```