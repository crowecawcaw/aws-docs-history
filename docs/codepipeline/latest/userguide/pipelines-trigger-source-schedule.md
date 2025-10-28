# Start a pipeline on a

schedule

You can set up a rule in EventBridge to start a pipeline on a schedule.

## Create an EventBridge rule that

schedules your pipeline to start (console)

###### To create an EventBridge rule with a schedule as the event source

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**, and then under **Rule
   detail**, choose **Schedule**.
4. Set up the schedule using a fixed rate or expression. For information, see
   [Schedule Expression for Rules](../../../AmazonCloudWatch/latest/events/ScheduledEvents.md "../../../AmazonCloudWatch/latest/events/ScheduledEvents.md").
5. In **Targets**, choose
   **CodePipeline**.
6. Enter the pipeline ARN for the pipeline execution for this
   schedule.

###### Note

You can find the pipeline ARN under **Settings** in
the console. See [View the pipeline ARN and service role ARN
(console)](pipelines-settings-console.md "pipelines-settings-console.md"). 7. Choose one of the following to create or specify an IAM service role that
gives EventBridge permissions to invoke the target associated with your EventBridge rule
(in this case, the target is CodePipeline).

    * Choose **Create a new role for this specific
     resource** to create a service role that grants EventBridge
     permissions to start your pipeline executions.
    * Choose **Use existing role** to enter a service
     role that grants EventBridge permissions to start your pipeline
     executions.

8. Choose **Configure details**.
9. On the **Configure rule details** page, enter a name and
   description for the rule, and then choose **State** to
   enable the rule.
10. If you're satisfied with the rule, choose **Create
    rule**.

## Create an EventBridge rule that

schedules your pipeline to start (CLI)

To use the AWS CLI to create a rule, call the **put-rule** command,
specifying:

- A name that uniquely identifies the rule you are creating. This name must
  be unique across all of the pipelines you create with CodePipeline associated with
  your AWS account.
- The schedule expression for the rule.

###### To create an EventBridge rule with a schedule as the event source

1. Call the **put-rule** command and include the `--name` and `--schedule-expression` parameters.

Examples:

The following sample command uses **--schedule-expression**
to create a rule called `MyRule2` that filters EventBridge on a
schedule.

```
aws events put-rule --schedule-expression 'cron(15 10 ? * 6L 2002-2005)' --name MyRule2
```

2.  To add CodePipeline as a target, call the **put-targets** command
    and include the following parameters:

        * The `--rule` parameter is used with the
         `rule_name` you created by using
         **put-rule**.
        * The `--targets` parameter is used with the list
         `Id` of the target in the list of targets and the
         `ARN` of the target pipeline.

    The following sample command specifies that for the rule called
    `MyCodeCommitRepoRule`, the target `Id` is
    composed of the number one, indicating that in a list of targets for the
    rule, this is target 1. The sample command also specifies an example
    `ARN` for the pipeline. The pipeline starts when something
    changes in the repository.

```
aws events put-targets --rule MyCodeCommitRepoRule --targets Id=1,Arn=arn:aws:codepipeline:us-west-2:80398EXAMPLE:TestPipeline
```

3. Grant permissions for EventBridge to use CodePipeline to invoke the rule. For more
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

   ```
   aws iam create-role --role-name Role-for-MyRule --assume-role-policy-document file://trustpolicyforEB.json
   ```

   3. Create the permissions policy JSON as shown in this sample for the
      pipeline named `MyFirstPipeline`. Name the permissions
      policy `permissionspolicyforEB.json`.

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
   aws iam put-role-policy --role-name Role-for-MyRule --policy-name CodePipeline-Permissions-Policy-For-EB --policy-document file://permissionspolicyforCWE.json
   ```
