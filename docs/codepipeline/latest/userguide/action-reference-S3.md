# Amazon S3 source action reference

Triggers the pipeline when a new object is uploaded to the configured bucket and object
key.

###### Note

This reference topic describes the Amazon S3 source action for CodePipeline where the source
location is an Amazon S3 bucket configured for versioning. For reference information about
the Amazon S3 deploy action in CodePipeline, see [Amazon S3 deploy action reference](action-reference-S3Deploy.md "action-reference-S3Deploy.md").

You can create an Amazon S3 bucket to use as the source location for your application
files.

###### Note

When you create your source bucket, make sure you enable versioning on the bucket. If
you want to use an existing Amazon S3 bucket, see [Using
versioning](../../../AmazonS3/latest/dev/Versioning.md "../../../AmazonS3/latest/dev/Versioning.md") to enable versioning on an existing bucket.

If you use the console to create or edit your pipeline, CodePipeline creates an EventBridge rule that
starts your pipeline when a change occurs in the S3 source bucket.

###### Note

For Amazon ECR, Amazon S3, or CodeCommit sources, you can also create a source override using input
transform entry to use the `revisionValue` in EventBridge for your pipeline event,
where the `revisionValue` is derived from the source event variable for your
object key, commit, or image ID. For more information, see the optional step for input
transform entry included in the procedures under [Amazon ECR source actions and EventBridge resources](create-cwe-ecr-source.md "create-cwe-ecr-source.md"), [Connecting to Amazon S3 source actions with a
source enabled for events](create-S3-source-events.md "create-S3-source-events.md"), or [CodeCommit source actions and EventBridge](triggering.md "triggering.md").

You must have already created an Amazon S3 source bucket and uploaded the source files as a

single ZIP file before you connect the pipeline through an Amazon S3 action.

###### Note

When Amazon S3 is the source provider for your pipeline, you may zip your source file or
files into a single .zip and upload the .zip to your source bucket. You may also upload
a single unzipped file; however, downstream actions that expect a .zip file will
fail.

###### Topics

