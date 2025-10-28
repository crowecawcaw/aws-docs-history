# Amazon ECR source action reference

Triggers the pipeline when a new image is pushed to the Amazon ECR repository. This action
provides an image definitions file referencing the URI for the image that was pushed to
Amazon ECR. This source action is often used in conjunction with another source action, such as
CodeCommit, to allow a source location for all other source artifacts. For more information, see
[Tutorial: Create a pipeline with an Amazon ECR
source and ECS-to-CodeDeploy deployment](tutorials-ecs-ecr-codedeploy.md "tutorials-ecs-ecr-codedeploy.md").

When you use the console to create or edit your pipeline, CodePipeline creates an EventBridge rule that
starts your pipeline when a change occurs in the repository.

###### Note

For Amazon ECR, Amazon S3, or CodeCommit sources, you can also create a source override using input
transform entry to use the `revisionValue` in EventBridge for your pipeline event,
where the `revisionValue` is derived from the source event variable for your
object key, commit, or image ID. For more information, see the optional step for input
transform entry included in the procedures under [Amazon ECR source actions and EventBridge resources](create-cwe-ecr-source.md "create-cwe-ecr-source.md"), [Connecting to Amazon S3 source actions with a
source enabled for events](create-S3-source-events.md "create-S3-source-events.md"), or [CodeCommit source actions and EventBridge](triggering.md "triggering.md").

You must have already created an Amazon ECR repository and pushed an image before you connect
the pipeline through an Amazon ECR action.

###### Topics

- [Action type](#action-reference-ECR-type "#action-reference-ECR-type")
- [Configuration parameters](#action-reference-ECR-config "#action-reference-ECR-config")
- [Input artifacts](#action-reference-ECR-input "#action-reference-ECR-input")
- [Output artifacts](#action-reference-ECR-output "#action-reference-ECR-output")
- [Output variables](#action-reference-ECR-variables "#action-reference-ECR-variables")
- [Service role permissions: Amazon ECR action](#edit-role-ecr "#edit-role-ecr")
- [Action declaration (Amazon ECR
  example)](#action-reference-ECR-example "#action-reference-ECR-example")
- [See also](#action-reference-ECR-links "#action-reference-ECR-links")

## Action type

- Category: `Source`
- Owner: `AWS`
- Provider: `ECR`
- Version: `1`

## Configuration parameters

**RepositoryName**

Required: Yes

The name of the Amazon ECR repository where the image was pushed.

**ImageTag**

Required: No

The tag used for the image.

###### Note

If a value for `ImageTag` is not specified, the value
defaults to `latest`.

## Input artifacts

- **Number of artifacts:**
  `0`
- **Description:** Input artifacts do not apply for
  this action type.

## Output artifacts

- **Number of artifacts:**
  `1`
- **Description:** This action produces an artifact

that contains an `imageDetail.json` file that contains the
URI for the image that triggered the pipeline execution. For information about
the `imageDetail.json` file, see [imageDetail.json file for Amazon ECS blue/green
deployment actions](file-reference.md#file-reference-ecs-bluegreen "file-reference.md#file-reference-ecs-bluegreen").

## Output variables

When configured, this action produces variables that can be referenced by the action
configuration of a downstream action in the pipeline. This action produces variables
which can be viewed as output variables, even if the action doesn't have a namespace.
You configure an action with a namespace to make those variables available to the
configuration of downstream actions.

For more information, see [Variables reference](reference-variables.md "reference-variables.md").

**RegistryId**

The AWS account ID associated with the registry that contains the
repository.

**RepositoryName**

The name of the Amazon ECR repository where the image was pushed.

**ImageTag**

The tag used for the image.

###### Note

The `ImageTag` output variable is not output when the
source revision is overridden

**ImageDigest**

The `sha256` digest of the image manifest.

**ImageURI**

The URI for the image.

## Service role permissions: Amazon ECR action

For Amazon ECR support, add the following to your policy statement:

```
{
    "Effect": "Allow",
    "Action": [
        "ecr:DescribeImages"
    ],
    "Resource": "`resource_ARN`"
},
```

For more information about this action, see [Amazon ECR source action reference](action-reference-ECR.md "action-reference-ECR.md").

## Action declaration (Amazon ECR

example)

YAML

```
Name: Source
Actions:
  - InputArtifacts: []
    ActionTypeId:
      Version: '1'
      Owner: AWS
      Category: Source
      Provider: ECR
    OutputArtifacts:
      - Name: SourceArtifact
    RunOrder: 1
    Configuration:
      ImageTag: latest
      RepositoryName: my-image-repo

    Name: ImageSource
```

JSON

```
{
    "Name": "Source",
    "Actions": [
        {
            "InputArtifacts": [],
            "ActionTypeId": {
                "Version": "1",
                "Owner": "AWS",
                "Category": "Source",
                "Provider": "ECR"
            },
            "OutputArtifacts": [
                {
                    "Name": "SourceArtifact"
                }
            ],
            "RunOrder": 1,
            "Configuration": {
                "ImageTag": "latest",
                "RepositoryName": "my-image-repo"
            },
            "Name": "ImageSource"
        }
    ]
},
```

## See also

The following related resources can help you as you work with this action.

- [Tutorial: Create a pipeline with an Amazon ECR
  source and ECS-to-CodeDeploy deployment](tutorials-ecs-ecr-codedeploy.md "tutorials-ecs-ecr-codedeploy.md") – This tutorial
  provides a sample app spec file and sample CodeDeploy application and deployment

group to create a pipeline with a CodeCommit and Amazon ECR source that deploys to Amazon ECS
instances.
