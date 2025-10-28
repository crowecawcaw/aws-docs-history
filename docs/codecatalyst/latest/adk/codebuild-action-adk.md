# AWS CodeBuild action using ADK

The following example action initiates a build in AWS CodeBuild. CodeBuild is an AWS service that compiles
source code, runs tests, and packages the code into artifacts. For more information, see the
[AWS CodeBuild Documentation](../../../codebuild/index.md "../../../codebuild/index.md").

This action invokes the AWS Command Line Interface (AWS CLI), which is preinstalled on the action's runtime
environment image within CodeCatalyst. The output of the CLI command is streamed to the
console using `stdout`. For more information about what tools are installed
on the runtime image, see [Curated images](../userguide/build-images.md#build-curated-images "../userguide/build-images.md#build-curated-images").

###### Topics

- [Prerequisites](#prerequisites-codebuild "#prerequisites-codebuild")
- [Update the action definition](#update-action-definition-codebuild "#update-action-definition-codebuild")
- [Update the action code](#update-action-code-codebuild "#update-action-code-codebuild")
- [Validate the action within the CodeCatalyst
  workflow](#validate-action-google-script "#validate-action-google-script")

## Prerequisites

Complete all of the steps in [Getting started with the Action Development Kit](getting-started.md "getting-started.md") before
moving on with developing the action.

### Languages and toolchains

In this example, we'll develop an action using npm and TypeScript.

## Update the action definition

Update the action definition (`action.yml`) that was generated in [Step 3: Initialize your action project](getting-started.md#initialize-action-workspace "getting-started.md#initialize-action-workspace") with the following `AWSCodeBuildProject` and `AWSRegion`
input parameters:

```
SchemaVersion: '1.0'
    Name: 'AWSCodeBuildAction Action'
    Version: '0.0.0'
    Description: 'This Action starts a build in CodeBuild'
    Configuration:
      AWSCodeBuildProject:
        Description: 'Project name for AWS CodeBuild project'
        Required: true
        DisplayName: 'AWSCodeBuildProject'
        Type: string
      AWSRegion:
        Description: 'AWS Region'
        Required: false
        DisplayName: 'AWSRegion'
        Type: string
    Environment:
      Required: true
    Runs:
      Using: 'node16'
      Main: 'dist/index.js'
```

## Update the action code

Update the
entry
point code in the `lib/index.ts` file that was
generated in [Step 4: Bootstrap the action code](getting-started.md#bootstrap-action-code "getting-started.md#bootstrap-action-code"):

```
// @ts-ignore
    import * as core from '@aws/codecatalyst-adk-core';
    // @ts-ignore
    import * as codecatalystProject from '@aws/codecatalyst-project';
    // @ts-ignore
    import * as codecatalystSpace from '@aws/codecatalyst-space';

    try {
      // Get inputs from the action
     const input_AWSCodeBuildProject = core.getInput('AWSCodeBuildProject'); // Project name for AWS CodeBuild project
     console.log(input_AWSCodeBuildProject);
     const input_AWSRegion = core.getInput('AWSRegion'); // AWS Region
     console.log(input_AWSRegion);

      // Interact with codecatalyst entities
      console.log(`Current CodeCatalyst space ${codecatalystSpace.getSpace().name}`);
      console.log(`Current codecatalyst project ${codecatalystProject.getProject().name}`);
      console.log(`AWS Region ${input_AWSRegion}`);

      // Action Code start

      console.log(core.command(`aws codebuild start-build --project-name ${input_AWSCodeBuildProject}`));
      // Set outputs of the action

    } catch(error) {
      core.setFailed(`Action Failed, reason: ${error}`);
    }
```

After bootstrapping and updating the action code, continue with [Step 4: Bootstrap the action code](getting-started.md#bootstrap-action-code "getting-started.md#bootstrap-action-code")
to complete the local build.

## Validate the action within the CodeCatalyst

workflow

After [Testing an action](testing-action.md "testing-action.md"),
validate
the action.

**To validate the action**

1. Open the CodeCatalyst console at [https://codecatalyst.aws/](https://codecatalyst.aws/ "https://codecatalyst.aws/").
2. Navigate to your project.
3. In the navigation pane, choose **CI/CD**, and then choose **Workflows**.
4. Choose the workflow with the action that you want to validate, then view
   **Logs** to confirm a successful run.
