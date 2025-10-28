# CodeCommit source action reference

Starts the pipeline when a new commit is made on the configured CodeCommit repository and
branch.

If you use the console to create or edit the pipeline, CodePipeline creates an EventBridge rule that
starts your pipeline when a change occurs in the repository.

###### Note

For Amazon ECR, Amazon S3, or CodeCommit sources, you can also create a source override using input
transform entry to use the `revisionValue` in EventBridge for your pipeline event,
where the `revisionValue` is derived from the source event variable for your
object key, commit, or image ID. For more information, see the optional step for input
transform entry included in the procedures under [Amazon ECR source actions and EventBridge resources](create-cwe-ecr-source.md "create-cwe-ecr-source.md"), [Connecting to Amazon S3 source actions with a
source enabled for events](create-S3-source-events.md "create-S3-source-events.md"), or [CodeCommit source actions and EventBridge](triggering.md "triggering.md").

You must have already created a CodeCommit repository before you connect the pipeline through a
CodeCommit action.

After a code change is detected, you have the following options for passing the code to
subsequent actions:

- **Default** – Configures the CodeCommit source
  action to output a ZIP file with a shallow copy of your commit.
- **Full clone** – Configures the source action
  to output a Git URL reference to the repository for subsequent actions.

Currently, the Git URL reference can only be used by downstream CodeBuild actions to
clone the repo and associated Git metadata. Attempting to pass a Git URL reference
to non-CodeBuild actions results in an error.

###### Topics

