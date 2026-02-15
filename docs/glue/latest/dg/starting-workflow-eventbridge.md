# Starting an AWS Glue workflow with an Amazon EventBridge event

Amazon EventBridge, also known as CloudWatch Events, enables you to automate your AWS services and respond
automatically to system events such as application availability issues or resource changes. Events
from AWS services are delivered to EventBridge in near real time. You can write simple rules to
indicate which events are of interest to you, and what automated actions to take when an event
matches a rule.

With EventBridge support, AWS Glue can serve as an event producer and consumer in an event-driven
architecture. For workflows, AWS Glue supports any type of EventBridge event as a consumer. The likely
most common use case is the arrival of a new object in an Amazon S3 bucket. If you have data arriving
in irregular or undefined intervals, you can process this data as close to its arrival as
possible.

###### Note

AWS Glue does not provide guaranteed delivery of EventBridge messages. AWS Glue performs no
deduplication if EventBridge delivers duplicate messages. You must manage idempotency based on your
use case.

Be sure to configure EventBridge rules correctly to avoid sending unwanted events.

###### Before you begin

If you want to start a workflow with Amazon S3 data events, you must ensure that events for the
S3 bucket of interest are logged to AWS CloudTrail and EventBridge. To do so, you must create a CloudTrail trail.
For more information, see [Creating a
trail for your AWS account](../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md "../../../awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.md").

###### To start a workflow with an EventBridge event

###### Note

In the following commands, replace:

- `<workflow-name>` with the name to assign to the
  workflow.
- `<trigger-name>` with the name to assign to the
  trigger.
- `<bucket-name>` with the name of the Amazon S3 bucket.
- `<account-id>` with a valid AWS account ID.
- `<region>` with the name of the Region (for example,
  `us-east-1`).
- `<rule-name>` with the name to assign to the EventBridge
  rule.

1. Ensure that you have AWS Identity and Access Management (IAM) permissions to create and view EventBridge rules and
   targets. The following is a sample policy that you can attach. You might want to scope it down
   to put limits on the operations and resources.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "events:PutRule",
 "events:DisableRule",
 "events:DeleteRule",
 "events:PutTargets",
 "events:RemoveTargets",
 "events:EnableRule",
 "events:List*",
 "events:Describe*"
 ],
 "Resource": "*"
 }
 ]
}`

```

2. Create an IAM role that the EventBridge service can assume when passing an event to
   AWS Glue.
   1. On the **Create role** page of the IAM console, choose **AWS
      Service**. Then choose the service **CloudWatch Events**.
   2. Complete the **Create role** wizard. The wizard automatically attaches
      the `CloudWatchEventsBuiltInTargetExecutionAccess` and
      `CloudWatchEventsInvocationAccess` policies.
   3. Attach the following inline policy to the role. This policy allows the EventBridge service
      to direct events to AWS Glue.

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Effect": "Allow",
    "Action": [
    "glue:notifyEvent"
    ],
    "Resource": [
    "arn:aws:glue:`us-east-1`:`111122223333`:workflow/`workflow-name`"
    ]
    }
    ]
   }`

   ```

3. Enter the following command to create the workflow.

See [create-workflow](../../../cli/latest/reference/glue/create-workflow.md "../../../cli/latest/reference/glue/create-workflow.md") in the _AWS CLI Command Reference_ for
information about additional optional command-line parameters.

```
aws glue create-workflow --name `<workflow-name>`
```

4. Enter the following command to create an EventBridge event trigger for the workflow. This will be
   the start trigger for the workflow. Replace `<actions>` with the
   actions to perform (the jobs and crawlers to start).

See [create-trigger](../../../cli/latest/reference/glue/create-trigger.md "../../../cli/latest/reference/glue/create-trigger.md") in the _AWS CLI Command Reference_ for
information about how to code the `actions` argument.

```
aws glue create-trigger --workflow-name `<workflow-name>` --type EVENT --name `<trigger-name>` --actions `<actions>`
```

If you want the workflow to be triggered by a batch of events instead of a single EventBridge
event, enter the following command instead.

```
aws glue create-trigger --workflow-name `<workflow-name>` --type EVENT --name `<trigger-name>` --event-batching-condition BatchSize=`<number-of-events>`,BatchWindow=`<seconds>` --actions `<actions>`
```

For the `event-batching-condition` argument, `BatchSize` is
required and `BatchWindow` is optional. If `BatchWindow` is omitted,
the window defaults to 900 seconds, which is the maximum window size.

###### Example

The following example creates a trigger that starts the `eventtest`
workflow after three EventBridge events have arrived, or five minutes after the first event
arrives, whichever comes first.

```
aws glue create-trigger --workflow-name eventtest --type EVENT --name objectArrival --event-batching-condition BatchSize=3,BatchWindow=300 --actions JobName=test1

```

