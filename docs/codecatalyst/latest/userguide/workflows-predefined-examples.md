Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Examples of referencing predefined

variables

The following examples show how to reference predefined variables in the workflow
definition file.

For more information about predefined variables, see [Using predefined variables](workflows-using-predefined-variables.md "workflows-using-predefined-variables.md").

###### Examples

- [Example:
  Referencing the "CommitId" predefined variable](#workflows-working-with-variables-ex-refer-action "#workflows-working-with-variables-ex-refer-action")
- [Example: Referencing
  the "BranchName" predefined variable](#workflows-working-with-variables-ex-branch "#workflows-working-with-variables-ex-branch")

## Example:

Referencing the "CommitId" predefined variable

The following example shows you how to refer to the `CommitId`
predefined variable in the `MyBuildAction` action. The
`CommitId` variable is output automatically by
CodeCatalyst. For more information, see
[List of predefined variables](workflow-ref-action-variables.md "workflow-ref-action-variables.md").

Although the example shows the variable being used in the build action, you can
use `CommitId` in any action.

```
MyBuildAction:
    Identifier: aws/build@v1
    Inputs:
      Sources:
        - WorkflowSource
    Configuration:
      Steps:
      #Build Docker image and tag it with a commit ID
        - Run: docker build -t image-repo/my-docker-image:latest .
        - Run: docker tag image-repo/my-docker-image:**${WorkflowSource.CommitId}**
```

## Example: Referencing

the "BranchName" predefined variable

The following example shows you how to refer to the `BranchName`
predefined variable in the `CDKDeploy` action. The
`BranchName` variable is output automatically by
CodeCatalyst. For more information, see
[List of predefined variables](workflow-ref-action-variables.md "workflow-ref-action-variables.md").

Although the example shows the variable being used in the **AWS CDK
deploy** action, you can use `BranchName` in any
action.

```
CDKDeploy:
    Identifier: aws/cdk-deploy@v2
    Inputs:
      Sources:
        - WorkflowSource
    Configuration:
      StackName: app-stack-**${WorkflowSource.BranchName}**
```
