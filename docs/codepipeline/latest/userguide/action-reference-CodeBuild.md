# AWS CodeBuild build and test action

reference

Allows you to run builds and tests as part of your pipeline. When you run a CodeBuild build or
test action, commands specified in the buildspec are run inside of a CodeBuild container. All
artifacts that are specified as input artifacts to a CodeBuild action are available inside of
the container running the commands. CodeBuild can provide either a build or test action. For
more information, see the [AWS CodeBuild User Guide](../../../codebuild/latest/userguide.md "../../../codebuild/latest/userguide.md").

When you use the CodePipeline wizard in the console to create a build project, the CodeBuild build
project shows the source provider is CodePipeline. When you create a build project in the CodeBuild
console, you cannot specify CodePipeline as the source provider, but adding the build action to
your pipeline adjusts the source in the CodeBuild console. For more information, see [ProjectSource](../../../codebuild/latest/APIReference/API_ProjectSource.md "../../../codebuild/latest/APIReference/API_ProjectSource.md") in the _AWS CodeBuild API Reference_.

###### Topics

- [Action type](#action-reference-CodeBuild-type "#action-reference-CodeBuild-type")
- [Configuration parameters](#action-reference-CodeBuild-config "#action-reference-CodeBuild-config")
- [Input artifacts](#action-reference-CodeBuild-input "#action-reference-CodeBuild-input")
- [Output artifacts](#action-reference-CodeBuild-output "#action-reference-CodeBuild-output")
- [Output variables](#action-reference-CodeBuild-variables "#action-reference-CodeBuild-variables")
- [Service role permissions: CodeBuild action](#edit-role-codebuild "#edit-role-codebuild")
- [Action declaration (CodeBuild
  example)](#action-reference-CodeBuild-example "#action-reference-CodeBuild-example")
- [See also](#action-reference-CodeBuild-links "#action-reference-CodeBuild-links")

## Action type

- Category: `Build` or `Test`
- Owner: `AWS`
- Provider: `CodeBuild`
- Version: `1`

## Configuration parameters

**ProjectName**

Required: Yes

`ProjectName` is the name of the build project in CodeBuild.

**PrimarySource**

Required: Conditional

The value of the `PrimarySource` parameter must be the name of
one of the input artifacts to the action. CodeBuild looks for the buildspec file
and runs the buildspec commands in the directory that contains the unzipped
version of this artifact.

This parameter is required if multiple input artifacts are specified for a
CodeBuild action. When there is only one source artifact for the action, the
`PrimarySource` artifact defaults to that artifact.

**BatchEnabled**

Required: No

The Boolean value of the `BatchEnabled` parameter allows the
action to run multiple builds in the same build execution.

When this option is enabled, the `CombineArtifacts` option is
available.

For pipeline examples with batch builds enabled, see [CodePipeline integration with
CodeBuild and batch builds](../../../codebuild/latest/userguide/sample-pipeline-batch.md "../../../codebuild/latest/userguide/sample-pipeline-batch.md").

**BuildspecOverride**

Required: No

An inline buildspec definition or buildspec file declaration that
overrides the latest one defined in the build project, for this build only.
The buildspec defined on the project is not changed.

If this value is set, it can be one of the following:

- An inline buildspec definition. For more information, see the
  syntax reference at [Buildspec syntax](../../../codebuild/latest/userguide/build-spec-ref.md#build-spec-ref-syntax "../../../codebuild/latest/userguide/build-spec-ref.md#build-spec-ref-syntax").
- The path to an alternate buildspec file relative to the value of
  the built-in `CODEBUILD_SRC_DIR` environment variable or
  the path to an S3 bucket. The bucket must be in the same
  AWS Region as the build project. Specify the buildspec file using
  its ARN (for example,
  `arn:aws:s3:::my-codebuild-sample2/buildspec.yml`).
  If this value is not provided or is set to an empty string, the
  source code must contain a buildspec file in its root directory. For
  more information about adding a path, see [Buildspec File Name and Storage Location](../../../codebuild/latest/userguide/build-spec-ref.md#build-spec-ref-name-storage "../../../codebuild/latest/userguide/build-spec-ref.md#build-spec-ref-name-storage").

###### Note

Since this property allows you to change the build commands that will
run in the container, you should note that an IAM principal with the
ability to call this API and set this parameter can override the default
settings. Moreover, we encourage that you use a trustworthy buildspec
location like a file in your source repository or a Amazon S3 bucket.

**CombineArtifacts**

Required: No

The Boolean value of the `CombineArtifacts` parameter combines
all build artifacts from a batch build into a single artifact file for the
build action.

To use this option, the `BatchEnabled` parameter must be
enabled.

**EnvironmentVariables**

Required: No

The value of this parameter is used to set environment variables for the
CodeBuild action in your pipeline. The value for the
`EnvironmentVariables` parameter takes the form of a JSON
array of environment variable objects. See the example parameter in [Action declaration (CodeBuild
example)](#action-reference-CodeBuild-example "#action-reference-CodeBuild-example").

Each object has three parts, all of which are strings:

- `name`: The name or key of the environment variable.
- `value`: The value of the environment variable. When
  using the `PARAMETER_STORE` or
  `SECRETS_MANAGER` type, this value must be the name
  of a parameter you have already stored in AWS Systems Manager
  Parameter Store or a secret you have already stored in AWS
  Secrets Manager, respectively.

###### Note

We strongly discourage the use of environment variables to
store sensitive values, especially AWS credentials. When you
use the CodeBuild console or AWS CLI, environment variables are
displayed in plain text. For sensitive values, we recommend that
you use the `SECRETS_MANAGER` type instead.

- `type`: (Optional) The type of environment variable.
  Valid values are `PARAMETER_STORE`,
  `SECRETS_MANAGER`, or `PLAINTEXT`. When
  not specified, this defaults to `PLAINTEXT`.

###### Note

When you enter the `name`, `value`, and
`type` for your environment variables configuration,
especially if the environment variable contains CodePipeline output variable
syntax, do not exceed the 1000-character limit for the configuration’s
value field. A validation error is returned when this limit is
exceeded.

For more information, see [EnvironmentVariable](../../../codebuild/latest/APIReference/API_EnvironmentVariable.md "../../../codebuild/latest/APIReference/API_EnvironmentVariable.md") in the AWS CodeBuild API Reference. For an
example CodeBuild action with an environment variable that resolves to the
GitHub branch name, see [Example: Use a BranchName
variable with CodeBuild environment variables](actions-variables.md#actions-variables-examples-env-branchname "actions-variables.md#actions-variables-examples-env-branchname").

## Input artifacts

- **Number of artifacts:**
  `1 to 5`
- **Description:** CodeBuild looks for the buildspec
  file and runs the buildspec commands from the directory of the primary source
  artifact. When either a single input source is specified or when more than one
  input source is specified for the CodeBuild action, the single artifact, or the
  primary artifact in the case of multiple input sources, must be set using the
  `PrimarySource` action configuration parameter in CodePipeline.

Each input artifact is extracted to its own directory, the locations of which
are stored in environment variables. The directory for the primary source
artifact is made available with `$CODEBUILD_SRC_DIR`. The directories
for all other input artifacts are made available with
`$CODEBUILD_SRC_DIR_yourInputArtifactName`.

###### Note

The artifact configured in your CodeBuild project becomes the input artifact
used by the CodeBuild action in your pipeline.

## Output artifacts

- **Number of artifacts:**
  `0 to 5`
- **Description:** These can be used to make the
  artifacts that are defined in the CodeBuild buildspec file available to subsequent
  actions in the pipeline. When only one output artifact is defined, this artifact
  can be defined directly under the `artifacts` section of the
  buildspec file. When more than one output artifact is specified, all artifacts
  referenced must be defined as secondary artifacts in the buildspec file. The
  names of the output artifacts in CodePipeline must match the artifact identifiers in
  the buildspec file.

###### Note

The artifact configured in your CodeBuild project becomes the CodePipeline input
artifact in your pipeline action.

If the `CombineArtifacts` parameter is selected for batch builds,
the output artifact location contains the combined artifacts from multiple
builds that were run in the same execution.

## Output variables

This action will produce as variables all environment variables that were exported as
part of the build. For more details on how to export environment variables, see [EnvironmentVariable](../../../codebuild/latest/APIReference/API_EnvironmentVariable.md "../../../codebuild/latest/APIReference/API_EnvironmentVariable.md") in the
_AWS CodeBuild API Guide_.

For more information about using CodeBuild environment variables in CodePipeline, see the
examples in [CodeBuild action output
variables](reference-variables.md#reference-variables-list-configured-codebuild "reference-variables.md#reference-variables-list-configured-codebuild"). For a list of the
environment variables you can use in CodeBuild, see [Environment variables in build
environments](../../../codebuild/latest/userguide/build-env-ref-env-vars.md "../../../codebuild/latest/userguide/build-env-ref-env-vars.md") in the _AWS CodeBuild User
Guide_.

## Service role permissions: CodeBuild action

For CodeBuild support, add the following to your policy statement:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "codebuild:BatchGetBuilds",
 "codebuild:StartBuild",
 "codebuild:BatchGetBuildBatches",
 "codebuild:StartBuildBatch"
 ],
 "Resource": [
 "arn:aws:codebuild:*:`111122223333`:project/[[ProjectName]]"
 ],
 "Effect": "Allow"
 }
 ]
}`

```

## Action declaration (CodeBuild

example)

YAML

```
Name: Build
Actions:
  - Name: PackageExport
    ActionTypeId:
      Category: Build
      Owner: AWS
      Provider: CodeBuild
      Version: '1'
    RunOrder: 1
    Configuration:
      BatchEnabled: 'true'
      CombineArtifacts: 'true'
      ProjectName: my-build-project
      PrimarySource: MyApplicationSource1
      EnvironmentVariables: '[{"name":"TEST_VARIABLE","value":"TEST_VALUE","type":"PLAINTEXT"},{"name":"ParamStoreTest","value":"PARAMETER_NAME","type":"PARAMETER_STORE"}]'
    OutputArtifacts:
      - Name: MyPipeline-BuildArtifact
    InputArtifacts:
      - Name: MyApplicationSource1
      - Name: MyApplicationSource2

```

JSON

```
{
    "Name": "Build",
    "Actions": [
        {
            "Name": "PackageExport",
            "ActionTypeId": {
                "Category": "Build",
                "Owner": "AWS",
                "Provider": "CodeBuild",
                "Version": "1"
            },
            "RunOrder": 1,
            "Configuration": {
                "BatchEnabled": "true",
                "CombineArtifacts": "true",
                "ProjectName": "my-build-project",
                "PrimarySource": "MyApplicationSource1",
                "EnvironmentVariables": "[{\"name\":\"TEST_VARIABLE\",\"value\":\"TEST_VALUE\",\"type\":\"PLAINTEXT\"},{\"name\":\"ParamStoreTest\",\"value\":\"PARAMETER_NAME\",\"type\":\"PARAMETER_STORE\"}]"
            },
            "OutputArtifacts": [
                {
                    "Name": "MyPipeline-BuildArtifact"
                }
            ],
            "InputArtifacts": [
                {
                    "Name": "MyApplicationSource1"
                },
                {
                    "Name": "MyApplicationSource2"
                }
            ]
        }
    ]
}
```

## See also

The following related resources can help you as you work with this action.

- [AWS CodeBuild User Guide](../../../codebuild/latest/userguide.md "../../../codebuild/latest/userguide.md") – For an example
  pipeline with a CodeBuild action, see [Use CodePipeline with
  CodeBuild to Test Code and Run Builds](../../../codebuild/latest/userguide/how-to-create-pipeline.md "../../../codebuild/latest/userguide/how-to-create-pipeline.md"). For examples of projects with
  multiple input and output CodeBuild artifacts, see [CodePipeline
  Integration with CodeBuild and Multiple Input Sources and Output Artifacts
  Sample](../../../codebuild/latest/userguide/sample-pipeline-multi-input-output.md "../../../codebuild/latest/userguide/sample-pipeline-multi-input-output.md") and [Multiple Input Sources and Output Artifacts Sample](../../../codebuild/latest/userguide/sample-multi-in-out.md "../../../codebuild/latest/userguide/sample-multi-in-out.md") .
- [Tutorial: Create a pipeline that builds and
  tests your Android app with AWS Device Farm](tutorials-codebuild-devicefarm.md "tutorials-codebuild-devicefarm.md") – This tutorial
  provides a sample buildspec file and sample application to create a pipeline
  with a GitHub source that builds and tests an Android app with CodeBuild and
  AWS Device Farm.
- [Build Specification Reference
  for CodeBuild](../../../codebuild/latest/userguide/build-spec-ref.md "../../../codebuild/latest/userguide/build-spec-ref.md") – This reference topic provides definitions and
  examples for understanding CodeBuild buildspec files. For a list of the environment
  variables you can use in CodeBuild, see [Environment variables in
  build environments](../../../codebuild/latest/userguide/build-env-ref-env-vars.md "../../../codebuild/latest/userguide/build-env-ref-env-vars.md") in the _AWS CodeBuild User
  Guide_.