5. Create a rule in Amazon EventBridge.
   1. Create the JSON object for the rule details in your preferred text editor.

   The following example specifies Amazon S3 as the event source, `PutObject` as
   the event name, and the bucket name as a request parameter. This rule starts a workflow
   when a new object arrives in the bucket.

   ```
   {
     "source": [
       "aws.s3"
     ],
     "detail-type": [
       "AWS API Call via CloudTrail"
     ],
     "detail": {
       "eventSource": [
         "s3.amazonaws.com"
       ],
       "eventName": [
         "PutObject"
       ],
       "requestParameters": {
         "bucketName": [
           "`<bucket-name>`"
         ]
       }
     }
   }
   ```

   To start the workflow when a new object arrives in a folder within the bucket, you
   can substitute the following code for `requestParameters`.

   ```
       "requestParameters": {
         "bucketName": [
           "`<bucket-name>`"
         ]
         "key" : [{ "prefix" : "`<folder1>`/`<folder2>`/*"}}]
     }
   ```

   2. Use your preferred tool to convert the rule JSON object to an escaped string.

   ```
   {\n  \"source\": [\n    \"aws.s3\"\n  ],\n  \"detail-type\": [\n    \"AWS API Call via CloudTrail\"\n  ],\n  \"detail\": {\n    \"eventSource\": [\n      \"s3.amazonaws.com\"\n    ],\n    \"eventName\": [\n      \"PutObject\"\n    ],\n    \"requestParameters\": {\n      \"bucketName\": [\n        \"`<bucket-name>`\"\n      ]\n    }\n  }\n}
   ```

   3. Run the following command to create a JSON parameter template that you can edit to
      specify input parameters to a subsequent `put-rule` command. Save the output in a
      file. In this example, the file is called `ruleCommand`.

   ```
   aws events put-rule --name `<rule-name>` --generate-cli-skeleton >ruleCommand
   ```

   For more information about the `--generate-cli-skeleton` parameter, see [Generating AWS CLI
   skeleton and input parameters from a JSON or YAML input file](../../../cli/latest/userguide/cli-usage-skeleton.md "../../../cli/latest/userguide/cli-usage-skeleton.md") in the _AWS Command Line Interface User Guide_.

   The output file should look like the following.

   ```
   {
       "Name": "",
       "ScheduleExpression": "",
       "EventPattern": "",
       "State": "ENABLED",
       "Description": "",
       "RoleArn": "",
       "Tags": [
           {
               "Key": "",
               "Value": ""
           }
       ],
       "EventBusName": ""
   }
   ```

   4. Edit the file to optionally remove parameters and to specify at a minimum the
      `Name`, `EventPattern`, and `State` parameters. For the
      `EventPattern` parameter, provide the escaped string for the rule details that you
      created in a previous step.

   ```
   {
       "Name": "`<rule-name>`",
       "EventPattern": "{\n  \"source\": [\n    \"aws.s3\"\n  ],\n  \"detail-type\": [\n    \"AWS API Call via CloudTrail\"\n  ],\n  \"detail\": {\n    \"eventSource\": [\n      \"s3.amazonaws.com\"\n    ],\n    \"eventName\": [\n      \"PutObject\"\n    ],\n    \"requestParameters\": {\n      \"bucketName\": [\n        \"`<bucket-name>`\"\n      ]\n    }\n  }\n}",
       "State": "DISABLED",
       "Description": "Start an AWS Glue workflow upon new file arrival in an Amazon S3 bucket"
   }

   ```

   ###### Note

   It is best to leave the rule disabled until you finish building out the workflow. 5. Enter the following `put-rule` command, which reads input parameters from the
   file `ruleCommand`.

   ```
   aws events put-rule --name `<rule-name>` --cli-input-json file://ruleCommand
   ```

   The following output indicates success.

   ```
   {
       "RuleArn": "<rule-arn>"
   }

   ```

6. Enter the following command to attach the rule to a target. The target is the workflow in
   AWS Glue. Replace `<role-name>` with the role that you created at the
   beginning of this procedure.

```
aws events put-targets --rule `<rule-name>` --targets "Id"="1","Arn"="arn:aws:glue:`<region>`:`<account-id>`:workflow/`<workflow-name>`","RoleArn"="arn:aws:iam::`<account-id>`:role/`<role-name>`" --region `<region>`
```

The following output indicates success.

```
{
    "FailedEntryCount": 0,
    "FailedEntries": []
}
```

7. Confirm successful connection of the rule and target by entering the following
   command.

```
aws events list-rule-names-by-target --target-arn arn:aws:glue:`<region>`:`<account-id>`:workflow/`<workflow-name>`
```

The following output indicates success, where `<rule-name>` is
the name of the rule that you created.

```
{
    "RuleNames": [
        "<rule-name>"
    ]
}

```

8. Sign in to the AWS Management Console and open the AWS Glue console at
   [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/").
9. Select the workflow, and verify that the start trigger and its actions—the jobs or
   crawlers that it starts— appear on the workflow graph. Then continue with the
   procedure in [Step 3: Add more triggers](creating_running_workflows.md#workflow-step3 "creating_running_workflows.md#workflow-step3"). Or add more
   components to the workflow by using the AWS Glue API or AWS Command Line Interface.
10. When the workflow is completely specified, enable the rule.

```
aws events enable-rule --name `<rule-name>`
```

The workflow is now ready to be started by an EventBridge event or event batch.

###### See also

- [_Amazon EventBridge User Guide_](../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md "../../../eventbridge/latest/userguide/what-is-amazon-eventbridge.md")
- [Overview of workflows in AWS Glue](workflows_overview.md "workflows_overview.md")
- [Creating and building out a workflow manually
  in AWS Glue](creating_running_workflows.md "creating_running_workflows.md")
