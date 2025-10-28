# Create pipelines with an S3 source

enabled for events (CLI)

Follow these steps to create a pipeline with an S3 source that uses an event in
EventBridge for change detection. For the full steps to create a pipeline with the CLI, see
[Create a pipeline, stages, and actions](pipelines-create.md "pipelines-create.md").

To build an event-driven pipeline with Amazon S3, you edit the
`PollForSourceChanges` parameter of your pipeline and then create the
following resources:

- EventBridge event rule
- IAM role to allow the EventBridge event to start your pipeline

###### To create an EventBridge rule with Amazon S3 as the event source and CodePipeline as the target

and apply the permissions policy

1. Grant permissions for EventBridge to use CodePipeline to invoke the rule. For more
   information, see [Using resource-based policies for Amazon EventBridge](../../../eventbridge/latest/userguide/eb-use-resource-based.md "../../../eventbridge/latest/userguide/eb-use-resource-based.md").
   1. Use the following sample to create the trust policy to allow EventBridge
      to assume the service role. Name it
      `trustpolicyforEB.json`.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Principal": {
    "Service": "events.amazonaws.com"
    },
    "Action": "sts:AssumeRole"
    }
    ]
   }`

   ```

   2. Use the following command to create the
      `Role-for-MyRule` role and attach the trust
      policy.

   **Why am I making this change?**
   Adding this trust policy to the role creates permissions for
   EventBridge.

   ```
   aws iam create-role --role-name Role-for-MyRule --assume-role-policy-document file://trustpolicyforEB.json
   ```

   3. Create the permissions policy JSON, as shown here for the pipeline
      named `MyFirstPipeline`. Name the permissions policy
      `permissionspolicyforEB.json`.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [
    "codepipeline:StartPipelineExecution"
    ],
    "Resource": [
    "arn:aws:codepipeline:us-west-2:`111122223333`:MyFirstPipeline"
    ]
    }
    ]
   }`

   ```

   4. Use the following command to attach the new
      `CodePipeline-Permissions-Policy-for-EB` permissions
      policy to the `Role-for-MyRule` role you created.

   ```
   aws iam put-role-policy --role-name Role-for-MyRule --policy-name CodePipeline-Permissions-Policy-For-EB --policy-document file://permissionspolicyforEB.json
   ```

2. Call the **put-rule** command and include the
   `--name`, `--event-pattern`, and
   `--role-arn` parameters.

The following sample command creates a rule named
`EnabledS3SourceRule`.

```
aws events put-rule --name "EnabledS3SourceRule" --event-pattern "{\"source\":[\"aws.s3\"],\"detail-type\":[\"Object Created\"],\"detail\":{\"bucket\":{\"name\":[\"amzn-s3-demo-source-bucket\"]}}}" --role-arn "arn:aws:iam::`ACCOUNT_ID`:role/Role-for-MyRule"
```

3. To add CodePipeline as a target, call the **put-targets** command
   and include the `--rule` and `--targets`
   parameters.

The following command specifies that for the rule named
`EnabledS3SourceRule`, the target `Id` is
composed of the number one, indicating that in a list of targets for the
rule, this is target 1. The command also specifies an example
`ARN` for the pipeline. The pipeline starts when something
changes in the repository.

```
aws events put-targets --rule EnabledS3SourceRule --targets Id=codepipeline-AppPipeline,Arn=arn:aws:codepipeline:us-west-2:80398EXAMPLE:TestPipeline
```

###### To edit your pipeline's PollForSourceChanges

parameter

###### Important

When you create a pipeline with this method, the `PollForSourceChanges`
parameter defaults to true if it is not explicitly set to false. When you add
event-based change detection, you must add the parameter to your output and set it to
false to disable polling. Otherwise, your pipeline starts twice for a single source
change. For details, see [Valid settings for the
PollForSourceChanges parameter](PollForSourceChanges-defaults.md "PollForSourceChanges-defaults.md").

1. Run the **get-pipeline** command to copy the pipeline structure into a
   JSON file. For example, for a pipeline named
   `MyFirstPipeline`, run the following command:

```
aws codepipeline get-pipeline --name `MyFirstPipeline` >`pipeline.json`
```

This command returns nothing, but the file you created should appear in the directory
where you ran the command. 2. Open the JSON file in any plain-text editor and edit the source stage by changing the
`PollForSourceChanges` parameter for a bucket named
`amzn-s3-demo-source-bucket` to `false`, as shown in this
example.

**Why am I making this change?** Setting this parameter
to `false` turns off periodic checks so you can use event-based change
detection only.

```
"configuration": {
    "S3Bucket": "amzn-s3-demo-source-bucket",
    `"PollForSourceChanges": "*false*",`
    "S3ObjectKey": "index.zip"
},
```

3. If you are working with the pipeline structure retrieved using the
   **get-pipeline** command, you must remove the `metadata`
   lines from the JSON file. Otherwise, the **update-pipeline** command
   cannot use it. Remove the `"metadata": { }` lines and the
   `"created"`, `"pipelineARN"`, and `"updated"`
   fields.

For example, remove the following lines from the structure:

```
"metadata": {
    "pipelineArn": "arn:aws:codepipeline:`region`:`account-ID`:`pipeline-name`",
    "created": "`date`",
    "updated": "`date`"
},
```

Save the file. 4. To apply your changes, run the **update-pipeline** command, specifying
the pipeline JSON file:

###### Important

Be sure to include `file://` before the file name. It is required in this command.

```
aws codepipeline update-pipeline --cli-input-json file://`pipeline.json`
```

This command returns the entire structure of the edited pipeline.

###### Note

The **update-pipeline** command stops the pipeline. If a revision
is being run through the pipeline when you run the
**update-pipeline** command, that run is stopped. You must
manually start the pipeline to run that revision through the updated pipeline. Use
the **start-pipeline-execution** command to manually start your
pipeline.
