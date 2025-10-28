# Create an EventBridge rule for an Amazon ECR source

(CLI)

Call the **put-rule** command, specifying:

- A name that uniquely identifies the rule you are creating. This name must
  be unique across all of the pipelines you create with CodePipeline associated with
  your AWS account.
- The event pattern for the source and detail fields used by the rule. For
  more information, see [Amazon EventBridge and Event Patterns](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md").

###### To create an EventBridge rule with Amazon ECR as the event source and CodePipeline as the

target

1. Add permissions for EventBridge to use CodePipeline to invoke the rule. For more
   information, see [Using resource-based policies for Amazon EventBridge](../../../eventbridge/latest/userguide/eb-use-resource-based.md "../../../eventbridge/latest/userguide/eb-use-resource-based.md").
   1. Use the following sample to create the trust policy that allows
      EventBridge to assume the service role. Name the trust policy
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

   ```
   aws iam create-role --role-name Role-for-MyRule --assume-role-policy-document file://trustpolicyforEB.json
   ```

   3. Create the permissions policy JSON, as shown in this sample, for
      the pipeline named `MyFirstPipeline`. Name the
      permissions policy
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

   4. Use the following command to attach the
      `CodePipeline-Permissions-Policy-for-EB` permissions
      policy to the `Role-for-MyRule` role.

   **Why am I making this change?**
   Adding this policy to the role creates permissions for EventBridge.

   ```
   aws iam put-role-policy --role-name Role-for-MyRule --policy-name CodePipeline-Permissions-Policy-For-EB --policy-document file://permissionspolicyforEB.json
   ```

2. Call the **put-rule** command and include the
   `--name`, `--event-pattern`, and
   `--role-arn` parameters.

**Why am I making this change?** You must
create an event with a rule that specifies how an image push must be made,
and a target that names the pipeline to be started by the event.

The following sample command creates a rule called
`MyECRRepoRule`.

```
aws events put-rule --name "MyECRRepoRule" --event-pattern "{\"detail-type\":[\"ECR Image Action\"],\"source\":[\"aws.ecr\"],\"detail\":{\"action-type\":[\"PUSH\"],\"image-tag\":[\"latest\"],\"repository-name\":[\"eb-test\"],\"result\":[\"SUCCESS\"]}}}" --role-arn "arn:aws:iam::`ACCOUNT_ID`:role/Role-for-MyRule"
```

###### Note

To view the full event pattern supported for Amazon ECR events, see [Amazon ECR Events and
EventBridge](../../../AmazonECR/latest/userguide/ecr-eventbridge.md "../../../AmazonECR/latest/userguide/ecr-eventbridge.md") or [Amazon Elastic Container Registry
Events](../../../eventbridge/latest/userguide/event-types.md#ecr-event-types "../../../eventbridge/latest/userguide/event-types.md#ecr-event-types"). 3. To add CodePipeline as a target, call the **put-targets** command
and include the following parameters:

    * The `--rule` parameter is used with the
     `rule_name` you created by using
     **put-rule**.
    * The `--targets` parameter is used with the list
     `Id` of the target in the list of targets and the
     `ARN` of the target pipeline.

The following sample command specifies that for the rule called
`MyECRRepoRule`, the target `Id` is composed of
the number one, indicating that in a list of targets for the rule, this is
target 1. The sample command also specifies an example `Arn` for
the pipeline and the example `RoleArn` for the rule. The pipeline
starts when something changes in the repository.

```
aws events put-targets --rule MyECRRepoRule --targets Id=1,Arn=arn:aws:codepipeline:us-west-2:80398EXAMPLE:TestPipeline,RoleArn=arn:aws:iam::80398EXAMPLE:role/Role-for-MyRule
```

4. (Optional) To configure an input transformer with source overrides for a
   specific image ID, use the following JSON in your CLI command. The following
   example configures an override where:
   - The `actionName`, `Source` in this example,
     is the dynamic value, defined at pipeline creation, not derived from
     the source event.
   - The `revisionType`, `IMAGE_DIGEST` in this
     example, is the dynamic value, defined at pipeline creation, not
     derived from the source event.
   - The `revisionValue`,
     <`revisionValue`> in this example,
     is derived from the source event variable.

```
{
    "Rule": "my-rule",
    "Targets": [
        {
            "Id": "MyTargetId",
            "Arn": "ARN",
            "InputTransformer": {
                "InputPathsMap": {
                    "revisionValue": "$.detail.image-digest"
                },
                "InputTemplate": {
                    "sourceRevisions": [
                        {
                            "actionName": "`Source`",
                            "revisionType": "`IMAGE_DIGEST`",
                            "revisionValue": "<`revisionValue`>"
                        }
                    ]
                }
            }
        }
    ]
}

```