- [Action type](#action-reference-S3-type "#action-reference-S3-type")
- [Configuration parameters](#action-reference-S3-config "#action-reference-S3-config")
- [Input artifacts](#action-reference-S3-input "#action-reference-S3-input")
- [Output artifacts](#action-reference-S3-output "#action-reference-S3-output")
- [Output variables](#action-reference-S3-variables "#action-reference-S3-variables")
- [Service role permissions: S3 source action](#edit-role-s3source "#edit-role-s3source")
- [Action declaration](#action-reference-S3-example "#action-reference-S3-example")
- [See also](#action-reference-S3-links "#action-reference-S3-links")

## Action type

- Category: `Source`
- Owner: `AWS`
- Provider: `S3`
- Version: `1`

## Configuration parameters

**S3Bucket**

Required: Yes

The name of the Amazon S3 bucket where source changes are to be
detected.

**S3ObjectKey**

Required: Yes

The name of the Amazon S3 object key where source changes are to be
detected.

**AllowOverrideForS3ObjectKey**

Required: No

`AllowOverrideForS3ObjectKey` controls whether source overrides
from `StartPipelineExecution` can override the already configured
`S3ObjectKey` in the source action. For more information on
source overrides with the S3 Object Key, see [Start a pipeline with a source
revision override](pipelines-trigger-source-overrides.md "pipelines-trigger-source-overrides.md").

###### Important

If you omit `AllowOverrideForS3ObjectKey`, CodePipeline defaults
the ability to override the S3 ObjectKey in the source action by setting
this parameter to `false`.

Valid values for this parameter:

- `true`: If set, the pre-configured S3 Object Key can be
  overridden by source revision overrides during a pipeline
  execution.

###### Note

If you intend to allow all CodePipeline users the ability to override
the pre-configured S3 Object Key while starting a new pipeline
execution, you must set `AllowOverrideForS3ObjectKey`
to `true`.

- `false`:

If set, CodePipeline will not allow the S3 Object Key to be overridden
using source revision overrides. This is also the default value for
this parameter.

**PollForSourceChanges**

Required: No

`PollForSourceChanges` controls whether CodePipeline polls the Amazon S3

source bucket for source changes. We recommend that you use CloudWatch Events and CloudTrail
to detect source changes instead. For more information about configuring
CloudWatch Events, see [Migrate polling pipelines with an
S3 source and CloudTrail trail (CLI)](update-change-detection.md#update-change-detection-cli-S3 "update-change-detection.md#update-change-detection-cli-S3") or [Migrate polling pipelines with an
S3 source and CloudTrail trail (CloudFormation template)](update-change-detection.md#update-change-detection-cfn-s3 "update-change-detection.md#update-change-detection-cfn-s3").

###### Important

If you intend to configure CloudWatch Events, you must set
`PollForSourceChanges` to `false` to avoid
duplicate pipeline executions.

Valid values for this parameter:

- `true`: If set, CodePipeline polls your source location for
  source changes.

###### Note

If you omit `PollForSourceChanges`, CodePipeline defaults
to polling your source location for source changes. This
behavior is the same as if `PollForSourceChanges` is
included and set to `true`.

- `false`: If set, CodePipeline does not poll your source
  location for source changes. Use this setting if you intend to
  configure a CloudWatch Events rule to detect source changes.

## Input artifacts

- **Number of Artifacts:**
  `0`
- **Description:** Input artifacts do not apply for
  this action type.

## Output artifacts

- **Number of artifacts:**
  `1`
- **Description:** Provides the artifacts that are
  available in the source bucket configured to connect to the pipeline. The
  artifacts generated from the bucket are the output artifacts for the Amazon S3
  action. The Amazon S3 object metadata (ETag and version ID) is displayed in CodePipeline as

the source revision for the triggered pipeline execution.

## Output variables

When configured, this action produces variables that can be referenced by the action
configuration of a downstream action in the pipeline. This action produces variables
which can be viewed as output variables, even if the action doesn't have a namespace.
You configure an action with a namespace to make those variables available to the
configuration of downstream actions.

For more information about variables in CodePipeline, see [Variables reference](reference-variables.md "reference-variables.md").

**BucketName**

The name of the Amazon S3 bucket related to the source change that triggered
the pipeline.

**ETag**

The entity tag for the object related to the source change that triggered
the pipeline. The ETag is an MD5 hash of the object. ETag reflects only
changes to the contents of an object, not its metadata.

**ObjectKey**

The name of the Amazon S3 object key related to the source change that
triggered the pipeline.

**VersionId**

The version ID for the version of the object related to the source change
that triggered the pipeline.

## Service role permissions: S3 source action

For S3 source action support, add the following to your policy statement:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion",
 "s3:GetBucketVersioning",
 "s3:GetBucketAcl",
 "s3:GetBucketLocation",
 "s3:GetObjectTagging",
 "s3:GetObjectVersionTagging"
 ],
 "Resource": [
 "arn:aws:s3:::[[S3Bucket]]",
 "arn:aws:s3:::[[S3Bucket]]/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:ResourceAccount": "`111122223333`"
 }
 }
 }
 ]
}`

```

## Action declaration

YAML

```
Name: Source
Actions:
  - RunOrder: 1
    OutputArtifacts:
      - Name: SourceArtifact
    ActionTypeId:
      Provider: S3
      Owner: AWS
      Version: '1'
      Category: Source
    Region: us-west-2
    Name: Source
    Configuration:
      S3Bucket: amzn-s3-demo-source-bucket
      S3ObjectKey: my-application.zip
      PollForSourceChanges: 'false'
    InputArtifacts: []

```

JSON

```
{
    "Name": "Source",
    "Actions": [
        {
            "RunOrder": 1,
            "OutputArtifacts": [
                {
                    "Name": "SourceArtifact"
                }
            ],
            "ActionTypeId": {
                "Provider": "S3",
                "Owner": "AWS",
                "Version": "1",
                "Category": "Source"
            },
            "Region": "us-west-2",
            "Name": "Source",
            "Configuration": {
                "S3Bucket": "amzn-s3-demo-source-bucket",
                "S3ObjectKey": "my-application.zip",
                "PollForSourceChanges": "false"
            },
            "InputArtifacts": []
        }
    ]
},
```

## See also

The following related resources can help you as you work with this action.

- [Tutorial: Create a simple pipeline (S3 bucket)](tutorials-simple-s3.md "tutorials-simple-s3.md")
  – This tutorial provides a sample app spec file and sample CodeDeploy
  application and deployment group. Use this tutorial to create a pipeline with an

Amazon S3 source that deploys to Amazon EC2 instances.
