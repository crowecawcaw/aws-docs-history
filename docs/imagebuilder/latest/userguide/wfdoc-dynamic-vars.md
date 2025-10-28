# Use dynamic variables in your workflow document

You can use dynamic variables in your workflow documents to represent values
that vary at runtime for your image creation process. Dynamic variable values are
represented as JSONPath selectors with structural nodes that uniquely
identify the target variable.

**JSONPath dynamic workflow variable structure**

```
`$.<document structure>.[<step name>.]<variable name>`
```

The first node after the root ($) refers to the workflow document structure, such as
`stepOutputs`, or in the case of Image Builder system variables, `imageBuilder`.
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

When an input parameter refers to a dynamic variable, the chaining indicator
(`.$`) must be attached to the end of the parameter name, as shown in
the following example.

**Example**

```
 `- name: ApplyTestComponents
 action: ExecuteComponents
 onFailure: Abort
 inputs:
 instanceId.$: "$.stepOutputs.LaunchTestInstance.instanceId"`
```

## Use Image Builder system variables

Image Builder provides the following system variables that you can use in your
workflow document:

| Variable name              | Description                                                                                                                      | Type        | Example value                                                                 |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ----------- | ----------------------------------------------------------------------------- | --------- | ------------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------- | ------- | ------ |
| cloudWatchLogGroup         | The name of the CloudWatch Logs group for output logs. Format: `/aws/imagebuilder/`<recipe-name>``                               | String      | `/aws/imagebuilder/`sampleImageRecipe``                                       |
| cloudWatchLogStream        | The name of the CloudWatch Logs stream for output logs.                                                                          | String      | `1.0.0/1`                                                                     |
| collectImageMetadata       | The setting that directs Image Builder whether to collect instance metadata.                                                     | Boolean     | `true`                                                                        | `false`   |
| collectImageScanFindings   | The current value of the setting that enables Image Builder to collect image scan findings.                                      | Boolean     | `true`                                                                        | `false`   |
| imageBuildNumber           | The build version number of the image.                                                                                           | Integer     | `1`                                                                           |           | imageId             | The AMI id of the base image.                                                                     | String                                                       | `ami-1234567890abcdef1`                        |
| imageName                  | The name of the image.                                                                                                           | String      | `sampleImage`                                                                 |
| imageType                  | The image output type.                                                                                                           | String      | `AMI`                                                                         | `Docker`  |
| imageVersionNumber         | The version number of the image.                                                                                                 | String      | `1.0.0`                                                                       |           | instanceProfileName | The name of the instance profile role that Image Builder uses to launch build and test instances. | String                                                       | `SampleImageBuilderInstanceProfileRole`        |
| platform                   | The operating system platform of the image that's built.                                                                         | String      | `Linux`                                                                       | `Windows` | `MacOS`             |
| s3Logs                     | A JSON object that contains configuration for the S3 logs that Image Builder writes.                                             | JSON object | {'s3Logs': {'s3BucketName': '`sample-bucket`', 's3KeyPrefix': '`ib-logs`'}}   |           | securityGroups      | The security group IDs that apply to build and test instances.                                    | List [String]                                                | `[sg-1234567890abcdef1, sg-11112222333344445]` |
| sourceImageARN             | The Amazon Resource Name (ARN) of the Image Builder image resource that the workflow uses for build and test stages.             | String      | arn:aws:imagebuilder:`us-east-1`:`111122223333`:image/`sampleImage`/`1.0.0/1` |           | subnetId            | The ID of the subnet to launch the build and test instances into.                                 | String                                                       | `subnet-1234567890abcdef1`                     |
| terminateInstanceOnFailure | The current value of the setting that directs Image Builder to terminate the instance on failure or keep it for troubleshooting. | Boolean     | `true`                                                                        | `false`   |                     | workflowPhase                                                                                     | The current stage that's running for the workflow execution. | String                                         | `Build` | `Test` |
| workingDirectory           | The path to the working directory.                                                                                               | String      | `/tmp`                                                                        |