- [Action type](#action-reference-CodeCommit-type "#action-reference-CodeCommit-type")
- [Configuration parameters](#action-reference-CodeCommit-config "#action-reference-CodeCommit-config")
- [Input artifacts](#action-reference-CodeCommit-input "#action-reference-CodeCommit-input")
- [Output artifacts](#action-reference-CodeCommit-output "#action-reference-CodeCommit-output")
- [Output variables](#action-reference-CodeCommit-variables "#action-reference-CodeCommit-variables")
- [Service role permissions: CodeCommit action](#edit-role-codecommit "#edit-role-codecommit")
- [Example action
  configuration](#action-reference-CodeCommit-example "#action-reference-CodeCommit-example")
- [See also](#action-reference-CodeCommit-links "#action-reference-CodeCommit-links")

## Action type

- Category: `Source`
- Owner: `AWS`
- Provider: `CodeCommit`
- Version: `1`

## Configuration parameters

**RepositoryName**

Required: Yes

The name of the repository where source changes are to be detected.

**BranchName**

Required: Yes

The name of the branch where source changes are to be detected.

**PollForSourceChanges**

Required: No

`PollForSourceChanges` controls whether CodePipeline polls the CodeCommit
repository for source changes. We recommend that you use CloudWatch Events to detect
source changes instead. For more information about configuring CloudWatch Events, see
[Migrate polling pipelines
(CodeCommit source) (CLI)](update-change-detection.md#update-change-detection-cli-codecommit "update-change-detection.md#update-change-detection-cli-codecommit") or [Migrate polling pipelines
(CodeCommit source) (AWS CloudFormation template)](update-change-detection.md#update-change-detection-cfn-codecommit "update-change-detection.md#update-change-detection-cfn-codecommit").

###### Important

If you intend to configure a CloudWatch Events rule, you must set
`PollForSourceChanges` to `false` to avoid
duplicate pipeline executions.

Valid values for this parameter:

- `true`: If set, CodePipeline polls your repository for source
  changes.

###### Note

If you omit `PollForSourceChanges`, CodePipeline defaults
to polling your repository for source changes. This behavior is
the same as if `PollForSourceChanges` is included and
set to `true`.

- `false`: If set, CodePipeline does not poll your repository
  for source changes. Use this setting if you intend to configure a
  CloudWatch Events rule to detect source changes.

\***\*OutputArtifactFormat\*\***

Required: No

The output artifact format. Values can be either
`CODEBUILD_CLONE_REF` or `CODE_ZIP`. If
unspecified, the default is `CODE_ZIP`.

###### Important

The `CODEBUILD_CLONE_REF` option can only be used by CodeBuild
downstream actions.

If you choose this option, you need to add the
`codecommit:GitPull` permission to your CodeBuild service
role as shown in [Add CodeBuild GitClone permissions for CodeCommit
source actions](troubleshooting.md#codebuild-role-codecommitclone "troubleshooting.md#codebuild-role-codecommitclone"). You also need to
add the `codecommit:GetRepository` permission to your CodePipeline
service role as shown in [Add permissions to the CodePipeline
service role](how-to-custom-role.md#how-to-update-role-new-services "how-to-custom-role.md#how-to-update-role-new-services"). For a tutorial
that shows you how to use the **Full clone** option,
see [Tutorial: Use full clone with a CodeCommit pipeline
source](tutorials-codecommit-gitclone.md "tutorials-codecommit-gitclone.md").

## Input artifacts

- **Number of artifacts:**
  `0`
- **Description:** Input artifacts do not apply for
  this action type.

## Output artifacts

- **Number of artifacts:**
  `1`
- **Description:** The output artifact of this
  action is a ZIP file that contains the contents of the configured repository and
  branch at the commit specified as the source revision for the pipeline
  execution. The artifacts generated from the repository are the output artifacts
  for the CodeCommit action. The source code commit ID is displayed in CodePipeline as the
  source revision for the triggered pipeline execution.

## Output variables

When configured, this action produces variables that can be referenced by the action
configuration of a downstream action in the pipeline. This action produces variables
which can be viewed as output variables, even if the action doesn't have a namespace.
You configure an action with a namespace to make those variables available to the
configuration of downstream actions.

For more information, see [Variables reference](reference-variables.md "reference-variables.md").

**CommitId**

The CodeCommit commit ID that triggered the pipeline execution. Commit IDs are
the full SHA of the commit.

**CommitMessage**

The description message, if any, associated with the commit that triggered
the pipeline execution.

**RepositoryName**

The name of the CodeCommit repository where the commit that triggered the
pipeline was made.

**BranchName**

The name of the branch for the CodeCommit repository where the source change
was made.

**AuthorDate**

The date when the commit was authored, in timestamp format.

**CommitterDate**

The date when the commit was committed, in timestamp format.

## Service role permissions: CodeCommit action

When CodePipeline runs the action, the CodePipeline service role policy requires the following permissions, appropriately scoped
down to the pipeline resource ARN in order to maintain access with least
privilege. For example, add the following to your policy statement:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "codecommit:CancelUploadArchive",
 "codecommit:GetBranch",
 "codecommit:GetCommit",
 "codecommit:GetRepository",
 "codecommit:GetUploadArchiveStatus",
 "codecommit:UploadArchive"
 ],
 "Resource": [
 "arn:aws:codecommit:*:`111122223333`:[[codecommitRepostories]]"
 ]
 }
 ]
}`

```

## Example action

configuration

### Example for default output artifact format

YAML

```
name: Source
actionTypeId:
  category: Source
  owner: AWS
  provider: CodeCommit
  version: '1'
runOrder: 1
configuration:
  BranchName: main
  PollForSourceChanges: 'false'
  RepositoryName: MyWebsite
outputArtifacts:
  - name: Artifact_MyWebsiteStack
inputArtifacts: []
region: us-west-2
namespace: SourceVariables

```

JSON

```
{
    "name": "Source",
    "actionTypeId": {
        "category": "Source",
        "owner": "AWS",
        "provider": "CodeCommit",
        "version": "1"
    },
    "runOrder": 1,
    "configuration": {
        "BranchName": "main",
        "PollForSourceChanges": "false",
        "RepositoryName": "MyWebsite"
    },
    "outputArtifacts": [
        {
            "name": "Artifact_MyWebsiteStack"
        }
    ],
    "inputArtifacts": [],
    "region": "us-west-2",
    "namespace": "SourceVariables"
}
```

### Example for full clone output artifact format

YAML

```
name: Source
actionTypeId:
  category: Source
  owner: AWS
  provider: CodeCommit
  version: '1'
runOrder: 1
configuration:
  BranchName: main
  OutputArtifactFormat: CODEBUILD_CLONE_REF
  PollForSourceChanges: 'false'
  RepositoryName: MyWebsite
outputArtifacts:
  - name: SourceArtifact
inputArtifacts: []
region: us-west-2
namespace: SourceVariables
```

JSON

```
{
    "name": "Source",
    "actionTypeId": {
        "category": "Source",
        "owner": "AWS",
        "provider": "CodeCommit",
        "version": "1"
    },
    "runOrder": 1,
    "configuration": {
        "BranchName": "main",
        "OutputArtifactFormat": "CODEBUILD_CLONE_REF",
        "PollForSourceChanges": "false",
        "RepositoryName": "MyWebsite"
    },
    "outputArtifacts": [
        {
            "name": "SourceArtifact"
        }
    ],
    "inputArtifacts": [],
    "region": "us-west-2",
    "namespace": "SourceVariables"
}
```

## See also

The following related resources can help you as you work with this action.

- [Tutorial: Create a simple pipeline (CodeCommit
  repository)](tutorials-simple-codecommit.md "tutorials-simple-codecommit.md") – This tutorial
  provides a sample app spec file and sample CodeDeploy application and deployment
  group. Use this tutorial to create a pipeline with a CodeCommit source that deploys
  to Amazon EC2 instances.
