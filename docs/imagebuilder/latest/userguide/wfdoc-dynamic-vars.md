# Use dynamic variables in your workflow document

You can use dynamic variables in your workflow documents to represent values
that vary at runtime for your image creation process. String interpolation for dynamic variables
allows you to embed JSONPath expressions within structured content such as JSON strings.This is
particularly useful when you need to pass runtime values within complex payloads to step actions
like `ExecuteStateMachine` or `WaitForAction`.

To use string interpolation for dynamic variables, wrap JSONPath expressions in double curly braces
`"{{...}}"` within your string content. Only JSONPath expressions wrapped in double curly braces are
processed as variables. Any JSONPath expressions not wrapped in double curly braces are
treated as literal string content.

**JSONPath dynamic workflow variable syntax**

```
`$.<document structure>.[<step name>.]<variable name>`
```

Dynamic variable values are represented as JSONPath selectors with structural nodes that uniquely
identify the target variable. The first node after the root ($) refers to the workflow document structure,
such as `stepOutputs`, or in the case of Image Builder system variables, `imageBuilder`.
The following list contains supported JSONPath workflow document structure nodes.

###### Document structure nodes

- parameters - The workflow parameters
- stepOutputs - Outputs from a step in the same workflow doc
- workflowOutputs - Outputs from a workflow doc that already ran
- imagebuilder - Image Builder system variables
  The `parameters` and `stepOutputs` document structure nodes include
  an optional node for the step name. This helps ensure unique variable names across all of
  the steps.

The final node in the JSONPath is the name of the target variable, such as
`instanceId`.

Each step can refer to the output of any prior step actions with these JSONPath dynamic
variables. This is also known as _chaining, or referencing_. To refer
to output from a prior step action, you might use the following dynamic variable.

```
`$.stepOutputs.`step-name`.`output-name``
```

###### Important

When an input parameter refers to a dynamic variable, the chaining indicator
(`.$`) must be attached to the end of the parameter name.

**Example 1: Input parameter chaining indicator**

The following example shows an input parameter that uses string interpolation to
resolve a dynamic variable in the parameter value at runtime.

```
 `- name: ApplyTestComponents
 action: ExecuteComponents
 onFailure: Abort
 inputs:
 instanceId.$: "$.`stepOutputs`.`LaunchTestInstance`.`instanceId`"`
```

**Example 2: String interpolation in dynamic variables**

The following example demonstrates how dynamic variables use string interpolation to
determine values at runtime.

```
`- name: ValidateImageConfiguration
 action: ExecuteStateMachine
 inputs:
 stateMachineArn: arn:aws:states:`us-east-1`:`111122223333`:stateMachine:ImageValidation
 input: |
 {
 "imageId": "{{ $.stepOutputs.CreateImageFromInstance.imageId }}",
 "region": "us-east-1",
 "buildDate": "{{ $.imagebuilder.dateTime }}",
 "instanceType": "{{ $.stepOutputs.LaunchStep.instanceType }}"
 }`
```

In this example, the JSONPath expressions wrapped in double curly braces are resolved
at runtime:

- `{{ $.stepOutputs.CreateImageFromInstance.imageId }}` - Resolves to the
  actual image ID from the CreateImageFromInstance step
- `{{ $.imagebuilder.dateTime }}` - Resolves to the current build timestamp. See
  [Use Image Builder system variables](#wfdoc-ib-vars "#wfdoc-ib-vars") for a list of Image Builder
  system variables that you can use.
- `{{ $.stepOutputs.LaunchStep.instanceType }}` - Resolves to the instance
  type used in the LaunchStep
  The literal strings like `"region": "us-east-1"` remain unchanged.

###### Note

String interpolation works with any string content in your workflow document,
including multiline strings using the YAML pipe (`|`) operator. The
curly brace requirement acts as an escape mechanism to clearly distinguish between
JSONPath variables and literal text content.

## Use Image Builder system variables

Image Builder provides the following system variables that you can use in your
workflow document:

| Variable name              | Description                                                                                                                      | Type          | Example value                                                                 |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ------------- | ----------------------------------------------------------------------------- | --------- | ------- |
| cloudWatchLogGroup         | The name of the CloudWatch Logs group for output logs.<br>Format: `/aws/imagebuilder/`<recipe-name>``                            | String        | `/aws/imagebuilder/`sampleImageRecipe``                                       |
| cloudWatchLogStream        | The name of the CloudWatch Logs stream for output logs.                                                                          | String        | `1.0.0/1`                                                                     |
| collectImageMetadata       | The setting that directs Image Builder whether to collect instance metadata.                                                     | Boolean       | `true`                                                                        | `false`   |
| collectImageScanFindings   | The current value of the setting that enables Image Builder to collect<br>image scan findings.                                   | Boolean       | `true`                                                                        | `false`   |
| imageBuildNumber           | The build version number of the image.                                                                                           | Integer       | `1`                                                                           |
| imageId                    | The AMI id of the base image.                                                                                                    | String        | `ami-1234567890abcdef1`                                                       |
| imageName                  | The name of the image.                                                                                                           | String        | `sampleImage`                                                                 |
| imageType                  | The image output type.                                                                                                           | String        | `AMI`                                                                         | `Docker`  |
| imageVersionNumber         | The version number of the image.                                                                                                 | String        | `1.0.0`                                                                       |
| instanceProfileName        | The name of the instance profile role that Image Builder uses to launch build and test instances.                                | String        | `SampleImageBuilderInstanceProfileRole`                                       |
| platform                   | The operating system platform of the image that's built.                                                                         | String        | `Linux`                                                                       | `Windows` | `MacOS` |
| s3Logs                     | A JSON object that contains configuration for the S3 logs that Image Builder writes.                                             | JSON object   | {'s3Logs': {'s3BucketName': '`sample-bucket`', 's3KeyPrefix': '`ib-logs`'}}   |
| securityGroups             | The security group IDs that apply to build and test instances.                                                                   | List [String] | `[sg-1234567890abcdef1, sg-11112222333344445]`                                |
| sourceImageARN             | The Amazon Resource Name (ARN) of the Image Builder image resource that the<br>workflow uses for build and test stages.          | String        | arn:aws:imagebuilder:`us-east-1`:`111122223333`:image/`sampleImage`/`1.0.0/1` |
| subnetId                   | The ID of the subnet to launch the build and test instances into.                                                                | String        | `subnet-1234567890abcdef1`                                                    |
| terminateInstanceOnFailure | The current value of the setting that directs Image Builder to terminate the instance on failure or keep it for troubleshooting. | Boolean       | `true`                                                                        | `false`   |
| workflowPhase              | The current stage that's running for the workflow execution.                                                                     | String        | `Build`                                                                       | `Test`    |
| workingDirectory           | The path to the working directory.                                                                                               | String        | `/tmp`                                                                        |
